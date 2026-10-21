# Source-record defects for UNIPROT

3 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IEA, GO_REF:0000117)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check the enables relation attached to this ARBA-derived GO:0005085 assertion. The authentic rule conclusion names the GO term without an explicit relation, so inheritance from a particular experimental enables row has not been demonstrated. Publication-backed UniProt SUBUNIT architecture and human reconstitution support a structural/regulatory contribution by delta to the exchange complex. A contributes_to relation may represent that scope more accurately. Positive delta assembly and ISRIB-pocket effects remain accepted; this is not a confirmed mapping error or a claim that enzyme subunits must function in isolation.

> 
> — PMID:29599213

> 
> — PMID:29599245

## 2. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check whether contributes_to better represents this GO:0005085 relation. PMID:25858979 directly perturbs hamster CHO Eif2b4 and measures whole-complex exchange and ISRIB response, while its supplementary Methods remain unavailable. Human structural/reconstitution evidence positively supports delta-mediated assembly and the ISRIB pocket. This is a query about the entity executing the complete exchange function, not rejection of delta participation, an isolation requirement, or a confirmed qualifier error.

> 
> — PMID:25858979

> 
> — PMID:29599213

> 
> — PMID:29599245

## 3. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check the enables relation for this source-specific GO:0005085 assertion. The inspected Methods and Results distinguish a S. pombe structural preparation from a human whole-complex translation comparator. Delta’s regulatory architecture and human interface-mutant data support a contribution to exchange. The present source scope does not independently assign the full exchange function to human delta, but neither does it demonstrate absence of such activity. Retain the imported relation pending curator assessment; this is a PROBABLE query, not a confirmed error.

> 
> — PMID:27023709

> 
> — PMID:29599213
