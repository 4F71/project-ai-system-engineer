<!-- File: docs/architecture/REPO-USAGE.md -->
# REPO-USAGE
## "What to Update When Adding Files" Manual

> This document is written **primarily for myself**.
> Purpose: To clarify **where to put what**, **which standard to follow**, and **what else needs updating** when adding something new to this repo.
> This repository is not a "note dump"; it is a **verifiable engineering progression system**.

---

## 0) The Golden Rule
**README tells the story → Template provides the structure → Content proves the claim.**  
These three cannot substitute for one another.

---

## 1) Repository Layers (Short Map)
- `docs/` → process + thought + decision + learning (the written system)
- `projects/` → end-to-end systems (integrated applications)
- `proofs/` → verifiable evidence (focused outputs)
- `roadmap/` → the plan (single source of truth: `MASTER-ROADMAP.md`)
- `scenarios/` → problem framing exercises (code not strictly required)
- `scripts/` → helper tools (support)
- `resources/` → curated lists of resources (inputs)
- `private/` → internal workings, prompts, thought logs (excluded from public narrative)

---

## 2) File Addition Decision Tree
I am going to write something new. Where do I put it?

### A) "Is this a weekly log?"
- **Yes** → `docs/journal/YYYY-MM-WeekNN.md`

### B) "Is this a learning note / concept explanation?"
- **Yes** → `docs/concepts/NN-topic-name.md`

### C) "Is this proof of an asserted skill?"
- **Yes** → `proofs/<domain>/...`

### D) "Is this a working system / integration / capstone?"
- **Yes** → `projects/<capstone>/...`

### E) "Is this a problem scenario (framing + tradeoff)?"
- **Yes** → `scenarios/<level>/scenario-XX-...md`

### F) "Is this a helper script?"
- **Yes** → `scripts/<scope>/...`

### G) "Is this an external resource list?"
- **Yes** → `resources/*.md`

### H) "Is this strictly my personal working setup?"
- **Yes** → `private/`

---

## 3) Template Usage Rules
Templates provide **minimal format**. Guidance belongs in the README.

Usage mapping:
- Journal → `docs/templates/journal-template.md`
- Concept → `docs/templates/concept-template.md`
- Retrospective → `docs/templates/retrospective-template.md`
- Proof → `docs/templates/proof-template.md`
- Scenario → `scenarios/_templates/scenario-template.md`

**Rule:** "How to write" instructions are not added inside the template.  
"How to write" stays in the respective directory's README.

---

## 4) Naming Standard (Immutable)
### Journal
- `docs/journal/YYYY-MM-WeekNN.md`
- Ex: `2026-02-Week02.md`

### Retrospective
- `docs/retrospectives/YYYY-MM-retro.md`
- Ex: `2026-02-retro.md`

### Concepts
- `docs/concepts/NN-topic-name.md`
- Ex: `01-linear-algebra-vectors.md`

### Scenarios
- `scenarios/<level>/scenario-XX-short-title.md`
- Ex: `scenario-01-churn-prediction.md`

### ADR (future)
- `docs/architecture/adr/YYYY-MM-DD-short-title.md`

---

## 5) "What to Update When Adding Files" — Mandatory Checklists

### 5.1 When adding a new Journal
**Add:**
- `docs/journal/YYYY-MM-WeekNN.md`

**Fix / Check:**
- Are all links within the journal real?
  - `projects/...`
  - `proofs/...`
  - `roadmap/...`
- The "deliverables this week" must include at least one of the following:
  - a proof file
  - a scenario file
  - a project update
  - or a clear ADR / runbook

**Quality Threshold:**
- "What did I do?" → concrete
- "What did I learn?" → specific
- "Evidence" → via file path

---

### 5.2 When adding a new Concept
**Add:**
- `docs/concepts/NN-...md`

**Fix / Check:**
- The concept must end with at least one of these links:
  - related `proofs/...`
  - related `projects/...`
- If the concept closes a roadmap item:
  - Do not just mark it as "read" in the roadmap,
  - It must be marked as "proven" (evidence: proof or project link)

**Quality Threshold:**
- definition + intuition + mini example + failure point + linkage

---

### 5.3 When adding a new Proof
**Add:**
- `proofs/<domain>/...md`

**Fix / Check:**
- Does the proof contain a "claim"?
- Is the claim proven?
  - measurement / result / demo / comparison / output
- Inside the proof file:
  - assumptions
  - constraints
  - reproduction path (script link if necessary)
- If the proof is derived from a project:
  - link to this proof from the project README (no copying, just linking)

**Quality Threshold:**
- "Text only" is not enough → there must be an evidence trail (output, metric, example, comparison).

---

### 5.4 When updating / adding a new Project
**Add:**
- `projects/<capstone>/...`

**Fix / Check:**
- Is the project README up to date?
  - boundaries
  - input/output
  - evaluation
  - related proofs
- If there are "artifact" files within the project (like an async interview):
  - these are not proofs → explicitly label them in the README
- As the project grows:
  - is it logical to add ADR/C4 to the `docs/architecture` side?

**Quality Threshold:**
- "Working system" narrative → clear boundaries + evaluation + links.

---

### 5.5 When adding a new Scenario
**Add:**
- `scenarios/<level>/scenario-XX-...md`

**Fix / Check:**
- In the scenario:
  - goal
  - assumptions
  - constraints
  - metric / definition of success
  - risks / failure mode
- If the scenario turns into a proof:
  - do not move it into `proofs/...`,
  - create a proof and link from the scenario to the proof

**Quality Threshold:**
- Code is not mandatory; **engineering thought process** is mandatory.

---

### 5.6 When adding a new Script
**Add:**
- `scripts/<scope>/...`

**Fix / Check:**
- Short header per script:
  - what it does
  - input/output
  - assumption
- If the script was written for a proof/project:
  - provide a link from the related file to the script

**Quality Threshold:**
- small, focused, reusable.

---

## 6) Commit Discipline (Summary)
The commits in this repo tell a **story**.

**Rule: One commit = one logical step.**  
Mixing examples (forbidden):
- README formatting + new proof in the same commit ❌
- Journal + massive refactor in the same commit ❌

### Ideal commit separations
- "README system" → single commit
- "WeekNN journal" → single commit
- "New proof" → single commit
- "Project milestone" → single commit
- "Refactor/cleanup" → single commit

**Standard for commit messages:** `private/prompts/commit-standard.md`

---

## 7) Weekly Work Routine (Practical System)
> Goal: To lock in the Roadmap → Output → Proof → Journal cycle

### Every week at a minimum:
1) 1 Journal (`docs/journal/...`)
2) 1 Proof **or** 1 Scenario
3) Update at least 1 item on the Roadmap with an "evidence link"

### End of month:
- 1 Retrospective (`docs/retrospectives/...`)

---

## 8) Most Common Mistakes (Self-Warning)
- Saying "I learned this" without providing an evidence link
- Writing a long narrative instead of a Proof
- Explaining a Project as if it were a Proof
- Piling everything into a single commit
- Using a template as a guide (forbidden)

---

## 9) Quick Commands (PowerShell)
### Status check
```powershell
git status
git diff
git diff --cached
```

### Typical Commit Cycle
```powershell
git add <file>
git commit -m "Brief summary" -m "Detailed explanation (why?)"
```
