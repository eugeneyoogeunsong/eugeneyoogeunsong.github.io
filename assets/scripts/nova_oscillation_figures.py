#!/usr/bin/env python3
"""Generate the two oscillation figures on /projects/2_nova/.

Everything here is computed from scratch - a full three-flavour propagation
through constant-density matter - so the figures are original work and carry no
licensing question, unlike lifting a collaboration plot out of a talk.

Physics
-------
The Hamiltonian in the flavour basis:

    M = U diag(0, dm21, dm31) U^dagger + diag(A, 0, 0)     [eV^2]
    P(a -> b) = | < b | exp(-i * 2.534 * M * L / E) | a > |^2

The constant is 2 x 1.267, not 1.267. The familiar textbook phase is
dm2 L / (4E) = 1.267 * dm2[eV^2] * L[km] / E[GeV], but that is the phase
DIFFERENCE that appears inside sin^2(); the evolution operator exp(-i H L)
with H = M / (2E) carries dm2 L / (2E), which is twice it. Getting this wrong
halves every phase and so doubles the apparent energy scale - the appearance
peak lands near 0.8 GeV instead of 1.6 GeV, which is the symptom to look for.

A = 2 E V is the matter term written as an effective mass-squared, with
V = sqrt(2) G_F n_e = 7.56e-14 * Y_e * rho[g/cm^3] eV. For antineutrinos both
U -> U* and A -> -A, which is the whole reason a long baseline can separate the
mass ordering from delta_CP: the matter sign flips with the ordering, the
delta_CP sign flips with the beam, and only a baseline long enough for matter to
matter can tell the two apart. At 810 km and 2 GeV the matter effect is ~19%,
against ~9% for T2K at 295 km.

Oscillation parameters are NOvA's ten-year values where NOvA measures them
(Phys. Rev. Lett. 136, 011802, 2026) and the solar/reactor values elsewhere.

Outputs a light and a dark variant of each figure; the page swaps them with the
.only-light / .only-dark classes so the plots follow the theme toggle.

Run:  python3 assets/scripts/nova_oscillation_figures.py
"""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------- parameters

S12_SQ = 0.307  # solar angle, global fits
S13_SQ = 0.022  # reactor angle; Daya Bay sin^2(2th13) = 0.0851 +- 0.0024
S23_SQ = 0.55  # NOvA 2026: sin^2(th23) = 0.55 +0.02 -0.06
DM21 = 7.53e-5  # eV^2, solar splitting
DM32_NO = 2.431e-3  # eV^2, NOvA 2026, normal ordering
DM32_IO = -2.479e-3  # eV^2, NOvA 2026, inverted ordering

BASELINE_KM = 810.0  # Fermilab -> Ash River
PEAK_GEV = 2.0  # off-axis flux peak, 14.6 mrad
RHO = 2.84  # g/cm^3, average crustal density on the NOvA chord
Y_E = 0.5  # electrons per nucleon

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "img", "projects"))


def pmns(delta_cp):
    """The PMNS matrix in the standard parameterisation."""
    s12, s13, s23 = np.sqrt([S12_SQ, S13_SQ, S23_SQ])
    c12, c13, c23 = np.sqrt(1 - np.array([S12_SQ, S13_SQ, S23_SQ]))
    e = np.exp(-1j * delta_cp)
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * e],
            [
                -s12 * c23 - c12 * s23 * s13 / e,
                c12 * c23 - s12 * s23 * s13 / e,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 / e,
                -c12 * s23 - s12 * c23 * s13 / e,
                c23 * c13,
            ],
        ]
    )


def probability(alpha, beta, energies, delta_cp, dm32, anti=False):
    """P(nu_alpha -> nu_beta) through constant-density matter.

    alpha, beta are 0, 1, 2 for e, mu, tau.
    """
    energies = np.atleast_1d(np.asarray(energies, dtype=float))
    dm31 = dm32 + DM21
    u = pmns(delta_cp)
    if anti:
        u = np.conjugate(u)
    mass = u @ np.diag([0.0, DM21, dm31]) @ u.conj().T

    v_ev = 7.56e-14 * Y_E * RHO  # sqrt(2) G_F n_e, in eV
    out = np.empty_like(energies)
    for k, e_gev in enumerate(energies):
        a = 2.0 * e_gev * 1e9 * v_ev  # effective mass-squared, eV^2
        if anti:
            a = -a
        h = mass + np.diag([a, 0.0, 0.0])
        evals, evecs = np.linalg.eigh(h)
        phase = np.exp(-1j * 2.534 * evals * BASELINE_KM / e_gev)
        s = evecs @ np.diag(phase) @ evecs.conj().T
        out[k] = np.abs(s[beta, alpha]) ** 2
    return out


