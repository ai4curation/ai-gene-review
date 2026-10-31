# FOXC2 notes

## 2026-10-31 — source-specific assessment

FOXC2 is a nuclear forkhead transcriptional regulator. Full-length human binding/reporter experiments and endogenous human promoter ChIP support a transcriptional activation core; purified-domain selection provides complementary sequence-specificity evidence. The assays retain their construct and host limits ([Study 16081467](https://pubmed.ncbi.nlm.nih.gov/16081467/), [Study 16456100](https://pubmed.ncbi.nlm.nih.gov/16456100/), [Study 28473536](https://pubmed.ncbi.nlm.nih.gov/28473536/)).

Mouse endothelial regulation of Itgb3 supports adhesion and migration rather than demonstrated repair of damaged vessels. Separate transfected human-cell experiments support NFAT1-associated transcriptional repression, without establishing a universal repressor function or native T-cell physiology ([Study 18579532](https://pmc.ncbi.nlm.nih.gov/articles/PMC2527100/), [Study 42023653](https://doi.org/10.1093/nar/gkag367)).

The current assessment covers 62 original contexts: 21 ACCEPT, 22 KEEP_AS_NON_CORE, 11 TOO_GENERAL, 3 MODIFY and 5 UNDECIDED. The three refinements concern TRIM27’s experimentally established E3 class and two migration contexts. Five unresolved assertions retain their source-specific uncertainties; no new annotation or quotation is proposed. One original annotation has two conjoined part_of atoms, which must remain together. The official 501-aa Q99958 record has no alternative-product comment block; experimental constructs are not silently assigned to natural products.

The [source guide](FOXC2-source-guide.md) records original URLs, selected assay locators and access limitations. The [source evidence](FOXC2-source-evidence.yaml) preserves all 62 original contexts, the genuine raw/TSV/stored mapping, access metadata and phylogenetic joins.

### Source follow-up

- What original FOXC2-specific assay establishes DNA binding, including the full two-atom conjunction, in PMID20956529? FOXM1 ChIP cannot resolve it.
- Can the exact FOXC2 self-pair/fraction from the PMID25609649 supplement and the exact functional evidence behind PMID21457232 be recovered?
- Which endpoint establishes negative cold-induced thermogenesis in PMID11551504, distinct from increased WAT oxidative metabolism?
- Should the mouse donor vascular-wound annotation be refined to its measured migration endpoint as well? This human review does not edit or replace the donor record.

### Biological questions

- Under which endogenous cellular conditions does FOXC2 interaction with NFAT1 repress transcription, and how does that response relate to FOXC2-dependent activation of other target genes?
- How much of Foxc2-dependent endothelial migration is mediated by integrin beta3, and is this target-to-migration relationship conserved in human endothelial cells?

## 2026-10-31 — acquisition and canonical application

A genuine fetch-gene run created 62 PENDING annotations with no alternative-product entries. Fresh official QuickGO records, every exported column and each complete seed source object matched the reviewed proposal. The current UniProt JSON and FASTA reproduce the 501-aa sequence. The two original extension atoms are restored as one conjunction.

All 21 planned normal sources are present: 12 exact-main sources were reused byte-for-byte and nine were acquired through repository tooling. The genuine Falcon/perplexity-lite attempt failed authentication/access and produced no research file. The existing manual primary reading is retained with its source-specific limits; no provider document was fabricated.

The applied assessment has 21 ACCEPT, 22 KEEP_AS_NON_CORE, 11 TOO_GENERAL, 3 MODIFY and 5 UNDECIDED actions, one activation core, 26 references (18 publication references), no NEW annotations and no publication quotations. The reference note for the auxiliary mouse donor study uses a source-access description without an internal reviewer label. Actual validation and rendering outcomes will be appended after execution.

## 2026-10-31 — validation

Ordinary schema, reference and ontology validation passed with eight advisories: six generic-binding retentions under the campaign instruction and two source-specific action differences (GO:0000978 and GO:0043565). The broader classifications and exact experimental assertions retain their independently justified scopes. Strict GOA matching, generated-history schema, private rendering and exact context/source conservation passed. The repository computes DRAFT. Its initial status mismatch report is retained; the existing status field was changed to that computed value after the ordinary update command left it unchanged. No scientific field changed.

The shared runtime emits an existing pkg_resources deprecation warning. Final history, status, rendering and conservation checks cover the factual documentation closeout. No full CI suite or actual-merge success is claimed. The original seed, raw response, source receipts and failed provider attempt remain preserved.
