# Lep (rat, P50596) - manual literature synthesis

No deep-research API was available for this review. This synthesis was written by
hand from the cached publications in `publications/`, the rat UniProt record
(`Lep-uniprot.txt`), the existing human LEP review in this repository
(`genes/human/LEP/`), and PubMed metadata lookups. Every claim carries its source.

## Identity and structure

- Rat leptin (gene *Lep*, RGD:3000, GeneID 25608) is a 167-residue precursor with a
  21-residue signal peptide and one disulfide (Cys117-Cys167), member of the leptin
  family with a four-helix cytokine-like core [file:rat/Lep/Lep-uniprot.txt
  "SIGNAL          1..21"; "Belongs to the leptin family."; InterPro IPR009079
  4_helix_cytokine-like_core].
- It is secreted [file:rat/Lep/Lep-uniprot.txt "SUBCELLULAR LOCATION: Secreted"] and
  circulates in serum, where its concentration tracks fat mass and nutritional state
  [PMID:21060836 "Serum leptin and total non-esterified fatty acids (NEFA) were elevated
  in HFD rats"].

## Molecular function: hormone acting through LEPR

- Leptin is an adipocyte hormone; the ob protein "serves an endocrine function to
  regulate body fat stores" [PMID:7624777 "These data suggest that the OB protein serves
  an endocrine function to regulate body fat stores."] (mouse).
- It binds the class I cytokine receptor LEPR and drives receptor assembly
  [PMID:36959263 "Leptin induces type I cytokine receptor assemblies featuring 3:3
  stoichiometry"] (human/mouse structural work).
- Rat receptor-signalling experiments: leptin induced STAT3 and MAPK tyrosine
  phosphorylation through rat OBRb, and MAPK only through OBRa [PMID:9618284 "As the
  result of leptin stimulation, enhanced levels of tyrosine phosphorylation of STAT3 and
  MAPK were detected in CHO-OBRb cells."]; leptin induced immediate early genes through
  both OBRb and OBRa [PMID:9070213 "which are induced by leptin addition, not only in CHO
  cells expressing the OBRb, but also in cells expressing one of the short form
  receptors, OBRa"].
- Rat leptin is also bound by the endocytic receptor megalin (LRP2), which mediates its
  renal clearance and its transport across the choroid plexus [PMID:15131016 "Megalin
  bound leptin in the presence of Ca(2+) and mediated its cellular internalization and
  degradation."; PMID:17324488 "We demonstrate that circulating leptin is transported
  into the brain by binding to megalin at the choroid plexus epithelium."]. This is
  cargo handling, not signalling.

## Central role: appetite and energy homeostasis

- In rat, PI3K is a key intracellular mediator of leptin-induced anorexia
  [PMID:11677594 title "Key enzyme in leptin-induced anorexia."] (no abstract cached).
- Chronic rAAV leptin in rats produced anorexia and increased energy expenditure, with
  persistent hypothalamic pSTAT3 [PMID:12130569 "phosphorylated signal transducer and
  activator of transcription-3 remained elevated for the duration of the study"].
- A central leptin antagonist increased food intake and weight gain on chow and high-fat
  diet [PMID:19726711 "Food consumption and body weight gain were exacerbated in the
  antagonist group during both chow and high-fat feeding periods"].
- Endogenous leptin activates hypothalamic JAK-STAT signalling already in newborn rats
  [PMID:21250909 "Systemically administered PEG-MLA effectively blocks leptin signal
  induction of hypothalamic JAK-STAT signaling."].
- Leptin regulates arcuate CART, an anorectic peptide [PMID:9590691 "Peripheral
  administration of leptin to obese mice stimulates CART mRNA expression."].
- Related (key paper requested for this review): TRH acting through hypothalamic
  histamine suppresses feeding in rats, and the authors propose that leptin activates
  histaminergic neurons indirectly via PVN TRH neurons [PMID:17760865 "it is likely that
  leptin may activate histaminergic neurons indirectly via neurons that release TRH"].
  This places leptin upstream of a TRH-histamine anorectic relay, but the paper does not
  itself test leptin.

## Neuroendocrine and reproductive effects

- Third-ventricle leptin raised serum LH and FSH in female rats [PMID:19112389 "The
  results showed that serum LH levels increased dramatically in group B, six hours after
  leptin administration."].
- Acute high-dose leptin inhibited gonadotrophin-induced ovulation in immature rats
  [PMID:17071778 "the ovulatory process was significantly inhibited in response to an
  acute treatment with leptin"], whereas leptin restores fertility of ob/ob mice
  [PMID:8589726 "recombinant human ob protein, leptin, into homozygous female ob/ob mice
  can correct their sterility"]: leptin regulates ovulation in both directions depending
  on dose and context.

## Peripheral (pleiotropic) effects in rat

- Heart: leptin increased palmitate oxidation in perfused hearts [PMID:12058043] and
  induced PPARalpha-dependent cardiomyocyte hypertrophy and ROS [PMID:20738325].
- Adipose: leptin reduced glyceroneogenesis and lipolytic gene expression via NO
  [PMID:21068181]; central leptin increased adipocyte apoptosis [PMID:17024416].
- Gut: luminal leptin induced chloride secretion [PMID:20203064], inhibited glutamine
  transport via ASCT2/B0AT1 [PMID:20448142], and reduced enterocyte apoptosis after
  resection [PMID:19730157].
- Vasculature and blood pressure: leptin gene transfer normalised blood pressure in
  diet-induced obese rats [PMID:20059648]; leptin attenuated phenylephrine
  vasoconstriction via iNOS [PMID:20978518].
- Immune and inflammatory: leptin up-regulated macrophage phagocytosis and
  pro-inflammatory cytokines [PMID:9438411]; primed microglial IL-1beta and TNF release
  [PMID:19922787]; increased leukocyte rolling and adhesion [PMID:20150963].
- Tissue cells: increased nucleus pulposus cell proliferation [PMID:18978578], catabolic
  effects on cartilage [PMID:19876764], hepatic stellate cell activation
  [PMID:19299451, PMID:20977462], improved bone growth in an IUGR model [PMID:21353474].

## Regulation of leptin itself (basis of most IEP rows)

Many rat rows are IEP: leptin mRNA or serum leptin changed with a stimulus (hypoxia /
ischemia [PMID:15284063], perinatal nutrition [PMID:15616803], estradiol
[PMID:12412816], retinoic acid [PMID:19212007], vitamin C [PMID:20400526], vitamin E
[PMID:20404018], ethanol [PMID:23380443, PMID:29089335], pregnancy [PMID:21303957],
circadian time [PMID:21164040], diet [PMID:21060836]). These describe regulation of the
*Lep* gene, not functions of the leptin protein.
