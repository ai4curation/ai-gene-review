# FBXO33 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q7Z6M2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO33/FBXO33-ai-review.yaml](FBXO33-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO33/FBXO33-ai-review.html
- Gene notes: missing - genes/human/FBXO33/FBXO33-notes.md
- GOA TSV: present - [genes/human/FBXO33/FBXO33-goa.tsv](FBXO33-goa.tsv)
- UniProt record: present - [genes/human/FBXO33/FBXO33-uniprot.txt](FBXO33-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO33.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO33.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO33.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO33.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO33/FBXO33-deep-research-falcon.md](FBXO33-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO33 (F-box only protein 33, FBX33) is the substrate-recognition subunit of a SCF (SKP1-CUL1-F-box protein) / CRL1-type E3 ubiquitin-protein ligase complex. As an F-box "other" (FBXO) protein it lacks the C-terminal leucine-rich repeat or WD40 substrate-binding domains found in typical F-box proteins; instead it uses its N-terminal region to engage substrate, while its F-box motif (residues 65-111) docks the adaptor SKP1, which in turn links it to the CUL1 scaffold and the catalytic RING subunit RBX1. Within this complex FBXO33 acts as the substrate receptor that selects target proteins for poly-ubiquitination and subsequent proteasomal degradation; it is the F-box adaptor and not the catalytic RING core, and it has been observed in both the nucleus and the cytoplasm. The best-documented substrate is the multifunctional cold-shock-domain transcription/translation/splicing regulator YBX1 (Y-box binding protein 1, YB-1/dbpB/p50): FBXO33 associates with the YBX1 cold-shock domain through its N-terminus and targets YBX1 for ubiquitin-dependent proteasomal degradation, a function with relevance to bone-marrow stromal cell fate during aging. Additional substrate-like targets and context-dependent roles have been reported: FBXO33 promotes ubiquitination and clearance of expanded-polyglutamine ataxin-3 (ATXN3), reducing toxic aggregation in models of polyglutamine disease (a proteostasis/protein-quality-control role); it can promote ubiquitination and degradation of MYC (suppressing stemness/metastasis in non-small-cell lung cancer) and of wild-type p53 (promoting metastasis in gallbladder cancer), illustrating that as a substrate adaptor it can be tumor-suppressive or oncogenic depending on the dominant substrate in a given context. FBXO33 was originally identified as a gene induced during programmed cell death and has also been implicated as a negative modulator of cardiomyocyte hypertrophy. It is widely expressed (with enhanced expression in bone) and has been recovered in SCF-network and chromatin/Polycomb-related interaction studies.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 8

## PN Consistency Summary

- **Consistency:** Strong. Deep research (Falcon → YBX1, ATXN3/polyQ, MYC, p53 substrates), UniProt and GOA agree FBXO33 is the SCF(FBXO33) substrate receptor for YBX1 (bound via N-terminus to YBX1 CSD). Review core MF = GO:1990756. NOTE: subtype label is "LRR" (IPR032675) but the review/UniProt explicitly state FBXO33 LACKS canonical LRR/WD40 substrate domains and engages substrate via its N-terminus — a minor PN-workbook signature-domain vs biology tension, not a GO mapping error.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF. Unlike FBXO22/25/30/34, FBXO33's GOA carries NO ubiquitin-ligase/transferase MF annotation to MODIFY (no GO:0061630/0004842; only protein binding IPI, SCF complex CC, SCF catabolism BP). So GO:1990756 in core_functions is **inferred-only** (asserted by the review/PN, not derived from an existing MF annotation). It is well-justified by the YBX1 IDA-grade biology, but technically the adaptor MF is NEW relative to GOA — this is the strongest "ADD GO:1990756 to GOA" candidate among these six. proposed_new_terms empty (correct; no substrate-specific term warranted). Conclusion: PN adaptor claim = defensible ADD to GOA (GO:1990756 verified real).
- **Evidence alignment:** PN cites only "15340381 / rev". Review anchored on PMID:16797541 (YB-1 degradation, the founding FBXO33 functional paper) + Falcon (Xiao 2023 EMBO J YBX1/BMSC; Chen 2019 ATXN3; Wei 2024 MYC; Wu 2025 p53) + interactome PMIDs + PMID:34445249. PN reference disjoint from and far thinner than review's.
- **Verdict:** CONSISTENT — no edits required; flag that GO:1990756 core MF is inferred-only (best ADD-to-GOA candidate; substrate-validated by YBX1).

## Full Consistency Review

- **UniProt:** Q7Z6M2 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (well-developed)
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` (aux domain IPR032675) ; **PN-node mapping:** group=mapped GO:1990756; subtype/type/branch=no_mapping; class=context_only (GO:0061630).
- **Consistency:** Strong. Deep research (Falcon → YBX1, ATXN3/polyQ, MYC, p53 substrates), UniProt and GOA agree FBXO33 is the SCF(FBXO33) substrate receptor for YBX1 (bound via N-terminus to YBX1 CSD). Review core MF = GO:1990756. NOTE: subtype label is "LRR" (IPR032675) but the review/UniProt explicitly state FBXO33 LACKS canonical LRR/WD40 substrate domains and engages substrate via its N-terminus — a minor PN-workbook signature-domain vs biology tension, not a GO mapping error.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF. Unlike FBXO22/25/30/34, FBXO33's GOA carries NO ubiquitin-ligase/transferase MF annotation to MODIFY (no GO:0061630/0004842; only protein binding IPI, SCF complex CC, SCF catabolism BP). So GO:1990756 in core_functions is **inferred-only** (asserted by the review/PN, not derived from an existing MF annotation). It is well-justified by the YBX1 IDA-grade biology, but technically the adaptor MF is NEW relative to GOA — this is the strongest "ADD GO:1990756 to GOA" candidate among these six. proposed_new_terms empty (correct; no substrate-specific term warranted). Conclusion: PN adaptor claim = defensible ADD to GOA (GO:1990756 verified real).
- **Mapping strategy:** Correct; gene does not change the node. GO:1990756 equals the review's core MF. Because there is no MF annotation in GOA, the PN projection (new_to_goa) genuinely adds value here.
- **Evidence alignment:** PN cites only "15340381 / rev". Review anchored on PMID:16797541 (YB-1 degradation, the founding FBXO33 functional paper) + Falcon (Xiao 2023 EMBO J YBX1/BMSC; Chen 2019 ATXN3; Wei 2024 MYC; Wu 2025 p53) + interactome PMIDs + PMID:34445249. PN reference disjoint from and far thinner than review's.
- **Verdict:** CONSISTENT — no edits required; flag that GO:1990756 core MF is inferred-only (best ADD-to-GOA candidate; substrate-validated by YBX1).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO33/FBXO33-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q7Z6M2
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR032675
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
