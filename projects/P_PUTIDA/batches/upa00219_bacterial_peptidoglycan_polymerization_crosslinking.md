---
title: "PSEPK bacterial peptidoglycan polymerization and crosslinking batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ftsW, mrdB, ftsI, mrdA-I, mrdA-II, mrcA, mrcB, mtgA, pbpC, dacA]
autolink_gene_symbols: false
---

# PSEPK peptidoglycan polymerization and crosslinking

- Module seed: `bacterial_peptidoglycan_polymerization_crosslinking`
- Upstream boundary: exported lipid II from `peptidoglycan_precursor_biosynthesis`
- Selected genes: 10

## Workflow

- [x] Confirm no prior PSEPK PR covers this downstream module.
- [x] Define a reusable module with more than one substantive part.
- [x] Fetch all selected PSEPK genes.
- [ ] Complete ten OpenScientist gene runs.
- [x] Complete generic module OpenScientist research.
- [x] Complete module + ppu00550 + PSEPK OpenScientist research.
- [ ] Review every GOA row and remove all PENDING actions.
- [ ] Reconcile provider output with UniProt, GOA, primary evidence, and module logic.
- [ ] Validate and render all changed artifacts.
- [ ] Shepherd one PR through review and merge readiness.

## Selected Genes

| Gene | Locus | UniProt | Module role | Initial state |
|---|---|---|---|---|
| `ftsW` | PP_1336 | Q88N77 | septal SEDS glycan polymerase | fetched; research running |
| `ftsI` | PP_1331 | Q88N82 | septal bPBP D,D-transpeptidase | curated; research complete |
| `mrdB` | PP_4806 | Q88DL9 | lateral-wall SEDS glycan polymerase | curated; research complete |
| `mrdA-I` | PP_3741 | Q88GI2 | PBP2/MrdA paralog | curated; research complete |
| `mrdA-II` | PP_4807 | Q88DL8 | PBP2/MrdA paralog | fetched; research running |
| `mrcA` | PP_5084 | Q88CU6 | class-A PBP1A | existing COMPLETE review; research running |
| `mrcB` | PP_4683 | Q88DY5 | class-A PBP1B | fetched; research running |
| `pbpC` | PP_0572 | Q88QC2 | accessory PBP1C glycan polymerase | curated; research complete |
| `mtgA` | PP_5107 | Q88CS3 | monofunctional glycan polymerase | curated; research complete |
| `dacA` | PP_4803 | Q88DM2 | D,D-carboxypeptidase stem trimming | fetched; research running |

## Boundary Decisions

- The module begins after MurJ-mediated lipid II export; precursor synthesis and
  flipping remain in the existing precursor module.
- FtsW-FtsI and RodA-MrdA are separate septal and lateral-wall systems, each
  modeled with polymerase and crosslinking roles.
- MrdA-I and MrdA-II are alternatives pending evidence for condition-specific
  specialization; they are not modeled as sequential steps.
- MrcA, MrcB, and PbpC are class-A PBP variants, not mandatory sequential parts.
- MtgA supplies a distinct monofunctional polymerization role.
- DacA-mediated pentapeptide trimming is downstream maturation, not generic
  proteolysis.
- PBP4/DacB endopeptidation and YkuD-family L,D-transpeptidation are adjacent
  crosslink-remodeling systems. They will be curated as a separate reusable
  module rather than appended as isolated steps here.

## Initial Annotation Risks

- FtsW and MrdB carry TreeGrafter lipid-II-transporter transfers alongside the
  better-supported SEDS glycosyltransferase role.
- FtsI and both MrdA paralogs inherit glycosyltransferase, L,D-transpeptidase,
  carboxypeptidase, and proteolysis terms that do not all describe bPBP
  D,D-transpeptidation.
- Class-A PBPs are bifunctional, but current GO vocabulary represents their
  transpeptidase chemistry through a carboxypeptidase-labeled term; the module
  does not silently equate those activities.
