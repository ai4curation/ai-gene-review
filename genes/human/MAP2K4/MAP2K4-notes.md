# MAP2K4 (MKK4 / SEK1 / JNKK1) curation notes

UniProt P45985, human, 399 aa, STE group MAP2K. Synonyms: MKK4, MEK4, JNKK1, SEK1, SERK1, SKK1.

## Identity and domains

- Dual-specificity MAP kinase kinase of the STE family, MAP2K subfamily
  [file:human/MAP2K4/MAP2K4-uniprot.txt "Belongs to the protein kinase superfamily. STE Ser/Thr"].
- N-terminal D domain (residues ~37-52) docks MAPK substrates; C-terminal DVD domain (364-387) docks MAP3Ks
  [file:human/MAP2K4/MAP2K4-uniprot.txt "The D domain (residues 34-52) contains a conserved docking"].
- The D-site is "necessary and sufficient" for high-affinity binding of JNK1-3 and p38alpha/beta
  [PMID:12788955 "This docking site was both necessary and sufficient for the high affinity binding of the MAPKs JNK1, JNK2, JNK3, p38 alpha, and p38 beta to MKK4."].
- The ~86-residue N-terminal regulatory region is intrinsically disordered and folds upon binding to
  p38alpha or JNK1 in two different conformations with comparable affinity
  [PMID:34439869 "the promiscuous interaction of the disordered regulatory domain of MKK4 with p38α and JNK1 is facilitated by folding-upon-binding into two different conformations"].
- Anthrax lethal factor cleaves the N terminus (two sites), destroying the D-site
  [Reactome:R-HSA-5211391 "cleaves MAP2K4 (MEK4, mitogen activated protein kinase kinase 4)"].

## Activation (upstream)

- Activated by MAP3K phosphorylation of Ser257/Thr261 in the activation loop
  [file:human/MAP2K4/MAP2K4-uniprot.txt "Activated by phosphorylation on Ser-257 and Thr-261 by MAP kinase"];
  MEKK1 [Reactome:R-HSA-2730896], TAK1 [Reactome:R-HSA-450337], MLK3 [PMID:9003778 "Immunoprecipitated MLK-3 catalyzed the phosphorylation of SEK1 in vitro"].
- MEKK1 binds the N-terminal extension of JNKK1; JNK and MEKK1 compete for binding, suggesting sequential
  MEKK1:JNKK1 then JNKK1:JNK interactions
  [PMID:9808624 "As JNK and MEKK1 compete for binding to JNKK1 and activation of JNKK1 prevents its binding to MEKK1"].

## Catalytic function (downstream)

- Original identification as JNKK: activates JNKs and p38 but not ERK
  [PMID:7716521 "JNKK activated the JNKs but did not activate the ERKs and was unresponsive to Raf-1 in transfected HeLa cells."];
  [PMID:7839144 "Two human MAP kinase kinases (MKK3 and MKK4) were cloned that phosphorylate and activate p38 MAP kinase."].
- Preference for JNK Tyr185 (MKK7 prefers Thr183); cooperation with MKK7 required for optimal JNK activation
  [PMID:16533805 "Optimal activation of JNK requires the activity of both MKK4 and MKK7"];
  [Reactome:R-HSA-168162 "MKK4 shows a striking preference for the tyrosine residue (Tyr-185)"].
- Loss of MKK4 in cells: JNK activity reduced ~80%, p38 ~20%
  [Reactome:R-HSA-450337 "JNK and p38 MAPK activities were decreased by around 80% and 20%, respectively"].
- Unlike MKK7 (JNK-only), MKK4 additionally activates p38 MAPKs
  [file:human/MAP2K4/MAP2K4-uniprot.txt "exclusively activates JNKs, MAP2K4/MKK4 additionally activates the p38"].
- No established serine-only or tyrosine-only substrates outside the MAPK TxY motifs; generic
  Rhea/EC-derived "protein serine kinase" and "protein tyrosine kinase" terms are best replaced by
  GO:0004708 MAP kinase kinase activity (same choice as MAP2K3 review).

## Location

- UniProt: Cytoplasm and Nucleus (by similarity, ECO:0000250). Reactome places the reactions in cytosol.
  Deep research: cytoplasmic and nuclear, context-dependent
  [file:human/MAP2K4/MAP2K4-deep-research-falcon.md "Its working localization is best annotated as **cytoplasmic and nuclear, dynamic and cell-context dependent**."].

## Biology / pleiotropy

- Stress activators: UV, gamma irradiation, heat shock, hyperosmolarity, peroxide, cytokines
  [file:human/MAP2K4/MAP2K4-uniprot.txt "Activated in response to a variety of cellular"].
- Tumour suppressor in some epithelial cancers (lung adenocarcinoma, Ahn 2011), pro-metastatic in others;
  MKK4 inhibition (HRX215) promotes liver regeneration via rerouting to MKK7-JNK1 (Zwirner 2024) - from the
  falcon deep-research report; not independently verified here and not used for GO annotation.

## Annotation decisions (summary)

- Core MF: MAP kinase kinase activity (GO:0004708) and its child JUN kinase kinase activity (GO:0008545).
- Core BP: JNK cascade (GO:0007254); p38MAPK cascade (GO:0038066) proposed NEW (MKK4 catalyses p38 activation;
  comparator MAP2K3/MAP2K6 carry the term; MKK4 performs the catalytic step so participation test is met).
- Protein binding rows: MAPK partners (JNK1/JNK2/p38alpha) -> GO:0051019 (matching the MAP2K3/MAP2K6 choice for
  substrate MAPK partners); MEKK1 -> GO:0031435; TRIB1 (pseudokinase, abstract-only) -> REMOVE.
- IEP cellular response to mechanical stimulus (PMID:19593445): the cached full text of this paper (BAD in prostate
  cancer) does not mention MKK4 or mechanical stimulation anywhere; same PMID is used for IEP mechanical-stimulus rows
  on FAS, GADD45A, MAP3K1, TNFRSF1A, suggesting a batch mis-citation. Marked UNDECIDED rather than REMOVE
  (curator decision, true source unknown).
- Mouse-derived IEA (Ensembl Compara from P47809): NMJ development source is an erbB2 mutant paper (PMID:10521398)
  -> over-annotation; SMC apoptosis / H2O2 apoptosis (PMID:24705900, miR-92a/MKK4-JNK) and ERBB signalling kept
  as non-core.
