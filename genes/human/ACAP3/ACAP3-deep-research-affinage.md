---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACAP3
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: Q96P50
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

# Affinage mechanistic annotation for ACAP3 (human)

## Current model (mechanistic narrative)

ACAP3 is a GTPase-activating protein (GAP) selective for the small GTPase Arf6 that governs cell morphological dynamics in both neural development and epithelial cancers [PMID:27330119]. In neurons, ACAP3 drives neurite outgrowth by cycling Arf6 between its GTP- and GDP-bound states; loss of ACAP3 raises GTP-bound Arf6 and abolishes outgrowth, a defect rescued by wild-type but not GAP-inactive ACAP3 [PMID:27330119], and the same GAP-dependent activity is required for cortical neuronal migration in vivo [PMID:28919417]. In cancer cells, ACAP3 acts as a tumour suppressor: in lung adenocarcinoma it inhibits EGFR signalling by impairing EGFR recycling and accelerating lysosome-mediated EGFR degradation in a GAP-activity-dependent manner, suppressing proliferation [PMID:41520057], and in papillary thyroid carcinoma it suppresses viability, migration, and invasion while promoting apoptosis through modulation of AKT and p53 signalling [PMID:39098591]. ACAP3 expression is held down epigenetically, via Myc-driven DNA hypermethylation and deacetylation in lung adenocarcinoma [PMID:41520057] and via HDAC2 in papillary thyroid carcinoma [PMID:39098591].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** ARF6, EGFR
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | ACAP3 functions as a GTPase-activating protein (GAP) specific to Arf6 in mouse hippocampal neurons. Knockdown of ACAP3 abrogated neurite outgrowth, which was rescued by wild-type ACAP3 but not by a GAP-inactive mutant. ACAP3 knockdown significantly increased GTP-bound Arf6 levels, confirming its role as an Arf6 GAP. Cycling between active and inactive forms of Arf6, regulated by ACAP3 together with a guanine-nucleotide-exchange factor, is required for neurite outgrowth. | PMID:27330119 | The Biochemical journal |
| 2017 | High | ACAP3 is required for neuronal migration in the developing mouse cerebral cortex in vivo. In utero knockdown of ACAP3 significantly impaired cortical neuron migration and the associated morphological changes; rescue with wild-type ACAP3 restored migration, but a GAP-inactive mutant did not, indicating the mechanism depends on Arf6 GAP activity. | PMID:28919417 | Biochemical and biophysical research communications |
| 2024 | Medium | HDAC2 negatively regulates ACAP3 expression in papillary thyroid carcinoma (PTC) cells. ACAP3 overexpression suppressed viability, proliferation, migration, and invasion, and promoted apoptosis of PTC cells, modulating AKT and p53 signalling (decreased p-AKT/AKT ratio, increased p-p53/p53 ratio, altered Bcl-2/Bax and E-cadherin/N-cadherin expression); HDAC2 overexpression reversed the tumour-suppressive effects of ACAP3. | PMID:39098591 | The international journal of biochemistry & cell biology |
| 2026 | Medium | Myc mediates epigenetic silencing of ACAP3 via DNA hypermethylation and deacetylation in lung adenocarcinoma (LUAD). ACAP3 inhibits EGFR signalling by impairing EGFR recycling and accelerating lysosome-mediated EGFR degradation in a GAP activity-dependent manner, thereby suppressing LUAD cell proliferation in vitro and in vivo. | PMID:41520057 | British journal of cancer |
| 2010 | Low | The intronic minisatellite UPS29 of the ACAP3 (CENTB5) gene possesses enhancer-like activity in neuronal-type cells (rat astrocytes) but not uniformly across cell types, as demonstrated by reporter gene (EGFP) transient transfection assays in HeLa, F9, and rat astrocyte cultures. | PMID:21105360 | Tsitologiia |

## Citations

- PMID:21105360
- PMID:27330119
- PMID:28919417
- PMID:39098591
- PMID:41520057
