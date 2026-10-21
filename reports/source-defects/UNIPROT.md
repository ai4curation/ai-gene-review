# Source-record defects for UNIPROT

2 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P49770 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B2/EIF2B2-ai-review.yaml`

The experimentally attributed UniProt P49770 SUBUNIT annotation places alpha/beta/delta in the regulatory subcomplex and gamma/epsilon in the catalytic subcomplex, citing PMID:25858979, PMID:27023709 and PMID:31048492. Please check whether the UniProt relation for this GO:0005085 assertion should be contributes_to rather than enables. The inspected main text and captions measure whole-eIF2B GDP release and CHO Eif2b4 delta mutants; supplementary Methods and the exact purified-complex preparation remain unavailable. The accepted evidence supports EIF2B2 beta as a structural/regulatory participant in the exchange complex. GO relation guidance distinguishes execution by a gene product from contribution to a complex function that is not attributable to that subunit. This is a proposed relation correction, not rejection of GEF participation or a claim that an enzyme must function in isolation. The incomplete source-specific assay scope warrants a curator query rather than a confirmed error. The imported qualifier is preserved pending upstream assessment. The official architecture supports this query but does not by itself confirm an error in this specific annotation relation.

> 
> — PMID:25858979

> 
> — PMID:29599213

> 
> — file:human/EIF2B2/EIF2B2-uniprot.txt

## 2. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P49770 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B2/EIF2B2-ai-review.yaml`

The experimentally attributed UniProt P49770 SUBUNIT annotation places alpha/beta/delta in the regulatory subcomplex and gamma/epsilon in the catalytic subcomplex, citing PMID:25858979, PMID:27023709 and PMID:31048492. Please check whether the UniProt relation for this GO:0005085 assertion should be contributes_to rather than enables. The inspected Methods and Results mainly concern S. pombe and include a human whole-complex translation comparator, not a subunit-specific exchange experiment. The accepted evidence supports EIF2B2 beta as a structural/regulatory participant in the exchange complex. GO relation guidance distinguishes execution by a gene product from contribution to a complex function that is not attributable to that subunit. This is a proposed relation correction, not rejection of GEF participation or a claim that an enzyme must function in isolation. The incomplete source-specific assay scope warrants a curator query rather than a confirmed error. The imported qualifier is preserved pending upstream assessment. The official architecture supports this query but does not by itself confirm an error in this specific annotation relation.

> 
> — PMID:27023709

> 
> — PMID:29599213

> 
> — file:human/EIF2B2/EIF2B2-uniprot.txt
