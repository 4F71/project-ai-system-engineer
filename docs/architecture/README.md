# Architecture Docs

Architecture documentation for systems thinking and production readiness.

## What goes here?
- **ADR (Architecture Decision Records)**: why a decision was made
- **C4**: system diagrams (Context/Container/Component)
- **Runbooks**: operational procedures (on-call style)

## When to write
- After a meaningful design/decision
- Before/after implementing a system boundary
- When an operational practice is established (deploy, rollback, incident steps)

## How to write
- Decisions: use `docs/architecture/adr/README.md` guidance
- Diagrams: store in `docs/architecture/c4/`
- Operations: store in `docs/architecture/runbooks/`

## Related outputs
- `projects/` (implementations)
- `proofs/04-mlops/` (deployment/evaluation evidence)

---

## Türkçe

Bu klasör, sistem tasarımı ve production hazırlığı için mimari dokümantasyonu içerir.

Ne zaman yazılır?
- Önemli bir karar alındığında
- Sistem sınırları/servisleşme netleştiğinde
- Operasyonel süreçler oluştuğunda (deploy, rollback, incident)
