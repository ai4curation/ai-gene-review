---
title: "PSEPK ppu00240 de novo UMP biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [carA, carB, pyrB, pyrC, pyrD, pyrE, pyrF]
autolink_gene_symbols: false
---

# PSEPK ppu00240: de novo UMP biosynthesis

- Module: `de_novo_pyrimidine_synthesis`
- Pathway context: KEGG `ppu00240` (pyrimidine metabolism)
- Focused genes: 7
- Broad membership-table candidates: 36

## Boundary

This batch covers the six reactions from glutamine-dependent carbamoyl-phosphate
formation through UMP:

1. `carA` and `carB`: glutamine-dependent carbamoyl-phosphate synthesis
2. `pyrB`: N-carbamoyl-L-aspartate formation
3. `pyrC`: dihydroorotate ring closure
4. `pyrD`: quinone-dependent orotate formation
5. `pyrE`: OMP formation from orotate and PRPP
6. `pyrF`: OMP decarboxylation to UMP

Carbamoyl phosphate also feeds arginine biosynthesis. Pyrimidine salvage,
nucleotide interconversion, RNA turnover, and DNA-precursor synthesis are
outside this module even though they occur in the broad KEGG bucket.

## Status

- [x] Fetch all seven focused genes from UniProt and GOA.
- [x] Curate all seven focused gene reviews.
- [x] Replace the three-node human fusion-centric module with six reusable reaction leaves.
- [x] Add exact PSEPK UniProt exemplars while retaining CAD, DHODH, and UMPS as cross-species architecture exemplars.
- [ ] Complete module + `ppu00240` + PSEPK OpenScientist research.
- [ ] Complete OpenScientist gene-level research for the seven focused genes.
- [x] Validate the module and all focused gene reviews.
- [ ] Render the gene reviews and batch page.
- [ ] Open one PR for this module and shepherd review and CI.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `carA` | PP_4724 | Q88DU5 | CPS glutaminase chain | Retain glutaminase and dual UMP/arginine roles; remove unsupported ATP binding |
| `carB` | PP_4723 | Q88DU6 | CPS ATP-dependent chain | Retain ammonia- and glutamine-dependent CPS context; remove glutamine metabolism assigned to the wrong chain |
| `pyrB` | PP_4998 | Q88D30 | aspartate carbamoyltransferase | Retain exact activity and de novo UMP process; remove amino-acid-metabolism transfer |
| `pyrC` | PP_1086 | Q88NW7 | dihydroorotase | Retain exact activity and zinc as non-core; reject redundant unsupported cytosol call |
| `pyrD` | PP_2095 | Q88L40 | quinone-dependent dihydroorotate dehydrogenase | Retain exact activity and plasma membrane; remove conflicting cytoplasm call |
| `pyrE` | PP_5291 | Q88C92 | orotate phosphoribosyltransferase | Retain exact activity and de novo UMP process; remove ribonucleoside-process transfer |
| `pyrF` | PP_1815 | Q88LW2 | OMP decarboxylase | Retain exact activity and final de novo UMP step |

## Evidence Notes

All seven PSEPK exemplars have reviewed UniProt entries with exact reaction,
pathway, and family assignments. The module models six chemical leaves rather
than bundling the first three reactions into CAD and the final two into UMPS.
Shared InterPro domain families connect the separate bacterial enzymes and
fused human exemplars without implying that the fusion architecture is
universal.

No cytoplasm/cytosol term is asserted at module level. PyrD alone carries a
leaf-specific membrane location in its gene review because the reviewed record
explicitly identifies it as a peripheral cell-membrane protein. The broad
candidate inventory is retained in
[`ppu00240_de_novo_pyrimidine_synthesis.tsv`](ppu00240_de_novo_pyrimidine_synthesis.tsv).
