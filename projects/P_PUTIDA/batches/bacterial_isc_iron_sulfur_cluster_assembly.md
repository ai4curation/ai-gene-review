---
title: "PSEPK bacterial Isc iron-sulfur cluster assembly"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [iscS, iscU, iscA, hscB, hscA, fdx]
autolink_gene_symbols: false
---

# PSEPK Isc iron-sulfur cluster assembly

This batch models the contiguous iscS-iscU-iscA-hscB-hscA-fdx machinery as a
reusable six-part bacterial assembly process. IscS and IscU form the conserved
assembly core; Fdx, IscA, and the HscB-HscA remodeling cycle are explicit
accessory branches rather than a mandatory linear sequence. The upstream iscR
regulator is important pathway control but is outside the assembly boundary.

## Workflow

- [x] Confirm no existing PSEPK Isc assembly PR or reusable bacterial Isc module.
- [x] Fetch current UniProt and GOA records for all six selected genes.
- [x] Start full-allowance OpenScientist research for six genes.
- [x] Start generic module and PSEPK module/pathway OpenScientist research.
- [x] Curate all six GOA sets and synthesize core functions.
- [ ] Integrate completed research without promoting unsupported hypotheses.
- [x] Validate and render gene, module, and project artifacts.
- [ ] Open one draft PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK gene | UniProt | Initial assessment |
|---|---|---|---|---|
| 1 | Sulfur mobilization | iscS / PP_0842 | Q88PK8 | Covered by the IscS-specific cysteine desulfurase |
| 2 | Transient cluster scaffold | iscU / PP_0843 | Q88PK7 | Covered by TIGR01999/IPR011339 IscU |
| 3 | Reducing-equivalent delivery | fdx / PP_0847 | Q88PK3 | Covered by TIGR02007/IPR011536 Isc ferredoxin |
| 4 | IscU targeting and ATPase activation | hscB / PP_0845 | Q88PK5 | Covered by the dedicated HscB co-chaperone |
| 5 | ATP-dependent scaffold remodeling | hscA / PP_0846 | Q88PK4 | Covered by the dedicated HscA chaperone ATPase |
| 6 | Late assembly or cluster transfer | iscA / PP_0844 | Q88PK6 | Covered by TIGR02011/IPR011302 proteobacterial IscA |

## Boundary

- Include direct Fe-S assembly, scaffold-remodeling, reduction, and transfer roles.
- Exclude IscR transcriptional regulation from the core machinery.
- Exclude Fe-S recipient proteins and downstream Fe-S-dependent reactions.
- Exclude Suf and Nif systems; they require separate variant-aware modules.
- Do not use generic cytoplasm/cytosol calls as module-defining biology.

Generated UTC: 2026-08-12
