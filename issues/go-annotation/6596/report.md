# go-annotation 6596 shadow rating report

## The issue

An SGD curator reported that the PAINT IBD at PANTHER node
PTN000122012 (PTHR11117, the succinate/malate-CoA ligase alpha-subunit family)
propagates `GO:0004776` succinate-CoA ligase (GDP-forming) activity to the *S.
cerevisiae* alpha subunit LSC1 (UniProtKB:P53598), when the purified yeast
enzyme is ATP-specific (PMID:9874242) and SGD annotates the ADP-forming
activity (`GO:0004775`) instead. The report also noted a 2017 precedent
(go-annotation 1423) for the same wrong term on the *S. pombe* orthologue
SPCC1620.08, fixed back then via a UniProt family-wide correction. This is a
`PAINT_IBA` issue: one node's IBD is questioned for one or more taxa.

## Approach taken

The worker (`claude-opus-5-5`) worked `BLIND` (opening post only). It was not
a cold start: `prior_work` records that a YeastPathways module PR had already
set `REMOVE` on the LSC1 row (without naming the issue) and that the
PTHR11117 family review already carried this node at `UNRESOLVED`;
`saw_prior_work: true` confirms the worker read both before concluding. Given
that, the worker's independent contribution is the reasoning and evidence
layered on top, not the bottom-line call.

The worker read the PAINT data for both the alpha family (PTHR11117) and the
partner beta family (PTHR11815), the PANTHER tree, QuickGO annotations for
seeds and recipients, and five abstract-only publications. It produced:
`genes/yeast/LSC1/LSC1-ai-review.yaml` (added a `reason` with the beta-subunit
mechanism and two new references), `interpro/panther/PTHR11117/PTHR11117-review.yaml`
(node assessment `UNRESOLVED` -> `NEEDS_PRUNING`, with reasoning and quotes),
and a history record. (The `member_exceptions` block now in the family review
and the `SPAC16E8.17c` gene review's `REMOVE` were added later by code
review, not by this worker; I rated only what `issue.yaml`'s `shadow` block
records as the worker's own proposal.)

## What upstream did

Read via `ai-gene-review shadow-issues show 6596` (`thread.jsonl`,
`comment:5947943682`): the PAINT curator (role: PAINT curator) agreed the call
was wrong, "especially created a **NOT** primary annotation for P53598 based
on PMID:9874242," and separately reviewed the whole family to add
`CONTRIBUTES_TO` qualifiers that were missing. The issue was closed the same
day (2026-10-02).

Checked downstream (QuickGO annotation search, all `checked_at: 2026-11-11`):

- `UniProtKB:P53598`, `GO:0004776`: one row, `enables ... IBA GO_REF:0000033
  GO_Central 20260528`, no `NOT` qualifier, no date later than the pre-fix
  release. The curator's fix is not yet visible in the public snapshot --
  release lag, not a wrong fix.
- `UniProtKB:O13750` (SPAC16E8.17c, the *S. pombe* alpha orthologue the
  worker also flagged): same unqualified `enables GO:0004776` IBA row,
  unchanged. The curator's fix was scoped to P53598 alone and never reached
  this gene.
- `UniProtKB:O94415` (SPCC1620.08, the *S. pombe* beta subunit): carries only
  `GO:0004775`, confirming the worker's correction that the 2017 precedent
  concerned the beta gene, not an alpha orthologue.
- IBA recipients of `GO:0004776` under `PTN000122012` with evidence code
  `ECO:0000318`: 178 total; counting fungal taxon ids among them gives
  roughly 18, matching the worker's "19 IBA recipients" figure for the Fungi
  clade (`PTN000874203`) closely enough to credit the claim.

## Rating

- **outcome: PARTIAL.** Core diagnosis matches; the applied fix is narrower
  in scope than what was proposed, and the matched part is not yet
  release-confirmed.
- **triage: AGREE.** Correctly scoped as `PAINT_IBA`.
- **diagnosis: AGREE.** Same conclusion as the curator (ATP not GTP for
  yeast SCS, PMID:9874242), with an added, verified mechanism (nucleotide
  specificity sits in the beta subunit: PMID:10353839, PMID:9765291) the
  curator's comment does not spell out. All three quotes and the two PAINT
  TSV line quotes verify verbatim (`validate-quotes`: 4/4 verified, 0
  failures).
- **actions: PARTIAL.** The `REMOVE` on P53598 matches the curator's actual
  fix in substance. The `ADD` (IKR NOT at the Fungi node PTN000874203) and
  the `REMOVE` on O13750 are not what the curator did -- the real fix was a
  point annotation on one sequence, not a node-level correction -- even
  though downstream data (above) now shows both of those proposals are
  independently correct and still needed.
- **downstream: PARTIAL.** The one item that does match (P53598) is not yet
  visible in released data (release lag). The broader, also-correct
  proposals (Fungi node, O13750) have no matching released change at all,
  because the curator never acted on them.
- **added_value: SUBSTANTIAL.** The worker found, and I independently
  confirmed, that the curator's fix leaves roughly 18 other Fungi recipients
  -- including the directly analogous *S. pombe* alpha subunit O13750 -- with
  the same uncorrected error. It also caught and corrected a factual slip in
  the issue's own framing (2017's SPCC1620.08 is the beta gene, not an alpha
  orthologue), verified independently via SPCC1620.08's current annotations.
  Both points are genuine, checkable gaps the curator's response does not
  address, not speculation.
