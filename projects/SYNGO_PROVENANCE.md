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
index_group: CROSS_CUTTING
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

[`SYNGO_PROVENANCE/syngo_inventory.py`](SYNGO_PROVENANCE/syngo_inventory.py) reads every committed `*-goa.tsv`, keeps rows
assigned by SynGO, and joins each to its review actions. Output:
[`SYNGO_PROVENANCE/data/syngo_rows.yaml`](SYNGO_PROVENANCE/data/syngo_rows.yaml).
It counts two units. A **row** is one GOA line. A **claim** is one gene, term, qualifier
and paper: SynGO usually files one assertion as an IDA + IMP (+ NAS) set on the same paper,
so rows overstate claims by about two to one. (The inventory counts a row as one term,
qualifier, evidence code and paper. QuickGO also lists each ECO code separately, and SynGO
often files IDA under two ECO codes, so a per-term QuickGO listing runs nearer four rows per
claim.) Run on `main` as of 2026-11-15:

| Measure | Rows | Claims |
|---|---|---|
| SynGO annotations | 558 | 300 |
| Genes | 104 | 104 |
| By taxon | rat 230, mouse 161, human 130, fly 21, worm 16 | rat 132, mouse 89, human 60, fly 11, worm 8 |
| Human, by evidence (rows) | IDA 60, IMP 51, NAS 9, EXP 5, IEP 5 | all 60 human claims carry experimental evidence |
| Review actions (rows) | KEEP_AS_NON_CORE 325, ACCEPT 173, MODIFY 31, UNDECIDED 21, MARK_AS_OVER_ANNOTATED 8 | |

Every SynGO row on `main` has been reviewed, and none has been removed. The GRIN2B,
GRIN2D, GRIN3A and GRIN3B reviews are not yet on `main`, so their rows are not counted.

## Cases found so far

All three concern `GO:0099507` (ligand-gated monoatomic ion channel activity involved in
regulation of presynaptic membrane potential). Each SynGO claim below arrives as a set of
IDA, IMP and NAS rows on the same paper, so one claim appears as several rows.

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
3. **GRIN2D, PMID:8886398 — probable wrong term, on the rat gene.** Now cached (abstract
   only): memantine and MK-801 block of rat NR1a/NR2A, NR1a/NR2B and NR1a/NR2D receptors in
   transfected HEK 293 cells, with no presynaptic content. The reference-level view
   ([`PMID_8886398.yaml`](SYNGO_PROVENANCE/data/reference_level/PMID_8886398.yaml)) shows
   one SynGO claim from the paper, on rat Grin2d (UniProtKB:Q62645), and no human row.
   Human GRIN2D carries `GO:0099507` only as an electronic IEA (GO_REF:0000107, Ensembl
   orthology) with rat Grin2d as its source, so the defect to report is the rat SynGO
   claim; the human IEA would follow from correcting it.

GRIN2A, GRIN2B, GRIN2D and GRIN3B are not in this page's `genes:` list until their reviews
merge.

Other human `GO:0099507` / `GO:1904315` SynGO rows on `main` (GRIA1, GRIA4, CHRNA1,
CHRNB1, CHRND, CHRNE) were already reviewed as MODIFY or UNDECIDED. The audit below
covers the `GO:0099507` ones.

## Audit: every SynGO `GO:0099507` annotation

[`SYNGO_PROVENANCE/term_audit_rows.py`](SYNGO_PROVENANCE/term_audit_rows.py) lists every
SynGO annotation to the term in QuickGO, grouped by paper
([`GO_0099507-rows.yaml`](SYNGO_PROVENANCE/data/term_audit/GO_0099507-rows.yaml), retrieved
2026-11-16): 99 rows, 25 gene-product claims, 19 papers. Each paper was cached, read
(abstract, or full text where cached), and checked with `reference_level.py`. The verdicts,
each with a verbatim quote, are in
[`GO_0099507-verdicts.yaml`](SYNGO_PROVENANCE/data/term_audit/GO_0099507-verdicts.yaml).

| Verdict | Papers | Claims | Human claims |
|---|---|---|---|
| Supported (presynaptic function of the annotated gene) | 4 | 6 | 0 |
| Wrong gene product (GRIN2B, PMID:19666514) | — | 1 | 1 |
| No presynaptic context (channel studies, mostly HEK cells or oocytes) | 12 | 14 | 9 |
| Postsynaptic context | 2 | 3 | 1 |
| Wrong reference (an erratum notice) | 1 | 1 | 1 |
| **Total** | **19** | **25** | **12** |

The supported claims are all rodent: BK channels (Kcnma1) in hippocampal terminals, GluK2
and GluK3 presynaptic autoreceptors at mossy fibre synapses, GABA-C receptors (Gabrr1) on
rod bipolar cell terminals, and rat Grin1 and Grin2a at parallel fibre synapses. **None of
the 12 human claims is supported.**

Most of the unsupported claims come from biophysics or pharmacology of a receptor
expressed in HEK cells or *Xenopus* oocytes. Those papers support ligand-gated channel
activity, but say nothing about where in a synapse the channel acts. In 15 of the 19
papers the word "presynaptic" does not occur in the cached text, and 17 of the 19 got
the presynaptic term without the postsynaptic twin `GO:1904315`. A pattern this regular
looks like a systematic choice, such as a default term for channel-function evidence,
rather than 18 separate slips. It should go to SynGO as one question with this table,
not as 18 row-level defect claims. The SynGO paper (PMID:31171447) documents no rule
for heterologous-cell evidence; its portal is a JavaScript application with no bulk
download reachable from here, so SynGO's own assay records were not compared.

