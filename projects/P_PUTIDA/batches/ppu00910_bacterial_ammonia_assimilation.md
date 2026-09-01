---
title: "PSEPK ppu00910 GS-GOGAT ammonia assimilation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00910: GS-GOGAT ammonia assimilation

- Module seed: `bacterial_ammonia_assimilation`
- Candidate genes from membership table: 20
- Primary bucket genes: 19
- Existing review files: 5
- Curated review files: 5
- Selected module genes: 3
- Selected gene reviews curated: 3
- Selected gene research: Asta retrieval-only (3/3); no relevant target-specific papers recovered

## Curated Boundary

- Required GS-GOGAT cycle: `glnA` (PP_5046), `gltB` (PP_5076), and `gltD` (PP_5075).
- `gdhA` is a distinct direct-amination alternative, not a required third step.
- Ammonium transport, Ntr/PII regulation, nitrate/nitrite reduction, carbonic
  anhydrases, and polyamine ligases are outside this module.
- Several broad-map "glutamine synthetase" rows are paralogous amide ligases;
  only `glnA` carries the canonical assimilatory GS assignment.

## Wave119 Repair

The reusable module remains a bacterial NADPH-dependent two-reaction GS-GOGAT
cycle. `scope: CONCRETE` is intentional because the module describes a
biologically realizable cycle grounded by extant proteins; it is not a gene-free
abstract motif. The `NCBITaxon:2` context deliberately restricts the model to the
bacterial GlnA-GltB/GltD implementation without making it PSEPK-specific.

The first leaf assigns GO:0004356 to the GlnA family. The second assigns
GO:0004355 to the complete GO:0009342 GltB/GltD complex, while the nested active
units carry their direct subunit functions: GltB enables GO:0004359 glutaminase
activity and GltD enables GO:0016651, while both contribute to the donor-general
GO:0015930 and the complete NADPH-dependent GO:0004355 reaction. The GOGAT
product list now records L-glutamate once
with stoichiometric coefficient two, avoiding duplicate entity entries. The
reverse cycle connection explicitly states that one glutamate replenishes the
GlnA substrate and the other is the net assimilatory product.

All family assignments and member containment were checked locally. GlnA uses
PTHR43407:SF2, GltB uses PTHR11938:SF148, and GltD uses PTHR42783:SF3 with its
exact official `SMALL CHAIN-RELATED` label retained and explained. Reviewed
E. coli K-12 exemplars P0A9C5, P09831, and P09832 were verified in UniProtKB and
all fall in the declared subfamilies. PTN000464923 is retained for GlnA
GO:0004356. PTN000234342 does support GO:0015930 in the broader GltB family, but
its seeds include fused proteins that independently perform the complete
reaction; it is not asserted for the standalone bacterial GltB subunit. No GltD
or holoenzyme PTN is asserted because the local PAINT data lack a suitably
specific IBD node.

The required annotation-reviewer consult examined every annotation and the
core-function synthesis for `glnA`, `gltB`, and `gltD`. The first pass confirmed
the complex-versus-subunit treatment and prompted removal of unsupported
target-specific wording, correction of the displayed GltB physiological
reaction direction, addition of `part_of GO:0009342` proposals for both
subunits, and documentation that the Asta reports returned no relevant
target-specific literature. A final-state pass identified and resolved the
remaining blocker by changing GO:0015930 from a direct GltB function to a
complex contribution; it also removed a redundant, mismatched GltD
electron-transfer proposal.

For PSEPK, Q88CY3, Q88CV4, and Q88CV5 satisfy the complete cycle by curated
family, reaction, domain, and gene-neighborhood evidence. Direct biochemical
characterization of these three KT2440 proteins was not located. Q88Q23 GdhA is
an alternative direct-amination route whose physiological assimilatory flux is
condition-dependent; it is not a third required part. Ammonium transport,
PII/GlnA regulation, nitrate and nitrite reduction, and downstream nitrogenous
biosynthesis remain outside this module.

## Required Workflow

### Wave119 Repair

- [x] Audit the two-reaction boundary, `CONCRETE` scope, cycle connections, and stoichiometry.
- [x] Verify reviewed cross-species UniProt exemplars and exact PANTHER member containment.
- [x] Verify PAINT IBD nodes and omit unsupported PTNs.
- [x] Complete the required annotation-reviewer consult for all three genes.
- [x] Reconcile complex-level and direct subunit GO molecular functions.

