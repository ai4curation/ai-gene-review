# ZNF598 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q86UK7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ZNF598/ZNF598-ai-review.yaml](ZNF598-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ZNF598/ZNF598-ai-review.html](ZNF598-ai-review.html)
- Gene notes: present - [genes/human/ZNF598/ZNF598-notes.md](ZNF598-notes.md)
- GOA TSV: present - [genes/human/ZNF598/ZNF598-goa.tsv](ZNF598-goa.tsv)
- UniProt record: present - [genes/human/ZNF598/ZNF598-uniprot.txt](ZNF598-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ZNF598.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ZNF598.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ZNF598.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ZNF598.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ZNF598 is a cytosolic RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27), the human ortholog of yeast Hel2/RQT1, that initiates ribosome-associated quality control (RQC) by acting as the sensor of ribosome collisions. When a trailing ribosome catches up with a slower or stalled leading ribosome (for example during translation of poly(A) stretches or other problematic sequences), ZNF598 specifically recognizes and binds the resulting collided di-ribosome (disome) via its extensive 40S-40S interface. Using the E2 enzyme UBE2D3, it then monoubiquitinates the 40S ribosomal proteins eS10 (RPS10) and uS3 (RPS3) and adds K63-linked polyubiquitin to uS10 (RPS20). This ubiquitin mark recruits the RQT (ribosome quality control trigger) complex, which dissociates the stalled ribosome into subunits and commits the nascent chain to the downstream RQC degradation machinery. ZNF598 is also an RNA-binding protein and a component of the 4EHP-GYF2 complex (with EIF4E2 and GIGYF2), acting as an adaptor that recruits this translational repressor to defective mRNAs and contributing to translation-coupled mRNA decay; it has additional reported roles as a negative regulator of interferon-stimulated gene expression. ZNF598 acts in the cytosol in association with cytosolic ribosomes.
- Existing/core annotation action counts: ACCEPT: 31; KEEP_AS_NON_CORE: 14

## PN Consistency Summary

- **Consistency:** Fully consistent and exemplary. Notes, review, and PN agree ZNF598 is the RING E3 (Hel2 ortholog) that senses ribosome collisions and ubiquitinates 40S eS10/RPS10, uS3/RPS3 (mono) and uS10/RPS20 (K63) via UBE2D3 to initiate RQC. Review captures this richly: GO:0061630 (IDA), GO:0170011 stalled ribosome sensor activity (IDA), GO:0072344 (many IDA/IMP), GO:1990116, GO:0070534, GO:0006513, GO:0043022. The two PN-projected MF/process targets (GO:0072344, GO:0061630) are both already_in_goa_exact and present in the review.
- **PN story / NEW pressure:** PN's RQC-group GO:0006515 (verified real, non-obsolete) is the only new_to_goa projection. The review already captures the RQC process at finer grain via GO:0072344 (rescue) AND GO:1990116 (ribosome-associated ubiquitin-dependent protein catabolic process, verified real) — both more specific than GO:0006515. Conclude: already captured (more specifically); GO:0006515 would be a defensible-but-broader add, not required.
- **Evidence alignment:** PN UPS row cites "19489725/rev" (a RING E3 review); RQC TR row has no titled reference. The review's foundational RQC papers (PMID:28065601, 28132843, 28685749, 30293783, 36302773, 32099016) are absent from the PN rows — large divergence, with the review far richer and PN citing only a generic E3 review.
- **Verdict:** Consistent and well-captured; ZNF598 is the canonical RQC-initiating E3. PN's GO:0006515 is broader than the review's GO:0072344/GO:1990116; no NEW term needed.

## Full Consistency Review

- **UniProt:** Q86UK7 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** TR `Cytosolic translation|Ribosome-associated QC|Ribosomal rescue`; UPS `E3 ubiquitin and UBL ligases|RING|other|other` ; **PN-node mapping:** RQC type→GO:0072344 rescue of stalled cytosolic ribosome (mapped, already_in_goa_exact); RQC group→GO:0006515 protein QC for misfolded/incompletely synthesized proteins (new_to_goa); E3 RING group→GO:0061630 ubiquitin protein ligase activity (already_in_goa_exact); class→GO:0061630 (context_only); type/subtype/branch = no_mapping.
- **Consistency:** Fully consistent and exemplary. Notes, review, and PN agree ZNF598 is the RING E3 (Hel2 ortholog) that senses ribosome collisions and ubiquitinates 40S eS10/RPS10, uS3/RPS3 (mono) and uS10/RPS20 (K63) via UBE2D3 to initiate RQC. Review captures this richly: GO:0061630 (IDA), GO:0170011 stalled ribosome sensor activity (IDA), GO:0072344 (many IDA/IMP), GO:1990116, GO:0070534, GO:0006513, GO:0043022. The two PN-projected MF/process targets (GO:0072344, GO:0061630) are both already_in_goa_exact and present in the review.
- **PN story / NEW pressure:** PN's RQC-group GO:0006515 (verified real, non-obsolete) is the only new_to_goa projection. The review already captures the RQC process at finer grain via GO:0072344 (rescue) AND GO:1990116 (ribosome-associated ubiquitin-dependent protein catabolic process, verified real) — both more specific than GO:0006515. Conclude: already captured (more specifically); GO:0006515 would be a defensible-but-broader add, not required.
- **Mapping strategy:** ZNF598 strongly supports both nodes; it does not change the mapping. PN-projected GO:0006515 is broader than the review's GO:0072344/GO:1990116 — a "broader than review" case (cf. TOMM20/HSPA8/RAB7A precedent). E3 RING group→GO:0061630 exact-matches the review core MF. Status/scope correct throughout.
- **Evidence alignment:** PN UPS row cites "19489725/rev" (a RING E3 review); RQC TR row has no titled reference. The review's foundational RQC papers (PMID:28065601, 28132843, 28685749, 30293783, 36302773, 32099016) are absent from the PN rows — large divergence, with the review far richer and PN citing only a generic E3 review.
- **Verdict:** Consistent and well-captured; ZNF598 is the canonical RQC-initiating E3. PN's GO:0006515 is broader than the review's GO:0072344/GO:1990116; no NEW term needed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/ZNF598/ZNF598-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q86UK7
- In branches: TR, UPS
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

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | other | other
- UniProt: Q86UK7
- In branches: TR, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR013087
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
