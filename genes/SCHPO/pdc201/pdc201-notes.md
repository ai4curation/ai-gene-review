# pdc201 (SPAC3G9.11c, UniProt O42873, PDC4_SCHPO) notes

- Clusters with ScPdc1/5/6 [PMID:25102102 "The Pdc201 and Pdc202 cluster together, along with three reported PDCs of S. cerevisiae (ScPdc1, 5, 6;"]. PANTHER PTHR43452:SF36.
- Stationary-phase induction via Phx1 [PMID:25102102 "Expression of pdc201+ and pdc202+ genes increased markedly during stationary phase, by about 500-fold and 50-fold, respectively."].
- PDC activity in stationary cells is Phx1 dependent [PMID:25102102 "PDC enzyme activity increased during stationary phase in wild type, but decreased in the mutant"].
- Protein up from ~7,000 to ~52,000 copies/cell in quiescence [PMID:25102102 "Pdc201 increases from ~7000 copies per cell during growth to ~52,000 copies during quiescence"].
- Chronological survival: deletion lowers, overexpression raises [PMID:25102102 "the Δpdc201 and Δpdc202 mutations reduced cell viability in the stationary phase"]; [PMID:25102102 "overproduction of either Pdc201 or Pdc202 increased the long-term viability of both the wild type and Δphx1 mutant"].
- UniProt: no gene name; fetched with `-u O42873`. Cytoplasm + nucleus from ORFeome.
- GO-CAM gomodel:678073a900000393: enables GO:0004737, part_of GO:0019660; the pdc201 activity has RO:0002413 (provides input for) edges to downstream activities, and the phx1 activity has RO:0002407 causal edges to the pdc activities.
- Review: nucleus rows KEEP_AS_NON_CORE; lifespan phenotypes not turned into NEW annotations (downstream of metabolic activity).


## 2026-10-25 alcoholic-fermentation member audit

PMID:25102102 links Pdc201 (SPAC3G9.11c; O42873) to Phx1-dependent stationary-phase induction and survival. “Expression of pdc201+ and pdc202+ genes increased markedly during stationary phase, by about 500-fold and 50-fold, respectively.” Total cellular PDC activity is measured; do not describe this as purified Pdc201 kinetics. Cytoplasm is refined to existing cytosol. Nuclear localization remains non-core and does not establish nuclear catalysis.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR43452; PYRUVATE DECARBOXYLASE; 1.
- DR   PANTHER; PTHR43452:SF36; PYRUVATE DECARBOXYLASE C3G9.11C-RELATED; 1.

The cached PomBase GO-CAM 678073a900000393 includes the acetaldehyde-producing PDC activities and downstream ethanol/acetate branches. This supports keeping the upstream process appropriately broad; it does not assign all product branches to every enzyme. PDC activities are family-supported, with stronger isozyme-specific physiology for Pdc101/Pdc201/Pdc202 than Pdc102.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 14 rows; ACCEPT=8, KEEP_AS_NON_CORE=3, MODIFY=3. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate SCHPO pdc201` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
