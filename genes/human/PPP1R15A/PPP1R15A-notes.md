# PPP1R15A (GADD34) review notes

## Literature search (no deep-research provider available)
Sources checked: UniProt O75807 (curated FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, INTRAMEM/REGION features);
all 16 GOA-cited PMIDs cached via `just fetch-gene-pmids`. Context only: integrated stress response module
(gadd34_pp1_regulator annoton: GO:0019888, GO:0036496, cytosol) (module proposed in ai4curation/ai-gene-review#5904).

## Key findings
- Holophosphatase: [PMID:11381086 "GADD34 formed a complex with the catalytic subunit of protein phosphatase 1 (PP1c) that specifically promoted the dephosphorylation of eIF2alpha in vitro."]
- Substrate redirection: [PMID:11564868 "While GADD34 inhibited PP1-catalyzed dephosphorylation of phosphorylase a, the GADD34-bound PP1 was an active eIF-2alpha phosphatase."]
- Scaffold: [PMID:26095357 "The data highlight independent interactions of PP1 and eIF2α with GADD34, demonstrating that GADD34 functions as a scaffold both in vitro and in cells."]
- ER membrane: [PMID:21518769 "Fluorescence protease protection and chemical modification of cysteines substituted in the membrane-binding domain pointed to a monotopic insertion of GADD34 into the outer layer of the ER membrane."]
- Influenza restriction: [PMID:41747053 "Among these NSGs, growth arrest and DNA damage-inducible protein 34 (GADD34) was crucial for IAV restriction."] (abstract only)

## Source defect found
DisProt IPI rows from PMID:34847777 (GO:0000164, GO:0071074) list UniProtKB:Q9BY44 = EIF2A (eIF-2A) as WITH/FROM;
the paper's substrate is Ser51-phosphorylated eIF2alpha = EIF2S1 (P05198). Recorded as WRONG_WITH_FROM / SYMBOL_COLLISION.
The same defect affects PPP1R15B rows (PMID:34847777, PMID:38159565).

## Decisions
- molecular adaptor activity -> enzyme-substrate adaptor activity (GO:0140767).
- protein phosphatase activator activity -> parent regulator activity (GADD34 inhibits PP1 toward other substrates).
- regulation of translational initiation (in response to stress) -> GO:0036496 (by eIF2 alpha dephosphorylation).
- Golgi apparatus IDA left UNDECIDED (abstract silent; no UniProt Golgi location).
