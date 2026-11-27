# PRR7 (APRR7, At5g02810; UniProt Q93WK5) curation notes

## 2026-10-06: initial review (module plant_circadian_clock_oscillator)

- Fetched with `just fetch-gene ARATH Q93WK5 --alias PRR7`. Falcon deep research failed; review based on cached publications.

### Key findings
- Repressor of CCA1/LHY with PRR9/PRR5 [PMID:20233950 "Here, we demonstrate that PRR9, PRR7, and PRR5 act as transcriptional repressors of CCA1 and LHY."]; acts with TPL/TPR [PMID:23267111].
- Directly represses morning-expressed growth, light and stress regulators [PMID:23808423 "PRR7 is important for cyclic gene expression by repressing the transcription of morning-expressed genes"].
- Nuclear PRR7-GUS; prr7 de-etiolation defect and phase advance [PMID:14563930 "A PRR7-beta-glucuronidase fusion protein localized to the nucleus"].
- prr5 prr7 double mutant nearly arrhythmic [PMID:15695441].
- Sugar entrainment: bZIP63 regulates PRR7 transcription [PMID:30078562]. The TAIR protein-binding row citing this paper has bZIP63 in WITH, but the paper's central result concerns PRR7 promoter regulation.

### Decisions
- Mitochondrion HDA (PMID:14671022, proteome of 416 proteins, about half predicted mitochondrial): MARK_AS_OVER_ANNOTATED, likely co-purification.
- Phosphorelay and cytokinin IEA: REMOVE. DNA-binding TF activity IBA: MODIFY to GO:0001227.
- Protein binding: REMOVE.
