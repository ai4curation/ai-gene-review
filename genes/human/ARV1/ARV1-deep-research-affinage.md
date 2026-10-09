---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARV1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9H2C2
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 21
citation_count: 21
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARV1 (human)

## Current model (mechanistic narrative)

ARV1 encodes a conserved ER transmembrane protein that integrates glycosylphosphatidylinositol (GPI) anchor biosynthesis with cellular lipid and sterol homeostasis [PMID:11063737, PMID:18287539, PMID:40378954]. Its N-terminal ARV1 homology domain (AHD) is oriented to the cytosol with an ER-luminal C-terminal region required for function [PMID:21539707], and this zinc-binding AHD directly binds cholesterol and phospholipids including phosphoinositides, with lipid binding dependent on conserved cysteine clusters and on ARV1 dimerization [PMID:39952408]. In its best-defined role, ARV1 is a component of the GPI N-acetylglucosaminyltransferase (GPI-GnT) complex that initiates GPI biosynthesis: it associates with the GPI-GnT subunit PIGQ and facilitates efficient use of phosphatidylinositol by the enzyme [PMID:40378954], a function conserved from yeast — where Arv1 supports delivery of early GPI intermediates and GPI flippase activity [PMID:18287539, PMID:32449190] — to human cells, where biallelic ARV1 loss reduces surface GPI-anchored protein expression rescuable by wild-type ARV1 [PMID:32165008, PMID:34296759]. ARV1 also governs sterol distribution and membrane homeostasis: its loss causes ER cholesterol accumulation, hypercholesterolemia and altered SREBP/FXR signaling [PMID:20663892], and triggers lipid-bilayer-stress-induced activation of the IRE1-dependent unfolded protein response [PMID:21266578, PMID:38588806]. Loss-of-function ARV1 variants cause an autosomal recessive epileptic encephalopathy, with neuronal Arv1 deletion in mice recapitulating seizures and lethality [PMID:27270415].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008289 lipid binding, GO:0016740 transferase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005783 endoplasmic reticulum, GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-1430728 Metabolism, R-HSA-8953897 Cellular responses to stimuli
- **partners:** PIGQ, ERG11, IQGAP1, MYH9, MYL9, EPLIN
- **complexes:** GPI N-acetylglucosaminyltransferase (GPI-GnT) complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2000 | High | Yeast ARV1 mediates sterol trafficking into the plasma membrane; deletion causes altered intracellular sterol distribution, defective sterol uptake, and nystatin sensitivity. Human ARV1 complements yeast arv1Δ defects, indicating functional conservation. ARV1 encodes a transmembrane protein with zinc-binding motifs. | PMID:11063737 | The Journal of biological chemistry |
| 2002 | High | Yeast Arv1p is required for normal sphingolipid metabolism, phospholipid biosynthesis, and proper fatty acid composition. arv1Δ cells have reduced complex sphingolipids, accumulate hydroxylated ceramide species, and have decreased phosphatidylcholine, phosphatidylethanolamine, phosphatidylserine, and phosphatidylglycerol levels. GFP-Arv1p localizes to the ER and Golgi. Human ARV1 cDNA suppresses sphingolipid metabolic defects of arv1Δ cells. | PMID:12145310 | The Journal of biological chemistry |
| 2008 | High | Yeast Arv1p is required for efficient delivery of the early GPI intermediate GlcN-acylPI to the first mannosyltransferase on the luminal side of the ER during GPI biosynthesis, consistent with a role as the GPI flippase. ARV1 deletion also affects inositol phosphorylceramide synthesis and intracellular sterol distribution, linking GPI anchor synthesis to lipid flow from the ER. | PMID:18287539 | Molecular biology of the cell |
| 2010 | High | Mammalian ARV1 is a resident ER protein required for sterol movement from the ER to the plasma membrane. Antisense oligonucleotide knockdown of ARV1 in murine liver causes cholesterol accumulation in the ER, hypercholesterolemia, elevated serum bile acids, activation of hepatic FXR pathway, and suppression of SREBP targets. | PMID:20663892 | The Journal of biological chemistry |
| 2011 | High | Loss of ARV1 in yeast causes sterol accumulation in the ER, subcellular membrane expansion, elevated lipid droplet formation, and vacuolar fragmentation. ARV1 deletion activates the unfolded protein response (UPR) via lipid bilayer stress; IRE1 is synthetically lethal with ARV1. Decreased ARV1 in murine macrophages also induces UPR and apoptosis. | PMID:21266578 | The Journal of biological chemistry |
| 2011 | Medium | The membrane topology of Arv1 in the ER was determined; the protein has a cytosolic N-terminal ARV1 homology domain and an ER luminal C-terminal region. The ER luminal region is required for Arv1 function, as demonstrated by truncation analysis. | PMID:21539707 | FEMS yeast research |
| 2010 | Medium | Arv1 is required for pheromone-induced MAP kinase signaling and mating in yeast. arv1 cells fail to polarize PI(4,5)P2 and the Ste5 scaffold to the plasma membrane, resulting in weakened MAP kinase activity. A plasma membrane-tethered Ste5(Q59L) mutant suppresses the MAP kinase defects of arv1 cells. The ARV1 homology domain (AHD) is required for mating and sterol trafficking. | PMID:21098723 | Genetics |
| 2013 | Medium | Arv1 deficiency in yeast does not affect anterograde or retrograde sterol transport between the ER and plasma membrane when measured directly by dehydroergosterol (DHE) tracking and metabolic labeling. Instead, Arv1 deficiency alters ER morphology and plasma membrane lipid bilayer organization, suggesting a role in membrane homeostasis rather than direct sterol transport. | PMID:23668914 | Traffic (Copenhagen, Denmark) |
| 2013 | Medium | ARV1 is the most liposensitive gene in a genome-wide fatty acid sensitivity screen. Down-regulation of ARV1 in MIN6 pancreatic β-cells or HEK293 cells decreases neutral lipid synthesis and increases fatty acid sensitivity and lipoapoptosis. Elevated human ARV1 expression in HEK293 cells or mouse liver increases triglyceride mass and lipid droplet number, accompanied by upregulation of DGAT1 and CD36. ARV1 is a transcriptional target of PPARα. | PMID:24273168 | The Journal of biological chemistry |
| 2016 | Medium | Neuronal deletion of Arv1 in mice causes seizures and severe survival defects, recapitulating the human ARV1-deficiency phenotype. The ARV1 p.(Lys59_Asn98del) variant fails to rescue temperature-sensitive growth in arv1Δ yeast and neither this nor the p.(Gly189Arg) variant express detectable protein in mammalian cells. | PMID:27270415 | Human molecular genetics |
| 2016 | Medium | Human Arv1 is recruited to the cleavage furrow during telophase by EPLIN. At the cleavage furrow, Arv1 interacts with IQGAP1 and recruits myosin heavy chain 9 (MYH9) and myosin light chain 9 (MYL9) to promote the contractile actomyosin ring. Loss of Arv1 delays telophase progression and causes furrow regression and multinuclear cell formation. This cell division function is independent of Arv1's lipid transporter activity. | PMID:27104745 | Cell cycle (Georgetown, Tex.) |
| 2020 | Medium | ARV1 deletion in yeast causes cold-sensitive defects in GPI anchor synthesis. The pathogenic human ARV1-G189R mutant fails to fully restore cold-sensitive phenotypes in yeast arv1Δ, supporting a role for ARV1 in GPI anchor synthesis as a GPI flippase. | PMID:32449190 | FEBS letters |
| 2020 | Medium | Biallelic splice mutations in human ARV1 cause significantly decreased GPI-anchored protein expression on the surface of patient neutrophils and fibroblasts, demonstrating that ARV1 function in GPI-anchor synthesis is conserved in humans. | PMID:32165008 | Molecular genetics and metabolism |
| 2020 | Medium | The ARV1 p.Gly189Arg mutation causes deficient maturation of the GPI-anchored protein Gas1 in yeast but does not affect sphingolipid synthesis, indicating that ARV1's role in GPI anchoring is separable from its role in sphingolipid metabolism. | PMID:32462292 | Neurogenetics |
| 2021 | Medium | Flow cytometric analysis of patient fibroblasts with biallelic ARV1 variants shows decreased GPI-anchored proteins on the cell surface. Lentiviral transduction with wild-type ARV1 cDNA rescues GPI-anchored protein expression, confirming ARV1's essential role in GPI biosynthesis. | PMID:34296759 | Clinical genetics |
| 2020 | Medium | Erg11 lanosterol 14-α-demethylase forms a heterodimeric complex with Arv1 in Saccharomyces cerevisiae and Candida albicans. This complex is required for Erg11 protein stability; Arv1 mutants unable to interact with Erg11 show reduced Erg11 protein levels and azole hypersusceptibility. CaArv1 mutants unable to interact with CaErg11 render C. albicans avirulent in a mouse model. | PMID:32678853 | PloS one |
| 2023 | Medium | ARV1 is required for upregulation of GPI biosynthesis triggered by accumulation of specific GPI-anchored protein precursors (CD55, CD48, PLET1) under ERAD-deficient conditions. The GPI-attachment signal peptide of the CD55 precursor is the active element driving this upregulation, and ARV1 is a prerequisite for this feedback mechanism. | PMID:36828365 | The Journal of cell biology |
| 2024 | Medium | ARV1 deletion in yeast activates the UPR by inducing lipid bilayer stress (not unfolded protein accumulation). In arv1Δ cells, UPR activation via Ire1 activates the HOG pathway through Hog1, which translocates Msn2 to the nucleus, inducing nicotinamidase Pnc1 expression, activating Sir2, and thereby enhancing rDNA silencing and stability. | PMID:38588806 | The Journal of biological chemistry |
| 2025 | High | Human ARV1 directly binds cholesterol and multiple phospholipids (including phosphoinositides) through its conserved N-terminal ARV1 homology domain (AHD, first 98 amino acids). The zinc-binding domain and conserved cysteine clusters within the AHD are necessary for lipid binding. ARV1 exists as a dimer in cells, and mutations disrupting dimerization abolish lipid binding. | PMID:39952408 | The Journal of biological chemistry |
| 2025 | High | ARV1 is a component of the GPI N-acetylglucosaminyltransferase (GPI-GnT) complex, which initiates GPI biosynthesis. ARV1 associates with PIGQ, a GPI-GnT subunit; ARV1 mutants defective in this association lose the ability to enhance GPI-GnT activity. ARV1-containing GPI-GnT uses phosphatidylinositol (PI) more efficiently than ARV1-less GPI-GnT, suggesting ARV1 facilitates recruitment of PI to GPI-GnT. | PMID:40378954 | The Journal of biological chemistry |
| 2025 | Medium | In Candida albicans, Arv1 physically interacts with the GPI-GnT complex (confirmed by SRRF co-localization, Co-IP, and FRET). CaArv1 also transcriptionally regulates GPI-GnT subunit expression via the epigenetic modulator Rtt109. Overexpressing GPI19 rescues cell wall, azole sensitivity, and GPI-GnT activity phenotypes of Caarv1Δ/Δ, while the filamentation defect is regulated independently through cAMP-PKA signaling (Efg1, Flo8, Tup1, Nrg1). | PMID:40801327 | The FEBS journal |

## Citations

- PMID:11063737
- PMID:12145310
- PMID:18287539
- PMID:20663892
- PMID:21098723
- PMID:21266578
- PMID:21539707
- PMID:23668914
- PMID:24273168
- PMID:27104745
- PMID:27270415
- PMID:32165008
- PMID:32449190
- PMID:32462292
- PMID:32678853
- PMID:34296759
- PMID:36828365
- PMID:38588806
- PMID:39952408
- PMID:40378954
- PMID:40801327
