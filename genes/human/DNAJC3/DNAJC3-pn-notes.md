# DNAJC3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q13217
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC3/DNAJC3-ai-review.yaml](DNAJC3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC3/DNAJC3-ai-review.html](DNAJC3-ai-review.html)
- Gene notes: present - [genes/human/DNAJC3/DNAJC3-notes.md](DNAJC3-notes.md)
- GOA TSV: present - [genes/human/DNAJC3/DNAJC3-goa.tsv](DNAJC3-goa.tsv)
- UniProt record: present - [genes/human/DNAJC3/DNAJC3-uniprot.txt](DNAJC3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC3 (p58IPK, also ERdj6/PRKRI) is an ER-resident J-domain co-chaperone with an N-terminal TPR-repeat region (nine TPR motifs) and a C-terminal J domain. It has two interlinked roles. As a co-chaperone it binds the HSP70 chaperones BiP (HSPA5) and HSC70 (HSPA8) via its J domain, stimulates their ATPase activity, and binds misfolded proteins through its TPR groove, functioning in ER protein folding and the unfolded protein response. As a stress-inducible inhibitor of the eIF2-alpha protein kinases, it binds and inhibits PKR (EIF2AK2), PERK (EIF2AK3) and GCN2 (EIF2AK4), preventing eIF2-alpha (Ser-51/52) phosphorylation and thereby restoring/attenuating protein synthesis during ER, viral, hypothermic and amino-acid-starvation stress. It is broadly expressed (high in pancreas and testis), induced via ATF6 during ER stress, and its loss causes an autosomal-recessive syndrome of juvenile-onset diabetes mellitus with multisystem neurodegeneration (ACPHD).
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 15

## PN Consistency Summary

- **Consistency:** Consistent on the chaperone axis, but the PN node captures only half the gene. Notes/YAML describe a dual-function ER J-protein: (1) TPR+J-domain co-chaperone binding BiP (HSPA5)/HSC70 (HSPA8), stimulating their ATPase and binding misfolded substrates via the TPR groove (GO:0051087, GO:0051787 ACCEPT/core); and (2) a stress-inducible inhibitor of the eIF2-alpha kinases PKR/PERK/GCN2 (GO:0004860 protein kinase inhibitor activity, GO:0019901 protein kinase binding ACCEPT/core). The PN "J-domain HSP70 cochaperone" type correctly captures axis (1); the kinase-inhibition axis is outside this node (legitimately, since it is not an HSP70 function).
- **PN story / NEW pressure:** PN's HSP70-binding assertion is fully captured (GO:0051087 ACCEPT/core, plus misfolded protein binding). PN-projected GO:0030544 (verified real, child of GO:0051087) is a defensible narrower specialization — DNAJC3 binds HSPA8/BiP directly via its J domain. No NEW proteostasis GO term needed; the second (kinase-inhibitor) function is already richly annotated. Verdict: already captured.
- **Evidence alignment:** Review core PMIDs (8576172 PKR inhibition; 25466870 disease/BiP co-chaperone; 8666242/12601012 p58IPK) are dual-function focused; PN frames only the cochaperone half. Complementary, not contradictory.
- **Verdict:** CONSISTENT — GO:0030544 sound for the cochaperone axis; PN node intentionally scopes out the (well-captured) eIF2-alpha-kinase-inhibitor function.

## Full Consistency Review

- **UniProt:** Q13217 (p58IPK/ERdj6/PRKRI) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch ER) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (parents no_mapping)
- **Consistency:** Consistent on the chaperone axis, but the PN node captures only half the gene. Notes/YAML describe a dual-function ER J-protein: (1) TPR+J-domain co-chaperone binding BiP (HSPA5)/HSC70 (HSPA8), stimulating their ATPase and binding misfolded substrates via the TPR groove (GO:0051087, GO:0051787 ACCEPT/core); and (2) a stress-inducible inhibitor of the eIF2-alpha kinases PKR/PERK/GCN2 (GO:0004860 protein kinase inhibitor activity, GO:0019901 protein kinase binding ACCEPT/core). The PN "J-domain HSP70 cochaperone" type correctly captures axis (1); the kinase-inhibition axis is outside this node (legitimately, since it is not an HSP70 function).
- **PN story / NEW pressure:** PN's HSP70-binding assertion is fully captured (GO:0051087 ACCEPT/core, plus misfolded protein binding). PN-projected GO:0030544 (verified real, child of GO:0051087) is a defensible narrower specialization — DNAJC3 binds HSPA8/BiP directly via its J domain. No NEW proteostasis GO term needed; the second (kinase-inhibitor) function is already richly annotated. Verdict: already captured.
- **Mapping strategy:** GO:0030544 mapping appropriate; DNAJC3 has direct chaperone-binding evidence so the type-level propagation does not over-reach. The node legitimately omits the eIF2-alpha-kinase-inhibition function, which is not HSP70-system biology.
- **Evidence alignment:** Review core PMIDs (8576172 PKR inhibition; 25466870 disease/BiP co-chaperone; 8666242/12601012 p58IPK) are dual-function focused; PN frames only the cochaperone half. Complementary, not contradictory.
- **Verdict:** CONSISTENT — GO:0030544 sound for the cochaperone axis; PN node intentionally scopes out the (well-captured) eIF2-alpha-kinase-inhibitor function.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC3/DNAJC3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q13217
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] ER proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
