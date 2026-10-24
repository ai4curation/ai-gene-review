# Source-record defects for UNIPROT

32 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P13945 enables GO:0003925 G protein activity (IEA, GO_REF:0000120)
- **Field:** With/From
- **Change:** check ARBA:ARBA00088750 (alternatives in the explanation)
- **Recorded in:** `genes/human/ADRB3/ADRB3-ai-review.yaml`

This combined IEA (GO_REF:0000120) to GO:0003925 G protein activity cites ARBA00088750 plus Ensembl Compara transfer from rat Adrb3 (P26255/ENSRNOP00000016907). The orthology arm only re-propagates the erroneous UniProt IDA from PMID:10207024 on the rodent orthologs, and will disappear when those are corrected. ARBA00088750 annotates GO:0003925, and all of its current condition sets require a Gene3D 3.40.50.300 (P-loop NTPase) FunFam, which ADRB3 lacks (Gene3D 1.20.1070.10 only); please check why the rule is credited for a GPCR and whether an earlier rule version was trained on the receptor IDA rows. The row should be deleted.

## 2. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P13945 enables GO:0003925 G protein activity (IDA, PMID:10207024)
- **Field:** GO_ID
- **Change:** GO:0003925 → GO:0015052 (beta3-adrenergic receptor activity)
- **Recorded in:** `genes/human/ADRB3/ADRB3-ai-review.yaml`

This IDA row (PMID:10207024, assigned by UniProt) gives the beta3-adrenergic receptor GO:0003925 G protein activity, a GTPase-activity child that describes the G protein itself. The paper shows agonist-stimulated 8-azido-GTP labelling of Galpha-s and Galpha-i, i.e. the receptor promoting GDP/GTP exchange on its G proteins, which is G protein-coupled receptor activity. ADRB3 has no GTPase domain. Repoint to GO:0015052 beta3-adrenergic receptor activity (or GO:0004930); since an IDA row to GO:0015052 from this paper already exists, deleting the row is equivalent.

> CL316,243 (5 microM) stimulated the incorporation of 8-azido-[32P]GTP into Galphas (1.57 +/- 0.12; n = 3) and Galphai (1. 68 +/- 0.13; n = 4) in adipocyte plasma membranes, directly demonstrating that beta3AR stimulation results in Gi-GTP exchange
> — PMID:10207024

## 3. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P25962
- **Subject:** UniProtKB:P13945
- **Field:** GO_ID
- **Change:** GO:0003925 → GO:0015052 (beta3-adrenergic receptor activity)
- **Recorded in:** `genes/human/ADRB3/ADRB3-ai-review.yaml`

The same UniProt IDA to GO:0003925 G protein activity from PMID:10207024 is on mouse Adrb3 (P25962) and propagates by ISO (GO_Central, GO_REF:0000096/0000119) and Ensembl Compara. It has the same defect: the paper shows the receptor stimulating GTP exchange on Galpha-s/Galpha-i (receptor activity), not G protein activity.

## 4. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P26255
- **Subject:** UniProtKB:P13945
- **Field:** GO_ID
- **Change:** GO:0003925 → GO:0015052 (beta3-adrenergic receptor activity)
- **Recorded in:** `genes/human/ADRB3/ADRB3-ai-review.yaml`

The same UniProt IDA to GO:0003925 G protein activity from PMID:10207024 is on rat Adrb3 (P26255); it is the ortholog source (ENSRNOP00000016907) of the human GO_REF:0000120 IEA row and is propagated by RGD ISO. Same defect as on human P13945.

## 5. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P52566 located_in GO:0005856 cytoskeleton (TAS, PMID:16130169)
- **Field:** DB:Reference
- **Change:** delete the record asserting PMID:16130169
- **Recorded in:** `genes/human/ARHGDIB/ARHGDIB-ai-review.yaml`

TAS annotation of ARHGDIB (P52566) to cytoskeleton (GO:0005856) citing a HUVEC two-dimensional gel proteome. The paper lists identified proteins by functional category (e.g. cell motility) but does not localize ARHGDIB, and RhoGDI2 is a soluble cytosolic protein that regulates actin indirectly via Rho GTPases. No source supports a cytoskeletal location; the row should be deleted.

