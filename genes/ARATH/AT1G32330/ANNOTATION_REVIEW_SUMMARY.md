# HSFA1D (AT1G32330) Annotation Review Summary

## Current Review Position

The YAML review treats HSFA1D as an HSE-binding class A heat shock transcription
activator. Existing DNA-binding, transcription-factor, nucleus, cytoplasm, and
heat-response annotations are retained where supported. Generic regulatory or binding
terms are narrowed only when the local evidence supports a more informative GO term.

## Key Decisions

- Retain existing `GO:0003700 DNA-binding transcription factor activity` annotations.
- Use `GO:0001228 DNA-binding transcription activator activity, RNA polymerase
  II-specific` as the core molecular-function framing.
- Retain nuclear and cytoplasmic localization annotations.
- Retain broad heat-response annotations without adding unsupported light, circadian,
  thermomorphogenesis, cold, osmotic, or salt process terms.
- Modify generic `GO:0005515 protein binding` to `GO:0051879 Hsp90 protein binding`
  based on PMID:19704818 and the UniProt HSP90-2 interaction.

## Non-Retained Draft Recommendations

Earlier draft summaries suggested future annotations for blue light response,
circadian regulation, brassinosteroid signaling, thermomorphogenesis, chilling, and
salt/osmotic stress. These are not current review recommendations.
