---
title: "PSEPK glyoxalase batch manual research reconciliation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [gloA, gloB, PP_4040]
autolink_gene_symbols: false
---

# Glyoxalase research reconciliation

This file records manual reconciliation and provider-attempt provenance. It is
not OpenScientist output and does not substitute invented text for a failed
provider report.

## Provider Attempts

On 2026-08-13, full OpenScientist retrievals were launched for:

| Scope | Target | Provider job | Outcome |
|---|---|---|---|
| Gene | `gloA` / Q88GF8 | `2fe78084-bfe4-41db-96f1-36d30d4ae6eb` | Timed out at 7,200 seconds; no report returned |
| Gene | `gloB` / Q88FF3 | `40af5c84-b457-4368-9508-6e74ed78346e` | Timed out at 7,200 seconds; no report returned |
| Gene | `PP_4040` / Q88FP9 | `3ccb3a2a-9e63-40b5-9c72-85949df3af6f` | Timed out at 7,200 seconds; no report returned |
| Reusable module | `methylglyoxal_detoxification` | `0b5780f6-c37a-457b-b929-6c61c3c3ab48` | Timed out at 7,200 seconds; no report returned |
| Module + pathway + taxon | `methylglyoxal_detoxification` + UPA00619 + PSEPK | `e74f47f3-1dfd-4a8d-ac5b-2b836694c99a` | Timed out at 7,200 seconds; no report returned |

An isolated serial retry for `PP_4040` (`159827c6-29fc-4ab1-b98d-0392c9c51273`)
also timed out at 7,200 seconds without a report. No job was manually
terminated. The client rejects provider timeouts above 7,200 seconds, so this
was the maximum supported retrieval window.

## Evidence Reconciled

The conservative curation uses only checkable repository evidence:

- Exact PSEPK UniProt and GOA records for Q88GF8, Q88FF3, and Q88FP9.
- Exact PANTHER subfamilies `PTHR10374:SF30` for GloA and
  `PTHR43705:SF1` for GloB.
- Reviewed cross-taxon UniProt exemplars Q9HU72 and Q9I2T1, plus reviewed
  same-species GloA exemplar P16635.
- Rhea 19069 and Rhea 21864 for the two chained reactions.
- The pre-existing ppu00620 species report and cached primary literature,
  interpreted with its explicit caveat that historical *P. putida* GloA work
  does not identify PP_3766/Q88GF8 as the tested locus.

No PAINT PTN was verified for either exact family, so none is asserted.

## Conservative Conclusions

The reusable module contains two required reactions: GloA forms
(R)-S-lactoylglutathione from the methylglyoxal-glutathione hemithioacetal, and
GloB hydrolyzes that intermediate to D-lactate while regenerating glutathione.
Q88GF8 and Q88FF3 satisfy those reactions in PSEPK.

Q88FP9/PP_4040 is only a short `PTHR33993:SF1` VOC-domain glyoxalase-family
candidate. It has no GOA, EC, Rhea, pathway, cofactor, or catalytic-residue
assignment. It therefore receives no proposed GO annotation and does not
satisfy either module reaction. Direct substrate and metal testing remains the
required resolution.
