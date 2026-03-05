# Deep Research Summary for ARBA00090252

## Literature Analysis from TMA16 Studies

Based on comprehensive literature review of ribosomal export factors from TMA16 deep research ([TMA16-deep-research-falcon.md](file:genes/human/TMA16/TMA16-deep-research-falcon.md)), the following key findings contradict the annotations proposed by ARBA00090252:

### True Ribosomal Export Factors

1. **TMA16 (Translation machinery-associated protein 16)**:
   - Functions as ribosome-associated factor (RAF) in **late-stage 60S maturation/export**
   - Listed alongside eIF6, NMD3, LLPH as **pre-60S export/maturation factors**
   - Acts as **export adapter** rather than structural component
   - Reference: Junod et al., iScience, 2023 [DOI: 10.1016/j.isci.2023.107445](https://doi.org/10.1016/j.isci.2023.107445)

2. **NMD3 (Nuclear export mediator)**:
   - Dedicated **adapter protein** for nuclear export of large ribosomal subunit
   - Provides **nuclear export signals** via Crm1/Exportin-1
   - **Not a structural component** of the ribosome
   - Reference: Klingauf-Nerurkar et al., eLife, 2020 [DOI: 10.7554/eLife.52474](https://doi.org/10.7554/eLife.52474)

3. **eIF6 (Eukaryotic translation initiation factor 6)**:
   - Anti-association factor preventing premature 60S joining
   - **Export accessory protein**, not ribosomal structural component
   - Reference: Junod et al., iScience, 2023

### Ribosomal Structural Proteins (ARBA00090252 Targets)

The literature clearly distinguishes between export factors and ribosomal proteins:

1. **RPL40 (60S ribosomal protein L40)**:
   - **Structural component** incorporated into 60S subunit during assembly
   - Ubiquitin-ribosomal fusion protein: ubiquitin cleaved off post-translation
   - Functions in **translation** (GO:0006412) and as **structural constituent** (GO:0003735)
   - **Exported as cargo**, not as export mediator

2. **RPL10A (60S ribosomal protein L10A)**:
   - **Structural component** of the 60S ribosomal subunit
   - Involved in **translation**, not nuclear export mediation
   - Part of ribosome structure, not export machinery

### Critical Distinction

The literature reveals a fundamental distinction missed by ARBA00090252:

- **Export factors** (TMA16, NMD3, eIF6): Have adapter/regulatory activity, provide export signals, facilitate transport
- **Ribosomal proteins** (RPL40, RPL10A): Structural components that are **passengers** in the export process

### Export Process Kinetics

Recent live-cell studies show:
- Pre-60S export time: **13 ± 1 ms** through nuclear pores
- Export factors (TMA16, NMD3, eIF6, LLPH) facilitate this process
- Ribosomal proteins are **cargo**, not facilitators

## Conclusion

The deep research definitively shows that ARBA00090252 incorrectly assigns export process function (GO:0000055) to structural proteins that are exported **as cargo**. The rule conflates being a component of an exported complex with mediating the export process itself, violating fundamental GO principles.

## References

- Junod SL et al. Dynamics of nuclear export of pre-ribosomal subunits revealed by high-speed single-molecule microscopy in live cells. iScience 26:107445, 2023. DOI: 10.1016/j.isci.2023.107445
- Klingauf-Nerurkar P et al. The GTPase Nog1 co-ordinates the assembly, maturation and quality control of ribosomal subunits. eLife 9:e52474, 2020. DOI: 10.7554/eLife.52474
- Prattes M et al. Visualizing maturation factor extraction from the nascent ribosome by the AAA-ATPase Drg1. Nature Structural & Molecular Biology 29:942-953, 2022. DOI: 10.1038/s41594-022-00832-5