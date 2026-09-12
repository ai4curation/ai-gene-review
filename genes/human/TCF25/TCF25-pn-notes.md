# TCF25 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BQ70
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TCF25/TCF25-ai-review.yaml](TCF25-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TCF25/TCF25-ai-review.html](TCF25-ai-review.html)
- Gene notes: present - [genes/human/TCF25/TCF25-notes.md](TCF25-notes.md)
- GOA TSV: present - [genes/human/TCF25/TCF25-goa.tsv](TCF25-goa.tsv)
- UniProt record: present - [genes/human/TCF25/TCF25-uniprot.txt](TCF25-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TCF25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TCF25.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TCF25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TCF25.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TCF25 (Ribosome quality control complex subunit TCF25; also known as Nulp1/hnulp1, "nuclear localized protein 1") is the human ortholog of the yeast RQC factor Rqc1 and a component of the ribosome-associated quality control (RQC) complex together with the E3 ubiquitin ligase LTN1/Listerin and NEMF on the stalled 60S ribosomal subunit. Within this complex TCF25 acts as an accessory factor required to promote formation of Lys48-linked polyubiquitin chains during LTN1-mediated ubiquitination of incompletely synthesized nascent chains, thereby ensuring efficient targeting of stalled translation products for proteasomal degradation. Despite the legacy "Transcription Factor 25" name, TCF25 has no demonstrated sequence-specific transcription-factor activity in this role; earlier work described it as a mainly nuclear basic-helix-loop-helix protein (Nulp1/hnulp1) with a transcriptional repressive domain and a role in cell-death control and XIAP binding. It is widely expressed with high levels in heart and, in the embryo, brain, and is found in both the nucleus and the cytosol.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 15

## PN Consistency Summary

- **Consistency:** Excellent. Deep research/notes, review and PN concur: TCF25 (= yeast Rqc1 ortholog; legacy Nulp1/hnulp1) is an accessory subunit of the 60S RQC complex (LTN1 + NEMF + TCF25), required to promote K48-linked polyubiquitin chains during LTN1-mediated nascent-chain ubiquitination (PMID:30244831). The legacy bHLH "transcription factor"/XIAP/cell-death role is correctly demoted to non-core. PN's "other RQC processes" no_mapping is consistent with the review treating TCF25 as a cofactor/scaffold without a clean own-MF. No contradictions.
- **PN story / NEW pressure:** GO:0006515 (verified real) is new_to_goa and absent from the review. The review instead uses GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process (NAS), GO:0061945 regulation of protein K48-linked ubiquitination (IDA), GO:0072344 (NAS/IDA) and GO:1990112 RQC complex (IDA/IBA/NAS). Verified via OLS: GO:1990116 sits in the **catabolic-process** branch (under GO:0006511), NOT under GO:0006515 — so GO:0006515 is a related but distinct higher-level QC-process term, a defensible ADD that better matches the canonical RQC framing. Conclude: function captured (via GO:0061945/GO:1990116/GO:1990112); GO:0006515 a reasonable additional/parent QC-process ADD.
- **Evidence alignment:** PN row cites no PMIDs. Review's key evidence PMID:30244831 (K48 linkage role) + PMID:35452614 (RQC review, ComplexPortal NAS) is HIGH/VERIFIED. The 14 IPI protein-binding partners are all high-throughput, correctly non-core. No divergence.
- **Verdict:** Fully consistent; function captured via GO:1990112/GO:0061945/GO:1990116; PN's GO:0006515 is a defensible additional QC-process ADD (distinct from the catabolic-branch GO:1990116). No YAML change needed.

## Full Consistency Review

- **UniProt:** Q9BQ70 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE (clean; core = RQC complex K48-chain cofactor, Nulp1 legacy non-core)
- **PN placement:** 1 row — `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes`. **PN-node mapping:** RQC-type ("other RQC processes")→no_mapping (heterogeneous bucket); RQC-group→mapped GO:0006515 protein QC (new_to_goa); class/branch context_only. Projected: GO:0006515 (new) only.
- **Consistency:** Excellent. Deep research/notes, review and PN concur: TCF25 (= yeast Rqc1 ortholog; legacy Nulp1/hnulp1) is an accessory subunit of the 60S RQC complex (LTN1 + NEMF + TCF25), required to promote K48-linked polyubiquitin chains during LTN1-mediated nascent-chain ubiquitination (PMID:30244831). The legacy bHLH "transcription factor"/XIAP/cell-death role is correctly demoted to non-core. PN's "other RQC processes" no_mapping is consistent with the review treating TCF25 as a cofactor/scaffold without a clean own-MF. No contradictions.
- **PN story / NEW pressure:** GO:0006515 (verified real) is new_to_goa and absent from the review. The review instead uses GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process (NAS), GO:0061945 regulation of protein K48-linked ubiquitination (IDA), GO:0072344 (NAS/IDA) and GO:1990112 RQC complex (IDA/IBA/NAS). Verified via OLS: GO:1990116 sits in the **catabolic-process** branch (under GO:0006511), NOT under GO:0006515 — so GO:0006515 is a related but distinct higher-level QC-process term, a defensible ADD that better matches the canonical RQC framing. Conclude: function captured (via GO:0061945/GO:1990116/GO:1990112); GO:0006515 a reasonable additional/parent QC-process ADD.
- **Mapping strategy:** Sound. The leaf "other RQC processes"→no_mapping (heterogeneous) is the right call; the only projection comes from the RQC-group→GO:0006515. TCF25 genuinely participates in protein QC of incompletely synthesized proteins, so GO:0006515 is appropriately scoped (not over-broad here, since TCF25 has no competing finer own-process term beyond the complex/regulation annotations). No node change.
- **Evidence alignment:** PN row cites no PMIDs. Review's key evidence PMID:30244831 (K48 linkage role) + PMID:35452614 (RQC review, ComplexPortal NAS) is HIGH/VERIFIED. The 14 IPI protein-binding partners are all high-throughput, correctly non-core. No divergence.
- **Verdict:** Fully consistent; function captured via GO:1990112/GO:0061945/GO:1990116; PN's GO:0006515 is a defensible additional QC-process ADD (distinct from the catabolic-branch GO:1990116). No YAML change needed.
- **Recommended edits:** none required. [YAML] (optional) GO:0006515 protein quality control for misfolded or incompletely synthesized proteins could be added as an `involved_in` process term to better surface TCF25's RQC role (currently only catabolic/regulation/complex terms present); supported by PMID:30244831.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/TCF25/TCF25-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: Q9BQ70
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
