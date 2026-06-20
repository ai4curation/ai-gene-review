# ARNT PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P27540
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1374)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ARNT/ARNT-ai-review.yaml](ARNT-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ARNT/ARNT-ai-review.html](ARNT-ai-review.html)
- Gene notes: present - [genes/human/ARNT/ARNT-notes.md](ARNT-notes.md)
- GOA TSV: present - [genes/human/ARNT/ARNT-goa.tsv](ARNT-goa.tsv)
- UniProt record: present - [genes/human/ARNT/ARNT-uniprot.txt](ARNT-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ARNT.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ARNT.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARNT.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARNT.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ARNT/ARNT-deep-research-falcon.md](ARNT-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ARNT encodes aryl hydrocarbon receptor nuclear translocator, also known as HIF-1 beta, a broadly expressed nuclear bHLH-PAS transcription factor subunit. ARNT dimerizes with AHR, HIF-alpha proteins, and other bHLH-PAS partners through PAS-domain interfaces, and the resulting complexes bind cis-regulatory DNA elements such as xenobiotic/dioxin response elements and hypoxia response elements to regulate RNA polymerase II transcription. Through these heterodimeric complexes, ARNT participates in xenobiotic response, hypoxia adaptation, angiogenic and metabolic gene regulation, and selected immune and developmental transcriptional programs. The primary molecular roles are sequence-specific regulatory DNA binding and partner-specific transcription factor dimerization in the nucleus.
- Existing/core annotation action counts: ACCEPT: 47; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 15; MODIFY: 20; REMOVE: 1

## PN Consistency Summary

- **Consistency:** CONTRADICTION between PN placement and the gene's biology. Deep research, notes, review YAML all establish ARNT (HIF-1β) as a **nuclear bHLH-PAS transcription-factor dimerization partner** for AHR/HIF-α — not a CUL4 ligase substrate adaptor. The notes explicitly reject the GO:1990756 projection: the AHR/ARNT/TBL3 leaf nodes are themselves no_mapping in the UPS YAML, and no reviewed ARNT literature shows it recruiting substrates to a CUL4 ligase.
- **PN story / NEW pressure:** PN asserts a UPS substrate-adaptor MF (GO:1990756) absent from ARNT GOA and unsupported. GO:1990756 is a real term, but applying it to ARNT **over-reaches** — the AHR/ARNT/TBL3 association reflects ARNT's transcription-complex role, not ligase-adaptor activity. Review correctly declined to add it to proposed_new_terms/core_functions. **Conclude: over-reaches.** ARNT's true functions (TF activity GO:0000981, heterodimerization GO:0046982, AHR binding GO:0017162) are already captured.
- **Evidence alignment:** PN cites PMID:17392787 and PMID:28416634 (AHR-associated CUL4B ligase / AHR-ARNT structure). These concern the AHR ligase context and the AHR-ARNT DRE complex, supporting ARNT as DNA-binding partner — not as a UPS adaptor. Review evidence (PMID:1317062, PMID:7539918, PMID:28396409) is TF-centric and divergent from the UPS framing.
- **Verdict:** PN UPS adaptor projection over-reaches and is correctly rejected in-review. **Recommended edits:** exempt ARNT from GO:1990756 group propagation at the mapping layer [MAP].

## Full Consistency Review

- **UniProt:** P27540 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE (Falcon DR present; large review)
- **PN placement:** `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|AHR / ARNT / TBL3 complex|PAS` ; **PN-node mapping:** subtype(PAS)/type(AHR/ARNT/TBL3)=no_mapping; group(Cul4A/Cul4B substrate adaptor)=mapped/ok GO:1990756 (ubiquitin-like ligase-substrate adaptor activity, new_to_goa); class=context_only GO:0061630; branch=no_mapping. PN refs: PMID:17392787, PMID:28416634. Auxiliary domain IPR000014 (PAS).
- **Consistency:** CONTRADICTION between PN placement and the gene's biology. Deep research, notes, review YAML all establish ARNT (HIF-1β) as a **nuclear bHLH-PAS transcription-factor dimerization partner** for AHR/HIF-α — not a CUL4 ligase substrate adaptor. The notes explicitly reject the GO:1990756 projection: the AHR/ARNT/TBL3 leaf nodes are themselves no_mapping in the UPS YAML, and no reviewed ARNT literature shows it recruiting substrates to a CUL4 ligase.
- **PN story / NEW pressure:** PN asserts a UPS substrate-adaptor MF (GO:1990756) absent from ARNT GOA and unsupported. GO:1990756 is a real term, but applying it to ARNT **over-reaches** — the AHR/ARNT/TBL3 association reflects ARNT's transcription-complex role, not ligase-adaptor activity. Review correctly declined to add it to proposed_new_terms/core_functions. **Conclude: over-reaches.** ARNT's true functions (TF activity GO:0000981, heterodimerization GO:0046982, AHR binding GO:0017162) are already captured.
- **Mapping strategy:** ARNT is a false-positive member of the Cul4 substrate-adaptor group (likely placed via the AHR-CUL4B literature where AHR, not ARNT, is the ligase component). The group→GO:1990756 mapping may be valid for genuine adaptors but must NOT propagate to ARNT. Recommend exempting ARNT from this group projection.
- **Evidence alignment:** PN cites PMID:17392787 and PMID:28416634 (AHR-associated CUL4B ligase / AHR-ARNT structure). These concern the AHR ligase context and the AHR-ARNT DRE complex, supporting ARNT as DNA-binding partner — not as a UPS adaptor. Review evidence (PMID:1317062, PMID:7539918, PMID:28396409) is TF-centric and divergent from the UPS framing.
- **Verdict:** PN UPS adaptor projection over-reaches and is correctly rejected in-review. **Recommended edits:** exempt ARNT from GO:1990756 group propagation at the mapping layer [MAP].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ARNT/ARNT-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate adaptor | AHR / ARNT / TBL3 complex | PAS
- UniProt: P27540
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR000014
- PN references (titles):
    - 17392787
    - 28416634
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|AHR / ARNT / TBL3 complex|PAS
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|AHR / ARNT / TBL3 complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
