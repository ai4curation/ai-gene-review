# Re-review of every IBA row marked REMOVE, 2026-11-21

Scope: every `existing_annotations` row with `evidence_type: IBA` and
`review.action: REMOVE` in `genes/`. On the starting commit that is 788 rows in 561
gene reviews. Each row is re-judged against the PANTHER family tree and the PAINT
node annotations, not against the wording of the earlier reason.

## Files

- `inventory.py` writes `inventory.tsv`: one line per row, with the PAINT node the
  pinned snapshot propagates the term from, its family, clade size, seed count,
  whether the gene is itself a seed, and any PAINT loss on the lineage. The `status`
  column is computed, never judged.
- `treeview.py` prints the tree context for one gene and term: the lineage from leaf
  to root with every PAINT record on it, and the child clades of the node holding the
  IBD, with members and the PAINT records inside each.
- `batches/batch-NN.yaml`: the manual verdicts, one entry per gene.

## What a verdict has to establish

An IBA is the projection of a PAINT curator's IBD at an ancestral node. A REMOVE is
therefore a claim about the tree, and it holds only when one of these is shown:

1. **Target-specific loss or divergence.** Evidence on the gene itself, or on its
   subfamily, that the function was lost or replaced (a pseudoenzyme, a
   neofunctionalised paralog, a different substrate or compartment that excludes the
   ancestral one). The PAINT fix is an IRD or IKR at the node where the loss arose.
2. **Misplaced IBD.** The experimental seeds all sit in one child clade and the
   target sits in another, across a duplication or an old speciation, and the term is
   wrong for the target's clade. The PAINT fix is moving the IBD to the seeded clade.
3. **Bad seed.** The experimental annotation the node rests on is itself wrong, and
   no other seed supports the node. The fix is at the seed, and the IBD goes with it.
4. **Lineage-inappropriate term.** The process or structure does not exist in the
   target's lineage.

A REMOVE does not hold on any of these grounds, and the row gets another action:

- the gene has no experimental annotation of its own (that is what an IBA is for);
- the WITH/FROM list is short, or the gene appears in it;
- the term is true but general, or duplicates another row (`MODIFY` to a supported
  descendant, or keep it: `ACCEPT` if core, `KEEP_AS_NON_CORE` if peripheral);
- the term is plausible and unverified (`MARK_AS_OVER_ANNOTATED` when the node
  placement is doubtful, `UNDECIDED` when the evidence could not be read);
- a root organelle term whose organelle claim holds (see `projects/ORGANELLES.md`).

Rows that share a term must carry consistent actions
(`docs/action_consistency.md`). When the gene is itself a seed of the node, the IBA
and the experimental row it rests on are judged together.

## Batch record format

```yaml
genes:
- gene_file: genes/human/LALBA/LALBA-ai-review.yaml
  rows:
  - go_id: GO:0003796
    go_label: lysozyme activity
    family: PTHR11407
    ibd_node: PTN004256961
    tree_reading: >-
      What the tree shows: where the seeds sit, where the target sits, the duplication
      or speciation between them, and any PAINT loss already recorded for the term.
    ground: TARGET_LOSS | MISPLACED_IBD | BAD_SEED | LINEAGE | NONE
    verdict: REMOVE_UPHELD | ACTION_CHANGED | UNRESOLVED
    new_action: KEEP_AS_NON_CORE   # only when verdict is ACTION_CHANGED
    paint_fix:
      paint_action: ADD_IRD | ADD_IKR | MOVE_IBD | REMOVE_IBD | NONE
      target_node_id: PTN000150677
    evidence_checked:
    - what was looked up, and what it returned
    review_edited: false
    notes: anything a later reader needs
```

`paint_action` uses the `family_review.yaml` vocabulary. `target_node_id` is read
from `treeview.py` output, never composed.