> illustrates various cellular functions more related to cell motility and angiogenesis
> — PMID:16130169

## 6. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 located_in GO:0000139 Golgi membrane (NAS, PMID:11514575)
- **Field:** DB:Reference
- **Change:** check PMID:11514575 (alternatives in the explanation)
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 (Kitagawa et al. 2001) cloned human chondroitin synthase, an 802-aa protein encoded on chromosome 15 (CHSY1, Q86X52). CSGALNACT1 (Q8TDX6) is a 532-aa protein encoded on chromosome 8. It was first cloned in PMID:11788602, which used the chondroitin synthase as the homology query. Q8TDX6's Golgi membrane location is correct but should cite PMID:11788602, or the row should be moved to Q86X52.

## 7. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 enables GO:0008376 acetylgalactosaminyltransferase activity (ISS, PMID:11788602)
- **Field:** Evidence_Code
- **Change:** check ECO:0000250 (alternatives in the explanation)
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11788602 (Uyama et al. 2002) cloned and assayed CSGALNACT1 itself: 532 aa, type II topology, chromosome 8, expressed in COS-1 cells. The four ISS rows on Q8TDX6 citing this paper with WITH UniProtKB:Q8N6G5 (CSGALNACT2) look like direct-assay evidence, which would be IDA without a WITH value. Please check whether the rows were meant for Q8N6G5 or should be IDA on Q8TDX6.

## 8. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 enables GO:0008376 acetylgalactosaminyltransferase activity (IDA, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:Q8TDX6 (alternatives in the explanation)
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 expressed and assayed human chondroitin synthase, an 802-aa protein encoded on chromosome 15 (CHSY1, Q86X52). It did not assay CSGALNACT1 (Q8TDX6, 532 aa, chromosome 8), which was cloned only later (PMID:11788602). The GalNAc-transferase activity in this paper belongs to CHSY1. CSGALNACT1 does have this activity, but the evidence is PMID:11788602 and PMID:12163485. Move the row to Q86X52 or re-cite it.

## 9. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 enables GO:0008955 peptidoglycan glycosyltransferase activity (IDA, PMID:11514575)
- **Field:** GO_ID
- **Change:** GO:0008955 → GO:0047238 (glucuronosyl-N-acetylgalactosaminyl-proteoglycan 4-beta-N-acetylgalactosaminyltransferase activity)
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

GO:0008955 peptidoglycan glycosyltransferase activity is the bacterial lipid II polymerisation reaction. PMID:11514575 measured transfer of GalNAc (and GlcA) from UDP-sugars onto polymer chondroitin, a vertebrate glycosaminoglycan. The GalNAc transfer onto chondroitin is GO:0047238; the GlcA transfer is GO:0050510. Peptidoglycan is not involved.

## 10. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 enables GO:0008955 peptidoglycan glycosyltransferase activity (IDA, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** delete the record asserting UniProtKB:Q8TDX6
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 describes an 802-aa chromosome-15 chondroitin synthase (CHSY1, Q86X52), not CSGALNACT1 (Q8TDX6, 532 aa, chromosome 8). Q86X52 already carries the corrected activities from this paper (GO:0047238 and GO:0050510 IDA), so this Q8TDX6 row should be deleted rather than moved.

## 11. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 involved_in GO:0015012 heparan sulfate proteoglycan biosynthetic process (NAS, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** delete the record asserting UniProtKB:Q8TDX6
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 is about chondroitin synthase (CHSY1, Q86X52, 802 aa, chromosome 15), not CSGALNACT1. It only compares that enzyme to the heparan sulfate polymerases. Neither protein synthesises heparan sulfate, so the row should be deleted rather than moved.

## 12. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 enables GO:0015020 glucuronosyltransferase activity (IDA, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:Q8TDX6 → UniProtKB:Q86X52 (CHSY1, chondroitin sulfate synthase 1)
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

