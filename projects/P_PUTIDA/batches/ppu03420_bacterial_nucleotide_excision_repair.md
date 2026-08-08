---
title: "PSEPK ppu03420 bacterial nucleotide-excision repair batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03420: bacterial nucleotide-excision repair

- Reusable module: `modules/bacterial_nucleotide_excision_repair.yaml`
- Correct pathway boundary: UvrABC lesion excision, repair synthesis, and Mfd-dependent transcription coupling
- KEGG-derived candidates inspected: 10
- Newly reviewed PSEPK proteins: 5
- Reused curated reviews: 5
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate bacterial UvrABC repair from eukaryotic XPD/TFIIH repair.
- [x] Distinguish the canonical UvrA protein from the divergent PP_3087 UvrA-family paralog.
- [x] Exclude PP_2839, a DinG/YoaA-like helicase, from core NER satisfiability.
- [x] Distinguish required LigA activity from secondary LigB.
- [x] Represent global-genome and Mfd-dependent transcription-coupled entry routes.
- [x] Add reviewed UniProt exemplars and a directly relevant PAINT ancestral node.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Transcription-coupled lesion recognition | `mfd` | Q88KZ1 | Covered; optional entry branch |
| 2 | Global-genome damage recognition | `uvrA` | Q88QK7 | Covered |
| 3 | Lesion verification and preincision complex | `uvrB` | Q88LF9 | Covered |
| 4 | Dual incision | `uvrC` | Q88FJ7 | Covered |
| 5 | Excised-oligonucleotide release | `uvrD` | Q88C31 | Covered; shared with other repair pathways |
| 6 | Repair-gap filling | `polA` | Q88RK6 | Covered; shared activity |
| 7 | Repair-nick sealing | `ligA` | Q88F25 | Covered; shared activity |

The canonical seven-role pathway is complete in KT2440. Mfd is required only
for the transcription-coupled branch, while global-genome NER enters through UvrA.

## Candidate Decisions

- PP_2839 is retained as a predicted DinG/YoaA-like DNA helicase but not as the
  eukaryotic XPD/ERCC2 step suggested by the combined KEGG map.
- PP_3087 belongs to a different UvrA PANTHER subfamily from canonical UvrA and
  remains an accessory UvrA2-family candidate with unresolved pathway specificity.
- LigB has NAD-dependent ligase activity but is not required for NER; LigA is the
  canonical essential nick-sealing enzyme.
- UvrD is genuinely shared among NER, mismatch repair, replication-associated
  repair, and recombination control; its NER role does not imply pathway exclusivity.

## Boundary Decisions

- Base-excision repair, mismatch repair, homologous recombination, SOS signaling,
  and translesion synthesis remain separate modules.
- Eukaryotic XPD/ERCC2 and TFIIH are not expected bacterial NER components.
- Cho-family alternative incision activity is optional and its absence is not a gap.
- Molecular functions are attached to the seven leaf annotons, not the module node.
- Cytoplasmic and cytosolic locations are omitted from the module because they do
  not distinguish the pathway or its individual roles.

## Grounding

Every leaf is grounded by a concrete KT2440 UniProt protein and a reviewed E. coli
exemplar. The UvrD leaf also carries the locally verified PAINT node
PTN000116141 for 3-prime-to-5-prime DNA helicase activity. Broad or misleading
PANTHER subfamily names are not used to infer pathway membership without the
required molecular function and exemplar context.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Local UniProt, GOA, PANTHER, and Rhea records
were used to check exact accessions and distinguish the three non-core candidates.

## Validation

The five new gene reviews, reusable module, and project page are validated and
rendered before publication.
