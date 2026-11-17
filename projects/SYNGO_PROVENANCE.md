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
2. **GRIN3B, PMID:22564863 — the paper does not support the term.** Now cached with full text. It is a
   pharmacology study of open-channel blockers on rat GluN1/GluN2A, GluN1/GluN2A/GluN3A and
   GluN1/GluN2A/GluN3B receptors expressed in *Xenopus* oocytes; the word "presynaptic"
   does not occur in it. The reference-level view
   ([`PMID_22564863.yaml`](SYNGO_PROVENANCE/data/reference_level/PMID_22564863.yaml))
   shows the GRIN3B triple is SynGO's only annotation from the paper. The paper supports
   channel activity for the GluN3B-containing receptor, not a presynaptic role.
3. **GRIN2D, PMID:8886398 — the paper does not support the term, on the rat gene.** Read in full from a PDF supplied
   by the project owner: memantine and MK-801 block of rat NR1a/NR2A, NR1a/NR2B and NR1a/NR2D receptors in
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

**Evidence depth.** Seventeen papers were read in full: five from cached full text, three
from their PubMed Central article pages, and nine from PDF or HTML copies supplied by the
project owner (PMID:19666514 first, then the eight that had been read as abstracts). Each
verdict records its `evidence_depth` and a `confidence`; a "no presynaptic context"
verdict is `CONFIRMED` only when the full text was read. All 12 such verdicts and both
postsynaptic verdicts are now read in full, and none changed: every one of the eight
papers added on 2026-11-17 is an HEK 293 study (one adds a neuroblastoma line, one a
neuron-HEK co-culture with the receptor on the postsynaptic side), with no presynaptic
experiment. Two papers remain abstract-only: PMID:17620617, a supported verdict, and the
erratum notice PMID:8137830, whose verdict rests on the two PubMed records. Read in full, PMID:20026616 mentions presynaptic
receptors only as background and as a prediction in its discussion; its experiments are
all in oocytes.

One reference is simply mis-keyed. PMID:8137830 is the 1994 erratum notice for the 1993
EMBO J glycine receptor paper, PMID:8404844, found by PubMed search. The two cached records
confirm each other: PMID:8137830 says "Erratum for EMBO J. 1993 Oct;12(10):3729-37" and
PMID:8404844 says "Erratum in EMBO J. 1994 Mar 15;13(6):1493". That paper, read in full
from a copy supplied by the project owner, is itself a HEK-293 study of glycine receptor
chloride conductance with no presynaptic content, so correcting the PMID would not make
the citation support the term.

**What the rows themselves record.** The row listing keeps each row's ECO code and
WITH/FROM. None of the 99 rows has a WITH/FROM, including all 48 human rows: no orthology
source is recorded for any human annotation made from a rodent paper. That is the
evidence for the first error category below, not an inference.

## Biology check: are the flagged seeds wrong, or only mis-sourced?

A failed citation does not make a claim false. The question that matters for the
annotations downstream is whether each flagged gene really has the activity the term
asserts, from any source. That is recorded per seed in
[`GO_0099507-seed-biology.yaml`](SYNGO_PROVENANCE/data/term_audit/GO_0099507-seed-biology.yaml),
from one PubMed screen per gene (method in the file header; it is a screen, not a
systematic review).

**Why it matters: the seeds are copied.** Of the 1,497 annotations to `GO:0099507` in
QuickGO (2026-11-17), 99 are SynGO's own. Almost all the rest are copies of SynGO's human
and mouse seeds into other species: 1,194 Ensembl orthology projections
(`GO_REF:0000107`, about 100 taxa), plus RGD and GO_Central ISO rows and UniProt rows
that name a seed in their WITH/FROM. There are no IBA rows for this term. Each human or
mouse seed is copied to 60-100 other annotations; the rat seeds are not projected.
[`seed_downstream.py`](SYNGO_PROVENANCE/seed_downstream.py) recomputes this and writes
[`GO_0099507-downstream.yaml`](SYNGO_PROVENANCE/data/term_audit/GO_0099507-downstream.yaml).
The 18 seeds whose citations fail account for 1,030 downstream rows.

| Biology | Seeds (downstream rows) | Rows |
|---|---|---|
| Supported independently | GABRA2 (94), GLRA1 (92), GRIN2B (92), GRIK4 (89), Htr3a (79), GRIK5 (78), Grin2d (2), Grik1, Gria2 | 526 |
| Partial (afferent axons, not clearly terminals) | GABRA5 (91) | 91 |
| Presynaptic localization only | GRIA4 (96), GRIA1 (94), GRIA3 (85), GRIN3B (76), Gabra1, Gabra3 | 351 |
| Indirect only (a presynaptic role proposed, not shown) | GABRB1 (62) | 62 |
| Not resolved (antibody does not separate paralogs) | Gabrb2 | 0 |

