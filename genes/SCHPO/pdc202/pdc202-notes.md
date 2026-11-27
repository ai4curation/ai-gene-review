# pdc202 (SPAC13A11.06, UniProt Q09737, PDC1_SCHPO) notes

- Naming trap: UniProt entry name PDC1_SCHPO, but the S. pombe gene pdc1 (SPAC4F10.01) is an mRNA decapping scaffold [PMID:25102102 "Since the gene name pdc1 has been already used for mRNA decapping scaffold protein (SPAC4F10.01)"].
- Clusters with ScPdc1/5/6 and pdc201 [PMID:25102102 "The Pdc201 and Pdc202 cluster together, along with three reported PDCs of S. cerevisiae (ScPdc1, 5, 6;"]. PANTHER PTHR43452:SF30.
- ~50-fold stationary induction, Phx1 dependent [PMID:25102102 "Expression of pdc201+ and pdc202+ genes increased markedly during stationary phase, by about 500-fold and 50-fold, respectively."]; strong late-meiosis induction [PMID:25102102 "The pdc202+ mRNA level dramatically increased during the late meiotic process in forming spores"].
- Protein not detected in proteomics [PMID:25102102 "Pdc102 and Pdc202 have not been detected at the protein level"].
- Deletion lowers and overexpression raises stationary viability (PMID:25102102).
- GO-CAM gomodel:678073a900000393: enables GO:0004737, part_of GO:0019655 (ISO from SGD PDC1) - the only pdc in the model with the ethanol-specific term; the other three use GO:0019660. Flagged as an inconsistency for module curator.
- UniProt has no gene name; fetched with `-u Q09737`.


## 2026-10-25 alcoholic-fermentation member audit

PMID:25102102 links Pdc202 (SPAC13A11.06; Q09737) to stationary-phase induction and survival. “overproduction of either Pdc201 or Pdc202 increased the long-term viability of both the wild type and Δphx1 mutant”. This is not a direct measurement of its share of fermentative flux. UniProt PDC1_SCHPO must not be confused with the unrelated gene pdc1 encoding a decapping scaffold. Generic pyruvate fermentation remains suitable for the shared acetaldehyde-producing step even though the ethanol-specific ISO row is also retained.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR43452; PYRUVATE DECARBOXYLASE; 1.
- DR   PANTHER; PTHR43452:SF30; PYRUVATE DECARBOXYLASE ISOZYME 1-RELATED; 1.

The cached PomBase GO-CAM 678073a900000393 includes the acetaldehyde-producing PDC activities and downstream ethanol/acetate branches. This supports keeping the upstream process appropriately broad; it does not assign all product branches to every enzyme. PDC activities are family-supported, with stronger isozyme-specific physiology for Pdc101/Pdc201/Pdc202 than Pdc102.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 12 rows; ACCEPT=8, KEEP_AS_NON_CORE=2, MODIFY=2. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate SCHPO pdc202` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
