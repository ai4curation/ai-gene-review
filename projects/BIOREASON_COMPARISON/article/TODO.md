---
title: "Paper TODO"
species: [rat, mouse]
---

# Paper TODO

## SFT prediction reviews: status as of 2026-09-27

### History

An earlier version of this file said the first automated SFT review script was a mistake. It recorded "29 genes manually reviewed (335 predictions)" and "155 genes auto-reviewed, MUST BE REDONE MANUALLY".

That script has since been replaced. `scripts/auto_review_sft_predictions.py` is now a conservative audit and repair tool. It changes an assessment only when an exact join to current GOA or AIGR makes the label inconsistent, and it records a "Current-snapshot audit reclassified X to Y" rationale when it does. The 29/155 split cannot be re-derived from the files, because the per-file review provenance is not recorded.

### What the committed files show

All counts come from `uv run python projects/BIOREASON_COMPARISON/audit_followup.py` (`scripted_rationales`, `argo95_current_snapshot_reclassifications`).

**ARGO95 (primary cohort; 95 files, 955 terms, all marked `COMPLETE`):**

- **Done.** 862 of 955 rationales are not one of the two templates below.
- **Deterministic audit changes.** 61 calls were relabelled `CNN` by the audit (27 from `UNC`, 25 from `COR`, 9 from `NPI`), and 23 were relabelled to `NPI` or `REP` (20 from `CNN`, 2 from `UNC`, 1 from `LSP`). Each relabelled call keeps its earlier rationale.
- **Scripted `CNN` rationales (disclosed; no action needed).** 71 `CNN` calls in 9 genes carry the template "Term is in GOA — already a known curated annotation." All 71 have an exact line in the committed GOA TSV. `CNN` is definitional for an exact in-GOA term, so these calls are acceptable. The project page discloses them.
- **Open.** 22 `UNC` calls carry the template "Generic or ancestor term not confirmed or refuted by GOA or AI gene review." They have not been reviewed term by term. All 93 templated ARGO95 rationales, `CNN` and `UNC` together, fall in 9 genes: mouse Calm1 and Pten, and rat Casp3, Hspa5, Rgn, Slc5a1, St13, Tp53 and Uggt1.
- **Open.** 62 of the 147 discordant (`NPI`/`PLI`/`REP`) ARGO95 terms carry no `error_type`. They are reported as untagged on the project page.

**Supplemental SFT union (198 files, 11,100 terms, all marked `COMPLETE`):**

- **Not manually reviewed.** 8,783 of the 11,100 rationales are the two templates above: 7,009 generic `UNC` and 1,774 in-GOA `CNN`. They span 42 genes.
- These files are used only as supplemental source-availability diagnostics, never as a main result.
- **Open.** Their `COMPLETE` status overstates review depth. Either downgrade them to `DRAFT` or review them manually, prioritizing any `COR` and `NPI` calls.

### Other open items

- A **human-rated anchor subset** for the RL narrative scores and the matched SFT/RL scores. All current raters are LLM agents.
- A **blinded matched SFT/RL re-rating** with the model identity hidden.
- **SFT narratives for the 29 ARGO139 genes absent from the HF catalogue.** They would have to be generated with the released SFT model.
- **Rebuild `manuscript.pdf`** from `manuscript.tex` once a LaTeX toolchain is available (see `README.md`).
