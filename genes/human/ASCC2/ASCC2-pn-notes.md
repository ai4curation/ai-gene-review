# ASCC2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H1I8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1373)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ASCC2/ASCC2-ai-review.yaml](ASCC2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ASCC2/ASCC2-ai-review.html](ASCC2-ai-review.html)
- Gene notes: present - [genes/human/ASCC2/ASCC2-notes.md](ASCC2-notes.md)
- GOA TSV: present - [genes/human/ASCC2/ASCC2-goa.tsv](ASCC2-goa.tsv)
- UniProt record: present - [genes/human/ASCC2/ASCC2-uniprot.txt](ASCC2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ASCC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ASCC2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ASCC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ASCC2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ASCC2/ASCC2-deep-research-falcon.md](ASCC2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ASCC2 is a CUE-domain ubiquitin-binding subunit of activating signal cointegrator complexes. In the nucleus, ASCC2 recognizes K63-linked polyubiquitin signals and helps recruit ASCC3 and ALKBH3 to alkylation-damage sites, supporting DNA dealkylation repair in nuclear foci associated with transcription and spliceosome components. In the cytosol, ASCC2 works with ASCC3 and TRIP4 as the human RQC-trigger complex to recognize K63-polyubiquitinated collided ribosomes and promote ribosome subunit dissociation, enabling rescue of stalled cytosolic ribosomes and downstream ribosome-associated quality control. ASCC2 was also described historically as the P100 subunit of an ASC-1 transcription coactivator complex, but its most mechanistically supported functions are K63-ubiquitin-dependent DNA repair and stalled-ribosome quality control.
- Existing/core annotation action counts: ACCEPT: 29; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 2; REMOVE: 4

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research, notes, review YAML agree ASCC2 is the CUE-domain K63-polyUb reader serving BOTH (1) nuclear ASCC-ALKBH3 alkylation repair and (2) cytosolic hRQT/RQC. Both PN rows map onto these two arms cleanly. Review holds GO:0070530 (K63-linked polyUb-dependent binding) as the MF for both core_functions, plus full RQC term set.
- **PN story / NEW pressure:** Row1 RQC role already captured by specific terms (GO:0072344, GO:0032790, GO:1990116, GO:0180022 ACCEPT; GO:0043130 ubiquitin binding MODIFY→GO:0070530). Notes correctly decline broad GO:0006515 as redundant. Row2 (UPS CUE / ubiquitin-reader) is honestly mapped no_mapping at leaf and context_only above (GO:0140036 ubiquitin-modified protein reader) — the actual reader function is captured more specifically by GO:0070530 in the review. **Conclude: already captured.** No NEW term needed.
- **Evidence alignment:** PN rows carry no reference titles. Review CUE/K63 evidence (PMID:29144457, PMID:36302773, PMID:34971705 Lombardi, PMID:33139697 Jia ASCC2-ASCC3 interface) and RQC (PMID:32099016, PMID:32579943) align with both PN arms. No citation conflicts.
- **Verdict:** Consistent and well-supported across both PN branches; specific GO:0070530 + RQC terms already capture the story. Broad projections correctly declined. No edits warranted.

## Full Consistency Review

- **UniProt:** Q9H1I8 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE (Falcon DR present)
- **PN placement:** TWO rows. Row1 `Translation|...|Ribosome-associated QC|Ribosomal rescue` (type=mapped/ok GO:0072344 already_in_goa_exact; group=mapped/ok GO:0006515 new_to_goa). Row2 `Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation|ribosome QC & DNA repair|CUE` (subtype/type=no_mapping; group/class context_only GO:0006412 / GO:0140036). Signature domain IPR003892 (CUE).
- **Consistency:** Fully consistent. Deep research, notes, review YAML agree ASCC2 is the CUE-domain K63-polyUb reader serving BOTH (1) nuclear ASCC-ALKBH3 alkylation repair and (2) cytosolic hRQT/RQC. Both PN rows map onto these two arms cleanly. Review holds GO:0070530 (K63-linked polyUb-dependent binding) as the MF for both core_functions, plus full RQC term set.
- **PN story / NEW pressure:** Row1 RQC role already captured by specific terms (GO:0072344, GO:0032790, GO:1990116, GO:0180022 ACCEPT; GO:0043130 ubiquitin binding MODIFY→GO:0070530). Notes correctly decline broad GO:0006515 as redundant. Row2 (UPS CUE / ubiquitin-reader) is honestly mapped no_mapping at leaf and context_only above (GO:0140036 ubiquitin-modified protein reader) — the actual reader function is captured more specifically by GO:0070530 in the review. **Conclude: already captured.** No NEW term needed.
- **Mapping strategy:** ASCC2 supports both nodes but drives neither toward change. Broad GO:0006515 (RQC node) and GO:0140036 (UPS class) are both broader than the review's GO:0070530 — the TOMM20/HSPA8/RAB7A "too broad" precedent applies; do not project. Row2 leaf no_mapping is the right call.
- **Evidence alignment:** PN rows carry no reference titles. Review CUE/K63 evidence (PMID:29144457, PMID:36302773, PMID:34971705 Lombardi, PMID:33139697 Jia ASCC2-ASCC3 interface) and RQC (PMID:32099016, PMID:32579943) align with both PN arms. No citation conflicts.
- **Verdict:** Consistent and well-supported across both PN branches; specific GO:0070530 + RQC terms already capture the story. Broad projections correctly declined. No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ASCC2/ASCC2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q9H1I8
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

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | translation | ribosome QC & DNA repair | CUE
- UniProt: Q9H1I8
- In branches: TR, UPS
- Signature domains: IPR003892
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation|ribosome QC & DNA repair|CUE
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation|ribosome QC & DNA repair
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: This PN group captures ubiquitin/UBL-binding factors assigned to translation-related contexts. The relationship to translation is real, but the group mixes heterogeneous subcontexts including repression, nascent-peptide binding, ribosome maturation, and ribosome-quality- control-adjacent roles.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
