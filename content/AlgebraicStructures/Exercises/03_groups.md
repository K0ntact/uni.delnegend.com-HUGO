---
title: 03.1. Groups
draft: false
---

# Exercise 1
Show that $\mathbb{R}^* = \mathbb{R} \backslash \text{\\{} 0 \text{\\}}$ is a group under multiplication.

{{<expand "Solution">}}
Let $a$ and $b$ be elements of $\mathbb{R}^\*$. Then $ab = ab \cdot 1 = ab \cdot \frac{1}{ab} = \frac{ab}{ab} = 1$.
{{</expand>}}

# Exercise 2
Give the group $\mathbb{R}^\*$ and $\mathbb{Z}$, let $G = \mathbb{R}^\* \times \mathbb{Z}$. Define a binary operation $\circ$ on $G$ by $(a;m) \circ (b;n) = (ab;m+n)$. Show that $G$ is a group under this operation.

# Exercise 3
Show that addition and multiplication mod $n$ are associative operations in $\mathbb{Z}$.

# Exercise 4
Let $G$ be a group and suppose that $(ab)^2 = a^2b^2$ for all $a$ and $b$ in $G$. Prove that $G$ is an abelian group.

# Exercise 5
Let $S = \mathbb{R} \backslash \text{\\{} -1 \text{\\}}$ and define a binary operation on $S$ by $a \circ b = a + b + ab$. Prove that $(S; \circ)$ is an abelian group.

# Exercise 6
Let $a$ and $b$ be elements of a group $G$. If $a^4b = ba$ and $a^3 = e$, prove that $ab = ba$.

# Exercise 7
If $xy = x^{-1}y^{-1}$ for all $x$ and $y$ in a group $G$, prove that $G$ must be abelian.

{{<expand "Solution">}}
Let $x$ and $y$ be elements of $G$. Then $xy = x^{-1}y^{-1} = (xy)^{-1} = y^{-1}x^{-1} = yx$. Hence $G$ is abelian.
- [Def 1 - prop 3](/AlgebraicStructures/2_Groups/#proposition-3)
{{</expand>}}

# Exercise 8
Let $a$ be an element in a group. Prove that $a^n = (a^{-1})^n$.

{{<expand "Solution">}}
Let $n$ be a positive integer. Then $a^n = a \cdot a^{n-1} = a \cdot (a^{-1})^{n-1} = (a^{-1})^{n-1} \cdot a = (a^{-1})^n$.
{{</expand>}}

# Exercise 9
Let $a$ and $x$ be elements in a group $G$. Prove that $ax = xa$ if and only if $a^{-1}x = xa^{-1}$.

# Exercise 10
Let $a$ and $b$ be elements of a group $G$. Assume that $a$ has order $5$ and $a^3b = ba^3$. Prove that $ab = ba$.

# Exercise 11
Let $a$ and $b$ be integers. Prove that the subset $a\mathbb{Z} + b\mathbb{Z} = \{ak + bl \mid k \in \mathbb{Z}\}$ is a subgroup of $\mathbb{Z}$.