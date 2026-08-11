---
title: "PSEPK ppu00650 ketone-body uptake and oxidation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [bhbP, hbdH, aacs]
autolink_gene_symbols: false
---

# PSEPK ketone-body uptake and oxidation

This batch extracts the D-3-hydroxybutyrate branch from the broad KEGG
`ppu00650` butanoate-metabolism map. The reusable module is
`ketone_body_oxidation`; the selected KT2440 locus contains `bhbP` (PP_3074),
`hbdH` (PP_3073), and `aacs` (PP_3071).

## Status

- [x] Define a multi-part, species-neutral module boundary.
- [x] Fetch `bhbP`, `hbdH`, and `aacs` from UniProt/GOA.
- [x] Curate the three selected gene reviews.
- [x] Validate the initial gene reviews and module YAML.
- [ ] Complete OpenScientist research for all selected genes (active; not a publication gate).
- [ ] Complete generic module and PSEPK pathway/taxon OpenScientist research (active; not a publication gate).
- [x] Complete an independent annotation-reviewer audit.
- [x] Render gene, module, and project pages.
- [x] Prepare one dedicated draft PR for this module.

## Module Boundary

The pathway contains four substantive roles: optional D-3-hydroxybutyrate
import, oxidation to acetoacetate, acetoacetate activation, and thiolytic
cleavage to acetyl-CoA. Acetoacetate activation is modeled as a variant point:
animal ketolysis commonly uses SCOT, whereas KT2440 supplies an ATP-dependent
Aacs route.

The prior module was mammal-specific and treated mitochondrial localization and
tissue expression as universal. This revision retains the conserved reaction
chain, moves those taxon-specific details out of the core, and adds exact PSEPK
candidate exemplars at the first three roles. `scope: CONCRETE` describes this
defined chemical topology; FAMILY selectors keep its bacterial and eukaryotic
realizations reusable. GO's "ketone body" process label is used for the
D-3-hydroxybutyrate/acetoacetate chemistry, not to import hepatic physiology
into the bacterial model.

## Satisfiability

| Role | KT2440 candidate | Status | Curation note |
|---|---|---|---|
| D-3-hydroxybutyrate import | `bhbP` / PP_3074 / Q88IC5 | covered | Replace incorrect family-derived gluconate annotations with broader monocarboxylate transport terms. |
| D-3-hydroxybutyrate oxidation | `hbdH` / PP_3073 / Q88IC6 | covered | EC 1.1.1.30 and IPR011294 support the specific dehydrogenase activity. |
| ATP-dependent acetoacetate activation | `aacs` / PP_3071 / Q88IC8 | covered | EC 6.2.1.16 and PTHR42921:SF1 support acetoacetate-CoA ligase activity. |
| Acetoacetyl-CoA thiolysis | multiple thiolase paralogs | candidate uncertain | BktB/Q88GH0 is reaction-capable, but the physiologically dominant enzyme during growth on D-3-hydroxybutyrate is unresolved. |

The 38-row companion TSV is retained as the complete `ppu00650` overlap table.
`bhbP` is adjacent and deliberately off-map, so it is reviewed for the optional
uptake boundary but is not appended to the immutable 38-row KEGG overlap table.
Most entries belong to neighboring 4-hydroxybutyrate, branched-chain amino-acid,
fatty-acid, PHA, or central-carbon modules and are not part of this focused
batch.

## Notes

### 2026-08-11

Initial curation completed from UniProt, GOA, InterPro, PANTHER, and local KEGG
membership. OpenScientist jobs continue at their full configured runtime but
are not a publication gate; completed literature checks were reconciled
independently for this review response.

Independent annotation-reviewer re-audit covered every GOA row for `bhbP`,
`hbdH`, and `aacs`. It retained broad MF treatment for BhbP, replaced the
gluconate BP with carboxylic acid transmembrane transport, removed unsupported
synthetic ketone-body annotations, and marked the broad Aacs lipid-metabolism
IEA as over-annotated. The molecular-function conclusions are predictions from
unreviewed records, family assignments, and homolog evidence, not direct assays
of the exact KT2440 proteins.

Intracellular storage-polymer-derived D-3-hydroxybutyrate can bypass uptake in
some bacteria, but *Pseudomonas* generally does not produce PHB and KT2440 is
primarily associated with medium-chain-length PHA. The substrate source,
relative HbdH/Aacs contribution, and terminal thiolase remain open rather than
being forced into a single KT2440 route.
