---
title: "PSEPK Lol-dependent outer-membrane lipoprotein trafficking"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [lolA, lolB, lolC, lolD, lolE]
---

# PSEPK Lol-dependent outer-membrane lipoprotein trafficking

This batch curates the complete canonical LolCDE-LolA-LolB route that moves
mature outer-membrane-destined lipoproteins from the inner membrane, across the
periplasm, and into the outer membrane.

## Workflow

- [x] Fetch all five PSEPK Lol gene records.
- [ ] Complete OpenScientist gene research.
- [x] Curate every GOA row for all five genes.
- [x] Create a species-neutral, multi-part module.
- [ ] Complete generic module research.
- [ ] Complete module + pathway + taxon research.
- [ ] Validate and render the reviews, module, and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | lolC | PP_2154 | Q88KY5 | LolCDE integral membrane subunit |
| [x] | lolD | PP_2155 | Q88KY4 | LolCDE ATPase subunit |
| [x] | lolE | PP_2156 | Q88KY3 | LolCDE integral membrane subunit |
| [x] | lolA | PP_4003 | Q88FS9 | Periplasmic lipoprotein carrier |
| [x] | lolB | PP_0724 | Q88PX4 | Outer-membrane delivery receptor |

## Boundary Decisions

- The reusable module has three substantive stages: LolCDE extraction/release,
  LolA periplasmic carriage, and LolB outer-membrane delivery.
- Lgt-LspA-Lnt lipoprotein maturation is an upstream module. The Lol route acts
  on already mature lipoproteins.
- Inner-membrane retention signals define substrate selection but are not a
  fourth enzymatic step.
- LolD directly enables ATP hydrolysis. It does not itself enable transmembrane
  transporter activity; that activity belongs to the assembled LolCDE complex.
- LolC and LolE are modeled as contributors to the complex transport function,
  rather than each being assigned a complete transporter activity.
- GO currently lacks precise molecular-function terms for LolCDE-mediated
  lipoprotein extraction, LolA carriage, and LolB delivery. These roles remain
  explicit free-text preferred terms without invented GO identifiers.
- KEGG assigns lolCDE to the broad ABC transporters pathway (ppu02010) and
  assigns lolA/lolB only to a functional transport bucket. The curated module
  restores their shared biological pathway boundary.

