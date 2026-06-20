# AKIRIN1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H9L7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1360)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AKIRIN1/AKIRIN1-ai-review.yaml](AKIRIN1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AKIRIN1/AKIRIN1-ai-review.html](AKIRIN1-ai-review.html)
- Gene notes: present - [genes/human/AKIRIN1/AKIRIN1-notes.md](AKIRIN1-notes.md)
- GOA TSV: present - [genes/human/AKIRIN1/AKIRIN1-goa.tsv](AKIRIN1-goa.tsv)
- UniProt record: present - [genes/human/AKIRIN1/AKIRIN1-uniprot.txt](AKIRIN1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AKIRIN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AKIRIN1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AKIRIN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AKIRIN1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AKIRIN1/AKIRIN1-deep-research-falcon.md](AKIRIN1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AKIRIN1 encodes a conserved nuclear Akirin-family protein that functions as a transcriptional cofactor in inducible gene-expression programs. It also has a context-dependent promyogenic role supporting myoblast and satellite-cell proliferation and differentiation during muscle repair. The protein localizes to the nucleus and nucleoplasm and is not an enzyme; its main role is to help regulate transcription in chromatin-associated nuclear contexts rather than to catalyze a biochemical reaction.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 11; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Contradiction between PN projection and review. PN projects proteasome binding (GO:0070628) onto AKIRIN1 via the shared "Akirin" adaptor bucket. The review and deep research (falcon) argue this is **paralog over-transfer**: the proteasome-import adaptor activity is established for AKIRIN2 (PMID:34711951), not AKIRIN1. UniProt and the review explicitly contrast AKIRIN1 (nuclear transcriptional cofactor, promyogenic) with AKIRIN2's proteasome role. The review does NOT adopt GO:0070628 and flags the projection as unsupported.
- **PN story / NEW pressure:** PN asserts proteasome binding not in GOA. GO:0070628 is a real term and genuinely absent from AKIRIN1 GOA, but there is **no AKIRIN1-specific primary evidence** for it; the only direct binding datum is an IntAct GOPC interaction (review MODIFY→GO:0044877 protein-containing complex binding). Verdict: over-reaches — this is family/paralog propagation (PLI-like: the wrong Akirin paralog), not a defensible ADD for AKIRIN1.
- **Evidence alignment:** Dossier lists no PN reference titles for AKIRIN1. Review cites PMID:18066067 (conserved nuclear cofactor), PMID:23516508 (promyogenic), and pointedly PMID:34711951 as a **negative contrast** (AKIRIN2-specific). Divergence is in interpretation, not citation.
- **Verdict:** PN GO:0070628 projection over-reaches — paralog mis-transfer from AKIRIN2; review correctly withholds.

## Full Consistency Review

- **UniProt:** Q9H9L7 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|Akirin` ; **PN-node mapping:** Akirin *type* no_mapping; *group* (adaptors) mapped→GO:0070628 (proteasome binding, propagate); class context_only→GO:0000502. Projection: **GO:0070628 new_to_goa**.
- **Consistency:** Contradiction between PN projection and review. PN projects proteasome binding (GO:0070628) onto AKIRIN1 via the shared "Akirin" adaptor bucket. The review and deep research (falcon) argue this is **paralog over-transfer**: the proteasome-import adaptor activity is established for AKIRIN2 (PMID:34711951), not AKIRIN1. UniProt and the review explicitly contrast AKIRIN1 (nuclear transcriptional cofactor, promyogenic) with AKIRIN2's proteasome role. The review does NOT adopt GO:0070628 and flags the projection as unsupported.
- **PN story / NEW pressure:** PN asserts proteasome binding not in GOA. GO:0070628 is a real term and genuinely absent from AKIRIN1 GOA, but there is **no AKIRIN1-specific primary evidence** for it; the only direct binding datum is an IntAct GOPC interaction (review MODIFY→GO:0044877 protein-containing complex binding). Verdict: over-reaches — this is family/paralog propagation (PLI-like: the wrong Akirin paralog), not a defensible ADD for AKIRIN1.
- **Mapping strategy:** The Akirin *type* node groups AKIRIN1+AKIRIN2; the parent "adaptors" group→GO:0070628 propagation is correct for AKIRIN2 but wrong for AKIRIN1. The mapping should split the Akirin type so proteasome binding propagates only to AKIRIN2, or mark AKIRIN1 as a no_mapping/excluded member.
- **Evidence alignment:** Dossier lists no PN reference titles for AKIRIN1. Review cites PMID:18066067 (conserved nuclear cofactor), PMID:23516508 (promyogenic), and pointedly PMID:34711951 as a **negative contrast** (AKIRIN2-specific). Divergence is in interpretation, not citation.
- **Verdict:** PN GO:0070628 projection over-reaches — paralog mis-transfer from AKIRIN2; review correctly withholds.
- **Recommended edits:** [MAP] Split the `adaptors|Akirin` type so GO:0070628 proteasome binding propagates to AKIRIN2 only; mark AKIRIN1 as no_mapping (nuclear transcription cofactor, no proteasome-binding evidence).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AKIRIN1/AKIRIN1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | Proteasome and associated proteins | adaptors | Akirin
- UniProt: Q9H9L7
- In branches: UPS
- Signature domains: IPR024132
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|Akirin
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070628 proteasome binding]
        rationale: This PN group captures proteasome adaptors and shuttle factors. Proteasome binding is the safe shared molecular-function target.
    - [class] Ubiquitin Proteasome System|Proteasome and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0000502 proteasome complex]
        rationale: This class records the proteasome branch context, but descendants include core and regulatory particle subunits, activators, assembly chaperones, adaptors, DUBs, E3 ligases, enzymes, and transcriptional regulators. Propagation should come from narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0070628 proteasome binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
