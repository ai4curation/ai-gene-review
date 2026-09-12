# Design: CI speedup + core_functions term cleanup

Date: 2026-06-15
Branch: `feat/speedup`

## Problem

CI takes **~80–90 min per PR**. `main.yaml` runs `just validate-all` over **all 2,555
gene-review files** on every PR, regardless of what changed, and there is **no ontology-DB
caching** (multi-GB GO/CHEBI SQLite re-downloaded each run).

Two complementary levers (both approved):

1. **Scope** PR validation to only the genes that changed (the pattern used in the
   `dismech` repo via `dorny/paths-filter`).
2. **Speed up the stack** so the unavoidable full runs (schema/`src`/validator changes,
   pushes to `main`) are also fast — primarily by caching the ontology DBs.

## Strictness finding (resolved)

CI is **not** at maximum strictness today. In `validate-all`, ontology **term/label
validation is advisory** (`|| echo "non-blocking"`, comment: "pre-existing issues on main",
introduced in #298). Schema, references, best-practices and PMID-markdown checks **are**
blocking. The per-gene `just validate` (local / `generate-pages`) **does** run terms.

Decision: when scoping to changed genes, run the **full strict per-gene validation,
including blocking term validation** — raising strictness to what was assumed. Because it
only runs on changed files, the only risk is fix-on-touch of pre-existing issues, which we
remove first via the cleanup below.

## Cleanup scope (Part A — done first)

A full corpus term run found **70 files** with **CI-blocking** term errors (validator
ERRORs). Root cause of the dominant category: curators put **protein-complex GO terms**
into `core_functions[].locations` (range `GOCellularLocationEnum`, which excludes the
`protein-containing complex` branch). The schema **already has an `in_complex` slot**
(range `GOProteinContainingComplexEnum`) — no schema change needed; this is data + stopping
the regression.

Edits are done **manually (targeted edits)**, never via a YAML load/dump script, to
preserve comments and key order.

### A1 — Mechanical migration (58 files, 67 occurrences)
For each `core_function` with exactly one complex term in `locations` and no pre-existing
`in_complex`: move that term to `in_complex`; keep any non-complex (real CC) `locations`
siblings; drop `locations` if it becomes empty.

### A2 — Judgment files (12 files, reviewer-fixed)
- `ATP6V1G3`, `UPF3A`: two complex terms in one `locations` — pick the appropriate single
  `in_complex` (most specific / correct sub-complex), demote/keep the other appropriately.
- `COP1`: `core_function` already has `in_complex` plus a complex in `locations` — reconcile.
- `EMC9`, `EMC10`: complex term `GO:0072546` ("EMC complex") sits in `molecular_function`
  (and locations) — move to `in_complex`; set a real subunit-appropriate MF.
- `SPCS1/2/3`: `GO:0006465` "signal peptide processing" is **obsolete** (concept is MF
  `GO:0009003` signal peptidase activity) in `directly_involved_in`; also a complex in
  locations — reconcile both.
- `HYPK`: `GO:0010699` in `molecular_function` does not denote "acetyltransferase inhibitor
  activity" (wrong id) — replace with the correct current MF.
- `rhp51`: `GO:0000730` "DNA recombinase assembly" (a BP) is in `molecular_function` → move
  to `directly_involved_in`.
- `SEC63`: `GO:0031204` (a BP) in `molecular_function` → move to `directly_involved_in`.
- `cdc12`: `GO:0051016` (a BP) in `molecular_function` → `directly_involved_in`; and
  `GO:0110085` "mitotic actomyosin contractile ring" (a CC, not a complex) sits in
  `in_complex` → move to `locations`.

### A3 — Regression prevention
Update the core-function-synthesizer guidance and the `locations`/`in_complex` schema slot
docs so complex terms go to `in_complex` going forward.

### A4 — Verify
Full corpus term validation returns **0 errors** for the touched files.

## Logged follow-up (Class 2 — NOT in this work)

Separate from CI-blocking errors: the term validator only checks branch-**reachability**,
so **obsolete GO terms that retain their edges pass validation**. ~16 files use such terms
in `core_functions` (validator does not flag them):
- `GO:0005615` "extracellular space" → obsolete, concept of `GO:0005576` "extracellular
  region" (~14 files: GAS6, PDGFA/B, IGFBP3, IFNL4, PCSK1N, CRISP3, mouse Edn1/Egf/Epo/Gas6…)
- `GO:0009097` (isoleucine biosynthesis, obsoleted for more-specific terms) — MISSI/ALS,
  MISSI/VAT1, PSEPK/ilvC
- `GO:0019264` (METEA/glyA), `GO:0019629` (PSEPK/acnB)

Decision: **log this as a data-quality follow-up**; do not fix now. Optionally, a future
change could add an obsolete-term check to strict validation (would make Class 2
CI-blocking). Recorded in `reports/` + a project note for later.

## CI speedup (Part B)

### B1 — Changed-files scoping (`main.yaml`)
`dorny/paths-filter` with `list-files: shell`, two filters:
- `genes`: `genes/**/*-ai-review.yaml` (+ pathway markdown for PMID checks)
- `infra`: schema (`src/ai_gene_review/schema/**`), `src/**`, `conf/**`,
  `scripts/run_*_validator.sh`, `justfile`, `project.justfile`

Logic (PR and push to `main`): **infra changed → full `validate-all`; else genes changed →
validate only changed genes (strict, terms blocking); else skip.** Deleted files skipped.

### B2 — Strict per-changed-gene recipe
New `just` recipe (e.g. `validate-changed FILES…`): schema + **terms (blocking)** +
references + best-practices + PMID-markdown per changed file.

### B3 — Ontology-DB cache
`actions/cache` on `~/.data/oaklib` with a weekly-rotating key + `restore-keys`; add
`jlumbroso/free-disk-space` so large DBs fit.

### B4 — Make full runs strict (after A merges)
Flip `validate-all` term validation from advisory to blocking so infra-change/`main`/weekly
runs enforce terms too.

### Safety net
A weekly scheduled full `validate-all` (or the existing weekly-compliance path) guards
against drift not covered by per-PR scoping.

## Sequencing

PR1 = Part A (cleanup + regression prevention + Class 2 log). PR2 = Part B (CI). Both on
`feat/speedup`. B4 lands only after A is merged so `main` stays green.

## Testing / verification

- Cleanup: per-file term validation = 0 errors on the 70 touched files; spot-render unaffected.
- CI: unit test(s) for `validate-changed`; a sample-PR scoping dry-run; confirm ontology-DB
  cache hit on a second run.
