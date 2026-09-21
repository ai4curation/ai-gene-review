---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF19
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8IW93
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 11
citation_count: 11
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF19 (human)

## Current model (mechanistic narrative)

ARHGEF19 (WGEF) is a Dbl-family Rho guanine nucleotide exchange factor that couples Wnt/planar cell polarity (PCP) signaling to Rho GTPase-driven cytoskeletal remodeling and tissue morphogenesis [PMID:15485661, PMID:18256687]. Through its DH-PH module it catalyzes nucleotide exchange on RhoA, Cdc42, and Rac1 and reorganizes the actin cytoskeleton when overexpressed [PMID:15485661]. In the Wnt-PCP branch it localizes to the plasma membrane, binds Dishevelled and Daam1, and activates RhoA to drive convergent extension; deletion of its Dishevelled-binding region yields a constitutively hyperactive form, indicating regulation by autoinhibition [PMID:18256687]. Structurally, the PDZ domain of Dishevelled2 engages a unique internal PDZ-binding motif within WGEF through an induced-fit mechanism, releasing it from autoinhibition and licensing GEF activity [PMID:38714795]. This Daam1/WGEF/Rho axis is required for pronephric tubulogenesis [PMID:21804089] and supports renal primary ciliogenesis in mammalian kidney epithelia [PMID:31469868]. In cancer, ARHGEF19 acquires a RhoA-independent role: its DH and PH domains bind BRAF in non-small cell lung cancer and HRAS in small cell lung cancer to activate MAPK/ERK signaling and promote tumor cell proliferation [PMID:29164615, PMID:32993957], and it is a direct target of miR-503 in hepatocellular carcinoma where its expression counters miR-503-mediated suppression of proliferation and metastasis [PMID:24405610]. Its requirement for Wnt/Dvl-induced RhoA activation is context-dependent, as it is dispensable in N1E-115 cells where other RhoGEFs predominate [PMID:20810787].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005886 plasma membrane, GO:0005929 cilium
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** DVL2, DAAM1, BRAF, HRAS, RHOA, ANKK1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | Medium | WGEF (ARHGEF19) is a RhoGEF with a classical DH-PH domain and a C-terminal SH3 domain that activates RhoA, Cdc42, and Rac1 (pulldown assay), and forced expression causes actin cytoskeleton rearrangement consistent with activation of these GTPases. | PMID:15485661 | Biochemical and biophysical research communications |
| 2008 | High | WGEF (ARHGEF19) is a component of the Wnt-PCP pathway in Xenopus: it preferentially localizes to the plasma membrane, binds Dishevelled and Daam-1, and its overexpression activates RhoA and rescues convergent extension suppressed by dominant-negative Wnt-11; depletion suppresses convergent extension rescued by RhoA or ROCK activation. Deletion of the Dishevelled-binding domain generates a hyperactive form. | PMID:18256687 | The EMBO journal |
| 2009 | Medium | WGEF (ARHGEF19) expression is regulated by DNA methylation at CpG sites in exon 1: demethylation occurs during adipogenesis of 3T3-L1 cells, and forced WGEF expression inhibits adipogenic marker gene expression and the adipogenic program, placing WGEF as a negative regulator of adipocyte differentiation. | PMID:19503838 | PloS one |
| 2010 | Medium | In mammalian (N1E-115) cells, WGEF shRNA did NOT suppress Dvl- and Wnt-3a-induced neurite retraction or RhoA activation, indicating that WGEF is not the primary RhoGEF for Wnt/Dvl-induced RhoA activation in this cellular context (p114-RhoGEF and Lfc/GEF-H1 fulfil this role instead). | PMID:20810787 | Molecular biology of the cell |
| 2011 | Medium | WGEF (ARHGEF19) and its binding partner Daam1 are expressed in the developing pronephric anlagen of Xenopus and zebrafish; inhibiting components of the Daam1/WGEF/Rho PCP pathway branch significantly reduces pronephric tubulogenesis, establishing this pathway as required for kidney tubule morphogenesis. | PMID:21804089 | Journal of the American Society of Nephrology |
| 2013 | Medium | ARHGEF19 is a direct target gene of miR-503 in hepatocellular carcinoma cells, as demonstrated by luciferase reporter assay; ARHGEF19 overexpression overcomes miR-503-mediated suppression of HCC cell proliferation and metastasis. | PMID:24405610 | The Journal of surgical research |
| 2017 | Medium | ARHGEF19 interacts with BRAF and activates the MAPK pathway in a RhoA-independent manner in non-small cell lung cancer cells: ARHGEF19 overexpression promotes MEK1/2 phosphorylation and both the DH and PH domains are required for this effect. | PMID:29164615 | International journal of cancer |
| 2019 | Medium | Knockdown of ArhGEF19 (WGEF) in polarized mammalian kidney epithelial cells (MDCKII and IMCD3) leads to loss of primary cilia, establishing a role for ARHGEF19 in renal ciliogenesis in vitro; however, knockdown of WGEF in Xenopus kidney did not produce the same cilia loss. | PMID:31469868 | PloS one |
| 2020 | Medium | ARHGEF19 promotes small cell lung cancer cell growth via interaction of its DH and PH domains with HRAS to activate the MAPK/ERK pathway. | PMID:32993957 | Biochemical and biophysical research communications |
| 2024 | High | The PDZ domain of Dishevelled2 (Dvl2PDZ) binds and activates WGEF via a unique 'internal PDZ-binding motif' (IPM) within WGEF, releasing it from autoinhibition; residues at P2, P0, P-2, and P-3 of the IPM stabilize the interaction, and MD simulations reveal an induced-fit mechanism for Dvl2PDZ binding. | PMID:38714795 | Communications biology |
| 2024 | Low | ANKK1 binds WGEF (ARHGEF19) in SH-SY5Y neuroblastoma cells and regulates its interaction with RhoA; during neuronal differentiation, the ANKK1–WGEF interaction is downregulated while the ANKK1–FARP1 interaction increases, suggesting ANKK1 coordinates Wnt/PCP GEF switching for bidirectional F-ACTIN control. | PMID:39409035 | International journal of molecular sciences |

## Citations

- PMID:15485661
- PMID:18256687
- PMID:19503838
- PMID:20810787
- PMID:21804089
- PMID:24405610
- PMID:29164615
- PMID:31469868
- PMID:32993957
- PMID:38714795
- PMID:39409035
