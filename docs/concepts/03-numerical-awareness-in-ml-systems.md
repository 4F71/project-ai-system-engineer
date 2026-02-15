# Numerical Awareness in ML Systems

## What this concept is
Numerical awareness means designing ML system decisions with floating-point reality in mind. In practice, many failures come not from “wrong math” but from fragile comparisons and scale-insensitive thresholds.

## The core principle
**Error magnitude alone is not meaningful. What you compare it against is what matters.**

## Where ML systems break numerically
Typical decision boundaries:
- Convergence checks (loss improvement)
- Early stopping (validation loss comparisons)
- Gradient checks (analytic vs numeric gradient)
- Norm thresholds (gradient norm, parameter norm, update norm)

These are all “small difference” problems.

## Equality is a trap
Avoid:
- `loss_curr == loss_prev`
- `grad_norm == 0`

Because floats are approximations, exact equality often fails even when values are practically identical.

Prefer:
- `np.isclose(a, b, atol=..., rtol=...)`
- scale-aware inequalities such as `metric < threshold`

## atol vs rtol (intuition)
- **atol (absolute tolerance):** “How many units of difference are acceptable?”
- **rtol (relative tolerance):** “What fraction of the value is acceptable?”

NumPy’s comparison rule:
`|a - b| <= atol + rtol * |b|`

Guideline:
- near zero / small numbers → atol matters
- large magnitude values → rtol matters
- many ML decisions → use both

## Scale-relative tolerance
The same absolute delta can mean opposite things:
- loss ~ 1e6, delta = 0.1 → tiny relative change
- loss ~ 1e-3, delta = 0.1 → huge relative change

A common scale-aware signal:
- `delta / loss_prev < rtol`

## Norm-based convergence (system engineer view)
Fixed norm thresholds are brittle:
- `grad_norm < 1e-8` depends on model scale and parameterization

More robust:
- `grad_norm / param_norm < rtol`

This ties the decision boundary to the scale of parameters and improves stability across models.

## Evidence in this repo
- Lab notebook: `scripts/math/numerical_awareness_convergence_lab.ipynb`
- Proof: `proofs/02-math/2026-02-numerical-awareness-convergence-proof.md`
- Assets: `proofs/02-math/assets/numerical-awareness/`
- Roadmap: `roadmap\MASTER-ROADMAP.md`