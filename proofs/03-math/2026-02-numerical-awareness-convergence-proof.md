# Proof — Numerical Awareness Convergence Lab (2026-02)

## Purpose

This proof documents why exact equality (`==`) is unsafe at ML decision boundaries and demonstrates how tolerance-based checks (`atol`, `rtol`, `np.isclose`) and scale-relative metrics produce more stable convergence behavior.

This is a system-level numerical reasoning validation, not theoretical math.

---

## Claims

1. Exact equality on floating-point values is unreliable for system decisions (convergence, early stopping, gradient checks).
2. A fixed absolute threshold can be brittle across different value magnitudes.
3. A stable convergence signal should be:
   - tolerance-based (`np.isclose(loss_t, loss_{t-1}, atol, rtol)`), and/or
   - scale-aware (e.g., `grad_norm / param_norm < tolerance`).

NumPy comparison rule:

|a - b| <= atol + rtol * |b|

This rule explicitly combines absolute and relative tolerance.

---

## Method

We executed a single lab notebook structured into four controlled experiments:

A — Equality Trap  
`0.1 + 0.2` compared to `0.3` using `==` and `np.isclose`.

B — Absolute vs Relative Intuition  
Same absolute delta under two different loss scales.

C — Convergence Rule Comparison  
Simulated loss curve and three stopping rules:
- absolute delta rule
- relative delta rule
- `np.isclose` rule

D — Norm-Based Convergence  
Comparison between:
- `grad_norm < constant`
- `grad_norm / param_norm < tolerance`

Notebook:
- scripts/math/numerical_awareness_convergence_lab.ipynb

---

## Evidence (Artifacts)

Concept Documentation:
- docs/concepts/03-numerical-awareness-in-ml-systems.md
- docs/concepts/03-numerical-awareness-in-ml-systems-TR.md

Notebook:
- scripts/math/numerical_awareness_convergence_lab.ipynb

Assets:
- proofs/02-math/assets/numerical-awareness/equality_isclose.png
- proofs/02-math/assets/numerical-awareness/scale_relative_delta.png
- proofs/02-math/assets/numerical-awareness/norm_based_stop.png

Roadmap Integration:
- roadmap/MASTER-ROADMAP.md (III.0 Numerical Foundations)

---

## Results

### 1. Floating Point Equality Failure

Observed:

|0.1 + 0.2 - 0.3| ≈ 5.55e-17

- Direct equality (`==`) → False
- `np.isclose()` → True

This demonstrates representational precision limits of binary floating point numbers.

---

### 2. Same Absolute Delta, Different Meaning

Case A:
loss = 1e6  
delta = 0.1  
relative change = 1e-7  

Case B:
loss = 1e-3  
delta = 0.1  
relative change = 1e2  

Identical absolute improvement.
Radically different relative meaning.

Fixed absolute tolerance ignores scale context.

---

### 3. Convergence Rule Behavior

Absolute-only stopping:
- May stop too early at small scales
- May stop too late at large scales

Relative or mixed tolerance (`atol + rtol`):
- Behaves more consistently across magnitudes

---

### 4. Norm-Based Interpretation

Fixed gradient magnitude tested against parameter scales:

Small parameter norm → large relative update  
Large parameter norm → negligible relative update  

Therefore:

`grad_norm < constant` is scale-blind.  
`grad_norm / param_norm < tolerance` is scale-aware.

---

## Engineering Conclusion

In ML systems:

- Equality is a design decision, not a mathematical guarantee.
- Tolerance is a boundary condition.
- Scale determines interpretation.
- Convergence must be defined relative to magnitude.

Robust ML systems must:

- Avoid `==` for float comparisons at decision points.
- Use tolerance-based comparisons (`atol`, `rtol`, `np.isclose`).
- Prefer scale-relative metrics for convergence.
- Tie stopping criteria to model magnitude.

This proof confirms numerical awareness as an engineering competency, not just mathematical familiarity.
