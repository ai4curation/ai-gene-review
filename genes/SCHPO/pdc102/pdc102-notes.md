# pdc102 (SPAC186.09, UniProt Q9P7P6, PDC3_SCHPO) notes

- Paralog of pdc101 in PTHR43452:SF1 [PMID:25102102 "Pdc101 and Pdc102 clustered closely in a separate clade, along with PDCs of N. crassa and A. fumigatus and four PDC proteins from plant kingdom"].
- Barely expressed [PMID:25102102 "The pdc102+ gene produced hardly detectable mRNA in both conditions."]; protein not detected [PMID:25102102 "Pdc102 and Pdc202 have not been detected at the protein level"].
- Deletion has no stationary viability phenotype [PMID:25102102 "The Δpdc102 mutation did not affect cell viability significantly."].
- UniProt PE 3 (homology); substrate and Mg2+ binding residues annotated by similarity [UniProt:Q9P7P6]. UniProt has no gene name (ORF only), so `just fetch-gene SCHPO pdc102` failed; fetched with `-u Q9P7P6`.
- ORFeome YFP (overexpressed): cytosol + nucleus (HDA PMID:16823372).
- GO-CAM gomodel:678073a900000393: enables GO:0004737, part_of GO:0019660.
- Review: MF accepted on conserved active site; nucleus kept as non-core; core function flagged as predicted.


## 2026-10-25 alcoholic-fermentation member audit

PMID:25102102 identifies Pdc102 (SPAC186.09; Q9P7P6). “The pdc102+ gene produced hardly detectable mRNA in both conditions.” Deletion did not significantly affect stationary-phase viability. Retain the inherited PDC activity from phylogenetic/family evidence; low expression neither demonstrates loss of catalysis nor proves substantial native pathway flux. Nuclear/cytosol screen annotations are curator-supported; target images were not independently inspected.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR43452; PYRUVATE DECARBOXYLASE; 1.
- DR   PANTHER; PTHR43452:SF1; PYRUVATE DECARBOXYLASE C186.09-RELATED; 1.

The cached PomBase GO-CAM 678073a900000393 includes the acetaldehyde-producing PDC activities and downstream ethanol/acetate branches. This supports keeping the upstream process appropriately broad; it does not assign all product branches to every enzyme. PDC activities are family-supported, with stronger isozyme-specific physiology for Pdc101/Pdc201/Pdc202 than Pdc102.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 11 rows; ACCEPT=8, KEEP_AS_NON_CORE=1, MODIFY=2. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate SCHPO pdc102` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
