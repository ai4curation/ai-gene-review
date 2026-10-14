# SEP4 (AGL3, At2g03710, P29383) notes

## 2026-10-05 — initial review (floral_organ_identity_abce module)

- Identity: UniProt P29383 AGL3_ARATH. The primary name is AGL3, with synonym SEP4 [ECO:0000303|PubMed:15530395]; At2g03710. Checked. The folder and gene_symbol use SEP4.
- Deep research: falcon failed (HTTP 402).
- AGL3 binds SRF/MCM1-like CArG sequences and is expressed in vegetative above-ground organs as well as flowers [PMID:7632923].
- Ditta et al. 2004 [PMID:15530395 "floral organs are converted into leaf-like organs in sep1 sep2 sep3 sep4 quadruple mutants"]: SEP4 contributes to all organ types and to meristem identity. All the IMP organ-development and meristem-identity rows are ACCEPT. NEW GO:0010093 from the same paper.
- SAP54 phytoplasma effector rows (PMID:24714165, PMID:37965720): REMOVE, matching SEP3. This is pathogen targeting and says nothing about SEP4's own function.
- The SCL23 hit from the phytohormone interactome (PMID:32612234) is REMOVE as uninformative. The TAS "DNA binding" row is MODIFY to GO:0000978.
