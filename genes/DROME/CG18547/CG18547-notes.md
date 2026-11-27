# CG18547 (Q9VGF3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output or prediction-evidence files were opened for this re-review.

### Identity
- Q9VGF3 is the single UniProt entry for FlyBase FBgn0037973 (CG18547), 345 aa, sequence
  version 1, TrEMBL (unreviewed), the full-length CG18547-RA product (RefSeq NP_650138.1).
  It is not a fragment, isoform or alternative gene model. Pfam PF00248 aldo-keto
  reductase domain spans 38-314.
- Bioinformatics (`CG18547-bioinformatics/RESULTS.md`): full AKR Asp-Tyr-Lys-His tetrad
  retained (D71, Y76, K102, H143, aligned to O81884 D54/Y59/K87/H124).

### Evolutionary placement (PANTHER 19, PTHR42686:SF1)
- CG18547 is one of three Drosophila-specific paralogs (with CG3397, CG12224) under
  duplication node PTN000199437; the Ecdysozoa node PTN000199440 joins them with
  C. elegans mec-14 (Q20127). No vertebrate member exists.
- Yeast ARA2 (D-arabinose dehydrogenase, NAD+) is in the sister fungal clade
  (LCA = Opisthokonts PTN000199433). Arabidopsis LGALDH (L-galactose dehydrogenase)
  is in the plant clade (LCA = Eukaryota PTN000199432).
- PAINT placed GO:0010349 (L-galactose DH) at the plant node PTN000920391 and
  ARA2's D-arabinose DH + GO:0070485 at the fungal node PTN000920371. CG18547 gets only
  GO:0016491 from the SF1 root PTN002448388. These omissions are treated as deliberate.

### Literature
- No biochemical, genetic or localisation study of CG18547 protein (deep research,
  falcon). Transcript is a marker of a GST-rich lymph gland prohemocyte subcluster
  (Cho et al. 2020, via deep research), and appears in high-fat diet and fred-RNAi
  transcriptome lists. These are expression observations, not function.
- mec-14 (the worm co-ortholog) has only genetic touch-sensitivity data
  (PMID:8692859, Gu, Caldwell & Chalfie 1996, dominant enhancer interactions among
  mec genes); no enzymology.

### Decisions
- GO:0016491 oxidoreductase activity (IBA + IEA): ACCEPT; this is the level PAINT chose
  and the level the evidence supports. Not refined to GO:0016616 because PAINT did not
  place a CH-OH/NAD(P) term at the SF1 root node.
- GO:0010349 L-galactose dehydrogenase activity (IEA, InterPro IPR044479 LGALDH-like):
  MARK_AS_OVER_ANNOTATED. InterPro2GO transfer of a plant-ascorbate-pathway activity to a
  metazoan clade that PAINT excluded; L-galactose oxidation is the first step of the
  plant Smirnoff-Wheeler pathway, not known in insects.
- GO:0070485 dehydro-D-arabinono-1,4-lactone biosynthetic process (ISS from ARA2,
  FlyBase): MARK_AS_OVER_ANNOTATED. Erythroascorbate synthesis is a fungal pathway;
  PAINT confined it to the Dikarya node; fly sits in the sister metazoan clade.
- Previously both were UNDECIDED; tree placement now gives a positive reason to demote
  them.

### Relative for next review
- C. elegans mec-14 (Q20127): co-ortholog by PANTHER Ecdysozoa speciation node
  PTN000199440; no review in repo. Experimental data are genetic only.
- Nearest biochemically characterised member: yeast ARA2 (Q04212), already COMPLETE at
  genes/yeast/ARA2/ARA2-ai-review.yaml.

### Family/module observations
- interpro/panther/PTHR42686/PTHR42686-review.yaml lists CG18547 in SF1, consistent with
  UniProt (PTHR42686:SF1). No disagreement on subfamily; note that SF1 is the only
  subfamily and spans LUCA, so "same subfamily" carries no functional weight here.
- modules/erythroascorbate_biosynthesis.yaml uses the whole PTHR42686 family as the
  selector for the Ara2-type D-arabinose dehydrogenase step. That family includes the
  metazoan and plant clades (CG18547, mec-14, LGALDH), which do not perform this step;
  the fungal node PTN000920371 would be the accurate selector.
