# ABCE1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P61221
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1321)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/ABCE1/ABCE1-ai-review.yaml](ABCE1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ABCE1/ABCE1-ai-review.html](ABCE1-ai-review.html)
- Gene notes: present - [genes/human/ABCE1/ABCE1-notes.md](ABCE1-notes.md)
- GOA TSV: present - [genes/human/ABCE1/ABCE1-goa.tsv](ABCE1-goa.tsv)
- UniProt record: present - [genes/human/ABCE1/ABCE1-uniprot.txt](ABCE1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ABCE1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ABCE1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABCE1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABCE1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ABCE1/ABCE1-deep-research-falcon.md](ABCE1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ABCE1 is a highly conserved cytosolic Fe-S ABC-family ATPase that drives eukaryotic ribosome recycling. After canonical termination, or after PELO/HBS1L recognition of stalled or vacant ribosomes, ABCE1 uses ATP hydrolysis to split 80S ribosomes into 60S and 40S subunits, thereby coupling translational termination, ribosome-associated quality control, and re-use of ribosomal subunits. ABCE1 contains an N-terminal 4Fe-4S cluster binding region and two ABC nucleotide-binding domains. It was originally identified as RNase L inhibitor/RLI and can inhibit the 2-5A/RNASEL pathway, but current biochemical and genetic evidence supports ribosome recycling as its core conserved function.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 2; NEW: 1; REMOVE: 6

## PN Consistency Summary

- **Consistency:** Strong, mutually consistent. Deep research (Fe-S ABC ATPase, core = ATP-driven ribosome recycling/splitting, with eRF1/eRF3 in termination and PELO/HBS1L in rescue), the review, the PN annotation (termination + ribosomal rescue), and the PN-node mappings all agree. Review accepts GO:0006415 (termination), GO:0072344 (rescue of stalled cytosolic ribosome), and adds GO:0006515 as NEW (IC) — exactly the three PN-projected terms. No contradictions.
- **PN story / NEW pressure:** PN asserts ribosome-associated QC; review already independently added GO:0006515 (NEW/IC, verified real) plus GO:0032790 ribosome disassembly as the most precise core term. All PN-projected terms verified real (GO:0072344, GO:0006415, GO:0006515). Conclusion: **already captured** — PN adds no term the review lacks; review is in fact more precise (adds GO:0032790).
- **Evidence alignment:** PN dossier lists no reference titles for ABCE1; alignment is via projected-term provenance. Review's supporting PMIDs (20122402, 21448132) plus Reactome RQC events (R-HSA-9948299/9955731) cover the same termination + rescue biology the PN nodes encode. No divergence.
- **Verdict:** Fully consistent; PN already captured and review is more granular. No edits warranted.

## Full Consistency Review

- **UniProt:** P61221 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|Ribosome splitting` (type=no_mapping) AND `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue` ; **PN-node mapping:** group `Translation termination`=mapped→GO:0006415; RQC-rescue type=mapped→GO:0072344; RQC group=mapped→GO:0006515; class/branch context_only (GO:0002181/GO:0006412 too_broad).
- **Consistency:** Strong, mutually consistent. Deep research (Fe-S ABC ATPase, core = ATP-driven ribosome recycling/splitting, with eRF1/eRF3 in termination and PELO/HBS1L in rescue), the review, the PN annotation (termination + ribosomal rescue), and the PN-node mappings all agree. Review accepts GO:0006415 (termination), GO:0072344 (rescue of stalled cytosolic ribosome), and adds GO:0006515 as NEW (IC) — exactly the three PN-projected terms. No contradictions.
- **PN story / NEW pressure:** PN asserts ribosome-associated QC; review already independently added GO:0006515 (NEW/IC, verified real) plus GO:0032790 ribosome disassembly as the most precise core term. All PN-projected terms verified real (GO:0072344, GO:0006415, GO:0006515). Conclusion: **already captured** — PN adds no term the review lacks; review is in fact more precise (adds GO:0032790).
- **Mapping strategy:** No change needed. The three "ok_for_propagation" projections are all present in GOA/review (goa_status already_in_goa_exact for two; GO:0006515 new and accepted). The class/branch context_only calls are correct (too broad). Unlike the TOMM20/HSPA8/RAB7A precedent, these PN projections are NOT broader than the review and were accepted.
- **Evidence alignment:** PN dossier lists no reference titles for ABCE1; alignment is via projected-term provenance. Review's supporting PMIDs (20122402, 21448132) plus Reactome RQC events (R-HSA-9948299/9955731) cover the same termination + rescue biology the PN nodes encode. No divergence.
- **Verdict:** Fully consistent; PN already captured and review is more granular. No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABCE1/ABCE1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Translation termination | Ribosome splitting
- UniProt: P61221
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation termination|Ribosome splitting
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

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: P61221
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072344 rescue of stalled cytosolic ribosome]
        rationale: This PN RQC type denotes rescue of stalled cytosolic ribosomes. The matching GO process term is the direct target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (3)
- GO:0006415 translational termination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Translation termination
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
