# EIF2D PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P41214
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EIF2D/EIF2D-ai-review.yaml](EIF2D-ai-review.yaml)
- AIGR review HTML: present - [genes/human/EIF2D/EIF2D-ai-review.html](EIF2D-ai-review.html)
- Gene notes: present - [genes/human/EIF2D/EIF2D-notes.md](EIF2D-notes.md)
- GOA TSV: present - [genes/human/EIF2D/EIF2D-goa.tsv](EIF2D-goa.tsv)
- UniProt record: present - [genes/human/EIF2D/EIF2D-uniprot.txt](EIF2D-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EIF2D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EIF2D.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF2D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF2D.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: EIF2D (also called Ligatin) is a cytoplasmic non-canonical translation factor and the single-polypeptide counterpart of the MCTS1-DENR heterodimer (MCTS1 and DENR together correspond to the N- and C-terminal halves of Ligatin). Containing SUI1, PUA and SWIB modules, EIF2D delivers initiator (Met) and, uniquely, elongator (non-Met) tRNAs into the P-site of the 40S small ribosomal subunit in a GTP-independent, eIF2-independent manner, specifically when the start codon is already positioned in the P-site (as on certain IRESs, leaderless and A-rich mRNAs). In addition to its role in initiation, EIF2D promotes recycling of post-termination 40S subunits by promoting release of deacylated tRNA and mRNA following ABCE1-mediated dissociation of post-termination ribosomal complexes. It is broadly expressed and conserved across eukaryotes.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 1; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Review/notes are accurate and self-consistent: EIF2D (Ligatin) is the single-polypeptide eIF2D-like factor that does GTP-independent P-site tRNA delivery and post-termination **40S recycling/reinitiation** (core MF GO:0003743). This CONTRADICTS the PN "Translation termination" placement and GO:0006415 projection — EIF2D is not a release factor. (Same node mis-classification as DENR, its split-paralog partner.)
- **PN story / NEW pressure:** Projected GO:0006415 translational termination is `more_specific_than_existing_goa`. Verified (OLS): GO:0006415 = polypeptide release at a stop codon — not EIF2D's activity. EIF2D's real roles (GO:0001731 preinitiation-complex formation, GO:0032790 ribosome disassembly/recycling, GO:0003743 initiation-factor activity) are **already in GOA** and reviewed. The projection **over-reaches / is biologically wrong**; no defensible NEW termination term.
- **Evidence alignment:** Dossier carries no reference titles. Review anchors PMID:20566627 (GTP-independent P-site tRNA delivery) and PMID:20713520 (Ligatin recycling), both VERIFIED — about initiation/recycling, none about termination. Divergence by omission in dossier.
- **Verdict:** Mapping mismatch — PN "translation termination" + GO:0006415 contradicts EIF2D's initiation/recycling biology already in GOA. **Recommended edits:** [MAP] do not project GO:0006415 to EIF2D; reclassify PN node toward reinitiation/40S recycling (GO:0001731 / GO:0032790 already in GOA).

## Full Consistency Review

- **UniProt:** P41214 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|tRNA, mRNA release` ; **PN-node mapping:** group `Translation termination` → GO:0006415 translational termination (mapped, ok_for_propagation); type `tRNA, mRNA release` no_mapping.
- **Consistency:** Review/notes are accurate and self-consistent: EIF2D (Ligatin) is the single-polypeptide eIF2D-like factor that does GTP-independent P-site tRNA delivery and post-termination **40S recycling/reinitiation** (core MF GO:0003743). This CONTRADICTS the PN "Translation termination" placement and GO:0006415 projection — EIF2D is not a release factor. (Same node mis-classification as DENR, its split-paralog partner.)
- **PN story / NEW pressure:** Projected GO:0006415 translational termination is `more_specific_than_existing_goa`. Verified (OLS): GO:0006415 = polypeptide release at a stop codon — not EIF2D's activity. EIF2D's real roles (GO:0001731 preinitiation-complex formation, GO:0032790 ribosome disassembly/recycling, GO:0003743 initiation-factor activity) are **already in GOA** and reviewed. The projection **over-reaches / is biologically wrong**; no defensible NEW termination term.
- **Mapping strategy:** Reinforces the DENR finding: the `Translation termination|tRNA, mRNA release` node lumps post-termination recycling/reinitiation factors (EIF2D, DENR) with genuine release factors. Recommend re-homing EIF2D under reinitiation/40S-recycling and not propagating GO:0006415.
- **Evidence alignment:** Dossier carries no reference titles. Review anchors PMID:20566627 (GTP-independent P-site tRNA delivery) and PMID:20713520 (Ligatin recycling), both VERIFIED — about initiation/recycling, none about termination. Divergence by omission in dossier.
- **Verdict:** Mapping mismatch — PN "translation termination" + GO:0006415 contradicts EIF2D's initiation/recycling biology already in GOA. **Recommended edits:** [MAP] do not project GO:0006415 to EIF2D; reclassify PN node toward reinitiation/40S recycling (GO:0001731 / GO:0032790 already in GOA).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/EIF2D/EIF2D-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation termination | tRNA, mRNA release
- UniProt: P41214
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation termination|tRNA, mRNA release
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Translation termination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006415 translational termination]
        rationale: This PN group denotes cytosolic translation termination and release factors. Translational termination is the shared process target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006415 translational termination | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Translation termination

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
