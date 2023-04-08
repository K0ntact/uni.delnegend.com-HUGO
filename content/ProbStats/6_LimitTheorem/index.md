---
title: "6. Limit Theorem"
draft: false
---

{{<toc>}}

# The course so far
{{<hint type="note" title="What we have learnt?">}}
- Fundamental probability.
- Discrete random variables, probability mass function (PMF).
- Continuous random variables, probability density function (PDF).
{{</hint>}}

# I. The context
- A sequence $X_1, X_2, \dots$ of <c-red> independent identically distributed </c-red> random variables with mean $\mu$ and variance $\sigma^2$.
- Let $S_n = X_1 + X_2 + \dots + X_n$.
- Sample mean $M_n = \frac{X_1 + X_2 + \dots + X_n}{n}$.
- $\mathbb{E}[M_n] = \mu$, $var(M_n) = \frac{\sigma^2}{n}$.

# II. Inequalities
## Markov's inequality
If a <c-red> non-negative </c-red> random variable has a small mean, then the probability that it takes a large value must also be small.

{{<hint type="important" title="Markov's inequality">}}
If a random variable $X$ can only take non-negative values, then
$$P(X \geq a) \leq \frac{\mathbb{E}[X]}{a} \text{ for all } a > 0$$
{{</hint>}}

{{<hint type="note" title="Example">}}
Let $X$ be uniformly distributed in the interval $[0, 4]$. Find $P(X \geq 3)$.

$$P(X \geq 3) \leq \frac{\mathbb{E}[X]}{3}$$
$$\begin{aligned}
&= \frac{\mathbb{E}[X]}{3} \\\
&= \frac{4}{3} \\\
&= 1.3333
\end{aligned}$$
{{</hint>}}

## Chebyshev's inequality
If a random variable has small variance, then the probability that it takes a value <c-red> far from its mean </c-red> must be small.

{{<hint type="important" title="Chebyshev's inequality">}}
If $X$ is a random variable with mean $\mu$ and variance $\sigma^2$, then
$$P(|X - \mu| \geq a) \leq \frac{\sigma^2}{a^2} \text{ for all } a > 0$$
{{</hint>}}

# III. Limit theorem
## The weak law of large numbers
{{<hint type="important" title="Definition">}}
Let $X_1, X_2, \dots$ be <c-red> independent identically distributed </c-red> random variables with mean $\mu$. For every $\epsilon > 0$, we have
$$P(|M_n - \mu| \geq \epsilon) \to 0 \text{ as } n \to \infty$$
{{</hint>}}

Intuition: for large $n$, the distribution of $M_n$ is concentrated around $\mu$.

{{<hint type="note" title="Probabilities and frequencies">}}
Consider:
- an event A and its probability is $p = P(A)$.
- $n$ independent repetitions of the experiment.
- $M_n$ is the number of times A occurs in the $n$ repetitions.
{{</hint>}}

## The central limit theorem

{{<plyr repo="https://cdn.jsdelivr.net/gh/unilec/central_limit_theorem">}}

{{%center%}}
[Central limit theorem | Inferential statistics | Probability and Statistics | Khan Academy](https://www.youtube.com/watch?v=JNm3M9cqWyc)
{{%/center%}}

- Let $X_1, X_2, \dots$ be <c-red> independent identically distributed </c-red> random variables with mean $\mu$ and variance $\sigma^2$.
- Let $S_n = X_1 + X_2 + \dots + X_n$ and its variance is $n\sigma^2$.
- Let $M_n = \frac{X_1 + X_2 + \dots + X_n}{n}$ and its variance is $\frac{\sigma^2}{n}$.
- What about $\frac{S_n}{\sqrt{n}} = \frac{X_1 + X_2 + \dots + X_n}{\sqrt{n}}$?
- And $Z_n = \frac{S_n - n\mu}{\sqrt{n\sigma^2}}$?
- $\mathbb{E}[Z_n] = 0$, $var(Z_n) = 1$.

{{<hint type="important" title="Definition">}}
Let $Z \sim N(0, 1)$ and $Z_n = \frac{X_1 + X_2 + \dots + X_n - n\mu}{\sqrt{n\sigma^2}}$, for every z
$$lim_{n \to \infty} P(Z_n \leq z) = P(Z \leq z)$$
{{</hint>}}


Examples $Z_n = \frac{S_n - n\mu}{\sqrt{n\sigma^2}}$
{{<hint type="note" title="Example 1">}}
- $P(S_n \leq a) \approx b$
- Packages weights $X_i$, i.i.d. exponential $\lambda = \frac{1}{2}$.
- Load container with $n = 100$ packages.\
Calculate $P(S_n > 210)$.
{{</hint>}}

{{<hint type="note" title="Example 2">}}
- $P(S_n \leq a) \approx b$
- Packages weights $X_i$, i.i.d. exponential $\lambda = \frac{1}{2}$.
- Load container with $n = 100$ packages.\
Find $a$ so that $P(S_n > a) \approx 0.05$.
{{</hint>}}

{{<hint type="note" title="Example 3">}}
- $P(S_n \leq a) \approx b$
- Packages weights $X_i$, i.i.d. exponential $\lambda = \frac{1}{2}$.\
How large should $n$ be so that $P(S_n > 210) \approx 0.05$?
{{</hint>}}

{{<hint type="note" title="Example 4">}}
- Packages weights $X_i$, i.i.d. exponential $\lambda = \frac{1}{2}$.
- Load container until weight exceeds 210.
- $N$ is number of loaded packages.\
Calculate $P(N \geq 100)$.
{{</hint>}}