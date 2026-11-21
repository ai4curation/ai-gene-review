# Re-reading overruled IBA rows with the tree

[← tree and alignment evidence](../tree-evidence.md)

A review that marks an IBA row `REMOVE` or `MARK_AS_OVER_ANNOTATED` argues with a PAINT
curator's placement of a term on a tree node. Until 2026-11 almost none of those verdicts
was made with the tree in view ([tree-evidence.md](../tree-evidence.md)). This folder is
the re-read: every such row, read again next to what the gene's tree extract
(`GENE-phylo.yaml`) says about it.

## Scope

`plan.yaml` is the frozen work list for gene reviews: 1,699 rows in 1,180 genes, in 73
batches of about 24 rows, which is what one agent reads in one go. Genes with a row on the
candidate list ([`tree-evidence-candidates.yaml`](../tree-evidence-candidates.yaml)) come
first.

- 1,686 rows are IBA rows with an overruling verdict that are still in the gene's GOA
  file and do not yet quote the extract.
- 13 rows are kept or refined although PAINT has removed the term on the path to the
  gene. They need a decision about the loss, not a quote, and are read but never edited
  by the script.

`plan-families.yaml` is the work list for family reviews: 386 node assessments in 218
families that dispute a PAINT placement (`TOO_DEEP`, `WRONG_NODE`, `NEEDS_PRUNING`,
`LOSS_CONTRADICTED`, `LOSS_TOO_BROAD`) without citing a tree listing, in 18 batches. They
are read against the family's node listing (`<PTHR>-tree-nodes.yaml`) in the same way,
with two additions from the release tree: where each seed sits, and how many leaves of
each subfamily the review names as affected lie below the node.

## Status (2026-11-21)

| | Batches | Rows read | Applied | Left for adjudication |
|---|---:|---:|---:|---:|
| Gene reviews, candidate genes (`g001` to `g012`) | 12 of 73 | 278 | 228 | 48, and 2 not read |
| Gene reviews, pilot of the corrected rules (`g013`, `g014`) | 2 of 73 | 47 | 47, one of them by hand | 0 |
| Gene reviews, the rest (`g015` to `g073`) | 0 of 59 | 0 | | |
| Family reviews (`f001` to `f018`) | 18 of 18 | 386 | 321, two of them by hand | 65 |

