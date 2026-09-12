# SERP2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N6R1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SERP2/SERP2-ai-review.yaml](SERP2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SERP2/SERP2-ai-review.html
- Gene notes: present - [genes/human/SERP2/SERP2-notes.md](SERP2-notes.md)
- GOA TSV: present - [genes/human/SERP2/SERP2-goa.tsv](SERP2-goa.tsv)
- UniProt record: present - [genes/human/SERP2/SERP2-uniprot.txt](SERP2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SERP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SERP2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SERP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SERP2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SERP2/SERP2-deep-research-falcon.md](SERP2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SERP2 (stress-associated endoplasmic reticulum protein 2, also RAMP4-2, ribosome-associated membrane protein RAMP4-2) is a small (65 aa) single-pass endoplasmic reticulum membrane protein of the RAMP4 family and a paralog of SERP1/RAMP4. Like SERP1, it associates with the Sec61 translocon and binds nascent membrane and secretory proteins during their translocation into the ER, protecting these still-unfolded substrates from degradation during ER stress and facilitating their N-glycosylation after stress resolves, including modulating which N-glycosylation sites are used. Through these activities SERP2 contributes to the endoplasmic reticulum unfolded protein response and to membrane-protein biogenesis at the translocon. It physically associates with components of the Sec61 complex (SEC61A1, SEC61B) and calnexin. Its function is established largely by orthology and paralogy, and it is less experimentally characterized than SERP1.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 4

## PN Consistency Summary

- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. All describe SERP2/RAMP4-2 as a single-pass ER membrane RAMP4-family paralog of SERP1, translocon-associated, stabilizing nascent membrane/secretory substrates during ER stress; function established largely by orthology/paralogy (less experimentally characterized than SERP1). No contradictions. The review adds a SERP2-specific experimental fact the PN row omits: RAMP4-2 is a tail-anchored substrate of the SPPL2c/SPP intramembrane proteases (PMID:30733280, PMID:37261541).
- **PN story / NEW pressure:** PN asserts only the unmapped accessory-protein grouping. SERP2's core functions — GO:0030968 ER unfolded protein response (IBA) and ER-membrane localization — are already in GOA/review. No defensible NEW GO term; review proposes none. Already captured. (The SPPL2c-substrate property is interesting but the review correctly added it as references only, no new GO assertion.)
- **Evidence alignment:** PN row is terse; review references go well beyond it (SPPL2c substrate papers, translocon Insight PMID:38787756, Gemmer & Forster review PMID:32019826). Overlap is essentially at the family/orthology level since both rely on RAMP4-family inference rather than SERP2-specific GOA experimental annotations (GOA has only IBA + 2 bare protein-binding IPI).
- **Verdict:** Consistent and well-curated. Recommend NOT propagating class-level GO:0015031 protein transport to SERP2 (over-reach); UPR + ER-membrane already captured.

## Full Consistency Review

- **UniProt:** Q8N6R1 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|SEC61 channel accessory protein` ; **PN-node mapping:** group "SEC61 channel accessory protein"=no_mapping (broad category); parent class "Protein transport"=mapped/ok GO:0015031 protein transport; branch=no_mapping.
- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. All describe SERP2/RAMP4-2 as a single-pass ER membrane RAMP4-family paralog of SERP1, translocon-associated, stabilizing nascent membrane/secretory substrates during ER stress; function established largely by orthology/paralogy (less experimentally characterized than SERP1). No contradictions. The review adds a SERP2-specific experimental fact the PN row omits: RAMP4-2 is a tail-anchored substrate of the SPPL2c/SPP intramembrane proteases (PMID:30733280, PMID:37261541).
- **PN story / NEW pressure:** PN asserts only the unmapped accessory-protein grouping. SERP2's core functions — GO:0030968 ER unfolded protein response (IBA) and ER-membrane localization — are already in GOA/review. No defensible NEW GO term; review proposes none. Already captured. (The SPPL2c-substrate property is interesting but the review correctly added it as references only, no new GO assertion.)
- **Mapping strategy:** Concern — parent **class** node projects **GO:0015031 protein transport** as `new_to_goa`. As for SERP1, SERP2 is a translocon-associated stabilizer, not a transport carrier; GO:0015031 over-reaches (TOMM20/HSPA8/RAB7A precedent). The group-level no_mapping is correct; do not propagate class-level GO:0015031 to SERP2.
- **Evidence alignment:** PN row is terse; review references go well beyond it (SPPL2c substrate papers, translocon Insight PMID:38787756, Gemmer & Forster review PMID:32019826). Overlap is essentially at the family/orthology level since both rely on RAMP4-family inference rather than SERP2-specific GOA experimental annotations (GOA has only IBA + 2 bare protein-binding IPI).
- **Verdict:** Consistent and well-curated. Recommend NOT propagating class-level GO:0015031 protein transport to SERP2 (over-reach); UPR + ER-membrane already captured.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SERP2/SERP2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | SEC61 channel accessory protein
- UniProt: Q8N6R1
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
