# GTPBP6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O43824
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GTPBP6/GTPBP6-ai-review.yaml](GTPBP6-ai-review.yaml)
- AIGR review HTML: present - [genes/human/GTPBP6/GTPBP6-ai-review.html](GTPBP6-ai-review.html)
- Gene notes: present - [genes/human/GTPBP6/GTPBP6-notes.md](GTPBP6-notes.md)
- GOA TSV: present - [genes/human/GTPBP6/GTPBP6-goa.tsv](GTPBP6-goa.tsv)
- UniProt record: present - [genes/human/GTPBP6/GTPBP6-uniprot.txt](GTPBP6-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GTPBP6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GTPBP6.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GTPBP6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GTPBP6.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: GTPBP6 (Putative GTP-binding protein 6, PGPL) is a TRAFAC-class OBG-HflX-like GTPase encoded by a pseudoautosomal gene near the Xp/Yp telomere. It functions in mitochondria as one of several conserved GTPases (alongside GTPBP5, GTPBP7 and GTPBP10) that drive late maturation of the mitochondrial large ribosomal subunit (mtLSU). GTPBP6 acts at a final step of mtLSU biogenesis, triggering a molecular switch that drives progression to a near-mature peptidyl transferase centre (PTC), and additionally has a role in recycling/dissociation of mature mitochondrial ribosomes, giving it a dual role in mitoribosome biogenesis and recycling. Its activity is GTP-dependent, consistent with the conserved G-domain motifs of the OBG-HflX-like family.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Partial mismatch. The review and notes cover ONLY the biogenesis arm (row 1): GO:1902775 mitochondrial large ribosomal subunit assembly (IDA), GO:0043023 mtLSU binding (IDA), mitochondrion, GTP binding. The review `description` does mention "recycling/dissociation of mature mitochondrial ribosomes ... dual role" (PMID:34135319), which maps to PN row 2's ribosome-rescue/recycling concept — but the review carries NO process annotation for it. PN row 2's GO:7770016 (rescue of stalled mitochondrial ribosome) and GO:0070126 (mitochondrial translational termination) are therefore absent from the review. Note: PN's "39S subunit assembly" maps to GO:0061668 (mito ribosome assembly, parent) whereas the review uses the more specific GO:1902775 (mtLSU assembly) — review is appropriately narrower.
- **PN story / NEW pressure:** PN row 2 asserts a stalled-mitoribosome-rescue/termination role not in GTPBP6 GOA and not in the review's annotations. Both projected terms verified real (GO:7770016 def: "freeing the ribosome from the stalled translation complex"; GO:0070126). However the review's recycling claim is dissociation of MATURE mitoribosomes (PMID:34135319), which is ribosome recycling, not stalled-ribosome rescue/termination — so GO:7770016 (stalled) may over-reach relative to the actual evidence; mitochondrial ribosome recycling / GO:0070126 is the better-fitting concept. Conclusion: biogenesis already captured (more specifically); row-2 termination story is **over-reaches as "stalled-ribosome rescue"** but a recycling term is defensible.
- **Evidence alignment:** PN lists no titles. Review anchors on PMID:34135319 (the single key structural paper, supports both biogenesis AND recycling), PMID:34800366 (mito proteome), PMID:9466997 (cloning). PN row 2 cites no PMID to compare.
- **Verdict:** Mostly consistent on biogenesis (already captured, review narrower); row-2 stalled-ribosome-rescue projection over-reaches vs the recycling evidence. **Recommended edits:** keep GO:7770016 as context-only / do not propagate to GTPBP6 unless stalled-ribosome evidence is found [MAP]; optionally add a mitochondrial-ribosome-recycling process annotation (anchored to PMID:34135319 dual-role) to capture row 2 accurately [YAML].

## Full Consistency Review

- **UniProt:** O43824 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** TWO rows. Row 1 `Translation|Mitochondrial translation|Mitoribosome biogenesis factor|39S subunit assembly` (type & group=mapped→GO:0061668 mitochondrial ribosome assembly). Row 2 `Translation|Mitochondrial translation|Translation termination|Termination on stalled ribosomes` (type=mapped→GO:7770016 rescue of stalled mitochondrial ribosome [new_to_goa]; group=mapped→GO:0070126 mitochondrial translational termination [new_to_goa]). Class/branch=context_only.
- **Consistency:** Partial mismatch. The review and notes cover ONLY the biogenesis arm (row 1): GO:1902775 mitochondrial large ribosomal subunit assembly (IDA), GO:0043023 mtLSU binding (IDA), mitochondrion, GTP binding. The review `description` does mention "recycling/dissociation of mature mitochondrial ribosomes ... dual role" (PMID:34135319), which maps to PN row 2's ribosome-rescue/recycling concept — but the review carries NO process annotation for it. PN row 2's GO:7770016 (rescue of stalled mitochondrial ribosome) and GO:0070126 (mitochondrial translational termination) are therefore absent from the review. Note: PN's "39S subunit assembly" maps to GO:0061668 (mito ribosome assembly, parent) whereas the review uses the more specific GO:1902775 (mtLSU assembly) — review is appropriately narrower.
- **PN story / NEW pressure:** PN row 2 asserts a stalled-mitoribosome-rescue/termination role not in GTPBP6 GOA and not in the review's annotations. Both projected terms verified real (GO:7770016 def: "freeing the ribosome from the stalled translation complex"; GO:0070126). However the review's recycling claim is dissociation of MATURE mitoribosomes (PMID:34135319), which is ribosome recycling, not stalled-ribosome rescue/termination — so GO:7770016 (stalled) may over-reach relative to the actual evidence; mitochondrial ribosome recycling / GO:0070126 is the better-fitting concept. Conclusion: biogenesis already captured (more specifically); row-2 termination story is **over-reaches as "stalled-ribosome rescue"** but a recycling term is defensible.
- **Mapping strategy:** Row 1 fine. Row 2 changes nothing in the review and risks projecting a stalled-rescue term onto a recycling function — recommend treating GO:7770016 as context-only for GTPBP6 pending evidence that GTPBP6 acts on STALLED (not mature) mitoribosomes.
- **Evidence alignment:** PN lists no titles. Review anchors on PMID:34135319 (the single key structural paper, supports both biogenesis AND recycling), PMID:34800366 (mito proteome), PMID:9466997 (cloning). PN row 2 cites no PMID to compare.
- **Verdict:** Mostly consistent on biogenesis (already captured, review narrower); row-2 stalled-ribosome-rescue projection over-reaches vs the recycling evidence. **Recommended edits:** keep GO:7770016 as context-only / do not propagate to GTPBP6 unless stalled-ribosome evidence is found [MAP]; optionally add a mitochondrial-ribosome-recycling process annotation (anchored to PMID:34135319 dual-role) to capture row 2 accurately [YAML].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/GTPBP6/GTPBP6-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Mitochondrial translation | Mitoribosome biogenesis factor | 39S subunit assembly
- UniProt: O43824
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Mitochondrial translation|Mitoribosome biogenesis factor|39S subunit assembly
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061668 mitochondrial ribosome assembly]
        rationale: This PN type denotes 39S mitoribosomal subunit assembly factors. Mitochondrial ribosome assembly is the shared process target.
    - [group] Translation|Mitochondrial translation|Mitoribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061668 mitochondrial ribosome assembly]
        rationale: This PN group denotes factors for mitoribosome assembly and maturation. Mitochondrial ribosome assembly is the most specific shared process target.
    - [class] Translation|Mitochondrial translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0032543 mitochondrial translation]
        rationale: This PN class is a useful mitochondrial-translation context, but it contains ribosome components, assembly factors, tRNA synthetases, regulatory factors, and translation factors. Direct propagation to mitochondrial translation would over-annotate several adjacent machinery classes, so the relationship is retained as context only.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Translation | Mitochondrial translation | Translation termination | Termination on stalled ribosomes
