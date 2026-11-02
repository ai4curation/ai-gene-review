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
- Historical decision, superseded by the 2026-10-25 audit below: ARBA carboxylic acid catabolic process was removed. The current review correctly refines this true pathway-level claim to fermentation.
- All experimental rows accepted. Considered NEW ethanol catabolic process (GO:0006068) for the mitochondrial oxidation, but left as a suggested question (PomBase curators did not add it; S. pombe cannot grow on ethanol).
- Core functions differ from S. cerevisiae ADH4 review (which uses Ehrlich leucine catabolism): S. pombe-specific evidence is for mitochondrial ethanol oxidation and back-up fermentation.


## 2026-10-25 alcoholic-fermentation member audit

PMID:16999687 (abstract-only after supported force refresh despite PMC1820810) directly states “which demonstrates that the enzyme is located in the matrix” and “we show conclusively that the novel mitochondrial ADH is encoded by adh4”. This supports mitochondrial ethanol oxidation and respiratory reducing-equivalent supply. PMID:15040954 independently supports compensatory ethanol production in adh1-null cells. Do not assign a matrix location to that reductive fermentative core without localization under those conditions. The iron-family name does not prove iron occupancy: UniProt assigns Zn by similarity; the native metal remains unresolved. Alcohol activity rows are refined to ethanol activity. The mitochondrial-to-matrix refinement originally made in this audit is superseded by the 2026-10-26 correction below: the informative root-organelle assertions are retained independently of matrix localization. Previous REMOVE of carboxylic acid catabolism was incorrect: QuickGO ancestry for GO:0019655 includes GO:0046395. An enzyme can participate in a pathway consuming pyruvate without directly acting on the carboxylic acid itself. The broad row is now MODIFY to fermentation.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR11496; ALCOHOL DEHYDROGENASE; 1.
- DR   PANTHER; PTHR11496:SF102; ALCOHOL DEHYDROGENASE 4; 1.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 15 rows; ACCEPT=7, MODIFY=8. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate SCHPO adh4` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.


## 2026-10-26 informative root-organelle correction

Restored the two existing mitochondrion rows (one-based ordinals 5 and 6) from MODIFY to ACCEPT. All 15 original annotation payloads remain unchanged; both separate matrix annotations and both core functions are unchanged. Current totals: ACCEPT=9, MODIFY=6.

PMID:16999687 explicitly reports Adh4-dependent ethanol-oxidizing activity in isolated mitochondria, identifies the enzyme through genetic knockouts, and uses approximately 16-fold Triton latency to support matrix localization. This establishes both organelle and finer compartment claims; matrix is not a replacement for the informative organelle assertion. The normal force refresh again retained an abstract-only cache. The live PMC page additionally exposed Methods and Results through the detergent-latency analysis (Table 1: 44±5 without versus 716±159 with Triton); a subsequent request hit a browser challenge. These accessible portions corroborate the cached abstract, but this follow-up does not claim to have recovered the entire primary text or a durable new full-text cache. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC1820810/.

PMID:16823372 is separately an ORFeome YFP localization screen. Its abstract describes the method, not the target image or matrix topology; the publisher page was inaccessible. Retain the curator's mitochondrial observation with independent target corroboration from PMID:16999687. Do not describe this screen row as if it measured isolated mitochondrial activity or detergent latency. No inaccessible screen content was inferred.

The earlier limitation remains: the oxidative mitochondrial assay does not locate the compensatory reductive fermentation documented in adh1-null cells. No relocalization, shuttle, metal identity or new biological-process assertion is introduced. Independent annotation-reviewer consultation agreed with this source-specific distinction. The prior actual Falcon/fallback failures remain documented above; this bounded corrective audit used manual primary-source reassessment, not a fabricated provider report.
