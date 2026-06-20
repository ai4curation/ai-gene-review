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
  themselves from PANTHER's `IBD.gaf` (the IBD/IRD/IKR — plus a few IBA-on-node —
  layer that is the *source* of every IBA). For each ancestral node our genes
  derive from, it lists the full
  node annotation set with the canonical seed counts, marks loss (IRD/IKR `NOT`)
  annotations, and flags node annotations that did **not** propagate to our gene
  (`propagated=false` → candidate missing annotation or lineage loss).
- `node_annotations.tsv` — the resulting per-node-annotation table.
- `extract_function_losses.py` — flags families where a **subfamily lost a
  function**: pairs every PAINT loss (any `NOT` annotation — usually IRD/IKR,
  occasionally `NOT|IBD`) with its ancestral gain node
  (IBD), checks the loss is within a cached family's PTN node set, and attributes
  it to the family **subfamilies** whose members descend from the loss node
  (resolved from the leaf GAF + member tables). This is the strongest
  within-family neo-/sub-functionalization signal and a direct curation guard:
  do not propagate the ancestral function to members under the loss node.
- `family_function_losses.tsv` — per-(family, lost-GO) findings with
  `ancestral_node`, `loss_node`, `gain_confirmed`, and the affected
  `subfamilies`. (`n_members_affected=0` means the loss is in an unsampled
  subfamily — the gain→loss pair is still confirmed.)
- `prepare_loss_analysis.py` — turns one loss finding into a ready-to-run input
  bundle for a bioinformatics agent to **reconstruct the key-residue rationale**
  (PANTHER never publishes which residues an IKR was based on — see the IKR note
  below). Emits YAML with `seed_uniprot` (where the function + its key residues
  are characterized), `loss_clade` (members predicted to have lost it), and
  `retaining_clade` (members that kept it). The agent fetches these sequences,
  aligns them, and compares the functional columns. Example:

  ```bash
  uv run python projects/PANTHER_IBA_REVIEW/prepare_loss_analysis.py \
      --family PTHR10443 --loss-node PTN000047776 --go GO:0016805
  ```

  Note: `loss_clade`/`retaining_clade` are resolved from the *reviewed* member
  tables + leaf GAF, so a finding with `n_members_affected=0` yields an empty
  `loss_clade` (the loss is in an unsampled subfamily); seeds are still provided.
  Of the 296 IKR findings, 49 have ≥1 attributed reviewed member and are
  immediately actionable.
- `REVIEW.md` — the written review and findings.

Regenerate:

```bash
uv run python projects/PANTHER_IBA_REVIEW/extract_iba_propagation.py
uv run python projects/PANTHER_IBA_REVIEW/extract_node_annotations.py
uv run python projects/PANTHER_IBA_REVIEW/extract_function_losses.py
```

The node-level source files (`IBD.gaf`, leaf GAF) are downloaded on demand into
a gitignored `.cache/panther/` and are not committed. Per-family node slices can
be materialised under `interpro/panther/<FAM>/<FAM>-paint.tsv` with:

```bash
just fetch-panther-paint PTHR10177
```

Scope: the 151 IBAs in the 40 reviewed genes (38 PANTHER families, all cached
locally). Note the cross-subfamily flag is deliberately sensitive and
over-fires on broadly conserved functions — it is triage, not a verdict.
