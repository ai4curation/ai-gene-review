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
- [ ] Complete OpenScientist gene research.
- [x] Curate every GOA row for all six genes.
- [x] Create a species-neutral, multi-part module.
- [ ] Complete generic module research.
- [ ] Complete module + pathway + taxon research.
- [ ] Validate and render the reviews, module, and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | mlaF | PP_0958 | Q88P94 | MlaFEDB ATPase |
| [x] | mlaE | PP_0959 | Q88P93 | MlaFEDB inner-membrane permease |
| [x] | mlaD | PP_0960 | Q88P92 | MlaFEDB MCE-domain lipid-binding interface |
| [x] | ttg2D | PP_0961 | Q88P91 | MlaC-family periplasmic phospholipid carrier; OpenScientist integrated |
| [x] | ttg2E | PP_0962 | Q88P90 | MlaB-like STAS accessory subunit |
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
