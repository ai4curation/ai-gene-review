---
title: "PSEPK peptidoglycan precursor biosynthesis and export"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK peptidoglycan precursor biosynthesis and export

This batch models the conserved pathway from UDP-N-acetylglucosamine through
UDP-MurNAc-pentapeptide, lipid I, and lipid II to translocation of lipid II
across the cytoplasmic membrane. It stops before glycan polymerization and
peptide cross-linking, which form a distinct multi-complex module.

The existing [PSEPK-aware OpenScientist satisfiability report](../deep-research/PSEPK__peptidoglycan_precursor_biosynthesis__ppu00550-deep-research-openscientist.md)
supports the KT2440 gene selection and the boundary decisions below. Generic
module structure is supported separately by the full module-level
OpenScientist report beside the module YAML.

## Workflow

- [x] Fetch the nine gene records not already present.
- [x] Run full OpenScientist research for all ten selected genes.
- [x] Curate all selected gene reviews, including every GOA row.
- [x] Create and validate the species-neutral
  `peptidoglycan_precursor_biosynthesis` module.
- [x] Run full OpenScientist module research.
- [x] Run full OpenScientist module + `ppu00550` + PSEPK research.
- [x] Render the module and project page.
- [x] Open one non-draft PR and clear review and CI.

## Wave 123 Repair

- [x] Re-audit the precursor-synthesis, lipid-carrier loading, and lipid II
  flipping boundary against the existing generic and PSEPK-aware
  OpenScientist reports.
- [x] Apply the annotation-reviewer workflow to every selected gene and every
  GOA row (69/69 rows; no `PENDING` or `UNDECIDED` decisions).
- [x] Add reviewed cross-species UniProt exemplars alongside the PSEPK proteins
  and restrict membrane locations to the three membrane-associated steps.
- [x] Verify the MurE branch, Ddl input, and MurF-to-MurJ route logic without
  importing polymerization, cross-linking, remodeling, recycling, or carrier
  supply.
- [x] Validate and render all changed outputs.
- [x] Prepare one non-draft PR and formal review request for the repaired
  module and batch.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `murA` | PP_0964 | Q88P88 | UDP-GlcNAc enolpyruvyl transfer |
| [x] | `murB` | PP_1904 | Q88LM5 | UDP-MurNAc formation |
| [x] | `murC` | PP_1338 | Q88N75 | L-alanine addition |
| [x] | `murD` | PP_1335 | Q88N78 | D-glutamate addition |
| [x] | `murE` | PP_1332 | Q88N81 | meso-diaminopimelate addition |
| [x] | `ddlB` | PP_1339 | Q88N74 | D-Ala-D-Ala dipeptide synthesis |
| [x] | `murF` | PP_1333 | Q88N80 | D-Ala-D-Ala addition to UDP-MurNAc-tripeptide |
| [x] | `mraY` | PP_1334 | Q88N79 | Lipid I synthesis |
| [x] | `murG` | PP_1337 | Q88N76 | Lipid II synthesis |
| [x] | `murJ` | PP_0601 | Q88Q94 | Lipid II translocation |

## Boundary Decisions

- `murJ` is added despite its absence from the broad KEGG `ppu00550` extract
  because lipid II translocation is required to connect cytoplasmic precursor
  synthesis to periplasmic assembly.
- `ftsW`/`ftsI`, `mrdB`/`mrdA`, class A PBPs, PbpC, and MtgA belong to the
  downstream polymerization and cross-linking module.
- `uppS` and `uppP` supply and recycle the undecaprenyl carrier but are not
  direct lipid II synthesis steps.
- D-Ala-D-Ala carboxypeptidases `dacA` and `dacB` are remodeling enzymes.
- `ddlA` and the third Ddl paralog are alternative D-Ala-D-Ala ligases in
  KT2440; the division-cluster `ddlB` copy is used as the concrete exemplar
  for this ten-gene satisfiability set. The reusable module represents the Ddl
  activity as a family role rather than encoding KT2440 paralog choice.

## Annotation-Reviewer Audit

| Gene | GOA rows | Audit result |
|---|---:|---|
| `murA` | 6 | Complete; five supported decisions retained and the demonstrably incorrect UDP-GalNAc-process IEA remains `REMOVE`. |
| `murB` | 7 | Complete; exact reductase activity and pathway retained, with redundant/broad terms kept non-core or marked over-annotated. |
| `murC` | 5 | Complete; exact L-alanine ligase activity and precursor-synthesis role retained. |
| `murD` | 7 | Complete; exact D-glutamate ligase activity retained without promoting indirect cell-shape or division terms. |
| `murE` | 8 | Complete; KT2440 meso-diaminopimelate specificity retained only in the species review. |
| `ddlB` | 6 | Complete; D-Ala-D-Ala ligation retained as the selected convergent-input activity. |
| `murF` | 7 | Complete; the DAP-specific child activity remains core while the reusable module uses the pentapeptide-generic parent. |
| `mraY` | 8 | Complete; lipid I formation is kept distinct from carrier supply and recycling. |
| `murG` | 8 | Complete; lipid II formation is kept distinct from glycan polymerization. |
| `murJ` | 7 | Complete; lipid II translocation is the terminal module step, not a polymerase activity. |

All 69 GOA-derived annotations have explicit evidence-aware decisions. The
only removal is an electronic MurA mapping to UDP-N-acetylgalactosamine
biosynthesis that conflicts with the exact UDP-N-acetylglucosamine substrate
in the target UniProt reaction. No experimental annotation is overruled.

## Reusable-Module Audit

- The module is `CONCRETE` because it encodes a chemically grounded reaction
  path, while its participants remain taxon-neutral family roles.
- Reviewed *Escherichia coli* K-12 proteins ground the conserved
  DAP-containing route; reviewed *Staphylococcus aureus* MurE Q2FZP6 grounds
  the L-lysine alternative.
- No PANTHER or PTN identifier is asserted. The shared MurE family does not
  encode DAP-versus-L-lysine substrate specificity, and an exact evolutionary
  family was not established for each reusable role.
- Molecular functions occur only on the eleven leaf annotons. Plasma membrane
  is asserted on MraY, MurG, and MurJ, the three membrane-associated steps, and
  no location is asserted at module level.
- The terminal product is exported lipid II. SEDS/class-A-PBP polymerization,
  D,D-transpeptidation, carboxypeptidase remodeling, peptidoglycan recycling,
  and undecaprenyl-carrier supply/recycling stay in their separate modules or
  pathway batches.

The complete 23-gene KEGG source snapshot remains in
`ppu00550_peptidoglycan_biosynthesis.tsv`.