`tree_rereview.py status` prints the current counts. Results and what they show are in
[tree-evidence.md](../tree-evidence.md#the-re-read). What is left for a curator is in
[`needs-curator.yaml`](needs-curator.yaml).

The 59 unread gene batches hold 1,370 overruled rows in 934 genes. Since the plans were
made, reviews merged on main have added 293 overruled IBA rows in 213 genes and 254
disputed node assessments: 238 in 138 families the plan does not cover, and 16 new ones
in 10 families it had read (as of the fifth merge, 2026-11-21). Those have extracts and
listings, and are not
in either plan; `plan` makes a plan once and does not extend it, so they need batches of
their own.

The plan is fixed in its batches, not in its rows. A batch names genes or families; its
rows are looked up when the batch is read, so a review that another change has edited in
the meantime brings its rows as they then are, and the counts above can drift from the
totals in `plan.yaml`. Making a record again for a batch that has been applied would
leave out its applied rows, which no longer need reading, so a batch is recorded once.

## Method

One batch at a time:

1. **Dossier.** `tree_rereview.py dossier` writes, for every row, the review's verdict,
   summary, reason, `propagation_review`, existing support and the other rows of the same
   review on the same term, next to the extract's facts for that row: where the PAINT node
   sits, where the gene sits, each seed with its relation to the gene and its identity in
   the family alignment, PAINT losses on the path, and the extract's summary by numbered
   sentence. Under the summary it names the sentences that stand against the verdict
   (`MUST QUOTE AND ADDRESS`).
2. **Reading.** An agent reads the dossier, and nothing else, and returns one reading per
   row (below), the summary sentences to quote, and one or two sentences on what the tree
   shows. It edits nothing. The instructions it works from are in
   [`workflows/`](workflows/).
3. **Verification.** A second agent tries to fault the first: every correction, every row
   on the candidate list, every row whose tree file has a sentence that stands against the
   verdict, and one in four of the rest. It checks the reading against the
   definitions and every fact in the sentence against the dossier. Where it faults a
   reading that only needs another reading, quote or sentence, it supplies the corrected
   one, which is then used whole; such a row is recorded with `verifier.agrees: false` and
   `outcome_detail: applied as corrected by the verifier`.
4. **Applying.** `tree_rereview.py apply` makes the edits from this one checkout:
   - quotes are assembled from the extract's own sentences and checked verbatim, so an
     agent never types a quote;
   - each edit changes the text of one row
     (`src/ai_gene_review/tools/review_row_edit.py`) and is refused if the reloaded file
     differs from the original by anything but the edit;
   - the review is validated afterwards and put back as it was if it no longer validates;
   - a history record is scaffolded for every review that changed, and checked against
     the history schema.

| Reading | Meaning | What the script does |
|---|---|---|
| `SUPPORTS` | The verdict argues about placement and the tree agrees | Quote the row; add the sentence to the reason |
| `NOT_A_TREE_ARGUMENT` | The verdict rests on something the tree cannot settle, and the tree contradicts nothing the review says | Quote the row; add the sentence |
| `PAINT_ALREADY_REMOVED` | PAINT has itself removed the term on the path; the cached row is stale | Quote the row, including the loss; add the sentence |
| `REASON_CONTRADICTED` | The review says something about placement, relatedness or the seeds that the tree contradicts, but the verdict stands on other stated grounds | If the verifier agrees and the claim is in the reason only: quote the row and replace the reason with the corrected one |
| `VERDICT_UNSUPPORTED` | The tree contradicts the argument the verdict depends on | Nothing. Listed for adjudication |
| `LOSS_APPLIES`, `LOSS_TOO_BROAD` | For the 13 kept rows under a PAINT loss | Nothing. Listed for adjudication |
| `CANNOT_TELL` | The dossier is not enough | Nothing. Listed for adjudication |

### What the script will not do

An edit is a quote plus a sentence, or a quote plus a corrected reason. Everything else
is left for a curator, with the reason in the run record:

- **No verdict is changed, and no failure mode.** A reading may propose either; the row
  then goes to adjudication. Six rows of the first batches had failure modes changed by
  the script before this rule. All six were checked by hand: two were put back (`DROME/mam`,
  `SCHPO/cab4`) and four were kept.
- **A contradicted claim outside the reason is not half-corrected.** The script rewrites
  `reason` (`assessment_reason` in a family review) and nothing else. When the claim the
  tree contradicts is also in the summary, in a failure mode, in a source note or in
  `affected_subfamilies`, rewriting the reason alone would leave the row contradicting
  itself, so the row is left alone. A row with no reason at all is left alone too.
  **Such a row is then corrected by hand before its batch is pushed.** The verifier
  accepted the reading whole, drafted correction included, so the review states something
  both agents found false, and what the script may rewrite does not decide whether that
  statement stays. `finish` names these rows, `needs-curator.yaml` marks them
  `contradicted_and_left` and counts them (0 today), and the run record's `correction`
  says what was done. Three rows so far: ARATH MNS1 `GO:0036503`, and the family
  assessments PTHR10048 `GO:0005944` and PTHR16675 `GO:0002476`, each checked against the
  release tree before the edit.
- **A contradiction whose draft the verifier faulted is not applied either.** Here no
  agreed correction exists, so there is nothing to apply by hand. Often the verifier
  accepted the finding and faulted only the drafted text, and then the review may still
  state something the tree contradicts. `needs-curator.yaml` marks these rows
  `contradiction_disputed` and counts them apart (15 today), with the verifier's objection;
  they need a new reading, and `finish` prints how many a batch leaves. A contradiction
  the verifier never saw would be counted here too; there is none today.
- **A row whose review changed on main after it was read is not re-applied.** The row is
  taken as on main, and the work list marks it `needs_new_reading` (29 today): its
  `action`, `tree_reading` and `note` describe the review as it was read and may no longer
  describe the committed one.
- **Quoting around an adverse fact.** A reading must quote more than the sentence that
  names the term, and must quote every sentence that stands against the verdict: that the
  gene is itself a seed, that it is inside the clade the seeds span, that seeds share its
  own branch below the node, that every seed is an ortholog although the row claims a
  paralog; for a family review, that the seeds bracket a node assessed as `TOO_DEEP`. The
  same rule is a validation warning for every gene review
  (`tree_evidence_adverse_unquoted`, [docs/phylo.md](../../../docs/phylo.md)).
- **An edit that would reach more than one row.** A row is matched by term, evidence code
  and negation (by node, term and negation in a family review). When a review has several
  such rows the edit is not made.
- **A value shared through a YAML anchor**, from either the row that defines it or a row
  that refers to it. Only a shared `supported_by` list is handled: it is written out in
  full in each row that used it, and the history record says so.

A row is also left for adjudication when the verifier disagrees with its reading without
supplying a usable correction.

### A review that disputes the placement itself

The relation between a gene and a seed ("ortholog", "one-to-one ortholog") is read from
the family and subfamily PANTHER placed the gene in. A review whose argument is that this
placement is the error (the gene lacks the domain that defines the family, the subfamily
lumps proteins of different architecture, the alignment covers a small part of the gene)
is not refuted by the relation, because the relation is the thing disputed. Such a row is
`NOT_A_TREE_ARGUMENT`: the sentence says that the tree places the seeds as orthologs and
that the review disputes that placement, and the failure mode `WRONG_ORTHOLOG_OR_PARALOG`,
whose definition includes a wrong family or subfamily, stays. A seed with a
horizontal-transfer node between it and the gene is never a one-to-one ortholog.

## Files

- `plan.yaml`, `plan-families.yaml`: the batches. Made once and kept.
- `runs/<batch>.yaml`: one record per batch. Every row with its reading, the sentence, the
  verifier's check where there was one, and the outcome: `applied`, `adjudicate` or
  `not_read`, with the reason in `outcome_detail`. `quotes_added` lists sentences added to
  a row's quotes afterwards (`requote`), and `correction` says what was put right by hand
  after review.
- `needs-curator.yaml`: what the re-read leaves for a curator, from the run records: every
  row left for adjudication or not read, and every applied row on which the reader left a
  note. An applied row quotes its tree file, so it leaves the work list and the validator's
  warnings; the note, often about a verdict or failure mode that no longer fits, would
  otherwise be lost in a run record. `contradicted_and_left` and `contradiction_disputed`
  mark the two kinds of row left for adjudication after a contradiction was read (see
  above); a row whose review changed on main after the reading is in neither and is marked
  `needs_new_reading`.
- `workflows/`: the instructions the reading and verifying agents work from, as workflow
  scripts. They define the readings.
- `tree_rereview.py`: `plan`, `dossier`, `inputs`, `record`, `apply`, `finish`, `status`,
  `worklist`, and two repair commands for rows applied before a rule existed: `requote`
  (add the sentences a row must quote) and `references` (list the quoted tree file under
  the review's `references`; `apply` now does this itself). Tests are in
  `tests/test_tree_rereview.py`.

## Reproduce

```bash
uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py status
uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py dossier g001 --out /tmp/dossiers
uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py worklist
```

A batch is run in three steps: `inputs g013 g014 --out DIR` writes the dossiers and the
arguments for the workflow in `workflows/`; the workflow returns the readings; `finish
--journal JOURNAL --date YYYY-MM-DD --pr N` records them, applies them, writes the history
records with the pull request linked, and renews `needs-curator.yaml`. Before the batch
is pushed, the rows `finish` names as contradicted and left are corrected by hand.

The readings themselves are agent output and are not regenerated by a command; the run
records are their record.
