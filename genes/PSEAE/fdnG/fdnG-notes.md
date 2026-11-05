# fdnG (PA4812, Q14T72) notes

Catalytic Mo-bisMGD alpha subunit of the nitrate-inducible respiratory formate dehydrogenase FdnGHI (fdnG-fdnH-fdnI, PA4812-PA4810). No deep-research provider was available; literature search by hand (PubMed search "formate dehydrogenase Pseudomonas aeruginosa", PMID:3038081 abstract, QuickGO for E. coli seeds).

## Literature

- Godfrey et al. 1987 (PMID:3038081; abstract only, PMC1147836 is a scanned PDF with no text via the PubMed MCP): FDH purified from anaerobically nitrate-grown P. aeruginosa ["The purification of formate dehydrogenase (FDH) from Pseudomonas aeruginosa after anaerobic growth on nitrate-containing medium was carried out."], co-fractionating with nitrate reductase ["found together in a particle fraction and constitute the short respiratory chain of this bacterium"]. Activity assayed with Nitro Blue Tetrazolium (artificial acceptor). The purest preparation contains a bis-histidine cytochrome, a [4Fe-4S]+ cluster and molybdenum ["These techniques have allowed the haem, iron-sulphur clusters and molybdenum components to be detected"]; [3Fe-4S] and cytochrome c are contaminants removed with NiR.
- The paper predates the genome and does not assign polypeptides to genes. A UniProt query (organism 208964, protein name "formate dehydrogenase", 2026-11-05) returns only PA4810-PA4812, so the purified enzyme is attributed to FdnGHI; the cofactor set matches (FdnG Mo-bisMGD + [4Fe-4S], FdnH 4x[4Fe-4S], FdnI di-haem cytochrome b).
- QuickGO (2026-11-05), E. coli comparators: FdnG P24183, FdnH P0AAJ3 and FdnI P0AEK7 each carry GO:0036397 by IDA (EcoCyc, PMID:1099093); FdoG P32176 and FdoH P0AAJ5 by IDA (PMID:1504073). So the complex-level activity is annotated to every subunit by convention, from purified-complex biochemistry.

## Operon-level phenotype check

The brief asked whether the FDH subunits show the cbb3/ccoP error (an operon mutant phenotype annotated to each subunit activity). They do not: the PseudoCAP rows come from biochemistry of a purified complex, the same evidence type and convention EcoCyc uses for E. coli FdnGHI. The only caveats are (a) the dye assay does not show quinone as acceptor (quinone linkage is inferred from the membrane nitrate-respiratory chain), and (b) gene attribution is inferred. Neither makes the row wrong, so verdict SOUND, no PSEUDOCAP or GO_CENTRAL defect. For FdnH and FdnI the complex activity is recorded as contributes_to_molecular_function in core_functions, with electron transfer as the subunit-level MF.

## Review decisions

- GO:0036397 IDA/IBA/IEA, GO:0015944, GO:0009061, GO:0009326, GO:0043546, GO:0051539, GO:0042597 (Tat signal): ACCEPT.
- GO:0009055 IBA/IEA: KEEP_AS_NON_CORE (internal electron relay, secondary).
- GO:0016491, GO:0045333: TOO_GENERAL (GO:0036397, GO:0009061 entail them).
- GO:0008863 formate dehydrogenase (NAD+) and GO:0047111 (cytochrome-c-553) IEA from IPR006443: REMOVE, wrong InterPro2GO mappings for a quinone-linked FDH-N catalytic subunit.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000745948 | GO:0036397 formate dehydrogenase (quinone) activity | 3 | 16 (12 taxa) | GO:0036397, IDA, PMID:3038081 (PseudoCAP) | SOUND | Purified-complex FDH activity (dye assay) on the catalytic subunit; membrane nitrate-respiratory chain implies quinone linkage. Abstract only; gene attribution inferred (only FDH-N cluster in PAO1). Node term suits the FdnG/FdoG clade. | E. coli FdnG P24183 (IDA PMID:1099093), FdoG P32176 (IDA PMID:1504073) | Yes, on the two E. coli seeds |

The three FDH subunit nodes (PTN000745948 here, PTN001732897 on fdnH, PTN001247840 and PTN001247839 on fdnI) all get the same verdict, SOUND, with no defects. This gene, the catalytic subunit, holds the most direct evidence and keeps the shared rationale; fdnH and fdnI cross-reference it.
