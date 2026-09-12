# GTPBP2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BX10
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GTPBP2/GTPBP2-ai-review.yaml](GTPBP2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/GTPBP2/GTPBP2-ai-review.html](GTPBP2-ai-review.html)
- Gene notes: present - [genes/human/GTPBP2/GTPBP2-notes.md](GTPBP2-notes.md)
- GOA TSV: present - [genes/human/GTPBP2/GTPBP2-goa.tsv](GTPBP2-goa.tsv)
- UniProt record: present - [genes/human/GTPBP2/GTPBP2-uniprot.txt](GTPBP2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GTPBP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GTPBP2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GTPBP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GTPBP2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: GTPBP2 (GTP-binding protein 2) is a cytoplasmic translational GTPase of the TRAFAC-class translation-factor superfamily, related to eEF1A, eRF3, Hbs1 and its paralog GTPBP1. It partners the ribosome-rescue factor PELO and functions in the rescue of ribosomes stalled because of non-functional or deficient tRNA, a role that is especially critical in neurons. Unlike its paralog GTPBP1, GTPBP2 lacks eEF1A-like elongation activity and does not stimulate exosomal mRNA degradation; it has only weak GTP-binding activity that is stimulated by aminoacyl-tRNA. Loss of GTPBP2 (in the context of a destabilized brain-specific tRNA in mouse, and through biallelic loss-of-function in humans) leads to ribosome stalling and neurodegeneration; human GTPBP2 deficiency causes Jaberi-Elahi syndrome, characterized by developmental delay, intellectual disability, movement abnormalities and cerebellar atrophy.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Consistent. Deep research (notes), review, and PN all agree GTPBP2 is a PELO-partnered translational GTPase that rescues ribosomes stalled on deficient/non-functional tRNA (Jaberi-Elahi syndrome, neuronal). No contradictions; the review additionally flags that GTPBP2 lacks eEF1A elongation activity (negated GO:0003746) and binds GTP only weakly — all coherent with the PN "ribosomal rescue" placement.
- **PN story / NEW pressure:** The PN rescue role is NOT captured by any process term in GTPBP2's GOA — the only BP annotation is GO:0006414 translational elongation (IBA), which the review marks MARK_AS_OVER_ANNOTATED. So GTPBP2 has no correct BP term for its actual function. GO:0072344 rescue of stalled cytosolic ribosome (verified real, non-obsolete) is the defensible ADD; GO:0006515 (verified real) is a broader parent and weaker. Conclusion: **ADD GO:0072344** (the review currently leaves the rescue role only in `description`/`core_functions` text, not as a proposed term).
- **Evidence alignment:** PN dossier lists no reference titles. Review/notes anchor on PMID:30108131 (GTPBP1/GTPBP2 GTPases) and UniProt; Ishimura 2014 (mouse Gtpbp2/Pelo) cited in notes but not as a YAML reference. No citation conflict; PN simply carries no PMIDs to compare.
- **Verdict:** Consistent; PN rescue story is real NEW pressure (GOA lacks a correct BP). **Recommended edits:** add GO:0072344 rescue of stalled cytosolic ribosome to `proposed_new_terms` (or as a NEW annotation) [YAML]; consider adding Ishimura 2014 Science to `references` for the PELO-rescue/neurodegeneration evidence [REF].

## Full Consistency Review

- **UniProt:** Q9BX10 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue` ; **PN-node mapping:** type `Ribosomal rescue`=mapped→GO:0072344 rescue of stalled cytosolic ribosome (more_specific_than_existing_goa); group `Ribosome-associated QC`=mapped→GO:0006515 protein quality control (new_to_goa); class/branch=context_only (too broad).
- **Consistency:** Consistent. Deep research (notes), review, and PN all agree GTPBP2 is a PELO-partnered translational GTPase that rescues ribosomes stalled on deficient/non-functional tRNA (Jaberi-Elahi syndrome, neuronal). No contradictions; the review additionally flags that GTPBP2 lacks eEF1A elongation activity (negated GO:0003746) and binds GTP only weakly — all coherent with the PN "ribosomal rescue" placement.
- **PN story / NEW pressure:** The PN rescue role is NOT captured by any process term in GTPBP2's GOA — the only BP annotation is GO:0006414 translational elongation (IBA), which the review marks MARK_AS_OVER_ANNOTATED. So GTPBP2 has no correct BP term for its actual function. GO:0072344 rescue of stalled cytosolic ribosome (verified real, non-obsolete) is the defensible ADD; GO:0006515 (verified real) is a broader parent and weaker. Conclusion: **ADD GO:0072344** (the review currently leaves the rescue role only in `description`/`core_functions` text, not as a proposed term).
- **Mapping strategy:** Node mapping is sound. Type-node GO:0072344 is the right specificity (not broader, unlike the TOMM20/HSPA8 precedent); group-node GO:0006515 is appropriately the fallback parent. The projected term is narrower-or-equal to the review's own functional picture, so no over-reach.
- **Evidence alignment:** PN dossier lists no reference titles. Review/notes anchor on PMID:30108131 (GTPBP1/GTPBP2 GTPases) and UniProt; Ishimura 2014 (mouse Gtpbp2/Pelo) cited in notes but not as a YAML reference. No citation conflict; PN simply carries no PMIDs to compare.
- **Verdict:** Consistent; PN rescue story is real NEW pressure (GOA lacks a correct BP). **Recommended edits:** add GO:0072344 rescue of stalled cytosolic ribosome to `proposed_new_terms` (or as a NEW annotation) [YAML]; consider adding Ishimura 2014 Science to `references` for the PELO-rescue/neurodegeneration evidence [REF].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/GTPBP2/GTPBP2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q9BX10
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

## Projected GO annotations (2)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
