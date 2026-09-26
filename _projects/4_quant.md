---
layout: page
title: Quantitative research
description: Numerics, stocks, derivatives etc. - all quantitative, not using the traditional qualitative approaches.
img: assets/img/projects/quant.jpg
importance: 1
category: Quant
---

**Independent practice · London · October 2025 – August 2026**

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/quant.jpg' | relative_url }}"
    alt="A trading screen: a dense grid of prices, volumes and percentage changes overlaid with candlestick and line charts"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="eager"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    The raw material: prices, volumes and their changes. Everything below is an attempt to decide
    which parts of a screen like this are signal.
  </figcaption>
</figure>

An independent research programme in futures, derivatives and equities. The organising question was simple to state and hard to answer: **how do you detect a regime shift without overfitting to the last one?**

**Lines of work.**

- **Non-stationarity.** Most published edges are stationary-regime artefacts. I was interested in signals whose derivation survives a change in the data-generating process, not signals that happened to survive a backtest.
- **Structural constraints.** Market impact, inventory, liquidity and latency are not frictions to be assumed away; they are boundary conditions. A strategy specified without them has not been specified.
- **Signal and noise.** Physics-inspired separation methods: the same problem as pulling a faint astrophysical signal out of an instrument's systematics, with an adversary added.
- **Stochastic control.** Hamilton–Jacobi–Bellman (HJB) formulations for execution and inventory, Monte Carlo for path-dependent problems, and Bayesian methods for parameter uncertainty.

