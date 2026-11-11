---
title: "Human Genes Re-Review: REMOVE actions"
species: [human]
---

# Re-review of REMOVE actions in human gene reviews

Back to the [project page](../HUMAN_GENES_RE_REVIEW.md). Tracked in
[#4097](https://github.com/ai4curation/ai-gene-review/issues/4097).

**Bottom line:** every annotation row with `action: REMOVE` in
`genes/human` was read again against the current review rules (November
2026). There were 23,802 such rows in 1,699 of the 3,588 human review files.
22,013 are bare `protein binding` rows, which the protein-binding policy
removes as uninformative; they were audited by script and none changed
action. The other 1,789 rows, in 820 reviews, were read one at a time.
**408 of them (23%) no longer say REMOVE**, 1,381 stand, and 64 errors in
source records were written down as structured `source_defects`. 222 review
files were edited. No row was changed to REMOVE.

The row-level record is in
[`remove_rereview_changes.yaml`](remove_rereview_changes.yaml): every changed
row with its old and new action and the rule applied, and 97 REMOVE rows
that were examined closely and left in place, each with a note. 48 of those
are marked `close_call`: a curator might decide them differently.

## Why this pass

`REMOVE` says the claim is unlikely to be correct. The first-pass reviews
also used it for things that are not that: a second row for a claim already
accepted, a true but broad term, a real observation thought unimportant, an
experimental annotation whose paper could not be read. The July sweep saw the
pattern and left it as reviewer discretion (see "Method notes" on the project
page). Since then the rules have been made explicit: a review judges claims,
not evidence codes; rows that share a term must agree; a true but broad term
is `TOO_GENERAL` or `MODIFY`; an experimental annotation is not overruled
from an abstract; ND and root organelle terms have their own policies. This
pass applies those rules to every REMOVE row.

## Method

1. All REMOVE rows were extracted from the review files. Bare `GO:0005515`
   rows were set aside for the policy audit below.
2. The 1,789 other rows were read in 25 alphabetical batches. For each row the
   reading used the term, evidence code and reference, the reviewer's summary
   and reason, the other rows of the review that carry the same term, any kept
   descendant of the term, and the cached publication with its
   `full_text_available` flag. For electronic and similarity transfers the
   donor annotation and its reference were looked up in QuickGO, and the donor
   paper's abstract was read from PubMed before anything was written about it.
3. REMOVE was kept wherever it is defensible under the rules. A row was
   changed only when the removal broke a rule, when its argument failed once
   the evidence was read, or when the reason itself conceded that the claim is
   true.
4. Edits were applied by a script that rewrites only the `review` block of the
   named row and checks that the rest of the file parses to the same content.
   Each batch was validated with `ai-gene-review validate` against a baseline
   taken before the pass, and all 222 edited files were validated together
   once more at the end: all are valid and no new error was introduced. Two of
   them (FZD7, GK5) had failed before the pass on three reference quotes that
   were not verbatim; those quotes were re-quoted from the cached papers.
5. The checks that CI runs on changed gene reviews were then run on the whole
   set: the PMID-reference check, the repository-wide quote check and the
   family/gene cross-check (`just validate-families`). The cross-check found
   one disagreement with a curated family review: `extracellular matrix` had
   been kept as non-core on PRG2 and PRG3 from two matrix proteomics studies,
   while the review of their PANTHER family (PTHR22803) scopes that term as
   not applicable to any member. Those four rows are
   `MARK_AS_OVER_ANNOTATED`: the detection is real, the location is not
   retained.

## Results

| Outcome for the 1,789 substantive REMOVE rows | Rows |
|---|---|
| REMOVE stands | 1,381 |
| → `MARK_AS_OVER_ANNOTATED` | 178 |
| → `KEEP_AS_NON_CORE` | 121 |
| → `TOO_GENERAL` | 30 |
| → `UNDECIDED` | 34 |
| → `ACCEPT` | 26 |
| → `MODIFY` | 19 |

Nine of the rows that stay REMOVE had a wrong or missing reason and were given
a correct one. One row that was not REMOVE was changed as well, so that the
rows of a re-adjudicated term agree: the electronic centriole row of HSPA1B,
from `MARK_AS_OVER_ANNOTATED` to `ACCEPT`.

The share of rows that changed depends strongly on the evidence code. Removals
of phylogenetic annotations, where the first-pass reviews argued at the PAINT
node, almost all stand. Removals of proteomics observations almost all fell.

| Evidence | REMOVE rows at start | Changed | Share |
|---|---|---|---|
| IEA | 669 | 165 | 25% |
| TAS | 310 | 57 | 18% |
| IDA | 215 | 54 | 25% |
| IBA | 216 | 7 | 3% |
| ISS | 109 | 31 | 28% |
| NAS | 93 | 7 | 8% |
| IMP | 55 | 15 | 27% |
| HDA | 45 | 39 | 87% |
| IPI (not bare protein binding) | 35 | 23 | 66% |
| IEP | 12 | 5 | 42% |
| ND | 11 | 0 | 0% |
| other (EXP, IGI, RCA, IC, HTP, HEP) | 19 | 5 | 26% |

### Rules applied

Counts are rows. The rule names are the keys used in the data file.

| Rule | MARK | KEEP | TOO_GENERAL | UNDECIDED | ACCEPT | MODIFY | Total |
|---|---|---|---|---|---|---|---|
| same-term-kept | 22 | 9 | | 2 | 23 | 4 | 60 |
| ancestor-of-kept | 1 | 1 | 30 | | 1 | | 33 |
| reason-concedes-truth, true-but-broad | 10 | 27 | | | | | 37 |
| general-to-specific, lateral-correction | | | | | | 15 | 15 |
| claim-established | | 52 | | | 2 | | 54 |
| electronic-unsupported-plausible, downstream-readout | 65 | | | | | | 65 |
| experimental-incomplete-evidence, experimental-fulltext-supports | 6 | 4 | | 29 | | | 39 |
| curated-statement | 6 | | | 2 | | | 8 |
| omics-location, omics-function | 45 | 3 | | | | | 48 |
| expression-only | 8 | | | | | | 8 |
| reactome-location, er-transit, organelle-root | 11 | 25 | | | | | 36 |
| other (cross-gene consistency, IBA node, promiscuous activity) | 4 | | | 1 | | | 5 |

What the main rules mean in practice:

- **Same term kept elsewhere (60 rows).** The review accepted or kept the term
  on one row and removed it on another, usually because the second row's
  reference was weaker. The row now takes its sibling's action, and a problem
  with its own reference is recorded as a source defect. Examples: AADAC
  serine hydrolase activity, ATF3 activator rows, WT1 positive regulation of
  transcription, FADD identical protein binding.
- **Ancestor of a kept term (33 rows).** A positive annotation entails its
  ancestors, so removing the broad term while keeping the specific one
  contradicts itself. These are now `TOO_GENERAL`. Example: TP53 cell
  population proliferation beside the kept neuroblast, glial cell and T cell
  proliferation rows.
- **Claims with an experimental basis elsewhere (119 rows, 105 of them IEA or
  ISS transfers).** Many Ensembl Compara and ISS rows were removed with "no
  evidence" although the mouse or rat donor annotation comes from a targeted
  experiment. Where that experiment
  establishes the claim the row is `KEEP_AS_NON_CORE` (TRAF6 lipid droplet,
  from the Viperin study; USO1 in insulin-stimulated GLUT4 translocation; UMPS
  in UDP and CTP synthesis). Where it over-reads a phenotype or a downstream
  consequence the row is `MARK_AS_OVER_ANNOTATED` (TP53 response to salt
  stress; TOMM70 negative regulation of cell growth). Where the donor
  annotation is itself on the wrong gene or uses the wrong term, REMOVE stands.
  A row is kept on donor evidence only when the donor paper, read as full text
  or abstract, shows the claim; each such row quotes it.
- **Rows judged without the full text (36 rows).** Removal of an IDA, IMP or
  IPI row whose paper was available only as an abstract, or of a transfer
  whose experimental donor paper could not be read or does not show the claim
  in its abstract, is now `UNDECIDED`, or the row is kept where the function is
  clearly correct for the gene. In three
  further rows the cached full text supports the annotation. Examples: ASCL1 negative regulation of neuron differentiation, VTI1A,
  several SIRT1 rows. Explicit contradictions in the abstract (wrong sign,
  wrong enzyme class) still support REMOVE.
- **Omics observations (48 rows).** A protein seen in an exosome, membrane or
  nuclear proteome, or pulled down in the E-cadherin or RNA interactome, was
  observed. Without a positive contradiction that is an over-annotation, not a
  false claim. Such a row is `KEEP_AS_NON_CORE` only when at least two
  independent studies find the protein there or a mechanism explains its
  presence; only the three exosome rows of CHMP1B, an ESCRT-III subunit found
  in three exosome proteomes, meet that test. A single proteome hit is marked. REMOVE stands where the location is topologically impossible
  for the protein (GCNT1, LRRC32, SCN1A and SYVN1 in nucleoplasm or nuclear
  bodies).
- **Reactome locations (36 rows with the organelle rows).** TRAF6 carried 21
  endosome membrane rows whose reasons addressed an unrelated claim; the
  Reactome reactions are steps of endosomal Toll-like receptor signalling and
  the rows are now `KEEP_AS_NON_CORE`, as for IRAK4.
- **MODIFY (19 rows).** Where the reason named the right term, the row is
  redirected to it: TXN to protein-disulfide reductase activity, TP53 to the
  negative regulation terms for fibroblast and stem cell proliferation, WT1 to
  retina development in camera-type eye, GAPDH ribonucleoprotein complex to
  GAIT complex.
- **Twin genes and complex subunits.** HSPA1B now mirrors HSPA1A, and SDHA,
  SDHB and SDHC mirror SDHD.

### What REMOVE means in the human set now

The 1,381 rows that stand are removals of the claim itself: an annotation on
the wrong gene product or from a symbol collision; a substrate, cargo or
stimulus annotated as a participant; a pseudoenzyme given the ancestral
activity; a sign error or the wrong enzyme class; an electronic mapping that
is wrong for this family member or this taxon; a phylogenetic annotation
argued against at its node; a Reactome placement that is biologically wrong;
a direct contradiction in the cited paper. All 12 removed NOT rows and all 11
removed ND rows were checked against the NOT and ND rules and stand.

Eight REMOVE rows still share a term with a kept row (ABCD4, ACTG2, CKB,
CSDE1, CXCR3, LPCAT4 twice, TLR2). Each was checked: the kept row is a
`MODIFY` that redirects an experiment to another term, a `located_in` row
beside a removed `is_active_in` row, or an `UNDECIDED` row beside accepted NOT
rows. Both actions agree that the stated claim is wrong.

## Corrections after review

The pull request for this pass
([ai4curation/ai-gene-review#6257](https://github.com/ai4curation/ai-gene-review/pull/6257))
was checked against the steps CI runs and was reviewed. That produced a
second round of changes, all included in the numbers above.

- **Family cross-check.** PRG2 and PRG3 had kept `extracellular matrix`, which
  the review of their PANTHER family scopes as not applicable; the four rows
  are `MARK_AS_OVER_ANNOTATED` (Method, step 5).
- **Prediction reviews.** The BioReason prediction review of GAPDH had
  classed four predicted terms as refuted because the gene review removed
  them. With the terms kept, the deterministic repair
  (`scripts/auto_review_sft_predictions.py`) returns them to correct but not
  novel.
- **Analysis lost in a rewrite.** The two ADGRA2 GPCR rows had carried an
  earlier reviewer's reference-level analysis (78 annotations from one survey
  over 27 entities, reproducible with `ADGRA2-bioinformatics/projection_test.py`).
  The rewritten reasons had dropped it and the sibling membrane row still
  called the two rows removed. The analysis is restored, the defect of the
  evidence code is recorded as a source defect, and the sibling row is
  corrected. The 418 rewritten reasons were then screened against the text
  they replaced, by the identifiers each had cited and by reading the 65
  longest or most detailed earlier reasons in full; no other row had lost
  analysis of this kind.
- **Summaries.** Twenty-one rows moved to a positive action still had a
  summary that argued against the claim; the summaries now match.
- **Evidence for kept rows.** Every paper cited in a rewritten reason is now
  in the review's `references` (93 entries in 71 reviews) and in
  `publications/` (67 fetched). Fifty-four rows kept, accepted or refined on
  the strength of a paper now quote it. Five rows whose donor paper is available
  only as an abstract that does not show the claim moved to `UNDECIDED`
  (INTU cell division, two rows; SCN1A Z disc, two rows; GDPD2
  lamellipodium), and two single-hit exosome rows (BAX, RASAL3) moved to
  `MARK_AS_OVER_ANNOTATED`.

## Earlier fence cases, now resolved

The project page listed four fence cases and two literature questions.

- **GAPDH**: 13 removed rows are no longer REMOVE. The GAIT-complex rows for
  negative regulation of translation are `ACCEPT`, ribonucleoprotein complex is
  refined to GAIT complex, nine moonlighting rows (interferon response,
  microtubule, S-nitrosylation, neuronal apoptosis and others) are
  `KEEP_AS_NON_CORE`, and lipid droplet is `MARK_AS_OVER_ANNOTATED`. NADP
  binding stays removed, with a corrected reason.
- **HSPA1B**: its own direct-assay chaperone rows are restored (ATP hydrolysis
  activity, protein refolding, cellular response to heat, centriole, negative
  regulation of inclusion body assembly as `ACCEPT`; unfolded protein binding
  as `MODIFY` to protein folding chaperone). Four rows in HSPA1A were changed
  with them so that the twin genes agree.
- **ATF3**: the activator rows (IDA) and the repressor row (TAS) are `ACCEPT`.
- **ASCL1**: negative regulation of neuron differentiation (IDA and IEA) is
  `UNDECIDED` until the source paper is read in full.
- **ATP23**: the DNA-PK complex and non-homologous end joining rows from its
  former identity as KUB3 are `MARK_AS_OVER_ANNOTATED`. DNA-dependent protein
  kinase activity stays removed.
- **AGO3, AGR2**: the removed NOT rows stand. Each negative is contradicted by
  later direct evidence.

## Source defects

When a row is wrong because the source record is wrong, the action says what
this repository does with the claim and `review.source_defects` says what the
source should fix. 64 defects were recorded on rows examined in this pass,
and one more on a sibling row of ADGRA2.

| Type | Count |
|---|---|
| WRONG_GENE_PRODUCT | 40 |
| WRONG_TERM | 12 |
| WRONG_REFERENCE | 7 |
| WRONG_WITH_FROM | 2 |
| WRONG_EVIDENCE_CODE | 3 |

By responsible resource: UniProt 33, MGI 12, ARUK-UCL 2, ComplexPortal 2,
IntAct 1, RGD 1, GO Central 1, and 12 assigned by groups the schema does not
list. 28 are marked CONFIRMED, 33 PROBABLE and 3 SUSPECTED. Examples:

- TOLLIP phosphorylation (IDA) cites a 1976 clinical report on lymphoma.
- ADGRA2 carries three TAS rows from a repertoire survey that gives 27
  entities, two of them pseudogenes, the same three terms: a bulk import
  under an author-statement code.
- CRY2 extracellular region and phosphate transport rows cite the paper that
  cloned stanniocalcin-2.
- EFEMP1 eye-development rows come from a study of fibrillin-3 (FBN3), not
  fibulin-3.
- ARPP19 rows from the alpha-endosulfine paper belong to ENSA.
- SREBF2 carries a row from a paper on SRBP-2, an unrelated protein of 206
  residues.
- HNF1A photoreceptor outer segment is transferred from the mouse ortholog,
  which was annotated from a study of Lef1 and Tcf1 mutants in which Tcf1 is
  T cell factor 1, not the hepatic factor once given the same symbol.
- COP1 Golgi membrane is transferred from the rat ortholog, which was
  annotated from a paper on COPI (coatomer) vesicles.

`just export-source-defects` turns these into per-resource reports.

## Protein binding audit

The 22,013 bare `protein binding` REMOVE rows (1,234 reviews; 22,009 IPI, 3
IDA, 1 ISS; none negated) were checked by script rather than read one by one,
because the policy removes the term whatever the evidence. The checks looked
for rows that are not what the policy covers. They flagged 255 rows whose text
questions the interaction itself and 100 rows whose text names a specific
binding term that the review does not assert; these were screened and the
distinct cases among them read. No action changed. Two rows
whose interactor is the wrong gene product (CALCA, TFAP2A) received source
defects, and 66 templated summaries in STAT3 that cited the wrong GO id for
protein kinase binding were corrected. 78 of these rows have no `reason`; the
policy is the reason, and they were left as they are.

## Follow-ups

- **UNDECIDED rows need full text.** Of the 34 rows moved to `UNDECIDED`, 16
  are experimental or author-statement annotations whose papers could not be
  read here, and 17 are electronic or similarity transfers that rest on such
  papers. Each reason states the question the full text must answer. The
  last is a phylogenetic annotation (SCGB2A2, androgen receptor signaling
  pathway) whose PAINT node has not been examined.
- **Source defects beyond this pass.** A text scan finds about 160 further
  REMOVE rows whose reasons read like a source error (wrong gene, substrate annotated as
  enzyme, wrong InterPro2GO mapping) without a structured defect. Only cases
  verified from the paper or the abstract were structured here.
- **Rows kept beside the ones changed.** The pass covered REMOVE rows only. A
  few inconsistencies among kept rows were seen and left: the TOMM40
  mitochondrion rows are `MARK_AS_OVER_ANNOTATED` against the organelle
  policy, and the ZP3 immune-response transfers from an immunization study are
  marked while the transcription transfers from the same study are removed.
- **Other organisms.** The same patterns are likely in the mouse and model
  organism reviews, which were not touched.
