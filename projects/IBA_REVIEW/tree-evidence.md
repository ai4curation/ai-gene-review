---
title: "Tree and Alignment Evidence Behind IBA Verdicts"
species: [human, MYCTU, VIBCH, yeast, SCHPO, worm, DROME, rat, mouse, ECOLI]
---

# Tree and alignment evidence behind IBA verdicts

[← back to the findings page](../IBA_REVIEW.md)

**Bottom line:** An IBA is a PAINT curator's placement of a function on a node of a family
tree, made with the tree and the family alignment in view. Our reviews judged those
placements from the GOA row alone, which carries a node id and a seed list. A census on
2026-11-09 found a tree or alignment artifact behind 1.8% of 29,084 IBA rows, and behind
4.5% of the 1,586 rows we had overruled. Every review can now read the PANTHER 19.0 tree
and family alignment for its own rows (`GENE-phylo.yaml`, from `just phylo`), and a
`REMOVE` or `MARK_AS_OVER_ANNOTATED` on an IBA row is asked to quote it, including what in
it stands against the verdict. Joining all 31,805 reviewed IBA rows with their tree facts
shows that our verdicts follow the gene tree closely although almost none was made with
it: we overrule 1.3% of rows where the gene is itself a seed, and 21.1% where the gene lies
outside the clade the seeds span and has no one-to-one ortholog among them. The same join
found errors in two of this project's own flagship write-ups, and 256 rows whose verdict
and tree pull in different directions. Those rows are listed for re-review; the analysis
itself changed no verdict.

## What was missing

A review of an IBA row had the node id, the seed ids, the family's member table with
subfamily labels, and the UniProt record. It did not have the tree's topology, its
duplication and transfer events, the leaves below the node, or the alignment. The cached
PAINT slice records a node's taxon for 72% of IBD rows and nothing else about where the
node sits.

| Evidence committed behind an IBA row (2026-11-09) | All 29,084 rows | 1,586 overruled rows |
|---|---:|---:|
| A family review assesses that node and term | 22.9% | 26.4% |
| That assessment cites a tree or clade listing | 0.1% | 0.1% |
| Gene folder has a script that reads the PANTHER tree | 0.8% | 0.7% |
| Gene folder has a multiple-alignment script | 0.6% | 1.6% |
| Review carries structured residue claims | 0.6% | 2.6% |
| Any tree or alignment artifact | 1.8% | 4.5% |

The census counted committed scripts, files and structured fields. A reviewer who looked
at a tree and left only prose was not counted.

## What exists now

- **`just fetch-panther-release`** reads PANTHER's release files once into a local
  database: every family tree with its speciation, duplication and transfer events and
  branch lengths, every family alignment, the full-length sequence of every leaf, and the
  node table that ties tree nodes to `PTN` ids. The live PANTHER tree service timed out on
  every family tried from this environment, so nothing depends on it.
- **`just phylo <org> <GENE>`** writes `GENE-phylo.yaml`. For each IBA row it states where
  the PAINT node sits, how many steps and duplications separate it from the gene, whether
  the seeds bracket the node, whether the gene is inside the clade the seeds span, how
  each seed is related to the gene, their identity and coverage in the family alignment,
  PAINT losses on the path, and the family's curated residue sites read off the alignment.
  Each row ends in a one-line `summary` for quoting.
- **`just phylo-family <PTHR>`** writes `<PTHR>-tree-nodes.yaml`, the same description for
  every node of a family's PAINT slice.
