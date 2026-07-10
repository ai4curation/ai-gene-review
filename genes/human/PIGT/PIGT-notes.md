# PIGT (Q969N2) review notes

## Summary of function
PIGT (GPI-anchor transamidase component PIG-T) is one of five subunits of the
glycosylphosphatidylinositol-anchor transamidase (GPI-T) complex, an ER-membrane
enzyme complex that attaches the pre-assembled GPI anchor to the C-terminus of
GPI-anchored proteins (GPI-APs). The complex is PIGK (catalytic, GPI8), GPAA1,
PIGS, PIGT, PIGU. It is NOT an independent enzyme; the catalytic activity resides
in PIGK.

- PIGT is a **required structural subunit**: it disulfide-links to the catalytic
  PIGK/GPI8 (Cys182 of PIGT ↔ Cys92 of PIGK) and stabilises/holds the complex
  together. [PMID:11483512 "we demonstrate that PIG-S and PIG-T form a protein
  complex with GAA1 and GPI8, and that PIG-T maintains the complex by stabilizing
  the expression of GAA1 and GPI8"]; disulfide bridge [PMID:12582175 "two subunits
  of mammalian GPI transamidase, GPI8 and PIG-T, form" ... "required for full
  transamidase activity"].
- Cryo-EM structures confirm an equimolar heteropentamer; PIGK holds the catalytic
  triad; a GPI substrate-binding cleft is formed by transmembrane helices under
  PIGK, and PIGT contributes lipid-substrate binding residues (UniProt BINDING
  461/521/523/527). [PMID:35551457 "revealing an equimolar" heteropentameric
  assembly; "endogenous GPI in the structure defines a composite cavity for the
  lipid"]; [PMID:35165458 "The PIGK subunit" is the catalytic component;
  "C206-H164-N58" triad]; [PMID:37684232 "replaces it with GPI via a transamidation
  reaction"].
- Localisation: ER membrane, single-pass type I membrane protein; ER retention is
  encoded in its transmembrane span. [PMID:15713669 "PIG-T is a type I" membrane
  glycoprotein; "PIG-T revealed that it is ER-localized because of information in
  its" transmembrane span].

## Disease
Biallelic loss-of-function variants cause **multiple congenital anomalies-hypotonia-
seizures syndrome 3 (MCAHS3; MIM:615398)**, an inherited GPI deficiency
(intellectual disability, hypotonia, epilepsy, dysmorphism, skeletal/endocrine/
ophthalmologic anomalies). A germline + somatic PIGT combination also causes a
**paroxysmal nocturnal hemoglobinuria-like phenotype (PNH2; MIM:615399)**. Patient
and knockout-rescue assays show variants reduce cell-surface GPI-AP display
(CD16b/CD59). [PMID:28327575; PMID:36970549 "leads to mildly reduced" activity]

## GOA term inventory (what is actually present)
- MF present: GO:0005515 protein binding (IPI, multiple); GO:0034235 GPI anchor
  binding (IDA, PMID:11483512). **No independent catalytic MF is annotated** — do
  not invent one; the transamidase catalysis is PIGK's.
- BP: GO:0016255 attachment of GPI anchor to protein; GO:0006506 GPI anchor
  biosynthetic process; GO:0180046 GPI anchored protein biosynthesis.
- CC: GO:0042765 GPI-anchor transamidase complex; GO:0005789 ER membrane;
  GO:0016020 membrane (HDA proteomics).

## Curation decisions
- Core BP = GO:0016255 / GO:0006506 (GPI anchor attachment / biosynthesis).
- Core CC = GO:0042765 (GPI-anchor transamidase complex) + GO:0005789 (ER membrane).
- GO:0034235 GPI anchor binding = informative MF, ACCEPT (structural support:
  PIGT lipid-binding residues; do not REMOVE an IDA whose full text I cannot see).
- GO:0005515 protein binding IPIs → MARK_AS_OVER_ANNOTATED (uninformative bare
  binding; the informative content is captured by GO:0042765 / GO:0034235). Per
  policy not REMOVE.
- GO:0016020 membrane (HDA, NK-cell membrane proteome) → too general vs ER
  membrane; KEEP_AS_NON_CORE.
- GO:0180046 GPI anchored protein biosynthesis — sibling/parent-level BP for the
  pathway output; ACCEPT (many IDA) but non-core relative to the direct
  attachment step; treat as accepted supporting BP.

## No deep-research file
falcon is out of credits (HTTP 402); no -deep-research-*.md generated. Grounded in
PIGT-uniprot.txt, PIGT-goa.tsv, and cached publications/PMID_*.md.