**The instrument: quantlab.** Those four lines of work needed somewhere to live, and that is [quantlab](https://github.com/eugeneyoogeunsong/quantlab), an open-source algorithmic trading research framework in Python that I built alongside the practice. It is organised as five layers (data, research, backtest, portfolio, execution) with derivatives pricing and mean-variance optimisation alongside, and it has one organising idea: **a backtest is not a result until it has a QA report attached.** The pipeline returns the performance and the checklist verdict in the same object, and the gate raises on any blocking failure, so looking at a Sharpe ratio without also seeing whether it is trustworthy is deliberately awkward. That is the [Process vs. Outcome](/blog/2026/process-vs-outcome/) principle written as software: a backtest is one hand, and the framework's job is to say whether the procedure that produced it would keep producing it.

The framework and the research questions above are the same work seen from two sides. Specifically:

- **Non-stationarity** becomes walk-forward validation with an embargo (parameters chosen on training data only, with a gap before the test window so lookback windows cannot straddle the boundary), plus a regime-coverage check, so a strategy that only ever saw one regime is flagged as such.
- **Overfitting** becomes the deflated Sharpe ratio, which corrects for how many variants were tried (every parameter combination in a sweep is counted, honestly), the probabilistic Sharpe for skew and fat tails, and the minimum track-record length: how many years you would need before the Sharpe is distinguishable from zero, which is frequently sobering.
- **Structural constraints** become the cost layer: five presets from institutional futures at 3.5 bps to small-cap equity at 25 bps plus slippage, and a square-root market-impact model in which total cost grows as size to the power 1.5, so you can run at two capital levels and find where the capacity limit actually is. A zero-cost model is a _failure_, not a warning, because "I forgot to add costs" and "costs are zero" produce identical numbers and only one of them is a decision.
- **Signal and noise** becomes the null-hypothesis suite: every strategy is run on forty zero-drift random walks, and anything that reliably profits there is finding structure that does not exist. The six reference strategies come out near zero on noise (cross-sectional momentum at a mean Sharpe of 0.02, time-series momentum at 0.06, mean reversion at 0.05), with the small positive bias for long-only books being Jensen's inequality rather than leakage, since zero log-drift implies an arithmetic drift of $$\sigma^{2}/2$$.

Look-ahead bias, the commonest way a backtest lies, is prevented structurally rather than by care: strategies return unshifted weights, the engine applies the execution lag at exactly one line, a lag of zero is refused, and four independent tests (truncation, weight-return correlation, a perfect-foresight canary that must be caught, and the null suite) defend it. There are 289 tests in all, fully offline, and two of them exist because they found real bugs during development: a Sharpe ratio of $$3.7 \times 10^{16}$$ on a constant return series, because the standard deviation of a constant array in floating point is $$10^{-19}$$ rather than zero; and a synthetic regime generator whose deterministic sine wave produced a 61% drawdown at 8.9% annual volatility, which no random walk can do (0 of 3,000 Monte Carlo paths came close). Both are kept as regression tests.

**Derivatives, by four routes.** The package prices European and American options analytically, on binomial and trinomial lattices, by finite-difference solution of the pricing PDE, and by Monte Carlo, with Greeks and implied-volatility inversion; every method follows a published reference. Four routes to one number is not redundancy: agreement between independent methods is evidence, and disagreement localises a bug (it is the same reason the neutrino experiment [NOvA](/projects/2_nova/) runs three independent fitters). The one substantive numerical finding came out of exactly that comparison. The binomial barrier pricer converges non-monotonically: the error against the closed form went $$1.2 \times 10^{-1} \to 1.4 \times 10^{-2} \to 2.7 \times 10^{-2}$$ as the step count went 500 to 2,000 to 5,000. The cause is structural, not a coding error: a CRR lattice can only take values $$S_0 u^{k}$$, the barrier generally falls between two of them, and changing the step count moves that misalignment erratically; aligning the lattice to the barrier fixes the placement but shifts the effective volatility by about 1%, which does comparable damage, and two branches cannot satisfy both constraints at once. Ritchken's stretched trinomial tree adds the third branch, i.e., the missing degree of freedom, and converges smoothly to $$7 \times 10^{-4}$$ over the same step counts. The binomial version is kept, with the limitation in its docstring, because the comparison is worth keeping visible.

**The execution problem, formally.** Liquidating inventory $$Q_t$$ at rate $$\nu_t$$ against a mid-price that your own trading moves is a stochastic control problem. With permanent impact $$b$$ and temporary impact $$k$$,

$$dS_t = -b\,\nu_t\,dt + \sigma\,dW_t, \qquad dQ_t = -\nu_t\,dt, \qquad d X_t = \nu_t\left(S_t - k\,\nu_t\right)dt$$

and the value function obeys a Hamilton–Jacobi–Bellman equation, the supremum running over the admissible trading rate:

$$\partial_t V + \frac{1}{2}\sigma^{2}\,\partial^{2}_{SS}V + \sup_{\nu}\Big\{\nu\left(S - k\nu\right)\partial_X V - \nu\,\partial_Q V - b\,\nu\,\partial_S V\Big\} = 0, \qquad V(T,\cdot) = -\alpha\,Q_T^{2}$$

The terminal penalty $$-\alpha Q_T^{2}$$ is the point. Impact, inventory and the closing bell are boundary conditions rather than frictions bolted on afterwards, and a strategy that omits them is solving a different problem from the one the market poses.

**Background.** The [Algorithmic Trading courses](https://algosoc.com/) run by the Imperial College Algorithmic Trading Society; [Securities Education Certificate](https://yoogeunsong.com/assets/pdf/securities-education-certificate.pdf) (Distinction, [Imperial College Investment Society](https://investmentsoc.com/)); [Finance Accelerator](https://my.amplifyme.com/certificate/72010d28-0612-4e53-b3ed-4188c32f3baf), London; member of Imperial's [Algorithmic Trading](https://algosoc.com/) and [Investment](https://investmentsoc.com/) societies.

**A note on the dual track.** I do not treat physics and quant as a hedge against each other. They are the same discipline (build a model of a process you cannot fully observe, quantify what you do not know, and act on the result), applied to data that pays differently.

_Work in progress; outputs will appear here and on [Publications](/publications/)._

{% include linkedin_card.liquid %}
