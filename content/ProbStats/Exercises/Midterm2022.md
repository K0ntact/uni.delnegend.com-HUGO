---
title: Midterm Exam 2022
draft: false
---
{{<toc>}}

# Question 1
Find the number of different 7-digit numbers which can be formed from the seven digits: 2, 2, 3, 5, 7, 7, 8 in each of the following cases:

a) Find the probability that the odd digits are together and the even digits are together.

{{<expand "Solution" "🧈">}}
- Number of ways to arrange the digits: $\frac{7!}{2! \times 2!}$ because there are 2 2's and 2 7's.
- Group the even digits together: 2, 2, 8
  - Number of ways to arrange the even digits: $\frac{3!}{2!}$ because there are 2 2's
- Group the odd digits together: 5, 3, 7, 7
  - Number of ways to arrange the odd digits: $\frac{4!}{2! \times 2!}$ because there are 2 7's
- Number of ways to arrange 2 groups: 2!

$\to P(\text{odd digits together and even digits together}) = 2! \times \frac{3!}{2!} \times \frac{4!}{2!} \times (\frac{7!}{2! \times 2!})^{-1}$
{{</expand>}}

b) Find the probability that the 2's are not together.

{{<expand "Solution" "🧈">}}
- Number of ways to arrange the digits: $\frac{7!}{2! \times 2!}$ because there are 2 2's and 2 7's.
- Group the 2's together: 2, 2
  - Number of ways to arrange the 2's: $\frac{2!}{2!}$ because there are 2 2's
- Group the rest of the digits: 5, 3, 7, 7, 8
  - Number of ways to arrange the rest of the digits: $\frac{5!}{2!}$ because there are 2 7's

$\to P(\text{2's not together}) = 1 - P(\text{2's together}) = 1 - \frac{2!}{2!} \times \frac{5!}{2!} \times (\frac{7!}{2! \times 2!})^{-1}$
{{</expand>}}

# Question 2
In a game, 3 coins named A, B, and C are tossed simultaneously. Let X be the number of heads obtained, find the $PMF p_x(x)$ if coins A and C are unfair that the prob of getting a head is 0.6 for coin A and 0.4 for coin C.

{{<expand "Solution" "🧈">}}
- Coin A: $P(H_A) = 0.6 ; P(T_A) = 0.4$
- Coin B: $P(H_B) = 0.5 ; P(T_B) = 0.5$
- Coin C: $P(H_C) = 0.4 ; P(T_C) = 0.6$
---
- $P(X = 0) = T_A \times T_B \times T_C = 0.4 \times 0.5 \times 0.6 = 0.12$
- $(X = 1)$:
  - $P(H_A) \times P(T_B) \times P(T_C) = 0.6 \times 0.5 \times 0.6 = 0.18$
  - $P(T_A) \times P(H_B) \times P(T_C) = 0.4 \times 0.5 \times 0.6 = 0.12$
  - $P(T_A) \times P(T_B) \times P(H_C) = 0.4 \times 0.5 \times 0.4 = 0.08$
  - $\to P(X = 1) = 0.18 + 0.12 + 0.08 = 0.38$
- $P(X = 2)$:
  - $P(T_A) \times P(H_B) \times P(H_C) = 0.4 \times 0.5 \times 0.4 = 0.08$
  - $P(H_A) \times P(T_B) \times P(H_C) = 0.6 \times 0.5 \times 0.4 = 0.12$
  - $P(H_A) \times P(H_B) \times P(T_C) = 0.6 \times 0.5 \times 0.6 = 0.18$
  - $\to P(X = 2) = 0.08 + 0.12 + 0.18 = 0.38$
- $P(X = 3) = H_A \times H_B \times H_C = 0.6 \times 0.5 \times 0.4 = 0.12$

---
$\to PMF: p_X(x) = \begin{cases} 0.06 \quad \text{if } x = 0 \\\ 0.38 \quad \text{if } x = 1 \\\ 0.38 \quad \text{if } x = 2 \\\ 0.12 \quad \text{if } x = 3 \end{cases}$
{{</expand>}}

# Question 3
The masses of honeydews are normally distributed with mean 1.5 kg and standard deviation 3.0 kg. The masses of rock melons are normally distributed mean 2.0 kg and standard deviation 4.0kg. Find the probability that 2 honeydews are more than three times as heavy as one rock melon.
- $\mu_{H} = 1.5, \sigma_{H} = 3.0$
- $\mu_{R} = 2.0, \sigma_{R} = 4.0$

{{<expand "Solution" "🧈">}}

Let H stands for honeydews and M stands for rock melons, using the formula $X \sim N(\mu, \sigma^2)$ to represent their normal distribution.
- $H \sim N(1.5, 3.0^2)$
- $M \sim N(2.0, 4.0^2)$

---
To find $P(H_1 + H_2 > 3R)$
- $P(H_1 + H_2 > 3R) = P(H_1 + H_2 - 3R > 0)$
- Let $X = H_1 + H_2 - 3R$

---
Find the mean and variance of $X$.
- $\mu_{X} = \mu_{H} + \mu_{H} - 3\mu_{R} = 1.5 + 1.5 - 3 \times 2.0 = -3$
- $\text{var}(X) = \text{var}(H_1) + \text{var}(H_2) + \text{var}(3R) = 3^2 + 3^2 + (3 \times 4)^2 = 162$

$\to X \sim N(-3, 162)$

---
Let $Z_{X} = \frac{X + 3}{\sqrt{162}}$.

$\begin{aligned}
P(X>0) &= P(Z_{X}> \frac{0 + 3}{\sqrt{162}}) \\\
&= 1 - P(Z_{X} < \frac{-3}{\sqrt{162}}) \\\
&= 1- \Phi(\frac{-3}{\sqrt{162}}) \\\
&= 1 - 0.0001 \\\
&= 0.9999
\end{aligned}$

{{</expand>}}