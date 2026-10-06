---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF26
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q96DR7
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 13
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF26 (human)

## Current model (mechanistic narrative)

ARHGEF26 (SGEF) is a RhoG-specific guanine nucleotide exchange factor that couples membrane remodeling and cell-cell adhesion to processes spanning leukocyte transendothelial migration, angiogenesis, epithelial junction assembly, and pathogen entry [PMID:15133129, PMID:23372835]. Its DH/PH module catalyzes nucleotide exchange selectively on RhoG (not Rac1/Rac3), and this catalytic activity drives macropinocytosis and is required for RhoG-dependent endothelial docking structure formation around ICAM-1 clusters that supports leukocyte transmigration, a function whose loss reduces atherosclerosis in mice [PMID:15133129, PMID:23372835]. GEF activity is gated by Src-mediated phosphorylation at Y530 in the DH domain, which suppresses RhoG binding and activation and inhibits cell migration [PMID:27437949]. In epithelia, SGEF assembles into a ternary complex with Scribble and Dlg1, targets to apical junctions in a Scribble-dependent manner, and uses both its GEF activity (E-cadherin adherens junctions, 3D cyst lumen formation) and a separable scaffolding activity (actomyosin contractility, ZO-1 stability, tight junction barrier function) to coordinate junction integrity [PMID:31248911, PMID:39350674]. Beyond catalysis, ARHGEF26 performs GEF-independent functions: it delays EGFR endosomal-to-lysosomal trafficking and inhibits EGFR ubiquitination to sustain downstream signaling, including NRF2 activation [PMID:23661635, PMID:40829739], and it stabilizes the transcription factor SOX2 by blocking K48-linked polyubiquitination in glioblastoma stem cells [PMID:41936941]. SGEF expression is induced by TWEAK-Fn14/NF-κB signaling, and nuclear SGEF complexes with BRCA1 to modulate DNA damage responses [PMID:26764186]. A CAD-risk coding variant (p.Val29Leu) confers gain-of-function with enhanced proangiogenic signaling, and ARHGEF26 promotes VEGFR2 macropinocytosis required for VEGF-dependent angiogenesis [PMID:34849650].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060089 molecular transducer activity, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005856 cytoskeleton, GO:0005768 endosome
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1500931 Cell-Cell communication, R-HSA-5653656 Vesicle-mediated transport, R-HSA-168256 Immune System, R-HSA-1266738 Developmental Biology
- **partners:** RHOG, SRC, SCRIB, DLG1, BRCA1, EGFR, SOX2
- **complexes:** Scribble-SGEF-Dlg1 ternary complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | SGEF (ARHGEF26) is a RhoG-specific guanine nucleotide exchange factor: recombinant SGEF DH/PH domain exchanged nucleotide on RhoG but not on Rac1 or Rac3 in vitro, and full-length SGEF activated RhoG (but not Rac) in fibroblasts. SGEF stimulated macropinocytosis in a manner requiring a catalytically active DH domain and the full-length protein. | PMID:15133129 | Molecular biology of the cell |
| 2004 | Medium | SGEF requires its proline-rich N-terminus to generate dorsal membrane ruffles (but not lateral ruffles), and requires a functional SH3 domain to colocalize with filamentous actin at sites of membrane protrusion. | PMID:15133129 | Molecular biology of the cell |
| 2003 | Medium | SGEF protein contains DH and PH domains, an N-terminal proline-rich domain, a C-terminal SH3 domain, and two nuclear localization signals. An alternate androgen-responsive promoter drives expression of a truncated isoform (CSGEF) in prostate and liver. | PMID:12697679 | Endocrinology |
| 2013 | High | SGEF-deficient mice crossed with ApoE-null mice show reduced atherosclerosis; SGEF-null mouse aortic endothelial cells display decreased RhoG activation around ICAM-1 clusters and reduced endothelial docking structures, establishing that SGEF promotes leukocyte transendothelial migration via RhoG-dependent docking structure formation. | PMID:23372835 | PloS one |
| 2013 | Medium | SGEF delays EGFR trafficking from early to late endosomes, thereby slowing EGFR lysosomal degradation and enhancing EGFR signaling and cell migration in prostate cancer cells; this function is independent of its GEF catalytic activity. | PMID:23661635 | Carcinogenesis |
| 2016 | High | Src kinase tyrosine-phosphorylates SGEF at Y530 within the DH domain, which suppresses SGEF interaction with RhoG, reduces RhoG activation, and inhibits SGEF-mediated cell migration; Y530F mutation blocks this inhibitory effect. | PMID:27437949 | PloS one |
| 2016 | Medium | SGEF expression is upregulated by TWEAK-Fn14 signaling via NF-κB activity; nuclear SGEF complexes with BRCA1 following temozolomide treatment, and SGEF knockdown reduces BRCA1 phosphorylation and sensitizes glioma cells to temozolomide-induced apoptosis. | PMID:26764186 | Molecular cancer research : MCR |
| 2019 | High | SGEF forms a ternary complex with Scribble and Dlg1; SGEF targets to apical junctions in a Scribble-dependent manner and regulates actomyosin contractility and tight junction barrier function (scaffolding activity) as well as E-cadherin adherens junction formation and 3D cyst lumen formation (GEF activity). Polarity establishment is not controlled by SGEF. | PMID:31248911 | The Journal of cell biology |
| 2021 | High | ARHGEF26 promotes Salmonella invasion into host epithelial cells in a serovar- and cell-type-dependent manner: it regulates SopB- and SopE-dependent S. Typhi infection in HeLa cells and SopB/SopE2-independent S. Typhimurium infection in polarized MDCK cells. DLG1, an ARHGEF26-associated protein, shows similar serovar-specific knockdown phenotypes. In vivo, Arhgef26 deletion reduces S. Typhimurium burden in enteric fever model and reduces colitis-associated inflammation. | PMID:34242364 | PLoS pathogens |
| 2022 | High | ARHGEF26 promotes macropinocytosis of VEGFR2 at the cell membrane, is required for VEGF-dependent angiogenesis in ECs, and promotes vessel sprouting ex vivo. Global or EC-specific (but not vascular smooth muscle cell-specific) ARHGEF26 deletion reduces atherosclerosis and enhances plaque stability in mice. A CAD-risk coding variant (p.Val29Leu) results in gain-of-function ARHGEF26 with enhanced proangiogenic signaling and protein interactions. | PMID:34849650 | Cardiovascular research |
| 2024 | Medium | The Scribble-SGEF-Dlg1 ternary complex is required for ZO-1 protein stability and tight junction permeability; SGEF alone (not Scribble or Dlg1) is required to regulate E-cadherin levels. Loss of SGEF destabilizes the E-cadherin/catenin complex, triggering endocytosis of E-cadherin, β-catenin nuclear signaling, and Slug-mediated transcriptional repression of E-cadherin in a positive feedback loop. | PMID:39350674 | Journal of cell science |
| 2025 | Medium | SGEF enhances EGFR stability by inhibiting its ubiquitination, leading to sustained downstream NRF2 activation and ferroptosis inhibition in cardiomyocytes; EGFR inhibitor osimertinib counteracts the cardioprotective effect of SGEF overexpression in pressure-overload cardiac hypertrophy. | PMID:40829739 | Cellular signalling |
| 2026 | Medium | ARHGEF26 interacts with and stabilizes the stemness transcription factor SOX2 by inhibiting K48-linked polyubiquitination and proteasomal degradation of SOX2 in glioblastoma stem cells. | PMID:41936941 | Laboratory investigation |

## Citations

- PMID:12697679
- PMID:15133129
- PMID:23372835
- PMID:23661635
- PMID:26764186
- PMID:27437949
- PMID:31248911
- PMID:34242364
- PMID:34849650
- PMID:39350674
- PMID:40829739
- PMID:41936941
