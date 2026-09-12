# AIRE PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O43918
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1358)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AIRE/AIRE-ai-review.yaml](AIRE-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AIRE/AIRE-ai-review.html](AIRE-ai-review.html)
- Gene notes: present - [genes/human/AIRE/AIRE-notes.md](AIRE-notes.md)
- GOA TSV: present - [genes/human/AIRE/AIRE-goa.tsv](AIRE-goa.tsv)
- UniProt record: present - [genes/human/AIRE/AIRE-uniprot.txt](AIRE-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AIRE.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AIRE.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AIRE.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AIRE.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AIRE/AIRE-deep-research-manual.md](AIRE-deep-research-manual.md)

## AIGR Review Snapshot

- Description: AIRE is a nuclear autoimmune regulator expressed most prominently in medullary thymic epithelial cells, where it promotes central self-tolerance by enabling promiscuous expression of tissue-restricted antigen genes. The protein contains an HSR oligomerization domain, a SAND domain, and two PHD zinc fingers; PHD1 acts as a histone H3K4me0 reader that helps target AIRE to poorly active chromatin and supports transcriptional activation of self-antigen genes. AIRE also forms nuclear-body-like structures and interacts with chromatin and transcription/RNA-processing partners. Loss-of-function or dominant-negative AIRE variants impair these transcriptional tolerance programs and cause autoimmune polyendocrine syndrome type 1 or related organ-specific autoimmune phenotypes.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 19; MARK_AS_OVER_ANNOTATED: 8; MODIFY: 5; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Major contradiction between PN annotation and review. PN classifies AIRE as a catalytic E3 ligase (RING-variant/PHD) and projects GO:0061630 as a new GOA annotation. The review and notes treat AIRE strictly as a nuclear chromatin reader / Pol II transcriptional activator (PHD1 = H3K4me0 histone reader, PMID:18292755, 19446523) and **explicitly decline** to add GO:0061630, adding instead a suggested experiment to test for absent E3 activity. Deep research (manual) and review are internally consistent; the PN node is the outlier.
- **PN story / NEW pressure:** PN asserts an E3-ligase MF not in GOA. GO:0061630 is a real term, but for AIRE this is a **domain-bucket inference** (PHD≈RING fold) not supported by the cached AIRE evidence, which characterizes the PHD as a histone-recognition module, not a catalytic ligase. Verdict: over-reaches as currently projected; treat as candidate requiring direct ubiquitin-transfer evidence, not an automatic ADD. (Some non-cached mouse literature reports AIRE E2-binding/E3-like activity — flag for full-text check before any REMOVE/ADD verdict; reviewer's conservative non-adoption is defensible.)
- **Evidence alignment:** Divergent. PN cites PMIDs 14734522 and 15150263 (not in the review's reference list); review is built on the chromatin/transcription corpus (PMID:11533054, 18292755, 19446523, 26084028). No PMID overlap — the PN E3 case rests on references the review never adjudicated.
- **Verdict:** PN E3-ligase placement/projection over-reaches for AIRE; review correctly withholds GO:0061630 pending direct evidence.

## Full Consistency Review

- **UniProt:** O43918 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|PHD|other` ; **PN-node mapping:** PHD/RING-variant subtype+type no_mapping; *group* (RING variant) mapped→GO:0061630 (ubiquitin protein ligase activity, propagate); class context_only (too_broad). Projection: **GO:0061630 new_to_goa**.
- **Consistency:** Major contradiction between PN annotation and review. PN classifies AIRE as a catalytic E3 ligase (RING-variant/PHD) and projects GO:0061630 as a new GOA annotation. The review and notes treat AIRE strictly as a nuclear chromatin reader / Pol II transcriptional activator (PHD1 = H3K4me0 histone reader, PMID:18292755, 19446523) and **explicitly decline** to add GO:0061630, adding instead a suggested experiment to test for absent E3 activity. Deep research (manual) and review are internally consistent; the PN node is the outlier.
- **PN story / NEW pressure:** PN asserts an E3-ligase MF not in GOA. GO:0061630 is a real term, but for AIRE this is a **domain-bucket inference** (PHD≈RING fold) not supported by the cached AIRE evidence, which characterizes the PHD as a histone-recognition module, not a catalytic ligase. Verdict: over-reaches as currently projected; treat as candidate requiring direct ubiquitin-transfer evidence, not an automatic ADD. (Some non-cached mouse literature reports AIRE E2-binding/E3-like activity — flag for full-text check before any REMOVE/ADD verdict; reviewer's conservative non-adoption is defensible.)
- **Mapping strategy:** The RING-variant group→GO:0061630 propagation is biologically safe for canonical RING E3s but **mis-fires on the PHD/"other" subtype** that AIRE occupies. The subtype is already no_mapping; the issue is the parent group propagating catalytic activity down to a histone-reader PHD. Mapping should not project GO:0061630 onto PHD-only members lacking ligase evidence.
- **Evidence alignment:** Divergent. PN cites PMIDs 14734522 and 15150263 (not in the review's reference list); review is built on the chromatin/transcription corpus (PMID:11533054, 18292755, 19446523, 26084028). No PMID overlap — the PN E3 case rests on references the review never adjudicated.
- **Verdict:** PN E3-ligase placement/projection over-reaches for AIRE; review correctly withholds GO:0061630 pending direct evidence.
- **Recommended edits:** [MAP] Mark AIRE (and other PHD-"other" members) as a gene-level exception to the RING-variant→GO:0061630 propagation, or downgrade that subtree to context_only, since PHD-reader members are not demonstrated catalytic E3s. [REF] Adjudicate PMID:14734522 and PMID:15150263 (the PN E3 references) — fetch full text and record a reference_review before any E3 verdict.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AIRE/AIRE-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING variant | PHD | other
- UniProt: O43918
- In branches: UPS
- Signature domains: IPR001965
- Auxiliary domains: (none)
- PN references (titles):
    - 14734522
    - 15150263
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|PHD|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|PHD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
