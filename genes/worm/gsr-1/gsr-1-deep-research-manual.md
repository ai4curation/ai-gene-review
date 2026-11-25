# gsr-1 (C46F11.2; UniProt Q93379) - manual literature research

No deep-research provider API was available for this review; this file records a manual
literature survey done from the cached publications (`publications/PMID_*.md`) and a PubMed
search (`gsr-1 glutathione reductase elegans`, 6 hits: PMIDs 40333285, 33096249, 30770874,
27117030, 23593298, 21199936).

## Identity and family

- gsr-1 encodes the only glutathione reductase (GR, EC 1.8.1.7) of *C. elegans*
  [PMID:23593298 "gsr-1 is the sole GSR encoding gene found in C. elegans"].
- Class-I pyridine nucleotide-disulfide oxidoreductase (UniProt SIMILARITY; InterPro IPR006322
  Glutathione_Rdtase_euk/bac; NCBIfam TIGR01421 gluta_reduc_1; PANTHER PTHR42737:SF2).
  It conserves the FAD and NADPH domains and the redox-active CVNVGC disulfide
  [PMID:27117030 "C. elegans GSR-1 is highly homologous through all protein domains to vertebrate glutathione reductases, including the conserved redox active site CVNVGC"].
- Two isoforms from alternative first exons/start codons: GSR-1a (473 aa, Q93379-1) with a
  14-residue N-terminal extension that acts as a mitochondrial targeting sequence, and GSR-1b
  (459 aa, Q93379-2) that is cytoplasmic [PMID:27117030 "the C. elegans gsr-1 gene encodes both mitochondrial (GSR-1a) and cytoplasmic (GSR-1b) isoforms"].

## Enzyme activity (direct evidence)

- Recombinant His-tagged GSR-1 (1380-bp ORF, i.e. the GSR-1b form) is an active homodimer that
  reduces GSSG with NADPH; Km 34.1 uM (GSSG) and 12.9 uM (NADPH)
  [PMID:23593298 "The protein catalysed the reduction of GSSG by using NADPH as an electron donor."].
- Recombinant GSR-1b reduces GSSG dose-dependently; the tm3574 in-frame deletion (Delta193-302,
  removing most of the NADPH domain) is inactive; GSR-1b has no thioredoxin reductase activity
  with yeast TRX3 or worm TRX-2 [PMID:27117030 "GSR-1b did not function as thioredoxin reductase when using either yeast TRX3 or worm TRX-2 as substrates"].

## Localization

- PGSR-1::GSR-1::GFP is mainly cytosolic in the 2013 study
  [PMID:23593298 "only strong cytosolic GFP expression was observed, possibly obscuring lesser granular mitochondrial GFP signals"].
- ATG-mutant GFP fusions separate the isoforms: GSR-1a gives a punctate mitochondrial pattern,
  GSR-1b a diffuse cytoplasmic pattern; the 14-aa extension alone targets GFP to mitochondria
  co-localizing with TOMM-20::mRFP [PMID:27117030 "the additional 14 amino acids of GSR-1a constitute a functional MTS on its own"].
- The MTS is predicted cleavable, placing GSR-1a in the matrix (prediction, not assayed)
  [PMID:27117030 "This predicts that GSR-1a is located in the mitochondrial matrix"].
- Expression: intestine, pharynx, vulval muscle, tail cells (2013); pharynx strongest, also
  hypodermis, spermatheca, coelomocytes, gonad sheath, some neurons (2016).

## Physiology / phenotypes

- Oxidative stress: among 67 GSH-metabolism genes, only gsr-1 RNAi abolished juglone tolerance;
  gsr-1 RNAi also sensitizes to paraquat and, less, organic hydroperoxides; not to arsenite
  [PMID:23593298 "GSR-1 was also found to be crucial for the tolerance against other pro-oxidants including paraquat and to a lesser extent cumene hydroperoxide and tert-butylhydroperoxide"].
- Redox state: RNAi barely changes GSH or GSH/GSSG at baseline, but under juglone the GSH/GSSG
  ratio falls to ~6:1 vs ~20:1 in controls; gsr-1 RNAi induces gcs-1 and gst-4 reporters.
- Overexpression increases juglone resistance and extends lifespan; RNAi shortens lifespan.
- gsr-1 expression is induced by juglone and starvation in a SKN-1 (not DAF-16) dependent manner
  [PMID:23593298 "These data strongly suggest that the gsr-1 promoter is regulated by SKN-1 and not by DAF-16."].
- Molting: gsr-1 RNAi in trxr-1 mutants causes molting arrest with oxidized cuticle disulfides;
  exogenous GSH reduces cuticle disulfides and induces apolysis (abstract only)
  [PMID:21199936 "molting involves the regulated reduction of cuticle components driven by TRXR-1 and GSR-1"].
- Embryogenesis: gsr-1(tm3574) is maternal-effect embryonic lethal (arrest at 17-103 cells, cell
  division delay, abnormal peripheral chromatin); cytoplasmic GSR-1b but not mitochondrial
  GSR-1a rescues [PMID:27117030 "cytoplasmic GSR-1b is essential for embryonic development"].
- gsr-1(m+,z-) animals show mitochondrial fragmentation, reduced membrane potential and
  mitochondrial UPR induction [PMID:27117030 "decreased gsr-1 levels cause mitochondrial stress and dysfunction"].
- Proteostasis: gsr-1 mutants enhance toxicity of aggregation-prone proteins and block HLH-30
  nuclear translocation and SQST-1 degradation (PMID:30770874, abstract).
- Suppression: loss of NMD suppresses gsr-1 embryonic lethality through cth-1/cth-2
  transsulfuration (cysteine supply), not through the thioredoxin system (PMID:40333285).

## Summary

GSR-1 is the sole NADPH-dependent glutathione disulfide reductase of the worm, present in the
cytosol (GSR-1b) and mitochondria (GSR-1a). Its catalytic activity is directly shown. Its
organismal roles (oxidative-stress tolerance, lifespan, molting, embryogenesis, proteostasis)
all follow from keeping glutathione reduced; these are downstream consequences rather than
separate molecular activities.