# ------------------------------------------------------------------ plotting

THEMES = {
    "light": dict(
        fg="#14141a",
        muted="#6b6b7b",
        grid="#d9d9e3",
        no="#4338ca",
        io="#b45309",
        band="#4338ca",
        face="#ffffff",
    ),
    "dark": dict(
        fg="#e4e4ef",
        muted="#9a9aae",
        grid="#34344a",
        no="#a5b4fc",
        io="#fbbf24",
        band="#a5b4fc",
        face="#14141a",
    ),
}


def style(theme):
    c = THEMES[theme]
    plt.rcParams.update(
        {
            "figure.facecolor": c["face"],
            "axes.facecolor": c["face"],
            "savefig.facecolor": c["face"],
            "text.color": c["fg"],
            "axes.labelcolor": c["fg"],
            "axes.edgecolor": c["muted"],
            "xtick.color": c["muted"],
            "ytick.color": c["muted"],
            "grid.color": c["grid"],
            "font.size": 11,
            "axes.titlesize": 12,
            "legend.frameon": False,
            "figure.dpi": 200,
        }
    )
    return c


def figure_spectrum(theme):
    """P(nu_mu -> nu_e) against energy, both orderings, both beam modes."""
    c = style(theme)
    energies = np.linspace(0.6, 5.0, 400)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.9), sharey=True)

    for ax, anti, title in zip(
        axes,
        [False, True],
        [r"neutrino beam:  $\nu_\mu \to \nu_e$", r"antineutrino beam:  $\bar\nu_\mu \to \bar\nu_e$"],
    ):
        for dm32, colour, label in [
            (DM32_NO, c["no"], "normal ordering"),
            (DM32_IO, c["io"], "inverted ordering"),
        ]:
            lo = probability(1, 0, energies, 0.0, dm32, anti)
            hi = probability(1, 0, energies, 0.0, dm32, anti)
            for d in np.linspace(0, 2 * np.pi, 49):
                p = probability(1, 0, energies, d, dm32, anti)
                lo = np.minimum(lo, p)
                hi = np.maximum(hi, p)
            ax.fill_between(energies, lo, hi, color=colour, alpha=0.22, lw=0)
            ax.plot(
                energies,
                probability(1, 0, energies, np.pi / 2, dm32, anti),
                color=colour,
                lw=1.9,
                label=label,
            )
        ax.axvline(PEAK_GEV, color=c["muted"], lw=0.9, ls=(0, (4, 3)))
        ax.set_title(title, color=c["fg"])
        ax.set_xlabel("neutrino energy  [GeV]")
        ax.grid(True, lw=0.5, alpha=0.6)
        ax.set_xlim(0.6, 5.0)
        ax.set_ylim(0, 0.092)

    axes[0].set_ylabel(r"appearance probability")
    axes[0].annotate(
        "flux peak,\n14.6 mrad off-axis",
        xy=(PEAK_GEV, 0.070),
        xytext=(2.65, 0.078),
        color=c["muted"],
        fontsize=8.5,
        arrowprops=dict(arrowstyle="-", color=c["muted"], lw=0.8),
    )
    axes[1].legend(loc="upper right", fontsize=9.5)
    fig.text(
        0.5,
        -0.04,
        r"Solid: $\delta_{CP}=\pi/2$.  Bands: the full range as $\delta_{CP}$ runs over $[0,2\pi)$."
        "\n"
        r"$L=810$ km through rock. The two orderings separate because matter changes sign with the ordering"
        "\n"
        r"and $\delta_{CP}$ changes sign with the beam - but the bands overlap, which is the degeneracy.",
        ha="center",
        va="top",
        color=c["muted"],
        fontsize=8.5,
    )
    fig.tight_layout()
    path = os.path.join(OUT, f"nova-appearance-{theme}.png")
    fig.savefig(path, bbox_inches="tight", pad_inches=0.28)
    plt.close(fig)
    return path


