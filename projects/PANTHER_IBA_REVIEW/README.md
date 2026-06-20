---
title: "PANTHER IBA family review"
---

# PANTHER IBA family review

Family-level (PANTHER/PAINT) review of the IBA annotations on the 40 reviewed
S. pombe genes. Reviews the *source* of the IBAs — the phylogenetic
propagation — rather than re-judging gene by gene.

- `extract_iba_propagation.py` — reproducible extractor: for each IBA, resolves
  the ancestral PANTHER node, the seed genes, and the subfamilies of our gene
  and its seeds (from the cached `interpro/panther/<FAM>/` tables); flags
  cross-subfamily and localization propagations and joins our curation action.
- `iba_propagation.tsv` — the resulting per-IBA table (regenerate with the script).
  Carries inline node-level (PAINT) columns joined from `IBD.gaf`:
  `node_seed_count` (the authoritative canonical seed count curated at the source
  node, vs. the few `n_seeds` echoed into the leaf), `node_evidence`
  (IBD/IRD/IKR), and `node_loss`. New flags: `SINGLE_NODE_SEED` (≤1 canonical
  seed — weak support), `NODE_LOSS` (an IRD/IKR loss at the source node), and
  `NODE_NOT_IN_IBD`.
- `extract_node_annotations.py` — pulls the **PTN node-level (PAINT) annotations**
  themselves from PANTHER's `IBD.gaf` (the IBD/IRD/IKR layer that is the *source*
  of every IBA). For each ancestral node our genes derive from, it lists the full
  node annotation set with the canonical seed counts, marks loss (IRD/IKR `NOT`)
  annotations, and flags node annotations that did **not** propagate to our gene
  (`propagated=false` → candidate missing annotation or lineage loss).
- `node_annotations.tsv` — the resulting per-node-annotation table.
- `REVIEW.md` — the written review and findings.

Regenerate:

```bash
uv run python projects/PANTHER_IBA_REVIEW/extract_iba_propagation.py
uv run python projects/PANTHER_IBA_REVIEW/extract_node_annotations.py
```

The node-level source files (`IBD.gaf`, leaf GAF) are downloaded on demand into
a gitignored `.cache/panther/` and are not committed. Per-family node slices can
be materialised under `interpro/panther/<FAM>/<FAM>-paint.{gaf,tsv}` with:

```bash
just fetch-panther-paint PTHR10177
```

Scope: the 151 IBAs in the 40 reviewed genes (38 PANTHER families, all cached
locally). Note the cross-subfamily flag is deliberately sensitive and
over-fires on broadly conserved functions — it is triage, not a verdict.