So most of the flagged seeds are **true claims with the wrong citation**. That includes
the two with the worst provenance: GRIN2B (wrong subunit on the cited paper) and GLRA1
(an erratum notice, whose corrected paper does not support the term either). Presynaptic
GluN2B-containing NMDA receptors and homomeric alpha1 glycine receptors on calyx of Held
terminals are both independently shown. For these, the fix is a better citation, not
removal.

**No seed is contradicted.** The candidates for a bad seed are the ones without direct
functional presynaptic evidence: GRIA4, GRIA1, GRIA3 and GRIN3B (immunogold only; the one
functional AMPA study implicates GluR2-containing receptors and found no presynaptic
effect with a GluR3-selective agonist) and GABRB1 (indirect only: Gabrb1 mutant mice have
reduced mIPSC frequency, and the authors propose presynaptic beta1 receptors as one
explanation, PMID:24281383). Together they feed 413 downstream rows. GABRA5 (91 rows) has
functional evidence, but on afferent axons rather than the presynaptic terminal membrane
the term specifies. Conventional heteromeric GABA-A receptors contain beta subunits (rho
subunits, by contrast, can assemble without them, PMID:9153229), but that does not say
whether a given presynaptic receptor contains beta1, beta2 or beta3.
None of these should be reported as "wrong" without an expert view; each should be
reported as "citation does not support the term, and we found no direct functional
evidence".

## GABA-B findings recorded on GABA-A genes

The two GABA receptor families share a letter. GABA-B receptor subunits are written
GABA(B1) and GABA(B2) (genes GABBR1, GABBR2); GABA-A beta subunits are beta1-3 (genes
GABRB1-3). Tracing GABRB1's presynaptic annotations led to a SynGO row on rat Gabrb1
taken from a GABA-B paper, so every SynGO annotation on a GABA receptor gene was checked
for the same slip. [`gaba_receptor_swaps.py`](SYNGO_PROVENANCE/gaba_receptor_swaps.py)
pulls them (339 rows from 38 papers), reads each paper's title and abstract, and flags a
GABA-A gene annotated from a paper mostly about GABA-B receptors, or the reverse. It
flagged three papers; its output is
[`gaba_receptor_swaps.yaml`](SYNGO_PROVENANCE/data/gaba_receptor_swaps.yaml) and the verdicts are in
[`gaba_receptor_swaps-verdicts.yaml`](SYNGO_PROVENANCE/data/gaba_receptor_swaps-verdicts.yaml).

| Paper | What SynGO did | Spread | Verdict |
|---|---|---|---|
| PMID:11498050, mice lacking GABA(B(1)) | Gave mouse **Gabrb1** the same 12 records as Gabbr1 (three terms), including `GO:0099528` G protein-coupled neurotransmitter receptor activity | 58 derived records per term in 57 species (all Ensembl, except 17 UniProt records for GABA-ergic synapse), including human GABRB1, which GO's inference then also gives `GO:0007186` G protein-coupled receptor signaling pathway | Wrong gene; the GPCR activity is biologically impossible for a GABA-A subunit |
| PMID:15174078, GABA(B1) and GABA(B2) in rat globus pallidus | Recorded 18 records on rat **Gabrb1** (6) and **Gabrb2** (12), none on Gabbr1/Gabbr2 | 12 records from Gabrb1 (Ensembl and UniProt), including the only presynaptic location on human GABRB1; 4 UniProt ISS records from Gabrb2 | Wrong gene; re-curate against Gabbr1/Gabbr2, re-checking compartments (much of the glutamatergic-synapse labelling is perisynaptic) |
| PMID:15749345, GABA-A and GABA-B receptors in monkey globus pallidus | Annotated macaque GABBR1 only | none | Not a swap (flagged because the paper covers both families) |

The first case is the clearest bad seed in this audit: an annotation that is wrong on
biological grounds, not only mis-sourced, and copied into 57 species. Human GABRB1 now
carries `G protein-coupled neurotransmitter receptor activity` (Ensembl IEA, from mouse
Gabrb1) beside its correct GABA-A annotations. Both cases are `WRONG_GENE_PRODUCT` with
cause `SYMBOL_COLLISION`, confirmed from the abstracts, which name the subunits studied;
PMID:15174078 was also read in full; its receptor antibodies target GABA(B1) and GABA(B2). SynGO's
other rat Gabrb1 paper, PMID:16469775 (also read in full), is a genuine GABA-A beta1 study
of fast IPSCs and is correctly attributed.