def figure_biprobability(theme):
    """The bi-probability ellipses at the flux peak."""
    c = style(theme)
    fig, ax = plt.subplots(figsize=(5.4, 5.0))

    deltas = np.linspace(0, 2 * np.pi, 361)
    for dm32, colour, label in [
        (DM32_NO, c["no"], "normal ordering"),
        (DM32_IO, c["io"], "inverted ordering"),
    ]:
        x = np.array([probability(1, 0, PEAK_GEV, d, dm32, False)[0] for d in deltas])
        y = np.array([probability(1, 0, PEAK_GEV, d, dm32, True)[0] for d in deltas])
        ax.plot(x, y, color=colour, lw=2.0, label=label)
        for d, marker, note in [
            (0.0, "o", r"$0$"),
            (np.pi / 2, "s", r"$\pi/2$"),
            (np.pi, "^", r"$\pi$"),
            (3 * np.pi / 2, "D", r"$3\pi/2$"),
        ]:
            px = probability(1, 0, PEAK_GEV, d, dm32, False)[0]
            py = probability(1, 0, PEAK_GEV, d, dm32, True)[0]
            ax.plot(px, py, marker, color=colour, ms=5.5)
            ax.annotate(
                note,
                xy=(px, py),
                xytext=(5, 4),
                textcoords="offset points",
                color=colour,
                fontsize=8.5,
            )

    ax.set_xlim(0.018, 0.072)
    ax.set_ylim(0.018, 0.072)
    ax.set_aspect("equal")
    diag = np.linspace(0.018, 0.072, 10)
    ax.plot(diag, diag, color=c["muted"], lw=0.8, ls=(0, (4, 3)), zorder=0)
    ax.annotate(
        "equal rates: no CP asymmetry",
        xy=(0.0235, 0.0235),
        xytext=(4, 4),
        textcoords="offset points",
        rotation=45,
        rotation_mode="anchor",
        color=c["muted"],
        fontsize=8.5,
        ha="left",
        va="bottom",
    )
    ax.annotate(
        "the loops all but touch here:\nrates alone cannot choose",
        xy=(0.0432, 0.0424),
        xytext=(0.0355, 0.0225),
        color=c["muted"],
        fontsize=8.5,
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="->", color=c["muted"], lw=0.8),
    )

    ax.set_xlabel(r"$P(\nu_\mu \to \nu_e)$  at 2 GeV")
    ax.set_ylabel(r"$P(\bar\nu_\mu \to \bar\nu_e)$  at 2 GeV")
    ax.grid(True, lw=0.5, alpha=0.6)
    ax.legend(loc="upper left", fontsize=9.5)
    fig.text(
        0.5,
        -0.02,
        r"Each loop is one mass ordering; going round it is $\delta_{CP}$ running from 0 to $2\pi$."
        "\n"
        r"The two far corners - (NO, $3\pi/2$) bottom right and (IO, $\pi/2$) top left - are the"
        "\n"
        "combinations NOvA's data disfavour, precisely because nothing else lands there.",
        ha="center",
        va="top",
        color=c["muted"],
        fontsize=8.5,
    )
    fig.tight_layout()
    path = os.path.join(OUT, f"nova-biprobability-{theme}.png")
    fig.savefig(path, bbox_inches="tight", pad_inches=0.28)
    plt.close(fig)
    return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for theme in ("light", "dark"):
        print(figure_spectrum(theme))
        print(figure_biprobability(theme))

    # Sanity checks printed to stdout, so a regeneration that silently breaks
    # the physics is visible rather than quiet.
    p_dis = probability(1, 1, PEAK_GEV, 0.0, DM32_NO)[0]
    p_app = probability(1, 0, PEAK_GEV, 0.0, DM32_NO)[0]
    print(f"check  P(nu_mu -> nu_mu) at 2 GeV, NO = {p_dis:.4f}  (expect a deep minimum)")
    print(f"check  P(nu_mu -> nu_e)  at 2 GeV, NO = {p_app:.4f}  (expect a few percent)")
    print(f"check  unitarity = {p_dis + p_app + probability(1, 2, PEAK_GEV, 0.0, DM32_NO)[0]:.6f}")
