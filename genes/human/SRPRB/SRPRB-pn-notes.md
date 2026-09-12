# SRPRB PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y5M8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SRPRB/SRPRB-ai-review.yaml](SRPRB-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SRPRB/SRPRB-ai-review.html
- Gene notes: present - [genes/human/SRPRB/SRPRB-notes.md](SRPRB-notes.md)
- GOA TSV: present - [genes/human/SRPRB/SRPRB-goa.tsv](SRPRB-goa.tsv)
- UniProt record: present - [genes/human/SRPRB/SRPRB-uniprot.txt](SRPRB-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SRPRB.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SRPRB.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRPRB.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRPRB.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SRPRB/SRPRB-deep-research-falcon.md](SRPRB-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SRPRB (signal recognition particle receptor subunit beta, SR-beta; also APMCF1) is a 271 aa single-pass ER membrane protein and a small Ras-superfamily GTPase closely related to Arf and Sar1. It is the membrane-anchored beta subunit of the heterodimeric signal recognition particle (SRP) receptor (SR), assembling with the soluble alpha subunit SRPRA via a Longin-domain interface and tethering SRPRA to the ER membrane. The SRP receptor docks the SRP-ribosome-nascent chain complex at the ER so that signal-sequence-bearing nascent secretory and membrane proteins are delivered to the Sec61 translocon for cotranslational translocation and insertion. SRP-dependent targeting is driven by a GTPase cycle in which the SR (SRPRA and SRPRB) and the SRP54 GTPase reciprocally activate one another; GTP binding and hydrolysis by SRPRB regulate ribosome-nascent chain handover and receptor recycling. SRPRB is broadly expressed and localizes to the ER membrane.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 6; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Largely consistent. Deep research, review YAML, and PN annotation agree SRPRB is the membrane-anchored beta subunit of the SRP receptor (a Ras/Arf/Sar1-family GTPase) that docks the SRP-RNC complex at the ER. PN "SRP receptor subunit"→GO:0006614 matches the review's core BP (GO:0045047 protein targeting to ER + GO:0006617 signal-sequence-recognition child, ACCEPT; goa_status here is entailed_by_goa_closure, correctly reflecting that SRPRB's GOA carries GO:0045047/0006617 rather than GO:0006614 directly). One internal review flag: GO:0005881 cytoplasmic microtubule (IDA, PMID:23264731) — re-examined below.
- **PN story / NEW pressure:** PN asserts only the canonical SR docking role in cotranslational targeting, already captured (GO:0045047, GO:0006617, GO:0005785 SR complex, GO:0005525 GTP binding, GO:0005789 ER membrane). A genuinely novel SRbeta function — coordinating cotranslational N-glycosylation via OST engagement (PMID:36921042) — is in the review references but is not the PN story; nearest GO term GO:0180058 (verified real, OST-centric) is not a clean fit. Conclusion: **already captured** for the PN node (no NEW pressure on the mapping).
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:16439358 SR-beta/SRalpha Longin structure; PMID:29567807 prehandover cryo-EM; PMID:34020957 SR compaction/GTPase; PMID:37643813 SRPRB KO stabilizes SRalpha) all encode SR docking biology. **MTR120 re-examination:** the cached full text of PMID:23264731 (now available) is entirely about MTR120/KIAA1383, a 120 kDa MT-associated protein found in an ORFeome localization screen; SRPRB (Q9Y5M8, 271 aa ER GTPase) is never mentioned or assayed. The GO:0005881 cytoplasmic-microtubule IDA on SRPRB is a definitive mis-attribution (wrong protein), not merely unverifiable — the review's UNDECIDED was conservative only because full text was unavailable; it now is.
- **Verdict:** Consistent for the PN node; PN already captured. One warranted edit: with full text confirming PMID:23264731 does not assay SRPRB, the cytoplasmic-microtubule annotation should move from UNDECIDED to MARK_AS_OVER_ANNOTATED (wrong-gene citation; correctness → WRONG_IDENTIFIER).

## Full Consistency Review

- **UniProt:** Q9Y5M8 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|SRP receptor subunit` ; **PN-node mapping:** group=mapped scope=ok_for_propagation_to_go→GO:0006614 (SRP-dependent cotranslational protein targeting to membrane); class `Protein transport`=mapped→GO:0015031; branch=no_mapping.
- **Consistency:** Largely consistent. Deep research, review YAML, and PN annotation agree SRPRB is the membrane-anchored beta subunit of the SRP receptor (a Ras/Arf/Sar1-family GTPase) that docks the SRP-RNC complex at the ER. PN "SRP receptor subunit"→GO:0006614 matches the review's core BP (GO:0045047 protein targeting to ER + GO:0006617 signal-sequence-recognition child, ACCEPT; goa_status here is entailed_by_goa_closure, correctly reflecting that SRPRB's GOA carries GO:0045047/0006617 rather than GO:0006614 directly). One internal review flag: GO:0005881 cytoplasmic microtubule (IDA, PMID:23264731) — re-examined below.
- **PN story / NEW pressure:** PN asserts only the canonical SR docking role in cotranslational targeting, already captured (GO:0045047, GO:0006617, GO:0005785 SR complex, GO:0005525 GTP binding, GO:0005789 ER membrane). A genuinely novel SRbeta function — coordinating cotranslational N-glycosylation via OST engagement (PMID:36921042) — is in the review references but is not the PN story; nearest GO term GO:0180058 (verified real, OST-centric) is not a clean fit. Conclusion: **already captured** for the PN node (no NEW pressure on the mapping).
- **Mapping strategy:** No change needed. GO:0006614 closure-entailed projection is consistent with the review's accepted GO:0045047/0006617 (both descend the same ER-targeting branch); not broader than the review in a problematic way. Class-level GO:0015031 is a broad class target, not asserted of SRPRB.
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:16439358 SR-beta/SRalpha Longin structure; PMID:29567807 prehandover cryo-EM; PMID:34020957 SR compaction/GTPase; PMID:37643813 SRPRB KO stabilizes SRalpha) all encode SR docking biology. **MTR120 re-examination:** the cached full text of PMID:23264731 (now available) is entirely about MTR120/KIAA1383, a 120 kDa MT-associated protein found in an ORFeome localization screen; SRPRB (Q9Y5M8, 271 aa ER GTPase) is never mentioned or assayed. The GO:0005881 cytoplasmic-microtubule IDA on SRPRB is a definitive mis-attribution (wrong protein), not merely unverifiable — the review's UNDECIDED was conservative only because full text was unavailable; it now is.
- **Verdict:** Consistent for the PN node; PN already captured. One warranted edit: with full text confirming PMID:23264731 does not assay SRPRB, the cytoplasmic-microtubule annotation should move from UNDECIDED to MARK_AS_OVER_ANNOTATED (wrong-gene citation; correctness → WRONG_IDENTIFIER).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SRPRB/SRPRB-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | SRP receptor subunit
- UniProt: Q9Y5M8
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|SRP receptor subunit
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006614 SRP-dependent cotranslational protein targeting to membrane]
        rationale: SRP receptor subunits participate in docking the SRP-ribosome complex to the ER membrane during cotranslational targeting. Mapping to the GO SRP-dependent targeting process is appropriate at propagation scope.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0006614 SRP-dependent cotranslational protein targeting to membrane | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=ER proteostasis|Protein transport|SRP receptor subunit

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
