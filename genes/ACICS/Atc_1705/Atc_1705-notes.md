# Atc_1705 (F9ZQD6): curation notes

- TrEMBL entry, Acidithiobacillus caldus SM-1. Name and EC 1.8.5.4 come from ARBA rules
  (unvetted). PE 3.
- **Type I (SqrA)**: 87.6% identical to the characterized A. ferrooxidans SQR AFE_1792
  (B7JBP8), with all three catalytic and FAD-proximal cysteines conserved (C128/C160/C356)
  (`file:ACIF2/AFE_1792/AFE_1792-bioinformatics/RESULTS.md`). SQR activity is a strong
  orthology inference, but the protein has not been assayed.
- A. caldus has several SQR copies, and their functional assignments rest on gene context
  [PMID:21687411 "the high similarity plus the conservation of gene context observed with A.
  ferrooxidans strongly suggests similar functional properties"]. That paper's sqr-1/sqr-2
  numbering refers to strain ATCC 51756 and could not be mapped to the SM-1 locus tag here.
  Other SM-1 SQR-family paralogs: Atc_1437, Atc_2423, Atc_2601.
- A 2026 study overexpressed and knocked out "SQR" in A. caldus and reported better chalcocite
  bioleaching [PMID:42031311 "In chalcocite bioleaching, the SQR overexpression strain enhanced
  sulfur metabolism and thereby increased the extraction of copper ions."]. Only the abstract
  is available, so the locus and strain could not be matched to Atc_1705. It is not used as
  annotation support.
- PANTHER places this protein in PTHR43755:SF1, while its ortholog B7JBP8 is in
  PTHR42913:SF6 (see RESULTS.md).

## Annotation decisions
- GO:0070224 (EC IEA): ACCEPT (orthology plus active-site conservation).
- GO:0016020: MODIFY to GO:0005886 plasma membrane.
- GO:0016491: TOO_GENERAL.

## CMMMech claim check
functional_role: "Membrane-bound sulfide-quinone reductase (EC 1.8.5.4; Atc_1705) in
Acidithiobacillus caldus SM-1 catalyzing sulfide oxidation coupled to quinone reduction at
moderately thermophilic leaching temperatures" (traction-battery-hydrometallurgical-residue).
- The activity is an orthology inference, not measured for Atc_1705. Nothing shows that this
  copy, rather than another A. caldus SQR paralog, acts at leaching temperatures. The CMMMech
  evidence note already says the strain is a stand-in for the CGMCC 1.15711 stock and that no
  genes were mutated. "catalyzing ... at moderately thermophilic leaching temperatures" should
  be read as putative.
