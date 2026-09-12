# MCTS1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9ULC4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MCTS1/MCTS1-ai-review.yaml](MCTS1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/MCTS1/MCTS1-ai-review.html](MCTS1-ai-review.html)
- Gene notes: present - [genes/human/MCTS1/MCTS1-notes.md](MCTS1-notes.md)
- GOA TSV: present - [genes/human/MCTS1/MCTS1-goa.tsv](MCTS1-goa.tsv)
- UniProt record: present - [genes/human/MCTS1/MCTS1-uniprot.txt](MCTS1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MCTS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MCTS1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MCTS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MCTS1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MCTS1 (Malignant T-cell-amplified sequence 1, MCT-1) is a cytoplasmic PUA-domain RNA-binding protein that, together with its obligate partner DENR, forms the MCTS1-DENR heterodimer, a non-canonical translation factor equivalent to eIF2D (Ligatin) split into two polypeptides (MCTS1 corresponds to the N-terminal half and DENR to the C-terminal SUI1 half). MCTS1 contributes the PUA domain that engages mRNA/the cap region and binds the 40S small ribosomal subunit, and recruits DENR. The complex acts at the post-termination 40S ribosome to promote translation reinitiation, particularly after short upstream ORFs (uORFs), and to recycle/recover post-termination 40S subunits by promoting release of deacylated tRNA and mRNA after ABCE1-mediated ribosome splitting; it also delivers initiator tRNA to the 40S P-site in an eIF2-independent manner when the start codon is positioned in the P-site (as on HCV-like IRESs). MCTS1-DENR-dependent reinitiation governs translation of a specific set of mRNAs (including JAK2) and is required for IFN-gamma immunity. MCTS1 was originally identified as an oncogene amplified in T-cell lymphoma.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 9

## PN Consistency Summary

- **Consistency:** Notes, review YAML, and deep-research are internally consistent and high quality: MCTS1 is the PUA-domain subunit of the eIF2D-like MCTS1-DENR reinitiation/recycling factor. The one tension is between the PN *taxonomy label* ("Translation termination | tRNA, mRNA release") and the biology: MCTS1 acts at the **post-termination** 40S (recycling/reinitiation), not in peptide-chain termination itself. The review correctly annotates GO:0032790 ribosome disassembly + GO:0002188 translation reinitiation, never GO:0006415. The leaf node is `no_mapping`, so no contradiction is projected onto MCTS1.
- **PN story / NEW pressure:** No NEW pressure. MCTS1's reinitiation/40S-recycling roles are already richly captured in GOA (GO:0002188 IDA/IMP, GO:0032790 IMP/IDA, GO:0003743, GO:0043024, GO:0001731) and accepted. The PN "tRNA, mRNA release" subtype maps to nothing. Already captured.
- **Evidence alignment:** PN row 1 carries no reference titles; review anchors on PMID:20713520, 29889857, 37875108, 16982740 (all VERIFIED). No divergence to reconcile.
- **Verdict:** Consistent; no changes. PN leaf correctly `no_mapping`; do not project GO:0006415 onto MCTS1 (it is post-termination recycling, not termination).

## Full Consistency Review

- **UniProt:** Q9ULC4 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|tRNA, mRNA release` ; **PN-node mapping:** type=no_mapping (no GO); only the parent *group* "Translation termination" is mapped (GO:0006415 translational termination, ok_for_propagation), with the class/branch context_only.
- **Consistency:** Notes, review YAML, and deep-research are internally consistent and high quality: MCTS1 is the PUA-domain subunit of the eIF2D-like MCTS1-DENR reinitiation/recycling factor. The one tension is between the PN *taxonomy label* ("Translation termination | tRNA, mRNA release") and the biology: MCTS1 acts at the **post-termination** 40S (recycling/reinitiation), not in peptide-chain termination itself. The review correctly annotates GO:0032790 ribosome disassembly + GO:0002188 translation reinitiation, never GO:0006415. The leaf node is `no_mapping`, so no contradiction is projected onto MCTS1.
- **PN story / NEW pressure:** No NEW pressure. MCTS1's reinitiation/40S-recycling roles are already richly captured in GOA (GO:0002188 IDA/IMP, GO:0032790 IMP/IDA, GO:0003743, GO:0043024, GO:0001731) and accepted. The PN "tRNA, mRNA release" subtype maps to nothing. Already captured.
- **Mapping strategy:** This gene does not change the node mapping. The leaf staying `no_mapping` is correct — MCTS1 release/recycling is not the same as the group's GO:0006415 termination. The group-level GO:0006415 projection (which MCTS1 does **not** inherit) is reasonable for true eRF/release-factor members but would be a mis-annotation if applied to MCTS1; current scoping correctly avoids that.
- **Evidence alignment:** PN row 1 carries no reference titles; review anchors on PMID:20713520, 29889857, 37875108, 16982740 (all VERIFIED). No divergence to reconcile.
- **Verdict:** Consistent; no changes. PN leaf correctly `no_mapping`; do not project GO:0006415 onto MCTS1 (it is post-termination recycling, not termination).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/MCTS1/MCTS1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation termination | tRNA, mRNA release
- UniProt: Q9ULC4
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
- GO:0006415 translational termination | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Translation termination

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
