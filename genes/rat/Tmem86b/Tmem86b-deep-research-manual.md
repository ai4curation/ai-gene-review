# Tmem86b (rat, UniProt B0BNF0) - manual literature review

No deep-research provider was available; this summary was compiled manually from cached
publications (publications/PMID_*.md) and PubMed searches ("TMEM86B OR lysoplasmalogenase",
25 hits, of which the gene-specific primary papers are summarised below).

## Identity

- Rat Tmem86b, 233 aa, eight predicted transmembrane helices, Pfam PF07947 YhhN,
  InterPro IPR012506 (TMEM86B-like), PANTHER PTHR31885:SF7 (LYSOPLASMALOGENASE).
  RGD:1593455, GeneID 690610.
- Paralog: Tmem86a (42% identity in rat) [PMID:21515882 "Tmem86b has 42% identity to another
  protein, Tmem86a"].

## Enzymatic activity (lysoplasmalogenase, EC 3.3.2.2)

- Wu et al. 2011 purified lysoplasmalogenase ~500-fold from rat liver microsomes and identified
  the ~19 kDa band as Tmem86b by mass spectrometry [PMID:21515882 "Rat liver microsomal
  lysoplasmalogenase was solubilized with octyl glucoside and purified 500-fold to near
  homogeneity using four chromatography steps."]. Km ~50 uM for both lysoplasmenylcholine and
  lysoplasmenylethanolamine; pH optimum 7.0; competitively inhibited by lysophosphatidic acid.
- The enzyme is specific for the sn-2-deacylated (lyso) form and does not act on diradyl
  plasmalogen [PMID:21515882 "Lysoplasmalogenase is a microsomal enzyme highly specific for the
  sn-2-deacylated form of plasmalogen and has no activity with diradyl plasmalogen"].
- Heterologous expression of human TMEM86B in HEK293T cells and in E. coli (which lacks
  plasmalogens and the activity) conferred lysoplasmalogenase activity, establishing that the
  protein itself is the enzyme rather than an activator [PMID:21515882].
- Kummer et al. 2025 developed an HPLC/dansylhydrazine assay, detected activity after
  transient expression of TMEM86A or TMEM86B, and found that most point mutations at
  predicted catalytic positions abolished activity, except histidine-108 and serine-182 in
  TMEM86B [PMID:40024572].
- Bacterial YhhN proteins (Legionella Lpg1991, M. tuberculosis Rv1401) are also
  lysoplasmalogenases, so the activity is ancestral to the YhhN family [PMID:25445671;
  PMID:35314194].

## Location

- Rat activity is in liver microsomes (ER-derived), and the protein is a multi-pass integral
  membrane protein [PMID:21515882 "Tmem86b is a hydrophobic transmembrane protein of the YhhN
  family."]. In transfected HEK293T cells the protein and activity were in membrane fractions
  (only ~1% of activity in cytosol) and immunofluorescence showed a reticular cytoplasmic
  distribution [PMID:21515882 "The immunofluorescence provided evidence that TMEM86b is located
  throughout the cytoplasm (green)."]. Paralog TMEM86A is ER-localised (UniProt Q9D8N3).

## Physiology

- Liver expresses the highest Tmem86b mRNA, matching tissue activity [PMID:21515882].
- Overexpression in HEK293T reduced plasmalogen levels [PMID:21515882].
- Global and hepatocyte-specific Tmem86b knockout mice are viable, with elevated plasmalogens
  and lysoplasmalogens in plasma, liver and NK cells [PMID:40245986].

## Annotation issues found

- GO:0047826 D-lysine 5,6-aminomutase activity (EC 5.4.3.3, a bacterial adenosylcobalamin-
  dependent enzyme) is asserted on human TMEM86B (Q8N661) as IDA:UniProtKB from PMID:21515882,
  a paper that only measures lysoplasmalogenase. This appears to be a curator mis-mapping; it
  has propagated to rat by IBA, ISS and ISO.
