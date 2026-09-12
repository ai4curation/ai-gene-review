# EIF3J PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75822
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EIF3J/EIF3J-ai-review.yaml](EIF3J-ai-review.yaml)
- AIGR review HTML: present - [genes/human/EIF3J/EIF3J-ai-review.html](EIF3J-ai-review.html)
- Gene notes: present - [genes/human/EIF3J/EIF3J-notes.md](EIF3J-notes.md)
- GOA TSV: present - [genes/human/EIF3J/EIF3J-goa.tsv](EIF3J-goa.tsv)
- UniProt record: present - [genes/human/EIF3J/EIF3J-uniprot.txt](EIF3J-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EIF3J.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EIF3J.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF3J.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EIF3J.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: EIF3J (eukaryotic translation initiation factor 3 subunit J) is a cytoplasmic accessory subunit of the 13-subunit eIF-3 complex, the largest eukaryotic translation initiation factor. eIF-3 associates with the 40S ribosomal subunit and orchestrates several steps of cap-dependent translation initiation, promoting recruitment of eIF-1, eIF-1A, the eIF-2-GTP-Met-tRNAi ternary complex and eIF-5 to form the 43S pre-initiation complex, stimulating mRNA recruitment and scanning to the AUG start codon, and contributing to disassembly/recycling of post-termination ribosomal complexes while preventing premature 40S-60S subunit joining. EIF3J is a loosely associated, sub-stoichiometric ("labile") subunit that docks onto the complex through EIF3B; it positions near the 40S mRNA entry channel/decoding region and is required for stable binding of eIF-3 (and its subcomplexes) to the 40S subunit, thereby modulating mRNA loading and 40S availability. It is a non-catalytic accessory factor (its initiation-factor activity is contributed in the context of the assembled complex) and is phosphorylated in a serum-stimulation-dependent manner.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 13

## PN Consistency Summary

- **Consistency:** Initiation row is fully consistent — review accepts GO:0005852 (core CC) and GO:0006413 (core BP), both in GOA. The RQC row is weakly supported: EIF3J/eIF-3 contributes to post-termination ribosome disassembly/40S recycling and prevents premature 40S-60S joining (noted via the ABCE1 interaction PMID:32296183/35271311), but the review captures this only obliquely (ABCE1 protein-binding KEEP_AS_NON_CORE) and assigns NO QC/recycling process term. So GO:0006515 is not reflected in the review.
- **PN story / NEW pressure:** RQC group projects GO:0006515 protein QC as `new_to_goa`. EIF3J's recycling role is real but is a *recycling/40S-availability* function, not protein quality control / misfolded-chain surveillance; GO:0006515 (protein QC for misfolded/incompletely synthesized proteins) mischaracterizes it and **over-reaches**. A ribosome-recycling/disassembly process term (e.g. GO:0032790 ribosome disassembly) would be more defensible than GO:0006515 if any RQC-row term is projected.
- **Evidence alignment:** Dossier gives no reference titles. Review anchors PMID:14688252 (j-subunit/40S stable binding, VERIFIED), PMID:17322308/18599441 (eIF-3 MS). Initiation evidence overlaps cleanly; the RQC claim has no dedicated citation in either source.
- **Verdict:** Initiation placement consistent and correct; RQC-group GO:0006515 projection over-reaches (EIF3J is a recycling accessory, not a protein-QC factor). **Recommended edits:** [MAP] drop GO:0006515 projection for EIF3J (or substitute GO:0032790 ribosome disassembly if a recycling term is wanted).

## Full Consistency Review

- **UniProt:** O75822 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** 2 rows — `Translation|Cytosolic translation|Translation initiation|eIF3 complex` and `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** initiation type → GO:0005852 eIF3 complex (mapped); initiation group → GO:0006413 translational initiation (mapped); RQC group → GO:0006515 protein QC (mapped, new_to_goa); RQC type no_mapping.
- **Consistency:** Initiation row is fully consistent — review accepts GO:0005852 (core CC) and GO:0006413 (core BP), both in GOA. The RQC row is weakly supported: EIF3J/eIF-3 contributes to post-termination ribosome disassembly/40S recycling and prevents premature 40S-60S joining (noted via the ABCE1 interaction PMID:32296183/35271311), but the review captures this only obliquely (ABCE1 protein-binding KEEP_AS_NON_CORE) and assigns NO QC/recycling process term. So GO:0006515 is not reflected in the review.
- **PN story / NEW pressure:** RQC group projects GO:0006515 protein QC as `new_to_goa`. EIF3J's recycling role is real but is a *recycling/40S-availability* function, not protein quality control / misfolded-chain surveillance; GO:0006515 (protein QC for misfolded/incompletely synthesized proteins) mischaracterizes it and **over-reaches**. A ribosome-recycling/disassembly process term (e.g. GO:0032790 ribosome disassembly) would be more defensible than GO:0006515 if any RQC-row term is projected.
- **Mapping strategy:** Initiation mapping is correct and well-supported. The `Ribosome-associated QC` group → GO:0006515 is too broad/mischaracterizing for EIF3J (a recycling accessory, not a QC factor); recommend not projecting GO:0006515 here.
- **Evidence alignment:** Dossier gives no reference titles. Review anchors PMID:14688252 (j-subunit/40S stable binding, VERIFIED), PMID:17322308/18599441 (eIF-3 MS). Initiation evidence overlaps cleanly; the RQC claim has no dedicated citation in either source.
- **Verdict:** Initiation placement consistent and correct; RQC-group GO:0006515 projection over-reaches (EIF3J is a recycling accessory, not a protein-QC factor). **Recommended edits:** [MAP] drop GO:0006515 projection for EIF3J (or substitute GO:0032790 ribosome disassembly if a recycling term is wanted).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/EIF3J/EIF3J-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Translation initiation | eIF3 complex
- UniProt: O75822
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation initiation|eIF3 complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005852 eukaryotic translation initiation factor 3 complex]
        rationale: This PN type denotes component membership in the eIF3 complex. Propagation to the matching GO cellular-component term is appropriate.
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
- UniProt: O75822
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
- GO:0005852 eukaryotic translation initiation factor 3 complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Translation initiation|eIF3 complex
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
