# nhr-49 Research Notes

## Gene Overview

nhr-49 (K10C3.6) encodes a nuclear hormone receptor in C. elegans (UniProt: O45666), classified as an orphan receptor belonging to the HNF4 (hepatocyte nuclear factor 4) family [PMID:15719061 "Despite its sequence relationship with the mammalian hepatocyte nuclear factor 4 receptor, the biological activities of nhr-49 were most similar to those of the mammalian PPARs"]. NHR-49 is a central regulator of lipid metabolism, functioning analogously to mammalian PPARalpha in controlling fatty acid beta-oxidation and desaturation [PMID:15719061 "nhr-49 served as a key regulator of fat usage, modulating pathways that control the consumption of fat and maintain a normal balance of fatty acid saturation"]. The protein contains a C4-type zinc finger DNA-binding domain (aa 8-83), a nuclear receptor ligand-binding domain (aa 157-422), and a 9aaTAD transactivation motif (aa 413-421). Four isoforms (a-d) are produced by alternative splicing. NHR-49 acts as a hub nuclear receptor that partners with distinct co-factors (NHR-80, NHR-66, NHR-13) to regulate separate branches of lipid metabolism [PMID:22511885 "NHR-49 regulates distinct subsets of its target genes by partnering with at least two other NHRs"].

## Core Pathway: LIPL-4 -> LBP-8 -> NHR-49/NHR-80

NHR-49 is a critical downstream component of the lysosome-to-nucleus retrograde lipid signaling pathway that promotes longevity. In this pathway, the lysosomal acid lipase LIPL-4 generates lipid signals including oleoylethanolamide (OEA), which are transported to the nucleus by the lipid chaperone LBP-8, where they activate the NHR-49/NHR-80 nuclear receptor heterodimer [PMID:25554789 "the lysosomal acid lipase LIPL-4 triggered nuclear translocalization of a lysosomal lipid chaperone LBP-8, which promoted longevity by activating the nuclear hormone receptors NHR-49 and NHR-80"].

Key details of NHR-49's role in this pathway:
- Both NHR-49 and NHR-80 are required for LIPL-4- and LBP-8-mediated longevity [PMID:25554789 "RNAi-mediated inactivation of nhr-49 in adult worms shortened the lifespan of WT worms but also completely suppressed longevity extension in lipl-4 Tg and lbp-8 Tg worms"]
- NHR-49 does NOT directly bind OEA; rather, OEA binds NHR-80 directly (Kd ~7.8 uM) and NHR-49 functions as a co-factor [PMID:25554789 "no binding was detected between NHR-49 and OEA or OEA analogue"]
- The NHR-49/NHR-80 heterodimer activates transcription of target genes including acs-2 (>15-fold increase in lipl-4 Tg animals) and lbp-8 itself, forming a positive feedback loop [PMID:25554789 "acs-2 transcription was increased more than 15-fold in lipl-4 Tg animals; this effect was dependent on nhr-49 and nhr-80"]
- The pathway is independent of dietary restriction [PMID:25554789 "the longevity extensions by lipl-4 Tg and eat-2(ad1116), a genetic model of dietary restriction in C. elegans, were additive"]

## Heterodimerization Partners

NHR-49 forms a homodimer and physically interacts with distinct partner NHRs to regulate separate metabolic programs [PMID:22511885 "NHR-49 regulates distinct subsets of its target genes by partnering with at least two other NHRs"].

### NHR-80: Fatty acid desaturation
- NHR-49 and NHR-80 directly interact, demonstrated by GST pull-down assays and yeast two-hybrid [PMID:22511885 "GST-NHR-49 successfully formed a homodimer with radiolabeled NHR-49. In addition, it was also able to interact directly with NHR-66 and NHR-80"]
- The NHR-49/NHR-80 partnership regulates delta-9 desaturase genes (fat-5, fat-6, fat-7) [PMID:22511885 "NHR-49 partners with...NHR-80 to regulate genes encoding fatty acid desaturases"]
- Loss of NHR-80 reduces lifespan to 13.19+/-0.38 days vs. 17.35+/-0.34 days in wild-type [PMID:22511885]
- nhr-80;nhr-13 double mutants have lifespan (12.29+/-0.37 days) approaching nhr-49 mutant lifespan (9.52+/-0.23 days) [PMID:22511885]
- Both NHR-49 and NHR-80 are derived from the same HNF4 ancestral gene [PMID:16839188 "Both of these transcription factors are proposed to be derived from the same ancestral gene that also is the progenitor of the mammalian gene encoding hepatocyte nuclear factor 4"]

