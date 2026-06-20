# ASCC3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N3C0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1371)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ASCC3/ASCC3-ai-review.yaml](ASCC3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ASCC3/ASCC3-ai-review.html](ASCC3-ai-review.html)
- Gene notes: present - [genes/human/ASCC3/ASCC3-notes.md](ASCC3-notes.md)
- GOA TSV: present - [genes/human/ASCC3/ASCC3-goa.tsv](ASCC3-goa.tsv)
- UniProt record: present - [genes/human/ASCC3/ASCC3-uniprot.txt](ASCC3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ASCC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ASCC3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ASCC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ASCC3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ASCC3/ASCC3-deep-research-falcon.md](ASCC3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ASCC3 encodes a large ATP-dependent superfamily II helicase that functions in distinct ASCC-containing complexes. In the nucleus, ASCC3 is the catalytic helicase subunit of the ALKBH3-associated ASCC DNA dealkylation repair complex, where it helps unwind alkylated duplex DNA and is recruited to alkylation-induced nuclear foci. In the cytosol, ASCC3/RQT2 is the ATPase subunit of the human ribosome quality control trigger complex with ASCC2 and TRIP4, where it promotes splitting of K63-ubiquitinated collided ribosomes to initiate ribosome-associated quality control. ASCC3 was also originally identified as a component of the ASC-1 transcription coactivator complex, but its best-supported mechanistic roles are DNA alkylation repair and stalled ribosome rescue.
- Existing/core annotation action counts: ACCEPT: 42; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 5; MODIFY: 2; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research, notes, and review YAML agree ASCC3 has two cores: (1) nuclear ATP-dependent 3'-5' DNA helicase of the ASCC-ALKBH3 dealkylation-repair complex; (2) cytosolic hRQT/RQT2 ATPase that splits K63-ubiquitinated collided ribosomes. The PN RQC placement matches the cytosolic role exactly. GO:0072344 is present in GOA and ACCEPTed in-review.
- **PN story / NEW pressure:** PN's ribosomal-rescue assertion is genuinely captured: review already holds GO:0072344, GO:0032790 (ribosome disassembly), GO:1990116, GO:0180022 (RQC-trigger complex), all ACCEPT. The group-level projection GO:0006515 (broad protein QC) is new_to_goa but the notes correctly decline it as **redundant/less informative** than the existing specific RQC terms. **Conclude: already captured** (specific terms preferred over the broad PN ancestor). No NEW term needed.
- **Evidence alignment:** PN row has no reference titles. Review RQC evidence (PMID:32099016 hRQT; PMID:32579943 disassembly; PMID:36302773 K63-uS10) is exactly on-point; DNA-repair arm (PMID:22055184, PMID:29144457) aligns with the nuclear role. No citation conflicts.
- **Verdict:** Consistent and well-supported; PN story already captured by specific GO terms. Broad GO:0006515 projection correctly declined. No edits warranted.

## Full Consistency Review

- **UniProt:** Q8N3C0 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE (Falcon DR present)
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue` ; **PN-node mapping:** type=mapped/ok GO:0072344 (already_in_goa_exact); group=mapped/ok GO:0006515 (new_to_goa); class/branch context_only.
- **Consistency:** Fully consistent. Deep research, notes, and review YAML agree ASCC3 has two cores: (1) nuclear ATP-dependent 3'-5' DNA helicase of the ASCC-ALKBH3 dealkylation-repair complex; (2) cytosolic hRQT/RQT2 ATPase that splits K63-ubiquitinated collided ribosomes. The PN RQC placement matches the cytosolic role exactly. GO:0072344 is present in GOA and ACCEPTed in-review.
- **PN story / NEW pressure:** PN's ribosomal-rescue assertion is genuinely captured: review already holds GO:0072344, GO:0032790 (ribosome disassembly), GO:1990116, GO:0180022 (RQC-trigger complex), all ACCEPT. The group-level projection GO:0006515 (broad protein QC) is new_to_goa but the notes correctly decline it as **redundant/less informative** than the existing specific RQC terms. **Conclude: already captured** (specific terms preferred over the broad PN ancestor). No NEW term needed.
- **Mapping strategy:** ASCC3 is the strongest driver/anchor for this RQC node — direct experimental evidence for splitting collided ribosomes. The exact-match GO:0072344 is well-justified. The broader GO:0006515 group mapping is the TOMM20/HSPA8/RAB7A-style "broader than review" case and should NOT be projected to ASCC3 (specific terms already exist). Node status/scope fine; ASCC3 needs no change.
- **Evidence alignment:** PN row has no reference titles. Review RQC evidence (PMID:32099016 hRQT; PMID:32579943 disassembly; PMID:36302773 K63-uS10) is exactly on-point; DNA-repair arm (PMID:22055184, PMID:29144457) aligns with the nuclear role. No citation conflicts.
- **Verdict:** Consistent and well-supported; PN story already captured by specific GO terms. Broad GO:0006515 projection correctly declined. No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ASCC3/ASCC3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q8N3C0
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
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
