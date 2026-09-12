# FBXL12 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NXK8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL12/FBXL12-ai-review.yaml](FBXL12-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL12/FBXL12-ai-review.html
- Gene notes: missing - genes/human/FBXL12/FBXL12-notes.md
- GOA TSV: present - [genes/human/FBXL12/FBXL12-goa.tsv](FBXL12-goa.tsv)
- UniProt record: present - [genes/human/FBXL12/FBXL12-uniprot.txt](FBXL12-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL12.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL12.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL12/FBXL12-deep-research-falcon.md](FBXL12-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL12 (F-box/LRR-repeat protein 12; FBL12) is a substrate-recognition subunit of an SCF (SKP1-CUL1-RBX1) E3 ubiquitin ligase complex. Its N-terminal F-box motif binds SKP1, linking it to the CUL1-RBX1 catalytic core, and its leucine-rich repeats confer substrate selectivity, so that SCF(FBXL12) directs substrate-specific (often K48-linked) polyubiquitination and proteasomal degradation. Several physiological substrates have been defined in distinct cellular programs, with substrate selection frequently gated by substrate phosphorylation. SCF(FBXL12) degrades calcium/calmodulin-dependent protein kinase I (CAMK1; acceptor Lys59), which lowers CAMK1-driven p27 phosphorylation, disrupts cyclin D1/CDK4 complex assembly, and triggers G1 cell-cycle arrest in lung epithelia. It targets the cyclin-dependent kinase inhibitors p57KIP2/CDKN1C (TGF-beta1-induced, phosphorylation-dependent turnover linked to osteoblast differentiation) and CDKN1B/p27 (Lys165 acceptor; degraded together with SCF(FBXL1)/SKP2 downstream of pre-TCR and Notch signaling to license the proliferative burst of thymocyte beta-selection). It promotes CHK1-phosphorylation-dependent degradation of chromatin-associated FANCD2 to support replication-fork recovery and cancer-cell survival under replication stress, and degrades the aldehyde dehydrogenases ALDH3A1/ALDH3A2 to permit trophoblast differentiation during placental development. An SCF complex containing FBXL12 also mediates DNA-damage-induced K48-linked ubiquitination and removal of the NHEJ factor Ku80 from DNA ends (shown in Xenopus extracts, with conservation to human inferred). FBXL12 acts in both the cytoplasm (where it co-localizes with CAMK1) and the nucleus/chromatin (FANCD2, Ku80). Many of its catalogued interactions derive from high-throughput proteomic screens and are not established functional substrates.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 18; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep research (falcon, marked VERIFIED here, cross-checked vs UniProt + cached PMID:18660753), review, PN annotation, and node mapping agree FBXL12 is the SCF(FBXL12) receptor with multiple substrates (p57KIP2/CDKN1C validated IDA PMID:18660753; CAMK1 PMID:23707388; plus falcon leads FANCD2, p27/CDKN1B-K165, ALDH3A1/2, Ku80). No contradictions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. FBXL12 GOA has NO MF beyond `protein binding`. The review adds `GO:1990756` as **action: NEW (IDA, PMID:18660753)** — the batch-correct call, matching the PN-projected new_to_goa term. BPs (`SCF catabolism`, `regulation of cell cycle`) already captured. Conclusion: adaptor MF correctly ADDED as NEW; no over-reach.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses gene-specific primaries (18660753, 23707388, 33234069) + falcon leads. No overlap with the PN placeholder; review evidence richer. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. Correct NEW→GO:1990756 application with a validated substrate anchor. No edits required.

## Full Consistency Review

- **UniProt:** Q9NXK8 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; class `context_only / too_broad / GO:0061630`.
- **Consistency:** Strong. Deep research (falcon, marked VERIFIED here, cross-checked vs UniProt + cached PMID:18660753), review, PN annotation, and node mapping agree FBXL12 is the SCF(FBXL12) receptor with multiple substrates (p57KIP2/CDKN1C validated IDA PMID:18660753; CAMK1 PMID:23707388; plus falcon leads FANCD2, p27/CDKN1B-K165, ALDH3A1/2, Ku80). No contradictions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. FBXL12 GOA has NO MF beyond `protein binding`. The review adds `GO:1990756` as **action: NEW (IDA, PMID:18660753)** — the batch-correct call, matching the PN-projected new_to_goa term. BPs (`SCF catabolism`, `regulation of cell cycle`) already captured. Conclusion: adaptor MF correctly ADDED as NEW; no over-reach.
- **Mapping strategy:** Gene does not change the node. Status/scope right; PN-projected GO:1990756 equals the review MF (not broader/narrower). Has a PMID-validated substrate (p57KIP2 IDA) — canonical receptor, NOT an orphan. Cytoplasmic + nuclear/chromatin dual localization is gene-specific and rightly outside the shared node mapping.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses gene-specific primaries (18660753, 23707388, 33234069) + falcon leads. No overlap with the PN placeholder; review evidence richer. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. Correct NEW→GO:1990756 application with a validated substrate anchor. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL12/FBXL12-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q9NXK8
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
