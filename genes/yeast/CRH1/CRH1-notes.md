# CRH1 Deep Research Notes

## Gene Identity

- **Gene**: CRH1 (Congo Red Hypersensitive protein 1)
- **Systematic name**: YGR189C
- **UniProt**: P53301
- **Organism**: Saccharomyces cerevisiae S288c
- **Family**: GH16 (glycoside hydrolase family 16), CRH1 subfamily
- **EC numbers**: EC 3.2.1.14 (endochitinase) and EC 2.4.-.- (chitin transglycosylase)

## Key Literature Summary

### Discovery and naming (PMID:10757808)
Rodriguez-Pena et al. (2000) identified CRH1, CRH2, and CRR1 as a novel family of cell wall-related proteins with homology to bacterial beta-glucanases and eukaryotic endotransglycosidases. Deletion of CRH1 and CRH2 caused additive sensitivity to Congo Red and Calcofluor White (cell wall-perturbing agents). The putative glycosidase domain was critical for function. Crh1-GFP localized to incipient bud site, septum area in late budding, and ascospore envelopes. The alkali-soluble glucan fraction in crh1/crh2 double mutant was almost twice wild-type levels. [PMID:10757808 "the alkali-soluble glucan fraction in the crh1Delta crh2Delta strain was almost twice the level in the wild-type"]

### GPI-anchor and cell wall attachment (PMID:9613572, PMID:15781460)
Hamada et al. (1998) identified CRH1 as a GPI-dependent cell wall protein through genome-wide screening. [PMID:9613572]
Yin et al. (2005) confirmed CRH1 is covalently attached to cell wall via GPI remnants by comprehensive proteomic analysis using tandem mass spectrometry. [PMID:15781460 "Crh1p...are classified as glycoside hydrolases"]

### Cross-linking function demonstrated (PMID:17302808)
Cabib et al. (2007) showed Crh1p and Crh2p are required for cross-linking chitin to beta(1-6)glucan. In crh1/crh2 double mutants, chitin linked to beta(1-6)glucan was completely absent. Heat stress (38C) increased chitin-beta(1-6)glucan cross-links and CRH1 expression (cell integrity pathway dependent). [PMID:17302808 "chitin linked to beta(1-6)glucan is...completely absent in a double mutant"]

### In vivo and in vitro transglycosylase activity (PMID:18694928)
Cabib et al. (2008) demonstrated that Crh1p and Crh2p act as transglycosylases both in vivo and in vitro. Using fluorescent sulforhodamine-linked laminari-oligosaccharides as artificial chitin acceptors, they showed CRH-dependent fluorescence at bud scars and cell contour. The cell wall reaction was inhibited by chitooligosaccharides. [PMID:18694928 "the Crh proteins act by transferring chitin chains to beta(1-6)glucan, with a newly observed high activity in the bud scar"]

### Chitin transfer to both beta(1-3)- and beta(1-6)glucan (PMID:19734368)
Cabib (2009) developed two novel techniques showing Crh1p and Crh2p transfer chitin to BOTH beta(1-3)- and beta(1-6)glucan. Previous results suggesting residual chitin-beta(1-3)glucan links in crh1/crh2 mutants were due to chitinase contamination in zymolyase. All chitin in crh1/crh2 double mutants is free (unlinked). [PMID:19734368 "Crh1p and Crh2p catalyze the transfer of chitin to both beta(1-3)- and beta(1-6)glucan"]

### Catalytic properties and fluorescence assay (PMID:23919454)
Mazan et al. (2013) heterologously expressed CRH1 and CRH2 in Pichia pastoris and characterized their catalytic properties:
- Both act as chitin transglycosylases
- Donors: soluble chitin derivatives (CM-chitin, glycol-chitin, chitooligosaccharides DP>=5)
- Acceptors: oligosaccharides from chitin, beta(1,3)-glucan (laminarin), beta(1,6)-glucan (pustulan)
- Minimal acceptor: 2 hexopyranose units; effectivity increases with chain length
- Both exhibit weak endochitinase activity (ratio of endo:exo ~4x higher in Crh1 vs Crh2)
- pH optimum: 3.5; temperature optimum: 37C
[PMID:23919454 "Both proteins act as chitin transglycosylases...Both proteins exhibited a weak chitinolytic activity"]

### Quantification of cell wall copies (PMID:17617218)
Yin et al. (2007) quantified CRH1 at 44,000 wall-bound copies per cell in log phase YPD. In gas1 mutants (constitutive cell wall integrity pathway), Crh1p levels increased ~3-5 fold. [PMID:17617218]

### Regulation by cell wall integrity pathway (PMID:10594829, PMID:11016834)
CRH1 is positively regulated by MPK1/SLT2 through the cell wall integrity signaling pathway via Rlm1 transcription factor. Expression is upregulated in response to cell wall damage (fks1 disruption) and heat stress. [PMID:10594829, PMID:11016834]

### Cell periphery localization (PMID:26928762)
Yofe et al. (2016) SWAp-Tag (SWAT) high-throughput localization study assigned CRH1 to cell periphery. This is a high-throughput dataset (HDA evidence). [PMID:26928762]

## Paralog: CRH2/UTR2

CRH2 (YEL040w, also called UTR2) is the key paralog. CRH1 and CRH2 have redundant transglycosylase activity for chitin-glucan cross-linking. Single mutants show partial phenotypes; double mutants show complete loss of chitin cross-links. CRH1 is cell-cycle regulated and expressed during sporulation; CRH2 expression is constitutive during mitotic cycle.

## Mechanism Summary

CRH1 is a dual-function enzyme: primarily a chitin transglycosylase (transfers chitin to glucan acceptors) with secondary weak endochitinase activity. The GH16 catalytic domain uses a retaining mechanism with a catalytic glutamate pair (E134 nucleophile, E138 proton donor, by homology). The enzyme forms a glycosyl-enzyme intermediate from a chitin donor, then transfers the chitin chain to beta(1-3)- or beta(1-6)glucan acceptors. This cross-links chitin into the cell wall glucan network, which is essential for cell wall integrity.

## Key Points for GO Annotation

1. **Molecular function**: glycosyltransferase activity (GO:0016757) is the primary function, specifically chitin transglycosylase. Endochitinase activity (GO:0008843) is secondary/minor.
2. **Biological process**: chitin metabolic process (GO:0006030) and fungal-type cell wall organization (GO:0031505) are well-supported.
3. **Cellular component**: fungal-type cell wall (GO:0009277) is primary; incipient cellular bud site (GO:0000131) is specific and well-supported by GFP localization.
4. **Hydrolase annotations** (GO:0004553, GO:0016798) from InterPro are technically correct but misleading -- the primary function is transglycosylase, not hydrolase. The hydrolysis is secondary.
5. **Extracellular region** (GO:0005576) IBA is reasonable given GPI-CWP nature but "fungal-type cell wall" is more specific and accurate.
6. **Membrane** (GO:0016020) IEA is technically correct (GPI-anchored to outer leaflet of plasma membrane) but imprecise.