### NHR-66: Sphingolipid breakdown and lipid remodeling
- NHR-49 partners with NHR-66 to repress genes involved in sphingolipid processing and lipid remodeling [PMID:22511885 "NHR-49 partners with NHR-66 to regulate sphingolipid and lipid remodeling genes"]
- Direct physical interaction confirmed by GST pull-down [PMID:22511885]
- NHR-66 does not contribute to the lifespan phenotype (nhr-66 lifespan: 17.16+/-0.41 days, similar to wild-type) [PMID:22511885]

### NHR-13: Fatty acid desaturation
- NHR-13 has a similar gene expression profile to NHR-80 regarding desaturase regulation [PMID:22511885]
- NHR-13 did not bind NHR-49 directly in vitro pull-down assays, suggesting indirect interaction or requirement for additional factors [PMID:22511885 "NHR-13 did not bind to NHR-49 in vitro above background levels, suggesting that additional factors may contribute to an interaction with NHR-49 in vivo"]
- nhr-13 mutants have shortened lifespan (14.17+/-0.4 days) [PMID:22511885]

### Additional interactions
- May interact with NHR-22, NHR-79, NHR-105, NHR-256 (UniProt, based on PMID:22511885)
- Physical interactions detected with MDT-15, NHR-13, NHR-181, NHR-19, NHR-20, NHR-234, NHR-76 (IntAct database, UniProt)

## Fatty Acid Metabolism (fat-5/6/7, acs-2 regulation)

NHR-49 regulates two distinct branches of fatty acid metabolism:

### Branch 1: Beta-oxidation (fat consumption)
- NHR-49 positively regulates acs-2 (acyl-CoA synthetase) and ech-1 (enoyl-CoA hydratase), which promote mitochondrial beta-oxidation [PMID:15719061 "The high-fat phenotype was due to reduced expression of enzymes in fatty acid beta-oxidation"]
- acs-2 expression is reduced in nhr-49(nr2041) mutants; ectopic acs-2 expression rescues the high-fat phenotype [PMID:15719061 "Ectopic expression of acs-2::gfp in nhr-49(nr2041) was sufficient to reduce Nile Red staining to WT levels"]
- In germline-less animals, NHR-49 upregulates 7 mitochondrial beta-oxidation genes: acs-2, acs-22, cpt-2, cpt-5, acdh-11, ech-1.1, and hacd-1 [PMID:25474470 "NHR-49 causes the increased expression of multiple genes involved in fatty-acid beta-oxidation and desaturation, triggering a metabolic shift towards lipid oxidation"]

### Branch 2: Fatty acid desaturation (fatty acid composition)
- NHR-49 activates expression of delta-9 desaturases fat-5, fat-6, fat-7, acting through partners NHR-80 and NHR-13 [PMID:15719061, PMID:22511885]
- fat-7 is the primary target; fat-7 RNAi phenocopies the shortened lifespan of nhr-49(nr2041) [PMID:15719061 "interference of only fat-7 resulted in a shortened life-span phenotype similar to that of nhr-49(nr2041)"]
- NHR-49 may form a negative feedback loop with fat-7: NHR-49 stimulates fat-7 and acs-2 expression, and fat-7 indirectly inhibits acs-2 and other beta-oxidation genes (UniProt, PMID:15719061)

### ACDH-11 and heat adaptation
- ACDH-11 (acyl-CoA dehydrogenase) sequesters medium-chain fatty acids (C11, C12). Loss of acdh-11 releases these fatty acids, which activate fat-7 expression through NHR-49 [PMID:25981666 "Acyl-CoA dehydrogenase drives heat adaptation by sequestering fatty acids"]
- NHR-49 RNAi eliminates the effect of C11 or C12 chain fatty acids in activating fat-7 and blocks fat-7 overexpression in acdh-11 mutants (UniProt, PMID:25981666)

## Longevity Function

NHR-49 impacts lifespan through multiple mechanisms:

### Direct lifespan effects
- nhr-49(nr2041) deletion mutants have drastically shortened lifespan (~41% reduction vs. wild-type) [PMID:15719061, PMID:25554789]
- The shortened lifespan correlates with impaired fat-7 expression and excess saturated fat [PMID:22511885 "there is a strong inverse correlation (r2 = 0.86) between the level of saturated fat and the duration of mean worm lifespan"]
- NHR-49 overexpression in fertile animals extends lifespan by ~15% [PMID:25474470 "wild type, fertile worms overexpressing NHR-49 lived ~15% longer than their non-transgenic siblings"]

