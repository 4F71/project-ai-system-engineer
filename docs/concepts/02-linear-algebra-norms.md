# Linear Algebra — Norms (L1 vs L2)

## L1 Norm

The L1 norm of a vector is the sum of the absolute values of its components.

Formula:

||v||₁ = |x₁| + |x₂| + ... + |xₙ|

Where |x| represents the absolute value (if negative, it becomes positive).

- No squaring.
- No square root.
- Geometrically, it represents the Manhattan (grid) distance.

---

## L2 Norm

The L2 norm is the generalized form of the Pythagorean theorem.

a² + b² = c² extended to n dimensions.

Formula:

||v||₂ = √(x₁² + x₂² + ... + xₙ²)

- Geometrically, it represents the straight-line (Euclidean) distance.

---

## Square Root Behavior

- If 0 < x < 1 → x² < x, √x > x  
  (Squaring reduces the number, square root increases it.)

- If x > 1 → x² > x, √x < x  
  (Squaring increases the number, square root decreases it.)

---

## ML Connection

- L2 norm is used in cosine similarity calculations.
- L1 norm is related to sparsity and L1 regularization.
- A vector with ||v||₂ = 1 is called a unit vector and is fundamental for normalization.
