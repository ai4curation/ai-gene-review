# Gene validation triage

Latest follow-up: added structured reference replacement metadata to the schema and JAK1. PMID:34521819 is recorded as a duplicate of PMID:32953130, based on the reviewer-supplied PubMed notice. The canonical full text was reviewed; both matching IPI rows now use KEEP_AS_NON_CORE and cite a verbatim canonical-PMID snippet. JAK1 passes validation with the expected legacy-PMID retrieval advisory. Earlier run results and intermediate decisions below are historical.

Follow-up: rebased onto `78ce621267`. CMC2 now passes `just validate yeast CMC2`. JAK1 was corrected to UNDECIDED for PMID:34521819, with the reference marked UNVERIFIED and the unsupported invalid/retracted claim removed. `just validate human JAK1` passes with one advisory warning for that inaccessible reference. The full-batch counts below describe the earlier run; the full batch was not rerun after this follow-up.

Validated after rebase onto origin/main at `0d925a0696`.

`just validate-all` exited 1: 4,796 reviews checked; 4,795 passed, one failed. Schema passed; term checks had no blocking errors (10 label warnings in 9 files); reference checks had 53 advisory warnings in 30 files; best-practice checks had 2 errors and 3,659 warnings in 1,805 files. All 54 pathway markdown files containing PMID references passed.

## Blocking failure

[yeast/CMC2](../genes/yeast/CMC2/CMC2-ai-review.yaml): the GO:0033617 / IMP / PMID:20220131 row includes `supporting_entities: [SGD:S000001620]` at lines 77–78, but the cached GOA WITH/FROM field is empty. This causes the same annotation to be reported as both missing and extra. Reconcile this metadata with its source; the term ID itself is not the mismatch.

## Priorities

- Inspect inconsistent annotation decisions and core-function/annotation discrepancies first. These warnings identify possible curation inconsistencies, not proven biological errors; evidence-specific differences can be valid.
- Resolve malformed or unsupported reference identifiers so citations can be checked. See the per-gene list below.
- In human/JAK1, the experimental protein-binding row for PMID:34521819 is REMOVE solely because its reference cannot be retrieved (lines 1603–1610). The repository instructs reviewers to use UNDECIDED for inaccessible evidence; missing access alone does not justify REMOVE or a retraction claim.
- Complete unfinished reviews (PENDING annotations, TODO descriptions, missing core functions) according to project priority.
- Missing structured propagation reviews are a large provenance backlog. Do not mechanically invent phylogenetic claims to silence them.
- Uncited deep research and term-label mismatches are lower priority than evidence and decision problems.

## Best-practice warning counts

| Warning | Instances | Genes |
|---|---:|---:|
| Missing structured propagation reviews | 1186 | 496 |
| Available deep research not cited | 804 | 804 |
| Core molecular function absent from annotation block | 356 | 306 |
| Core process absent from annotation block | 349 | 294 |
| Core location absent from annotation block | 246 | 202 |
| Inconsistent actions for the same GO term | 260 | 154 |
| Missing core functions | 177 | 177 |
| PENDING annotations | 52 | 52 |
| Missing references | 3 | 3 |
| TODO description | 58 | 58 |
| Core complex absent from annotation block | 103 | 103 |
| Accepted annotation lacks supported_by | 65 | 20 |

## Unresolved reference warnings

These are fetch/identifier warnings, not findings that the cited biology is false. PMID:34521819 is already documented as unresolvable in the reviews. Some unsupported source types may need validator support rather than curation changes.