The GlcUA-transferase activity in PMID:11514575 was measured for chondroitin synthase (CHSY1, Q86X52; 802 aa, chromosome 15). CSGALNACT1 (Q8TDX6) was not studied in that paper and has only GalNAc-transferase activity. Q86X52 already carries the more specific GO:0050510 from this paper.

## 13. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 involved_in GO:0019276 obsolete UDP-N-acetylgalactosamine metabolic process (IDA, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** delete the record asserting UniProtKB:Q8TDX6
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 studied chondroitin synthase (CHSY1, Q86X52), not CSGALNACT1. The process term also only reflects donor-substrate use. Delete the row.

## 14. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 involved_in GO:0030210 heparin proteoglycan biosynthetic process (NAS, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** delete the record asserting UniProtKB:Q8TDX6
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 is about chondroitin synthase (CHSY1), not CSGALNACT1, and supports heparin biosynthesis for neither protein.

## 15. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 involved_in GO:0046398 UDP-glucuronate metabolic process (IDA, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** delete the record asserting UniProtKB:Q8TDX6
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 studied chondroitin synthase (CHSY1, Q86X52), not CSGALNACT1. The process term reflects only donor-substrate use. Delete the row.

## 16. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q8TDX6 involved_in GO:0050650 chondroitin sulfate proteoglycan biosynthetic process (IDA, PMID:11514575)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:Q8TDX6 (alternatives in the explanation)
- **Recorded in:** `genes/human/CSGALNACT1/CSGALNACT1-ai-review.yaml`

PMID:11514575 assayed chondroitin synthase (CHSY1, Q86X52), not CSGALNACT1. CSGALNACT1's involvement in CS proteoglycan biosynthesis is true but should cite PMID:11788602 or PMID:12163485. The row as written belongs on Q86X52, which already carries it.

## 17. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P49770 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B2/EIF2B2-ai-review.yaml`

The experimentally attributed UniProt P49770 SUBUNIT annotation places alpha/beta/delta in the regulatory subcomplex and gamma/epsilon in the catalytic subcomplex, citing PMID:25858979, PMID:27023709 and PMID:31048492. Please check whether the UniProt relation for this GO:0005085 assertion should be contributes_to rather than enables. The inspected main text and captions measure whole-eIF2B GDP release and CHO Eif2b4 delta mutants; supplementary Methods and the exact purified-complex preparation remain unavailable. The accepted evidence supports EIF2B2 beta as a structural/regulatory participant in the exchange complex. GO relation guidance distinguishes execution by a gene product from contribution to a complex function that is not attributable to that subunit. This is a proposed relation correction, not rejection of GEF participation or a claim that an enzyme must function in isolation. The incomplete source-specific assay scope warrants a curator query rather than a confirmed error. The imported qualifier is preserved pending upstream assessment. The official architecture supports this query but does not by itself confirm an error in this specific annotation relation.

- **Evidence reference:** PMID:25858979

- **Evidence reference:** PMID:29599213

- **Evidence reference:** file:human/EIF2B2/EIF2B2-uniprot.txt

## 18. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P49770 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B2/EIF2B2-ai-review.yaml`

The experimentally attributed UniProt P49770 SUBUNIT annotation places alpha/beta/delta in the regulatory subcomplex and gamma/epsilon in the catalytic subcomplex, citing PMID:25858979, PMID:27023709 and PMID:31048492. Please check whether the UniProt relation for this GO:0005085 assertion should be contributes_to rather than enables. The inspected Methods and Results mainly concern S. pombe and include a human whole-complex translation comparator, not a subunit-specific exchange experiment. The accepted evidence supports EIF2B2 beta as a structural/regulatory participant in the exchange complex. GO relation guidance distinguishes execution by a gene product from contribution to a complex function that is not attributable to that subunit. This is a proposed relation correction, not rejection of GEF participation or a claim that an enzyme must function in isolation. The incomplete source-specific assay scope warrants a curator query rather than a confirmed error. The imported qualifier is preserved pending upstream assessment. The official architecture supports this query but does not by itself confirm an error in this specific annotation relation.

