---
title: "PSEPK assimilatory nitrate uptake and reduction batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [nasA, PP_1703, nirB, nirD]
autolink_gene_symbols: false
---

# PSEPK ppu00910: assimilatory nitrate uptake and reduction

- Module seed: `bacterial_assimilatory_nitrate_reduction`
- Selected genes: 4
- Existing curated review reused: `nasA`
- New gene reviews: `PP_1703`, `nirB`, `nirD`

## Curated Boundary

- The module begins with nitrate import by NasA/Q88L43.
- PP_1703/Q88M71 is the candidate fused NAD(P)H-linked assimilatory nitrate
  reductase. Its imported NapA-like periplasmic and sulfite-reductase calls are
  not treated as established.
- NirB/Q88M69 and NirD/Q88M68 form the two-subunit assimilatory nitrite
  reductase that produces ammonium.
- GS-GOGAT ammonium incorporation, respiratory nitrate reduction,
  denitrification, and DNRA are separate modules.

## Required Workflow

- [x] Curate the species-neutral multi-part module.
- [x] Fetch selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Complete OpenScientist research jobs for each newly fetched gene.
- [x] Complete module-level OpenScientist research job.
- [x] Complete module + pathway + PSEPK OpenScientist research job.
- [x] Curate all selected gene reviews and every imported GOA row.
- [x] Consult the annotation reviewer and module curator.
- [x] Validate and render module, project, and gene reviews.
- [x] Open draft PR [#2577](https://github.com/ai4curation/ai-gene-review/pull/2577) for this module.

## Selected Genes

| Done | Gene | Locus | UniProt | Role | Research |
|---|---|---|---|---|---|
| [x] | `nasA` | PP_2092 | Q88L43 | nitrate/nitrite porter; nitrate import is core | Falcon complete |
| [x] | `PP_1703` | PP_1703 | Q88M71 | candidate fused assimilatory nitrate reductase | OpenScientist report complete |
| [x] | `nirB` | PP_1705 | Q88M69 | nitrite reductase catalytic large subunit | job complete; no report materialized |
| [x] | `nirD` | PP_1706 | Q88M68 | nitrite reductase Rieske-fold small subunit | job complete; no report materialized |

## Notes

2026-08-13: Defined a focused three-step module rather than editing the full
nitrogen-cycle overview. PP_1703 has a fused nitrate-reductase and
pyridine-nucleotide reductase architecture, but its current electronic
annotations conflict; direct biochemical evidence remains a priority.

2026-08-13: Integrated the completed PP_1703 OpenScientist report with direct
KT2440 pathway evidence (PMID:32523942), same-lineage `nasB` genetics
(PMID:10852866), and comparative fused diflavin-NAS biochemistry
(PMID:32111737). The `nirB`, `nirD`, generic-module, and
module+pathway+taxon jobs completed without materializing reports; no provider
coverage is invented for them.

2026-08-13: Verified every module UniProt accession against UniProtKB. Verified
PTHR43809:SF1 and PTHR40562:SF1 against the exact PSEPK records and reviewed
E. coli exemplars. The only selected-gene PTN, PTN000177398, occurs in the
rejected PP_1703 membrane IEA and is deliberately not used as module grounding.
The final module is species-neutral: concrete proteins are exemplars of reusable
families or architectural variants rather than species-locked selectors.