### Germline-mediated longevity
- NHR-49 is essential for the longevity of germline-less (glp-1) animals; nhr-49 RNAi completely abrogates glp-1 longevity [PMID:25474470 "two independent RNAi clones targeting nhr-49 completely abrogated the longevity of glp-1 mutants"]
- Upon germline removal, NHR-49 is transcriptionally upregulated by DAF-16/FOXO and TCER-1/TCERG1 in somatic tissues [PMID:25474470 "NHR-49 is transcriptionally up-regulated by DAF-16 and TCER-1 in the soma upon germline removal"]
- NHR-49 is NOT required for daf-2/insulin-pathway longevity [PMID:25474470 "nhr-49 was not essential for the longevity of daf-2 mutants"]
- NHR-49 is NOT required for mitochondrial electron transport chain mutant longevity (cyc-1, cco-1 RNAi) [PMID:25474470]

### LIPL-4/LBP-8 pathway longevity
- Required for LIPL-4 and LBP-8 overexpression-mediated lifespan extension [PMID:25554789]
- Functions together with NHR-80 as the downstream effector of lysosomal lipid signaling [PMID:25554789]

### Mit mutant longevity
- NHR-49 is required for lifespan extension of isp-1(qm150) Mit mutants [PMID:24107417 "NHR-49...were also essential for isp-1 life extension"]
- Not required for RNAi-induced Mit mutants (nuo-1, ucr-1, cyc-1, cco-3) [PMID:24107417]

## Hypoxia Adaptation

NHR-49 plays a critical role in adaptation to low oxygen environments, acting in parallel with HIF-1 [PMID:35285794, Doering et al. 2022]:
- nhr-49 mutants show severe hypoxia sensitivity: only 25% of embryos develop to L4 stage in 0.5% O2 vs. 86% in wild-type (UniProt, PMID:35285794)
- In a hif-1 mutant background, nhr-49 loss is nearly lethal under hypoxia (<2% survival to L4) (UniProt, PMID:35285794)
- NHR-49 activates expression of acs-2, autophagy-related genes, and autophagosome formation during hypoxia, independent of HIF-1 (UniProt, PMID:35285794)
- NHR-49 activates the detoxification gene fmo-2 (flavin mono-oxygenase), acting in parallel with HIF-1 during hypoxia (UniProt, PMID:35285794)
- NHR-49 acts in multiple somatic tissues, probably cell non-autonomously, in regulating hypoxia response (UniProt, PMID:35285794)
- nhr-49 mutants are unaffected by hydrogen sulfide (UniProt, PMID:35285794)
- Hypoxia exposure (0.5% oxygen) triggers nhr-49-dependent responses (UniProt, PMID:35285794)

## Mediator Complex Interaction (MDT-15)

MDT-15, a subunit of the C. elegans Mediator complex, acts as a transcriptional coactivator for NHR-49 [PMID:16651656 "MDT-15, a subunit of the C. elegans Mediator complex, as an NHR-49-interacting protein and transcriptional coactivator"]:
- MDT-15 is required for fasting-induced expression of NHR-49 target genes in vivo [PMID:16651656 "Knockdown of mdt-15 by RNA interference (RNAi) prevented fasting-induced mRNA accumulation of NHR-49 targets in vivo"]
- MDT-15 is also required for fasting-independent expression of NHR-49 targets including fat-5 and fat-7 [PMID:16651656]
- MDT-15 additionally regulates NHR-49-independent targets, such as fat-6, suggesting it integrates multiple regulatory inputs [PMID:16651656 "mdt-15 RNAi affected additional FA-metabolism genes (including the third FA-Delta9-desaturase, fat-6) that are regulated independently of NHR-49"]
- mdt-15 knockdown causes dramatically decreased unsaturated fatty acids and pleiotropic phenotypes (short lifespan, sterility, uncoordinated locomotion, morphological defects) [PMID:16651656]
- Physical interaction between NHR-49 and MDT-15 confirmed (IntAct, UniProt)

## PKG and Lysosomal Lipid Metabolism

During short-term fasting, NHR-49 acts in the intestine to regulate lysosomal lipid accumulation in coordination with EGL-4/PKG signaling from sensory neurons [PMID:24854345 "EGL-4 acts in sensory neurons to enhance lysosomal lipid accumulation through inhibiting the DAF-3/SMAD pathway, whereas NHR-49 acts in intestine to inhibit lipids accumulation via activation of IPLA-2"]:
- NHR-49 inhibits lysosomal lipid accumulation during fasting via activation of IPLA-2 (intracellular phospholipase A2) in the cytoplasm and hydrolases in lysosomes [PMID:24854345]
- This fasting-induced lysosomal lipid accumulation is independent of autophagy and RAB-7-mediated endocytosis [PMID:24854345]

## Transgenerational Epigenetic Regulation

