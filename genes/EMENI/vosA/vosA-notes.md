# vosA (Aspergillus nidulans) — curation notes

UniProt Q5BBX1 (VOSA_EMENI). Velvet-family regulator of spore maturation/dormancy.
Member of the `conidiation_regulatory_cascade` module (velvet maturation tier).

- Velvet/NF-kB-like DNA-binding regulator; VosA/VelB repress spore cell-wall
  (beta-glucan) biosynthetic genes. [PMID:25960370 "turned off by the NF-kB like fungal regulators VosA and VelB in Aspergillus nidulans"].
- Couples sporogenesis to trehalose biogenesis; expressed during conidial and
  ascospore formation. [PMID:17912349 "we identify the novel regulator VosA that couples the formation of spores and focal trehalose biogenesis in the model fungus Aspergillus nidulans"].
- Core MF asserted: GO:0003700 (DNA-binding TF) from velvet NF-kB-like domain
  [PMID:24391470] — note GOA has not yet annotated this MF (proposed by review).
- protein binding / identical protein binding (IPI) kept non-core (velvet complex
  interactions; uninformative MF).

## 2026-10-01 re-review (GOA refresh)

- No new or vanished GOA rows.
- Protein binding IPI (PMID:24391470) changed KEEP_AS_NON_CORE -> MODIFY to GO:0046982 protein
  heterodimerization activity (VosA-VelB heterodimer crystal structure).
- Added NEW GO:0003700 DNA-binding transcription factor activity (IDA, PMID:24391470): ChIP-chip,
  motif discovery and EMSA with motif deletions show sequence-specific promoter binding, and vosA
  deletion alters target transcripts. This grounds the core MF, which previously had no row.
- Added supporting text to nucleus IDA rows (PMID:21152013, PMID:17912349).
