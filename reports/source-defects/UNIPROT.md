# Source-record defects for UNIPROT

4 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P49770 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B2/EIF2B2-ai-review.yaml`

The experimentally attributed UniProt P49770 SUBUNIT annotation places alpha/beta/delta in the regulatory subcomplex and gamma/epsilon in the catalytic subcomplex, citing PMID:25858979, PMID:27023709 and PMID:31048492. Please check whether the UniProt relation for this GO:0005085 assertion should be contributes_to rather than enables. The inspected main text and captions measure whole-eIF2B GDP release and CHO Eif2b4 delta mutants; supplementary Methods and the exact purified-complex preparation remain unavailable. The accepted evidence supports EIF2B2 beta as a structural/regulatory participant in the exchange complex. GO relation guidance distinguishes execution by a gene product from contribution to a complex function that is not attributable to that subunit. This is a proposed relation correction, not rejection of GEF participation or a claim that an enzyme must function in isolation. The incomplete source-specific assay scope warrants a curator query rather than a confirmed error. The imported qualifier is preserved pending upstream assessment. The official architecture supports this query but does not by itself confirm an error in this specific annotation relation.

- **Evidence reference:** PMID:25858979

- **Evidence reference:** PMID:29599213

- **Evidence reference:** file:human/EIF2B2/EIF2B2-uniprot.txt

## 2. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P49770 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B2/EIF2B2-ai-review.yaml`

The experimentally attributed UniProt P49770 SUBUNIT annotation places alpha/beta/delta in the regulatory subcomplex and gamma/epsilon in the catalytic subcomplex, citing PMID:25858979, PMID:27023709 and PMID:31048492. Please check whether the UniProt relation for this GO:0005085 assertion should be contributes_to rather than enables. The inspected Methods and Results mainly concern S. pombe and include a human whole-complex translation comparator, not a subunit-specific exchange experiment. The accepted evidence supports EIF2B2 beta as a structural/regulatory participant in the exchange complex. GO relation guidance distinguishes execution by a gene product from contribution to a complex function that is not attributable to that subunit. This is a proposed relation correction, not rejection of GEF participation or a claim that an enzyme must function in isolation. The incomplete source-specific assay scope warrants a curator query rather than a confirmed error. The imported qualifier is preserved pending upstream assessment. The official architecture supports this query but does not by itself confirm an error in this specific annotation relation.

- **Evidence reference:** PMID:27023709

- **Evidence reference:** PMID:29599213

- **Evidence reference:** file:human/EIF2B2/EIF2B2-uniprot.txt

## 3. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9NR50 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B3/EIF2B3-ai-review.yaml`

Please check the gene-product relation on UniProtKB:Q9NR50!238451548 for EIF2B3/Q9NR50, GO:0005085, PMID:25858979. The independently assessed study measures GDP exchange by whole eIF2B and does not resolve an isolated gamma exchange reaction; exact gamma construct details and the unread Table S1 exception remain bounded. Human gamma binds epsilon and supports assembly of the active complex, so its catalytic-subcomplex role is substantial and the biological function is retained. The available evidence favors contributes_to rather than assigning the exchange reaction to gamma individually. This is a query, not proof that gamma has no direct contribution or an instruction to remove the annotation; retain enables if additional source evidence establishes individual execution.

- **Evidence reference:** PMID:25858979

- **Evidence reference:** PMID:15060152

- **Evidence reference:** PMID:29599213

## 4. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9NR50 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B3/EIF2B3-ai-review.yaml`

Please check the gene-product relation on UniProtKB:Q9NR50!238451549 for EIF2B3/Q9NR50, GO:0005085, PMID:27023709. The original Methods and Figure 2h demonstrate a human whole-eIF2B translation comparator; its gamma-epsilon subcomplex expression and structural preparation are S. pombe. They do not resolve an isolated human gamma exchange reaction. Human gamma binds epsilon and supports assembly of the active complex, so its catalytic-subcomplex role is substantial and the biological function is retained. The available evidence favors contributes_to rather than assigning the exchange reaction to gamma individually. This is a query, not proof that gamma has no direct contribution or an instruction to remove the annotation; retain enables if additional source evidence establishes individual execution.

- **Evidence reference:** PMID:27023709

- **Evidence reference:** PMID:15060152

- **Evidence reference:** PMID:29599213
