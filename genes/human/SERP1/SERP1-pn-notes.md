# SERP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y6X1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SERP1/SERP1-ai-review.yaml](SERP1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SERP1/SERP1-ai-review.html
- Gene notes: present - [genes/human/SERP1/SERP1-notes.md](SERP1-notes.md)
- GOA TSV: present - [genes/human/SERP1/SERP1-goa.tsv](SERP1-goa.tsv)
- UniProt record: present - [genes/human/SERP1/SERP1-uniprot.txt](SERP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SERP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SERP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SERP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SERP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SERP1/SERP1-deep-research-falcon.md](SERP1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SERP1 (stress-associated endoplasmic reticulum protein 1, also RAMP4, ribosome-attached/associated membrane protein 4) is a small (66 aa) single-pass endoplasmic reticulum membrane protein that associates with the Sec61 translocon. It is induced by ER stress and hypoxia and binds nascent membrane and secretory proteins during their translocation into the ER, protecting these still-unfolded substrates from degradation while ER stress persists and then facilitating their N-glycosylation after stress resolves, including modulating which N-glycosylation sites are used. Through these activities SERP1 contributes to the endoplasmic reticulum unfolded protein response and to the biogenesis and quality control of membrane proteins at the translocon. It physically associates with components of the Sec61 complex (SEC61A1, SEC61B) and calnexin.
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 9; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. All describe SERP1/RAMP4 as a stress-induced, Sec61-translocon-associated single-pass ER membrane protein that stabilizes nascent membrane/secretory substrates during ER stress and facilitates post-stress N-glycosylation; 2024 cryo-EM (PMID:38896445) places RAMP4 in the Sec61 lateral gate. No contradictions. The PN group is deliberately left unmapped (heterogeneous "SEC61 accessory" members), which fits.
- **PN story / NEW pressure:** PN asserts no specific role beyond the unmapped accessory-protein grouping. SERP1's substantive functions — GO:0030968 ER unfolded protein response (IBA, CORE) and translocon-associated ER membrane localization — are already captured in GOA/review. No defensible NEW GO term is needed; review proposes none. Already captured.
- **Evidence alignment:** Good overlap on the defining paper (PMID:10601334) and translocon structure (PMID:38896445). Review extends with antiviral/ER-stress papers (DENV-2 PMID:31461934; hepatic injury PMID:35419615; translocon reviews) not enumerated in the terse PN row. Review also flags PMID:23264731 as a wrong-gene (MTR120) mis-attribution → REMOVE for GO:0005881 cytoplasmic microtubule.
- **Verdict:** Consistent and well-curated. Recommend NOT propagating class-level GO:0015031 protein transport to SERP1 (over-reach); UPR + ER-membrane already captured.

## Full Consistency Review

- **UniProt:** Q9Y6X1 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|SEC61 channel accessory protein` ; **PN-node mapping:** group "SEC61 channel accessory protein"=no_mapping (broad category); parent class "Protein transport"=mapped/ok GO:0015031 protein transport; branch=no_mapping.
- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. All describe SERP1/RAMP4 as a stress-induced, Sec61-translocon-associated single-pass ER membrane protein that stabilizes nascent membrane/secretory substrates during ER stress and facilitates post-stress N-glycosylation; 2024 cryo-EM (PMID:38896445) places RAMP4 in the Sec61 lateral gate. No contradictions. The PN group is deliberately left unmapped (heterogeneous "SEC61 accessory" members), which fits.
- **PN story / NEW pressure:** PN asserts no specific role beyond the unmapped accessory-protein grouping. SERP1's substantive functions — GO:0030968 ER unfolded protein response (IBA, CORE) and translocon-associated ER membrane localization — are already captured in GOA/review. No defensible NEW GO term is needed; review proposes none. Already captured.
- **Mapping strategy:** Concern — the parent **class** node projects **GO:0015031 protein transport** as `new_to_goa`. SERP1 is a translocon-associated substrate stabilizer/chaperone, not a transport carrier; it does not itself transport proteins. GO:0015031 over-reaches (TOMM20/HSPA8/RAB7A precedent: rejected as broader/unsupported). The group-level no_mapping decision is appropriate; the class-level GO:0015031 should not propagate to SERP1.
- **Evidence alignment:** Good overlap on the defining paper (PMID:10601334) and translocon structure (PMID:38896445). Review extends with antiviral/ER-stress papers (DENV-2 PMID:31461934; hepatic injury PMID:35419615; translocon reviews) not enumerated in the terse PN row. Review also flags PMID:23264731 as a wrong-gene (MTR120) mis-attribution → REMOVE for GO:0005881 cytoplasmic microtubule.
- **Verdict:** Consistent and well-curated. Recommend NOT propagating class-level GO:0015031 protein transport to SERP1 (over-reach); UPR + ER-membrane already captured.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SERP1/SERP1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | SEC61 channel accessory protein
- UniProt: Q9Y6X1
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|SEC61 channel accessory protein
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
