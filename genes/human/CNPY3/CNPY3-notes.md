# CNPY3 (Protein canopy homolog 3 / PRAT4A) — Review notes

UniProt: Q9BT09. Gene synonyms: CTG4A, ERDA5, PRAT4A (Protein Associated with TLR4), TNRC5. HGNC:11968. 278 aa precursor.

## Core biology

CNPY3 is an ER-resident, glycosylated protein with a signal peptide (1-30) and a single
Saposin B-type / MD-2-related lipid-recognition (ML) domain (47-271). It functions as a
Toll-like-receptor-specific co-chaperone for the ER HSP90 paralog HSP90B1 (gp96 / GRP94 / endoplasmin).

- UniProt FUNCTION: "Toll-like receptor (TLR)-specific co-chaperone for HSP90B1. Required for
  proper TLR folding, except that of TLR3, and hence controls TLR exit from the endoplasmic
  reticulum. Consequently, required for both innate and adaptive immune responses." [file:human/CNPY3/CNPY3-uniprot.txt FUNCTION; By similarity, ECO:0000250]
- UniProt SUBUNIT: "Interacts with HSP90B1; this interaction is disrupted in the presence of ATP.
  Interacts with TLR1, TLR2, TLR4 and TLR9. Strongest interaction with TLR4." [file:human/CNPY3/CNPY3-uniprot.txt SUBUNIT]
- UniProt SUBCELLULAR LOCATION: Endoplasmic reticulum. [file:human/CNPY3/CNPY3-uniprot.txt]
- Reactome pathway R-HSA-1679131 "Trafficking and processing of endosomal TLR"; events
  R-HSA-1678923 "TLR folding by chaperones GP96 and CNPY3" and R-HSA-1678944
  "Folded full-length TLR7/8/9 dissociates from the GP96:CNPY3 complex". [file:human/CNPY3/CNPY3-uniprot.txt DR Reactome]

The mechanism was established originally in mouse (PRAT4A): gp96/HSP90B1 and CNPY3/PRAT4A
form a TLR-folding module required for cell-surface TLRs (TLR1/2/4/5/6) and endosomal nucleic-acid-sensing
TLRs (TLR7/9) to exit the ER; TLR3 is CNPY3-independent. The interaction between CNPY3 and gp96
is ATP-sensitive, consistent with a HSP90-cochaperone client-handoff cycle. [PMID:20865800 "Folding of
Toll-like receptors by the HSP90 paralogue gp96 requires a substrate-specific cochaperone"; cited in
file:human/CNPY3/CNPY3-uniprot.txt RN 8]

## Disease

Biallelic loss-of-function variants in CNPY3 cause Developmental and epileptic encephalopathy 60
(DEE60, MIM:617929), autosomal recessive, with seizure onset in the first months of life.
A missense variant Gly125Arg is reported. [PMID:29394991 "Biallelic Variants in CNPY3, Encoding an
Endoplasmic Reticulum Chaperone, Cause Early-Onset Epileptic Encephalopathy"; file:human/CNPY3/CNPY3-uniprot.txt
DISEASE + RN 13]

## Feature / domain evidence (UniProt)

- Saposin B-type domain 47-271; this is the ML/saposin-like fold that mediates client engagement.
- Three disulfide bonds (49-206, 52-194, 104-166) stabilize the domain [ECO:0000250].
- N-glycosylation at Asn-153 [PMID:19159218].
- Belongs to the canopy family (CNPY1-4). PANTHER PTHR15382:SF2 "PROTEIN CANOPY HOMOLOG 3".

## Existing GO annotations (GOA) — assessment summary

1. GO:0005102 signaling receptor binding (IBA, GO_REF:0000033) — CNPY3 does physically engage TLR
   ectodomains in the ER as a folding chaperone client interaction. "signaling receptor binding" is a
   defensible MF for the TLR interaction but does not capture the chaperone activity. Keep as non-core;
   the chaperone MF terms are more informative.
2. GO:0005783 endoplasmic reticulum (IEA, GO_REF:0000044, from UniProt SubCell) — correct, ACCEPT.
3. GO:0005515 protein binding (IPI) x5 from high-throughput interactome screens (PMID:28514442,
   32296183, 32814053, 33961781). These are uninformative bare "protein binding" with WITH/FROM partners
   that are largely not functionally relevant (ATN1, CLDN5, DMWD, FAM209A, GOLM1, GRN, KCNJ6, KLK6,
   RNF11, SLITRK4, SPRED1, WFS1). MARK_AS_OVER_ANNOTATED per curation guideline (avoid bare protein binding).
4. GO:0005102 signaling receptor binding (IEA, GO_REF:0000107, ortholog transfer from mouse Q9DAU1) —
   redundant with the IBA; keep as non-core.
5. GO:0005788 endoplasmic reticulum lumen (TAS, Reactome) x2 — correct subcellular location, more
   specific than GO:0005783. ACCEPT.

## Candidate better / new terms

- MF: GO:0051082 unfolded protein binding (core chaperone activity).
- MF: GO:0051087 protein-folding chaperone binding and/or GO:0051879 Hsp90 protein binding
  (binds HSP90B1; co-chaperone). GO:0051879 is the most specific for the gp96 interaction.
- BP: GO:0034975 protein folding in endoplasmic reticulum (TLR folding in ER).
- BP: GO:0072657 protein localization to membrane / establishment of protein localization (TLR exit from ER).
- BP: GO:0045087 innate immune response (UniProtKB-KW Immunity/Innate immunity).
- BP: GO:0034123 positive regulation of toll-like receptor signaling pathway (required for TLR signaling).

Note: GO co-chaperone activity (GO:0003767) and chaperone cofactor-dependent refolding (GO:0051085) are
obsolete; GO:0061077 chaperone-mediated protein folding is obsolete. Use unfolded protein binding +
Hsp90 protein binding + protein folding in ER instead.