- **harm: NONE.** The Fungi-wide NOT recommendation rests on the same logic
  PAINT already applies to the beta family (PTHR11815's IKR NOT on the
  reciprocal term), and the one acknowledged uncertainty (Viridiplantae, and
  the other 17 fungal recipients not reviewed individually) was left as
  `FLAG_FOR_CHECK` rather than acted on.

## What the worker got right, what it missed

Right: the core biochemistry, the mechanistic explanation, the quantitative
scope of the problem (Fungi-wide, not LSC1-only), and the S. pombe
beta-vs-alpha correction -- all independently verifiable and verified here.
Missed/left open: it did not check plant (Viridiplantae) nucleotide
specificity before flagging it, did not individually review the other 17
fungal recipients, and (reasonably) could not have known the curator would
fix only the single reported sequence rather than the node. No claim here was
refuted.

## Confounds

- `prior_work: COVERS_SUBJECT` on both work products: a YeastPathways module
  PR had already set `REMOVE` on the LSC1 row, and the family review already
  had this node at `UNRESOLVED`, before the shadow work started.
  `saw_prior_work: true` is recorded. This is not a cold diagnosis, but the
  mechanistic citations, the Fungi-wide quantitative check, and the S.
  pombe beta/alpha correction are the worker's own addition on top of that
  starting point.
- RETROSPECTIVE study; the opening post itself names the gene, term and
  node, so triage was not a disposition-blind call, but the literature
  synthesis behind the diagnosis still had to be done for real.
- `self_rating_seen: NEVER` -- `self-rating.yaml` was not opened at any
  point before or during scoring, and no git history on `rating.yaml`,
  `report.md` or `issue.yaml`, PR 6220, or `history/` records mentioning 6596
  were consulted.

## Lessons

A curator's "fixed" comment on a PAINT issue can mean a point annotation on
the one reported sequence, even when the root cause (and the reporter's own
2017 precedent) is family- or clade-wide. The resolution record here captures
that distinction explicitly rather than treating "closed, completed" as full
resolution of the underlying node problem; `downstream: PARTIAL` plus the
`resolution.evidence` GOA_DIFF checks make the gap re-checkable after the
next PAINT/GOA release.

## Cost

`shadow.started_at` 2026-11-10T01:46:36Z to `completed_at` 02:00:00Z: about
13.5 minutes of wall time for the worker run. Token cost not recorded.
