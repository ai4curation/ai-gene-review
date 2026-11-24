# Re-review of every IBA row marked MARK_AS_OVER_ANNOTATED, 2026-11-24

Scope: every `existing_annotations` row with `evidence_type: IBA` and
`review.action: MARK_AS_OVER_ANNOTATED` in `genes/`. This follows the pass over IBA
rows marked REMOVE ([`../rereview-2026-11-21/`](../rereview-2026-11-21/README.md)) and
uses the same tools (`inventory.py`, `treeview.py` in that folder) and the same PAINT
snapshot. Human genes are judged first.

## The question for each row

`MARK_AS_OVER_ANNOTATED` says the term is not entirely wrong for the gene but claims
more than the evidence supports. For an IBA, the evidence is a PAINT curator's IBD at
an ancestral node, so the claim has to be located on the tree. It holds when one of
these can be stated:

1. **SEED_OVERREACH.** The experimental annotations the node rests on do not show that
   the gene product does the work of the term: a phenotype read as participation, an
   overexpression or in vitro activity of unknown relevance, a transit location. The
   over-annotation starts at the seeds and the IBD spreads it. The PAINT fix is usually
   `REMOVE_IBD`, with the seed rows named.
2. **NODE_TOO_DEEP.** The seeds are sound, but they sit in one part of the clade and the
   node covers branches, the target's among them, where nothing shows the function and
   the biology gives reason to doubt it. The fix is `MOVE_IBD` to the seeded clade. If
   the doubt amounts to evidence that the target's branch lacks the function, the row is
   a `REMOVE` on MISPLACED_IBD grounds, not an over-annotation.
3. **TARGET_DOUBT.** Evidence on the gene or its subfamily that the function is weak,
   conditional or partly diverged, short of showing loss. No PAINT fix follows from
   doubt alone; say what experiment would settle it.

It does not hold, and the row gets another action, when:

- the node is soundly seeded, the target sits inside the seeded clade and nothing on the
  target argues against the term: `ACCEPT` if the function is core, `KEEP_AS_NON_CORE`
  if it is peripheral. "No experimental data on this gene", a short donor list, and the
  gene being one of its own seeds are not reasons to doubt an IBA;
- the term is true but less specific than the evidence supports: `MODIFY` to a
  supported descendant, or keep it when it is as precise as the evidence allows;
- the term is a root organelle term whose organelle claim holds
  (`projects/ORGANELLES.md`): keep it;
- the term is wrong for the target on TARGET_LOSS, MISPLACED_IBD, BAD_SEED or LINEAGE
  grounds as defined in the REMOVE pass: `REMOVE`, with the PAINT fix;
- the evidence could not be read: `UNDECIDED`.

Rows that share a term must carry consistent actions (`docs/action_consistency.md`).

## Batch record format

```yaml
genes:
- gene_file: genes/human/XYZ/XYZ-ai-review.yaml
  rows:
  - go_id: GO:0000000
    go_label: term label
    family: PTHR00000
    ibd_node: PTN000000000
    tree_reading: >-
      What the tree shows: where the seeds sit, where the target sits, the duplication
      or speciation between them, and any PAINT loss recorded for the term.
    ground: SEED_OVERREACH | NODE_TOO_DEEP | TARGET_DOUBT | TARGET_LOSS | MISPLACED_IBD | BAD_SEED | LINEAGE | NONE
    verdict: OVER_ANNOTATION_UPHELD | ACTION_CHANGED | UNRESOLVED
    new_action: ACCEPT            # only when verdict is ACTION_CHANGED
    paint_fix:
      paint_action: ADD_IRD | ADD_IKR | MOVE_IBD | REMOVE_IBD | NONE
      target_node_id: PTN000000000
    evidence_checked:
    - what was looked up, and what it returned
    review_edited: false
    notes: anything a later reader needs
```

`ground` is NONE exactly when the row moves to ACCEPT, KEEP_AS_NON_CORE, MODIFY or
UNDECIDED. `target_node_id` is read from `treeview.py` output, never composed.
