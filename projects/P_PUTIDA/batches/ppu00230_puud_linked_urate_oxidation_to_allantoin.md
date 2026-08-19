---
title: "PSEPK PuuD-linked urate oxidation to allantoin"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK PuuD-linked urate oxidation to allantoin

This batch models the PuuD-linked three-reaction conversion of urate to
(S)-allantoin: membrane cytochrome c-dependent urate oxidation, hydrolysis of
5-hydroxyisourate, and decarboxylation of OHCU. Upstream xanthine oxidation and
downstream allantoin degradation are adjacent but separate pathway modules.

## Workflow

- [x] Fetch the four gene records needed to establish the module and boundary correction.
- [ ] Complete full OpenScientist research for all four selected/boundary genes.
- [ ] Integrate the completed gene reports after checking claims against primary evidence.
- [x] Curate all current GOA rows and the missing pathway/process annotations.
- [x] Create and validate the species-neutral `puud_linked_urate_oxidation_to_allantoin` module.
- [x] Complete full OpenScientist module research.
- [x] Run full OpenScientist module + `ppu00230` + PSEPK research.
- [ ] Render the module, gene reviews, and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `PP_4289` | PP_4289 | Q88F11 | COG3748 PuuD candidate; membrane urate-oxidation entry step |
| [ ] | `pucM` | PP_4285 | Q88F14 | 5-hydroxyisourate hydrolase |
| [ ] | `pucL` | PP_4287 | Q88F12 | OHCU decarboxylase |

## Boundary Correction

`puuD`/PP_3099 (Q88IA0) is reviewed in this batch because its legacy name and
EC-derived GO:0004846 annotation created a false route assignment. Its
IPR010269/IPR044031/IPR044032, PF05943/PF18945, and PTHR35565:SF3
classifications identify a TssC1/VipB type VI secretion sheath protein. It is
not a member of the urate module; its urate-oxidase annotation is removed and
its T6SS role is curated instead.

The canonical PP_3099 gene review is already owned by the approved type VI
secretion apparatus PR
[#2515](https://github.com/ai4curation/ai-gene-review/pull/2515). This urate PR
does not add a competing copy of that review. It retains the independently
generated OpenScientist boundary report because that report was commissioned
for this pathway decision and independently rejects the uricase assignment.

## Research Adjudication

The first species/pathway OpenScientist run was launched before the curated
module YAML existed. It correctly recovered `pucM` and `pucL`, but declared the
entry step a pathway hole after searching only soluble Uox and HpxO families.
That conclusion is superseded: the report's own locus table includes Q88F11 as
a cytochrome c domain protein, but it did not inspect Q88F11's COG3748,
IPR010389/PF06181, eight-transmembrane-helix, and cytochrome c architecture.
PMID:26349049 identifies precisely that architecture as PuuD and directly tests
the A. fabrum A9CI11/Atu2314 exemplar.

The generated report remains unchanged at
`../deep-research/PSEPK__bacterial-urate-oxidation-to-allantoin__ppu00230-deep-research-openscientist.md`.
The second module-level run uses the curated PuuD-linked boundary and is tracked
separately at
`../../../modules/puud_linked_urate_oxidation_to_allantoin-deep-research-openscientist.md`.

The Q88F11 gene-level report found the correct PuuD family but over-specified
the unresolved electron acceptor as O2 and asserted direct respiratory-chain
coupling. Those claims were not imported. GO:0004846 and RHEA:21368 explicitly
produce hydrogen peroxide, whereas the PuuD study distinguishes the
cytochrome-mediated route from that soluble-Uox chemistry. The review therefore
uses GO:0009055 for the supported electron-transfer component, adds
GO:0019628 for pathway participation, and proposes a mechanism-appropriate GO
MF rather than applying GO:0004846 as a false exact match.

The completed reusable-module report supports the three-reaction boundary and
explicitly says that PuuD's physiological electron acceptor is unresolved. It
also repeatedly writes the first step as `urate + O2 -> HIU`, including in its
summary table and diagram. That internally inconsistent oxygen assignment was
not imported. The module records the acceptor and balanced stoichiometry as a
knowledge gap and deliberately omits GO:0004846/RHEA:21368.

## Adjacent But Separate

- `xdhA`/`xdhB` and `guaD` supply urate upstream and belong to an upstream
  purine-ring oxidation module.
- `puuE`/PP_4286 and `allA`/PP_4288 consume allantoin-derived intermediates and
  belong to downstream allantoin degradation.
- `uacT`/PP_4290 is a substrate-supply transporter, not one of the three
  urate-to-allantoin reactions.
- `paoABC` is an aldehyde oxidoreductase system and does not fill the PuuD step.

The 65-gene KEGG source snapshot is retained in
`ppu00230_puud_linked_urate_oxidation_to_allantoin.tsv`. Q88F11 is absent from
that KEGG membership export and was added to the curated module from exact
domain, neighborhood, and primary-literature evidence.
