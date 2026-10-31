---
title: "LBNL Hackathon: Dark Protein Atlas genes"
maturity: SCOPING
tags: [EVALUATION]
species: [LACLM, LACLA, SALTY, ECOLI]
genes: [sufB, ybbO, yxcA]
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
| SALTY/ybbO | *Salmonella enterica* serovar Typhimurium LT2 | Q7CR11 | not linked | n/a | NADPH-dependent aldehyde reductase (GO:0008106), by 1:1 orthology to E. coli YbbO |
| ECOLI/ybbO | *Escherichia coli* K-12 | P0AFP4 | not linked | n/a | NADPH-dependent aldehyde reductase (GO:0008106), direct assays |

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
- SALTY/ybbO (STM0505) and its E. coli orthologue ECOLI/ybbO (b0493) were reviewed
  during the hackathon on request rather than picked from the queue, so they have no
  dashboard item or dashboard call yet. (The dashboard sits behind a Cloudflare bot
  check, so it could not be searched from the review session.) The Salmonella
  protein has no experiments of its own; its function rests on E. coli YbbO, whose
  purified enzyme reduces C2-C18 aldehydes with NADPH. The transfer is supported by
  reciprocal best hits across both proteomes, conserved gene order (ybbN-ybbO-tesA-ybbA),
  90.6% identity and an invariant catalytic tetrad (N105-S133-Y146-K150), with only one
  of 24 substitutions in the predicted active-site pocket. See
  `genes/SALTY/ybbO/ybbO-bioinformatics/RESULTS.md`.
- A sequence-only OpenScientist run on SALTY/ybbO reached the same activity call but
  identified the protein from an exact UniParc checksum match. Hiding the gene name
  therefore does not blind a sequence test; this matters for any dashboard-style
  evaluation that relies on that kind of blinding.
- For ECOLI/ybbO, a proposed retinol dehydrogenase annotation was withdrawn. Retinal
  reduction is seen only in engineered strains, has not been assayed with purified
  enzyme or a defined cofactor, and uses a substrate E. coli does not make. Studies in yeast
  disagree on how efficient it is.
