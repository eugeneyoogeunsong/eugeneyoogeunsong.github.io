---
layout: post
title: Process vs. Outcome
date: 2026-09-25 18:00:00+0100
description: A hundred jump shots, two kinds of people, and why I read a p-value the way I play a hand.
tags: notes
categories:
featured: false
---

<style>
  .pic-duo {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    gap: 0.75rem;
    margin: 1.5rem 0 2rem;
  }
  .pic-duo img {
    display: block;
    flex: 0 1 0;
    min-width: 0;
    width: 100%;
    height: auto;
    border-radius: 9px;
    background: var(--global-card-bg-color);
  }
  .pic-duo figcaption {
    flex-basis: 100%;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
    text-align: center;
    margin-top: 0.25rem;
  }
</style>

On my [Interests](/interests/) page there is a paragraph, under chess and poker, that I keep coming back to. It started as a note about card games and turned out to be about everything else, so it gets a post of its own.

<figure class="pic-duo">
  <img src="{{ '/assets/img/interests/chess-duo.jpg' | relative_url }}" alt="A chess board mid-game, gold pieces facing silver across the squares" width="880" height="1100" style="flex-grow:0.800" loading="lazy" decoding="async">
  <img src="{{ '/assets/img/interests/poker-duo.jpg' | relative_url }}" alt="A scattered deck of playing cards face up on a blue cloth, a joker near the centre" width="959" height="1100" style="flex-grow:0.872" loading="lazy" decoding="async">
  <figcaption>Complete information on the left; incomplete on the right. Most of life is the one on the right.</figcaption>
</figure>

Here is the paragraph, as it stands there:

> So what I hold myself to is the quality of the _process_: whether the equity was counted honestly, whether the expected value was positive at the moment I committed, whether I had genuinely tried everything I possibly can and truly left no stone unturned. Outcomes still matter, but as evidence rather than as a verdict: one hand tells you almost nothing; a thousand tell you everything. You have to stay at the table long enough for the thousand to arrive. The same holds for a person, a career or a run of results: what you want is the whole process, not one part of the story. That is why I always _trust the process_, and that habit carries directly into my research: it is the conviction that the outcome I want is produced by a sound procedure repeated, and that wanting it harder produces nothing on its own. The process, and the progression through it, are the parts that are genuinely mine to control (as the Stoics said), and the only parts that improve when I work at them; and it turns out to be the same discipline that governs how I read a p-value or a backtest.

That is the compressed version. The uncompressed version needs a basketball court.

**A hundred jump shots.** Give two people the same instruction: go and take a hundred jump shots. The first person hears a hundred repetitions of a movement, and their attention goes to the movement: where the feet are set, how high the jump is, whether the elbow stays under the ball, whether the release is the same on the ninetieth shot as on the first. The number is the container; what is inside it is the form. The second person hears a hundred, and their attention goes to the count: get to a hundred, by whichever means the ball goes through the hoop, or does not, and be done. Same court, same ball, same instruction; two entirely different afternoons.

Neither of them is wrong, and that is what makes the difference interesting rather than moral. The second person will finish first. The first person will be better at the hundred-and-first shot. If the goal is a number today, be the second; if the goal is a shooter, be the first. However, most goals worth having are the second kind dressed up as the first: a paper count is a proxy for a research programme; a year's returns are a proxy for a strategy; a hundred made shots are a proxy for a jump shot. Aim at the proxy directly and you can hit it while missing the thing it stood for.

**It shapes the person.** What struck me is that this is not merely a habit of attention; it hardens into a disposition. Do the hundred with your eyes on the form for long enough and you become someone who sees form everywhere, i.e., someone who, handed any task, first asks how it is done well. Do it with your eyes on the count and you become someone who first asks what done looks like, and works backwards from there. The personality literature noticed this too. In [Linda Berens' Interaction Styles](https://lindaberens.com/resources/methodology-articles/interaction-styles/), one of the axes along which the four styles are sorted is precisely a focus on _outcome_ against a focus on _process_: two of the styles are organised around getting the result or controlling its quality, and the other two around having a process or being inside one. A caveat belongs here, and it is the process-focused person's caveat: very little of personality typology, Berens' work included, sits inside the scientific realm as of now; these are descriptive frameworks built on observation and Jungian tradition, not measured constructs with the predictive track record that, say, the five-factor model has accumulated. I cite it as a vocabulary that happens to name the distinction well, not as evidence for it. Whether the habit builds the person or the person chooses the habit is, I suspect, a loop rather than an arrow; either way, I know which side of that axis I sit on, and I knew it from the basketball court before I knew it from any framework.

**Why it governs how I read a number.** Poker is where I learned this properly, because poker punishes the outcome view within an evening. You can play a hand perfectly and lose it; you can play it badly and win. Judge yourself by the outcome and you will learn the wrong lessons quickly and with great confidence. Judge yourself by the process, i.e., by whether the decision was correct given what could be known when it was made, and the outcomes start to mean something, but only in aggregate: one hand is noise, a thousand are data. Research is the same game with a slower clock. A p-value is one hand. A backtest is one hand. The question a process-focused person asks of either is not "did it come out the way I wanted?" but "would this procedure, repeated, keep producing it?" That is the whole of what a calibrated result is, and it is also, not by coincidence, the only question that survives someone checking your work.

So: form first, count second, and stay at the table long enough for the count to become evidence. That is the paragraph, uncompressed. I will keep coming back to it.

{% include linkedin_card.liquid %}
