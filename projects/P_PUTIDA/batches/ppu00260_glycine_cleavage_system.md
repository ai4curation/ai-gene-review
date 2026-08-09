---
title: "PSEPK ppu00260 glycine cleavage system batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00260: glycine cleavage system

- Reusable module: `modules/glycine_cleavage_system.yaml`
- Correct pathway boundary: four-component P/H/T/L glycine cleavage system
- Broad ppu00260 candidates inspected: 66
- Newly reviewed PSEPK proteins: 6
- Reused shared-E3 review: 1
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Remove the human disease-specific framing and mitochondrial restriction.
- [x] Replace the one-part complex node with four substantive mechanistic roles.
- [x] Fetch and review both KT2440 P/H/T paralog sets.
- [x] Represent the L-protein step as covered but locus-ambiguous.
- [x] Ground P and T functions with exact Rhea reactions and available PAINT nodes.
- [x] Integrate the OpenScientist report with local UniProt, GOA, and PANTHER data.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | P-protein decarboxylation/loading | `gcvP1`; `gcvP2` | Q88P65; Q88CI9 | Covered by two EC 1.4.4.2 paralogs with Rhea 24304 |
| 2 | H-protein lipoyl carrier | `gcvH1`; `gcvH2` | Q88P64; Q88CI8 | Covered by two HAMAP-supported GcvH carriers |
| 3 | T-protein one-carbon transfer | `gcvT-I`; `gcvT` | Q88P67; Q88CI7 | Covered by two EC 2.1.2.10 paralogs with Rhea 16945 |
| 4 | L-protein carrier reoxidation | provisional exemplar `lpdG`; alternatives `lpd`, `lpdV` | Q88FB1; Q88C17; Q88EP9 | Reaction covered; physiological locus unresolved and candidates unranked |

The module is completely satisfiable at the reaction-role level. KT2440 has two
complete P/H/T sets, but no dedicated `gcv`-linked L protein. The available
evidence supports a shared dihydrolipoyl dehydrogenase but does not distinguish
LpdG, Lpd, and LpdV physiologically. LpdG is used only as a provisional exemplar,
without a GCS-specific process annotation.

## Annotation Decisions

- Exact P-protein glycine dehydrogenase and T-protein aminomethyltransferase
  functions are accepted for both paralog sets.
- The missing H-protein lipoic acid binding term is added from the reviewed
  HAMAP-backed UniProt records.
- H-protein `protein lipoylation` is left undecided because GcvH is certainly
  modified and may also be an obligatory lipoyl-relay intermediate, but the
  KT2440 transfer topology has not been established.
- Broad glycine-metabolism and substrate-binding terms are retained as non-core
  or marked over-annotated where exact catalytic/process terms are available.
- Redundant cytoplasm/cytosol annotations are not repeated in core summaries.
- LpdG remains a shared dihydrolipoyl dehydrogenase; GCS-specific locus usage is
  explicitly left unresolved.
- The UniProt aminotransferase keyword on GcvT-I and its derived GO:0008483 call
  are flagged for correction because the exact reaction is aminomethyl transfer,
  not transamination.

## Boundary Decisions

- LipA/LipB-mediated H-protein lipoylation is an activation dependency, not a
  fifth core GCS part.
- Choline/betaine, dimethylglycine, and sarcosine catabolism are upstream
  glycine-supply pathways.
- GlyA-mediated serine/glycine interconversion and downstream folate chemistry
  are neighboring one-carbon modules.
- Nonketotic hyperglycinemia is a human clinical consequence, not the identity
  or taxonomic scope of the reusable biochemical module.

## Grounding

Every core role has multiple UniProt exemplars. PTHR11773 and PTHR43757 are
additionally grounded by local PAINT nodes PTN000206531 and PTN000354058,
respectively. The H role uses the exact GcvH family and reviewed target records;
no unsupported H-protein PTN is asserted. The broad L-protein family is
constrained by required GO:0004148 activity and exact target exemplars.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. The report supplied species-aware retrieval
and boundary analysis; local UniProt, GOA, Rhea, PANTHER, and PAINT records ground
the curated assertions. P. aeruginosa genetics provides comparative support for
two GCS sets and a regulated gcs2 operon (PMID:27303730; PMID:23457254), but is
not treated as direct evidence for KT2440 paralog specialization.

## Validation

All seven touched gene reviews passed schema, GOA, reference, best-practice,
and ontology-term validation. The module passed LinkML and semantic validation
with zero warnings. Gene, module, and project renderers completed successfully.
