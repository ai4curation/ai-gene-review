---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASPN
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9BXN1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 15
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASPN (human)

## Current model (mechanistic narrative)

ASPN (PLAP-1/asporin) is an extracellular matrix small leucine-rich repeat proteoglycan that acts as a multi-target regulator of growth factor and inflammatory signaling and as a structural organizer of connective tissue [PMID:17522060, PMID:37958972]. It directly binds BMP-2 and inhibits BMP-2-induced cytodifferentiation and mineralization, competitively blocking BMP-2 engagement of BMP receptor-IB and the downstream Smad cascade through its LRR5 motif, which alone is sufficient to recapitulate inhibition [PMID:17522060, PMID:18407830]; the N-terminal aspartic acid repeat length tunes this activity, with the D14 variant binding BMP-2 more strongly and suppressing differentiation more potently than D13 [PMID:24453179]. In contrast to its inhibitory role toward BMP-2, ASPN positively regulates FGF-2 by binding it and promoting FGF-2–FGFR1 complex formation [PMID:26239644]. ASPN also binds TLR2 and TLR4 to dampen NF-κB activation, stabilizing IκBα and reducing proinflammatory cytokine output [PMID:26399972], and it suppresses HIF-1α transcriptional activity in a hypoxia-induced feedback loop [PMID:35138637]. Consistent with a matrix-organizing function, ASPN-deficient mice show enlarged periodontal ligament space, altered collagen fibril architecture, and accelerated alveolar bone resorption [PMID:37958972]. Across mesenchymal lineages ASPN restrains osteogenic differentiation of periodontal ligament and bone marrow stromal cells while promoting adipogenesis [PMID:33654143, PMID:25038933, PMID:26031659]. In cancer, ASPN contributes to oxaliplatin resistance in colorectal cancer and amplifies MATN3-driven gastric cancer progression [PMID:36228517, PMID:39301785].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0005198 structural molecule activity
- **localization:** GO:0031012 extracellular matrix, GO:0005576 extracellular region
- **pathway (Reactome):** *(none)*
- **partners:** BMP2, BMPR1B, FGF2, FGFR1, TLR2, TLR4, HAPLN1, MATN3
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | PLAP-1/asporin directly binds BMP-2, as demonstrated by co-immunoprecipitation, and negatively regulates BMP-2-induced cytodifferentiation and mineralization of periodontal ligament (PDL) cells; overexpression inhibited mineralization while knockdown enhanced BMP-2-induced differentiation. | PMID:17522060 | The Journal of biological chemistry |
| 2008 | High | PLAP-1/asporin inhibits BMP-2 signaling by competitively preventing BMP-2 from binding to BMP receptor-IB (BMPR-IB), thereby blocking Smad activation; the leucine-rich repeat 5 (LRR5) motif is the functional domain mediating this interaction, as LRR5 mutation rescues inhibition and a 26-aa LRR5-derived peptide recapitulates inhibition. | PMID:18407830 | Biochemical and biophysical research communications |
| 2014 | Medium | The aspartic acid (D) repeat polymorphism of PLAP-1/asporin influences its functional potency: D14-PLAP-1 suppresses BMP-2-induced cytodifferentiation more strongly than D13-PLAP-1 and shows stronger binding affinity to BMP-2 by co-immunoprecipitation. | PMID:24453179 | Journal of dental research |
| 2015 | High | PLAP-1/asporin positively regulates FGF-2 activity by directly binding FGF-2 and promoting FGF-2–FGFR1 complex formation; Plap-1 knockout MEFs show defective FGF-2 responses rescued by Plap-1 transfection, and reduced FGF-2/FGFR1 co-localization. | PMID:26239644 | Journal of dental research |
| 2015 | High | PLAP-1/asporin directly binds TLR2 and TLR4 (shown by immunoprecipitation), suppresses TLR2/4-induced NF-κB activity, reduces IκBα kinase degradation, and downregulates proinflammatory cytokine expression in PDL cells and macrophages. | PMID:26399972 | Journal of dental research |
| 2021 | Medium | PLAP-1/asporin enhances adipogenesis: recombinant PLAP-1 promotes lipid accumulation in 3T3-L1 cells, Plap-1 knockout mice and Plap-1-knockdown 3T3-L1 cells show reduced lipid accumulation, and primary preadipocytes from Plap-1 KO mice exhibit less adipogenic differentiation than wild-type. | PMID:33654143 | Scientific reports |
| 2019 | Medium | 1,25(OH)2D3 suppresses PLAP-1 expression transcriptionally through a vitamin D response element (VDRE) in the PLAP-1 promoter that binds VDR, as confirmed by ChIP assay and reporter gene assays, leading to enhanced osteogenic differentiation of hPDLSCs under inflammatory conditions. | PMID:31837573 | International immunopharmacology |
| 2022 | Medium | PLAP-1/asporin suppresses HIF-1α signaling: hypoxia-induced PLAP-1 expression is HIF-1α-dependent (blocked by chetomin), and recombinant PLAP-1 or PLAP-1 gene transfection reduces hypoxia-induced HRE-luciferase activity and nuclear HIF-1α accumulation in PDL cells. | PMID:35138637 | Journal of periodontal research |
| 2022 | High | PLAP-1/asporin knockout mice display enlarged periodontal ligament space, increased collagen fibril diameter, altered ECM protein expression (elevated Col3, BGN, DCN), reduced tooth extraction force, and accelerated alveolar bone resorption with more osteoclasts in ligature-induced periodontitis, establishing a structural and protective role for PLAP-1 in PDL collagen organization and periodontal inflammation. | PMID:37958972 | International journal of molecular sciences |
| 2014 | Medium | Overexpression of PLAP-1 in rat bone marrow stromal cells (rBMSCs) inhibits their differentiation into osteoblast-like cells, reducing mineralized nodule formation and decreasing expression of osteoblast markers (Runx2, Osterix, ALP, BSP, osteocalcin). | PMID:25038933 | Journal of molecular histology |
| 2015 | Medium | Overexpression of PLAP-1 in rBMSCs transplanted into rat critical-size skull defects inhibits new bone formation and mineralization in vivo, confirming its role as a negative regulator of osteogenesis in a skeletal repair context. | PMID:26031659 | Journal of molecular histology |
| 2023 | Medium | ASPN interacts with HAPLN1, and their combined knockdown synergistically increases ALP, OPN, OCN, and COL1A1 expression and ECM mineralization in BMSCs while decreasing osteoclast markers in bone marrow macrophages, indicating ASPN and HAPLN1 cooperate to inhibit osteogenic differentiation. | PMID:37427673 | Orthopaedic surgery |
| 2022 | Medium | ASPN mediates oxaliplatin (OXA) resistance in colorectal cancer; siRNA-mediated ASPN knockdown reverses OXA resistance and promotes cell apoptosis both in vitro and in patient-derived xenograft models in vivo. | PMID:36228517 | Biomaterials |
| 2026 | Medium | Exosomal miR-143-5p from H. pylori-infected epithelial cells functions as a nuclear activating microRNA (NamiRNA) that binds the super-enhancer region of the ASPN gene, increases H3K27ac enrichment, and promotes ASPN transcription in fibroblasts, leading to upregulation of pro-inflammatory cytokines (IL-4, IL-6, TGF-β); in vivo antagomir-143-5p reduced ASPN and cytokine expression and alleviated gastric inflammation. | PMID:41723544 | Gut pathogens |
| 2024 | Medium | ASPN overexpression amplifies MATN3-driven gastric cancer cell proliferation, migration, and invasion, and MATN3-ASPN protein-protein interaction was confirmed; co-overexpression of MATN3 and ASPN enhanced tumor growth and metastasis in vivo. | PMID:39301785 | Human molecular genetics |

## Citations

- PMID:17522060
- PMID:18407830
- PMID:24453179
- PMID:25038933
- PMID:26031659
- PMID:26239644
- PMID:26399972
- PMID:31837573
- PMID:33654143
- PMID:35138637
- PMID:36228517
- PMID:37427673
- PMID:37958972
- PMID:39301785
- PMID:41723544