The swapped seeds did reach PAINT, through three IBA terms. PAINT lists its donors by MGI
or RGD identifier, so [`swap_iba_donors.py`](SYNGO_PROVENANCE/swap_iba_donors.py) takes
each swapped gene's identifier, lists every IBA that names it, and keeps those whose term
is a swapped term or an ancestor of one (output
[`gaba_receptor_swaps-iba.yaml`](SYNGO_PROVENANCE/data/gaba_receptor_swaps-iba.yaml),
QuickGO and UniProt, 2026-11-17):

| IBA term (PAINT node) | Swapped genes among the donors | Donors whose only support is the swap |
|---|---|---|
| `GO:0098982` GABA-ergic synapse (PTN008566841, 241 rows) | mouse Gabrb1 MGI:95619, rat Gabrb1 RGD:2649, rat Gabrb2 RGD:2650 | mouse Gabrb1, rat Gabrb2 |
| `GO:0045211` postsynaptic membrane (PTN008360792, 39 rows) | rat Gabrb1 (its swapped postsynaptic specialization membrane row is a descendant) | rat Gabrb1 |
| `GO:0005886` plasma membrane (PTN001054635) | rat Gabrb1, rat Gabrb2 | none |

Each node keeps independent support. For GABA-ergic synapse, eight of the nine other
donors have their own experimental rows for the term (mouse Gabrr3 has no reviewed
UniProt entry and was not checked); for postsynaptic membrane, all three other donors do
(rat Gabrb3, human GABRB3 and bovine GABRB1); plasma membrane has dozens. So correcting
the seeds removes donors without changing any node. Mouse Gabrb1 is a donor to no other IBA, and no
IBA anywhere uses the G protein-coupled neurotransmitter receptor activity row. The
script records each donor's support, so the roster can be re-checked. An earlier version
of this page said no IBA used the seeds; that check searched WITH/FROM for UniProt
accessions, which PAINT does not use, and a later one looked only at the swapped terms
themselves. Outside PAINT, the spread is Ensembl orthology projections, UniProt automatic
rows and four UniProt ISS rows; the ISS rows copy rat Gabrb2's postsynaptic specialization
membrane, which rat Gabrb2 also has from an independent IDA (PMID:9464994), so the term
can stand on those rows once the swapped support is removed.

## Ontology issues behind these annotations

The annotations above sit on a part of GO where several partly overlapping classification axes
are combined in precomposed terms. These are questions for the GO editors, not row-level
corrections. Term structure was read from OLS and annotation counts from QuickGO on
2026-11-17.

| Term | Gating | Ion | Receptor | Context | Annotations |
|---|---|---|---|---|---|
| `GO:0004890` GABA-A receptor activity | none | none | GABA receptor activity | none | 21,889 |
| `GO:0022851` GABA-gated chloride ion channel activity | transmitter-gated, extracellular ligand-gated | chloride | neurotransmitter receptor activity | none | 2,515 |
| `GO:1904315` transmitter-gated ... involved in regulation of postsynaptic membrane potential | transmitter-gated, extracellular ligand-gated | monoatomic ion | neurotransmitter receptor activity | postsynaptic | 3,513 |
| `GO:0099507` ligand-gated ... involved in regulation of presynaptic membrane potential | ligand-gated only | monoatomic ion | none | presynaptic | 1,497 |

