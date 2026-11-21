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

## Results

`summarize.py` checks the batch records against the inventory and the gene reviews and
writes `results.tsv`, one line per row. Every one of the 788 rows has a verdict, and
every recorded action matches the gene review as it stands.

| | Rows |
|---|---:|
| Live rows re-judged against the tree | 735 |
| REMOVE upheld | 658 |
| Action changed | 77 |
| Withdrawn upstream (PAINT no longer propagates the term) | 53 |

Of the 221 live human rows, 184 are upheld and 37 changed.

Upheld rows by ground: loss or divergence in the target clade 359, misplaced IBD 188,
bad seed 73, lineage-inappropriate term 38. Each names a PAINT change and a node.

Changed rows by new action: `MARK_AS_OVER_ANNOTATED` 50, `MODIFY` 12,
`KEEP_AS_NON_CORE` 10, `UNDECIDED` 5. They are in 72 gene reviews. A further 78 rows
kept REMOVE but had the written reason corrected, because it rested on a non-ground or
misstated the tree.

### What the spurious removals had in common

`reason_scan.py` flags reasons by phrase and by where the seeds sit; `reason_scan.tsv`
holds the flags for every live row. Calibrated on the first 252 rows re-judged, against
each row's original text:

| Signal in the original reason | Rows | Changed |
|---|---:|---:|
| Argues absence of evidence and cites no PAINT node | 20 | 50% |
| Short reason (under 45 words) | 19 | 37% |
| Argues absence of evidence | 44 | 27% |
| Cites no PAINT node | 110 | 24% |
| Cites a PAINT node | 142 | 6% |

Seed position alone predicted little (a seed in the target's own child clade: 17%
changed, against 14% overall), because a close seed is often a diverged paralog. The
reverse held: with no seed in the target's child clade, 45 of 47 removals stood.

Three recurring errors, none visible without the tree:

- The gene is itself a seed of the node, through its own experimental row, and that
  row is kept. The inventory's `target_is_seed` column matches UniProt accessions
  only; seeds listed by model-organism id were checked by hand.
- The reason says the seeds are elsewhere in the family and a seed sits in the
  target's own clade.
- The term is true and general, and a descendant of it is accepted on another row.

### Open items

Not resolved by this pass:

- **Judgement calls left as recorded.** Six CAP-family molecular adaptor rows and five
  secreted FGF cytoplasm rows are `MARK_AS_OVER_ANNOTATED` where a misplaced-IBD
  reading would keep REMOVE. Mouse Krit1 keeps REMOVE on its own knockout while human
  and horse KRIT1 are `MARK_AS_OVER_ANNOTATED` on the same node. AGK ceramide kinase,
  PUS3, AN1593, `ccr1`/NCP1 cytosol and CYP2R1 are upheld on thin evidence.
- **Seed papers read as abstracts only.** Bad-seed verdicts that rest on an abstract
  say so in the batch record and should not go upstream as confirmed defects.
- **Family reviews now out of date or in disagreement** (not edited): PTHR10529,
  PTHR10553, PTHR10880, PTHR11022, PTHR11606, PTHR11670, PTHR15186, PTHR21601,
  PTHR22802, PTHR30417, PTHR30627, PTHR42760, PTHR43406, PTHR43418, PTHR43507,
  PTHR43876, PTHR48083. The batch `notes` say what each one misses.
- **Tree placement artefacts.** NTN1 and NTN3 sit in the POU family tree, yeast CDC4
  in the Utp13 family, worm `ccep-290` beside SMC2, and poplar `atpB` on a V-ATPase
  leaf. These need a leaf reassignment, which the PAINT change vocabulary cannot
  express.
- **Rows outside the scope that should follow.** GRB2 and Grb2 COP9 signalosome,
  PSEAE `rpoS` cis-regulatory region binding, fly CG14717 carboxylesterase ISS,
  `stlB` fatty acid biosynthesis IEA, and `atpB` rows from the same mis-mapped leaf.
- **Papers cited in prose only** because they are not in `publications/`:
  PMID:15340082 (SWI2), PMID:12950171 and PMID:17240044 (PCSK1), PMID:7867932 (tub),
  and the three SLC26A3 sulfate transport papers.
- `genes/SCHPO/mid1` fails validation on a quote that predates this work.
