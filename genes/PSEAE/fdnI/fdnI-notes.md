# fdnI (PA4810, Q9HUZ9) notes

Di-haem cytochrome b556 (gamma) membrane subunit of the respiratory formate dehydrogenase FdnGHI; four TM helices (21-41, 53-74, 113-133, 153-174), Pfam Ni_hydr_CYTB, IPR016174 Di-haem_cyt_TM. Literature search as for fdnG (see genes/PSEAE/fdnG/fdnG-notes.md).

## Literature

- Godfrey et al. 1987 (PMID:3038081; abstract only, PMC1147836 is a scanned PDF with no text via the PubMed MCP): FDH purified from anaerobically nitrate-grown P. aeruginosa ["The purification of formate dehydrogenase (FDH) from Pseudomonas aeruginosa after anaerobic growth on nitrate-containing medium was carried out."], co-fractionating with nitrate reductase ["found together in a particle fraction and constitute the short respiratory chain of this bacterium"]. Activity assayed with Nitro Blue Tetrazolium (artificial acceptor). The purest preparation contains a bis-histidine cytochrome, a [4Fe-4S]+ cluster and molybdenum ["These techniques have allowed the haem, iron-sulphur clusters and molybdenum components to be detected"]; [3Fe-4S] and cytochrome c are contaminants removed with NiR.
- The paper predates the genome and does not assign polypeptides to genes. A UniProt query (organism 208964, protein name "formate dehydrogenase", 2026-11-05) returns only PA4810-PA4812, so the purified enzyme is attributed to FdnGHI; the cofactor set matches (FdnG Mo-bisMGD + [4Fe-4S], FdnH 4x[4Fe-4S], FdnI di-haem cytochrome b).
- QuickGO (2026-11-05), E. coli comparators: FdnG P24183, FdnH P0AAJ3 and FdnI P0AEK7 each carry GO:0036397 by IDA (EcoCyc, PMID:1099093); FdoG P32176 and FdoH P0AAJ5 by IDA (PMID:1504073). So the complex-level activity is annotated to every subunit by convention, from purified-complex biochemistry.

## Operon-level phenotype check

The brief asked whether the FDH subunits show the cbb3/ccoP error (an operon mutant phenotype annotated to each subunit activity). They do not: the PseudoCAP rows come from biochemistry of a purified complex, the same evidence type and convention EcoCyc uses for E. coli FdnGHI. The only caveats are (a) the dye assay does not show quinone as acceptor (quinone linkage is inferred from the membrane nitrate-respiratory chain), and (b) gene attribution is inferred. Neither makes the row wrong, so verdict SOUND, no PSEUDOCAP or GO_CENTRAL defect. For FdnH and FdnI the complex activity is recorded as contributes_to_molecular_function in core_functions, with electron transfer as the subunit-level MF.

## Review decisions

- GO:0036397 IDA/IBA, GO:0015944, GO:0009061, GO:0009326, GO:0005886, GO:0009055, GO:0022904: ACCEPT.
- GO:0016020: MODIFY to GO:0005886. GO:0045333: TOO_GENERAL.
- GO:0008863 formate dehydrogenase (NAD+) IEA (IPR006471): REMOVE, wrong mapping for a membrane cytochrome b subunit.
- NEW GO:0020037 heme binding (ISS; E. coli FdnI IDA; bis-His haem in purified FDH).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001247840 | GO:0036397 formate dehydrogenase (quinone) activity | 2 | 14 (9 taxa) | GO:0036397, IDA, PMID:3038081 (PseudoCAP) | SOUND | Purified-complex activity annotated to the cytochrome b subunit (the quinone-reducing site) on the E. coli convention; not an operon mutant phenotype. Abstract only. Node term suits the FdnI/FdoI clade. | E. coli FdnI P0AEK7 (IDA PMID:1099093) | Yes, on E. coli FdnI |
| PTN001247839 | GO:0016491 oxidoreductase activity | 2 | 5 (4 taxa) | GO:0036397, IDA, PMID:3038081 (PseudoCAP; descendant of the node term) | SOUND | Same seed row; the general node term is entailed by GO:0036397. The term is broad for a cytochrome b clade that also holds hydrogenase HybB, but not wrong for a clade of redox-complex membrane subunits. fdnI itself has no GO:0016491 IBA row (it carries the more specific term). | E. coli FdnI P0AEK7 (IDA GO:0036397, a descendant) | Yes, on E. coli FdnI |

Node-level reasoning for the FDH subunits is kept on fdnG; no PSEUDOCAP or GO_CENTRAL defect.
