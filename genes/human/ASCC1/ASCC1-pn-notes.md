# ASCC1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N9N2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1370)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ASCC1/ASCC1-ai-review.yaml](ASCC1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ASCC1/ASCC1-ai-review.html](ASCC1-ai-review.html)
- Gene notes: present - [genes/human/ASCC1/ASCC1-notes.md](ASCC1-notes.md)
- GOA TSV: present - [genes/human/ASCC1/ASCC1-goa.tsv](ASCC1-goa.tsv)
- UniProt record: present - [genes/human/ASCC1/ASCC1-uniprot.txt](ASCC1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ASCC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ASCC1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ASCC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ASCC1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ASCC1/ASCC1-deep-research-falcon.md](ASCC1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ASCC1 encodes the p50 subunit of the nuclear activating signal cointegrator 1 complex. The protein acts with TRIP4/ASC-1, ASCC2, and ASCC3 in a transcription coactivator complex that supports AP-1, SRF, NF-kappaB, and context-specific gene-expression responses. ASCC1 also functions as an accessory/regulatory subunit of the ASCC alkylation-damage response, where it interacts with ASCC3 and helps coordinate recruitment and assembly of the ALKBH3-ASCC repair complex at nuclear alkylation-damage foci. ASCC1 localizes mainly to the nucleus and nuclear speckles; loss-of-function variants disrupt neuromuscular development and cause spinal muscular atrophy with congenital bone fractures.
- Existing/core annotation action counts: ACCEPT: 18; MARK_AS_OVER_ANNOTATED: 5; NEW: 2; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Internally consistent but PN placement is contradicted by the gene's own evidence. Deep research, notes, and review YAML all frame ASCC1 as a **nuclear** ASC-1/ASCC subunit (transcription coactivation + ALKBH3-linked alkylation-damage repair); none place ASCC1 in cytosolic ribosome rescue. The notes explicitly flag the RQC projection as a workbook propagation artifact and cite PMID:38366554 that ASCC1 is **dispensable** for the cytoplasmic ribosome-splitting step. GOA confirms no RQC term on ASCC1.
- **PN story / NEW pressure:** The PN asserts a ribosomal-rescue/RQC role not in GO and not supported by ASCC1-specific data. GO:0072344 and GO:0006515 are real terms, but projecting them to ASCC1 over-reaches: the RQC role belongs to the ASCC complex via ASCC3/ASCC2/TRIP4, with ASCC1 dispensable. **Conclude: over-reaches** (do not project to ASCC1). No defensible NEW GO term for ASCC1 from the PN node; the review already proposes the correct NEWs (GO:0060090 molecular adaptor; GO:0003713 transcription coactivator, contributes_to).
- **Evidence alignment:** PN row carries no reference titles; the review's RQC-adjacent papers (PMID:37092320 translation initiation; PMID:38366554 disassembly) are complex/ASCC3-centric and were deliberately not used to add RQC terms to ASCC1. No PMID conflict — divergence is conceptual (node-level vs gene-level).
- **Verdict:** Consistent review; PN RQC projection over-reaches for ASCC1 and is correctly rejected in-review. No edits needed beyond exempting ASCC1 from RQC propagation at the mapping layer.

## Full Consistency Review

- **UniProt:** Q8N9N2 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE (rich; Falcon DR present)
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue` ; **PN-node mapping:** type=mapped/ok GO:0072344 (rescue of stalled cytosolic ribosome); group=mapped/ok GO:0006515; class/branch context_only. Both projected terms new_to_goa.
- **Consistency:** Internally consistent but PN placement is contradicted by the gene's own evidence. Deep research, notes, and review YAML all frame ASCC1 as a **nuclear** ASC-1/ASCC subunit (transcription coactivation + ALKBH3-linked alkylation-damage repair); none place ASCC1 in cytosolic ribosome rescue. The notes explicitly flag the RQC projection as a workbook propagation artifact and cite PMID:38366554 that ASCC1 is **dispensable** for the cytoplasmic ribosome-splitting step. GOA confirms no RQC term on ASCC1.
- **PN story / NEW pressure:** The PN asserts a ribosomal-rescue/RQC role not in GO and not supported by ASCC1-specific data. GO:0072344 and GO:0006515 are real terms, but projecting them to ASCC1 over-reaches: the RQC role belongs to the ASCC complex via ASCC3/ASCC2/TRIP4, with ASCC1 dispensable. **Conclude: over-reaches** (do not project to ASCC1). No defensible NEW GO term for ASCC1 from the PN node; the review already proposes the correct NEWs (GO:0060090 molecular adaptor; GO:0003713 transcription coactivator, contributes_to).
- **Mapping strategy:** This gene is a counter-example for the RQC node, not a driver. The type/group mappings (GO:0072344/GO:0006515) are biologically sound for the node but must not be auto-projected to ASCC1. Status/scope of the node need not change for other members; ASCC1 should be exempted from propagation.
- **Evidence alignment:** PN row carries no reference titles; the review's RQC-adjacent papers (PMID:37092320 translation initiation; PMID:38366554 disassembly) are complex/ASCC3-centric and were deliberately not used to add RQC terms to ASCC1. No PMID conflict — divergence is conceptual (node-level vs gene-level).
- **Verdict:** Consistent review; PN RQC projection over-reaches for ASCC1 and is correctly rejected in-review. No edits needed beyond exempting ASCC1 from RQC propagation at the mapping layer.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ASCC1/ASCC1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q8N9N2
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
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
