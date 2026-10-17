# ENTR1 (donkey, A0A8C4MKL2) notes

## Sequence and record

- Unreviewed TrEMBL entry, 356 aa, "Endosome-associated-trafficking regulator 1"; PANTHER
  PTHR31259:SF3; Pfam ENTR1 coiled-coil region (PF29363) at 178..347
  [file:EQUAS/ENTR1/ENTR1-uniprot.txt "Belongs to the ENTR1 family."].
- No literature on donkey ENTR1. All 8 GOA rows are TreeGrafter IEA (GO_REF:0000118) from
  PTN009117290.
- Pairwise comparison to human Q96C92 (435 aa): 81.41% identity over 355 paired residues; the
  donkey sequence covers only 81.61% of human
  [file:EQUAS/ENTR1/ENTR1-bioinformatics/RESULTS.md "Paired coverage is 81.61% of the human sequence and 99.72% of the donkey sequence."].
  Inspection of `alignment.txt`: RESULTS.md lists human residues 9-85 as unpaired;
  donkey residue 9 onward aligns from human residue ~86. The donkey sequence also begins with Gln
  ("QPPVHAAP..."), not Met, so this entry is most likely an N-terminally incomplete gene model
  (UniProt does not flag it as a fragment). Seven donkey ENTR1 entries exist in UniProt
  (351-476 aa; UniProt REST query 2026-10-14), so longer models of the same gene exist.
- Consequence: the human N-terminal region (aa 1-100) is the one shown to be necessary and
  sufficient for basal-body localization, ciliogenesis rescue and IFT88 binding
  [PMID:27767179 "Amino acids 1-100 of SDCCAG3 are necessary and sufficient for basal body localization"].
  Human UniProt also maps GIT1 binding to the N-terminus
  [file:EQUAS/ENTR1/ENTR1-bioinformatics/human_Q96C92-uniprot.txt "Interacts (via N-terminus) with GIT1"].
  The conserved C-terminal coiled-coil region is intact.

## Human ortholog biology

- Endosomal protein (early and recycling endosomes) with roles in receptor sorting, cytokinesis
  and ciliogenesis [file:EQUAS/ENTR1/ENTR1-bioinformatics/human_Q96C92-uniprot.txt
  "Endosome-associated protein that plays a role in membrane receptor sorting, cytokinesis and ciliogenesis"].
- SNX27-retromer cargo recycling: VPS35 interactome identified SDCCAG3; depletion caused
  trafficking defects of retromer cargo [PMID:25278552 "Depletion of these proteins resulted in trafficking defects of retromer-dependent cargo"].
  Human GOA (QuickGO 2026-10-14) has GO:0032456 endocytic recycling (IMP, PMID:25278552) and
  GO:0030904 retromer complex only as `colocalizes_with` (IDA, PMID:25278552).
- Cilia: basal body localization, IFT88 interaction, PKD2 ciliary localization
  [PMID:27767179 "we demonstrate that SDCCAG3 is important for ciliary localization of the membrane protein Polycystin-2"].
- Cytokinesis/midbody (PMID:23108400, not cached; cited via human UniProt text).

## Decisions

- Endosome localizations (early, recycling): ACCEPT, core.
- Cytokinesis, midbody, centrosome: KEEP_AS_NON_CORE.
- Cilium-related terms: KEEP_AS_NON_CORE for the gene, with the caveat that this entry lacks the
  N-terminal region that mediates these roles in human.
- NEW: GO:0032456 endocytic recycling (ISS from human IMP), as the core process.

## ProtNLM2 (donkey40 snapshot)

- GO:0032456 endocytic recycling -> COR (not in donkey GOA; supported by human IMP).
- GO:0030904 retromer complex -> UNC (human evidence is colocalization/interaction, not
  subunit membership).
- Non-GO: subcellular_location "Membrane" (not scored).
