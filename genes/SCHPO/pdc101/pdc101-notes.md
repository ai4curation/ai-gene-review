# pdc101 (SPAC1F8.07c, UniProt Q92345, PDC2_SCHPO) notes

## Naming trap
- Fission-yeast pdc1 is an mRNA decapping scaffold (SPAC4F10.01), hence the pdc101/102/201/202 names [PMID:25102102 "Since the gene name pdc1 has been already used for mRNA decapping scaffold protein (SPAC4F10.01) [24], we propose to name the paralogs as pdc101(SPAC1F8.07c), pdc102(SPAC186.09), pdc201(SPAC3G9.11c), and pdc202(SPAC13A11.06)"].
- UniProt entry names do not follow the gene numbers: pdc101 = PDC2_SCHPO, pdc102 = PDC3_SCHPO, pdc201 = PDC4_SCHPO, pdc202 = PDC1_SCHPO.

## Evidence
- Main growth-phase isozyme [PMID:25102102 "Therefore, Pdc101 is most likely the primary pyruvate decarboxylase that supports exponential growth."]; not Phx1-dependent.
- Probably essential [PMID:25102102 "We were not able to obtain a Δpdc101 mutant, consistent with the prediction that this gene is essential"].
- Abundant protein [PMID:25102102 "Pdc101 is expressed at ~500,000 copies per cell during growth"].
- Phylogeny: separate clade from ScPdc1/5/6 [PMID:25102102 "Pdc101 and Pdc102 clustered closely in a separate clade, along with PDCs of N. crassa and A. fumigatus and four PDC proteins from plant kingdom"]. PANTHER PTHR43452:SF1.
- No purified-enzyme data; activity rests on conserved active site and IBA.

## GO-CAM
- gomodel:678073a900000393: pdc101 enables GO:0004737, part_of GO:0019660 pyruvate fermentation (generic; curator comment says fermentation terms to be refined, go-ontology issue 29511). Acetaldehyde in the model feeds both adh1 (ethanol) and atd1 (acetate, GO:0019654).

## Review decisions
- Generic root/parent MFs MODIFY -> GO:0004737; all else ACCEPT. Core BP = GO:0019660 to follow PomBase (differs from ScPDC1 core, which uses GO:0019655).


## 2026-10-25 alcoholic-fermentation member audit

PMID:25102102 identifies Pdc101 (SPAC1F8.07c; Q92345) as the predominant growth-phase PDC. “Therefore, Pdc101 is most likely the primary pyruvate decarboxylase that supports exponential growth.” Failure to recover deletion is suggestive, not definitive proof of essentiality. Its generic 2-oxocarboxylate UniProt reaction does not alone prove pyruvate specificity; the PDC family classification and primary paralog analysis provide that context.

Exact current UniProt PANTHER cross-references (official labels checked against the local PANTHER ontology):

- DR   PANTHER; PTHR43452; PYRUVATE DECARBOXYLASE; 1.
- DR   PANTHER; PTHR43452:SF1; PYRUVATE DECARBOXYLASE C186.09-RELATED; 1.

The cached PomBase GO-CAM 678073a900000393 includes the acetaldehyde-producing PDC activities and downstream ethanol/acetate branches. This supports keeping the upstream process appropriately broad; it does not assign all product branches to every enzyme. PDC activities are family-supported, with stronger isozyme-specific physiology for Pdc101/Pdc201/Pdc202 than Pdc102.

Research provenance: normal fetch/publication caching completed. No pre-existing provider research was available for these records. The default Falcon attempt for SCHPO adh4 failed authentication; its perplexity-lite fallback failed because quota/credits were unavailable (session log /tmp/bacillus-ferment-deep.log). The same known outage was not retried for seven additional genes. This is manual primary-literature research, not a generated provider report. FEBA fitness data are not required for these eukaryotic genes. Cached full-text flags were inspected; abstracts are not represented as full-text readings. UniProt quotes use curated statements or family/features, not DE names, GO annotation lines, ARBA predictions or protein-existence levels.

Every original annotation was independently assessed; no source annotation fields or negation flags were changed. No NEW annotation rows were added. Core functions distinguish catalytic activity from stress induction and avoid pathway-exclusivity or compartment assumptions. Review counts: 9 rows; ACCEPT=7, MODIFY=2. Targeted schema, quote, consistency and ontology validation is run after record-section backfill.

Validation outcome: targeted `just validate SCHPO pdc101` passed; the matching codex history record also passed schema validation. Original source annotation fields were preserved.