- **Evidence reference:** PMID:27023709

- **Evidence reference:** PMID:29599213

- **Evidence reference:** file:human/EIF2B2/EIF2B2-uniprot.txt

## 19. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9NR50 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B3/EIF2B3-ai-review.yaml`

Please check the gene-product relation on UniProtKB:Q9NR50!238451548 for EIF2B3/Q9NR50, GO:0005085, PMID:25858979. The independently assessed study measures GDP exchange by whole eIF2B and does not resolve an isolated gamma exchange reaction; exact gamma construct details and the unread Table S1 exception remain bounded. Human gamma binds epsilon and supports assembly of the active complex, so its catalytic-subcomplex role is substantial and the biological function is retained. The available evidence favors contributes_to rather than assigning the exchange reaction to gamma individually. This is a query, not proof that gamma has no direct contribution or an instruction to remove the annotation; retain enables if additional source evidence establishes individual execution.

- **Evidence reference:** PMID:25858979

- **Evidence reference:** PMID:15060152

- **Evidence reference:** PMID:29599213

## 20. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9NR50 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B3/EIF2B3-ai-review.yaml`

Please check the gene-product relation on UniProtKB:Q9NR50!238451549 for EIF2B3/Q9NR50, GO:0005085, PMID:27023709. The original Methods and Figure 2h demonstrate a human whole-eIF2B translation comparator; its gamma-epsilon subcomplex expression and structural preparation are S. pombe. They do not resolve an isolated human gamma exchange reaction. Human gamma binds epsilon and supports assembly of the active complex, so its catalytic-subcomplex role is substantial and the biological function is retained. The available evidence favors contributes_to rather than assigning the exchange reaction to gamma individually. This is a query, not proof that gamma has no direct contribution or an instruction to remove the annotation; retain enables if additional source evidence establishes individual execution.

- **Evidence reference:** PMID:27023709

- **Evidence reference:** PMID:15060152

- **Evidence reference:** PMID:29599213

## 21. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IEA, GO_REF:0000117)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check the enables relation attached to this ARBA-derived GO:0005085 assertion. The authentic rule conclusion names the GO term without an explicit relation, so inheritance from a particular experimental enables row has not been demonstrated. Publication-backed UniProt SUBUNIT architecture and human reconstitution support a structural/regulatory contribution by delta to the exchange complex. A contributes_to relation may represent that scope more accurately. Positive delta assembly and ISRIB-pocket effects remain accepted; this is not a confirmed mapping error or a claim that enzyme subunits must function in isolation.

- **Evidence reference:** PMID:29599213

- **Evidence reference:** PMID:29599245

## 22. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:25858979)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check whether contributes_to better represents this GO:0005085 relation. PMID:25858979 directly perturbs hamster CHO Eif2b4 and measures whole-complex exchange and ISRIB response, while its supplementary Methods remain unavailable. Human structural/reconstitution evidence positively supports delta-mediated assembly and the ISRIB pocket. This is a query about the entity executing the complete exchange function, not rejection of delta participation, an isolation requirement, or a confirmed qualifier error.

- **Evidence reference:** PMID:25858979

- **Evidence reference:** PMID:29599213

- **Evidence reference:** PMID:29599245

## 23. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UI10 enables GO:0005085 guanyl-nucleotide exchange factor activity (IDA, PMID:27023709)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EIF2B4/EIF2B4-ai-review.yaml`

Please check the enables relation for this source-specific GO:0005085 assertion. The inspected Methods and Results distinguish a S. pombe structural preparation from a human whole-complex translation comparator. Delta’s regulatory architecture and human interface-mutant data support a contribution to exchange. The present source scope does not independently assign the full exchange function to human delta, but neither does it demonstrate absence of such activity. Retain the imported relation pending curator assessment; this is a PROBABLE query, not a confirmed error.

- **Evidence reference:** PMID:27023709

- **Evidence reference:** PMID:29599213

