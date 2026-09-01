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
- [ ] Complete OpenScientist gene research (lolB and lolC complete; three jobs running).
- [x] Curate every GOA row for all five genes.
- [x] Create a species-neutral, multi-part module.
- [x] Complete generic module research.
- [x] Complete module + pathway + taxon research.
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
- LolC and LolE are modeled as integral components of the complex extraction
  machinery, without GO:0022857. LolCDE uses MacB-like mechanotransmission to
  extract cargo from the outer leaflet rather than conducting it through a
  membrane pore.
- GO currently lacks precise molecular-function terms for LolCDE-mediated
  lipoprotein extraction, LolA carriage, and LolB delivery. These roles remain
  explicit free-text preferred terms without invented GO identifiers.
- KEGG assigns lolCDE to the broad ABC transporters pathway (ppu02010) and
  assigns lolA/lolB only to a functional transport bucket. The curated module
  restores their shared biological pathway boundary.
- LolB research supports the terminal receptor/insertion role but found no
  direct KT2440 structure, biochemistry, or essentiality experiment; detailed
  mechanism remains transferred from E. coli and Pseudomonas aeruginosa.
- Generic module research supports the three-stage post-maturation boundary
  and confirms that LolCDE extracts cargo by mechanotransmission rather than
  translocating it through a membrane pore.
- The canonical route is not universal across all diderms: some lineages use
  homodimeric LolF-like extractors or lack canonical LolB. This module is the
  reusable LolCDE-LolA-LolB implementation, with lineage replacements left for
  grounded variants.
- The species-aware report correctly finds all five KT2440 components and no
  biological gap. Its additional claim that the ppu02010 candidate set contains
  no Lol genes is rejected: the wrapper prompt displayed only the first 80 of
  207 candidates, while the local partition explicitly assigns lolC, lolD, and
  lolE to ppu02010.
- Recent model-organism bypass experiments caution against asserting universal
  LolA/LolB essentiality. No such bypass or essentiality result is projected
  onto KT2440.
