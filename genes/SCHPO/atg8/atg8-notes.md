# SCHPO atg8 manual review notes

## Scope

Reviewed all seeded `existing_annotations` for `SCHPO/atg8` against the cached GOA-supporting papers, UniProt `O94272`, and `interpro/panther/PTHR10969/PTHR10969-paint.tsv`.

Deep-research provider runs were not available in this worktree because credentials are blocked, so these are manual notes rather than a generated `atg8-deep-research-*.md`.

## PANTHER / PAINT

`atg8` is UniProt `O94272`, a 121 aa S. pombe member of PANTHER family `PTHR10969` / InterPro `IPR004241`.

PAINT places the canonical ATG8-family autophagy annotations on the eukaryotic node `PTN000103522`:

- `GO:0000045 autophagosome assembly`
- `GO:0000421 autophagosome membrane`
- `GO:0000423 mitophagy`
- `GO:0008429 phosphatidylethanolamine binding`
- `GO:0006995 cellular response to nitrogen starvation`
- `GO:0097352 autophagosome maturation`

Those transfers are biologically consistent with the single-copy S. pombe ATG8. The short mitophagy donor list is not a weakness: fission yeast has its own Atg43 receptor evidence showing that forced mitochondrial Atg8 recruitment restores mitophagy in `atg43`-deficient cells [PMID:33138913].

PAINT also places `GO:0000329 fungal-type vacuole membrane` on fungal node `PTN000861115`, seeded by both `PomBase:SPBP8B7.24c` and `SGD:S000000174`. The S. pombe self-source is expected because the PomBase experimental row is part of the descendant evidence used to place the IBD node; it is not circular or weak. The 2018 Hfl1 paper directly supports this location [PMID:30451685].

## Cached literature

- [PMID:30451685] Liu et al. identified the Hfl1-vacuole-membrane pathway. Atg8 physically interacts with Hfl1, is recruited to the vacuole membrane in a lipidation-independent manner, and acts with Hfl1 in a non-autophagic pathway that maintains vacuole morphology.
- [PMID:31941401] Yu et al. identified Atg38 as a PtdIns3K complex I subunit and showed that its fission-yeast-specific AIM binds Atg8 at the PAS to create a positive-feedback loop for efficient autophagosome formation.
- [PMID:33138913] Fukuda et al. identified Atg43 as the fission-yeast mitochondrial outer-membrane mitophagy receptor and showed that Atg43's AIM tethers Atg8-positive isolation membranes to mitochondria.
- [PMID:32735772] Zhao et al. identified Epr1 as a soluble Atg8-interacting ER-phagy receptor. The cache is abstract-only, so the review removes only the generic `protein binding` row and leaves reticulophagy as a curator question rather than a `NEW` assertion.
- [PMID:41917004] Ma et al. identified Npr1 as a second Atg8-binding nucleophagy receptor that works with Epr1. The abstract directly states that Atg8 colocalizes with Npr1 and/or Epr1 on nuclear-envelope protrusions that detach as nucleophagy-cargo-containing autophagosomes, which supports adding `GO:0044804 nucleophagy`.

The 2006 ORFeome paper [PMID:16823372], the 2007 and 2009 early autophagy papers [PMID:17295836; PMID:19778961], and the 2015 DJ-1/Hsp31 paper [PMID:26624998] were useful for localization-marker rows but did not change the core functional model.

## 2024-2026 search

Manual PubMed query:

`(atg8[Title/Abstract]) AND (Schizosaccharomyces pombe[Title/Abstract] OR fission yeast[Title/Abstract]) AND 2024:2026[pdat]`

Manual EuropePMC query:

`(TITLE_ABS:atg8) AND ((TITLE_ABS:"Schizosaccharomyces pombe") OR (TITLE_ABS:"fission yeast")) AND FIRST_PDATE:[2024-01-01 TO 2026-12-31]`

Results:

- PMID:41917004, Ma et al. 2026, `Nucleophagy is promoted by two autophagy receptors and inhibited by chromatin-nuclear envelope tethering in fission yeast.` This is new primary evidence for Atg8 in nucleophagy and was cached for the review.
- PMID:40057225, Kumar et al. 2025, `Yeast Knowledge Graphs Database for Exploring Saccharomyces Cerevisiae and Schizosaccharomyces Pombe.` This is a knowledge-graph/database paper, not new primary Atg8 biology.
- PMID:39603377, Li and Huang 2025, `Schizosaccharomyces pombe Grx4 is subject to autophagic degradation under nitrogen- and iron- starvation and ER-stress.` This implicates AIM-dependent autophagic turnover of Grx4 but did not warrant a new Atg8 annotation.
- EuropePMC also found the 2025 bioRxiv preprint of Ma et al. and the 2024 bioRxiv preprint of Kumar et al.; the peer-reviewed papers supersede both preprints for this review.

## Curation decisions

The generic `GO:0005515 protein binding` IPI rows to Hfl1, Atg38, Epr1, and Atg43 all reflect true physical interactions but were all marked `REMOVE` because generic protein binding is not a useful molecular-function assertion and there is no more specific GO molecular-function term for "Atg8 binding to an AIM-containing receptor/regulator" to use as a replacement.

The `GO:0005737 cytoplasm` rows were marked `TOO_GENERAL` because accepted cytosol, PAS, autophagosome membrane, and fungal-type vacuole membrane rows capture the functional sites more precisely.

The generic `GO:0005774 vacuolar membrane` rows were refined to `GO:0000329 fungal-type vacuole membrane`, which is directly supported by the Hfl1 paper and by the fungal PAINT node. The broad `GO:0000324 fungal-type vacuole` row from PomBase was kept as a non-core vacuole-proper localization because the cached abstract is insufficient to re-interpret the 2009 GFP-Atg8 processing evidence as a membrane observation.

The high-throughput `GO:0005634 nucleus` row was marked over-annotated because the ORFeome localization screen is not supported by directed Atg8 studies; the 2026 nucleophagy paper places Atg8 on outer-nuclear-membrane protrusions rather than in the nucleus interior.

`GO:0044804 nucleophagy` was added as a conservative `NEW` assertion from the 2026 Npr1/Epr1 paper. This passes the participation test: Atg8 is recruited by outer-nuclear-membrane receptors to nuclear-envelope protrusions that become autophagosomes containing nucleophagy cargo; Atg8 is part of the machinery that builds/captures cargo into the autophagosome rather than a cargo substrate.
