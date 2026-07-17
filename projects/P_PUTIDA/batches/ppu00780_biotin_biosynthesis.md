---
title: "PSEPK ppu00780 de novo biotin biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00780: de novo biotin biosynthesis

- Reusable module: `modules/biotin_biosynthesis.yaml`
- KEGG ppu00780 candidates inspected: 16
- Pathway-specific core reviewed: 6 proteins covering 6 dedicated reactions
- Shared fatty-acid-synthase dependency: explicit but not assigned as biotin-specific membership
- Excluded utilization, regulation, shared-machinery, or map-spillover candidates: 10
- Gene-level provider: OpenScientist
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a multi-step, species-neutral module boundary.
- [x] Separate de novo synthesis from biotin attachment and BirA regulation.
- [x] Fetch the six pathway-specific PSEPK genes.
- [x] Review every GOA annotation for the selected genes.
- [ ] Complete OpenScientist module and gene reports.
- [x] Complete initial module and gene validation.
- [ ] Render module, gene, and project pages after research integration.
- [ ] Open one draft PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK gene | UniProt | Decision |
|---|---|---|---|---|
| 1 | Malonyl-ACP carboxyl methylation | `bioC` | Q88QW9 | Covered |
| dependency | Two fatty-acid-synthase elongation cycles | shared FAS machinery | multiple | Required handoff; no Fab paralog is labeled as a biotin-specific module member |
| 2 | Pimeloyl-ACP methyl ester hydrolysis | `bioH` | Q88QX0 | Covered; new biotin-process annotation proposed |
| 3 | 8-amino-7-oxononanoate formation | `bioF` | Q88QX1 | Covered |
| 4 | 7,8-diaminononanoate formation | `bioA` | Q88D44 | Covered |
| 5 | Dethiobiotin formation | `bioD` | Q88QW8 | Covered |
| 6 | Radical-SAM sulfur insertion to form biotin | `bioB` | Q88QX2 | Covered; missing 4Fe-4S binding annotation proposed |

The BioC-BioH route and all four ring-assembly reactions are present in KT2440.
The module is satisfiable at the level of pathway-specific enzymes. The exact
fatty-acid-synthase paralogs that carry the masked pimelate intermediate remain
an organism-specific knowledge gap rather than a reason to assign every
ppu00780 Fab candidate to this module.

## Excluded Candidates

| Gene | Reason outside the dedicated biosynthesis-member boundary |
|---|---|
| `birA` | Biotin-protein ligase and transcriptional repressor; belongs to biotin utilization/regulation and the broader biotin cycle |
| `fabZ`, `fabG`, `fabF`, `fabB`, `PP_0581`, `PP_1852`, `PP_3303` | Generic fatty-acid-synthesis activities that may provide the shared elongation handoff but are not biotin-specific members on current evidence |
| `PP_2540` | Broad SDR oxidoreductase without a BioC-BioH-specific assignment |
| `PP_2783` | Aromatic-compound dihydrodiol dehydrogenase; KEGG map spillover rather than biotin synthesis |

## Module Decisions

- The module contains six substantive pathway-specific reaction parts; it is
  not a one-enzyme wrapper.
- Shared fatty-acid elongation is recorded on the BioC-to-BioH connection as an
  external dependency, avoiding unsupported paralog selection.
- Molecular functions occur only on leaf annotons, and every leaf has an exact
  PSEPK UniProt exemplar.
- BirA-dependent biotin attachment and operon regulation remain in the broader
  biotin-cycle scope rather than de novo synthesis.
- No cytoplasm/cytosol pair is asserted at module level. In the BioD gene
  review, cytoplasm is retained as non-core and the duplicate cytosol term is
  marked over-annotated.
- GO:0102130 is accepted for BioC because its definition and Rhea grounding
  specify malonyl-ACP, while its current label misleadingly says malonyl-CoA.

## Validation

Initial LinkML, module-validator, and six gene-review validations pass. Final
validation will be rerun after OpenScientist evidence integration.
