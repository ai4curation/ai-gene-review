# AAAS PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NRG9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1325)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AAAS/AAAS-ai-review.yaml](AAAS-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AAAS/AAAS-ai-review.html](AAAS-ai-review.html)
- Gene notes: present - [genes/human/AAAS/AAAS-notes.md](AAAS-notes.md)
- GOA TSV: present - [genes/human/AAAS/AAAS-goa.tsv](AAAS-goa.tsv)
- UniProt record: present - [genes/human/AAAS/AAAS-uniprot.txt](AAAS-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AAAS.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AAAS.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AAAS.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AAAS.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AAAS/AAAS-deep-research-falcon.md](AAAS-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AAAS encodes ALADIN, a WD-repeat scaffold nucleoporin of the nuclear pore complex. ALADIN is anchored at the nuclear envelope through NDC1 and contributes to normal NPC-associated nucleocytoplasmic transport, especially in tissues affected by triple-A syndrome such as adrenal, gastrointestinal, and neural systems. In mitosis, ALADIN also localizes to spindle structures and helps spatially regulate inactive Aurora A and downstream spindle factors, supporting robust spindle formation and chromosome alignment.
- Existing/core annotation action counts: ACCEPT: 45; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 2; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Consistent. Deep research (NDC1-anchored NPC scaffold / selective transport regulator), the review (ALADIN nucleoporin; nuclear pore + nucleocytoplasmic transport; plus a mitotic spindle/Aurora-A side role), and the PN annotation all agree on the NPC/transport identity. The review explicitly engages the PN projection and declines GO:0015031 as too broad, retaining the more specific GO:0006913 nucleocytoplasmic transport instead. This is a deliberate, documented divergence, not a contradiction.
- **PN story / NEW pressure:** PN's "protein transport" story is already captured at a more informative level by existing GO:0006913 nucleocytoplasmic transport (IBA/NAS) and GO:0005643 nuclear pore (multiple evidence codes). GO:0015031 is a real term but is a broad parent of GO:0006913. Conclusion: **already captured** (more specifically); PN's class-level projection over-reaches toward a broad parent.
- **Evidence alignment:** PN dossier lists no reference titles. Review cites ALADIN-specific PMIDs (12730363, 19782045 NDC1 anchoring, 27016207, 24315095) plus the spindle paper (26246606) — consistent with the NPC node; the spindle/Aurora-A biology is outside the PN nuclear-transport frame (not in PN, legitimately reviewer-added). No citation conflict.
- **Verdict:** Consistent; PN protein-transport projection correctly rejected as broader (review keeps narrower GO:0006913). No edits warranted.

## Full Consistency Review

- **UniProt:** Q9NRG9 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Nuclear proteostasis|Protein transport|Nuclear pore complex` ; **PN-node mapping:** group `Nuclear pore complex`=mapped→GO:0005643 nuclear pore (already_in_goa_exact); class `Protein transport`=mapped→**GO:0015031 protein transport** (new_to_goa); branch `Nuclear proteostasis`=no_mapping.
- **Consistency:** Consistent. Deep research (NDC1-anchored NPC scaffold / selective transport regulator), the review (ALADIN nucleoporin; nuclear pore + nucleocytoplasmic transport; plus a mitotic spindle/Aurora-A side role), and the PN annotation all agree on the NPC/transport identity. The review explicitly engages the PN projection and declines GO:0015031 as too broad, retaining the more specific GO:0006913 nucleocytoplasmic transport instead. This is a deliberate, documented divergence, not a contradiction.
- **PN story / NEW pressure:** PN's "protein transport" story is already captured at a more informative level by existing GO:0006913 nucleocytoplasmic transport (IBA/NAS) and GO:0005643 nuclear pore (multiple evidence codes). GO:0015031 is a real term but is a broad parent of GO:0006913. Conclusion: **already captured** (more specifically); PN's class-level projection over-reaches toward a broad parent.
- **Mapping strategy:** Matches the TOMM20/HSPA8/RAB7A precedent — the PN-projected GO:0015031 is broader than what the review already holds and is correctly NOT added. Group-node GO:0005643 is right (already in GOA). Class-node `Protein transport`→GO:0015031 should be treated as context-only / non-propagating for AAAS, since gene-specific evidence supports the narrower nucleocytoplasmic-transport term.
- **Evidence alignment:** PN dossier lists no reference titles. Review cites ALADIN-specific PMIDs (12730363, 19782045 NDC1 anchoring, 27016207, 24315095) plus the spindle paper (26246606) — consistent with the NPC node; the spindle/Aurora-A biology is outside the PN nuclear-transport frame (not in PN, legitimately reviewer-added). No citation conflict.
- **Verdict:** Consistent; PN protein-transport projection correctly rejected as broader (review keeps narrower GO:0006913). No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AAAS/AAAS-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Nuclear proteostasis | Protein transport | Nuclear pore complex
- UniProt: Q9NRG9
- In branches: NU
- PN-node mapping records (path + ancestors):
    - [group] Nuclear proteostasis|Protein transport|Nuclear pore complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005643 nuclear pore]
        rationale: This PN group denotes core components of the nuclear pore complex. The closest current GO target in the local ontology cache is the cellular-component term nuclear pore.
    - [class] Nuclear proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN nuclear Protein transport class covers the machinery and routes that move proteins across the nuclear envelope. GO protein transport is the correct propagation target, although the PN class is specialized to the nuclear compartment.
    - [branch] Nuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Nuclear proteostasis|Protein transport
- GO:0005643 nuclear pore | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Nuclear proteostasis|Protein transport|Nuclear pore complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
