# Curation Notes: Variovorax paradoxus `iadI` (`A0A0H2M433`, `VPARA_32130`)

## Summary
- **Gene symbol**: `iadI` (annotated as `kynB2`, locus tag `VPARA_32130`, 270 aa; orthologous to *V. paradoxus* CL14 IMG `2643613664`).
- **Operon & pathway context (`PMID:36266335`, `PMID:37459330`)**:
  - Encoded within the conserved *Variovorax* `iad` auxin-degradation operon between `iadH` (`VPARA_32140`) and `iadJ` (`VPARA_32120`).
  - Metabolomics with $^{13}\text{C}_6$-IAA in *V. paradoxus* CL14 demonstrates that the `iad` pathway degrades IAA through dioxindole-3-acetic acid, dioxindole, isatin, and isatinic acid to anthranilic acid [PMID:36266335, "The intermediates dioxindole, isatin and isatinic acid, and the product anthranilic acid were all detected and thus produced in the bacterial cultures. Importantly, catechol, the main product of the iac IAA degradation, was not detected in any of the V. paradoxus CL14 samples."].
  - `IadI` belongs to the kynurenine formamidase / cyclase metallohydrolase family (`PF04199` / `IPR007325`, EC 3.5.1.9) and provides the arylformamidase activity that hydrolyzes the formyl/acyl group from ring-opened oxidized indole intermediates to yield anthranilic acid.
- **Annotation review**:
  - `ACCEPT` `GO:0004061` (`arylformamidase activity`).
  - `REMOVE` `GO:0006569` (`L-tryptophan catabolic process`, `IEA` from `InterPro:IPR007325`), which is an automated domain projection from canonical tryptophan-kynurenine pathway formamidases (`KynB`), and add `NEW` `GO:0042437` (`indoleacetic acid catabolic process`, `IEP`, `PMID:36266335`).
