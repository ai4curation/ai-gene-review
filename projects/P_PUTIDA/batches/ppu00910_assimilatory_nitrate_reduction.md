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
- [x] Merge PR #2577 after review and CI (2026-08-28).

## Selected Genes

| Done | Gene | Locus | UniProt | Role | Research |
|---|---|---|---|---|---|
| [x] | `nasA` | PP_2092 | Q88L43 | nitrate/nitrite porter; required for extracellular-nitrate realization | Falcon complete |
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

## Wave 118 Repair Audit (2026-09-01)

Repair PR: [#2903](https://github.com/ai4curation/ai-gene-review/pull/2903).

The repaired reusable boundary preserves the ordered nitrate import -> nitrate
reduction -> NirBD nitrite reduction sequence while distinguishing pathway core
from whole-cell input context. Nitrate import is optional at the module boundary:
it is required when a realization starts from extracellular nitrate, but the two
reductive steps can be instantiated from an intracellular-nitrate input. GS-GOGAT
remains a separate downstream ammonia-assimilation module; respiratory nitrate
reduction, denitrification, and DNRA remain outside.

`scope: CONCRETE` is retained because this is a grounded, bacteria-scoped pathway
realization with representative proteins at every leaf, not a gene-free abstract
motif. Both transporter and nitrate-reductase variant sets retain `ONE_OR_MORE`
as relaxed modeling. Transport systems can coexist, but the model neither asserts
coexistence nor universal exclusivity of nitrate-reductase architectures.

Species-specific PP_1703 uncertainty has been removed from generic role and
module-note prose and remains documented in this PSEPK batch and gene review.
The ferredoxin-linked branch now uses reviewed bacterial NasA Q9L2E6 rather than
P39458, whose current UniProt catalytic reaction is quinol-linked. Exact PANTHER
subfamilies were added for NrtABCD components and NasC only where official labels
and member containment match the role. PTN009073875 grounds nitrate transport and
PTN008082957 grounds the NirD complex contribution; misleading or unresolved
molybdopterin-reductase family/PTN identifiers remain omitted.

The mandatory annotation-reviewer pass covered all GOA rows for nasA, PP_1703,
nirB, and nirD. It found one required source-fidelity repair: all nine nasA rows
were missing their GOA qualifiers, which are now restored. PP_1703, nirB, and
nirD required no action changes; the nirB iron-sulfur replacement rationale now
quotes both the 2Fe-2S and 4Fe-4S assignments.

Fresh PSEPK module/pathway OpenScientist research completed with the configured
7200-second job allowance in 1660.53 seconds. It recovered NasA, PP_1703, and
NirBD as a complete three-step whole-cell realization and kept GS-GOGAT plus
respiratory, denitrification, and DNRA machinery outside. Its claims that
PP_1703 is directly functional and cytoplasmic exceed the cited target-strain
evidence; wave 118 therefore retains the existing candidate wording and does
not add a localization annotation.

The separate generic module OpenScientist job was allowed to run uninterrupted
for the full configured 7200 seconds, then exited at the client timeout without
materializing a report. No generic research artifact or unsupported evidence
claim was added from that unsuccessful run.
