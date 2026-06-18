# FBXL8 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96CD0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL8/FBXL8-ai-review.yaml](FBXL8-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL8/FBXL8-ai-review.html
- Gene notes: missing - genes/human/FBXL8/FBXL8-notes.md
- GOA TSV: present - [genes/human/FBXL8/FBXL8-goa.tsv](FBXL8-goa.tsv)
- UniProt record: present - [genes/human/FBXL8/FBXL8-uniprot.txt](FBXL8-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL8.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL8.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL8/FBXL8-deep-research-falcon.md](FBXL8-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL8 (F-box/LRR-repeat protein 8, FBL8) is a member of the FBXL subfamily of F-box proteins. It has an N-terminal F-box domain through which it docks onto the SKP1 adaptor and, via SKP1, onto CUL1 and the catalytic RING subunit RBX1, assembling a Cullin-RING (SCF) E3 ubiquitin ligase in which the F-box protein serves as the substrate-recognition subunit. Despite the "LRR" in its name, UniProt notes that FBXL8 does not actually contain canonical leucine-rich repeats; nonetheless its C-terminal substrate-binding region is functionally required for substrate engagement (deletion of either the F-box or the C-terminal region abolishes substrate turnover). FBXL8 acts as the substrate-recognition subunit of SCF-FBXL8 and targets several substrates in a strongly context-dependent manner: it promotes ubiquitination and proteasomal degradation of the tumor suppressor p53 (in colorectal cancer), of Thr283- phosphorylated cyclin D3 (CCND3) (in lymphoma), of Snail1 (in post-myocardial- infarction cardiac fibroblasts, dampening RhoA signaling and myofibroblast differentiation), and of unphosphorylated c-MYC (a distinct c-MYC pool from that controlled by FBXW7, with reported heterotypic K48/K63 chains); CCND2 and IRF5 are additional candidate substrates accumulating upon FBXL8 knockdown. Reported localization is predominantly cytoplasmic (loss of FBXL8 causes nuclear c-MYC accumulation), and in heart FBXL8 is enriched in cardiac fibroblasts. Its net effect is context-dependent rather than uniformly oncogenic or tumor-suppressive: oncogenic in colorectal and breast cancer, but tumor-suppressive in lymphoma and anti-fibrotic after myocardial infarction.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 17

## PN Consistency Summary

- **Consistency:** Mostly consistent, with one structural gap. Review, PN annotation, and node mapping agree FBXL8 is an SCF substrate receptor. **Non-canonical F-box: UniProt notes FBXL8 does NOT contain canonical leucine-rich repeats despite the "LRR" name** — yet the PN places it under the `...|F-box|LRR` subtype. The review captures this caveat in its description; the PN subtype label is therefore mildly inaccurate for this member (subtype is `no_mapping`, so no propagation harm). Falcon substrates (p53, phospho-Thr283 CCND3, Snail1, unphospho c-MYC) are UNVERIFIED leads, correctly not added as GO terms.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. FBXL8 GOA has NO MF beyond `protein binding` (SKP1) and no SCF-process IDA. The review's core_functions assigns `GO:1990756`, but — unlike FBXL7/FBXL12 — **it is NOT added as an `action: NEW` entry in existing_annotations.** This is the one batch-pattern deviation: the adaptor MF that PN projects as new_to_goa is endorsed in core_functions but never materialized as a reviewable annotation. Conclusion: ADD GO:1990756 as NEW to existing_annotations for parity.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses SKP1 interactome PMIDs + PMID:33234069 + falcon leads. No PMID overlap with placeholder.
- **Verdict:** MAPPING CONSISTENT but YAML gap. **Recommended edits:** [YAML] add `GO:1990756` as `action: NEW` in FBXL8 existing_annotations (mirror FBXL7/FBXL12) so the PN-projected adaptor MF is materialized; [MAP] consider noting the non-canonical (no-LRR) status on the F-box|LRR subtype for FBXL8.

## Full Consistency Review

- **UniProt:** Q96CD0 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; class `context_only / too_broad / GO:0061630`.
- **Consistency:** Mostly consistent, with one structural gap. Review, PN annotation, and node mapping agree FBXL8 is an SCF substrate receptor. **Non-canonical F-box: UniProt notes FBXL8 does NOT contain canonical leucine-rich repeats despite the "LRR" name** — yet the PN places it under the `...|F-box|LRR` subtype. The review captures this caveat in its description; the PN subtype label is therefore mildly inaccurate for this member (subtype is `no_mapping`, so no propagation harm). Falcon substrates (p53, phospho-Thr283 CCND3, Snail1, unphospho c-MYC) are UNVERIFIED leads, correctly not added as GO terms.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. FBXL8 GOA has NO MF beyond `protein binding` (SKP1) and no SCF-process IDA. The review's core_functions assigns `GO:1990756`, but — unlike FBXL7/FBXL12 — **it is NOT added as an `action: NEW` entry in existing_annotations.** This is the one batch-pattern deviation: the adaptor MF that PN projects as new_to_goa is endorsed in core_functions but never materialized as a reviewable annotation. Conclusion: ADD GO:1990756 as NEW to existing_annotations for parity.
- **Mapping strategy:** Gene does not change the group GO:1990756 (defensible on F-box + SKP1 grounds). **FLAGS: (1) non-canonical F-box (no true LRRs) — PN `|LRR` subtype label is a misnomer here; (2) no PMID-validated substrate in existing_annotations — adaptor MF is inferred-only.** Scope/status otherwise correct.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses SKP1 interactome PMIDs + PMID:33234069 + falcon leads. No PMID overlap with placeholder.
- **Verdict:** MAPPING CONSISTENT but YAML gap. **Recommended edits:** [YAML] add `GO:1990756` as `action: NEW` in FBXL8 existing_annotations (mirror FBXL7/FBXL12) so the PN-projected adaptor MF is materialized; [MAP] consider noting the non-canonical (no-LRR) status on the F-box|LRR subtype for FBXL8.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL8/FBXL8-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q96CD0
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
