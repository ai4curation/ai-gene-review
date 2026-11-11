# SCGB1A1 (rabbit uteroglobin / blastokinin, P02779) — review notes

Founding member of the secretoglobin superfamily; classic progesterone-binding, PLA2-inhibitory
secreted protein.

## Identity & structure
- UniProt UTER_RABIT P02779: "RecName: Full=Uteroglobin; AltName: Full=Blastokinin; AltName:
  Full=Secretoglobin family 1A member 1". Mature chain 22-91 after signal peptide 1-21.
- Antiparallel disulfide-linked homodimer. UniProt SUBUNIT: "Antiparallel homodimer; disulfide-linked
  (PubMed:2704039, PubMed:3656405)." Interchain disulfides Cys24<->Cys90'.
- Crystal structures PDB 1UTG (1.34 A) and 2UTG (1.64 A).
  [PMID:2704039 "Uteroglobin is a dimer of two independent polypeptide chains of 70 residues linked by
  two disulfide bridges"; "An oblong hydrophobic pocket is observed inside the dimer, and the possibility
  that it represents a progesterone-binding site is discussed"].
  [PMID:3656405 "Uteroglobin is a dimer and its secondary structure consists of four alpha-helices per
  monomer that align in an anti-parallel fashion"].

## Function
- Progesterone / steroid binding:
  [file:genes/RABIT/SCGB1A1/SCGB1A1-uniprot.txt CC:FUNCTION "Uteroglobin binds progesterone specifically
  and with high affinity"].
  [PMID:568483 "Uteroglobin, a steroid-binding protein of the uterine secretion of the rabbit which is
  induced by progesterone"].
  [PMID:281700 "near the progesterone binding site of blastokinin"]. → NEW GO:1990239 steroid hormone binding.
- Phospholipase A2 inhibitor:
  [file CC:FUNCTION "It is also a potent inhibitor of phospholipase A2"]. → NEW GO:0019834.
- Secreted; synthesized in uterus and lung; induced by progesterone (UniProt TISSUE SPECIFICITY / INDUCTION).

## GOA review decisions
- GO:0005576 extracellular region (IEA) — ACCEPT (curated Secreted).
- GO:0005737 cytoplasm (IEA TreeGrafter) — REMOVE (over-propagation; secreted protein, no cytoplasmic function).
- GO:0007165 signal transduction (IEA InterPro2GO IPR000329) — REMOVE (incorrect; uteroglobin is a
  ligand-binding/PLA2-inhibitor protein, not a signal transducer). Replaced by the two MF NEW terms.
