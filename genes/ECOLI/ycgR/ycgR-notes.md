# ycgR: c-di-GMP module member review

## 2026-11-05

Direct E. coli YcgR binding was established with purified protein [PMID:16920715, “bind c-di-GMP tightly and specifically”]. That paper also reports Salmonella motility genetics; the species are distinguished. E. coli motor mechanisms are directly supported by PMID:20303158 and PMID:31836667. PMID:20346719 reports FliG/FliM interactions and includes Salmonella fluorescent basal-body localization, which is not relabeled as an E. coli localization assay.

The early hns/yhjH suppression studies [PMID:11031114; PMID:17941710] are consistent with motor regulation. Broad motility rows are refined to GO:0071945; the original evidence payloads remain unchanged. Generic protein-binding rows are removed as uninformative, without denying motor contacts. GO:0140659 names a cytoskeletal motor regulator, so it is not used for the bacterial rotary flagellar motor.

No PANTHER family is recorded for YcgR, so the standard PAINT lineage-loss tool could not run a lineage check. PMID:31836667 remained abstract-only after standard cache refresh; the abstract explicitly describes MotA binding and the structural mechanism. No additional NEW annotation is needed because the established receptor MF and motor-regulatory BP are already present.

Falcon deep research was attempted with the standard recipe and failed with HTTP 403 authentication. No provider report was authored manually. This review uses primary-source retrieval and cached papers. Original GOA annotation payloads and UniProt/GOA files were preserved.


## PR #6062 review follow-up — 2026-11-06

Refined all three generic protein-binding rows to GO:0140678, grounded in the original interaction studies and PMID:20303158 motor braking, and separated the inhibitory core from ligand recognition. Marked the electronic basal-body assignment over-annotated because protein contacts and Salmonella imaging do not establish E. coli basal-body residence. No new annotation row or substitute localization was added.
