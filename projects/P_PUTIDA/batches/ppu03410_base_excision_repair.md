---
title: "PSEPK ppu03410 base-excision repair batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03410: base-excision repair

- Reusable module: `modules/bacterial_base_excision_repair.yaml`
- Correct pathway boundary: lesion excision, AP-site processing, gap filling, and nick sealing
- KEGG-derived candidates inspected: 14
- Newly reviewed PSEPK proteins: 10
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate BER from nucleotide excision repair, mismatch repair, and homologous recombination.
- [x] Recover PP_1348/MutT, which was absent from the KEGG-derived candidate list.
- [x] Exclude PP_5292/Crc, an inactive ExoIII-fold translational regulator.
- [x] Model lesion-specific glycosylases as distinct reusable roles.
- [x] Review both KT2440 Xth-family paralogs without claiming equal AP-endonuclease confidence.
- [x] Add shared PolA and LigA downstream activities.
- [x] Add reviewed UniProt exemplars and exact Rhea reactions where available.
- [x] Split the glycosylase and class I AP-lyase functions of MutM and Nth into separate leaf annotons.
- [x] Ground the XthA transfer in reviewed E. coli XthA and primary comparative literature.
- [x] Validate and render the module, genes, and project page.
- [ ] Review PP_5292/Crc separately as a translational regulator; it is excluded from BER and is not silently recast here.
- [x] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Oxidized nucleotide sanitation | `PP_1348` | Q88N67 | Covered; exact MutT-family activity, symbol absent from UniProt |
| 2 | Uracil excision | `ung` | Q88N05 | Covered |
| 3 | Oxidized purine excision/AP lyase | `mutM` | Q88CQ5 | Covered |
| 4 | Adenine excision opposite 8-oxoG | `mutY` | Q88R48 | Covered; incorrect 8-oxoG-excision transfer removed |
| 5 | Oxidized pyrimidine excision/AP lyase | `nth` | Q88NW2 | Covered with GO:0000703 glycosylase and GO:0140078 AP-lyase leaves |
| 6 | Alkylated-base excision | `tag`; additional AlkA/Mpg candidates | Q88RR7 | Covered with redundant families |
| 7 | AP-site incision/end processing | `xthA`; `PP_2707` | Q88IV9; Q88JE2 | Covered by Xth family; xthA receives the exemplar-grounded AP-endonuclease transfer, while blocked-end chemistry remains a target-specific gap |
| 8 | Repair-gap filling | `polA` | Q88RK6 | Covered; shared with replication and other repair pathways; exact MF guards against the anomalous PTHR10133:SF27 label |
| 9 | Nick sealing | `ligA` | Q88F25 | Covered; LigB is not required for satisfiability |

The reusable BER relay is complete. KT2440 lacks an obvious Nfo/Endonuclease IV,
so the target-organism implementation is Xth-family dependent. This is a
lineage-specific satisfiability result rather than a universal module requirement.

## Annotation Decisions

- MutY's TreeGrafter `8-oxoG DNA N-glycosylase activity` is removed: MutY excises
  adenine opposite 8-oxoG, whereas MutM removes 8-oxoG itself.
- MutY's broad mismatch-repair assignment is marked over-annotated: it acts on
  a mismatched pair, but the lesion-specific glycosylase reaction is more
  precisely represented as BER.
- The precise glycosylase and polymerase/ligase activities are retained while
  generic catalytic, hydrolase, nuclease, and nucleotidyltransferase parents are
  marked over-annotated.
- Cytoplasmic/cytosolic locations are retained as non-core and are not repeated
  at module level.
- PP_2707 remains a candidate AP-site processor; only xthA receives the proposed
  AP-endonuclease activity in this first pass.
- Broad `DNA repair` annotations are retained uniformly as non-core when the
  biochemical activity or a more specific repair process is available.

## Boundary Decisions

- MutT is an upstream nucleotide-pool sanitation branch and is not connected as
  if it acted on a DNA repair intermediate.
- PolA and LigA are shared downstream enzymes, not BER-specific proteins.
- RecJ is ancillary to resection/long-patch contexts and is not required for the
  short-patch BER module.
- PP_5292/Crc is excluded despite its ExoIII-like fold because its established
  KT2440 role is Hfq-associated translational repression.
- NER, mismatch repair, homologous recombination, SOS signaling, and direct
  alkylation reversal remain separate modules.

## Grounding

Every leaf is grounded by a concrete KT2440 UniProt protein and a reviewed
E. coli exemplar from the matching PANTHER family or subfamily. Exact Rhea reactions are
included for MutT, class I AP-lyase chemistry, and DNA polymerase I. No PTN is
asserted because the fetched GOA exposes TreeGrafter nodes rather than a locally
verified PAINT IBD table. XthA additionally uses UniProtKB:P09030 as the ISS
exemplar and PMID:16524897/PMID:25748880 as primary comparative support.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Local UniProt, GOA, PANTHER, KEGG, and Rhea
records were used to correct the report's candidate list and qualify paralog claims.

## Validation

All ten gene reviews passed schema, GOA, reference, best-practice, and
ontology-term validation. The module passed LinkML and semantic validation with
zero warnings. Gene, module, and project renderers completed successfully.
