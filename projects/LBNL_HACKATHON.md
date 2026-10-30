---
title: "LBNL Hackathon: Dark Protein Atlas genes"
maturity: SCOPING
tags: [EVALUATION]
species: [LACLM, LACLA]
genes: [sufB, yxcA]
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
| LACLA/yxcA | *Lactococcus lactis* subsp. *lactis* IL1403 | Q9CDI2 | [NZ_VXKC01000008.1_19](https://gene-annotate-dashboard.kbase.us/review/NZ_VXKC01000008.1_19) | PlsA plasmalogen biosynthesis protein combining activation and reduction/dehydration functions for anaerobic plasmalogen production | supported (GO:0016836 hydro-lyase is an overreach) |

## Notes

- The dashboard sequence for NZ_LKLC01000161.1_58 is 100% identical to A2RMK5
  (llmg_1969), so the review is filed under the MG1363 reference proteome.
- The dashboard sequence for NZ_VXKC01000008.1_19 (UniParc UPI00072AC48C,
  RefSeq WP_081041604) had no active UniProt entry: its two TrEMBL records,
  A0A0V8CX59 and A0A2A5SIM0, were deleted as "Not part of a reference
  proteome". The review is filed under the closest reference-proteome
  entry, Q9CDI2 (IL1403 *yxcA*, 98.3% identical). The protein is the
  single-chain anaerobic plasmalogen synthase PlsA, not HgdC. Reviewing it
  turned up a GO labelling problem: GO:0047159 "plasmalogen synthase
  activity" is an acyltransferase on lysoplasmalogen. It also showed that
  GO has no MF term for the anaerobic, vinyl-ether-forming activity. Draft
  GO issues for both points are pending.
