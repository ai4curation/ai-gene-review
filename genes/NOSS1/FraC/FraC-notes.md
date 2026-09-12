# FraC (alr2392) — research notes

Gene: **fraC** / OrderedLocusName **alr2392**
UniProt: **P46078** (FRAC_NOSS1), REVIEWED, 179 aa, MW ~21 kDa.
Organism: *Nostoc* (*Anabaena*) sp. PCC 7120 (NCBITaxon:103690).
Product name (UniProt): "Filament integrity protein FraC".

## Summary

FraC is a small, polytopic integral cytoplasmic-(inner)-membrane protein of the
filamentous, heterocyst-forming cyanobacterium *Nostoc*/*Anabaena* sp. PCC 7120. It is
one of several septal proteins that build and maintain the intercellular septa joining
adjacent cells in a filament, and it is required for filament integrity and for
diazotrophic (N2-fixing) growth. FraC localizes to the intercellular septa, where the
septal-junction (SJ) machinery — the gap-junction-like channels that connect the
cytoplasms of neighboring cells across the septal peptidoglycan — is assembled. Loss of
FraC causes filament fragmentation under nitrogen deprivation, mislocalization of the
septal protein SepJ, and impaired intercellular transfer of small molecules.

## Genetics and discovery

- FraC was identified as the gene mutated in the short-filament fragmentation mutant
  strain 129 of *Anabaena* PCC 7120. [PMID:7883709 "The affected gene in strain 129, fraC, was cloned by complementation and characterized. It encodes a unique 179-amino-acid protein rich in phenylalanine."]
- Insertional inactivation reproduces the mutant phenotype, confirming FraC is causal.
  [PMID:7883709 "Insertional inactivation of the chromosomal copy of fraC results in a phenotype identical to that of strain 129"]
- The mutant fragments specifically upon nitrogen starvation (not upon sulfate,
  phosphate, iron, or calcium starvation) and forms few heterocysts; heterocyst
  differentiation itself is not blocked (extra hetR restores heterocysts). Thus FraC's
  role is in cell-junction/filament integrity rather than differentiation per se.
  [PMID:7883709 "Thus, FraC is required for the integrity of cell junctions in general but is apparently not directly involved in normal differentiation and nitrogen fixation."]

## Operon and expression

- *fraC* (alr2392) is the first gene of the **fraC(alr2392)-fraD(alr2393)-fraE(alr2394)**
  operon and is constitutively expressed.
  [PMID:20487302 "Whereas fraC (alr2392) was constitutively expressed as an operon together with two downstream genes, alr2393 (fraD) and alr2394 (fraE)"]

## Localization and cell-cell communication

- GFP fusions place FraC (and FraD) at the intercellular septa.
  [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also located at the intercellular septa."]
- *fraC* (and *fraD*) mutants mislocalize the septal junction protein SepJ and are
  impaired in intercellular exchange of the fluorescent tracer calcein, indicating a
  role in septal-junction-mediated intercellular molecular transfer.
  [PMID:20487302 "The fraC and fraD mutants showed an impaired localization of SepJ at the intercellular septa and were hampered in the intercellular transfer of the fluorescent probe calcein."]
- FraC, together with SepJ and FraD, shapes the architecture and function of the
  intercellular septa.
  [PMID:20487302 "at least three different proteins, SepJ, FraC and FraD, influence the architecture and function of the"]

## Structural / biophysical features

- UniProt (P46078) annotates FraC as an integral cell-membrane protein with **4
  predicted transmembrane helices** (residues 10-30, 46-66, 96-116, 156-176) and no
  large soluble domain; subcellular location "Cell membrane; Multi-pass membrane
  protein". Phenylalanine-rich (noted in the original description).
  [file:NOSS1/FraC/FraC-uniprot.txt "TRANSMEM"]

## Protein family

- **TCDB 1.V.1.1.1** — "the filamentous cyanobacterial septal pore (septum) family"
  (the same family as its operon partner FraD/alr2393).
  [file:NOSS1/FraC/FraC-uniprot.txt "TCDB; 1.V.1.1.1; the filamentous cyanobacterial septal pore (septum) family."]
- **Pfam PF24301** (FraC); **InterPro IPR054663** (FraC); **NCBIfam NF045624**
  (filament_FraC). No PANTHER family (PCC 7120 is not a PANTHER reference genome).
- This family is restricted to multicellular, filamentous, heterocyst-forming
  cyanobacteria (Nostocales), consistent with a dedicated role in the cyanobacterial
  septal junction / filament-integrity machinery rather than a housekeeping function.

## Functional interpretation for GO review

- **Molecular function:** FraC is a non-catalytic, structural integral-membrane
  component of the septal (intercellular-junction) machinery; best captured by
  **structural molecule activity (GO:0005198)**. Avoid the uninformative "protein
  binding".
- **Biological process:** Required for filament integrity and for gated intercellular
  molecular exchange; **cell-cell signaling (GO:0007267)** captures the calcein-transfer /
  intercellular-communication role. There is currently no dedicated GO term for the
  bacterial/cyanobacterial "septal junction" structure or for "filament integrity".
- **Cellular component:** Integral to the cytoplasmic (inner) membrane, localized to the
  intercellular septa; **plasma membrane (GO:0005886)** is the existing GOA CC and is
  well supported.

## Existing GOA annotation

- GO:0005886 plasma membrane, IEA, GO_REF:0000044 (UniProtKB-SubCell) — ACCEPT.

## Caveats

- Cached PMID:20487302 and PMID:7883709 are abstract-only; the experimental
  annotations rest on the full-text assays (GFP localization, calcein-transfer FRAP,
  mutant phenotyping) reported by those primary papers.
