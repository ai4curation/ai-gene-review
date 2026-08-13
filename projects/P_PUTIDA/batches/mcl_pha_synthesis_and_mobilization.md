---
title: "PSEPK medium-chain-length PHA synthesis and mobilization batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [phaG, phaA, phaC, phaZ]
autolink_gene_symbols: false
---

# PSEPK medium-chain-length PHA synthesis and mobilization

This batch integrates the previously single-step PhaG monomer-supply bridge
into a reusable multi-part module spanning monomer supply, PhaC polymerization,
and PhaZ-dependent intracellular mobilization.

## Workflow

- [x] Define a reusable module with more than one substantive part.
- [x] Add exact KT2440 accessions and reviewed cross-taxon exemplars.
- [x] Consume every materialized OpenScientist gene report.
- [x] Integrate the generic module and correct UPA00212 module + pathway + taxon reports.
- [x] Reconcile the module and gene reviews with all completed research outputs.
- [x] Consult the annotation reviewer and address findings.
- [x] Review all six imported GOA rows with no PENDING actions.
- [x] Validate and render all changed artifacts.
- [x] Open one focused draft PR: [#2585](https://github.com/ai4curation/ai-gene-review/pull/2585).

## Selected genes

| Done | Gene/folder | Locus | UniProt | Module role |
|---|---|---|---|---|
| [x] | `phaG` | PP_1408 | O85207 | Optional FAS-derived monomer routing |
| [x] | `phaA` (`phaC1`) | PP_5003 | Q88D25 | Class II PHA polymerase isoenzyme |
| [x] | `phaC` (`phaC2`) | PP_5005 | Q88D23 | Class II PHA polymerase isoenzyme |
| [x] | `phaZ` | PP_5004 | Q88D24 | Intracellular PHA depolymerase |

## Boundary decisions

- PhaG is optional because beta-oxidation-derived routes can also supply
  medium-chain-length (R)-3-hydroxyacyl-CoA.
- PhaC1 and PhaC2 are alternative or condition-dependent members of one
  polymerization step, not sequential pathway parts.
- Evidence from another P. putida strain supports stronger PhaC1 activity than
  PhaC2 under the tested overexpression condition, but this batch does not
  promote that result to a KT2440-specific "primary synthase" assertion.
- PhaF, PhaI, and PhaD are granule-organization or regulatory context and are
  not represented as reaction steps.
- The existing single-step UPA00212 batch remains provenance for the original
  PhaG review; this batch supplies the broader multi-part module it anticipated.

## Annotation decisions

- `phaA` and `phaC`: modify generic acyltransferase activity to GO:0016747 and
  replace the incorrect PHB-specific process with GO:0042621. Both are modeled
  as class II synthase exemplars; no primary/secondary or substrate-specialized
  division of labor is asserted. Granule localization is direct for PhaC1 and
  comparative for PhaC2.
- `phaG`: the GOA snapshot has no rows. New broad acyltransferase activity is
  supported only by the purified in-vitro reaction, while GO:0042621 captures
  the experimentally established pathway role. The review and module preserve
  the unresolved direct-transacylase versus thioesterase-plus-ligase chemistry.
- `phaZ`: replace TreeGrafter triacylglycerol-lipase and glycerolipid-catabolism
  annotations with the dedicated PHA depolymerase MF and PHA metabolic process;
  add experimentally supported PHA-granule localization.

## Research provenance

Materialized OpenScientist reports were integrated for `phaC`, `phaZ`, the
generic PhaG monomer-supply module, and the correct module+pathway+taxon query
`UPA00212` in PSEPK. The latter is
`projects/P_PUTIDA/deep-research/PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-openscientist.md`.
The unrelated `ppu00500` trehalose report was explicitly excluded. Late
duplicate jobs for `phaA`, `phaG`, the broader module, and the UPA00212 query
exited without materializing additional reports; no output was invented or
restarted. Existing Falcon reports and primary literature were also audited.

## Identifier audit and residual gaps

Current UniProt records were verified for O85207, Q88D25, Q88D23, Q88D24,
Q51553, Q9KJH8, P26494, P26496, P26495, and candidate ligase Q88PT5. GOA PTN
`PTN002251178` was verified as the source of PhaZ's broad TreeGrafter lipase and
glycerolipid annotations; it is not used as an ancestral node for the exact PHA
depolymerase function.

Residual uncertainties are the native PhaG reaction mechanism, whether PP_0763
or another ligase completes CoA activation under a two-step mechanism, and the
relative physiological contributions and substrate preferences of PhaC1 and
PhaC2 in KT2440.
