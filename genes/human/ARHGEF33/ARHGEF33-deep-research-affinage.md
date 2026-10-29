---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF33
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: A8MVX0
self_evaluation_pairwise: 
faith_pct: 50.0
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

# Affinage mechanistic annotation for ARHGEF33 (human)

## Current model (mechanistic narrative)

ARHGEF33 is a guanine nucleotide exchange factor that activates the small GTPase RhoA and feeds into the RhoA-ROCK signaling axis to control cytoskeletal contractility and neurite morphology [PMID:33293601]. Its GEF activity toward RhoA is demonstrated by Rhotekin-RBD pulldown of active RhoA [PMID:33293601], and in neuronal cells its expression inhibits neurite extension in a manner partially reversed by ROCK inhibition, placing it upstream of RhoA-ROCK in this process [PMID:33293601]. Beyond this RhoA-ROCK-linked role in cytoskeletal regulation, the upstream regulatory inputs and physiological substrates of ARHGEF33 are uncharacterized in the available corpus; its transcription is responsive to the C/EBPδ transcription factor in fibroblasts [PMID:23245923].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** RHOA
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | Medium | ARHGEF33 protein exhibits GEF (guanine nucleotide exchange factor) activity toward RhoA, as demonstrated by a pull-down assay using Rhotekin-RBD. | PMID:33293601 | Scientific reports |
| 2020 | Low | Overexpression of ARHGEF33 in HEK293 cells induces cell contraction, consistent with RhoA activation downstream of ARHGEF33. | PMID:33293601 | Scientific reports |
| 2020 | Medium | ARHGEF33 expression inhibits neurite extension in Neuro 2A cells; this inhibition is partially rescued by a Rho-kinase (ROCK) inhibitor, placing ARHGEF33 upstream of RhoA-ROCK signaling in neurite outgrowth. | PMID:33293601 | Scientific reports |
| 2020 | Low | ARHGEF33 is expressed in the middle layer of the inner nuclear layer at the parafovea of the zebra finch retina, suggesting predominant expression in Müller glial cells during foveal development. | PMID:33293601 | Scientific reports |
| 2012 | Low | ARHGEF33 (ArhGEF33) is identified as a C/EBPδ-dependent, trans-regulated gene in mouse embryonal fibroblasts; its expression is regulated downstream of C/EBPδ transcription factor activity, classifying it as a cytoskeletal regulator in the context of cell spreading and contact guidance on nanometric grooves. | PMID:23245923 | Biomaterials |

## Citations

- PMID:23245923
- PMID:33293601
