# fdnH (PA4811, Q9HUZ8) notes

Iron-sulfur (beta) electron-transfer subunit of the respiratory formate dehydrogenase FdnGHI. Four ferredoxin-type cysteine clusters (16 Cys ligands; PIRNR036298 "Binds 4 [4Fe-4S] clusters per subunit"), C-terminal TM anchor 256-273. Literature search as for fdnG (see genes/PSEAE/fdnG/fdnG-notes.md).

## Literature

- Godfrey et al. 1987 (PMID:3038081; abstract only, PMC1147836 is a scanned PDF with no text via the PubMed MCP): FDH purified from anaerobically nitrate-grown P. aeruginosa ["The purification of formate dehydrogenase (FDH) from Pseudomonas aeruginosa after anaerobic growth on nitrate-containing medium was carried out."], co-fractionating with nitrate reductase ["found together in a particle fraction and constitute the short respiratory chain of this bacterium"]. Activity assayed with Nitro Blue Tetrazolium (artificial acceptor). The purest preparation contains a bis-histidine cytochrome, a [4Fe-4S]+ cluster and molybdenum ["These techniques have allowed the haem, iron-sulphur clusters and molybdenum components to be detected"]; [3Fe-4S] and cytochrome c are contaminants removed with NiR.
- The paper predates the genome and does not assign polypeptides to genes. A UniProt query (organism 208964, protein name "formate dehydrogenase", 2026-11-05) returns only PA4810-PA4812, so the purified enzyme is attributed to FdnGHI; the cofactor set matches (FdnG Mo-bisMGD + [4Fe-4S], FdnH 4x[4Fe-4S], FdnI di-haem cytochrome b).
- QuickGO (2026-11-05), E. coli comparators: FdnG P24183, FdnH P0AAJ3 and FdnI P0AEK7 each carry GO:0036397 by IDA (EcoCyc, PMID:1099093); FdoG P32176 and FdoH P0AAJ5 by IDA (PMID:1504073). So the complex-level activity is annotated to every subunit by convention, from purified-complex biochemistry.

## Operon-level phenotype check

The brief asked whether the FDH subunits show the cbb3/ccoP error (an operon mutant phenotype annotated to each subunit activity). They do not: the PseudoCAP rows come from biochemistry of a purified complex, the same evidence type and convention EcoCyc uses for E. coli FdnGHI. The only caveats are (a) the dye assay does not show quinone as acceptor (quinone linkage is inferred from the membrane nitrate-respiratory chain), and (b) gene attribution is inferred. Neither makes the row wrong, so verdict SOUND, no PSEUDOCAP or GO_CENTRAL defect. For FdnH and FdnI the complex activity is recorded as contributes_to_molecular_function in core_functions, with electron transfer as the subunit-level MF.

## Review decisions

- GO:0036397 IDA/IBA/IEA, GO:0015944, GO:0009061, GO:0009326, GO:0051539, GO:0005886: ACCEPT.
- GO:0016020: MODIFY to GO:0005886. GO:0045333: TOO_GENERAL.
- NEW GO:0009055 electron transfer activity (ISS from E. coli FdnH P0AAJ3, IDA; PIRNR function text).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001732897 | GO:0036397 formate dehydrogenase (quinone) activity | 3 | 18 (11 taxa) | GO:0036397, IDA, PMID:3038081 (PseudoCAP) | SOUND | Purified-complex activity annotated to the beta subunit on the E. coli convention; not an operon mutant phenotype. Abstract only. Node term suits the FdnH/FdoH clade. | E. coli FdnH P0AAJ3 (IDA PMID:1099093), FdoH P0AAJ5 (IDA PMID:1504073) | Yes, on the two E. coli seeds |

Node-level reasoning for the FDH subunits is kept on fdnG (catalytic subunit); no PSEUDOCAP or GO_CENTRAL defect.
