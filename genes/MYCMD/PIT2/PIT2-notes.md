# PIT2 (UMAG_01375, A0A0D1EAR7) — curation notes

## 2026-10-02 initial review

Sources: UniProt entry, GOA (3 rows, all `extracellular region`), the Falcon deep research file, and the
cached papers PMID:21692877 (abstract only), PMID:27093436 (full text), PMID:23459172 (full text, newly
cached) and PMID:30952847 (full text, newly cached).

### Identity
- Secreted 120-aa effector of *Ustilago maydis*. Signal peptide 1-25. Encoded next to *pit1*
  (transmembrane protein) in the pit cluster. Not related to the rice NLR also called Pit2.
- "Pit2 is secreted to the biotrophic interface" [PMID:21692877 "Pit1 localizes to the fungal plasma membrane at hyphal tips, endosomes and vacuoles while Pit2 is secreted to the biotrophic interface."]

### Molecular function: PLCP inhibitor
- [PMID:23459172 "We now show that Pit2 functions as an inhibitor of a set of apoplastic maize cysteine proteases, whose activity is directly linked with salicylic-acid-associated plant defenses."]
- Y2H: binds CP1A, CP1B, CP2 and XCP2, but not CatB. Co-IP with CP2. Recombinant Pit2 at 10 uM inhibits
  CP2 by 85% [PMID:23459172 "Moreover, addition of 10 µM Pit2 resulted in an 85% inhibition of CP2 (Figure 1E)."]
- Specificity [PMID:23459172 "Together, we conclude from these data that Pit2 functions as an inhibitor of the apoplastic maize cysteine proteases CP1A, CP2 and XCP2 but not CatB."]
- PID14 motif (aa 44-57). Mutant 49-53 loses inhibition [PMID:23459172 "By contrast to the native protein, Pit2mut49–53 did not cause a significant inhibition of protease activity when being applied at similar concentrations (Figure 6A)."]. The mutant proteins still localize to the interface, so their loss of virulence is biochemical and not a trafficking defect.
- The free PID14 peptide also inhibits CatB, so the specificity of the intact protein comes from the
  flanking regions [PMID:23459172 "PID14, in contrast to full length Pit2, also inhibits CatB"].
- Substrate-mimic model [PMID:30952847 "Pit2 is a suitable substrate for apoplastic PLCPs and its processing releases the embedded inhibitor peptide, which in turn blocks PLCPs to modulate host immunity."]
- Both processing and inhibition are needed [PMID:30952847 "Both features, substrate recognition by PLCPs and subsequently PLCP inhibition, are required for full Pit2 virulence function in maize"].

### Process / pathway
- The targets CP1 and CP2 process PROZIP1 into Zip1, which amplifies SA defence (Ziemann et al. 2018,
  via the deep research file; that paper is not cached here).
- Deletion phenotype [PMID:23459172 "Deletion mutants for pit2 successfully penetrate host cells but elicit various defense responses, which stops further fungal proliferation."]

### Regulation (fungal side, not a Pit2 function)
- The UPR regulator Cib1 binds the UPRE in the pit1/pit2 promoter. ER stress increases secretion
  [PMID:27093436 "Secretion of Pit2-mCherry is strongly increased upon ER stress and dependent on Cib1"].

### Curation decisions
- All 3 `extracellular region` rows: ACCEPT.
- NEW GO:0004869 cysteine-type endopeptidase inhibitor activity (IDA, PMID:23459172). Comparator:
  *P. infestans* EPIC2B (D0NBV3), an apoplastic PLCP-inhibitor effector, has GO:0004869/GO:0030414 in GOA.
- NEW GO:0140403 effector-mediated suppression of host innate immune response (IMP). EPIC2B carries the
  parent term GO:0052170. I did not use GO:0140502 (SA-signalling suppression, which CMU1 uses) because
  Pit2 acts on proteases that amplify SA signalling, not on SA itself. This is raised as a question in the
  review.
- NEW GO:0140593 host apoplast, which matches CMU1.
- GO ids checked in QuickGO: GO:0004869, GO:0140403 (is_a GO:0052170, GO:0140590), GO:0140593 and
  GO:0140502 are all current.

### Open / not used
- A 2025 bioRxiv preprint (Mendoza-Rojas et al.) reports a Pit2-derived peptide that activates the fungal
  GPCR Gpe1. It is not peer reviewed and was not annotated.
