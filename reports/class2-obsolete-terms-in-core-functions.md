# Obsolete GO terms in `core_functions` — RESOLVED

Originally logged as a deferred follow-up during the CI-speedup / term-cleanup work
(see `docs/superpowers/specs/2026-06-15-ci-speedup-and-term-cleanup-design.md`).
**Now resolved**: `core_functions` is our own synthesis and should reference reasonably
up-to-date GO, so each obsolete term was migrated to its current equivalent. (Obsolete
terms remaining in `existing_annotations` are intentionally left as-is — those are
historical GOA annotation records.)

## The validator gap (still open, optional future work)

`linkml-term-validator` validates `core_functions` GO slots against dynamic enums expanded
by branch-**reachability** (`reachable_from`); it does **not** check `owl:deprecated`. An
obsolete term that keeps its `is_a` edges still passes. So nothing currently *prevents*
obsolete terms from re-entering `core_functions`.

Optional enhancement: add an obsolete-term check to strict term validation so obsolete
terms in `core_functions` become hard errors. Safe to add now that the data is clean.

## Migrations applied (21 usages across 16 files)

| Obsolete term | → current term | slot | count |
|---|---|---|---|
| `GO:0005615` extracellular space | `GO:0005576` extracellular region | locations | 16 |
| `GO:0009097` isoleucine biosynthetic process | `GO:1901705` L-isoleucine biosynthetic process | directly_involved_in | 3 |
| `GO:0019264` glycine biosynthetic process from L-serine | `GO:0006545` glycine biosynthetic process | directly_involved_in | 1 |
| `GO:0019629` propionate catabolic process, 2-methylcitrate cycle | `GO:0019543` propionate catabolic process | directly_involved_in | 1 |

Replacements verified against OLS/QuickGO (current, non-obsolete). Where a `locations` list
already contained `GO:0005576`, the resulting duplicate was removed (this also cleaned up 3
pre-existing duplicate `GO:0005576` entries in `ANOGA/TEP1`, `ANOGA/D7L1`, `ANOGA/TEP2`).

Verification: corpus-wide scan now reports **0 obsolete terms and 0 duplicate location
lists** in `core_functions`, and all touched files pass schema + term validation.
