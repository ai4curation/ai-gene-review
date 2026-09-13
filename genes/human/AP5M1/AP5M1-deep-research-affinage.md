---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP5M1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9H0R1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP5M1 (human)

## Current model (mechanistic narrative)

AP5M1 (MUDENG/MuD) is a 490-amino-acid adaptin-domain-containing protein that regulates the intrinsic apoptotic program, with context-dependent pro-death and anti-apoptotic activities documented across multiple cancer cell types [PMID:18395520, PMID:27136675]. Ectopic overexpression drives cell death in Jurkat and HeLa cells, and in cervical cancer cells this killing operates strictly through the mitochondrial pathway: AP5M1 upregulates BAX and loses all apoptotic activity in BAX-knockout or BAX-knockdown cells [PMID:18395520, PMID:31427081]. During TRAIL-induced apoptosis, AP5M1 is itself a caspase-3 substrate, cleaved at D276 and D290 within its adaptin domain to generate a fragment with reduced cell-killing activity, indicating that an intact adaptin domain is required for its pro-death function [PMID:23665015]. In astroglioma cells AP5M1 acts as an anti-apoptotic factor at the Bid/Bcl-2 junction downstream of TRAIL: its depletion enhances cleavage of caspase-3, caspase-9, and Bid, drives conversion of Bcl-2 to a truncated 25-kDa pro-apoptotic fragment, and this TRAIL-sensitizing effect is abrogated by co-depletion of Bid [PMID:27136675]. AP5M1 localizes predominantly to the endoplasmic reticulum and partly to mitochondria [PMID:27136675]. Beyond its role in apoptotic signaling, no clathrin- or adaptor-complex trafficking function has been characterized for AP5M1 in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005783 endoplasmic reticulum, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-5357801 Programmed Cell Death
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | Medium | MUDENG (AP5M1) encodes a 490 amino acid protein containing an adaptin domain homologous to the mu2 subunit of adaptor protein complexes related to clathrin-mediated endocytosis; ectopic overexpression of MUDENG induced cell death in Jurkat T cells and HeLa cells, establishing it as a pro-death protein. | PMID:18395520 | Biochemical and biophysical research communications |
| 2013 | High | MUDENG (AP5M1) is cleaved by caspase-3 at residues D276 and D290 within its adaptin domain during TRAIL-induced apoptosis; in vitro cleavage assay with recombinant active caspase-3 confirmed these cleavage sites, and cleaved MUDENG showed reduced cell-killing activity, indicating that intact adaptin domain integrity is required for MUDENG's pro-death function. | PMID:23665015 | Biochemical and biophysical research communications |
| 2016 | High | MUDENG (AP5M1/MuD) functions as an anti-apoptotic protein in human astroglioma cells: MuD protein levels decrease ~33% following TRAIL stimulation (via caspase-3-mediated cleavage), stable overexpression of MuD enhanced cell survival upon TRAIL treatment (77% vs 46%), and MuD depletion increased susceptibility to TRAIL by enhancing cleavage of caspase-3, caspase-9, and Bid. MuD depletion also caused Bcl-2 conversion to a truncated pro-apoptotic 25-kDa fragment, and the TRAIL-sensitizing effect of MuD depletion was abrogated by Bid co-depletion, placing MuD function at the Bid/Bcl-2 junction. MuD localizes predominantly in the endoplasmic reticulum and partly in mitochondria. | PMID:27136675 | Oncogenesis |
| 2019 | Medium | AP5M1 (MUDENG) induces apoptosis in cervical cancer cells in a BAX-dependent manner: AP5M1 overexpression upregulated BAX protein levels, and AP5M1 completely lost apoptotic activity in BAX-knockout or BAX-knockdown cervical cancer cells, demonstrating functional dependence on BAX for the mitochondrial apoptotic pathway. | PMID:31427081 | Biochemical and biophysical research communications |
| 2013 | Low | A monoclonal antibody (M3H9) against residues 244–326 in the middle domain of human MUDENG (AP5M1) was generated, confirming protein expression in astroglioma cell lines, primary astrocytes, and formalin-fixed mouse ovary and uterus tissues, and validating the middle domain as an antigenic region. | PMID:23909422 | Monoclonal antibodies in immunodiagnosis and immunotherapy |

## Citations

- PMID:18395520
- PMID:23665015
- PMID:23909422
- PMID:27136675
- PMID:31427081
