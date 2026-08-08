---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABHD18
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q0P651
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 5
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABHD18 (human)

## Current model (mechanistic narrative)

ABHD18 is a conserved α/β-hydrolase that acts as the cardiolipin (CL) lipase in the CL remodelling pathway, functionally homologous to yeast Cld1 [PMID:40903572, PMID:40378955]. It deacylates CL to generate monolysocardiolipin (MLCL) in vitro, and its inactivation in cells and mice shifts the lipidome toward nascent CL [PMID:40903572]. Rather than removing a single acyl chain, ABHD18 carries out stepwise hydrolysis, further deacylating CL to dilyso-CL and beyond, with CL species bearing more than five double bonds being resistant to its activity [PMID:40378955]. In the context of TAZ deficiency (Barth syndrome), inactivation of ABHD18—genetically or with a selective covalent small-molecule inhibitor—suppresses pathological MLCL accumulation and rescues mitochondrial dysfunction and organismal morbidity/mortality across TAZ-mutant cells, mice, human patient fibroblasts, and zebrafish embryos, establishing ABHD18 as a genetic suppressor of TAZ loss-of-function and a druggable node in CL metabolism [PMID:40903572, PMID:40378955].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0016740 transferase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1430728 Metabolism
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2025 | High | ABHD18 functions as a deacylase (lipase) in the cardiolipin (CL) biosynthesis/remodelling pathway, converting CL into monolysocardiolipin (MLCL) in vitro; its inactivation in cells and mice results in a shift toward nascent CL (nCL) in serum and tissues. | PMID:40903572 | Nature |
| 2025 | High | ABHD18 inactivation rescues mitochondrial defects in TAZ-mutant cells and rescues morbidity/mortality in Barth syndrome mice, establishing ABHD18 as a genetic suppressor of TAZ loss-of-function in the CL remodelling cascade. | PMID:40903572 | Nature |
| 2025 | High | A selective covalent small-molecule inhibitor of ABHD18 was identified and shown to rescue TAZ-mutant phenotypes in human patient fibroblasts and in zebrafish embryos, pharmacologically validating ABHD18 enzymatic activity as the therapeutic target. | PMID:40903572 | Nature |
| 2025 | High | ABHD18 is functionally homologous to yeast Cld1 (the CL lipase); knockdown of Abhd18 decreased MLCL concentration in murine TAZ-knockout myoblasts, and inactivation in Drosophila substantially increased CL abundance and reversed the accumulation of deacylated CLs (MLCL and dilyso-CL) in TAZ-deficient flies. | PMID:40378955 | The Journal of biological chemistry |
| 2025 | Medium | ABHD18 does not merely remove a single fatty acid from CL but performs stepwise hydrolysis, deacylating CL further to produce dilyso-CL and beyond; CL species with more than five double bonds are resistant to ABHD18 activity. | PMID:40378955 | The Journal of biological chemistry |

## Citations

- PMID:40378955
- PMID:40903572
