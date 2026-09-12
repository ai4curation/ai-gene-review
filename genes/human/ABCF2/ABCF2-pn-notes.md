# ABCF2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UG63
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1326)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ABCF2/ABCF2-ai-review.yaml](ABCF2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ABCF2/ABCF2-ai-review.html](ABCF2-ai-review.html)
- Gene notes: present - [genes/human/ABCF2/ABCF2-notes.md](ABCF2-notes.md)
- GOA TSV: present - [genes/human/ABCF2/ABCF2-goa.tsv](ABCF2-goa.tsv)
- UniProt record: present - [genes/human/ABCF2/ABCF2-uniprot.txt](ABCF2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ABCF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ABCF2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABCF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABCF2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ABCF2/ABCF2-deep-research-falcon.md](ABCF2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ABCF2 encodes ATP-binding cassette sub-family F member 2, a soluble member of the ABCF family with two ABC nucleotide-binding domains and no transmembrane domains. It is best described as a cytosolic ABC-family ATPase rather than a membrane transporter. ABCF2 expression is regulated by NFE2L2/NRF2 through a promoter antioxidant-response element in ovarian cancer cells, where altered ABCF2 abundance affects cisplatin sensitivity, but the direct molecular mechanism linking ABCF2 to drug resistance remains unresolved. ABCF2 has also been reported as a putative anti-apoptotic host factor that is bound and destabilized by the enteropathogenic Escherichia coli type III effector EspF, with cytoplasmic and partial mitochondrial localization, consistent with a role in restraining the intrinsic (mitochondrial) apoptotic pathway.
- Existing/core annotation action counts: ACCEPT: 4; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Consistent in conclusions, with a deliberate divergence. Deep research and notes frame ABCF2 as a soluble two-NBD ABCF ATPase (no TMDs, not a transporter; ABC-F family = ribosome-E-site translation factors), with an NFE2L2/cisplatin angle and a putative anti-apoptotic EspF-interaction role. The review accepts ATP binding / ATP hydrolysis / cytosol and removes the membrane/plasma-membrane rows. The review **explicitly declines** the PN-projected GO:0006515 because no ABCF2-specific stalled-ribosome/RQC evidence exists — recording it as an open question instead. PN (RQC bucket) vs review (no RQC process) is a documented, evidence-based divergence, not an error.
- **PN story / NEW pressure:** PN asserts a ribosome-associated QC role not in GOA. The projected GO:0006515 is verified real, but ABCF2-specific RQC evidence is absent; family/context inference alone is insufficient. Conclusion: **PN over-reaches** for ABCF2; correctly held as a suggested question rather than a NEW term. No defensible NEW GO term to add now.
- **Evidence alignment:** PN dossier lists no reference titles. Review/notes cite PMID:28112439 (NRF2/cisplatin, cytosolic non-transporter), PMID:17064289 (EspF), PMID:19946888, Reactome R-HSA-9796042 — none establish RQC, so they neither support nor are cited by the PN RQC node. No citation conflict.
- **Verdict:** Consistent (review conservatively rejects the PN RQC projection). **Recommended edits:** [REF] Reconcile UniProt accession — PN dossier/workbook uses A0A090N7X1 but the canonical reviewed entry and review YAML use Q9UG63; update the PN workbook to Q9UG63. [MAP] Keep GO:0006515 non-propagating for ABCF2.

## Full Consistency Review

- **UniProt:** Q9UG63 (review YAML) — dossier lists **A0A090N7X1** (TrEMBL/secondary accession mismatch) · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** type `other RQC processes`=no_mapping; group `Ribosome-associated QC`=mapped→**GO:0006515 protein quality control for misfolded/incompletely synthesized proteins** (new_to_goa); class/branch context_only.
- **Consistency:** Consistent in conclusions, with a deliberate divergence. Deep research and notes frame ABCF2 as a soluble two-NBD ABCF ATPase (no TMDs, not a transporter; ABC-F family = ribosome-E-site translation factors), with an NFE2L2/cisplatin angle and a putative anti-apoptotic EspF-interaction role. The review accepts ATP binding / ATP hydrolysis / cytosol and removes the membrane/plasma-membrane rows. The review **explicitly declines** the PN-projected GO:0006515 because no ABCF2-specific stalled-ribosome/RQC evidence exists — recording it as an open question instead. PN (RQC bucket) vs review (no RQC process) is a documented, evidence-based divergence, not an error.
- **PN story / NEW pressure:** PN asserts a ribosome-associated QC role not in GOA. The projected GO:0006515 is verified real, but ABCF2-specific RQC evidence is absent; family/context inference alone is insufficient. Conclusion: **PN over-reaches** for ABCF2; correctly held as a suggested question rather than a NEW term. No defensible NEW GO term to add now.
- **Mapping strategy:** The group node `Ribosome-associated QC`→GO:0006515 is sound for bona fide RQC members but should NOT propagate to ABCF2, which sits under the `other RQC processes` (no_mapping) catch-all on family/context grounds only. Treat the GO:0006515 projection as non-propagating for this gene pending direct ribosome-binding/RQC evidence.
- **Evidence alignment:** PN dossier lists no reference titles. Review/notes cite PMID:28112439 (NRF2/cisplatin, cytosolic non-transporter), PMID:17064289 (EspF), PMID:19946888, Reactome R-HSA-9796042 — none establish RQC, so they neither support nor are cited by the PN RQC node. No citation conflict.
- **Verdict:** Consistent (review conservatively rejects the PN RQC projection). **Recommended edits:** [REF] Reconcile UniProt accession — PN dossier/workbook uses A0A090N7X1 but the canonical reviewed entry and review YAML use Q9UG63; update the PN workbook to Q9UG63. [MAP] Keep GO:0006515 non-propagating for ABCF2.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABCF2/ABCF2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: A0A090N7X1
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
