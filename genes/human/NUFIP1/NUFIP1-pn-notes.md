# NUFIP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UHK0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NUFIP1/NUFIP1-ai-review.yaml](NUFIP1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/NUFIP1/NUFIP1-ai-review.html
- Gene notes: present - [genes/human/NUFIP1/NUFIP1-notes.md](NUFIP1-notes.md)
- GOA TSV: present - [genes/human/NUFIP1/NUFIP1-goa.tsv](NUFIP1-goa.tsv)
- UniProt record: present - [genes/human/NUFIP1/NUFIP1-uniprot.txt](NUFIP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NUFIP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NUFIP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NUFIP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NUFIP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NUFIP1 (nuclear fragile X mental retardation-interacting protein 1) is a small zinc-finger, RNA-binding nucleocytoplasmic shuttling protein with two well-supported, distinct roles. In the nucleus/nucleolus it acts as a box C/D small nucleolar ribonucleoprotein (snoRNP) biogenesis/assembly factor: as part of the R2TP-associated pre-snoRNP machinery (with ZNHIT3, BCD1/ZNHIT6 and the AAA+ ATPases RUVBL1/TIP49 and RUVBL2/TIP48), NUFIP1 serves as a scaffold that bridges interactions between the core box C/D proteins, facilitating assembly of the snoRNPs that process and modify rRNA. In the cytoplasm, upon mTORC1 inhibition/nutrient starvation, NUFIP1 relocalizes from the nucleus to autophagosomes and functions as the selective-autophagy receptor for ribosomes (ribophagy): together with its partner ZNHIT3 it binds ribosomes and delivers them to the autophagosome by directly binding the ATG8-family protein LC3B through a LIR motif, providing metabolites that support cell survival under starvation. NUFIP1 was originally identified as a nuclear interactor of the fragile X protein FMR1/FMRP and is associated with active synaptoneurosomes; it has also been reported to cooperate with BRCA1 and the elongation factor P-TEFb (via Cyclin T1) to stimulate RNA polymerase II transcription, although it does not bind DNA directly. NUFIP1 localizes mainly to the nucleoplasm, nucleolus, perichromatin fibrils and nuclear matrix, redistributing to the cytoplasm during starvation-induced ribophagy.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 21; NEW: 2

## PN Consistency Summary

- **Consistency:** Strongly consistent. PN (ribophagy receptor binding ATG8/ubiquitinated cargo), review, notes and references all agree: NUFIP1's headline cytoplasmic function is the starvation/mTORC1-induced ribophagy receptor that binds ribosomes (with ZNHIT3) and LC3B via a LIR motif (PMID:29700228, Wyant et al. Science 2018). The review also fully covers the second, nuclear box C/D snoRNP-assembly function (which PN does not address — PN is single-row, ALP-only). No contradictions; PN simply scopes only the autophagy arm.
- **PN story / NEW pressure:** Strong, defensible ADD pressure: ribophagy is genuinely absent from GOA (confirmed — NUFIP1 GOA has no ribophagy/autophagy term). GO:0034517 ribophagy is verified real. The review ALREADY adds this as a core function (GO:0034517 ribophagy involved_in + GO:0160247 autophagy cargo adaptor activity as the MF, both supported by PMID:29700228) — fully matching the PN projection. The review additionally proposes a NEW bespoke "ribophagy receptor activity" term; per the established precedent (BNIP3L/CALCOCO1) this over-reaches — the existing GO:0160247 autophagy cargo adaptor activity already captures the ribosome-LC3B bridging MF and should be used instead of minting a new term.
- **Evidence alignment:** Strong overlap on the autophagy arm. PN cites the LIR/cargo-receptor review and the Wyant ribophagy paper (= PMID:29700228, review HIGH, PubMed-verified). Review refs additionally span the snoRNP-assembly (PMID:17636026) and FMRP/transcription (PMID:10556305, 15107825) functions that PN omits.
- **Verdict:** Consistent; ribophagy ADD already implemented in review; only the proposed bespoke MF term over-reaches. **Recommended edits:** [YAML] drop the `proposed_new_terms` "ribophagy receptor activity" entry — the existing GO:0034517 ribophagy (BP) + GO:0160247 autophagy cargo adaptor activity (MF), both already in the review's core_functions, fully capture the role (mirrors the BNIP3L/CALCOCO1 "use existing terms, don't mint new" precedent).

## Full Consistency Review

- **UniProt:** Q9UHK0 · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (thorough, dual-function)
- **PN placement:** 1 row — `ALP|Autophagy substrate selection|Selective autophagy receptor|Ribophagy`. **PN-node mapping:** Ribophagy type → mapped/ok GO:0034517 ribophagy (new_to_goa); ancestors (group/class/branch) = no_mapping.
- **Consistency:** Strongly consistent. PN (ribophagy receptor binding ATG8/ubiquitinated cargo), review, notes and references all agree: NUFIP1's headline cytoplasmic function is the starvation/mTORC1-induced ribophagy receptor that binds ribosomes (with ZNHIT3) and LC3B via a LIR motif (PMID:29700228, Wyant et al. Science 2018). The review also fully covers the second, nuclear box C/D snoRNP-assembly function (which PN does not address — PN is single-row, ALP-only). No contradictions; PN simply scopes only the autophagy arm.
- **PN story / NEW pressure:** Strong, defensible ADD pressure: ribophagy is genuinely absent from GOA (confirmed — NUFIP1 GOA has no ribophagy/autophagy term). GO:0034517 ribophagy is verified real. The review ALREADY adds this as a core function (GO:0034517 ribophagy involved_in + GO:0160247 autophagy cargo adaptor activity as the MF, both supported by PMID:29700228) — fully matching the PN projection. The review additionally proposes a NEW bespoke "ribophagy receptor activity" term; per the established precedent (BNIP3L/CALCOCO1) this over-reaches — the existing GO:0160247 autophagy cargo adaptor activity already captures the ribosome-LC3B bridging MF and should be used instead of minting a new term.
- **Mapping strategy:** No node change needed. Ribophagy projection (GO:0034517) is correct, specific, and new_to_goa. Cargo-adaptor MF (GO:0160247) over bare protein binding is the prescribed receptor pattern and the review already uses it. The PN node need not also project the MF — the review covers it.
- **Evidence alignment:** Strong overlap on the autophagy arm. PN cites the LIR/cargo-receptor review and the Wyant ribophagy paper (= PMID:29700228, review HIGH, PubMed-verified). Review refs additionally span the snoRNP-assembly (PMID:17636026) and FMRP/transcription (PMID:10556305, 15107825) functions that PN omits.
- **Verdict:** Consistent; ribophagy ADD already implemented in review; only the proposed bespoke MF term over-reaches. **Recommended edits:** [YAML] drop the `proposed_new_terms` "ribophagy receptor activity" entry — the existing GO:0034517 ribophagy (BP) + GO:0160247 autophagy cargo adaptor activity (MF), both already in the review's core_functions, fully capture the role (mirrors the BNIP3L/CALCOCO1 "use existing terms, don't mint new" precedent).
- **2026-06-18 follow-up:** Implemented the YAML cleanup: added explicit NEW recommendations for GO:0034517 ribophagy and GO:0160247 autophagy cargo adaptor activity, and removed the redundant bespoke ribophagy-receptor NTR block.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/NUFIP1/NUFIP1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Ribophagy
- UniProt: Q9UHK0
- In branches: ALP
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in ribophagy
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - NUFIP1 is a ribosome receptor for starvation-induced ribophagy (science.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Ribophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034517 ribophagy]
        rationale: The PN category covers receptors for autophagic turnover of ribosomes. These genes belong in the ribophagy process, but the PN label denotes a receptor role rather than the entire process class.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0034517 ribophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Ribophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