- UniProt: O43824
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Mitochondrial translation|Translation termination|Termination on stalled ribosomes
        status=mapped scope=ok_for_propagation_to_go GO=[GO:7770016 rescue of stalled mitochondrial ribosome]
        rationale: This PN type denotes handling of stalled mitochondrial ribosomes. The GO rescue of stalled mitochondrial ribosome process is the best matching target.
    - [group] Translation|Mitochondrial translation|Translation termination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070126 mitochondrial translational termination]
        rationale: This PN group denotes mitochondrial translation termination machinery. The matching GO process term is appropriate for propagation.
    - [class] Translation|Mitochondrial translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0032543 mitochondrial translation]
        rationale: This PN class is a useful mitochondrial-translation context, but it contains ribosome components, assembly factors, tRNA synthetases, regulatory factors, and translation factors. Direct propagation to mitochondrial translation would over-annotate several adjacent machinery classes, so the relationship is retained as context only.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (4)
- GO:0061668 mitochondrial ribosome assembly | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Mitochondrial translation|Mitoribosome biogenesis factor
- GO:0061668 mitochondrial ribosome assembly | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Mitochondrial translation|Mitoribosome biogenesis factor|39S subunit assembly
- GO:0070126 mitochondrial translational termination | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Mitochondrial translation|Translation termination
- GO:7770016 rescue of stalled mitochondrial ribosome | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Mitochondrial translation|Translation termination|Termination on stalled ribosomes

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
