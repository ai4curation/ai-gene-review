---
title: "PSEPK ppu00670 folate one-carbon interconversion batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [folD1, folD2, metF, PP_4638, fau]
autolink_gene_symbols: false
---

# PSEPK ppu00670: folate one-carbon interconversion

- Module seed: `folate_one_carbon_interconversion`
- KEGG candidate genes from membership table: 31
- Selected focused genes reviewed here: 5
- Curated review files in this batch: 5
- Module/pathway OpenScientist reports: 1 of 2 complete
- Gene-level OpenScientist reports currently present: 0 of 5

## Required Workflow

- [x] Curate the species-neutral multi-operation module.
- [ ] Complete module-level OpenScientist deep research.
- [x] Complete module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Complete OpenScientist deep research for all selected genes.
- [x] Curate every GOA row with no `PENDING` actions.
- [x] Validate the current module and gene reviews.
- [ ] Render the touched module, genes, and project page.
- [ ] Open one non-draft PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Focused Candidates

| Done | Gene | Locus | UniProt | Primary bucket | Curation | OpenScientist research | Module interpretation | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `folD1` | PP_1945 | Q88LI7 | kegg:ppu00670 | CURATED | RUNNING | covered: NADP FolD dehydrogenase and cyclohydrolase | Bifunctional protein FolD 1 |
| [x] | `folD2` | PP_2265 | Q88KM5 | kegg:ppu00670 | CURATED | RUNNING | covered: NADP FolD dehydrogenase and cyclohydrolase | Bifunctional protein FolD 2 |
| [x] | `metF` | PP_4977 | Q88D51 | kegg:ppu00670 | CURATED | RUNNING | covered: compact NADH-linked MetF | Methylenetetrahydrofolate reductase |
| [x] | `PP_4638` | PP_4638 | Q88E30 | kegg:ppu00670 | CURATED | RUNNING | candidate_uncertain: MTHFR-like fold, reaction not supported | MTHFR-like FAD-linked oxidoreductase |
| [x] | `fau` | PP_5203 | Q88CH8 | kegg:ppu04981 | CURATED | RUNNING | covered: 5-formyl-THF salvage | 5-formyltetrahydrofolate cyclo-ligase |

## Boundary

This batch covers only interconversion among 5,10-methylene-THF,
5,10-methenyl-THF, 10-formyl-THF, 5-methyl-THF, and salvaged
5-formyl-THF. The reusable module has four substantive operations. The
FolD/MTHFD redox and methenyl/formyl hydrolysis operations are the required
coupled core; MTHFR reduction and ATP-dependent 5-formyl-THF salvage are
independently optional branches. Alternative implementations are defined by
verified cofactor use and enzyme architecture rather than kingdom. They include
fused FolD/MTHFD enzymes and the experimentally supported monofunctional MtdA
plus FchA implementation. The MTHFR alternatives separately represent compact
NADH-linked MetF, plant regulatory-architecture NADH MTHFR, and regulatory
NADPH MTHFR rather than treating taxon as a cofactor selector.

The completed
[module/pathway/taxon report](../deep-research/PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist.md)
supports all four operations in KT2440 through folD1/folD2, metF, and fau.
It independently flags PP_4638 as uncertain. The report is useful for pathway
partitioning and family-level transfer, but it did not retrieve the strongest
PP_4638 evidence: the primary KT2440 fitness comparison in PMID:33534785. Its
claim that all four operations are jointly required and its bacterial/eukaryotic
cofactor shorthand are not adopted in the final module; route logic and variant
labels were corrected independently.

## Gene Decisions

- `folD1` and `folD2`: accept both specific FolD molecular functions and
  tetrahydrofolate interconversion. Do not infer paralog-specific division of
  labor; correct broad catalytic/oxidoreductase parents are retained as
  non-core, as is FolD2's redundant cytoplasm parent.
- `metF`: accept GO:0106312 and FAD binding, retain carrier-state
  interconversion, retain broad GO:0004489 as non-core, and narrow the broad
  L-methionine metabolism row to live GO:0071265 (L-methionine biosynthetic
  process).
- `PP_4638`: accept only the FAD-binding MTHFR-like fold and probable soluble
  location. Remove the NADH-specific reaction; leave broad MTHFR activity,
  methionine metabolism, and tetrahydrofolate interconversion undecided because
  the available conditions do not exclude every noncanonical role. PP_4638 is
  not a MetF reaction representative in the module.
- `fau`: accept 5-formyl-THF cyclo-ligase and carrier-state
  interconversion; retain broad folate-compound biosynthesis as non-core because
  formation of 5,10-methenyl-THF is within that process and PAINT supports it.

## Identifier And Family Audit

- Rhea reactions: 22812 (NADP FolD), 22892 (NAD MTHFD2), 23700
  (cyclohydrolase), 19821 (NADH MTHFR), 19817 (NADPH MTHFR), and 10488
  (5-formyl-THF cyclo-ligase).
- Reviewed P55818 MtdA experimentally supports a monofunctional NADP-linked
  RHEA:22812 implementation on THF as its secondary carrier substrate; reviewed
  Q49135 FchA provides the separate RHEA:23700 cyclohydrolase operation.
- Formal expansion yields 64 minimal routes. Every route contains exactly one
  dehydrogenase architecture and one cyclohydrolase architecture; eight routes
  contain only that two-operation core, and MTHFR/Fau absence and presence occur
  in all four independent combinations.
- Local `PTHR48099` entries place Q88LI7 and Q88KM5 in `SF5` and human
  MTHFD1 in `SF1`, despite the same generic PANTHER label. The local PAINT
  file supports GO:0004488/GO:0004477 at `PTN000002250` and GO:0004487 at
  `PTN002224686`.
- `PTHR45754:SF3` contains both E. coli NADH MetF P0AEZ1 and human MTHFR
  P42898, plus Arabidopsis, rice, and maize NADH-labeled proteins, despite its
  NADPH label. The module therefore uses architecture-specific InterPro terms
  and reaction/exemplar evidence to distinguish cofactor variants. Reviewed
  Arabidopsis MTHFR2 O80585 is an experimentally supported RHEA:19821 exemplar
  for the NADH-linked regulatory plant implementation.
- The local `PTHR23407` PAINT file supports GO:0030272 at
  `PTN000601268` and also has a positive non-negated GO:0009396 IBD row;
  E. coli YgfA P0AC28 is included as an experimental seed alongside KT2440 Fau.

## Exclusions

Upstream one-carbon loading by SHMT/glyA and glycine cleavage is outside this
module. De novo folate synthesis/regeneration (including folA and folM),
formate loading or release, and purU unloading are excluded. Purine,
thymidylate, and methionine consumers such as purN, purH, thyA, metH, and metE
are downstream. Broad KEGG ppu00670 members from choline/betaine metabolism,
redox recycling, and overview maps are not selected.

`PP_4594` is explicitly excluded and remains owned by open PR #2080. The
focused five-gene set does not overlap the other open Putida PRs checked when
this batch was started.

## Evidence Gaps

The four operations are grounded mainly in conserved family, EC/Rhea, domain,
and PAINT evidence; direct KT2440 biochemical measurements were not found. The
MtdA/FchA implementation is experimentally supported in M. extorquens AM1, not
KT2440. The physiological division between FolD1 and FolD2 is unknown.
For PP_4638, published fitness data argue against redundant canonical MetF
activity in the tested conditions but do not reveal its actual substrate,
redox partner, or direction.

Generated UTC: 2026-07-20T21:02:00Z
