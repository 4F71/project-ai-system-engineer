# Proof — L1 and L2 Norm Practice

## Example 1
v = [3,4]

L1 = 7  
L2 = 5

---

## Example 2
v = [0.8, 0.6]

L2 = 1 (unit vector)

---

## Example 3
v = [-5, 2, -1]

L1 = 8  
L2 = √30 ≈ 5.47

---

## Observation

For the same vector:
L1 ≥ L2


---

# Additional Practice (2026-02)

## Proof — L1 and L2 Norm Practice

## Example 1 — v = [6, 8]

L1 = |6| + |8| = 14  
L2 = √(6² + 8²) = √(36 + 64) = √100 = 10

---

## Example 2 — v = [-3, 4, 12]

L1 = |-3| + |4| + |12| = 3 + 4 + 12 = 19  
L2 = √((-3)² + 4² + 12²) = √(9 + 16 + 144) = √169 = 13

---

## Example 3 — v = [0.3, 0.4]

L1 = |0.3| + |0.4| = 0.7  
L2 = √(0.3² + 0.4²) = √(0.09 + 0.16) = √0.25 = 0.5

Unit vector check:
A unit vector satisfies ||v||₂ = 1.  
Here ||v||₂ = 0.5, so v is not a unit vector.

Evidence: proofs/02-math/assets/vectors-demo.png, proofs/02-math/assets/l1-vs-l2-path.png, scripts/math/norm_demo.py, scripts/math/vector_plot_demo.py, scripts/math/norm_distance_demo.py
