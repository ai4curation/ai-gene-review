# PIGO (Q8TEQ8) — curation notes

Human PIGO, HGNC:23215, UniProtKB Q8TEQ8. GPI ethanolamine phosphate transferase 3,
catalytic subunit ("PIG-O", GPI-ET-III). NCBITaxon:9606.

No deep-research file: falcon provider is out of credits (HTTP 402). Review grounded in
the UniProt record, the seeded GOA, and cached publications.

## Verified biology

- **Function / MF.** PIGO is the catalytic subunit of the GPI ethanolamine phosphate
  transferase 3 complex. It transfers a **bridging ethanolamine phosphate (EtNP) from
  phosphatidylethanolamine (PE) onto the 6-OH of the third mannose (Man3)** of the GPI
  intermediate. This is the EtNP to which the mature protein's C-terminus is ultimately
  attached by the GPI transamidase (the "protein-attachment" EtNP).
  - UniProt FUNCTION: "transfers an ethanolamine phosphate (EtNP) from a
    phosphatidylethanolamine (PE) to the 6-OH position of the third alpha-1,2-linked
    mannose ... participates in the tenth step of the glycosylphosphatidylinositol-anchor
    biosynthesis" [file:human/PIGO/PIGO-uniprot.txt].
  - Kinoshita review: "Two EtNPs are sequentially transferred to the 6-positions of Man3
    and then Man2 by PIGO [46] and PIGG (initially termed GPI7) [67]"
    [PMID:32156170]. Table 2 lists PIGO at step 10 as "GPI-ETIII, catalytic".
  - GO:0051377 "mannose-ethanolamine phosphotransferase activity" def = "Catalysis of the
    transfer of ethanolamine phosphate to a mannose residue in the GPI lipid precursor" —
    exact match. This is the GOA MF term (IBA + IEA + 3 IMP).

- **Complex / accessory subunit.** PIGO acts with PIGF, which stabilises it. UniProt
  SUBUNIT: "Part of the ethanolamine phosphate transferase 3 complex composed by PIGO and
  PIGF ... PIGF is required to stabilize PIGO" [file:human/PIGO/PIGO-uniprot.txt].
  Kinoshita: "Both PIGO and PIGG are stabilized by association with PIGF" [PMID:32156170].
  ComplexPortal CPX-2679 = "Glycosylphosphatidylinsitol ethanolamine-phosphate transferase
  III complex".

- **Localization.** ER membrane, multi-pass. "The core GPI is assembled on the
  endoplasmic reticulum (ER) membrane" [PMID:32156170]. UniProt SUBCELLULAR LOCATION:
  "Endoplasmic reticulum membrane ... Multi-pass membrane protein". 14 predicted TM
  helices. ISS from mouse ortholog Q9JJI6.

- **Disease.** Biallelic loss-of-function causes Hyperphosphatasia with impaired
  intellectual development syndrome 2 (HPMRS2 / Mabry syndrome; MIM 614749); phenotype
  spans infantile lethality → mild learning difficulties, with seizures, developmental
  delay, brachytelephalangy, elevated serum ALP. Patient variants (R119W, T130N, M344K,
  N370S, K1047E) reduce mannose-ethanolamine phosphotransferase activity in functional
  assays [file:human/PIGO/PIGO-uniprot.txt VARIANT notes; PMID:24417746, PMID:28337824,
  PMID:24049131].

## GOA annotation summary (19 lines)

- MF GO:0051377 mannose-ethanolamine phosphotransferase activity: IBA + IEA + 3×IMP → all
  ACCEPT (exact function; IMPs backed by variant activity assays + UniProt EC/305 sourcing).
- MF GO:0016772 transferase activity, transferring phosphorus-containing groups (IEA,
  InterPro): correct but a very high-level parent of GO:0051377 → MARK_AS_OVER_ANNOTATED.
- BP GO:0006506 GPI anchor biosynthetic process: IBA + IEA + 2×IMP + ISS → all ACCEPT
  (core process). One extra IMP (PMID:24049131) also ACCEPT.
- CC GO:0005789 endoplasmic reticulum membrane: IBA + IEA + 2×ISS + NAS → all ACCEPT.
- CC GO:0016020 membrane (HDA, PMID:19946888, NK-cell membrane proteome MS): true but
  uninformative parent of ER membrane → MARK_AS_OVER_ANNOTATED.

## Core functions

1. MF GO:0051377 mannose-ethanolamine phosphotransferase activity (GPI-ET-III; adds
   bridging EtNP to Man3).
2. directly involved in BP GO:0006506 GPI anchor biosynthetic process (step 10 of 11).
3. located in CC GO:0005789 endoplasmic reticulum membrane.
