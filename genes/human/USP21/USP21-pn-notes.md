# USP21 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UK80
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/USP21/USP21-ai-review.yaml](USP21-ai-review.yaml)
- AIGR review HTML: present - [genes/human/USP21/USP21-ai-review.html](USP21-ai-review.html)
- Gene notes: present - [genes/human/USP21/USP21-notes.md](USP21-notes.md)
- GOA TSV: present - [genes/human/USP21/USP21-goa.tsv](USP21-goa.tsv)
- UniProt record: present - [genes/human/USP21/USP21-uniprot.txt](USP21-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/USP21.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/USP21.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/USP21.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/USP21.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: USP21 (ubiquitin carboxyl-terminal hydrolase 21) is a cysteine-protease deubiquitinating enzyme (DUB) of the peptidase C19 / ubiquitin-specific protease (USP) family. Its catalytic USP domain (residues ~212-558) uses a Cys-221 nucleophile and a His-518 proton acceptor and contains a structural zinc site; mutation of Cys-221 abolishes activity. USP21 hydrolyzes isopeptide and peptide bonds at the C-terminal Gly of ubiquitin to remove ubiquitin from conjugated substrates, and it has dual specificity, also removing the ubiquitin-like modifier NEDD8 (but not SUMO/Sentrin-1). It localizes to both the cytoplasm and the nucleus and carries a CRM1-dependent nuclear export signal. Through its DUB activity USP21 antagonizes ubiquitin-dependent signaling and degradation of diverse substrates. It deubiquitinates 40S ribosomal proteins RPS10/eS10 and RPS20/uS10 to counteract ZNF598-mediated ribosomal ubiquitylation and limit ribosome-associated quality control (RQC); it deubiquitinates and stabilizes the NoRC component BAZ2A/TIP5 to promote rDNA silencing together with BEND3; and (by similarity to the mouse ortholog) it deubiquitinates histone H2A to relieve transcriptional repression and act as a transcriptional coactivator. Additional reported substrates include RIPK1, RIG-I, GATA3, MARK3 and ACLY, consistent with broad roles in innate immune signaling, transcription and metabolism.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 11

## PN Consistency Summary

- **Consistency:** Consistent. Notes, review, and PN agree USP21 is a dual ubiquitin/NEDD8 cysteine-type DUB (GO:0004843, GO:0019784) that, per PMID:32011234, deubiquitinates 40S eS10/RPS10 and uS10/RPS20 to antagonize ZNF598 and limit RQC. The RQC role is captured in the review as GO:0016579 protein deubiquitination (IDA). MF-granularity note: PN projects GO:0101005 (parent) while GOA/review use child GO:0004843; "entailed_by_goa_closure" is the correct status, no conflict.
- **PN story / NEW pressure:** PN asserts an RQC process role. GOA/review for USP21 contain GO:0016579 but NOT the projected GO:0006515 (verified real, non-obsolete) nor any rescue/RQC-specific process term. Unlike ZNF598/USP10, USP21 has no GO:0072344 or GO:1990116. GO:0006515 (or the more specific GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process, verified real) is a defensible ADD: USP21's RQC role is a *negative* regulator (it reverses the mark), so a generic "involved_in protein QC" term is biologically defensible. Conclude: defensible ADD (broad), but the negative-regulator nuance means the bare process term slightly over-states; GO:0016579 already partly captures it.
- **Evidence alignment:** PN UPS row cites "19734957/rev" (Komander/Clague DUB review) — not in review references; the RQC TR row has no titled reference. Review's RQC evidence (PMID:32011234) is more specific and absent from the PN rows. Strong divergence: the key RQC paper is in the review but not cited by PN.
- **Verdict:** Consistent; RQC role captured via GO:0016579 (IDA). PN's GO:0006515 is a defensible-but-broader ADD; no NEW term required.

## Full Consistency Review

- **UniProt:** Q9UK80 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** TR `Cytosolic translation|Ribosome-associated QC|Deubiquitination`; UPS `DUBs and UBL demodifiers|USP|other|other` ; **PN-node mapping:** RQC type→GO:0101005 deubiquitinase activity (mapped, ok_for_propagation); RQC group→GO:0006515 protein QC for misfolded/incompletely synthesized proteins (new_to_goa); UPS group→GO:0101005 (entailed_by_goa_closure); type/subtype/class/branch = no_mapping.
- **Consistency:** Consistent. Notes, review, and PN agree USP21 is a dual ubiquitin/NEDD8 cysteine-type DUB (GO:0004843, GO:0019784) that, per PMID:32011234, deubiquitinates 40S eS10/RPS10 and uS10/RPS20 to antagonize ZNF598 and limit RQC. The RQC role is captured in the review as GO:0016579 protein deubiquitination (IDA). MF-granularity note: PN projects GO:0101005 (parent) while GOA/review use child GO:0004843; "entailed_by_goa_closure" is the correct status, no conflict.
- **PN story / NEW pressure:** PN asserts an RQC process role. GOA/review for USP21 contain GO:0016579 but NOT the projected GO:0006515 (verified real, non-obsolete) nor any rescue/RQC-specific process term. Unlike ZNF598/USP10, USP21 has no GO:0072344 or GO:1990116. GO:0006515 (or the more specific GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process, verified real) is a defensible ADD: USP21's RQC role is a *negative* regulator (it reverses the mark), so a generic "involved_in protein QC" term is biologically defensible. Conclude: defensible ADD (broad), but the negative-regulator nuance means the bare process term slightly over-states; GO:0016579 already partly captures it.
- **Mapping strategy:** USP21 does not change the node. PN-projected GO:0006515 is broader than the review's GO:0016579/GO:0004843 — a "broader than review" case (cf. TOMM20/HSPA8 precedent). UPS group→GO:0101005 entailed by GOA closure (GO:0004843 child present). Status/scope correct.
- **Evidence alignment:** PN UPS row cites "19734957/rev" (Komander/Clague DUB review) — not in review references; the RQC TR row has no titled reference. Review's RQC evidence (PMID:32011234) is more specific and absent from the PN rows. Strong divergence: the key RQC paper is in the review but not cited by PN.
- **Verdict:** Consistent; RQC role captured via GO:0016579 (IDA). PN's GO:0006515 is a defensible-but-broader ADD; no NEW term required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/USP21/USP21-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Deubiquitination
- UniProt: Q9UK80
- In branches: TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN RQC type denotes deubiquitinases acting in ribosome-associated quality control. Deubiquitinase activity is the shared molecular-function target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Ubiquitin Proteasome System | DUBs and UBL demodifiers | USP | other | other
- UniProt: Q9UK80
- In branches: TR, UPS
- Signature domains: IPR028889
- Auxiliary domains: (none)
- PN references (titles):
    - 19734957 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|other|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN group is an active deubiquitinase family bucket. The shared molecular-function assertion is deubiquitinase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
