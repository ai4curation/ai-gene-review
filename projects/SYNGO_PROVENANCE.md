---
title: "SynGO Annotation Provenance"
maturity: SCOPING
tags: [EVALUATION, PIPELINE]
species: [human, rat, mouse]
genes:
  - GRIN1
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

Whether experimental codes should carry over to the human ortholog, or the transfer be
coded ISO (inferred from sequence orthology; see the
[GO evidence code guide](https://geneontology.org/docs/guide-go-evidence-codes/)), is a
single convention question for SynGO and the GO Consortium, not a per-row defect, and reviews should not
file `WRONG_EVIDENCE_CODE` source defects for it row by row. Reviews that did so have
removed them (the in-progress GRIN3B review).

## Inventory

`SYNGO_PROVENANCE/syngo_inventory.py` reads every committed `*-goa.tsv`, keeps rows
assigned by SynGO, and joins each to its review actions. Output:
[`SYNGO_PROVENANCE/data/syngo_rows.yaml`](SYNGO_PROVENANCE/data/syngo_rows.yaml).
It counts two units. A **row** is one GOA line. A **claim** is one gene, term, qualifier
and paper: SynGO usually files one assertion as an IDA + IMP (+ NAS) set on the same paper,
so rows overstate claims by about two to one. Run on `main` as of 2026-11-15:

| Measure | Rows | Claims |
|---|---|---|
| SynGO annotations | 558 | 300 |
| Genes | 104 | 104 |
| By taxon | rat 230, mouse 161, human 130, fly 21, worm 16 | rat 132, mouse 89, human 60, fly 11, worm 8 |
| Human, by evidence (rows) | IDA 60, IMP 51, NAS 9, EXP 5, IEP 5 | 60 human claims carry experimental evidence |
| Review actions (rows) | KEEP_AS_NON_CORE 325, ACCEPT 173, MODIFY 31, UNDECIDED 21, MARK_AS_OVER_ANNOTATED 8 | |

Every SynGO row on `main` has been reviewed, and none has been removed. The GRIN2B,
GRIN2D, GRIN3A and GRIN3B reviews are not yet on `main`, so their rows are not counted.

## Cases found so far

All three concern `GO:0099507` (ligand-gated monoatomic ion channel activity involved in
regulation of presynaptic membrane potential). Each SynGO claim below arrives as an IDA,
IMP and NAS triple on the same paper: one claim, three rows.

The reference-level views come from
[`SYNGO_PROVENANCE/reference_level.py`](SYNGO_PROVENANCE/reference_level.py), which
queries the QuickGO annotation API for every SynGO row citing a paper and writes the
query URL, retrieval date and a sorted table to `SYNGO_PROVENANCE/data/reference_level/`.

1. **GRIN2B, PMID:19666514 — confirmed wrong subunit.** The cached abstract already names
   the subunit ("the kinetics of the NR2A subunits expressed by parallel fibers implement
   a high-pass filter plasticity rule"). The full text, read from a PDF supplied by the
   project owner, adds that an NR2B-selective antagonist did not prevent the LTD. The cache
   is abstract-only, so the GRIN2B review (PR #6368) records those full-text quotes in
   `supporting_text_fulltext`, which the verbatim check does not test. The reference-level
   view ([`PMID_19666514.yaml`](SYNGO_PROVENANCE/data/reference_level/PMID_19666514.yaml))
   shows SynGO gave this paper's `GO:0099507` to rat Grin1 and rat Grin2a, and only
   location terms to rat Grin2b; the one human claim is the GRIN2B triple, and human GRIN2A
   has none. That reads as a mapping slip on one gene, not a family-wide practice.
   Recorded as a CONFIRMED `WRONG_GENE_PRODUCT` defect requesting a repoint to GRIN2A.
2. **GRIN3B, PMID:22564863 — probable wrong term.** Now cached with full text. It is a
   pharmacology study of open-channel blockers on rat GluN1/GluN2A, GluN1/GluN2A/GluN3A and
   GluN1/GluN2A/GluN3B receptors expressed in *Xenopus* oocytes; the word "presynaptic"
   does not occur in it. The reference-level view
   ([`PMID_22564863.yaml`](SYNGO_PROVENANCE/data/reference_level/PMID_22564863.yaml))
   shows the GRIN3B triple is SynGO's only annotation from the paper. The paper supports
   channel activity for the GluN3B-containing receptor, not a presynaptic role.
3. **GRIN2D, PMID:8886398 — probable wrong term.** Now cached (abstract only): memantine
   and MK-801 block of rat NR1a/NR2A, NR1a/NR2B and NR1a/NR2D receptors in transfected
   HEK 293 cells, with no presynaptic content. The reference-level view
   ([`PMID_8886398.yaml`](SYNGO_PROVENANCE/data/reference_level/PMID_8886398.yaml)) shows
   one SynGO claim, on rat Grin2d. Whether the human GRIN2D row is a mapping of it is to be
   checked when the GRIN2D review is finished.

GRIN2A, GRIN2B, GRIN2D and GRIN3B are not in this page's `genes:` list until their reviews
merge.

Other human `GO:0099507` / `GO:1904315` SynGO rows on `main` (GRIA1, GRIA4, CHRNA1,
CHRNB1, CHRND, CHRNE) were already reviewed as MODIFY or UNDECIDED; they are the next
sample.

## Plan

- [ ] For every human IDA/IMP SynGO claim (not a sample), record the species and cell
  system of the paper (neurons, heterologous cells, oocytes), from the cached abstract and
  full text.
- [ ] For every `GO:0099507` and `GO:1904315` claim, check that the paper assays the
  annotated subunit and a presynaptic (or postsynaptic) context. Both are precomposed
  "X involved in Y" terms, so a row that survives the check is also decomposed under
  [INVOLVED_IN_PRECOMPOSITION](INVOLVED_IN_PRECOMPOSITION.md) (`review.decomposed_into`),
  as GRIA4's MODIFY rows already do; the CHRN MODIFY rows and GRIA1 do not yet record it.
- [ ] For each suspected case, run `reference_level.py` (how SynGO annotated the whole
  paper) before recording a defect, as for PMID:19666514.
- [ ] Re-run the inventory once the GRIN reviews merge.
- [ ] Export confirmed defects (`just export-source-defects`) and send one report to
  SynGO, with the ISO convention raised as a separate question.
