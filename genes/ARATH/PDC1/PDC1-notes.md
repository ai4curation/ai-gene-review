# PDC1 research notes


## 2026-10-25 alcoholic-fermentation member audit

O82647 / At4g33070 is PDC1. PMID:12805625 establishes impaired anoxia tolerance in pdc1; PMID:12857811 measures pathway manipulation and supports improved fermentative flux/survival after PDC1 overexpression. No claim that all four Arabidopsis paralogs have identical regulation is warranted. PMID:38165809 demonstrates nitrate-dependent modulation of PDC1 induction, not nitrate catalysis. Membrane HDA and AtSubP chloroplast assignments remain UNDECIDED because the target-specific localization evidence was not independently resolved. PDC1’s inherited cytosol annotation is retained, not used to exclude minor organellar/membrane pools. No NEW process annotation is manufactured to make the module complete.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR43452; PYRUVATE DECARBOXYLASE; 1.
- DR   PANTHER; PTHR43452:SF18; PYRUVATE DECARBOXYLASE 1; 1.

PMID:30861072 (PMC6436157), “Conservation of ethanol fermentation and its regulation in land plants”, was force-refetched successfully with full text. It detects ethanol output even in adh1, adh1 adh2 and pdc1 pdc2 seedlings. Conserved native ethanol output therefore does not establish exclusive reliance on these exact paralogs across plants. The tested Marchantia ADH-like candidate did not complement Arabidopsis ADH1 and groups with GSNOR-like proteins; no functionally validated liverwort ADH1 exemplar is added from that candidate.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 14 rows; ACCEPT=7, KEEP_AS_NON_CORE=1, MODIFY=4, UNDECIDED=2. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate ARATH PDC1` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
