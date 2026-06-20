# ABTB2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N961
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1331)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ABTB2/ABTB2-ai-review.yaml](ABTB2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ABTB2/ABTB2-ai-review.html](ABTB2-ai-review.html)
- Gene notes: present - [genes/human/ABTB2/ABTB2-notes.md](ABTB2-notes.md)
- GOA TSV: present - [genes/human/ABTB2/ABTB2-goa.tsv](ABTB2-goa.tsv)
- UniProt record: present - [genes/human/ABTB2/ABTB2-uniprot.txt](ABTB2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ABTB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ABTB2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABTB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABTB2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ABTB2/ABTB2-deep-research-manual.md](ABTB2-deep-research-manual.md)

## AIGR Review Snapshot

- Description: ABTB2 is a large ankyrin-repeat and BTB/POZ-domain protein with protein-protein interaction domains and isoform diversity. Direct experimental work in pancreatic ductal adenocarcinoma models supports a substrate-adaptor-like role in which ABTB2 binds TRAP1, promotes TRAP1 ubiquitination-dependent degradation, and suppresses Wnt/beta-catenin and PI3K/Akt signaling. ABTB2 has been detected in the nucleoplasm, but its normal tissue substrates and broader physiological roles remain incompletely defined.
- Existing/core annotation action counts: KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 2; NEW: 2

## PN Consistency Summary

- **Consistency:** Deep-research (manual fallback), notes, review YAML, and the PN Cul3-adaptor mapping are mutually consistent. All converge on ABTB2 as a **BTB/POZ substrate-adaptor** that binds CUL3 and promotes TRAP1 ubiquitin-dependent degradation (PMID:41322190). No contradictions. The review prudently treats older BPOZ-2 papers as nomenclature-ambiguous with ABTB1 and excludes them as primary evidence.
- **PN story / NEW pressure:** PN asserts adaptor activity not in the original GOA (which had only GO:0046982 heterodimerization IEA, GO:0005515 protein binding IPI, GO:0005654 nucleoplasm). The review **adds** the PN-projected **GO:1990756** (OLS-verified real) as a direct IDA NEW annotation, supported by ABTB2-TRAP1 co-IP, TRAP1 ubiquitination/degradation, and reported ABTB2-cullin-3 interaction, plus companion **GO:0016567** protein ubiquitination. This is gene-specific support, not domain-only projection. Conclusion: legitimate ADD, executed in the review.
- **Evidence alignment:** PN row references (PMID:15071497, 23912815 — generic Cul3/BTB reviews) do NOT overlap the review's primary evidence (PMID:41322190, the 2025 PDAC study); the review rests on stronger gene-specific data than the PN row's domain-review citations. Generic 14-3-3 interactome (PMID:36931259) shared but marked over-annotated.
- **Verdict:** Fully consistent; PN GO:1990756 projection validated by direct evidence and correctly added as NEW. **Recommended edits:** none (mapping and review aligned).

## Full Consistency Review

- **UniProt:** Q8N961 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant|ankyrin` ; **PN-node mapping:** group `Cul3 substrate receptor`=mapped→**GO:1990756 ubiquitin-like ligase-substrate adaptor activity** (new_to_goa); class `E3 ubiquitin and UBL ligases`=context_only (too_broad→GO:0061630); subtype/type/branch=no_mapping.
- **Consistency:** Deep-research (manual fallback), notes, review YAML, and the PN Cul3-adaptor mapping are mutually consistent. All converge on ABTB2 as a **BTB/POZ substrate-adaptor** that binds CUL3 and promotes TRAP1 ubiquitin-dependent degradation (PMID:41322190). No contradictions. The review prudently treats older BPOZ-2 papers as nomenclature-ambiguous with ABTB1 and excludes them as primary evidence.
- **PN story / NEW pressure:** PN asserts adaptor activity not in the original GOA (which had only GO:0046982 heterodimerization IEA, GO:0005515 protein binding IPI, GO:0005654 nucleoplasm). The review **adds** the PN-projected **GO:1990756** (OLS-verified real) as a direct IDA NEW annotation, supported by ABTB2-TRAP1 co-IP, TRAP1 ubiquitination/degradation, and reported ABTB2-cullin-3 interaction, plus companion **GO:0016567** protein ubiquitination. This is gene-specific support, not domain-only projection. Conclusion: legitimate ADD, executed in the review.
- **Mapping strategy:** This gene **strengthens** the Cul3-substrate-receptor group mapping with direct experimental evidence (unlike its paralog ABTB3). The group-level GO:1990756 scope is appropriate (adaptor activity, not catalytic E3); the review correctly avoids GO:0061630 ubiquitin protein ligase activity. No change needed.
- **Evidence alignment:** PN row references (PMID:15071497, 23912815 — generic Cul3/BTB reviews) do NOT overlap the review's primary evidence (PMID:41322190, the 2025 PDAC study); the review rests on stronger gene-specific data than the PN row's domain-review citations. Generic 14-3-3 interactome (PMID:36931259) shared but marked over-annotated.
- **Verdict:** Fully consistent; PN GO:1990756 projection validated by direct evidence and correctly added as NEW. **Recommended edits:** none (mapping and review aligned).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABTB2/ABTB2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul3 substrate receptor | BTB-BACK, variant | ankyrin
- UniProt: Q8N961
- In branches: UPS
- Signature domains: IPR000210, cd18526
- Auxiliary domains: IPR002110
- PN references (titles):
    - 15071497 / rev
    - 23912815 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant|ankyrin
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
