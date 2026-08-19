---
title: "PSEPK bacterial purine base oxidation to urate"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK bacterial purine base oxidation to urate

This batch models two convergent purine-base entry routes and the shared
terminal oxidation to urate. `guaD` converts guanine to xanthine. The
two-subunit `xdhA`/`xdhB` complex converts hypoxanthine to xanthine and then
xanthine to urate. Purine salvage and the downstream PuuD-linked conversion of
urate to allantoin are separate modules.

## Workflow

- [x] Rebase the pathway branch onto current `origin/main`.
- [x] Fetch the three selected KT2440 gene records and relevant family data.
- [x] Define the reusable multi-part module boundary and exact reactions.
- [x] Complete full OpenScientist research for all three genes.
- [x] Complete full OpenScientist generic-module research.
- [x] Complete full OpenScientist module + `ppu00230` + PSEPK research.
- [x] Integrate provider reports after checking every imported claim.
- [x] Complete and validate the three gene reviews and module.
- [x] Render the gene reviews, module, and project page.
- [ ] Open one PR for this module and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Module role |
|---|---|---|---|---|
| [x] | `guaD` | PP_4281 | Q88F18 | Zinc-dependent guanine deamination to xanthine |
| [x] | `xdhA` | PP_4278 | Q88F21 | FAD/[2Fe-2S] electron-transfer subunit of XdhAB |
| [x] | `xdhB` | PP_4279 | Q88F20 | Molybdenum-cofactor catalytic subunit of XdhAB |

## Research Adjudication

The generic and pathway-plus-taxon OpenScientist reports were used as retrieval
support, not as authority. The following claims survived source checking:

- The reusable boundary is a convergent guanine/hypoxanthine supply part plus
  terminal xanthine oxidation, with the two XdhAB reactions kept distinct.
- The characterized P. putida strain-86 enzyme supports two-subunit architecture,
  both purine-base substrates, and NAD+ preference, but is not a KT2440 assay.
- PMID:26355499 directly supports target-strain use of guanine, hypoxanthine,
  xanthine, and uric acid as sole nitrogen sources. This establishes pathway
  operation but does not identify the responsible enzymes genetically.
- XdhC is a non-catalytic maturation factor in a homologous two-subunit system;
  maturation stays outside this catalytic module and remains untested in KT2440.

Claims rejected or narrowed during curation:

- The combined report calls PP_3099/PuuD an urate oxidase. Its reviewed
  TssC/VipB-family architecture instead supports a type VI secretion-system
  sheath role, so this claim is not used here.
- The report reverses the names of GO:0004854 and GO:0004855. This module uses
  validated GO:0004854 xanthine dehydrogenase activity.
- Target-specific oligomeric state, exact electron path, localization,
  catalytic residues, and XdhC requirement were not imported from homologs.
- The XdhB report correctly separates the molybdopterin catalytic architecture
  from XdhA's FAD/Fe-S modules. Its AlphaFold metrics, XdhA2B2 stoichiometry,
  exact Moco form, methylxanthine range, and target-specific maturation claims
  remain unverified for Q88F20 and were not imported.
- `paoABC` is not used as an alternative XDH assignment merely because it
  shares a broad molybdenum-enzyme architecture.

Research artifacts:

- `modules/bacterial_purine_base_oxidation_to_urate-deep-research-openscientist.md`
- `projects/P_PUTIDA/deep-research/PSEPK__bacterial_purine_base_oxidation_to_urate__ppu00230-deep-research-openscientist.md`

## Boundary Decisions

- The module has two substantive root parts: alternative xanthine supply and
  terminal xanthine oxidation to urate.
- The xanthine-supply part has two alternatives: `guaD`-dependent guanine
  deamination and XdhAB-dependent hypoxanthine oxidation. A genome may carry
  either or both entry routes.
- `GO:0070674`/`RHEA:24670` and `GO:0004854`/`RHEA:16669` are distinct
  NAD+-linked activities of the same assembled XdhAB complex.
- Complex-level catalytic terms use `contributes_to` in the subunit reviews;
  neither isolated subunit is treated as independently enabling the complete
  reaction.
- `xdhA` contains the FAD- and [2Fe-2S]-binding architecture. The broad
  InterPro-derived iron annotation on `xdhB` is not compatible with its
  molybdopterin-binding architecture and requires correction.
- The characterized Pseudomonas putida 86 enzyme is homologous evidence for a
  two-subunit, NAD-preferring XDH. It is not direct evidence for KT2440.
- GuaD is additionally grounded by the current PAINT IBD node
  `PTN000138455`. No Xdh PTN is asserted: the available exact PTHR45444 nodes
  are on eukaryotic branches, and PTHR11908 supplies only a broad
  oxidoreductase node for the molybdopterin-binding family.

## Satisfiability Assessment

| Module step | PSEPK assignment | Status | Evidence boundary |
|---|---|---|---|
| Guanine to xanthine | `guaD` / PP_4281 | family-inferred; pathway active | Exact PTHR11271:SF6/IPR014311 family and RHEA:14665; PMID:26355499 confirms guanine supports KT2440 nitrogen use but does not assign GuaD directly. |
| Hypoxanthine to xanthine | `xdhA` + `xdhB` / PP_4278-PP_4279 | family-inferred; pathway active | Complementary Xdh subunit architectures and homologous two-subunit Pseudomonas biochemistry; PMID:26355499 confirms target-strain hypoxanthine use, but no KT2440 reconstitution was found. |
| Xanthine to urate | `xdhA` + `xdhB` / PP_4278-PP_4279 | family-inferred; pathway active | GO:0004854/EC 1.17.1.4 and exact Xdh subunit architecture; PMID:26355499 confirms target-strain xanthine use, while the complex-level qualifier remains essential. |

## Adjacent But Separate

- Nucleoside phosphorolysis and phosphoribosyltransferase salvage are covered
  by `bacterial_purine_salvage`.
- PuuD, PucM, and PucL consume urate in
  `puud_linked_urate_oxidation_to_allantoin`.
- Molybdenum-cofactor synthesis and Xdh maturation are enabling systems, not
  catalytic parts of this reaction chain.
- `paoABC` is a distinct promiscuous aldehyde oxidoreductase system and is not
  used to satisfy XdhAB.

The immutable KEGG membership snapshot is retained in
`ppu00230_bacterial_purine_base_oxidation_to_urate.tsv`.
