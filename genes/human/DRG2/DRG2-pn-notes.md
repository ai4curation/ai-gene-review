# DRG2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P55039
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DRG2/DRG2-ai-review.yaml](DRG2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DRG2/DRG2-ai-review.html](DRG2-ai-review.html)
- Gene notes: present - [genes/human/DRG2/DRG2-notes.md](DRG2-notes.md)
- GOA TSV: present - [genes/human/DRG2/DRG2-goa.tsv](DRG2-goa.tsv)
- UniProt record: present - [genes/human/DRG2/DRG2-uniprot.txt](DRG2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DRG2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DRG2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DRG2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DRG2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DRG2 (Developmentally-regulated GTP-binding protein 2) is a translational GTPase of the TRAFAC class, OBG-HflX-like superfamily (DRG/OBG GTPase family). It catalyzes hydrolysis of GTP to GDP, using Mg2+ as cofactor, and belongs to the conserved DRG family of ribosome-associated GTPases. DRG2 is stabilized by and functions together with its DFRP (DRG family regulatory protein) cofactor DFRP2/RWDD1, whose binding protects DRG2 from polyubiquitination and proteolytic degradation. DRG2 is a substrate of the JmjC oxygenase JMJD7, which catalyzes (3S)-lysyl hydroxylation at Lys-21; this modification is associated with RNA binding and a role in translation. DRG2 is found in both the cytoplasm and the nucleus and is most highly expressed in skeletal muscle, heart and kidney. Through its GTPase activity and ribosome/translation association it is implicated in regulation of protein synthesis, and at the cellular level it has been linked to cell proliferation and growth control.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Review and notes are consistent with each other (DRG2 = TRAFAC/OBG-family translational GTPase; core MF GO:0003924 GTPase activity; JMJD7-hydroxylation/RNA-binding context; DFRP2/RWDD1 cofactor). They are NOT consistent with the PN placement: nothing in the review, notes, or GOA establishes DRG2 as a ribosome-associated quality-control / surveillance factor. The review even keeps the broad GO:0002181 cytoplasmic translation as non-core because "the specific regulatory role of human DRG2 in translation is not precisely defined."
- **PN story / NEW pressure:** Dossier projects GO:0006515 protein QC as `new_to_goa`. No evidence (GOA has GO:0002181 + GO:0003924 only; no QC/RQC/rescue terms) supports DRG2 as an RQC factor. Asserting GO:0006515 would be an unsupported functional claim, not merely a broad umbrella — **over-reaches**. No defensible NEW term; if anything the gene is at most a generic ribosome-associated GTPase.
- **Evidence alignment:** Dossier provides no reference titles. Review anchors are PMID:29915238 (JMJD7/GTPase, VERIFIED) and PMID:7929244 (original cloning, VERIFIED) — both about GTPase identity, neither about RQC. Divergence: dossier RQC framing has no supporting citation.
- **Verdict:** GTPase biology is solid, but the PN RQC placement and GO:0006515 projection are unsupported for DRG2. **Recommended edits:** [MAP] do not project GO:0006515 (protein QC) to DRG2 — no RQC/surveillance evidence; GTPase activity (GO:0003924) is the supported core.

## Full Consistency Review

- **UniProt:** P55039 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** type `other RQC processes` no_mapping; group `Ribosome-associated QC` → GO:0006515 protein QC (mapped, ok_for_propagation); class/branch context_only.
- **Consistency:** Review and notes are consistent with each other (DRG2 = TRAFAC/OBG-family translational GTPase; core MF GO:0003924 GTPase activity; JMJD7-hydroxylation/RNA-binding context; DFRP2/RWDD1 cofactor). They are NOT consistent with the PN placement: nothing in the review, notes, or GOA establishes DRG2 as a ribosome-associated quality-control / surveillance factor. The review even keeps the broad GO:0002181 cytoplasmic translation as non-core because "the specific regulatory role of human DRG2 in translation is not precisely defined."
- **PN story / NEW pressure:** Dossier projects GO:0006515 protein QC as `new_to_goa`. No evidence (GOA has GO:0002181 + GO:0003924 only; no QC/RQC/rescue terms) supports DRG2 as an RQC factor. Asserting GO:0006515 would be an unsupported functional claim, not merely a broad umbrella — **over-reaches**. No defensible NEW term; if anything the gene is at most a generic ribosome-associated GTPase.
- **Mapping strategy:** This gene weakens the `Ribosome-associated QC` group → GO:0006515 mapping: DRG2's membership in "other RQC processes" looks like taxonomic placement of a ribosome-associated GTPase rather than a demonstrated QC role. Recommend NOT projecting GO:0006515 onto DRG2 (no QC evidence).
- **Evidence alignment:** Dossier provides no reference titles. Review anchors are PMID:29915238 (JMJD7/GTPase, VERIFIED) and PMID:7929244 (original cloning, VERIFIED) — both about GTPase identity, neither about RQC. Divergence: dossier RQC framing has no supporting citation.
- **Verdict:** GTPase biology is solid, but the PN RQC placement and GO:0006515 projection are unsupported for DRG2. **Recommended edits:** [MAP] do not project GO:0006515 (protein QC) to DRG2 — no RQC/surveillance evidence; GTPase activity (GO:0003924) is the supported core.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/DRG2/DRG2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: P55039
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