1. **GABA-A receptor activity is disconnected from the channel branch.** `GO:0004890` has
   no channel or chloride ancestor and no children; its definition says "GABA-A receptors
   function as chloride channels", and its comment asks curators to also annotate chloride
   channel activity. `GO:0022851` GABA-gated chloride ion channel activity is not under
   `GO:0016917` GABA receptor activity. So the most used term (21,889 annotations) is not
   connected to the GABA-gated channel term through the GABA receptor branch; the two meet
   only at signaling receptor activity. Open ticket
   [geneontology/go-ontology#31035](https://github.com/geneontology/go-ontology/issues/31035)
   (2025-11-07) raises the same problem for acetylcholine receptor activity, where
   nicotinic channels get annotated to a term meant for the muscarinic GPCRs. We found no
   ticket for the GABA case.
2. **The pre- and postsynaptic twins differ in scope.** `GO:1904315` is a transmitter-gated,
   extracellular-ligand-gated neurotransmitter receptor activity; `GO:0099507` is any
   ligand-gated ion channel activity. That breadth may be deliberate: presynaptic
   ligand-gated channels include channels opened by intracellular ligands, such as the
   calcium-activated BK channels supported in this same audit (PMID:11739569). The
   consequence for GABA-A subunits is that a `GO:0099507` row adds a context and says
   less about the channel than their other terms. This is a point about how the term is
   used, not necessarily an ontology error.
3. **The precomposed context terms are already on GO's obsoletion list.**
   `GO:0099507` is listed in the open ticket
   [geneontology/go-ontology#14324](https://github.com/geneontology/go-ontology/issues/14324)
   ("Function involved in process to OBSOLETE", 2017), which follows the general proposal
   [#14138](https://github.com/geneontology/go-ontology/issues/14138) (closed 2022) to stop
   precomposing molecular functions with processes.
   [#31205](https://github.com/geneontology/go-ontology/issues/31205) (closed 2025-12-11)
   obsoleted 11 "channel activity involved in X" terms, replacing each with its plain
   activity, but not `GO:0099507` or `GO:1904315`, which carry most of SynGO's annotations
   (1,497 and 3,513).

For the audit this means the `CONTEXT_NOT_ASSAYED` fix is low-cost: replacing `GO:0099507`
with the specific activity a GABA-A subunit already carries (`GO:0022851`) gains chloride
selectivity and transmitter gating, and loses only the untested context. If GO goes ahead
with #14324, the same replacement would happen for every row, and the precomposed term's
own problems (evidence that can reach only half of it) would go with it.

## Error categories this audit needs

The repository's source-defect vocabulary records *what* is wrong (`defect_type`) and,
optionally, *how* it arose (`cause`). These cases needed two causes the vocabulary did not
have. #6449 added them as `ORTHOLOG_TRANSFER_AS_EXPERIMENTAL` and
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
   receptor-specific child the gene already carries). Before generalising, check for
   an independent paper that does assay the presynaptic context; if there is one, the
   claim is true but mis-sourced, so re-source the row instead of dropping the context.
   GRIK4/GRIK5 need this check, because presynaptic kainate autoreceptors are
   established from other work (PMID:17620617 supports the GluK2/GluK3 case in this
   same cohort). In a gene review this is a MODIFY
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
- [x] Schema PR #6449 (merged): a `SYNGO` value for `SourceResourceEnum` and the two causes above.
- [ ] Before sending the question to SynGO, look for per-annotation assay types in the
  supplementary tables of PMID:31171447 and in the SynGO release files. They would show
  directly whether `GO:0099507` was a default term for channel evidence.
- [x] Read the full text of the abstract-only papers with flagged verdicts (eight, from
  copies supplied by the project owner, 2026-11-17); all verdicts confirmed.
- [x] Read PMID:8404844, the paper the GLRA1 erratum citation should point to: an
  HEK-293 conductance study with nothing presynaptic.
- [x] Separate provenance from biology: a PubMed screen per flagged seed gene
  (`GO_0099507-seed-biology.yaml`). Most seeds are true but mis-sourced; none is
  contradicted; five lack direct functional evidence and one (GABRA5) has it on axons.
- [x] Check every SynGO annotation on a GABA receptor gene for GABA-A/GABA-B swaps
  (`gaba_receptor_swaps.py`): two confirmed (PMID:11498050, PMID:15174078).
- [x] Check whether the swapped seeds are PAINT donors (`swap_iba_donors.py`): they feed
  three IBA terms (GABA-ergic synapse, postsynaptic membrane, plasma membrane); every node
  keeps independent support.
- [ ] Raise with the GO editors that GABA-A receptor activity is disconnected from the
  GABA-gated channel branch (cite #31035 as the parallel case). The pre/post scope
  difference is noted but may be deliberate.
- [ ] Look for the same kind of name collision beyond GABA receptors (for example other
  receptor families whose subunit and receptor-type names share a letter or number).
- [ ] Ask an expert (or SynGO) about the five seeds without direct functional evidence
  (GRIA4, GRIA1, GRIA3, GRIN3B, GABRB1), and about GABRA5's axonal evidence, before
  calling any of them wrong.
- [x] Count the downstream annotations each seed feeds (`seed_downstream.py`): 1,030
  rows derive from the 18 flagged seeds.
- [ ] Export confirmed defects (`just export-source-defects`) and send one report to
  SynGO, with two convention questions kept separate from the row-level defects: the ISO
  question, and the use of `GO:0099507` for channel evidence without presynaptic context.
