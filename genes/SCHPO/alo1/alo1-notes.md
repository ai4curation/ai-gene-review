# alo1 review notes

## 2026-10-10 fungal PAINT re-review

### Setup and literature search

- Started from a fresh `origin/main` worktree on branch
  `codex/schpo-alo1-fungal-alo1`.
- Ran `UV_FROZEN=1 just fetch-gene SCHPO alo1`, then forced a refresh with
  `UV_FROZEN=1 just fetch-gene SCHPO alo1 --force`. The forced refresh updated
  the current GOA export: stale positive exact `GO:0003885` and `GO:0070485`
  rows disappeared, and PomBase now exports `NOT` IGC rows for both exact
  assertions while retaining broad positive `GO:0016899` oxidoreductase
  activity.
- Tried `UV_FROZEN=1 just deep-research-falcon SCHPO alo1 --fallback
  perplexity-lite`; the provider stack was unavailable in this workspace, so no
  new provider report was generated.
- Searched for newer S. pombe alo1 literature by `alo1`, `SPAPB1A10.12c`, and
  UniProt `Q9HDX8`. I found no direct newer biochemical, genetic, or
  localization paper for the S. pombe protein beyond the cached PomBase ORFeome
  localization paper.

### Evidence summary

- The direct S. pombe experimental row is the PomBase HDA mitochondrion row from
  the fission-yeast ORFeome localization study. The cached paper is
  abstract-only and does not list alo1 in the visible text, but the abstract
  describes the YFP localization screen covering 4,431 fission-yeast proteins.
- The current PomBase curation is deliberately broad: positive
  oxygen-dependent CH-OH oxidoreductase activity, target-local mitochondrial
  localization, and orthology-transferred mitochondrial outer-membrane
  localization, paired with `NOT` rows against exact D-arabinono-1,4-lactone
  oxidase activity and dehydro-D-arabinono-1,4-lactone biosynthesis.
- Cached S. cerevisiae publications, including the 1998 ALO1 enzymology paper
  and the 2025 Alo1/Myo2 study, are useful for family context but do not
  justify transferring the exact substrate, the D-erythroascorbate biosynthetic
  process, or mitochondrial inheritance to S. pombe alo1.

### PAINT / IBA review

- `PANTHER:PTN000356408` carries broad `GO:0016491 oxidoreductase activity`
  across a mixed eukaryotic/bacterial aldonolactone oxidoreductase node. That is
  a valid but generic parent activity for S. pombe alo1.
- `PANTHER:PTN000356435` now carries the exact fungal `GO:0003885
  D-arabinono-1,4-lactone oxidase activity` IBD seeded by SGD and CGD ALO1, but
  this node is not in the current S. pombe alo1 GOA IBA row. The old S. pombe
  IBA for GO:0003885 via `PANTHER:PTN001015900` was stale and was removed by
  the forced GOA refresh.
- `PANTHER:PTN001015900` carries the fungal `GO:0005739 mitochondrion` IBD and
  an IRD pruning `GO:0019853 L-ascorbic acid biosynthetic process` below the
  broad `PTN000356408` placement. Do not add an ascorbate biosynthetic process
  row.

### Main curation decisions

- Removed stale positive exact `GO:0003885` and `GO:0070485` rows that are no
  longer present in the current GOA export.
- Accepted the new PomBase `NOT` rows against exact
  D-arabinono-1,4-lactone oxidase activity and
  dehydro-D-arabinono-1,4-lactone biosynthesis.
- Accepted the positive `GO:0016899` rows as the best current molecular-function
  level and kept broad `GO:0016491` and FAD-binding rows as non-core support.
- Kept the PAINT `GO:0005739` mitochondrion IBA and the ORFeome mitochondrion
  HDA as broad non-core location support, and accepted the PomBase ISO
  mitochondrial outer-membrane row as the core location.
- Did not add any `NEW` rows. Neither exact D-erythroascorbate biosynthesis,
  L-ascorbate biosynthesis, oxidative-stress response, nor the S. cerevisiae
  Alo1/Myo2 inheritance role is currently justified for S. pombe alo1.
