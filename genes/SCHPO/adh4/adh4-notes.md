# adh4 (SPAC5H10.06c, UniProt Q09669) notes

## Identity
- Iron-activated group III ADH family [UniProt:Q09669 "Belongs to the iron-containing alcohol dehydrogenase"], ortholog of S. cerevisiae ADH4; PANTHER PTHR11496:SF102. UniProt gives Zn2+ cofactor by similarity only.
- Transcript induced by zinc deficiency (UniProt, PMID:18203864, not cached).

## Mitochondrial ethanol oxidation
- [PMID:16999687 "exhibit antimycin A-sensitive oxygen uptake activity that is exclusively dependent on ethanol"]
- Matrix location from detergent latency [PMID:16999687 "which demonstrates that the enzyme is located in the matrix"].
- [PMID:16999687 "we show conclusively that the novel mitochondrial ADH is encoded by adh4"].
- Also mitochondrial in the ORFeome YFP screen (HDA PMID:16823372).

## Back-up fermentative ADH
- Induced in adh1 null cells [PMID:15040954 "ADH4-like gene product (SPAC5H10.06C named adh4(+))"]; adh1 adh4 double null non-fermentative [PMID:15040954 "only these two ADHs produce ethanol for fermentative growth"].
- Open issue: how a matrix enzyme supports cytosolic fermentation (shuttle? relocalisation?). Not resolved by cached abstracts.
- adh4 is NOT in the PomBase fermentation GO-CAM (gomodel:678073a900000393); the module lists it as the iron-ADH variant.

## Review decisions
- ARBA carboxylic acid catabolic process REMOVED (ethanol is not a carboxylic acid; no evidence).
- All experimental rows accepted. Considered NEW ethanol catabolic process (GO:0006068) for the mitochondrial oxidation, but left as a suggested question (PomBase curators did not add it; S. pombe cannot grow on ethanol).
- Core functions differ from S. cerevisiae ADH4 review (which uses Ehrlich leucine catabolism): S. pombe-specific evidence is for mitochondrial ethanol oxidation and back-up fermentation.


## 2026-10-25 alcoholic-fermentation member audit

PMID:16999687 (abstract-only after supported force refresh despite PMC1820810) directly states “which demonstrates that the enzyme is located in the matrix” and “we show conclusively that the novel mitochondrial ADH is encoded by adh4”. This supports mitochondrial ethanol oxidation and respiratory reducing-equivalent supply. PMID:15040954 independently supports compensatory ethanol production in adh1-null cells. Do not assign a matrix location to that reductive fermentative core without localization under those conditions. The iron-family name does not prove iron occupancy: UniProt assigns Zn by similarity; the native metal remains unresolved. Broad mitochondrion and alcohol activity rows are refined to matrix and ethanol activity. Previous REMOVE of carboxylic acid catabolism was incorrect: QuickGO ancestry for GO:0019655 includes GO:0046395. An enzyme can participate in a pathway consuming pyruvate without directly acting on the carboxylic acid itself. The broad row is now MODIFY to fermentation.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR11496; ALCOHOL DEHYDROGENASE; 1.
- DR   PANTHER; PTHR11496:SF102; ALCOHOL DEHYDROGENASE 4; 1.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 15 rows; ACCEPT=7, MODIFY=8. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate SCHPO adh4` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
