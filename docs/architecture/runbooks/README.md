# Runbooks

Operational playbooks for systems:
- how to deploy
- how to rollback
- how to debug incidents
- how to validate health

## When to write
- When a system becomes runnable/deployable
- After an incident or a repeated operational task

## Format
Each runbook should include:
- Purpose
- Preconditions
- Step-by-step procedure
- Verification checklist
- Common failures + fixes
- Links to metrics/logs locations (if applicable)

## Related outputs
- `scripts/` (automation)
- `projects/` (services/pipelines)
- `proofs/04-mlops/` (evidence)

---

## Türkçe

Runbook, operasyonel adımları standartlaştırır (deploy/rollback/debug).

Her runbook:
Amaç / Ön koşul / Adımlar / Doğrulama / Sık hata + çözüm / Linkler