## 24. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q99607 located_in GO:0016605 PML body (IDA, PMID:14970218)
- **Field:** DB:Reference
- **Change:** check PMID:14970218 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELF4/ELF4-ai-review.yaml`

Please check the reference supporting this ELF4 PML-body location assertion. The inspected indexed original PMID14970218 contains genuine MEF–AML1 association, while its operative reporter experiments concern NERF2; no PML text was found in that indexed original. PMID14976184 contains direct human MEF/PML localization and lysozyme promoter activation. The proposed replacement is conditional on the curator’s complete source record; this is not a wrong-gene claim, a confirmed absence from every unavailable supplement, or an inferred cause of miscitation. Biological annotation and imported reference are preserved.

- **Evidence reference:** PMID:14970218

- **Evidence reference:** PMID:14976184

## 25. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q99607 involved_in GO:0045944 positive regulation of transcription by RNA polymerase II (IDA, PMID:14970218)
- **Field:** DB:Reference
- **Change:** check PMID:14970218 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELF4/ELF4-ai-review.yaml`

Please check the reference supporting this ELF4 positive polymerase-II transcription assertion. The inspected indexed original PMID14970218 contains genuine MEF–AML1 association, but its operative BLK-promoter transactivation experiments concern NERF2/ELF2. PMID14976184 instead reports MEF-dependent lysozyme-promoter activation enhanced by PML and increased endogenous lysozyme RNA. The proposed replacement is conditional on the curator’s complete source record; this is not a wrong-gene claim, a confirmed absence from every unavailable supplement, or an inferred cause of miscitation. Biological annotation and imported reference are preserved.

- **Evidence reference:** PMID:14970218

- **Evidence reference:** PMID:14976184

## 26. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P30793  GO:0003924 GTPase activity (IDA, PMID:2463916)
- **Field:** GO_ID
- **Change:** GO:0003924 → GO:0003934 (GTP cyclohydrolase I activity)
- **Recorded in:** `genes/human/GCH1/GCH1-ai-review.yaml`

This IDA row (PMID:2463916, assigned by UniProt) gives GCH1 GTPase activity (GTP + H2O = GDP + phosphate). The paper purifies GTP cyclohydrolase I, which converts GTP to 7,8-dihydroneopterin 3'-triphosphate and formate and produces no GDP. The evidence supports GO:0003934 GTP cyclohydrolase I activity instead.

