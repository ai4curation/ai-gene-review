# uvrA (UvrABC system protein A) - Escherichia coli K-12 (P0A698)

Provider deep research was unavailable for this review (no provider API keys in the
session), so no `-deep-research-<provider>.md` file exists. These notes are built from the
cached publications in `publications/` and the UniProt record `uvrA-uniprot.txt`.

## Function
- UvrA is the initial damage-sensing ATPase of bacterial nucleotide excision repair (NER).
  [PMID:19208636 "The UvrA protein is the initial damage-recognizing factor in bacterial nucleotide excision repair."]
- Damage-specific DNA binding by UvrA alone (no UvrB) was shown by AFM on a defined lesion.
  [PMID:19208636 "AFM analysis of UvrA bound to a DNA substrate containing a defined lesion revealed that ATP is not required for damage detection."]
  [PMID:19208636 "UvrA (in absence of UvrB) binds DNA with a preference for single-stranded or damaged DNA (13,14)."]
- ATPase: each monomer has two ABC-type ATPase sites; hydrolysis (not mere binding) drives dimerization.
  [PMID:19208636 "This strongly suggests that it is not the binding of ATP that stimulates formation of UvrA dimers, but the hydrolysis of ATP to ADP."]
- UvrA acts catalytically to load UvrB onto lesions; it is not part of the incision complex.
  [PMID:2546148 "Under conditions of saturating UvrB protein approximately one UvrB molecule binds to DNA per damaged site in a reaction that requires catalytic amounts of UvrA subunit."]
  [PMID:19183285 "As in global repair, UvrA loads UvrB onto the damaged DNA to initiate repair."]
  [PMID:19183285 "After the damage is found, UvrA hydrolyzes ATP, dissociates from the complex, and the UvrB-DNA preincision complex is formed."]
- The scanning complex is UvrA2B2.
  [PMID:12145219 "we show here that the damage recognition complex consists of two UvrA and two UvrB subunits"]
- UvrA is the docking point for the transcription-repair coupling factor Mfd and for the
  alkyltransferase-like protein Atl (YbaZ).
  [PMID:22331906 "recruits the Uvr(A)BC nucleotide excision repair machinery via UvrA binding"]
  [PMID:19269902 "The YbaZ protein is shown to interact with UvrA."]
- Substrate range includes oxidative lesions as well as bulky adducts.
  [PMID:2690930 "In this study we show that the E. coli nucleotide excision repair enzyme (A)BC excinuclease removes from DNA the two major products of oxidative damage, thymine glycol and the baseless sugar (AP site)."]

## Regulation
- uvrA is an SOS (LexA-repressed) gene; UvrA levels rise after UV.
  [PMID:19183285 "The SOS regulon includes the uvrA and uvrB genes involved in the nucleotide excision repair (NER) pathway"]

## Zinc
- About 2 Zn per molecule; Cys253 (first C4 zinc finger) mutation reduces activity
  (UniProt MISCELLANEOUS and MUTAGEN, PubMed:2550431).

## Curation notes
- GOA row GO:0005515 IPI from PMID:19458048 (a PBP1b crystal-structure paper, IntAct) with
  UvrB as partner: the abstract does not mention UvrA or UvrB; full text not cached.
  Suspected wrong reference; recorded as a SUSPECTED source defect with CHECK.
- GOA row GO:0005515 IPI from PMID:19516334 with UvrB as partner: the cached full text
  reports Atl-UvrA and Atl-UvrC far-western interactions but no UvrA-UvrB assay in the text
  (figure/supplement not cached). Removed under the protein-binding policy regardless.
- Generic terms (DNA binding, DNA repair, DNA damage response, catalytic activity,
  cytoplasm, DNA repair complex, identical protein binding) are MODIFIED to the specific
  terms; same choices applied to P. putida KT2440 UvrA (Q88QK7) for shared terms.
