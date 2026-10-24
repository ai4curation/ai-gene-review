# Source-record defects for UNIPROT

10 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

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

## 5. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IEA, GO_REF:0000117)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check the enables relation attached to this ARBA-derived GO:0005085 assertion. The authentic rule conclusion names the GO term without an explicit relation, so inheritance from a particular experimental enables row has not been demonstrated. Publication-backed UniProt SUBUNIT architecture and human reconstitution support a structural/regulatory contribution by delta to the exchange complex. A contributes_to relation may represent that scope more accurately. Positive delta assembly and ISRIB-pocket effects remain accepted; this is not a confirmed mapping error or a claim that enzyme subunits must function in isolation.

- **Evidence reference:** PMID:29599213

- **Evidence reference:** PMID:29599245

## 6. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check whether contributes_to better represents this GO:0005085 relation. PMID:25858979 directly perturbs hamster CHO Eif2b4 and measures whole-complex exchange and ISRIB response, while its supplementary Methods remain unavailable. Human structural/reconstitution evidence positively supports delta-mediated assembly and the ISRIB pocket. This is a query about the entity executing the complete exchange function, not rejection of delta participation, an isolation requirement, or a confirmed qualifier error.

- **Evidence reference:** PMID:25858979

- **Evidence reference:** PMID:29599213

- **Evidence reference:** PMID:29599245

## 7. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check the enables relation for this source-specific GO:0005085 assertion. The inspected Methods and Results distinguish a S. pombe structural preparation from a human whole-complex translation comparator. Delta’s regulatory architecture and human interface-mutant data support a contribution to exchange. The present source scope does not independently assign the full exchange function to human delta, but neither does it demonstrate absence of such activity. Retain the imported relation pending curator assessment; this is a PROBABLE query, not a confirmed error.

- **Evidence reference:** PMID:27023709

- **Evidence reference:** PMID:29599213

## 8. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q99607 located_in GO:0016605 PML body (IDA, PMID:14970218)
- **Field:** DB:Reference
- **Change:** check PMID:14970218 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELF4/ELF4-ai-review.yaml`

Please check the reference supporting this ELF4 PML-body location assertion. The inspected indexed original PMID14970218 contains genuine MEF–AML1 association, while its operative reporter experiments concern NERF2; no PML text was found in that indexed original. PMID14976184 contains direct human MEF/PML localization and lysozyme promoter activation. The proposed replacement is conditional on the curator’s complete source record; this is not a wrong-gene claim, a confirmed absence from every unavailable supplement, or an inferred cause of miscitation. Biological annotation and imported reference are preserved.

- **Evidence reference:** PMID:14970218

- **Evidence reference:** PMID:14976184

## 9. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q99607 involved_in GO:0045944 positive regulation of transcription by RNA polymerase II (IDA, PMID:14970218)
- **Field:** DB:Reference
- **Change:** check PMID:14970218 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELF4/ELF4-ai-review.yaml`

Please check the reference supporting this ELF4 positive polymerase-II transcription assertion. The inspected indexed original PMID14970218 contains genuine MEF–AML1 association, but its operative BLK-promoter transactivation experiments concern NERF2/ELF2. PMID14976184 instead reports MEF-dependent lysozyme-promoter activation enhanced by PML and increased endogenous lysozyme RNA. The proposed replacement is conditional on the curator’s complete source record; this is not a wrong-gene claim, a confirmed absence from every unavailable supplement, or an inferred cause of miscitation. Biological annotation and imported reference are preserved.

- **Evidence reference:** PMID:14970218

- **Evidence reference:** PMID:14976184

## 10. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P30793  GO:0003924 GTPase activity (IDA, PMID:2463916)
- **Field:** GO_ID
- **Change:** GO:0003924 → GO:0003934 (GTP cyclohydrolase I activity)
- **Recorded in:** `genes/human/GCH1/GCH1-ai-review.yaml`

This IDA row (PMID:2463916, assigned by UniProt) gives GCH1 GTPase activity (GTP + H2O = GDP + phosphate). The paper purifies GTP cyclohydrolase I, which converts GTP to 7,8-dihydroneopterin 3'-triphosphate and formate and produces no GDP. The evidence supports GO:0003934 GTP cyclohydrolase I activity instead.
