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


## 2026-10-31 — proposed content-review follow-up

The content review identified a missing UniProt-linked phosphorylation paper and an underrepresented NFAT1 mechanism. The qualified new PMID23878394 normal cache is abstract-only; selected original public HTML was read separately. Human lymphatic endothelial chromatin recruitment, preserved nuclear localization/naked-DNA binding, and mouse blood-endothelial remodeling remain distinct. All prior source files are unchanged.

The proposed follow-up retains all 62 original source contexts and both extension atoms, makes the three binding-specificity actions consistent, and promotes the two negative-transcription contexts using independently established human NFAT1 corepression. It adds one supported transcription-corepressor MF annotation and a second, scoped core, with five quote-free findings across the two mechanistic sources. The original-source actions become 23 ACCEPT, 20 KEEP_AS_NON_CORE, 13 TOO_GENERAL, 3 MODIFY and 3 UNDECIDED, plus one NEW MF. There are no new process annotations, product claims or publication quotations. The precise PMID20956529 assay and the cold-response direction retain explicit limitations. NFAT1/NFATC2 is not conflated with NFATC1 lymphatic-valve biology.

These are proposed changes awaiting application and final checks. Initial PR build jobs succeeded; its full test suite was explicitly skipped for the data-only trigger. A failed provider attempt is not retried without changed authentication.


The lymphatic-context follow-up adds genuinely acquired PMID19398761 and selected original primary reading. It supports collecting-vessel maturation in mouse genetics/pharmacology and endogenous FOXC2 chromatin occupancy with selected enhancer assays in human lymphatic endothelium. NFATc1-dependent reporter responses are fragment specific and distinct from the NFAT1/NFATC2 corepressor mechanism. The original GO:0001946 clinical source and non-core action remain; only auxiliary context is added. The proposed record now has 28 references, two cores, one new MF and 23 normal sources; all original source rows and the published notes prefix are preserved.


### Follow-up application and local validation

The reviewed proposal was applied with a new CLI-generated EDIT history. Ordinary schema/reference/ontology validation passed with six advisories, all from the supported generic-binding retentions covered by the campaign instruction. The earlier two same-term action advisories are resolved. Strict GOA validation, source-context/source-byte conservation, history validation, report-only status and private rendering passed. The computed status remains DRAFT. The existing eutils/pkg_resources deprecation diagnostic was retained; no environment or provider retry was introduced.

The final scientific record has 62 original contexts plus one NEW transcription-corepressor MF, two cores, 28 references and 23 normal sources. All original source fields/order, the two-atom conjunction, prior publication/history bytes and notes prefix remain intact. Selected original reading supports seven quote-free findings across the NFAT1, phosphorylation and NFATc1 studies. Initial published-head CI completed successfully, with its full test suite skipped; these local results do not claim follow-up CI or an actual merge.
