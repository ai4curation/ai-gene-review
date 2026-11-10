# go-annotation 6596 shadow report

**Outcome: CONCORDANT.** A blind worker agreed with the curator that the PAINT
IBA of GO:0004776 succinate-CoA ligase (GDP-forming) activity on yeast LSC1
(UniProtKB:P53598) is wrong. It traced the error to where the term sits in the
PANTHER tree, and found a small error in the issue itself. Rated 2026-11-10.
A published copy of an earlier version of this report is at `report_url` in
`rating.yaml`; this file is the record.

## The issue

An SGD curator reported that node PTN000122012, the root of the alpha-subunit
family PTHR11117, propagates GDP-forming activity to LSC1 (IBA made
2026-05-28), although the yeast enzyme uses ATP only (PMID:9874242). SGD
annotates the ADP-forming activity, GO:0004775. The issue recalls a 2017 case in
which the same wrong term reached the *S. pombe* orthologue through EC2GO.
Kind: PAINT_IBA, in scope.

## Approach

- **Blinding.** BLIND: the worker read only the opening post
  (`just show-shadow-issue 6596 --opening-only`), not the thread, the upstream
  issue, linked ontology work, or this repo's history about the issue.
- **Prior work.** The repo's LSC1 review already marked this row REMOVE
  (YeastPathways module PR d77f71b566, 2026-10-16, after the issue closed and
  without naming it), and the PTHR11117 family review had the node assessment
  UNRESOLVED (eb207ae287). The worker read both (`saw_prior_work: true`).
- **Investigation.** What the term asserts and which subunit decides it; PAINT
  data for both subunit families (PTHR11117 alpha, PTHR11815 beta); the PANTHER
  19 tree; the seeds' own evidence and the recipients in QuickGO; five abstracts.
- **Work products.** A reason with the beta-subunit evidence on the LSC1 REMOVE
  row (`genes/yeast/LSC1/LSC1-ai-review.yaml`); the PTHR11117 node verdict moved
  from UNRESOLVED to NEEDS_PRUNING
  (`interpro/panther/PTHR11117/PTHR11117-review.yaml`); the shadow record in
  this folder.

## The worker's diagnosis

Nucleotide specificity is set by the beta subunit: its nucleotide site is in the
beta subunit's N-terminal domain (PMID:10353839), and animal ATP- and
GTP-specific enzymes share one alpha subunit and differ in the beta
(PMID:9765291). PAINT models this correctly in the beta family, where the
GDP-forming IBD sits only on the GTP-specific clade PTN000929335. In the alpha
family the term sits at the root, so it reaches every lineage, including Fungi
(PTN000874203, 19 IBA recipients), whose only beta subunit is ADP-forming.

Proposed: REMOVE GO:0004776 on LSC1, keeping GO:0004775; add an IKR NOT for
GO:0004776 at the Fungi node; flag plants (PTN000122078, 66 recipients) for a
curator's check. It also found that the 2017 precedent's gene, SPCC1620.08, is
the *S. pombe* beta subunit; the alpha orthologue SPAC16E8.17c (O13750) carries
the same IBA today.

## What upstream did

The PAINT curator agreed and closed the issue on 2026-10-02 (thread record
`comment:5947943682`). They made a NOT primary annotation for GO:0004776 on
P53598 from PMID:9874242, and re-reviewed the whole PTHR11117 annotation set,
adding the `contributes_to` qualifier most rows lacked. The thread does not say
whether a NOT was placed at a Fungi node.

None of this is in released data yet. On 2026-11-10, QuickGO and the GO API
still showed the IBA from PTN000122012 on both P53598 and O13750 and no NOT
row. PAINT changes reach GOA only with a PANTHER or GO release, so this is
release lag.

## Rating

| Dimension | Score | Reason |
|---|---|---|
| Triage | AGREE | In scope, PAINT_IBA. Weak evidence: the title and the label-derived `suggested_kind` both gave the kind away. |
| Diagnosis | AGREE | Same problem, from the same paper. |
| Actions | PARTIAL | REMOVE has the same effect as the curator's NOT. The Fungi-node NOT cannot be checked against the thread. The `contributes_to` fix was noticed but not proposed. |
| Downstream | PENDING_RELEASE | Not yet released; re-rate after the next release. |
| Added value | SOME | The precedent's subunit error, and the root-placement cause; both verified. |
| Harm | NONE | The Fungi-wide NOT extrapolates from two species but is well founded; plants were left open. |

## Right, missed, refuted

- **Right.** The LSC1 annotation is wrong, for the curator's reason; the cause
  is the term's placement at the alpha-family root; SPCC1620.08 is the
  *S. pombe* beta subunit (O94415) and SPAC16E8.17c the alpha, carrying the
  same IBA; both yeasts have a single beta subunit (UniProt).
- **Missed.** The family-wide `contributes_to` fix; plant and protist clades;
  the 17 other fungal recipients.
- **Refuted.** Nothing. The three key quotes are verbatim in the cached
  abstracts (PMID:9874242, PMID:10353839, PMID:9765291).

## Confounds

- **Not independent of the repo.** The repo already said REMOVE before the
  worker started, and the worker read it. This run is partly a confirmation.
- **Weak rater independence.** The rater ran on the same model as the worker
  (`SAME_MODEL_SEPARATE_RUN`), in a separate subagent launched by the same
  coordinator session. It saw the end of the worker's self-rating only after
  scoring (`self_rating_seen: AFTER_SCORING`).
- **Triage is circular for backfilled issues.** The label-derived hint matched
  the kind. Retrospective stubs no longer carry that hint.

## Follow-up from review

The PR review found the NEEDS_PRUNING verdict was not machine-checkable and the
*S. pombe* row was left at MARK_AS_OVER_ANNOTATED. Both are fixed: PTHR11117
now has a GO:0004776 term assessment with LSC1 and SPAC16E8.17c as member
exceptions (pruned node PTN000122012, lost in PTN000874203), which the
family/gene cross-check enforces, and the SPAC16E8.17c row is REMOVE.

## Cost

| Step | Agent | Tokens | Wall time | Tool calls |
|---|---|---|---|---|
| Shadow work | claude-opus-5-5 worker | 147,016 | 13 min 52 s | 63 |
| Rating | claude-opus-5-5 rater | 98,440 | 2 min 16 s | 14 |