- **Checks.** `just validate` warns when an IBA row is overruled without a quote from the
  gene's own extract (`missing_tree_evidence`), when the quote leaves out a sentence that
  stands against the verdict (`tree_evidence_adverse_unquoted`: the gene is itself a seed,
  is inside the seed clade, shares its branch with seeds, or every seed is an ortholog
  under a paralog claim), when a row is kept although PAINT has removed the term on the
  path to the gene (`kept_under_paint_loss`), and when a propagated row is overruled for
  residue loss without a checkable residue claim (`missing_residue_evidence`; 105 rows in
  65 reviews on 2026-11-21, [below](#residue-arguments-without-a-residue-claim)).
  `just validate-families` reports a node assessment that disputes a placement without
  quoting a tree listing (`NODE_TREE_EVIDENCE`).
- **Backfill.** Extracts are committed for 1,401 genes: every gene whose review overrules
  an IBA row that is still in its GOA file, and the genes with a kept row under a PAINT
  loss. Node listings are committed for 357 families: those whose family review disputes a
  node placement, and PTHR48034 (the CIRBP family below). A review row whose IBA has since
  been withdrawn from GOA has no tree row to quote and is not asked for one.

The file format, the numbering rules and the limits are in
[docs/phylo.md](https://github.com/ai4curation/ai-gene-review/blob/main/docs/phylo.md).

Two things the extract settles that this project had been doing by hand:

- **Seed identity.** A PANTHER leaf carries its MOD id and its UniProt accession together
  (`RAT|RGD=1565256|UniProtKB=Q4V898`), so a MOD-id seed resolves by lookup, not by name
  match. The 31,778 placed rows carry 213,504 seed tokens; 567 of them (0.3%) name no leaf
  of the tree, and every seed resolves on 31,258 rows. Arabidopsis `AGI_LocusCode` seeds
  are resolved through UniProt's locus names.
- **Residue numbering.** PANTHER's alignment rows leave out the stretches the family model
  does not align, so counting along a row does not give a position in the protein. The
  extract lays each row back onto the full-length sequence and reports positions in the
  protein's own numbering.

## What the tree says about our verdicts

`tree_evidence.py` joins each reviewed IBA row with its tree facts. Of 31,783 positive
rows in 8,224 genes, 31,778 are placed in a PANTHER 19.0 tree (the figures are of
2026-11-17, after the second merge with main). "Overruled" is `REMOVE` or
`MARK_AS_OVER_ANNOTATED`; "refined" is `MODIFY` or `TOO_GENERAL`; "kept" is `ACCEPT` or
`KEEP_AS_NON_CORE`.

### Where the gene stands relative to the seeds

| | rated | kept | refined | overruled | % overruled | % `REMOVE` |
|---|---:|---:|---:|---:|---:|---:|
| Gene is itself a seed | 15,933 | 14,361 | 1,358 | 214 | 1.3% | 0.2% |
| Inside the seed clade, with a one-to-one ortholog seed | 4,322 | 3,840 | 353 | 129 | 3.0% | 0.8% |
| Outside the seed clade, with a one-to-one ortholog seed | 2,603 | 2,197 | 180 | 226 | 8.7% | 2.4% |
| Inside the seed clade, no one-to-one ortholog seed | 5,148 | 4,001 | 494 | 653 | 12.7% | 5.6% |
| Outside the seed clade, no one-to-one ortholog seed | 3,329 | 2,336 | 289 | 704 | 21.1% | 9.9% |
| PAINT loss on the path to the gene | 22 | 8 | 4 | 10 | 45.5% | 27.3% |

The seed clade is the smallest clade that holds all the seeds of the row. A one-to-one
ortholog is a seed that joins the gene at a speciation node with no duplication and no
horizontal-transfer node on either side since. Half of all IBA rows are on a gene that is
one of the row's own seeds.

"Inside the seed clade" means less than it sounds on many rows. When the seeds bracket the
node, the seed clade is everything below the node, so every gene the row reaches is inside
it; a gene can be outside only when the term was placed above the seeds' own common
ancestor. The "inside" rows therefore mix genes that sit in a tight clade with the seeds
and genes that merely descend from a node whose seeds span it, and this table and the one
on node height below describe partly the same variable. The extract says which case a row
is: for a bracketing node it gives the number of seeds on the gene's own branch below the
node instead.

A PAINT loss can be seen only where the family has a local PAINT slice, which is so for
24,133 of the 31,778 placed rows. The last line counts rows in those families and says
nothing about the others.

### Similarity to the seeds in the family alignment

Rows where the gene is not itself a seed, by identity to the most similar seed:

| Identity | rated | overruled | % overruled | % `REMOVE` |
|---|---:|---:|---:|---:|
| under 20% | 485 | 127 | 26.2% | 19.2% |
| 20-30% | 1,644 | 349 | 21.2% | 11.1% |
| 30-40% | 2,383 | 442 | 18.5% | 8.0% |
| 40-60% | 4,075 | 429 | 10.5% | 3.7% |
| 60-80% | 2,815 | 215 | 7.6% | 2.2% |
| 80% or more | 4,016 | 160 | 4.0% | 1.0% |

### Relation of the nearest seed, and duplications on the path

Rows where the gene is not itself a seed:

| | rated | overruled | % overruled | % `REMOVE` |
|---|---:|---:|---:|---:|
| Nearest seed is an ortholog | 11,543 | 999 | 8.7% | 3.0% |
| Nearest seed is a paralog | 3,786 | 707 | 18.7% | 9.6% |
| Nearest seed is a xenolog | 92 | 16 | 17.4% | 7.6% |
| No duplication between the PAINT node and the gene | 5,549 | 463 | 8.3% | 2.8% |
| One duplication | 4,749 | 612 | 12.9% | 5.9% |
| Two duplications | 2,771 | 372 | 13.4% | 5.7% |
| Three or more | 2,373 | 275 | 11.6% | 5.4% |

### How far above the seeds the node was placed

Rows with two or more seeds, by how far the seeds' own common ancestor is below the PAINT
node:

| | rated | overruled | % overruled | % `REMOVE` |
|---|---:|---:|---:|---:|
| Seeds bracket the node | 10,065 | 497 | 4.9% | 2.1% |
| Common ancestor one step below | 3,929 | 148 | 3.8% | 1.3% |
| Two or three steps below | 5,310 | 266 | 5.0% | 2.3% |
| Four or more steps below | 5,583 | 345 | 6.2% | 2.3% |

### Reading these tables

- **The gene's own position matters; the node's height above the seeds does not.** A
  curator placing a term several nodes above the seeds' common ancestor is not, by
  itself, associated with our overruling it. What is associated is the gene lying outside
  the seed clade, having only paralogs among the seeds, or being under 40% identical to
  every seed.
- **One duplication is most of the effect.** The rate rises from 8.3% to 12.9% with the
  first duplication between the node and the gene, and further duplications add little
  (13.4% with two, 11.6% with three or more).
- **These are our verdicts, not ground truth.** The tables say where we overrule, not
  where PAINT is wrong. They are less circular than the
  [species-distance analysis](single-organism-distance.md), whose reviewers had been told
  to scrutinise deep transfers: when these verdicts were made no row cited a tree extract,
  and under 2% had any tree artifact. A reviewer can still infer paralogy from gene names
  in the seed list, so the two are not independent.
- **The species-distance analysis measured a proxy.** Its distance is the depth of the
  donor and target species' common ancestor. Two proteins from the same species can be
  paralogs across the family root, and two from different kingdoms can be one-to-one
  orthologs. The tables here use the gene tree.

## What it corrected in our own write-ups

Reading the tree for this project's own featured examples found three errors that had
stood since the examples were written.

- **Cds1, "longest branch".** The findings page, the family notes and both gene reviews
  gave the Cds1 branch's length (0.528) as the longest from the PTHR10314 root and read it
  as evidence of neo-functionalization. The five branches below the root measure 0.412,
  0.528, 0.659, 0.458 and 0.402; the threonine synthase branch is the longest. What the
  tree does show is stronger: the root is a duplication, all 19 seeds of
  `GO:0019344` sit in three of the other four branches, none is in the Cds1 branch, and
  Cds1 is 21-27% identical to them. PAINT already stops the term at the other branch
  without a seed, the threonine synthases, with an IRD at `PTN000741516` (2026-08-28);
  the Cds1 branch (`PTN008304321`) is the one seedless root branch that still inherits
  it. Both gene reviews also quoted the family notes for the
  claim with text that is not in the notes: a paraphrase, which the quote check had on its
  list of known failures.
- **CIRBP, "its own subfamily node".** The findings page, the family analysis and the gene
  review called `PTN008729690` the CIRBP/RBM3 subfamily node, and recommended that PAINT
  put an IRD there. It is the root of PTHR48034, with all 405 leaves below it and above the
  node that carries the splicing terms. The CIRBP/RBM3 branch is `PTN008483167`, a
  speciation node at Euteleostomi with 45 leaves, 14 steps below the splicing node. The
  recommendation now names it.
- **CIRBP, "rat Tra2" seeds.** `RGD:1565256` and `RGD:1306751` were described as rat Tra2.
  The PANTHER leaf ids resolve them to rat Rbmx (Q4V898) and rat Rbmxrtl (P84586), in the
  same branch as human RBMX. Rat Tra2b is not a seed.

The verdicts on these rows stand. The reasons now rest on what the tree shows, and the
three gene reviews (MYCTU and VIBCH `cds1`, human CIRBP) quote their extracts.

Review of this work then found three more, in the work itself.

- **CIRBP, quoting around the adverse fact.** The corrected CIRBP reasons said the seeds
  "all sit in one branch below" the splicing node and that "CIRBP's own branch holds none
  of them". The first branch is the one directly below the node (`PTN000391533`); the
  second is the CIRBP/RBM3 clade 14 steps further down (`PTN008483167`). At the node's own
  level every seed is in CIRBP's branch, and CIRBP is inside the clade the seeds span,
  which the extract says in the sentence between the two that were quoted. The reasons now
  state both facts and quote that sentence. The verdict rests on what does separate CIRBP
  from each seed, a duplication (`PTN009224850` for the RBMX-family seeds, `PTN004472736`
  for TRA2A and TRA2B), and on the absence of splicing evidence for CIRBP.
- **"One-to-one ortholog" across a transfer.** The extract counted a seed as a one-to-one
  ortholog whenever it joined the gene at a speciation with no duplication between, even
  with a horizontal-transfer node on the way. For SCHPO cab4 it called all six seeds of
  `GO:0004140` one-to-one orthologs; four of them (the kinase-only proteins) are separated
  from cab4 by transfer nodes at 11-16% identity. Such seeds are now counted and named
  apart. 251 rows in 138 extracts changed, 34 of which had counted such a seed as
  one-to-one.
- **An ortholog call used against a review that disputes the placement.** For DROME mam
  and SCHPO cab4 the re-read removed the failure mode `WRONG_ORTHOLOG_OR_PARALOG` because
  the tree calls the seeds orthologs. Both reviews argue that the family or subfamily
  placement is itself the artefact, and the ortholog call is read from that placement. The
  mode is back on both, and the script no longer changes failure modes.

## Rows to re-review

`tree-evidence-candidates.yaml` lists 256 rows in three groups. None is a finding that
the verdict is wrong; each is a row where the verdict and the tree pull apart and someone
should look. The file is regenerated from the current reviews, so it grows as reviews are
merged and rows leave it as they are corrected. It held 233 rows when it was first built,
and the first twelve batches of the re-read below were planned from that list.

| Group | Rows | Why it is listed |
|---|---:|---|
| PAINT loss on the path | 23 | PAINT has removed the term (IRD or IKR) between the node and the gene and not asserted it again below, so the cached IBA row is stale. We keep or refine 12 of these, which now raise `kept_under_paint_loss`. |
| Paralog claim without a duplication | 19 | Overruled as `WRONG_ORTHOLOG_OR_PARALOG`, but every seed joins the gene at a speciation and no duplication or transfer node lies between the node and the gene. In none of them is every seed a one-to-one ortholog. |
| Overruled although the gene is a seed | 214 | The gene's own experimental annotation is among the node's seeds. Either that annotation is disputed too (a seed-side error, as in the PseudoCAP sweep) or the verdict needs another look. |

Examples: yeast SSA1 to SSA4 are accepted for `GO:0042026` protein refolding while PAINT
carries an IRD for that term at the fungal node `PTN001065099` (2026-06-16), which lies on
their path as well as on that of SSB1, SSB2 and SSZ1. Either the loss is too broad or four
accepted rows are stale. SCHPO cab4 and yeast CAB4 are overruled as wrong paralogs where
every seed joins them at a speciation, four of the six across horizontal-transfer nodes.
Both reviews dispute the subfamily placement itself, so the rows are on the list as rows
to look at; the tree's relation is read from that placement and does not settle them.

When the list was first built, 1,689 overruled rows had an extract and 4 quoted it, and
392 node assessments in 219 family reviews disputed a placement, 6 of them citing a tree
listing. Now all 1,936 overruled rows have an extract and 232 quote it.

## The re-read

Between 2026-11-11 and 2026-11-16 every gene with a row on the candidate list, and every
disputed family node assessment, was read against the tree: by one agent working from a
dossier of the review's verdict next to the tree facts, checked by a second agent, and
then edited by script. The method, the plans and a record of every row are in
[tree-rereview](tree-rereview/README.md).

| | Rows read | Applied | Left for adjudication |
|---|---:|---:|---:|
| Gene reviews: the 12 batches that hold every candidate gene | 278 | 228 | 48, and 2 not read |
| Gene reviews: two further batches, as a pilot of the corrected rules | 47 | 47, one of them by hand | 0 |
| Family reviews: every disputed node assessment without a tree listing | 386 | 321, two of them by hand | 65 |

An applied row quotes its own extract or listing in `supported_by` and says in its reason
what the tree shows. The script changed no verdict. 29 rows that had been applied were
changed on main before this work was merged with it (26 at the first merge, 2 at the
second, 1 at the fourth); their edits were not carried over, and they are counted here as
left for adjudication.

Review of the first batches found four things the script should not have done, and all
four were put right on 2026-11-16 and 2026-11-17, in the rows already applied and in the
script:

- **It quoted around adverse facts.** A row could be applied with quotes that left out the
  sentence saying the gene is inside the seed clade or shares its branch with seeds. 65
  applied rows in 52 reviews had done so; each now quotes that sentence too, and a reading
  that leaves one out is no longer applied. No reason among the 65 said the opposite of
  the sentence it had left out.
- **It changed failure modes.** On six rows it removed or added a failure mode as the
  reading proposed. Two of those changes were wrong (mam and cab4, above) and are undone;
  four were checked and kept. A reading that proposes a change of failure modes now goes to
  a curator.
- **It corrected a reason and left the same claim standing elsewhere in the row.** On five
  gene rows the claim the tree contradicts was in the summary or a source note as well
  (NDUFA9, SDHAF2 twice, TK2, ADH3; and HMOX2, whose source note called rat Hmox1 an
  ortholog and labelled it Hmox2), and on four family rows the corrected reason said that
  a subfamily listed as affected holds seeds of the assertion. Those fields now agree with
  the corrected reasons, and a reading whose contradicted claim is anywhere but the reason
  goes to a curator.
- **It let an edit reach a second row.** The mam failure-mode change reached a row the
  script had refused to edit, through a YAML block the two rows share. The editor now
  refuses a shared value from either side.

Two of the unread batches (`g013` and `g014`, 47 rows in 35 genes) were then run on the
corrected rules as a pilot, reader and verifier both on Opus. Every row whose extract has
a sentence against the verdict went to the verifier (32 of the 47), and every reading
quoted the sentences it had to. The verifier faulted 3 of the 36 readings it checked, each
for a fact stated wrongly in the sentence (a miscount, two facts run together, the wrong
seed named as the one on the gene's branch), and supplied the correction each time. One
reason was corrected: ARATH LCYB `GO:0005739` said the gene is outside the clade that
inherited the function, while two seeds share its branch. The script applied 46 rows and
left one for a curator, because its contradicted claim is also in the summary and a
source note: ARATH MNS1 `GO:0036503` said that no seed of the ERAD term lies in MNS1's own
branch, and human MAN1A1 does. The two batches took 622,000 agent tokens, 311,000 a
batch, against about 275,000 before the verifier was given every such row.

Review of the pilot asked why a statement that both agents had found false should stay in
a review because of what the script may rewrite. It should not. MNS1 was corrected by
hand in all three places, with the reason the verifier had checked. So were the two
family assessments of the same kind, PTHR10048 `GO:0005944` and PTHR16675 `GO:0002476`,
each of which listed as affected a subfamily with no leaf below the node; both were
checked against the release tree first, and the second against QuickGO (human HFE does
not carry the row). `finish` now names such rows, and `needs-curator.yaml` counts them
(`contradicted_and_left`, 0 today). That count covers a reading the verifier accepted
whole. A contradiction whose drafted correction the verifier faulted is counted apart
(`contradiction_disputed`, 15 today, below).

What the re-read leaves for a curator is in
[`needs-curator.yaml`](tree-rereview/needs-curator.yaml): the rows below, and the 350
applied rows on which the reader left a note, often about a verdict or failure mode that
no longer fits.

What the readers found in the gene rows, which were chosen as the ones most likely to have
a problem:

| Reading | Rows |
|---|---:|
| The verdict rests on something the tree cannot settle, and the tree contradicts nothing the review says | 198 |
| The review states something about placement, relatedness or the seeds that the tree contradicts | 27 |
| The tree agrees with a placement argument | 26 |
| PAINT has itself removed the term on the path | 10 |
| A kept row under a PAINT loss (loss too broad 7, loss applies 6) | 13 |
| The verdict is not supported by the tree | 2 |
| Not read | 2 |

And in the family node assessments:

| Reading | Rows |
|---|---:|
| The tree agrees with the reviewer's argument about the node, its seeds or the subfamilies | 210 |
| The assessment rests on functional evidence the tree cannot settle | 115 |
| The assessment states something about the tree that the listing contradicts | 30 |
| The listing has no entry for the node or the term | 26 |
| The assessment is not supported by the tree | 5 |

Three things follow.

- **Most overrulings of an IBA are not arguments about the tree.** Seven in ten of the
  gene rows object to the term's scope, to the seed annotation itself, or to a missing
  domain, and the tree neither helps nor hurts them. For these the extract's use is to
  show that placement is not the issue, which several reviews had implied it was.
- **About one gene row in ten, and one family row in thirteen, said something about the
  tree that was wrong.** Typical cases:
  a "paralog" that the tree makes a one-to-one ortholog, a "broad" node with five leaves,
  a seed list described from gene names, a subfamily named as affected that does not
  descend from the node. 11 gene rows and 24 family rows had their reason corrected after
  the verifier agreed with the correction, and three more were corrected by hand (above);
  the rest are among the rows left for a curator.
- **Family reviewers argue from the tree more than gene reviewers, and are mostly right.**
  More than half of the disputed node assessments make a placement argument that the tree
  bears out.

113 rows are left for adjudication, each with its reason in the run records: 42 where the
verifier did not accept the reading or its correction (among them 2 verdicts the reader
found unsupported and 2 kept rows under a PAINT loss), 26 family rows whose node or term
is not in the listing, 29 rows that changed on main after they were read, 11 kept rows
under a PAINT loss, and 5 verdicts or assessments the tree does not support. Two gene
rows were not read: the reader returned no entry for them. The 29 rows that changed on
main are marked `needs_new_reading` in `needs-curator.yaml`: what their entries say
describes the review as it was read.

Fifteen of the 42 are readings of a contradiction (11 gene rows, 4 family rows). In most
of them the verifier accepted that the review states something the tree contradicts and
faulted the drafted correction: a clause that overstates, a second claim that is no
contradiction, a missing quote. No agreed text exists for these. They were also read
before the reader rules were corrected, and against extracts that have since been
regenerated, so the old drafts cannot simply be applied: they need a fresh reading under
the corrected rules, and are the first rows a curator should look at. `needs-curator.yaml`
marks them `contradiction_disputed`.

Not yet read: 59 gene batches with no candidate row, 1,370 overruled rows in 934 genes.
They still raise `missing_tree_evidence`. So do 293 overruled rows in 213 genes that
reviews merged on main have added since the plan was made. 254 disputed node assessments
are in the same position: 238 in 138 families the plan does not cover, and 16 new ones in
10 families it had read (as of the fifth merge, 2026-11-21). These have extracts and
listings but are in neither plan.

The readers of the candidate gene batches and of the first four family batches ran on the
session's model; the remaining family batches and the pilot ran on Opus. A trial of a smaller model as reader on
two batches gave the same reading on 38 of 43 rows but missed four of the five rows where
the review contradicts the tree, so it is not used.

### Residue arguments without a residue claim

The pilot met four rows overruled as `PSEUDO_OR_SUBACTIVITY_LOSS` with nothing in
`residue_claims` (ARATH CRY1 `GO:0003904`, and GID1A, GID1B and GID1C `GO:0016787`).
Counted over every gene review on 2026-11-21, with or without an extract: 175 rows in 96
reviews use the failure mode; 46 state residue claims, 16 say why the argument is not a
point-residue question, 8 are not overruled and so are not asked, and **105 rows in 65
reviews** raise `missing_residue_evidence` (84 `REMOVE`, 21 `MARK_AS_OVER_ANNOTATED`; 72
of them IBA rows). On 2026-11-18 it was 97 rows in 63 reviews; the eight more came with
reviews merged on main. They are listed in
[`residue-evidence-backlog.yaml`](residue-evidence-backlog.yaml). For 5 of them the
gene's extract already reads the family's curated sites off the alignment. These are
rows as their reviews wrote them; the re-read notes them and changes none.

## Reproduce

```bash
just fetch-panther-release                                      # once per machine
uv run python projects/IBA_REVIEW/tree_evidence.py              # tree-evidence-rows.tsv.gz
uv run python projects/IBA_REVIEW/tree_evidence.py --summary    # the tables above
uv run python projects/IBA_REVIEW/tree_evidence.py --candidates # tree-evidence-candidates.yaml
uv run python projects/IBA_REVIEW/tree_evidence.py --seed-lists # GOA seed lists against the PAINT slices
uv run python projects/IBA_REVIEW/tree_evidence.py --residue-backlog  # residue-evidence-backlog.yaml (no database needed)
```

The census of 2026-11-09 was a one-off count of committed artifacts and is not
regenerated by these commands.

## Limits

- The tree is PANTHER's reconciliation and can be wrong. A horizontal-transfer node says
  one of its branches was transferred, not which, so transfers are counted and not
  interpreted.
- "Ortholog" and "paralog" are read from the event where two leaves join. An ortholog
  with duplications since the split is an ortholog of a whole group of later paralogs,
  which is why the tables separate one-to-one orthologs. An ortholog with a
  horizontal-transfer node between it and the gene is not one-to-one either. And every
  such relation is read from the family and subfamily PANTHER placed the gene in: it does
  not answer a review that disputes that placement.
- PAINT losses are read from a family's local PAINT slice. Rows in a family without one
  carry no loss information, so the loss counts here are over the families with a slice.
- Identity and coverage are over the family model's columns. A domain the model does not
  cover is invisible.
- A seed list in a cached GOA row is a snapshot and can lag PAINT. Of the 24,133 placed
  rows whose family has a local PAINT slice, 23,514 still have an IBD row for the same
  node and term in the slice. On those the two seed lists are the same on 87.0%, differ by
  one seed on 8.7%, by two on 1.8% and by three or more on 2.5%. The other 619 rows have no
  IBD row for that node and term in the slice: PAINT has since moved or removed the
  assertion. The extract describes the seeds of the GOA row, which is what the review is
  reviewing. For Cds1 the slice of 2026-08-28 lists fly `FBgn0031148` and MYCTU `P9WP51`
  where the GOA row lists E. coli CysK and CysM; the count is 19 either way.
- Genes outside PANTHER's reference proteomes are not leaves of any tree. TreeGrafter
  rows for such genes are not covered here; see [TREEGRAFTER](../TREEGRAFTER.md).
