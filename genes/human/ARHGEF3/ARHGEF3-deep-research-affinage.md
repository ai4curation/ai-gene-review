---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NR81
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 17
citation_count: 17
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF3 (human)

## Current model (mechanistic narrative)

ARHGEF3 (XPLN) is a DH-PH domain guanine nucleotide exchange factor that selectively activates RhoA and RhoB to drive actin cytoskeletal remodeling, stress fiber and focal adhesion assembly through Rho kinase, while also executing GEF-independent regulatory functions [PMID:12221096, PMID:23192023]. Its enzymatic specificity is intrinsic: ARHGEF3 catalyzes GDP-to-GTP exchange on RhoA and RhoB but not RhoC, a discrimination set by isoleucine 43 of RhoC, and its tandem DH-PH module undergoes PH-domain rearrangement upon RhoA engagement [PMID:12221096, PMID:23192023]. Through this RhoA/ROCK axis ARHGEF3 governs diverse programs in vivo: it restrains skeletal muscle mass, fiber size, and regeneration by blocking autophagy flux, an activity that requires GEF function and is recapitulated in dystrophic mdx muscle [PMID:33406419, PMID:37311604]; it supports erythroid transferrin/iron uptake upstream of RhoA [PMID:21715309]; and it shapes P-cadherin gradients and placode cell fate during hair follicle morphogenesis [PMID:41490244]. ARHGEF3 carries a separable, GEF-independent activity through its N-terminal 125-amino-acid domain that binds mTORC2 via rictor and inhibits its kinase activity toward Akt Ser473, thereby negatively regulating myoblast differentiation and the mTORC2-SPARC axis [PMID:24043828, PMID:28315487]. In a further non-canonical role, ARHGEF3 stabilizes ATP-citrate lyase by reducing its acetylation and blocking NEDD4-mediated degradation to promote tumor cell proliferation [PMID:36241648]. Additional context-specific roles in AML macrophage differentiation, adipocyte hypertrophy, antiviral restriction, and tumor microenvironment remodeling have been described [PMID:25494542, PMID:40216078, PMID:36016278, PMID:42023986].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0140096 catalytic activity, acting on a protein, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-9612973 Autophagy, R-HSA-1266738 Developmental Biology
- **partners:** RHOA, RHOB, RICTOR, ACLY
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | High | XPLN (ARHGEF3) is a guanine nucleotide exchange factor that stimulates GDP-to-GTP exchange on RhoA and RhoB but not RhoC, RhoG, Rac1, or Cdc42 in vitro, and the selectivity against RhoC is determined by isoleucine 43 in RhoC (valine in RhoA/RhoB). XPLN preferentially associates with RhoA and RhoB, and when expressed in cells stimulates stress fiber and focal adhesion assembly in a Rho kinase-dependent manner. | PMID:12221096 | The Journal of biological chemistry |
| 2012 | High | Crystal structure of the tandem DH-PH domains of mouse XPLN (ARHGEF3) was determined at 1.79 Å resolution by multiwavelength anomalous dispersion. The structure revealed an α4-α5 loop in the DH domain that is flexible and intramolecular DH-PH interactions, suggesting PH-domain rearrangement occurs upon RhoA binding. High structural similarity to other RhoGEFs (NET1, PDZ-RhoGEF, LARG, ITSN1/2) was observed. | PMID:23192023 | Acta crystallographica. Section F, Structural biology and crystallization communications |
| 2013 | High | XPLN (ARHGEF3) interacts with mTORC2 (but not mTORC1) in a rictor-dependent manner and acts as an endogenous inhibitor of mTORC2 kinase activity toward Akt. Knockdown of XPLN enhances Akt Ser473 phosphorylation; overexpression suppresses it. Purified XPLN inhibits mTORC2 kinase activity in vitro without affecting mTORC1. The GEF activity of XPLN is dispensable for mTORC2 inhibition, whereas the N-terminal 125-amino-acid fragment is necessary and sufficient for mTORC2 inhibition and for negative regulation of myoblast differentiation. | PMID:24043828 | Proceedings of the National Academy of Sciences of the United States of America |
| 2015 | Medium | In AML cells (U937), ARHGEF3 protein is primarily nuclear but undergoes cytoplasmic translocation upon HDACi (MS275) treatment. Cytoplasmic ARHGEF3 activates the RhoA/ROCK pathway, leading to SAPK/JNK phosphorylation and Elk1 activation. ARHGEF3 silencing prevents RhoA activation, reduces SAPK/JNK phosphorylation and Elk1 activity, and blocks CD68 macrophage differentiation marker expression. | PMID:25494542 | Epigenetics |
| 2011 | Medium | Silencing of arhgef3 in zebrafish causes microcytic hypochromic anemia rescued by intracellular iron supplementation, demonstrating that ARHGEF3 regulates transferrin/iron uptake in erythroid cells. Silencing of RhoA phenocopies arhgef3 loss. In K562 cells, ARHGEF3 knockdown severely impairs transferrin uptake, placing ARHGEF3 upstream of RhoA in an iron-uptake pathway. | PMID:21715309 | Blood |
| 2021 | High | ARHGEF3 KO mice show enhanced skeletal muscle mass, fiber size, and function after acute injury. This effect requires the GEF activity of ARHGEF3 (not Akt signaling) and operates via the RhoA/ROCK pathway. ARHGEF3 KO promotes autophagy, and autophagy activation is required for the enhanced regeneration phenotype. Overexpression of ARHGEF3 inhibits muscle regeneration in a ROCK-dependent manner. In aged mice, ARHGEF3 depletion prevents muscle weakness by restoring autophagy. | PMID:33406419 | Cell reports |
| 2017 | Medium | XPLN (ARHGEF3) knockdown in human lung fibroblasts stimulates SPARC expression and Akt Ser473 phosphorylation. TGF-β1 downregulates XPLN via Smad2/3. HDACi treatment upregulates XPLN mRNA and reverses TGF-β1-induced SPARC expression, establishing XPLN as a negative regulator of the mTORC2-SPARC axis. | PMID:28315487 | Pulmonary pharmacology & therapeutics |
| 2014 | Medium | ARHGEF3 knockdown in osteoblast-like cells causes downregulation of TNFRSF11B (osteoprotegerin). RHOA knockdown in osteoblast-like cells downregulates ACTA2 (alpha-2 actin) and upregulates PTH1R, and in osteoclast-like cells downregulates ARHGDIA and ACTA2, placing ARHGEF3/RhoA upstream of these bone-cell gene-expression programs. | PMID:24840563 | PloS one |
| 2022 | Medium | ARHGEF3 overexpression inhibits HCV subgenomic replicon RNA replication and full-length HCV replication, as well as replication of yellow fever virus and Zika virus (Flaviviridae), in cell-based systems. This antiviral activity is conserved between human and rhesus macaque ARHGEF3. | PMID:36016278 | Viruses |
| 2022 | Medium | ARHGEF3 promotes NSCLC cell proliferation in vitro and in vivo by stabilizing ATP-citrate lyase (ACLY) protein: ARHGEF3 reduces acetylation of ACLY on Lys17 and Lys86, preventing ACLY interaction with its E3 ubiquitin ligase NEDD4 and subsequent degradation. This function is independent of ARHGEF3's GEF activity. | PMID:36241648 | Cell death & disease |
| 2023 | High | ARHGEF3 is elevated in dystrophic mdx muscles and drives RhoA/ROCK activation. ARHGEF3 KO in mdx mice restores muscle quality (force production) and morphology without affecting regeneration. ARHGEF3 overexpression further compromises mdx muscle quality in a GEF activity- and ROCK-dependent manner. The ARHGEF3/ROCK pathway impairs muscle function by blocking autophagy flux, as chloroquine-mediated autophagy inhibition abolishes the benefit of ARHGEF3/ROCK inhibition. | PMID:37311604 | Journal of cachexia, sarcopenia and muscle |
| 2025 | Medium | ARHGEF3 promotes adipocyte hypertrophy and differentiation through two coordinated mechanisms: (1) RhoA-dependent facilitation of YAP nuclear translocation and YAP binding to the RhoA promoter, and (2) enhancement of PPARγ transcriptional activity, establishing a reciprocal activation loop. ARHGEF3-deficient mice on a high-fat diet show reduced weight gain and smaller adipocyte size correlated with decreased RhoA expression and altered cytoskeletal dynamics. | PMID:40216078 | Journal of advanced research |
| 2026 | Medium | Tumor-intrinsic ARHGEF3 activates the RHOA-ROCK-PTEN cascade to inhibit AKT signaling, which upregulates IRF1-dependent chemokines CXCL10 and CXCL11 (promoting T-cell infiltration) and suppresses FASN-mediated fatty acid synthesis (limiting myeloid immunosuppression). These dual effects reshape the tumor microenvironment toward T-cell inflammation. | PMID:42023986 | Advanced science |
| 2026 | Medium | ARHGEF3 restricts placode cell fate acquisition and establishes a radial gradient of P-cadherin (but not E-cadherin) across hair follicle placodes during embryonic development. In Arhgef3-KO embryos, placodes are enlarged with elevated P-cadherin at junctions and disrupted gradient, correlating with aberrant epithelial organization and altered hair follicle downgrowth geometry. | PMID:41490244 | PLoS biology |
| 2024 | Medium | miR-451a directly binds the 3'-UTR of ARHGEF3 mRNA (confirmed by dual-luciferase reporter assay), and knockdown of ARHGEF3 in K562 cells reverses hydroquinone-induced suppression of erythroid differentiation, placing ARHGEF3 as a downstream effector of the miR-451a/c-Jun axis in erythroid maturation. | PMID:38801936 | Toxicology |
| 2025 | Low | Inhibition of miR-512-3p in Moyamoya disease endothelial colony-forming cells increases ARHGEF3 expression and downstream RhoA GTPase activity, leading to enhanced tubule formation (angiogenesis rescue). Bioinformatics and functional data identify ARHGEF3 as a direct target of miR-512-3p. | PMID:40634490 | Scientific reports |
| 2024 | Low | ARHGEF3 promotes F-actin accumulation at the cell cortex and P-cadherin enrichment at cell-cell junctions in culture models, consistent with its role in hair placode morphogenesis. | PMID:39314354 | bioRxiv |

## Citations

- PMID:12221096
- PMID:21715309
- PMID:23192023
- PMID:24043828
- PMID:24840563
- PMID:25494542
- PMID:28315487
- PMID:33406419
- PMID:36016278
- PMID:36241648
- PMID:37311604
- PMID:38801936
- PMID:39314354
- PMID:40216078
- PMID:40634490
- PMID:41490244
- PMID:42023986
