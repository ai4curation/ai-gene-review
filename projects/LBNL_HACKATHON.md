---
title: "LBNL Hackathon: Dark Protein Atlas genes"
maturity: SCOPING
tags: [EVALUATION]
species: [LACLM, LACLA]
genes: [sufB, yudI]
---

# LBNL Hackathon: Dark Protein Atlas genes

A collection of gene reviews made during the LBNL hackathon. Each gene comes
from the KBase Dark Protein Atlas review queue
(https://gene-annotate-dashboard.kbase.us/review), where an LLM pipeline proposes
a function and GO terms for a poorly annotated bacterial protein and a curator
judges the call.

For each queue item we find the matching UniProt entry (an identical or
near-identical sequence), write a standard gene review, and record the verdict
on the dashboard's call in the gene notes file.

## Genes

| Gene | Organism | UniProt | Dashboard item | Dashboard call | Verdict |
|---|---|---|---|---|---|
| LACLM/sufB | *Lactococcus lactis* subsp. *cremoris* MG1363 | A2RMK5 | [NZ_LKLC01000161.1_58](https://gene-annotate-dashboard.kbase.us/review/NZ_LKLC01000161.1_58) | SufB Fe-S cluster assembly scaffold protein of the SUF system | supported |
| LACLA/yudI | *Lactococcus lactis* subsp. *lactis* IL1403 | Q9CE84 | [CP006766.1_2177](https://gene-annotate-dashboard.kbase.us/review/CP006766.1_2177) | DusB-like FMN-dependent tRNA-dihydrouridine synthase | supported |

## Notes

- The dashboard sequence for NZ_LKLC01000161.1_58 is 100% identical to A2RMK5
  (llmg_1969), so the review is filed under the MG1363 reference proteome.
- The dashboard sequence for CP006766.1_2177 differs from Q9CE84 (IL1403 L19272) at one
  position (E267G), so the review is filed under the IL1403 reference proteome.
