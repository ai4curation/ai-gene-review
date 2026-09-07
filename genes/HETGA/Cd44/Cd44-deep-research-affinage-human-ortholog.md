---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/CD44
affinage_run_date: 2026-06-09T22:57:17
uniprot_accession: P16070
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 20
citation_count: 20
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for CD44 (human)

## Current model (mechanistic narrative)

CD44 is a transmembrane glycoprotein that serves as the principal cell-surface receptor for hyaluronan (HA), mediating HA endocytosis and routing it to lysosomes for degradation, although the protein itself has no intrinsic catalytic activity toward HA [PMID:1370836]. HA recognition is conformationally gated by glycosylation: N-linked glycans at multiple sites within the HA-recognition domain, together with membrane-proximal glycosaminoglycan attachment motifs, are required for binding, and the avidity of the interaction scales with HA size, receptor density, and an inducible activation state that controls ligand retention [PMID:8601595, PMID:10871609]. CD44 transduces these adhesive cues into intracellular signaling and is regulated by sequential proteolysis: ADAM10-catalyzed ectodomain shedding, augmented by CD44 ligation and Rac1-driven cytoskeletal remodeling, is followed by γ-secretase intramembrane cleavage to liberate a CD44 intracellular domain (CD44-ICD) that enters the nucleus and activates transcription [PMID:14623895, PMID:15596040]. Through its cytoplasmic tail CD44 couples to cytoskeletal and signaling machinery—binding IQGAP1, signaling via RhoA to sustain YAP/Hippo output, and engaging Syk/Rac1/PI3K to act as a phagocytic receptor independent of Fc receptors [PMID:16455948, PMID:21117172, PMID:25101858]. CD44 functions as a Wnt co-receptor by associating with and positioning LRP6 [PMID:25301071], suppresses TLR2-driven NF-κB inflammation via its cytoplasmic domain [PMID:18322236], and promotes lymphocyte survival by engaging PI3K-Akt to limit Fas-mediated apoptosis [PMID:20079666, PMID:7545465]. In cancer, CD44 supports Kras-MAPK-driven lung adenocarcinoma, drives invasion through a Snail1→MT1-MMP axis, sustains stemness and proliferation through CD44-ICD-dependent transcription, and orchestrates endocytosis of iron-bound hyaluronates that catalyzes histone demethylation to enforce mesenchymal epigenetic plasticity through an iron-CD44 positive feedback loop [PMID:25566991, PMID:32747755, PMID:23208496, PMID:35954411]. CD44 itself is transcriptionally repressed by the androgen receptor through a defined androgen-response-element silencer [PMID:33687952].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0038024 cargo receptor activity, GO:0098631 cell adhesion mediator activity, GO:0060089 molecular transducer activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005764 lysosome
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-168256 Immune System, R-HSA-5653656 Vesicle-mediated transport, R-HSA-1643685 Disease, R-HSA-4839726 Chromatin organization
- **partners:** LRP6, TLR2, IQGAP1, ADAM10, COL17A1, GPNMB
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1992 | High | CD44 mediates the endocytosis and lysosomal degradation of hyaluronan; antibodies against CD44 block HA uptake and internalization in fibroblasts and macrophages, and agents blocking lysosomal acidification (chloroquine, NH4Cl) inhibit subsequent HA degradation. CD44 itself lacks intrinsic degradative activity, as isolated membrane preparations containing CD44 do not break down HA. | PMID:1370836 | The Journal of cell biology |
| 1996 | High | N-linked glycosylation of CD44 is required for hyaluronan binding; tunicamycin abolishes HA-mediated cell adhesion, while mutation of any one of five N-linked glycosylation sites within the HA-recognition domain abrogates binding. Mutation of Ser-Gly motifs providing glycosaminoglycan attachment sites in the membrane-proximal domain also impairs HA binding, indicating that specific glycosylation patterns maintain the HA-recognition domain in the appropriate conformation. | PMID:8601595 | The Journal of cell biology |
| 2000 | High | HA binding at the cell surface involves multivalent interactions dependent on HA size, CD44 density, and CD44 activation state. Monovalent binding requires 6–18 sugar residues; divalent binding begins at ~20–38 residues. An inducing anti-CD44 mAb (IRAWB14) dramatically slows HA dissociation from the cell surface (without affecting binding kinetics), revealing that CD44 activation state is a key regulator of HA retention. | PMID:10871609 | The Journal of biological chemistry |
| 2003 | High | CD44 undergoes ectodomain shedding catalyzed by ADAM10 (a disintegrin and metalloproteinase 10), which is augmented by CD44 ligation and Rac1-mediated cytoskeletal rearrangement. CD44 engagement activates Rac1, causing redistribution of CD44 to membrane ruffles at the leading edge; ADAM10 knockdown by RNAi suppresses CD44 cleavage. CD44 cleavage promotes tumor cell migration and invasion. | PMID:14623895 | The Journal of biological chemistry |
| 2004 | Medium | CD44 undergoes sequential proteolytic cleavages: (1) ectodomain shedding regulated by metalloproteinases and triggered by multiple stimuli, which controls cell attachment to and migration on HA matrix; (2) subsequent intramembranous cleavage by presenilin-dependent γ-secretase, generating a CD44 intracellular domain (CD44-ICD) that translocates to the nucleus and activates transcription. | PMID:15596040 | Cancer science |
| 2006 | High | CD44 functions as a primary phagocytic receptor: macrophages expressing CD44 efficiently engulf HA-coated beads and anti-CD44-opsonized erythrocytes via a mechanism involving Syk kinase, Rac1, and PI3-kinase, and inducing phagocyte oxidase activation. CD44-deficient macrophages cannot perform this phagocytosis, and the pathway is independent of Fc receptors. | PMID:16455948 | Blood |
| 2008 | Medium | CD44 directly associates with TLR2 upon stimulation by the TLR2 ligand zymosan and negatively regulates TLR-mediated NF-κB activation and proinflammatory cytokine production in vivo. The cytoplasmic domain of CD44 is required for this regulatory effect on TLR signaling. | PMID:18322236 | Journal of immunology |
| 2010 | High | CD44 promotes survival of effector Th1 cells by limiting Fas-mediated apoptosis, thereby enabling memory Th1 cell generation. CD44 ligation engages the PI3K-Akt signaling pathway in Th1 cells. This survival function is Th1-specific and is not observed in Th2, Th17, or CD8+ T cells despite equivalent CD44 expression. | PMID:20079666 | Immunity |
| 2010 | Medium | CD44 interacts with IQGAP1 (an actin-binding protein) via its intracellular C-terminus; an endogenous CD44-IQGAP1 complex was demonstrated in normal and transformed cell types, linking CD44 to cytoskeletal reorganization. | PMID:21117172 | IUBMB life |
| 2014 | High | CD44 acts as a positive regulator of the Wnt receptor complex by physically associating with LRP6 upon Wnt stimulation and modulating LRP6 membrane localization. CD44 knockdown decreases, and overexpression increases, Wnt/β-catenin signaling activity. Epistasis experiments place CD44 function at the level of LRP6. CD44 regulates Wnt target gene expression (tcf-4 and en-2) in Xenopus brain development. | PMID:25301071 | Cell death and differentiation |
| 2014 | Medium | CD44 signals through RhoA to regulate YAP expression and nuclear localization in the Hippo pathway. CD44 knockdown reduces RhoA expression, and constitutively active RhoA (RhoA-V14) rescues the YAP decrease caused by CD44 knockdown. CD44 knockdown also reduces expression of YAP target genes (CTGF, Cyr61, EDN1) and promotes apoptosis while inhibiting proliferation and migration. | PMID:25101858 | Cellular signalling |
| 2015 | Medium | CD44 regulates pancreatic cancer invasion through a CD44→Snail1→MT1-MMP (MMP14) axis: CD44 drives expression of the EMT transcription factor Snail1, which in turn regulates membrane-bound MT1-MMP expression required for invasion. Loss of CD44 reduces Snail1 and MT1-MMP levels and abolishes invasion in vitro and in vivo. | PMID:25566991 | Molecular cancer research |
| 2017 | Low | Atomistic molecular dynamics simulations reveal that hyaluronan binds CD44's hyaluronan-binding domain via three topographically distinct binding modes. The crystallographic mode is the strongest; two metastable modes are more frequently observed in unbiased simulations. CD44 can diffuse along HA in a 1D manner when attached via weaker modes, potentially influencing CD44 aggregation kinetics relevant to signaling. | PMID:28715483 | PLoS computational biology |
| 2018 | Medium | GPNMB attenuates astrocyte inflammatory responses through CD44: recombinant GPNMB reduces cytokine-induced iNOS, nitric oxide, ROS, and IL-6 in astrocytes, and this anti-inflammatory effect is abolished in CD44 knockout astrocytes, establishing CD44 as the required receptor for GPNMB-mediated neuroprotection. | PMID:29519253 | Journal of neuroinflammation |
| 2020 | High | CD44 mediates endocytosis of iron-bound hyaluronates, providing an alternative iron-uptake mechanism in mesenchymal-state cells. Internalized iron acts as a metal catalyst to demethylate repressive histone marks (H3K9me2/me3 and H3K27me3), thereby governing expression of mesenchymal genes and enabling epigenetic plasticity. CD44 expression is itself transcriptionally upregulated by nuclear iron through a positive feedback loop, in contrast to the negative iron regulation of transferrin receptor. | PMID:32747755 | Nature chemistry |
| 2021 | Medium | CD44 regulates membrane accumulation of COL17A1 (collagen XVII) in multilayered transformed epithelia. CD44 and COL17A1 accumulate in oncogene (RasV12, Src, ErbB2)-transformed epithelial cells, suppress mitochondrial ROS production, and thereby promote resistance to ferroptosis-mediated cell death during cell extrusion, enabling clonal expansion of transformed cells. | PMID:34087104 | Current biology |
| 2012 | Medium | CD44 is required for Kras-mediated MAPK signaling and lung adenocarcinoma formation in vivo: deletion of CD44 in a KrasG12D mouse model attenuates MAPK pathway activation, reduces tumor cell proliferation, decreases lung adenocarcinoma formation, and prolongs survival. | PMID:23208496 | Oncogene |
| 1995 | Medium | CD44 engagement (by HA or anti-CD44 mAbs) inhibits apoptosis induced by anti-CD3 mAbs and dexamethasone in T cells, but not UV-induced (p53-dependent) apoptosis, without upregulating Bcl-2 or affecting proliferation. This places CD44 as a survival signal that specifically counteracts TCR- and glucocorticoid-mediated apoptotic pathways. | PMID:7545465 | Blood |
| 2021 | Medium | CD44 depletion (CRISPR/Cas9 KO) in GBM cells impairs proliferation (decreased Ki67, reduced CREB phosphorylation, elevated p16), decreases stemness, and induces senescence. γ-Secretase inhibition (DAPT, blocking CD44-ICD release) phenocopies some of these effects, suggesting CD44-ICD-dependent transcriptional regulation. CD44 KO also deregulates HAS2 and hyaluronan synthesis, and downregulation of HAS2 reduces CD44 protein levels, indicating a CD44/hyaluronan positive feedback circuit. | PMID:35954411 | Cancers |
| 2021 | High | Androgen receptor (AR) directly represses CD44 transcription through a novel androgen response element silencer in the CD44 locus, as demonstrated by CRISPR-based mutagenesis of the ARE. AR ChIP-seq and transcriptomics confirmed CD44 as an AR-regulated gene, and AR and CD44 expression are inversely correlated in human bladder tumors. | PMID:33687952 | Cancer research |

## Citations

- PMID:10871609
- PMID:1370836
- PMID:14623895
- PMID:15596040
- PMID:16455948
- PMID:18322236
- PMID:20079666
- PMID:21117172
- PMID:23208496
- PMID:25101858
- PMID:25301071
- PMID:25566991
- PMID:28715483
- PMID:29519253
- PMID:32747755
- PMID:33687952
- PMID:34087104
- PMID:35954411
- PMID:7545465
- PMID:8601595
