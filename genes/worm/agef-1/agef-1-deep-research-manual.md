# agef-1 (C. elegans) - manual literature review

No deep-research API was available for this session. This file was written by hand from
PubMed searches (queries "agef-1 elegans"; "(AGEF-1 OR agef-1 OR BIG2 OR ARFGEF) AND
Caenorhabditis elegans AND (Golgi OR dense core OR insulin OR neuron)") and from the cached
publications in `publications/`. Every claim carries its source.

## Identity

- Gene: agef-1 (Y6B3A.1, WBGene00012386), chromosome I. UniProt G5EFH7 (TrEMBL, unreviewed),
  1594 aa, isoform a.
- Domain architecture (UniProt/InterPro): DCB, HUS, Sec7 (residues 506-695, PROSITE PS50190),
  HDS (Mon2/Sec7/BIG1-like) and BIG2_C domains. PANTHER PTHR10663:SF375.
- Orthology: the single C. elegans member of the large BIG/Sec7 subfamily of Arf GEFs;
  orthologous to human ARFGEF1 (BIG1) and ARFGEF2 (BIG2), yeast Sec7p and Drosophila Sec71
  [PMID:25329472 "elegans AGEF-1, a homolog of yeast Sec7p and the mammalian BIG1 and BIG2 Arf GEFs, as negatively regulating EGFR/Ras/MAPK-mediated vulva induction"].
  The distinct GBF1-subfamily paralog is GBF-1 (C24H11.7) [PMID:23840591].

## Molecular function

- No in vitro exchange assay has been published for the worm protein. The GEF assignment rests
  on the conserved Sec7 domain and the established activity of BIG1/BIG2
  [PMID:25329472 "BIG1 and BIG2 are Sec7 domain containing guanine nucleotide exchange factors (GEFs) for class I Arf GTPases"].
- In vivo, a Sec7 glutamic-finger mutant designed from the catalytically dead BIG2 E738K
  (AGEF-1[E608K]; E608 lies in the Sec7 domain of G5EFH7) acts as a dominant negative and
  phenocopies loss of agef-1 in the epidermis, and human BIG2 rescues the worm mutant
  [PMID:42312793 "To test this notion, we engineered a dominant negative agef-1 cDNA (AGEF-1[E608K]), which mimics a previously validated mutation in BIG2 that renders the SEC7 domain catalytically inactive"]
  [PMID:42312793 "Importantly, we found that SKIN::BIG2 fully restored the penetrance of PLM axon breaks"].
  This shows that Sec7 catalytic activity is needed for the in vivo function.
- Genetic partners: ARF-1.2 and ARF-3 act with AGEF-1 in vulval signalling [PMID:25329472];
  ARF-1 and ARF-5 are needed for the agef-1(vh4) yolk-extrusion phenotype, and vh4 (E1028K, in
  HDS2, next to the residue matching the activating Sec7p L1376D) is predicted to be activating
  [PMID:42388253 "Based on structure of the yeast AGEF-1 ortholog, Sec7p, the E1028K change is predicted to activate AGEF-1"].
- AGEF-1 is in proximity to ARF-1 (positive control) and to RAB-35 by split-GFP in the epidermis;
  whether it acts on RAB-35 directly or through an Arf is unresolved
  [PMID:42312793 "These results demonstrate that a subset of AGEF-1 is in proximity to RAB-35 in vivo suggesting that these molecules interact, either directly or indirectly"].

## Localization

- No worm study shows AGEF-1 on the Golgi directly. Endogenously tagged epidermal AGEF-1 is in
  puncta [PMID:42312793 "We found that epidermal AGEF-1::GFPx7 and AGEF-1[S784L]::GFPx7 localized to small puncta throughout the cytoplasm and membrane of the epidermis"].
- Phenotypes place its action at the trans-Golgi: agef-1(RNAi) inflates Golgi cisternae
  [PMID:23840591 "agef-1(RNAi) resulted in large inflated cisternae, consistent with a block in secretion at the trans-Golgi"]
  [PMID:23840591 "GBF-1 mainly acts at the cis-Golgi, while AGEF-1 is more important at the trans-Golgi."].
- C. elegans Golgi is dispersed in mini-stacks rather than a perinuclear ribbon
  [PMID:23840591 "The Golgi in C. elegans germ line is organized in small mini stacks localized in close proximity to ER-exit sites (ERES)."].

## Biological processes (mutant evidence)

- Secretion: agef-1(vh4) is defective in secretion of ssGFP from muscle and yolk from intestine
  [PMID:25329472 "Consistent with yeast Sec7p and human BIG1/BIG2 functioning in the secretory pathway, we found that agef-1(vh4) animals had defects in secretion of ssGFP from body wall muscles and Yolk::GFP from the intestine."].
- Golgi-to-plasma-membrane transport of caveolin (CAV-1 bodies) in oocytes requires AGEF-1
  [PMID:23840591 "In the absence of AGEF-1 or ARF-1.2, the internal CAV-1 structures become trapped in a perinuclear Golgi compartment"].
- Endolysosomal: agef-1(RNAi) delays fluid-phase uptake and enlarges lysosomes in coelomocytes
  [PMID:22446376 "Our results suggest that AGEF-1 regulates endosome/lysosome fusion or fission events, in addition to earlier steps in endocytic transport."];
  AGEF-1 and AP-1 regulate late endosome/lysosome size [PMID:25329472].
- Polarized sorting / signalling: agef-1(vh4) increases basolateral LET-23 EGFR and enhances vulval
  induction; an AGEF-1/Arf/AP-1 ensemble antagonises LET-23 basolateral localization
  [PMID:25329472].
- Neuron-epidermis attachment: epidermal AGEF-1 acts upstream of RAB-35 to modulate
  neuron-epidermal attachment and PLM axon integrity in a spectrin-compromised background
  [PMID:42312793].

## Interpretation

AGEF-1 is the nematode BIG1/BIG2 Arf GEF. The best-supported core is Sec7-dependent Arf activation
at the trans-Golgi network to drive post-Golgi cargo sorting (with AP-1) and secretion. Its
signalling, endolysosomal and axon-integrity phenotypes are downstream consequences of that
trafficking role, not separate activities.
