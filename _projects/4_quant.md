---
layout: page
title: Quantitative research
description: Alpha under non-stationary market dynamics, treated as a signal-and-noise problem.
img: assets/img/projects/quant.jpg
importance: 1
category: Quant
---

**Independent practice · London · October 2025 – August 2026**

An independent research programme in futures, derivatives and equities. The organising question was simple to state and hard to answer: **how do you detect a regime shift without overfitting to the last one?**

**Lines of work.**

- **Non-stationarity.** Most published edges are stationary-regime artefacts. I was interested in signals whose derivation survives a change in the data-generating process, not signals that happened to survive a backtest.
- **Structural constraints.** Market impact, inventory, liquidity and latency are not frictions to be assumed away; they are boundary conditions. A strategy specified without them has not been specified.
- **Signal and noise.** Physics-inspired separation methods: the same problem as pulling a faint astrophysical signal out of an instrument's systematics, with an adversary added.
- **Stochastic control.** Hamilton–Jacobi–Bellman (HJB) formulations for execution and inventory, Monte Carlo for path-dependent problems, and Bayesian methods for parameter uncertainty.

**The execution problem, formally.** Liquidating inventory $$Q_t$$ at rate $$\nu_t$$ against a mid-price that your own trading moves is a stochastic control problem. With permanent impact $$b$$ and temporary impact $$k$$,

$$dS_t = -b\,\nu_t\,dt + \sigma\,dW_t, \qquad dQ_t = -\nu_t\,dt, \qquad d X_t = \nu_t\left(S_t - k\,\nu_t\right)dt$$

and the value function obeys a Hamilton–Jacobi–Bellman equation, the supremum running over the admissible trading rate:

$$\partial_t V + \frac{1}{2}\sigma^{2}\,\partial^{2}_{SS}V + \sup_{\nu}\Big\{\nu\left(S - k\nu\right)\partial_X V - \nu\,\partial_Q V - b\,\nu\,\partial_S V\Big\} = 0, \qquad V(T,\cdot) = -\alpha\,Q_T^{2}$$

The terminal penalty $$-\alpha Q_T^{2}$$ is the point. Impact, inventory and the closing bell are boundary conditions rather than frictions bolted on afterwards, and a strategy that omits them is solving a different problem from the one the market poses.

**Background.** [Securities Education Certificate](https://investmentsoc.com/SEC) (Distinction, [Imperial College Investment Society](https://investmentsoc.com/)); [Finance Accelerator](https://my.amplifyme.com/certificate/72010d28-0612-4e53-b3ed-4188c32f3baf), London; member of Imperial's [Algorithmic Trading](https://algosoc.com/) and [Investment](https://investmentsoc.com/) societies.

**A note on the dual track.** I do not treat physics and quant as a hedge against each other. They are the same discipline - build a model of a process you cannot fully observe, quantify what you do not know, and act on the result - applied to data that pays differently.

_Work in progress; outputs will appear here and on [Publications](/publications/)._
