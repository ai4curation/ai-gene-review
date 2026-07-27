---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADCK5
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q3MIX3
self_evaluation_pairwise: win
faith_pct: 50.0
n_discoveries: 5
citation_count: 5
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADCK5 (human)

## Current model (mechanistic narrative)

ADCK5 is an atypical kinase implicated in cancer cell motility and in cellular senescence of airway epithelium. In lung cancer cells, ADCK5 phosphorylates the transcription factor SOX9 at serine 181, and phospho-SOX9 in turn upregulates the oncogene PTTG1, defining an ADCK5–SOX9–PTTG1 axis that drives invasion and migration [PMID:32277958]. In airway epithelial cells, ADCK5 overexpression elevates senescence markers (SA-β-gal, P21, P16), increases ROS and γH2AX, impairs mitochondrial membrane potential, and activates PI3K/AKT phosphorylation, placing ADCK5 upstream of the PI3K/AKT axis in senescence [PMID:41222693]. Beyond these gain-of-function and phenotypic studies, no direct in vitro reconstitution of ADCK5 kinase activity or substrate biochemistry has been characterized in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** SOX9
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | Medium | ADCK5 promotes invasion and migration of lung cancer cells by phosphorylating transcription factor SOX9, with serine 181 identified as a required phosphorylation site; phospho-SOX9 then upregulates the oncogene PTTG1, defining an ADCK5-SOX9-PTTG1 signaling pathway. | PMID:32277958 | Experimental cell research |
| 2024 | Low | ADCK5 protein expression is upregulated in cancer cells following BET bromodomain inhibitor (JQ1) treatment, confirmed by immunoblotting, suggesting ADCK5 as a compensatory kinase target in BRD inhibitor resistance. | PMID:39241280 | Neoplasia (New York, N.Y.) |
| 2025 | Medium | ADCK5 overexpression in airway epithelial cells increases markers of cellular senescence (SA-β-gal-positive cells, P21, P16), elevates ROS and γH2AX, impairs mitochondrial membrane potential, and activates PI3K/AKT phosphorylation, placing ADCK5 upstream of the PI3K/AKT signaling axis in airway epithelial senescence. | PMID:41222693 | Naunyn-Schmiedeberg's archives of pharmacology |
| 2025 | Low | ADCK5 is identified as a highly expressed senescence-related gene in severe asthma airway cells; Leucokinin VIII acetate inhibits ADCK5 expression and reduces excessive cellular senescence in vitro, establishing ADCK5 as a driver of airway cell senescence. | PMID:40885090 | International immunopharmacology |
| 2024 | Low | A PPI network analysis identified strong interactions between ADCK5 and MFN1 (mitofusin-1) and between BNIP3 and NBR1 in the context of mitochondria-related gene networks, suggesting ADCK5 participates in mitochondrial protein interaction networks. | PMID:38783263 | BMC medical genomics |

## Citations

- PMID:32277958
- PMID:38783263
- PMID:39241280
- PMID:40885090
- PMID:41222693