## 27. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q99527 enables GO:0030284 nuclear estrogen receptor activity (IDA, PMID:15539556)
- **Field:** GO_ID
- **Change:** GO:0030284 → GO:0038054 (G protein-coupled estrogen receptor activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/human/GPER1/GPER1-ai-review.yaml`

The PMID:15539556 IDA annotation of GPER1 (Q99527) to GO:0030284 nuclear estrogen receptor activity uses a term defined as a nuclear receptor (DNA-binding transcription factor) activity. GPER1 is a seven-transmembrane class A GPCR with no DNA-binding domain, and the paper reports estrogen binding coupled to G-protein signaling. The correct term is GO:0038054 G protein-coupled estrogen receptor activity, which GPER1 already carries by ISS.

> GPR30, an orphan receptor unrelated to nuclear estrogen receptors, has all the binding and signaling characteristics of a mER
> — PMID:15539556

## 28. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q99527 enables GO:0030284 nuclear estrogen receptor activity (IDA, PMID:15705806)
- **Field:** GO_ID
- **Change:** GO:0030284 → GO:0038054 (G protein-coupled estrogen receptor activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/human/GPER1/GPER1-ai-review.yaml`

The PMID:15705806 IDA annotation of GPER1 (Q99527) to GO:0030284 nuclear estrogen receptor activity uses a term defined as a nuclear receptor (DNA-binding transcription factor) activity. GPER1 is a seven-transmembrane class A GPCR with no DNA-binding domain, and the paper reports estrogen binding coupled to G-protein signaling. The correct term is GO:0038054 G protein-coupled estrogen receptor activity, which GPER1 already carries by ISS.

> GPR30 is uniquely localized to the endoplasmic reticulum, where it specifically binds estrogen and fluorescent estrogen derivatives
> — PMID:15705806

## 29. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q99527 involved_in GO:0032962 positive regulation of inositol trisphosphate biosynthetic process (IDA, PMID:15705806)
- **Field:** GO_ID
- **Change:** check GO:0032962 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/human/GPER1/GPER1-ai-review.yaml`

PMID:15705806 (Revankar et al. 2005) reports GPR30-dependent synthesis of phosphatidylinositol 3,4,5-trisphosphate (PIP3) in the nucleus. The annotation uses GO:0032962 positive regulation of inositol trisphosphate biosynthetic process, which refers to soluble IP3. Unless the full text also measured IP3, the term appears to confuse PIP3 with IP3; the PI3K output is already annotated as GO:0051897 from the same paper.

> Activating GPR30 by estrogen resulted in intracellular calcium mobilization and synthesis of phosphatidylinositol 3,4,5-trisphosphate in the nucleus
> — PMID:15705806

## 30. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UQL6 enables GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding (IDA, PMID:24413532)
- **Field:** GO_ID
- **Change:** check GO:0000978 (alternatives in the explanation)
- **Recorded in:** `genes/human/HDAC5/HDAC5-ai-review.yaml`

This IDA row gives HDAC5 RNA polymerase II cis-regulatory region sequence-specific DNA binding from PMID:24413532, where class II HDACs act within MTA1 complexes recruited to the ESR1 regulatory region by TFAP2C or IFI16. HDAC5 has no DNA-binding domain; promoter occupancy reflects recruitment by DNA-binding partners. A coregulator term (GO:0003712, or a corepressor/coactivator child depending on context in the full text) fits; if only occupancy was shown, a chromatin localization annotation may be preferable.

> Importantly, class II HDACs are involved in the MTA1-mediated differential regulation of ERα.
> — PMID:24413532

## 31. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O88559
- **Subject:** UniProtKB:O00255
- **Field:** GO_ID
- **Change:** GO:0001216 → GO:0003713 (transcription coactivator activity)
- **Recorded in:** `genes/human/MEN1/MEN1-ai-review.yaml`

Mouse menin (O88559) carries GO:0001216 DNA-binding transcription activator activity, IDA, PMID:14992727, assigned by UniProt; Ensembl Compara projects it to human O00255. PMID:14992727 shows menin co-purifying with an MLL2/Ash2L H3K4 methyltransferase complex, binding to the Hoxc8 locus by ChIP, and loss of Hoxc6/Hoxc8 expression in Men1-null cells; it does not show sequence-specific DNA binding by menin. Menin binds DNA only sequence-independently (PMID:15331604) and acts as a coactivator/scaffold that brings MLL methyltransferase activity to target genes. GO:0003713 transcription coactivator activity (or GO:0030674 protein-macromolecule adaptor activity) fits the evidence.

> menin activates the transcription of differentiation-regulating genes by covalent histone modification
> — PMID:14992727

> These results indicate that menin not only binds to DNA in a non-sequence specific fashion
> — PMID:15331604

## 32. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q15814 enables GO:0003924 GTPase activity (IDA, PMID:11847227)
- **Field:** GO_ID
- **Change:** GO:0003924 → GO:0005096 (GTPase activator activity)
- **Recorded in:** `genes/human/TBCC/TBCC-ai-review.yaml`

This IDA row (PMID:11847227, assigned by UniProt) gives TBCC GTPase activity (catalysis of GTP + H2O = GDP + phosphate). The paper shows that cofactor C, together with cofactors D and E, stimulates the GTPase activity of native tubulin and that mutation of the conserved arginine abolishes this stimulation (the UniProt R262A mutagenesis note says "Inhibits stimulation of tubulin GTPase activity"). TBCC has no GTPase domain; beta-tubulin hydrolyses the GTP. The evidence supports GO:0005096 GTPase activator activity, which MGI already annotates from the same paper.

> Together with cofactors D and E, cofactor C stimulates the GTPase activity of native tubulin
> — PMID:11847227

> R->A: Inhibits stimulation of tubulin GTPase
> — file:human/TBCC/TBCC-uniprot.txt
