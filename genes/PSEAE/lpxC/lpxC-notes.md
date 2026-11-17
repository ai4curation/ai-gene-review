# lpxC (PA4406, P47205) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P47205 --alias lpxC`; accession matches the worklist. No
deep-research provider used. PMID:9068651 is abstract-only: PubMed MCP returned no body and Europe
PMC has no full-text XML for PMC178929.

### Literature

- [PMID:9068651 "We devised a novel, rapid, and reproducible assay for the deacetylase which facilitated purification of the enzyme in three steps."]
  Recombinant P. aeruginosa LpxC is soluble, EDTA-sensitive and reactivated by metal. UniProt cites
  the paper (ECO:0000269) for function, catalytic activity and Zn cofactor.

### Annotation decisions

- All 7 rows ACCEPT (GO:0103117 x3, GO:0009245 x3, GO:0005737 IBA). No source defects.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002134692 | GO:0009245 lipid A biosynthetic process | 2 | 79 (62 taxa) | GO:0009245, IDA, PMID:9068651 (PseudoCAP) | SOUND | The abstract states the enzyme was expressed, assayed and purified; LpxC performs the committed step of lipid A synthesis. | E. coli LpxC P0A725 | Yes (E. coli LpxC has extensive experimental support) |

The plant and Aquifex seeds of the node's GO:0103117 and GO:0005737 IBDs do not affect this gene.
