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
- Audited PSEPK reviews: 9 (six P/H/T proteins and three E3 paralogs)
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Remove the human disease-specific framing and mitochondrial restriction.
- [x] Replace the one-part complex node with four substantive mechanistic roles.
- [x] Fetch and review both KT2440 P/H/T paralog sets.
- [x] Audit the initially locus-ambiguous L-protein step across all three E3 paralogs.
- [x] Ground P and T functions with exact Rhea reactions and available PAINT nodes.
- [x] Integrate the OpenScientist report with local UniProt, GOA, and PANTHER data.
- [x] Consult the annotation-reviewer and audit all three E3 paralogs.
- [x] Replace the three-way E3 ambiguity with the verified LPD-glc/LPD-val distinction.
- [x] Validate and render the module, genes, and project page.
- [x] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | P-protein decarboxylation/loading | `gcvP1`; `gcvP2` | Q88P65; Q88CI9 | Covered by two EC 1.4.4.2 paralogs with Rhea 24304 |
| 2 | H-protein lipoyl carrier | `gcvH1`; `gcvH2` | Q88P64; Q88CI8 | Covered by two HAMAP-supported GcvH carriers |
| 3 | T-protein one-carbon transfer | `gcvT-I`; `gcvT` | Q88P67; Q88CI7 | Covered by two EC 2.1.2.10 paralogs with Rhea 16945 |
| 4 | L-protein carrier reoxidation | `lpdG` | Q88FB1 | Covered by the KT2440 LPD-glc homolog; P. putida biochemistry supports LPD-glc rather than LPD-val, with a KT2440 strain-transfer caveat |

The module is completely satisfiable at the reaction-role level. KT2440 has two
complete P/H/T sets, but no dedicated `gcv`-linked L protein. PMID:1902462
identifies P. putida LPD-glc/lpdG as the L-factor for glycine oxidation, and
PMID:6546487 shows that the glycine oxidation system uses LPD-glc rather than
LPD-val. Q88FB1 is therefore the evidence-backed KT2440 implementation by
orthology and conserved `sucA-sucB-lpdG` context. Direct KT2440 GCS
reconstitution is still absent, so no GCS-specific GO process annotation is
added to LpdG. Q88EP9 is the `bkd`-linked LPD-val paralog; Q88C17 is LPD-3-like
and its physiological niche remains unresolved.

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
- Generic cytoplasm annotations are handled consistently as non-core across all
  three E3 reviews.
- LpdG's 2-oxoglutarate process annotation is accepted from conserved `lpdG`
  function and operon context; LpdV's corresponding TreeGrafter call is removed
  as a paralog transfer because LpdV is the branched-chain-complex E3.
- Lpd and LpdV retain exact GO:0004148 chemistry, while unsupported client-complex
  assignments are kept unresolved or rejected conservatively.
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

Every core role has concrete UniProt grounding. PTHR11773 and PTHR43757 are
additionally grounded by local PAINT nodes PTN000206531 and PTN000354058,
respectively. The H role uses the exact GcvH family; GO:0031405 remains on its
leaf annoton rather than acting as a module-level function. The L role uses the
exact PTHR22912 label with a required GO:0004148 function constraint because
valid E3 proteins span several subfamilies; Q88FB1 and human DLD are verified
members. No L-step PTN is asserted because ancestry of the PSEPK grafts to the
candidate taxon-unrestricted PAINT node was not established. The module includes
Q88FB1 as an exemplar while this batch records the KT2440 strain-transfer caveat.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. The report supplied species-aware retrieval
and boundary analysis; local UniProt, GOA, Rhea, PANTHER, and PAINT records ground
the curated assertions. Gene-level OpenScientist reports exposed the historical
LPD-glc/LPD-val literature that supersedes the module report's PE-level E3
ranking; PMID:1902462 and PMID:6546487 were fetched and verified before use. P.
aeruginosa genetics provides comparative support for two GCS sets and a regulated
gcs2 operon (PMID:27303730; PMID:23457254), but is not treated as direct evidence
for KT2440 paralog specialization. No new OpenScientist run was needed.

## Validation

All nine audited gene reviews passed schema, GOA, reference, best-practice,
and ontology-term validation. The module passed LinkML and semantic validation
with zero warnings. Gene, module, and project renderers completed successfully.