| Gene | Warning | Occurrences |
|---|---|---:|
| [9POAL/psbA](../genes/9POAL/psbA/psbA-ai-review.yaml) | Could not fetch reference: HAMAP-Rule:MF_01379 | 1 |
| [ACET2/cipA](../genes/ACET2/cipA/cipA-ai-review.yaml) | Could not fetch reference: cipA-deep-research-falcon.md | 1 |
| [ANOGA/CLIPB4](../genes/ANOGA/CLIPB4/CLIPB4-ai-review.yaml) | Could not fetch reference: saab2024insightintothe | 1 |
| [ANOGA/CLIPB4](../genes/ANOGA/CLIPB4/CLIPB4-ai-review.yaml) | Could not fetch reference: vandana2024wolbachiainfectionresponsiveimmune | 1 |
| [ARATH/AT5G05410](../genes/ARATH/AT5G05410/AT5G05410-ai-review.yaml) | Could not fetch reference: AT5G05410-notes.md | 1 |
| [ARATH/AT5G05410](../genes/ARATH/AT5G05410/AT5G05410-ai-review.yaml) | Could not fetch reference: AT5G05410-deep-research-perplexity.md | 1 |
| [ARATH/AT5G05410](../genes/ARATH/AT5G05410/AT5G05410-ai-review.yaml) | Could not fetch reference: AT5G05410-uniprot.txt | 1 |
| [ARATH/FLS2](../genes/ARATH/FLS2/FLS2-ai-review.yaml) | Could not fetch reference: PANTHER:PTHR48056 | 1 |
| [ARATH/PAL1](../genes/ARATH/PAL1/PAL1-ai-review.yaml) | Could not fetch reference: P35510 | 9 |
| [CUPNH/glcE](../genes/CUPNH/glcE/glcE-ai-review.yaml) | Could not fetch reference: UniProtKB-EC | 1 |
| [CUPNH/glcE](../genes/CUPNH/glcE/glcE-ai-review.yaml) | Could not fetch reference: InterPro | 1 |
| [CUPNH/glcE](../genes/CUPNH/glcE/glcE-ai-review.yaml) | Could not fetch reference: curator_inference | 1 |
| [CUPNH/glcE](../genes/CUPNH/glcE/glcE-ai-review.yaml) | Could not fetch reference: glcE-falcon-research | 1 |
| [DROME/CG6051](../genes/DROME/CG6051/CG6051-ai-review.yaml) | Could not fetch reference: Q9VB70 | 1 |
| [DROME/Ced-12](../genes/DROME/Ced-12/Ced-12-ai-review.yaml) | Could not fetch reference: deep-research | 1 |
| [ECOLI/yrhB](../genes/ECOLI/yrhB/yrhB-ai-review.yaml) | Could not fetch reference: DOI:10.1007/978-0-8176-4747-1 | 1 |
| [PSEPK/pvdS](../genes/PSEPK/pvdS/pvdS-ai-review.yaml) | Could not fetch reference: curator_inference | 1 |
| [WHEAT/RHT1](../genes/WHEAT/RHT1/RHT1-ai-review.yaml) | Could not fetch reference: Q9ST59 | 1 |
| [human/ANKFY1](../genes/human/ANKFY1/ANKFY1-ai-review.yaml) | Could not fetch reference: projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv | 1 |
| [human/BCL2](../genes/human/BCL2/BCL2-ai-review.yaml) | Could not fetch reference: croce2025thebcl2protein | 1 |
| [human/C1QBP](../genes/human/C1QBP/C1QBP-ai-review.yaml) | Could not fetch reference: deep-research | 1 |
| [human/CKAP2](../genes/human/CKAP2/CKAP2-ai-review.yaml) | Could not fetch reference: CKAP2-deep-research.md | 1 |
| [human/FOXO1](../genes/human/FOXO1/FOXO1-ai-review.yaml) | Could not fetch reference: santos2023foxofamilyisoforms | 1 |
| [human/FOXO1](../genes/human/FOXO1/FOXO1-ai-review.yaml) | Could not fetch reference: cheng2024forkheadboxo | 1 |
| [human/FOXO1](../genes/human/FOXO1/FOXO1-ai-review.yaml) | Could not fetch reference: rodriguezcolman2024foxotranscriptionfactors | 1 |
| [human/GGCT](../genes/human/GGCT/GGCT-ai-review.yaml) | Could not fetch reference: reactome/R-HSA-1247922.md | 1 |
| [human/GSS](../genes/human/GSS/GSS-ai-review.yaml) | Could not fetch reference: GSS-deep-research-falcon.md | 1 |
| [human/JAK1](../genes/human/JAK1/JAK1-ai-review.yaml) | Could not fetch reference: PMID:34521819 | 1 |
| [human/PARD6G](../genes/human/PARD6G/PARD6G-ai-review.yaml) | Could not fetch reference: earl2025capturemutualinhibition | 1 |
| [human/PCSK1N](../genes/human/PCSK1N/PCSK1N-ai-review.yaml) | Could not fetch reference: geneontology/go-annotation#6407 | 1 |
| [human/PEMT](../genes/human/PEMT/PEMT-ai-review.yaml) | Could not fetch reference: reactome/R-HSA-1483191.md | 1 |
| [human/PEMT](../genes/human/PEMT/PEMT-ai-review.yaml) | Could not fetch reference: reactome/R-HSA-1483174.md | 4 |
| [human/SCN1A](../genes/human/SCN1A/SCN1A-ai-review.yaml) | Could not fetch reference: clinical_literature | 1 |
| [human/STAT1](../genes/human/STAT1/STAT1-ai-review.yaml) | Could not fetch reference: PMID:34521819 | 1 |
| [human/STAT2](../genes/human/STAT2/STAT2-ai-review.yaml) | Could not fetch reference: PMID:34521819 | 1 |
| [worm/hsp-4](../genes/worm/hsp-4/hsp-4-ai-review.yaml) | Could not fetch reference: urban2025functionallydiversifiedcaenorhabditis | 1 |
| [worm/hsp-4](../genes/worm/hsp-4/hsp-4-ai-review.yaml) | Could not fetch reference: waldherr2024endoplasmicreticulumunfolded | 1 |
| [worm/hsp-4](../genes/worm/hsp-4/hsp-4-ai-review.yaml) | Could not fetch reference: xu2024theunfoldedprotein | 1 |
| [worm/ire-1](../genes/worm/ire-1/ire-1-ai-review.yaml) | Could not fetch reference: ire-1-deep-research-falcon.md | 1 |
| [worm/lrx-1](../genes/worm/lrx-1/lrx-1-ai-review.yaml) | Could not fetch reference: BioGRID | 1 |
| [yeast/THI22](../genes/yeast/THI22/THI22-ai-review.yaml) | Could not fetch reference: SGD:S000006325 | 2 |

Full logs: [all stages](validation-all.log). Detailed best-practice issues: [TSV](validation-all.tsv). Individual CMC2 check: [log](validation-CMC2.log).
