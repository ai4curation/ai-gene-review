---
title: "SynGO Annotation Provenance"
maturity: SCOPING
tags: [EVALUATION, PIPELINE]
species: [human, rat, mouse]
genes:
  - GRIN1
  - GRIN2A
  - GRIN2B
  - GRIN2D
  - GRIN3B
  - GRIA1
  - GRIA4
  - CHRNA1
  - CHRNB1
  - CHRND
  - CHRNE
description: >-
  Audit of GO annotations contributed by SynGO: which species and cell system each
  experimental row rests on, and whether the term matches the paper.
---

# SynGO Annotation Provenance

SynGO (PMID:31171447) is an expert-curated synapse knowledge base that contributes GO
annotations to GOA. Reviews in this repository have met SynGO rows repeatedly, mostly as
sound location annotations, but the NMDA receptor reviews (GRIN1, GRIN2A, GRIN2B, GRIN3A,
GRIN3B, GRIN2C, GRIN2D) turned up rows where the function term does not belong to the
gene that carries it. This project sets out to measure how often that happens and to
report confirmed cases to SynGO in one batch.

## The species convention is documented, not an error

Many SynGO rows on human genes carry IDA or IMP evidence from rat or mouse experiments.
That is SynGO's stated method:

> "For any given study, annotations were made for the species used and these were
> subsequently mapped to the consensus human ortholog using HUGO Gene Nomenclature
> Committee (HGNC) data resource" (PMID:31171447)

GO's own guidance would record such a transfer as ISO. This is a single convention
question for SynGO and the GO Consortium, not a per-row defect, and reviews should not
file `WRONG_EVIDENCE_CODE` source defects for it row by row. Reviews that did so have
removed them (the in-progress GRIN3B review).

## Inventory

`SYNGO_PROVENANCE/syngo_inventory.py` reads every committed `*-goa.tsv`, keeps rows
assigned by SynGO, and joins each to its review action. Output:
[`SYNGO_PROVENANCE/data/syngo_rows.yaml`](SYNGO_PROVENANCE/data/syngo_rows.yaml).
Run on `main` as of 2026-11-15:

| Measure | Count |
|---|---|
| SynGO rows | 558 |
| Genes | 104 |
| Rows by taxon | rat 230, mouse 161, human 130, fly 21, worm 16 |
| Human rows by evidence | IDA 60, IMP 51, NAS 9, EXP 5, IEP 5 |
| Review actions | KEEP_AS_NON_CORE 325, ACCEPT 173, MODIFY 31, UNDECIDED 21, MARK_AS_OVER_ANNOTATED 8 |

Every SynGO row on `main` has been reviewed, and none has been removed. The GRIN2B,
GRIN2D, GRIN3A and GRIN3B reviews are not yet on `main`, so their rows are not counted.

## Cases found so far

All three concern `GO:0099507` (ligand-gated monoatomic ion channel activity involved in
regulation of presynaptic membrane potential).

1. **GRIN2B, PMID:19666514.** Full text read. The presynaptic NMDA receptor function the
   paper reports is attributed to GluN2A-containing receptors. A reference-level QuickGO
   view (2026-11-15) shows SynGO gave this paper's `GO:0099507` to rat Grin1 and rat
   Grin2a, and only location terms to rat Grin2b; the three human GRIN2B rows (IDA, IMP,
   NAS) are the only GluN2B function rows from the paper, and human GRIN2A has none. This
   looks like a mapping slip on one gene, not a family-wide practice. Recorded as a
   CONFIRMED `WRONG_GENE_PRODUCT` defect in the GRIN2B review (PR #6368).
2. **GRIN3B, PMID:22564863.** A channel-block study of rat subunits expressed in oocytes, with no
   presynaptic content in the abstract. Full text not yet read; a query at most.
3. **GRIN2D, PMID:8886398.** A HEK293 study; noted during the GRIN2D review, not yet
   verified against the paper.

Other human `GO:0099507` / `GO:1904315` SynGO rows on `main` (GRIA1, GRIA4, CHRNA1,
CHRNB1, CHRND, CHRNE) were already reviewed as MODIFY or UNDECIDED; they are the next
sample.

## Plan

- [ ] Sample the 111 human IDA/IMP SynGO rows: record the species and cell system of each
  paper (neurons, heterologous cells, oocytes), from the cached abstract and full text.
- [ ] For every `GO:0099507` and `GO:1904315` row, check that the paper assays the
  annotated subunit and a presynaptic (or postsynaptic) context.
- [ ] For each suspected case, run the reference-level check (how SynGO annotated the
  whole paper) before recording a defect, as for PMID:19666514.
- [ ] Re-run the inventory once the GRIN reviews merge.
- [ ] Export confirmed defects (`just export-source-defects`) and send one report to
  SynGO, with the ISO convention raised as a separate question.
