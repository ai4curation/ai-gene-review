# EIF4E2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O60573
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EIF4E2/EIF4E2-ai-review.yaml](EIF4E2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/EIF4E2/EIF4E2-ai-review.html](EIF4E2-ai-review.html)
- Gene notes: present - [genes/human/EIF4E2/EIF4E2-notes.md](EIF4E2-notes.md)
- GOA TSV: present - [genes/human/EIF4E2/EIF4E2-goa.tsv](EIF4E2-goa.tsv)
- UniProt record: present - [genes/human/EIF4E2/EIF4E2-uniprot.txt](EIF4E2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EIF4E2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EIF4E2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF4E2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF4E2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: EIF4E2 (eIF4E homologous protein, 4EHP) is a class II member of the eIF4E cap-binding protein family. It recognizes and binds the 7-methylguanosine (m7G) mRNA 5' cap but, unlike the canonical eIF4E, cannot bind the scaffold eIF4G; it therefore competes with eIF4E for the cap and blocks assembly of the eIF4F initiation complex, acting as a repressor of cap-dependent translation initiation rather than a promoter of it. 4EHP is the catalytic-cap-binding core of the 4EHP-GIGYF2 translational-repressor module: bound to GIGYF2 (and ZNF598/DDX6) it sequesters the cap of specific mRNAs to suppress their translation, including as part of ribosome-associated quality control, where it lowers the translational load on messages that cause ribosome stalling. 4EHP is also an integral component of miRNA-mediated silencing, contributing cap-binding activity that, via 4E-T and the CCR4-NOT complex, represses translation of miRNA targets, and it mediates miR-34a- directed negative-feedback control of IFNB1 (type I interferon) production - a circuit co-opted by SARS-CoV-2 nsp2. It localizes to the cytoplasm and to P-bodies and is itself a substrate for ubiquitylation by the RBR E3 ligase ARIH1/HHARI.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 21; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 3; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent on biology but with a sharp, important divergence on one node. Deep research, notes, and review agree: 4EHP is a cap-binding REPRESSOR that cannot bind eIF4G and is NOT a productive eIF4F component; it acts in the 4EHP-GIGYF1/2 RQC/repression module. The review explicitly REMOVEs GO:0016281 (eukaryotic translation initiation factor 4F complex, IBA) and MARK_AS_OVER_ANNOTATED GO:0006413 (translational initiation) as misleading family-level transfers. The PN-node mapping for the "eIF4F complex" type, however, maps to exactly GO:0016281 and the initiation group to GO:0006413 — the two terms the review rejects/downgrades. Direct contradiction at the eIF4F-complex node.
- **PN story / NEW pressure:** PN's RQC framing (GO:0006515, verified real) is fully borne out — review independently asserts negative regulation of translational initiation (GO:0045947, IDA) and rescue of stalled cytosolic ribosome (GO:0072344, IDA) for the RQC module. GO:0006515 is broader than these but defensible as an RQC umbrella; **already captured** (more specifically) by the review.
- **Evidence alignment:** PN dossier lists no reference titles for EIF4E2; alignment is via projected terms. Review's RQC PMIDs (32726578, 35878012, 22751931, 33053355) cover the same repression/RQC biology the GO:0006515 node encodes. No PMID divergence; the only conflict is term-level (GO:0016281).
- **Verdict:** Biology consistent; one node-level contradiction (PN GO:0016281 vs review REMOVE). RQC story already captured more precisely. **Recommended edits:** [MAP] flag the EIF4E2 "eIF4F complex" type→GO:0016281 projection as inappropriate (4EHP cannot bind eIF4G / is not an eIF4F component — see review REMOVE of GO:0016281); do not propagate GO:0016281 to O60573.

## Full Consistency Review

- **UniProt:** O60573 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation initiation|eIF4F complex` AND `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** initiation type=mapped→GO:0016281 (eIF4F complex); initiation group=mapped→GO:0006413; RQC group=mapped→GO:0006515; RQC type=no_mapping; class/branch context_only (GO:0002181/GO:0006412 too_broad).
- **Consistency:** Mostly consistent on biology but with a sharp, important divergence on one node. Deep research, notes, and review agree: 4EHP is a cap-binding REPRESSOR that cannot bind eIF4G and is NOT a productive eIF4F component; it acts in the 4EHP-GIGYF1/2 RQC/repression module. The review explicitly REMOVEs GO:0016281 (eukaryotic translation initiation factor 4F complex, IBA) and MARK_AS_OVER_ANNOTATED GO:0006413 (translational initiation) as misleading family-level transfers. The PN-node mapping for the "eIF4F complex" type, however, maps to exactly GO:0016281 and the initiation group to GO:0006413 — the two terms the review rejects/downgrades. Direct contradiction at the eIF4F-complex node.
- **PN story / NEW pressure:** PN's RQC framing (GO:0006515, verified real) is fully borne out — review independently asserts negative regulation of translational initiation (GO:0045947, IDA) and rescue of stalled cytosolic ribosome (GO:0072344, IDA) for the RQC module. GO:0006515 is broader than these but defensible as an RQC umbrella; **already captured** (more specifically) by the review.
- **Mapping strategy:** The "eIF4F complex" type→GO:0016281 mapping is wrong for 4EHP and should be revisited at the PN level: 4EHP is a class-II eIF4E paralog that does not assemble into eIF4F. The PN node groups true eIF4F components, but projecting GO:0016281 onto EIF4E2 contradicts curated biology. RQC group→GO:0006515 is acceptable (broad umbrella over the review's GO:0045947/GO:0072344).
- **Evidence alignment:** PN dossier lists no reference titles for EIF4E2; alignment is via projected terms. Review's RQC PMIDs (32726578, 35878012, 22751931, 33053355) cover the same repression/RQC biology the GO:0006515 node encodes. No PMID divergence; the only conflict is term-level (GO:0016281).
- **Verdict:** Biology consistent; one node-level contradiction (PN GO:0016281 vs review REMOVE). RQC story already captured more precisely. **Recommended edits:** [MAP] flag the EIF4E2 "eIF4F complex" type→GO:0016281 projection as inappropriate (4EHP cannot bind eIF4G / is not an eIF4F component — see review REMOVE of GO:0016281); do not propagate GO:0016281 to O60573.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/EIF4E2/EIF4E2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Translation initiation | eIF4F complex
- UniProt: O60573
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation initiation|eIF4F complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016281 eukaryotic translation initiation factor 4F complex]
        rationale: This PN type denotes eIF4F complex components. The GO eukaryotic translation initiation factor 4F complex term resolves the previous deferred state.
    - [group] Translation|Cytosolic translation|Translation initiation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006413 translational initiation]
        rationale: This PN group denotes cytosolic translation initiation factors and complexes. Translational initiation is the shared process target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: O60573
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

## Projected GO annotations (3)
- GO:0006413 translational initiation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Translation initiation
- GO:0016281 eukaryotic translation initiation factor 4F complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Translation initiation|eIF4F complex
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