### Initial Pass

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research (full-duration attempt; no report produced).
- [x] Confirm all selected gene folders and source records are present.
- [x] Review the existing Asta deep-research reports for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [#2316](https://github.com/ai4curation/ai-gene-review/pull/2316).
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-07-26: OpenScientist timed out after 7200s for the module + pathway +
PSEPK report; no report file was produced.

2026-09-01: Wave119 retried the module + pathway + PSEPK OpenScientist request
with the required 7200-second allowance. The provider again timed out after the
full allowance and produced no report. The completed generic module report,
local source records, reviewed cross-species exemplars, and required
annotation-reviewer passes therefore ground this repair.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Gene research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `cynT` | PP_0100 | Q88RM9 | kegg:ppu00910 | MISSING | MISSING | MISSING | Carbonic anhydrase (EC 4.2.1.1) (Carbonate dehydratase) |
| [ ] | `PP_0430` | PP_0430 | Q88QQ8 | kegg:ppu00910 | MISSING | MISSING | MISSING | Uncharacterized protein |
| [ ] | `gdhA` | PP_0675 | Q88Q23 | kegg:ppu00910 | PRESENT | CURATED | MISSING | Glutamate dehydrogenase |
| [ ] | `arcC` | PP_0999 | Q88P54 | kegg:ppu00910 | MISSING | MISSING | MISSING | Carbamate kinase |
| [ ] | `nirB` | PP_1705 | Q88M69 | kegg:ppu00910 | MISSING | MISSING | MISSING | Nitrite reductase [NAD(P)H] large subunit (EC 1.7.1.4) |
| [ ] | `nirD` | PP_1706 | Q88M68 | kegg:ppu00910 | MISSING | MISSING | MISSING | Nitrite reductase |
| [ ] | `gdhB` | PP_2080 | Q88L55 | kegg:ppu00430 | MISSING | MISSING | MISSING | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) |
| [ ] | `nasA` | PP_2092 | Q88L43 | kegg:ppu00910 | PRESENT | CURATED | MISSING | Nitrate/nitrite transporter |
| [ ] | `puuA-I` | PP_2178 | Q88KW1 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [ ] | `PP_3148` | PP_3148 | Q88I53 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamine synthetase |
| [ ] | `PP_3392` | PP_3392 | Q88HG6 | kegg:ppu00910 | MISSING | MISSING | MISSING | Gamma carbonic anhydrase family protein |
| [ ] | `yrpB` | PP_3827 | Q88G98 | kegg:ppu00910 | MISSING | MISSING | MISSING | Nitronate monooxygenase (Propionate 3-nitronate monooxygenase) |
| [ ] | `PP_4399` | PP_4399 | Q88EQ4 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamine synthetase |
| [ ] | `PP_4547` | PP_4547 | Q88EB9 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamine synthetase |
| [x] | `glnA` | PP_5046 | Q88CY3 | kegg:ppu00910 | PRESENT | CURATED | PRESENT (Asta) | Glutamine synthetase (EC 6.3.1.2) |
| [x] | `gltD` | PP_5075 | Q88CV5 | kegg:ppu00910 | PRESENT | CURATED | PRESENT (Asta) | Glutamate synthase (NADPH) beta subunit (EC 1.4.1.13) |
| [x] | `gltB` | PP_5076 | Q88CV4 | kegg:ppu00910 | PRESENT | CURATED | PRESENT (Asta) | Glutamate synthase [NADPH] large chain (EC 1.4.1.13) (Glutamate synthase subunit alpha) |
| [ ] | `spuB` | PP_5183 | Q88CJ7 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamylpolyamine synthetase |
| [ ] | `spuI` | PP_5184 | Q88CJ6 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamylpolyamine synthetase |
| [ ] | `puuA-II` | PP_5299 | Q88C84 | kegg:ppu00910 | MISSING | MISSING | MISSING | Glutamate-putrescine ligase (EC 6.3.1.11) |

## Notes

The curated module is the two-reaction GS-GOGAT cycle, implemented by three
proteins because GltB and GltD form the glutamate-synthase complex. The broad
KEGG nitrogen-metabolism bucket is retained above only as a candidate
partition; unchecked rows are outside this module.

Generated UTC: 2026-07-27T00:45:33.874258+00:00
