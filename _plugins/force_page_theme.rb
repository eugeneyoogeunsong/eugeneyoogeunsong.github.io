# frozen_string_literal: true

# Lock a single page to one theme, whatever the visitor's setting is.
# =============================================================================
#
# Usage: put this in the page's front matter.
#
#     force_theme: dark        # or: light
#
# Why it exists
# -------------
# /pictures/ is a gallery of studio headshots shot against dark backdrops. They
# read as intended on a dark page and look like cut-outs pasted onto paper on a
# light one. That is a property of the content, not a visitor preference, so the
# page pins itself rather than following the toggle.
#
# How it works, and why not just set the attribute
# ------------------------------------------------
# theme.js separates two things:
#
#     determineThemeSetting()   -> "dark" | "light" | "system"   (what you chose)
#     determineComputedTheme()  -> "dark" | "light"              (what gets painted)
#
# This overrides the SECOND one only, immediately after theme.js loads and
# before the inline initTheme() that ends the head - the same injection point
# _plugins/default_theme_dark.rb uses, and for the same reason: any later and
# the page paints once in the wrong theme and visibly flips.
#
# Overriding the computed theme rather than just stamping data-theme="dark" on
# <html> matters because applyTheme() does more than set that attribute: it also
# retargets the syntax-highlight stylesheet, the search overlay, Giscus, Mermaid
# and the calendar iframe. Setting the attribute by hand would leave all of those
# on the visitor's theme, so opening search (Cmd+K) here would flash a light
# panel over a dark page.
#
# It deliberately does NOT touch localStorage, so the visitor's real preference
# survives untouched and every other page still honours it.
#
# The toggle button is hidden on a pinned page (see the CSS in the page itself).
# Leaving it visible would mean shipping a control that appears broken: it would
# still record the visitor's choice, but nothing on screen would change.
#
# Failure mode: if an upgrade renames theme.js or that function, the pattern
# stops matching and the build FAILS rather than quietly unpinning the page.

module ForcePageTheme
  SCRIPT_TAG = %r{(<script[^>]*\ssrc="[^"]*assets/js/theme\.js[^"]*"[^>]*>\s*</script>)}
  ALLOWED = %w[dark light].freeze

  @wanted = 0
  @injected = 0

  class << self
    attr_accessor :wanted, :injected

    def snippet(theme)
      <<~HTML.gsub(/\n\s*/, " ").strip
        <script>
          try {
            determineComputedTheme;
            determineComputedTheme = function () { return "#{theme}"; };
          } catch (e) {}
        </script>
      HTML
    end
  end
end

Jekyll::Hooks.register %i[pages documents], :post_render do |item|
  theme = item.data["force_theme"]
  next if theme.nil?

  unless ForcePageTheme::ALLOWED.include?(theme)
    raise "force_theme: #{theme.inspect} in #{item.relative_path} is not one of #{ForcePageTheme::ALLOWED.join(', ')}"
  end

  ForcePageTheme.wanted += 1
  next unless item.output&.match?(ForcePageTheme::SCRIPT_TAG)

  item.output = item.output.sub(ForcePageTheme::SCRIPT_TAG) { "#{Regexp.last_match(1)} #{ForcePageTheme.snippet(theme)}" }
  ForcePageTheme.injected += 1
end

Jekyll::Hooks.register :site, :post_write do |_site|
  next if ForcePageTheme.injected == ForcePageTheme.wanted

  raise "_plugins/force_page_theme.rb: #{ForcePageTheme.wanted} page(s) asked for a pinned theme but only " \
        "#{ForcePageTheme.injected} could be pinned - the theme.js script tag in <head> has changed shape. " \
        "Fix the pattern in that file."
end
