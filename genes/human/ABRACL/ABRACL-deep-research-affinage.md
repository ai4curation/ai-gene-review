---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABRACL
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q9P1F3
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABRACL (human)

## Current model (mechanistic narrative)

ABRACL is a small winged helix-like protein that regulates actin cytoskeletal dynamics and cell motility, a role conserved from the Dictyostelium ortholog Costars, whose loss produces aberrant F-actin distribution and excessive pseudopod formation that human ABRACL rescues [PMID:20940261]. Structurally it adopts a three-helix, four-stranded antiparallel β-sheet winged helix-like fold that lacks DNA-binding activity and presents a conserved hydrophobic groove implicated in protein–protein interaction [PMID:21082705]. Mechanistically, ABRACL binds cofilin and inhibits cofilin-stimulated F-actin depolymerization, shifting the F/G-actin balance toward polymerized actin at the leading edge to drive cell migration [PMID:33670794]. This actin-promoting activity underlies a recurrent pro-tumorigenic role: ABRACL knockdown suppresses proliferation, migration, and invasion across esophageal, breast, gastric, and glioma cancer models [PMID:33728339, PMID:35341461, PMID:39286126, PMID:39376051], with its expression transcriptionally activated by MYBL2 and CBX4 [PMID:35341461, PMID:39376051] and post-transcriptionally repressed by miR-145-5p [PMID:33728339]. In neural progenitor cells ABRACL localizes to the nucleus and inhibits neuronal differentiation, indicating a context-dependent role distinct from its cytoplasmic actin function [PMID:26537243].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0005856 cytoskeleton, GO:0005634 nucleus
- **pathway (Reactome):** *(none)*
- **partners:** CFL1, MYBL2, CBX4
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | Dictyostelium Costars (ortholog of human ABRACL) is required for normal actin dynamics and cell motility: cosA-null cells show aberrant F-actin distribution, increased cytoskeleton-associated actin, and excessive pseudopod formation. Expression of the human ABRACL counterpart rescued these defects, establishing functional conservation. | PMID:20940261 | Journal of cell science |
| 2011 | High | The solution structure of human ABRACL (HSPC280) was determined by NMR: it adopts a winged helix-like fold with three α-helices and four antiparallel β-strands, lacks DNA-binding activity, and contains a conserved hydrophobic groove (shared with the ABRA C-terminal domain family) proposed to mediate protein–protein interactions. The protein presents an unusually long wing-1 loop and asymmetric charge distribution. | PMID:21082705 | Protein science |
| 2015 | Medium | ABRACL (HSPC280) is localized to the nucleus in neural progenitor cells, and its overexpression in Neuro2a cells inhibits neuronal differentiation in vitro, placing it in the regulation of neural progenitor proliferation vs. differentiation. | PMID:26537243 | Histochemistry and cell biology |
| 2021 | High | Human ABRACL physically interacts with cofilin (supported by immunofluorescence colocalization at the leading edge and proximity ligation assay), and inhibits cofilin-stimulated F-actin depolymerization in vitro (pyrene actin assay), thereby promoting actin polymerization and cell migration. | PMID:33670794 | International journal of molecular sciences |
| 2021 | Medium | miR-145-5p directly targets the ABRACL 3′-UTR (validated by dual-luciferase reporter assay), reducing ABRACL expression and consequently suppressing proliferation, migration, and invasion of esophageal carcinoma cells. | PMID:33728339 | BioMed research international |
| 2022 | Medium | The transcription factor MYBL2 directly transcriptionally activates ABRACL expression in breast cancer cells (validated by luciferase reporter assay and ChIP), and MYBL2 overexpression reverses the suppressive effects of ABRACL knockdown on proliferation, invasion, migration, and EMT. | PMID:35341461 | Bioengineered |
| 2024 | Medium | ABRACL knockdown in glioma cells inhibits proliferation, migration, invasion, and cytoskeletal dynamics and induces apoptosis and cell-cycle arrest; these effects are associated with activation (not suppression) of STAT3 signaling, suggesting ABRACL acts upstream of STAT3 to promote glioma malignancy. | PMID:39286126 | Heliyon |
| 2024 | Medium | The transcription factor CBX4 binds the ABRACL promoter and transcriptionally upregulates ABRACL expression in gastric cancer cells (validated by luciferase reporter and ChIP); CBX4 overexpression reverses the inhibitory effects of ABRACL silencing on proliferation, migration, invasion, and apoptosis. | PMID:39376051 | Histology and histopathology |

## Citations

- PMID:20940261
- PMID:21082705
- PMID:26537243
- PMID:33670794
- PMID:33728339
- PMID:35341461
- PMID:39286126
- PMID:39376051