NHR-49 is required for transgenerational inheritance of high-fat-diet (HFD)-induced lipid accumulation [PMID:35140229]:
- NHR-49, NHR-80, SBP-1/SREBP, and DAF-16/FOXO are all required for transgenerational epigenetic inheritance of obesogenic lipid accumulation [PMID:35140229 "daf-16, nhr-49, nhr-80 and sbp-1 were required for HFD-induced TEI of lipid accumulation"]
- NHR-49 and NHR-80 function as executors (effectors), not transmitters, of heritable lipid metabolic memory [PMID:35140229 "nhr-49 and nhr-80 functioned solely as executors"]
- The transgenerational signal is mediated by histone H3K4me3 modification [PMID:35140229]
- Delta-9 desaturases (fat-5, fat-6, fat-7) are also required for the transgenerational lipid phenotype [PMID:35140229]

## Subcellular Localization

- NHR-49 localizes to both nucleus and cytoplasm, with highest expression in intestinal cells [PMID:25474470 "In adults, it was visible in all somatic tissues, localized to both nuclei and cytoplasm, with highest expression in intestinal cells"]
- Expressed in head, intestine, and hypodermal seam cells (UniProt, PMID:35285794)
- Also expressed in neurons, muscle, and hypodermis [PMID:25474470]
- NHR-49::GFP is visible throughout embryonic and larval development [PMID:25474470]
- Nuclear localization predicted by PROSITE NR DBD domain (UniProt)

## Regulation

- Germline removal: NHR-49 mRNA and protein levels are elevated upon germline ablation, dependent on DAF-16/FOXO and TCER-1/TCERG1 [PMID:25474470 "Germline depletion resulted in increased NHR-49::GFP, especially in intestinal cells"]
- In fertile animals, nhr-49 expression is DAF-16 and TCER-1 independent [PMID:25474470 "NHR-49 is differentially regulated depending on the reproductive status of the animal"]
- Fasting: NHR-49 coordinates expression of fatty acid metabolic genes during feeding and in response to fasting [PMID:16651656]
- Hypoxia: Exposure to 0.5% oxygen triggers NHR-49-dependent transcriptional responses (UniProt, PMID:35285794)
- NHR-49 is an orphan receptor; no endogenous ligand has been identified [PMID:25981666, UniProt]

## Disruption Phenotype

nhr-49(nr2041) mutants (893 bp deletion) exhibit:
- **Elevated fat storage**: Increased Nile Red staining; high-fat phenotype due to reduced beta-oxidation gene expression [PMID:15719061]
- **Shortened lifespan**: ~41% reduction compared to wild-type; lifespan of 9.52+/-0.23 days vs. 17.35+/-0.34 at 20C [PMID:15719061, PMID:22511885]
- **Altered fatty acid composition**: Increased ratio of stearic acid to oleic acid (C18:0/C18:1n9 ratio of 3.74+/-0.33 vs. 0.98+/-0.06 in wild-type) [PMID:15719061, PMID:22511885]
- **Vacuole formation and germline necrosis**: Widespread vacuoles in intestine and gonadal collapse [PMID:15719061 "fat-7 RNAi animals displayed many of the same characteristics of the nhr-49(nr2041) mutant, including widespread vacuole formation and germ line necrosis"]
- **Abnormal mitochondrial morphology**: ~25% of intestinal mitochondria show irregular shape with more turns; reduced oxygen consumption (5.22 vs. 9.625 pmoles/min/worm in wild-type); reduced beta-oxidation [PMID:22511885 "about 25% of the intestinal mitochondria of the nhr-49 mutants were uncharacteristically irregular in shape"]
- **Hypoxia sensitivity**: Only 25% embryo survival to L4 under 0.5% O2; L1 larvae survival reduced to 19% vs. 95% in wild-type (UniProt, PMID:35285794)
- **Mild developmental delay**: Slower larval growth (UniProt, PMID:35285794)
- **Suppressed glp-1 longevity**: Completely abolishes the lifespan extension of germline-less animals [PMID:25474470]

## Mitochondrial Function

NHR-49 is important for maintaining mitochondrial morphology and function [PMID:22511885]:
- nhr-49 mutants have reduced basal oxygen consumption rates (5.22 pmoles/min/worm vs. 9.625 in wild-type) [PMID:22511885 "nhr-49 animals consumed oxygen at significantly reduced rates"]
- Reduced beta-oxidation measured by radiolabeled palmitate assay (0.56 vs. 1.29 pmole/min/ug protein in wild-type) [PMID:22511885]
- NHR-49 maintains mitochondrial morphology via multiple pathways including NHR-66 and NHR-80 dependent regulation [PMID:22511885 "NHR-49 maintains mitochondrial morphology via multiple pathways, including NHR-66 and NHR-80 dependent regulation as well as additional, unknown mechanisms"]
