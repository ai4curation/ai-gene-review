---
title: "PANTHER IBA family review"
maturity: MATURE
last_reviewed: "2026-10-04"
tags: [EVALUATION, PIPELINE]
species: [SCHPO]
manifest:
  slides:
    - href: PANTHER_IBA_REVIEW/slides/PANTHER_IBA_REVIEW-slides.html
      description: AI generated
---

# PANTHER IBA family review

**Bottom line:** every IBA annotation descends from a PAINT curator's IBD
judgment placed at an ancestral node of a PANTHER tree, so the place to test
an IBA is that node and the target's position below it. We rebuilt the
propagation behind all 161 IBAs on the 41 reviewed *S. pombe* genes (36 of
which carry IBAs) from cached repo data: source node, seed genes, subfamilies,
PAINT loss annotations, and our per-gene action. We did this to check whether
the per-gene calls hold up at the family level, and to find the patterns that
mark a real over-propagation. They held up. The per-gene reviews kept 149 of
the 161 IBAs (118 ACCEPT, 31 KEEP_AS_NON_CORE); the 38 cross-subfamily flags
turned out to be mostly conserved functions; and the family lens confirmed the
two localization REMOVEs (pom1 `cytoskeleton`, rqh1 `cytoplasm`) and recast the
third REMOVE (mid1 septin ring organization) as sub-functionalization between
the two pombe anillins. No new IBA errors were found among the accepted rows.

The same tooling also extracts PAINT's own loss annotations, mostly IRD/IKR, as
a curation guard: 2,498 loss findings across 622 cached families (2,492 paired
with a confirmed ancestral gain), of which 68 IKR losses fall on a reviewed
member and are ready for residue-level follow-up
([#3991](https://github.com/ai4curation/ai-gene-review/issues/3991)). The
written review is in [REVIEW.md](PANTHER_IBA_REVIEW/REVIEW.md).

The rest of this page documents the scripts and tables.

- `PANTHER_IBA_REVIEW/extract_iba_propagation.py` — reproducible extractor: for each IBA, resolves
  the ancestral PANTHER node, the seed genes, and the subfamilies of our gene
  and its seeds (from the cached `interpro/panther/<FAM>/` tables); flags
  cross-subfamily and localization propagations and joins our curation action.
- `PANTHER_IBA_REVIEW/iba_propagation.tsv` — the resulting per-IBA table (regenerate with the script).
  Carries inline node-level (PAINT) columns joined from `IBD.gaf`:
  `node_seed_count` (the authoritative canonical seed count curated at the source
  node, vs. the few `n_seeds` echoed into the leaf), `node_evidence`
  (IBD/IRD/IKR), and `node_loss`. New flags: `SINGLE_NODE_SEED` (≤1 canonical
  seed — a provenance count, not a measure of evidential strength), `NODE_LOSS` (an IRD/IKR loss at the source node), and
  `NODE_NOT_IN_IBD`; `NONE` denotes a row with no propagation flags.
- `PANTHER_IBA_REVIEW/extract_node_annotations.py` — pulls the **PTN node-level (PAINT) annotations**
  themselves from PANTHER's `IBD.gaf` (the IBD/IRD/IKR — plus a few IBA-on-node —
  layer that is the *source* of every IBA). For each ancestral node our genes
  derive from, it lists the full
  node annotation set with the canonical seed counts, marks loss (IRD/IKR `NOT`)
  annotations, and flags node annotations that did **not** propagate to our gene
  (`propagated=false` → candidate missing annotation or lineage loss).
- `PANTHER_IBA_REVIEW/node_annotations.tsv` — the resulting per-node-annotation table.
- `PANTHER_IBA_REVIEW/extract_function_losses.py` — flags families where a **subfamily lost a
  function**: pairs every PAINT loss (any `NOT` annotation — usually IRD/IKR,
  occasionally `NOT|IBD`) with its ancestral gain node
  (IBD), checks the loss is within a cached family's PTN node set, and attributes
  it to the family **subfamilies** whose members descend from the loss node
  (resolved from the leaf GAF + member tables). This is the strongest
  within-family neo-/sub-functionalization signal and a direct curation guard:
  do not propagate the ancestral function to members under the loss node.
- `PANTHER_IBA_REVIEW/family_function_losses.tsv` — per-(family, lost-GO) findings with
  `ancestral_node`, `loss_node`, `gain_confirmed`, and the affected
  `subfamilies`. (`n_members_affected=0` means the loss is in an unsampled
  subfamily — the gain→loss pair is still confirmed.)
- `PANTHER_IBA_REVIEW/prepare_loss_analysis.py` — turns one loss finding into a ready-to-run input
  bundle for a bioinformatics agent to **reconstruct the key-residue rationale**
  (PANTHER never publishes which residues an IKR was based on — see the IKR note
  below). Emits YAML with `seed_uniprot` (where the function + its key residues
  are characterized), `loss_clade` (members predicted to have lost it), and
  `retaining_clade` (members that kept it). The agent fetches those sequences,
  aligns them, and compares the functional columns.
- `PANTHER_IBA_REVIEW/REVIEW.md` — the written review and findings.

Example:

```bash
uv run python projects/PANTHER_IBA_REVIEW/prepare_loss_analysis.py \
    --family PTHR10443 --loss-node PTN000047776 --go GO:0016805
```

Note: `loss_clade`/`retaining_clade` are resolved from the *reviewed* member
tables + leaf GAF, so a finding with `n_members_affected=0` yields an empty
`loss_clade` (the loss is in an unsampled subfamily); seeds are still provided.
Of the 504 IKR findings, 68 have ≥1 attributed reviewed member and are
immediately actionable
([#3991](https://github.com/ai4curation/ai-gene-review/issues/3991)).

Regenerate:

```bash
just refresh-panther-iba-project
```

The three tables can also be refreshed independently with
`just refresh-panther-iba-propagation`,
`just refresh-panther-iba-node-annotations`, and
`just refresh-panther-iba-function-losses`.

The node-level source files (`IBD.gaf`, leaf GAF) are downloaded on demand into
a gitignored `.cache/panther/` and are not committed. Per-family node slices can
be materialised under `interpro/panther/<FAM>/<FAM>-paint.tsv` with:

```bash
just fetch-panther-paint PTHR10177
```

Scope: the 161 IBAs in the 41 reviewed genes (39 PANTHER families, all cached
locally). Note the cross-subfamily flag is deliberately sensitive and
over-fires on broadly conserved functions — it is triage, not a verdict.
One well-characterized descendant can soundly ground an ancestral assertion.
Review its phylogenetic placement and relevant functional divergence; do not
infer weak support from a short seed list.
