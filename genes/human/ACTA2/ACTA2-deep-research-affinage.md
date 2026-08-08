---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTA2
affinage_run_date: 2026-06-09T22:02:39
uniprot_accession: P62736
self_evaluation_pairwise: win
faith_pct: 83.33333333333333
n_discoveries: 20
citation_count: 20
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACTA2 (human)

## Current model (mechanistic narrative)

ACTA2 encodes smooth muscle α-actin, the dominant actin isoform of vascular smooth muscle cells and myofibroblasts, where it provides the structural filament that supports myosin-driven contraction and cell motility [PMID:26153420, PMID:24204762]. Pathogenic missense variants act largely through allosteric and dominant-negative effects on filament behavior: R258C destabilizes filaments, sensitizes them to cofilin severing, expands the G-actin pool by tighter profilin binding, and slows myosin-driven motility [PMID:26153420]; R149C is additionally retained by the CCT chaperonin folding complex, lowering mutant monomer levels and reducing penetrance while enhancing aberrant formin-driven nucleation [PMID:34600884]; and modeling of R179 places it at the inter-strand filament interface, consistent with its severe phenotype [PMID:26637293]. Functionally, these variants drive a contractile-to-synthetic phenotypic switch in SMCs, increasing proliferation and migration while reducing contractility — a switch that is reversible by base-editing correction of R179H in iPSC-SMCs and humanized mice, and by metabolic rescue (boosting oxidative respiration with nicotinamide riboside) in R179C SMCs [PMID:40378078, PMID:40603847, PMID:34244757]. Beyond its structural role, ACTA2 loss perturbs cytoskeletal signaling, reducing ERK1/2 phosphorylation in myofibroblasts and altering RhoA/Rac1 balance [PMID:24204762]. ACTA2 transcription is repressed by the purine-rich element binding protein Purβ, which binds the purine-rich strand of the promoter MCAT cis-element as a homodimer through electrostatic and hydrophobic ssDNA interactions and recruits the corepressor YBX1 [PMID:23724822, PMID:27064749], and is epigenetically tuned by histone H4 acetylation at its promoter and by H3K27 trimethylation that mediates sustained angiotensin II-induced silencing [PMID:25853442, PMID:35360022]. In some cell types Acta2 is functionally dispensable, as cardiac fibroblast-specific deletion is compensated by upregulation of other actin isoforms [PMID:36007455].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-397014 Muscle contraction, R-HSA-74160 Gene expression (Transcription), R-HSA-1266738 Developmental Biology
- **partners:** MYH11, CCT, TPM (SMOOTH MUSCLE TROPOMYOSIN), CFL (COFILIN), PFN (PROFILIN)
- **complexes:** CCT/TCP1 chaperonin (transient client)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | High | The R258C mutation in smooth muscle α-actin (SM α-actin, ACTA2) disrupts actin filament stability: R258C filaments are less stable than WT, more susceptible to severing by cofilin, and smooth muscle tropomyosin provides little protection from cofilin cleavage of mutant filaments. Profilin binds tighter to the R258C monomer, increasing the pool of G-actin. In an in vitro motility assay, smooth muscle myosin moves R258C filaments more slowly than WT, and under loaded conditions small ensembles of myosin are unable to produce force on R258C actin-tropomyosin filaments, suggesting tropomyosin occupies an inhibitory position on mutant actin. These defects are allosteric—many cannot be explained by direct interaction with the mutated residue. | PMID:26153420 | Proceedings of the National Academy of Sciences of the United States of America |
| 2021 | High | The common ACTA2 variant p.Arg149Cys (R149C) causes increased retention of mutant SM α-actin in the chaperonin-containing TCP1 (CCT) folding complex, reducing the amount of mutant protein that reaches functional levels in smooth muscle cells. This explains reduced penetrance: enhanced CCT binding lowers mutant monomer levels, minimizing its effect on SMC function. In vitro motility assays confirmed decreased interaction of R149C mutant filaments with SM myosin. TIRF microscopy showed enhanced nucleation of R149C SM α-actin by formin, correlating with disorganized and reduced actin filaments in Acta2R149C/+ SMCs. | PMID:34600884 | The Journal of biological chemistry |
| 2025 | High | The ACTA2 R179H pathogenic variant causes a dramatic phenotypic switch in human iPSC-derived smooth muscle cells from a contractile to a synthetic state, associated with increased proliferation and migration and reduced contractility. CRISPR adenine base editing (ABE8e-SpCas9-VRQR) correcting R179H prevented this phenotypic switch and restored normal SMC function in vitro. In humanized R179H mice, in vivo AAV9-delivered base editing rescued aortic dilation/dissection, bladder enlargement, gut dilation, and hydronephrosis. | PMID:40378078 | Circulation |
| 2025 | High | SMCs carrying the Acta2 R179C mutation fail to fully differentiate and maintain stem cell-like features including increased migration and elevated glycolytic flux compared to WT SMCs. Boosting mitochondrial oxidative respiration with nicotinamide riboside (NR) drives differentiation and decreases migration of mutant SMCs. In an Acta2SMC-R179C/+ mouse carotid injury model, mutant mice develop intraluminal SMC accumulation causing moyamoya-like occlusive lesions, neurological symptoms, and neuron loss; NR treatment prevents all of these phenotypes. | PMID:40603847 | Nature communications |
| 2013 | High | Purine-rich element binding protein B (Purβ) represses ACTA2 transcription by cooperatively binding the sense (purine-rich) strand of the ACTA2 5′ promoter-enhancer MCAT cis-element as a homodimer with three separate ssDNA-binding modules formed by inter- and intramolecular subdomain interactions. Purβ knockdown in mouse embryo fibroblasts promoted myofibroblast-like morphology, increased ACTA2 expression (confirmed by promoter-reporter assay), and increased cell migration. Discrete Purβ subdomains mediating ssDNA binding, protein-protein interaction with corepressor YBX1, and ACTA2 enhancer inhibition were mapped. | PMID:23724822 | Biochemistry |
| 2016 | High | Purβ represses ACTA2 transcription through electrostatic and hydrophobic interactions with the purine-rich ssDNA of the MCAT element in the Acta2 promoter. Site-directed mutagenesis of basic residues R267 (intermolecular subdomain) and K82/R159 (intramolecular subdomains) reduced both ssDNA binding affinity and Acta2 repressor activity in fibroblast promoter-reporter assays. R267A mutation additionally impaired binding to the Acta2 corepressor YBX1. | PMID:27064749 | Biochemistry |
| 2013 | Medium | ACTA2 is required for myofibroblast cell motility and contraction in hepatic stellate cells. Inhibition of Acta2 by multiple knockdown techniques reduced cellular motility and contraction without affecting other cytoplasmic actin isoforms. Acta2 knockdown was also associated with a significant reduction in ERK1/2 phosphorylation, indicating ACTA2 regulates signaling (MAPK pathway) in addition to its structural role. | PMID:24204762 | PloS one |
| 2022 | High | Cardiac fibroblast-specific deletion of Acta2 does not prevent myofibroblast differentiation or impair post-MI cardiac repair. Acta2-null cardiac myofibroblasts show normal proliferation, migration, and contractility and a normal total filamentous actin level because deletion triggers compensatory transcriptional upregulation of non-Acta2 actin isoforms (particularly Actg2 and Acta1). MRTF-A is critical for myofibroblast differentiation but is not required for this compensatory response. | PMID:36007455 | Journal of molecular and cellular cardiology |
| 2015 | Medium | TGF-β2 treatment of lens epithelial cells increases histone H4 acetylation specifically at the ACTA2 promoter region (assessed by ChIP), correlating with increased ACTA2 mRNA and protein expression and EMT. The HDAC inhibitor trichostatin-A (TSA) suppresses TGF-β2-induced ACTA2 upregulation and EMT while globally elevating acetylated H4 (but reducing H4 acetylation at the ACTA2 promoter under TGF-β2 stimulation). | PMID:25853442 | Eye (London, England) |
| 2016 | Medium | EGFR/HER2 dimerization induces ACTA2 expression through a JAK2/STAT1 signaling pathway in breast cancer cells. HER2 overexpression increases both STAT1 and ACTA2 protein levels; STAT1 inhibition (fludarabine) or JAK2 inhibition (AG490) decreases basal ACTA2 expression, and STAT1 overexpression increases ACTA2. ACTA2 knockdown suppresses cell motility in vitro and reduces lung metastatic nodules in vivo. | PMID:28881584 | Oncotarget |
| 2013 | Medium | ACTA2 expression in lung adenocarcinoma cells is required for metastatic potential: ACTA2 knockdown impairs in vitro migration, invasion, clonogenicity, and transendothelial penetration without affecting proliferation, and reduces in vivo metastatic potential. ACTA2 downregulation reduces c-MET and FAK expression in lung adenocarcinoma cells and is accompanied by loss of mesenchymal characteristics. | PMID:23995859 | Clinical cancer research |
| 2018 | Medium | Deletion of ACTA2 in mice promotes angiotensin II-induced aortic lumen dilation, with increased expression of osteopontin (OPN), elevated Bax/Bcl-2 ratio, increased VSMC apoptosis, and phenotypic modulation of VSMCs compared to WT mice receiving AngII. Baseline ACTA2 knockout mice had no severe vascular phenotype. | PMID:30233845 | Journal of thoracic disease |
| 2020 | Low | ACTA2 downregulation in neural stem cells (NSCs) inhibits migration by impeding actin filament polymerization via increased RhoA expression and decreased Rac1 expression, placing ACTA2 upstream of RhoA/Rac1 GTPase balance in NSC cytoskeletal regulation. | PMID:32508931 | Stem cells international |
| 2021 | Medium | ACTA2 pathogenic variants (ACTA2, MYH11) in transdifferentiated VSMC-like cells show impaired migration velocity and reduced contractility (ACTA2) and decreased SMAD2 phosphorylation in ACTA2 cells, providing functional evidence that ACTA2 mutations directly impair SMC contractile and migratory function. | PMID:34244757 | Human molecular genetics |
| 2024 | Medium | Novel ACTA2 missense variants associated with TAAD act through a dominant-negative mechanism on yeast actin, disrupting actin cytoskeletal organization and mitochondrial distribution. Wild-type yeast expressing heterozygous mutant ACTA2 alleles showed significant increases in cells with abnormal mitochondrial distribution and abnormal actin cytoskeleton organization, consistent with dominant-negative interference with WT actin function. | PMID:38486025 | European journal of human genetics |
| 2015 | Low | 3D molecular modeling of the actin filament structure revealed that the R179 residue is positioned at the interface between the two strands of filamentous actin, and the R179H mutation destabilizes inter-strand bundling, providing a structural explanation for the severe vascular phenotype associated with this mutation. | PMID:26637293 | Acta neuropathologica communications |
| 1990 | High | The vascular smooth muscle actin gene (ACTSA/ACTA2) was assigned to human chromosome 10, specifically the long arm at q22-q24, by Southern blot analysis of rodent-human somatic cell hybrids and in situ hybridization. | PMID:2398629 | Jinrui idengaku zasshi. The Japanese journal of human genetics |
| 2022 | Medium | Transient angiotensin II infusion causes sustained downregulation of ACTA2 (α-smooth muscle actin) in aortic tissue beyond AngII withdrawal, associated with increased H3K27me3 at aortic nuclei and decreased myocardin (MYOCD) expression, indicating epigenetic silencing of ACTA2 as a 'vascular memory' mechanism. This was reproduced in cultured human aortic VSMCs. | PMID:35360022 | Frontiers in cardiovascular medicine |
| 2023 | Medium | In Hirschsprung disease (HSCR) aganglionic segments, ACTA2 expression is abnormally elevated specifically in circular smooth muscle beginning at embryonic day E15.5 in Ednrb−/− mice. siRNA knockdown of Acta2 in intestinal smooth muscle cells (iSMCs) weakens their contraction ability, demonstrating that elevated ACTA2 directly drives hyperactive contraction in aganglionic bowel. | PMID:37278766 | Pediatric surgery international |
| 2014 | Low | RHOA knockdown significantly downregulates ACTA2 gene expression in both osteoblast-like and osteoclast-like cells, placing RHOA upstream of ACTA2 in a bone cell regulatory pathway. | PMID:24840563 | PloS one |

## Citations

- PMID:23724822
- PMID:2398629
- PMID:23995859
- PMID:24204762
- PMID:24840563
- PMID:25853442
- PMID:26153420
- PMID:26637293
- PMID:27064749
- PMID:28881584
- PMID:30233845
- PMID:32508931
- PMID:34244757
- PMID:34600884
- PMID:35360022
- PMID:36007455
- PMID:37278766
- PMID:38486025
- PMID:40378078
- PMID:40603847
