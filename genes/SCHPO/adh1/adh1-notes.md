# adh1 (SPCC13B11.01, UniProt P00332) notes

Evidence journal (no paid deep research run; built from UniProt, cached PMIDs and the PomBase GO-CAM).

## Identity and activity
- Zinc medium-chain ADH, EC 1.1.1.1, ortholog of S. cerevisiae ADH1 [UniProt:P00332 "Belongs to the zinc-containing alcohol dehydrogenase"].
- Function: [UniProt:P00332 "Reduces acetaldehyde to ethanol during the fermentation of"] glucose.
- Kinetics of the cloned S. pombe enzyme compared with ScADH I-III [PMID:3546317 "All four wild-type enzymes were produced from the cloned genes"]; S. pombe ADH has Met at position 294 like ScADH I [PMID:3546317 "Isozyme I and the S. pombe enzyme have methionine at position 294"]. UniProt KM for acetaldehyde 1.6 mM, NADH 100 uM.
- Two Zn2+ per subunit, homotetramer by similarity to P00330 [UniProt:P00332].

## Physiology
- adh1 null cells still ferment; adh4 is induced and takes over [PMID:15040954 "this ethanol production is caused by the enhanced expression of a Saccharomyces cerevisiae ADH4-like gene product"]; double mutant is non-fermentative [PMID:15040954 "only these two ADHs produce ethanol for fermentative growth"].
- Kim et al. note adh1 overexpression extends lifespan in S. pombe [PMID:25102102 "There are reports that overexpression of the adh1+ gene extends lifespan in S. cerevisiae [35] and in S. pombe [36]"].

## GO-CAM
- PomBase gomodel:678073a900000393 (fermentation): adh1 enables GO:0120542, occurs_in cytosol, part_of GO:0019655 (IGI PMID:15040954 with adh4).

## Review decisions
- All MF/CC rows accepted; oxidoreductase -> MODIFY to GO:0120542; ARBA ethanol metabolic process -> MODIFY to GO:0019655.
- Core function matches S. cerevisiae ADH1 review (GO:0120542, GO:0019655, cytosol). No Ehrlich-pathway core function added: not studied in S. pombe.


## 2026-10-25 alcoholic-fermentation member audit

PMID:3546317 characterizes cloned fission-yeast ADH alongside budding-yeast enzymes. “The mechanisms for all five enzymes were predominantly ordered with ethanol (but partially random with butanol)”. Therefore broad alcohol dehydrogenase activity retains measured substrate breadth, while the ethanol-specific activity represents the main fermentative reaction. Cytoplasm rows are refined to existing cytosol. PMID:15040954 establishes Adh4 compensation in adh1-null cells; the two-enzyme genetic conclusion is bounded to tested conditions. Reversible ethanol oxidation is real and is not denied by assigning the dominant native fermentative process.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR42940; ALCOHOL DEHYDROGENASE 1-RELATED; 1.
- DR   PANTHER; PTHR42940:SF3; ALCOHOL DEHYDROGENASE 1-RELATED; 1.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 13 rows; ACCEPT=8, MODIFY=5. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate SCHPO adh1` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