**Evidence depth.** Nine papers were read in full: five from cached full text, three
from their PubMed Central article pages, and PMID:19666514 from a PDF supplied by the
project owner. The other ten were read as abstracts only, because their full text could
not be fetched from this environment (publishers block XML download, and the PMC pages
were not reachable). Each verdict records its `evidence_depth` and a `confidence`. A
"no presynaptic context" verdict is `CONFIRMED` only when the full text was read (5
papers), and `PROBABLE` when it rests on the abstract (7 papers), since a full text can
hold an experiment its abstract omits. Read in full, PMID:20026616 mentions presynaptic
receptors only as background and as a prediction in its discussion; its experiments are
all in oocytes.

One reference is simply mis-keyed. PMID:8137830 is the 1994 erratum notice for the 1993
EMBO J glycine receptor paper, PMID:8404844, found by PubMed search. The two cached records
confirm each other: PMID:8137830 says "Erratum for EMBO J. 1993 Oct;12(10):3729-37" and
PMID:8404844 says "Erratum in EMBO J. 1994 Mar 15;13(6):1493". That paper is itself a
HEK-293 study with no presynaptic content.

**What the rows themselves record.** The row listing keeps each row's ECO code and
WITH/FROM. None of the 99 rows has a WITH/FROM, including all 48 human rows: no orthology
source is recorded for any human annotation made from a rodent paper. That is the
evidence for the first error category below, not an inference.

## Error categories this audit needs

The repository's source-defect vocabulary records *what* is wrong (`defect_type`) and,
optionally, *how* it arose (`cause`). These cases need two causes the vocabulary does not
had. They are added by #6449 as `ORTHOLOG_TRANSFER_AS_EXPERIMENTAL` and
`CONTEXT_NOT_ASSAYED`, with a `SYNGO` resource value.

1. **Ortholog transfer recorded as experimental evidence** ("implicit ISO"). A study in
   rat or mouse is annotated to the human gene with IDA or IMP. The rodent result can be
   sound and the human row still misrepresents its evidence: GO records annotation
   transferred by orthology as ISO (or ISS). This is SynGO's documented method
   (PMID:31171447), so it is one convention question, not a per-row error. The cause is
   for reporting the cohort once, with the date range and row count, not for filing on
   every row. Where it is filed, it is `defect_type: WRONG_EVIDENCE_CODE`, and the fix has
   two parts: the evidence code becomes ISO, and `With/From` names the rodent gene that
   was assayed.
2. **Context asserted but not assayed.** The paper shows the activity, but not the
   biological context the term asserts. `GO:0099507` is a precomposed term: it claims a
   ligand-gated channel *and* a role in setting presynaptic membrane potential. A
   receptor expressed in HEK cells or oocytes can support the first half only. GO has
   no explicit guideline on heterologous-system evidence, but for a context term the
   context is the claim, so evidence that cannot reach it does not support the term. As
   a defect it is `defect_type: WRONG_TERM`, with `corrected_value` the plain activity
   term (for example `GO:0015276` ligand-gated monoatomic ion channel activity, or the
   receptor-specific child the gene already carries). In a gene review this is a MODIFY
   that decomposes a precomposed term, so the row records `review.decomposed_into` with
   `context_dropped: true`: the context was never assayed.

The existing vocabulary covers the rest: the GRIN2B case is `WRONG_GENE_PRODUCT`, the
erratum is `WRONG_REFERENCE` (PMID:8137830 → PMID:8404844), and the PMID:20026616
pattern, if SynGO took the discussion's prediction as a finding, is
`SPECULATION_AS_ASSERTION`. If SynGO confirms that it used the term as a default for
channel evidence, `PRACTICE_CHANGE` would describe the cohort for a bulk fix.

## Plan

- [ ] For every human IDA/IMP SynGO claim (not a sample), record the species and cell
  system of the paper (neurons, heterologous cells, oocytes), from the cached abstract and
  full text.
- [x] For every `GO:0099507` claim, check that the paper assays the annotated subunit and a
  presynaptic context (done 2026-11-16; see the audit above).
- [ ] Do the same for `GO:1904315` (124 rows; same scripts), checking for a postsynaptic
  context. Both terms are precomposed "X involved in Y" terms, so a row that survives the
  check is also decomposed under
  [INVOLVED_IN_PRECOMPOSITION](INVOLVED_IN_PRECOMPOSITION.md) (`review.decomposed_into`),
  as GRIA4's MODIFY rows already do; the CHRN MODIFY rows and GRIA1 do not yet record it.
- [ ] For each suspected case, run `reference_level.py` (how SynGO annotated the whole
  paper) before recording a defect, as for PMID:19666514.
- [ ] Re-run the inventory once the GRIN reviews merge.
- [ ] Schema PR #6449: a `SYNGO` value for `SourceResourceEnum` and the two causes above.
- [ ] Before sending the question to SynGO, look for per-annotation assay types in the
  supplementary tables of PMID:31171447 and in the SynGO release files. They would show
  directly whether `GO:0099507` was a default term for channel evidence.
- [ ] Read the full text of the ten abstract-only papers (needs institutional access or
  supplied PDFs) and upgrade or revise their `PROBABLE` verdicts.
- [ ] Export confirmed defects (`just export-source-defects`) and send one report to
  SynGO, with two convention questions kept separate from the row-level defects: the ISO
  question, and the use of `GO:0099507` for channel evidence without presynaptic context.
