# ITGA5 mechanobiology review notes

## Research setup

- `just fetch-gene human ITGA5` seeded the GOA review and fetched the missing cached publications available from the seed.
- `just deep-research-falcon human ITGA5 --fallback perplexity-lite` was attempted for an external narrative review, but neither the Falcon nor Perplexity provider was available in this runtime. I therefore reviewed the seeded cached publications and the existing human `ITGB1` review manually.

## Main curation decisions

- Treat ITGA5 as the alpha subunit of the alpha5-beta1 fibronectin receptor. Its core GO surface is `GO:0004895` cell adhesion receptor activity, `GO:0001968` fibronectin binding, `GO:0007160` cell-matrix adhesion, `GO:0007229` integrin-mediated signaling pathway, `GO:0034674` integrin alpha5-beta1 complex, and focal-adhesion/plasma-membrane localization.
- Keep angiogenesis, definitive endoderm differentiation, CD40L signaling, P-selectin binding, ruffle/ruffle-membrane localization, anoikis, and wound-spreading outcomes as non-core: these are real ligand- or tissue-specific readouts of alpha5beta1 receptor function rather than the receptor's primary molecular role.
- Remove or refine the many `GO:0005515` protein binding rows. Alpha5-beta1 pairing belongs on `GO:0034674`, fibronectin/fibrillin/COMP rows are extracellular-matrix ligand binding rows, and protease/cytokine/cell-adhesion-molecule ligands get their specific binding term when the row's own paper supports one.
- Rows derived from `PMID:10022831`, `PMID:19141530`, and the receptor-crosstalk subset of `PMID:19267251` are alphaV-beta3 rows that landed on ITGA5. These were removed with `source_defects` for the upstream assigned-by groups.

## Mechanosensation scope

Alpha5-beta1 is a force-bearing extracellular-matrix receptor at focal adhesions, not a direct mechanosensitive ion channel. The reviewed evidence supports alpha5beta1 as a matrix-binding receptor and integrin signaling initiator upstream of focal-adhesion force coupling; it does not support `GO:0008381` mechanosensitive ion channel activity or direct sensory `detection of mechanical stimulus` BP terms.
