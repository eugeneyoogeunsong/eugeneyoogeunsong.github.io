# frozen_string_literal: true

# Make DARK the default theme for visitors who have never chosen one.
# =============================================================================
#
# Why a plugin rather than an edit
# --------------------------------
# The decision lives in one function in the gem-owned assets/js/theme.js:
#
#     let determineThemeSetting = () => {
#       let themeSetting = localStorage.getItem("theme");
#       if (themeSetting != "dark" && themeSetting != "light" && themeSetting != "system") {
#         themeSetting = "system";        // <- the default
#       }
#       return themeSetting;
#     };
#
# There is no config key for it. The obvious fixes both cost more than they
# should:
#
#   * shadowing assets/js/theme.js forks 24 KB of live behaviour to change one
#     word, and every al-folio upgrade then needs that fork re-audited;
#   * shadowing _includes/head.liquid forks the page shell (meta, preloads,
#     config-driven tags) for the same one word.
#
# So instead this injects four lines that REPLACE that one function at runtime,
# immediately after theme.js is loaded and before the inline initTheme() call
# that ends the head. Nothing gem-owned is copied into this repo.
#
# Why the placement matters
# -------------------------
# The built head ends like this:
#
#     <script src="/assets/js/theme.js?v=..."></script>
#     <link ... id="highlight_theme_dark">
#     <script> initTheme(); </script>
#     </head>
#
# theme.js only DEFINES functions; initTheme() is what reads the setting and
# paints. Injecting between the two means the override is in place before the
# first paint, so there is no flash of light theme. Doing this any later (in
# the footer, on DOMContentLoaded) would render light and then flip, which
# looks broken.
#
# What this does and does not reach
# ---------------------------------
# It overrides the FALLBACK only: a stored choice still wins, so anyone who has
# used the toggle keeps what they picked.
#
# Two consequences worth knowing, both inherited from stock theme.js rather
# than introduced here:
#
#   1. initTheme() calls setThemeSetting(), which ALWAYS persists to
#      localStorage. So a first-time visitor gets "dark" written on first load.
#      Delete this file later and those browsers stay dark, because by then
#      they hold a stored value.
#   2. For the same reason, anyone who has ALREADY loaded the site is holding
#      a stored "system" that stock theme.js wrote for them, and they keep
#      following their OS setting. This only changes what genuinely new
#      browsers see. To reset your own: run
#      localStorage.removeItem("theme") in the console and reload.
#
# Forcing dark on those returning visitors would mean overriding a stored
# value, and nothing distinguishes "system because they chose it" from "system
# because it was written automatically" - so that is deliberately not done.
#
# Failure mode
# ------------
# If an upgrade renames theme.js or restructures the head, the pattern stops
# matching. Rather than silently reverting the site to the system default, the
# build FAILS with the message below, so it cannot go unnoticed.

module DefaultThemeDark
  SCRIPT_TAG = %r{(<script[^>]*\ssrc="[^"]*assets/js/theme\.js[^"]*"[^>]*>\s*</script>)}

  # Below this viewport width the default stays "system" (follow the OS) rather
  # than becoming "dark". 767px is the site's own breakpoint: it is where the
  # layout stops floating the portrait and stacks, so "phone" means the same
  # thing here as it does in the stylesheets.
  MOBILE_QUERY = "(max-width: 767px)"

  SNIPPET = <<~HTML.gsub(/\n\s*/, " ").strip
    <script>
      try {
        /* Touch it first: if an upgrade removed this function, the read throws
           and the catch leaves stock behaviour intact rather than half-applying. */
        determineThemeSetting;
        determineThemeSetting = function () {
          var t = localStorage.getItem("theme");
          if (t === "dark" || t === "light" || t === "system") return t;
          try { if (window.matchMedia("#{MOBILE_QUERY}").matches) return "system"; } catch (e) {}
          return "dark";
        };
      } catch (e) {}
    </script>
  HTML

  @injections = 0

  class << self
    attr_accessor :injections
  end
end

Jekyll::Hooks.register %i[pages documents], :post_render do |item|
  next unless item.output_ext == ".html"
  next unless item.output&.match?(DefaultThemeDark::SCRIPT_TAG)

  item.output = item.output.sub(DefaultThemeDark::SCRIPT_TAG) { "#{Regexp.last_match(1)} #{DefaultThemeDark::SNIPPET}" }
  DefaultThemeDark.injections += 1
end

Jekyll::Hooks.register :site, :post_write do |_site|
  next if DefaultThemeDark.injections.positive?

  raise "_plugins/default_theme_dark.rb matched no pages: the theme.js script tag in <head> has changed shape. " \
        "Fix the pattern in that file, or delete it to go back to the system default."
end
