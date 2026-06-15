# Follow-up: obsolete GO terms in `core_functions` (not CI-blocking)

Generated 2026-06-15 as a logged follow-up from the CI-speedup / term-cleanup work
(see `docs/superpowers/specs/2026-06-15-ci-speedup-and-term-cleanup-design.md`).

## The validator gap

`linkml-term-validator` validates the `core_functions` GO term slots (`molecular_function`,
`directly_involved_in`, `locations`, `in_complex`, …) against **dynamic enums expanded by
branch-reachability** (`reachable_from`). It does **not** check whether a term is marked
`owl:deprecated`. An obsolete GO term that still retains its `is_a` edges therefore **passes
validation** — it is reachable from the branch root even though it is obsolete.

Consequence: obsolete terms can sit in `core_functions` indefinitely without failing CI.
This is distinct from the complex-misslotting errors fixed in the cleanup (those failed
because complex terms are genuinely outside the cellular-location branch).

## Current obsolete-term usages

See `class2-obsolete-terms-in-core-functions.tsv` (21 usages across 16 files). Obsoletion
status confirmed against QuickGO:

| Term | Status | Recommended replacement | Count |
|------|--------|-------------------------|-------|
| `GO:0005615` extracellular space | obsolete | same concept as `GO:0005576` extracellular region | 16 |
| `GO:0009097` isoleucine biosynthetic process | obsolete | use a more-specific isoleucine biosynthesis term | 3 |
| `GO:0019264` glycine biosynthetic process from L-serine | obsolete (represents a GO-CAM model) | re-express as activity/process terms | 1 |
| `GO:0019629` propionate catabolic process, 2-methylcitrate cycle | obsolete (too narrow) | use a broader propionate catabolism term | 1 |

## Suggested remediation (future PR)

1. **Data:** replace the obsolete terms above with their current equivalents in the affected
   `core_functions` (mostly `GO:0005615` → `GO:0005576`).
2. **Validator (optional but recommended):** add an explicit obsolete-term check to strict
   term validation so obsolete terms in `core_functions` become hard errors. Note this would
   make the usages above CI-blocking, so it must land *after* the data is fixed.
