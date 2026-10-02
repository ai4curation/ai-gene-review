---
title: "Arabidopsis Single-Cell Response to Fungal Infection"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [ARATH]
genes: [MYB122, MYB51, MYB34, CYP71A12, CYP71A13, FRK1]
---

# Arabidopsis Single-Cell Response to Fungal Infection

**Bottom line:** this project reviews the GO annotations of the Arabidopsis
genes that a single-cell atlas of fungal infection singled out
([PMID:37741284](https://pubmed.ncbi.nlm.nih.gov/37741284/), Tang et al. 2023,
*Cell Host & Microbe* 31:1732). The paper profiled 95,040 leaf cells infected
with the hemibiotrophic fungus *Colletotrichum higginsianum*. The first batch
covers six genes: MYB122, the one gene the paper tested genetically, plus its
indole-glucosinolate regulator paralogs MYB51 and MYB34, the camalexin
cytochromes CYP71A12 and CYP71A13, and the immune marker FRK1. Results are in
the [review status](#review-status) table. All six reviews are complete: 96
existing annotations were assessed, with 49 accepted, 22 kept as non-core, 7
modified, 5 marked over-annotated, 11 removed and 2 left undecided, plus 7 new
annotations proposed.

We picked this paper because it separates two kinds of evidence that GO
annotation usually blurs together. Most of its findings say *where* a gene is
expressed: which cell type, and how close the cell is to the fungus. Expression
like that supports at most a `response to` term, not a function. Only the
myb122 mutant phenotype is functional evidence. The review question for each
gene is whether its existing annotations hold up, and whether the paper adds
anything that meets the bar for a new annotation.

**Project start date:** 2026-10-02
**Organism:** *Arabidopsis thaliana* (ARATH)
**Source paper:** Tang B, Feng L, Hulin MT, Ding P, Ma W (2023). Cell-type-specific
responses to fungal infection in plants revealed by single-cell transcriptomics.
*Cell Host Microbe* 31:1732–1747. doi:10.1016/j.chom.2023.08.019 (open access,
CC BY-NC-ND). The cached copy (`publications/PMID_37741284.md`) holds only the
abstract, so review quotes from this paper are limited to the abstract.

## What the paper found

| Finding | Kind of evidence | Genes named |
|---|---|---|
| Leaf atlas of 95,040 cells in 25 clusters (mesophyll about 70%, vasculature 13%, epidermis 8%, guard cells 3%) | scRNA-seq, 24 and 40 h post inoculation | cell-type markers |
| TIR-NLRs (TNLs) are expressed mainly in procambium, and many are induced further by infection | expression | RPP1, RPP5, SNC1, RPS6 |
| A subset of TNLs is induced only in phloem companion cells at 24 h, not at 40 h | expression | RRS1B, CSA1, CHS1 |
| RPS4 is induced in epidermal, guard, procambium and phloem companion cells | expression | RPS4 |
| Each RNL helper paralog has its own cell-type pattern; NRG1.1 goes down after infection while NRG1.2 goes up | expression | ADR1, ADR1-L1, ADR1-L2, NRG1.1, NRG1.2 |
| CNLs have no general vascular bias, with a few exceptions | expression | ZAR1, CW9, RF9, SUMM2 |
| Along the infection trajectory, FRK1 rises toward the cells touching the hyphae; a pFRK1 reporter confirms this in live imaging | expression and reporter imaging | FRK1, KTI1, GSTU10, WRKY75, PEP2 |
| In guard cells near the fungus, positive ABA regulators go up, negative ones go down, and stomata close | expression and stomatal-aperture imaging | PED1, CAR8, CPK11 (up); ABR1, ABI1, FER1, GCR1 (down) |
| Glucosinolate and camalexin genes are induced at infection sites, each in its own cell types | expression | ASA1, TSB1, SUR1, SOT16, CYP71A12 (epidermis), CYP71A13 (vasculature), MYB51 (vasculature), MYB122 (epidermis) |
| **Two independent myb122 T-DNA mutants are hypersusceptible:** larger lesions, and faster branching of invasive hyphae in the epidermis | **genetics (loss of function)** | **MYB122** |

## Curation approach

- **Cell-type expression is not function.** That a gene is induced in procambium or
  in guard cells near the fungus is a fact about the gene's regulation. GO has no
  "expressed in cell type" relation, so these findings do not become annotations.
  At most they support a `response to fungus` row with IEP evidence, and only when
  that row is not already there.
- **MYB122 is the only gene with new functional evidence from this paper.** Even
  there, the phenotype shows that MYB122 is needed for resistance. It does not show
  which step of defense MYB122 carries out. Glucosinolate regulation is the likely
  route, but the paper did not measure glucosinolates in the mutant. Any new process
  term has to meet the `NEW` bar in `CLAUDE.md`.
- **FRK1 is a marker.** It is the standard reporter gene for PTI, and its own
  biochemical role is barely characterized. Being induced by flg22 is not evidence
  that it takes part in defense.

## Review status

The first batch covers the genes on the paper's functional thread (MYB122) and
its glucosinolate and camalexin context. Action counts are taken from the review
files.

| Gene | Locus | UniProt | Role in the paper | Status | Annotations reviewed | Summary |
|---|---|---|---|---|---|---|
| MYB122 | At1g74080 | Q9C9C8 | Epidermis-specific induction at infection sites; mutant is hypersusceptible | ✅ complete | 12 | 8 accept, 3 non-core, 1 over-annotated; NEW regulation of glucosinolate biosynthetic process |
| MYB51 | At1g18570 | O49782 | Induced only in vasculature at infection sites | ✅ complete | 12 | 6 accept, 4 non-core, 1 modify, 1 over-annotated; NEW transcription activator activity |
| MYB34 | At5g60890 | O64399 | Third indole-glucosinolate MYB; not induced | ✅ complete | 17 | 10 accept, 1 non-core, 2 modify, 3 over-annotated, 1 remove; 2 NEW |
| CYP71A12 | At2g30750 | O49340 | IAOx to IAN; induced mainly in epidermis | ✅ complete | 17 | 9 accept, 5 non-core, 1 modify, 1 remove, 1 undecided; NEW IAOx dehydratase activity, defense response to fungus |
| CYP71A13 | At2g30770 | O49342 | IAOx to IAN; induced almost only in vasculature | ✅ complete | 24 | 11 accept, 8 non-core, 4 remove, 1 undecided |
| FRK1 (SIRK) | At2g19190 | O64483 | Marker for proximity to the infection | ✅ complete | 14 | 5 accept, 1 non-core, 3 modify, 5 remove; NEW response to fungus |

### Genes already reviewed in other projects

SUR1 (core glucosinolate C-S lyase), ABI1 (negative regulator of ABA
signaling), and EDS1 and PAD4 (TNL and RNL signaling hubs) already have
reviews in the repo.

### Candidate backlog

These genes are named in the paper but not yet reviewed. UniProt accessions were
taken from UniProt's reviewed entries (October 2026). The four helper-NLR paralogs
(ADR1-L1, ADR1-L2, NRG1.1, NRG1.2) do not resolve by name in UniProt and need
their accessions looked up before they are fetched.

| Group | Gene | Locus | UniProt |
|---|---|---|---|
| TNL | RPP1 | At3g44480 | F4J339 |
| TNL | RPP5 | At4g16950 | F4JNB7 |
| TNL | SNC1 | At4g16890 | O23530 |
| TNL | RPS6 | At5g46470 | F4KHH8 |
| TNL | RPS4 | At5g45250 | Q9XGM3 |
| TNL | RRS1B | At5g45050 | Q9FL92 |
| TNL | CSA1 | At5g17880 | F4KIF3 |
| TNL | CHS1 | At1g17610 | F4I902 |
| RNL | ADR1 | At1g33560 | Q9FW44 |
| RNL | ADR1-L1, ADR1-L2, NRG1.1, NRG1.2 | to be looked up | to be looked up |
| CNL | ZAR1 | At3g50950 | Q38834 |
| CNL | SUMM2 | At1g12280 | P60838 |
| CNL | RF9 | At1g58848 | P0DI17 |
| Guard-cell ABA | CPK11 | At1g35670 | Q39016 |
| Guard-cell ABA | PED1 (KAT2) | At2g33150 | Q56WD9 |
| Guard-cell ABA | ABR1 | At5g64750 | Q9FGF8 |
| Guard-cell ABA | GCR1 | At1g48270 | O04714 |
| Guard-cell ABA | FER1 | At5g01600 | Q39101 |
| Indole and glucosinolate | ASA1 | At5g05730 | P32068 |
| Indole and glucosinolate | TSB1 | At5g54810 | P14671 |
| Indole and glucosinolate | SOT16 | At1g74100 | Q9C9D0 |
| Infection-site markers | KTI1 (KTI4) | At1g73260 | Q8RXD5 |
| Infection-site markers | GSTU10 | At1g74590 | Q9CA57 |
| Infection-site markers | WRKY75 | At5g13080 | Q9FYA2 |
| Infection-site markers | PROPEP2 | At5g64890 | Q9LV88 |

The NLRs are the natural next batch. Many of them carry `EC 3.2.2.6` (NAD+
hydrolase) in UniProt, so the reviews should check that TIR-domain NADase
activity is annotated consistently across the TNLs.

## Findings

- **Regulators were annotated as enzymes.** MYB34 and MYB51 carried `GO:0009759`
  indole glucosinolate biosynthetic process. Both were changed to `GO:0010439`
  regulation of glucosinolate biosynthetic process, which MYB122 also received as a
  new annotation, because the transcription factors catalyse no step of the pathway.
  GO has no positive or indole-specific child of `GO:0010439`; the MYB34 review
  proposes one.
- **MYB122's fungal-defense annotation already exists.** GOA carries
  `GO:0050832` defense response to fungus for MYB122 from this paper. It was
  accepted, with a note that the evidence is a mutant phenotype (IMP) rather than
  IDA. The paper's key-resources table lists both myb122 lines under the wrong
  locus (AT3G25800, not At1g74080) and calls one a CRISPR line while the text says
  T-DNA. These look clerical and are recorded on the reference.
- **The three MYBs divide by cell type and by signal.** Several independent
  studies agree that MYB34, unlike MYB51 and MYB122, is not induced by pathogens or
  wounding, and Tang et al. found the same at infection sites. MYB34's
  `response to other organism` row was marked over-annotated on that basis.
- **The CYP71A12 and CYP71A13 paralogs were kept distinct.** CYP71A12 gained its
  enzyme activity (`GO:0047720`, IDA) and `defense response to fungus` (IMP), as
  the main enzyme for pathogen-induced indole-3-carboxylic acid derivatives;
  CYP71A13 remains the main leaf camalexin enzyme. Both carry an ER-lumen IDA from
  PMID:33831160, a PMID that no longer resolves, and both were left undecided.
- **FRK1 is a marker, not a demonstrated defense component.** Its two
  `defense response to bacterium` rows were changed to `response to bacterium`,
  and one flg22-only row to `response to molecule of bacterial origin`. A motif
  scan shows FRK1 has an intact kinase domain, but no activity, substrate or mutant
  phenotype has been published.
- **Induced systemic resistance looks mis-propagated.** For MYB51 and CYP71A12
  the source study describes salicylic-acid-dependent resistance, while
  `GO:0009682` is defined as salicylic-acid-independent. This is worth raising
  with PAINT and the GOA curators.
- **Open hypotheses for single-cell reanalysis.** Whether MYB122 levels track its
  indole glucosinolate targets cell by cell in epidermis, and whether CYP71A12-high
  and CYP71A13-high cells switch on different downstream branches. Only raw reads
  are deposited (ENA PRJEB61052); there is no processed count matrix.
