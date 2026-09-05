---
title: "PSEPK Mla/VacJ intermembrane phospholipid transport"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [mlaF, mlaE, mlaD, ttg2D, ttg2E, vacJ]
---

# PSEPK Mla/VacJ intermembrane phospholipid transport

This batch curates the complete KT2440 Mla/Ttg2 architecture spanning the
outer membrane, periplasm, and inner membrane. It models conserved
phospholipid-exchange interfaces while leaving the physiologically dominant
net transport direction open.

## Workflow

- [x] Fetch all six PSEPK gene records.
- [x] Complete OpenScientist gene research.
- [x] Curate every GOA row for all six genes.
- [x] Create a species-neutral, multi-part module.
- [x] Complete generic module research.
- [x] Complete module + pathway + taxon research.
- [x] Validate and render the reviews, module, and project page.
- [x] Open one non-draft PR: [#2851](https://github.com/ai4curation/ai-gene-review/pull/2851). Review and CI are pending.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | mlaF | PP_0958 | Q88P94 | MlaFEDB ATPase; OpenScientist integrated |
| [x] | mlaE | PP_0959 | Q88P93 | MlaFEDB inner-membrane permease; OpenScientist integrated |
| [x] | mlaD | PP_0960 | Q88P92 | MlaFEDB MCE-domain lipid-binding interface; OpenScientist integrated |
| [x] | ttg2D | PP_0961 | Q88P91 | MlaC-family periplasmic phospholipid carrier; OpenScientist integrated |
| [x] | ttg2E | PP_0962 | Q88P90 | MlaB-like STAS accessory subunit; OpenScientist integrated |
| [x] | vacJ | PP_2163 | Q88KX6 | MlaA-family outer-membrane interface; OpenScientist integrated |

## Boundary Decisions

- The reusable module has three substantive envelope-spanning parts: MlaA/VacJ
  at the outer membrane, MlaC/Ttg2D in the periplasm, and MlaFEDB at the inner
  membrane.
- Ttg2D and Ttg2E retain their Pseudomonas gene names while being modeled as
  the MlaC-family carrier and probable MlaB-like accessory subunit,
  respectively.
- ATP hydrolysis belongs directly to MlaF. Phospholipid transporter activity
  belongs to the assembled MlaFEDB complex, with MlaE contributing the
  integral membrane translocation role.
- Obsolete GO:0005548 is not used in authored module or core-function
  assertions; GO:0120014 phospholipid transfer activity represents the
  assembled MlaFEDB role.
- MlaD and Ttg2D directly bind phospholipids. No generic protein-binding term
  is used.
- UniProt currently describes retrograde transport. The module does not encode
  a directional connection because published Mla models have supported
  different net directions under different experimental interpretations.
- Toluene-tolerance phenotypes are downstream consequences of envelope lipid
  homeostasis, not separate core module steps.
- The KEGG ABC-transporter bucket contains MlaFEDB and Ttg2D/Ttg2E but omits
  VacJ/MlaA from the same primary bucket; module curation restores the complete
  envelope-spanning system.
- The species-aware report confirms complete coverage by PP_0958-PP_0962 plus
  PP_2163. PP_0140-PP_0142 are a separate Mce-like system despite shared
  MlaF/E/D-like signatures, while PP_1737 remains an unresolved second
  MlaA-family candidate. Neither is counted as a core duplicate.
- The generic report supports the three-interface boundary and direction-neutral
  architecture. It also confirms that MlaB is an accessory regulatory/stability
  subunit, MlaA signal-peptide classes vary, and a named OmpC/OmpF partner
  should not be required across all diderm lineages.
- The MlaD report supports Q88P92's single membrane anchor, MCE domain,
  phospholipid binding, and periplasm-facing MlaFEDB interface. Its categorical
  retrograde-direction language and proposed direct link to solvent tolerance
  are not promoted: direction remains an explicit module gap, and the local
  solvent phenotype is indirect pathway context rather than MlaD-specific
  evidence.
- The MlaF report supports Q88P94's intact ABC ATPase motif set, cytoplasmic
  membrane-face localization, and energy-coupling role. Its categorical
  retrograde framing is not promoted; ATP hydrolysis is assigned directly to
  MlaF, while transport direction remains a system-level gap.
- The MlaE report supports Q88P93's five-pass inner-membrane topology and
  permease contribution to the phospholipid-conducting pathway. Its permease
  assignment is retained independently of competing net-direction models.
- The Ttg2E report strengthens the MlaB-equivalent call through its single
  STAS domain and F-E-D-C-B operon position. Assembly/activity support from
  orthologs is retained, but no target-specific regulatory mechanism,
  catalytic MF, or direct toluene-tolerance role is asserted.
