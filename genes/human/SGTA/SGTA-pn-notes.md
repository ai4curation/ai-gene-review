# SGTA PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O43765
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SGTA/SGTA-ai-review.yaml](SGTA-ai-review.yaml)
- AIGR review HTML: present - [genes/human/SGTA/SGTA-ai-review.html](SGTA-ai-review.html)
- Gene notes: present - [genes/human/SGTA/SGTA-notes.md](SGTA-notes.md)
- GOA TSV: present - [genes/human/SGTA/SGTA-goa.tsv](SGTA-goa.tsv)
- UniProt record: present - [genes/human/SGTA/SGTA-uniprot.txt](SGTA-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SGTA.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SGTA.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SGTA.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SGTA.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: SGTA (small glutamine-rich tetratricopeptide repeat-containing protein alpha, also called SGT or alpha-SGT) is a cytosolic TPR-domain co-chaperone that operates in the biogenesis and quality control of tail-anchored (TA) and other hydrophobic membrane proteins. Through its central TPR domain it binds the chaperones HSC70/HSPA8, HSP70 and HSP90 and regulates their ATPase activity, while its glutamine-rich and N-terminal dimerization regions mediate homodimerization and client capture. SGTA binds the transmembrane/hydrophobic segments of newly synthesized clients rapidly and, acting upstream of and together with the BAG6 complex and the ASNA1/TRC40 (GET) targeting pathway, delivers TA proteins to the endoplasmic reticulum membrane. It also functions as a quality-control rheostat; by competing with the E3 ligase RNF126 for BAG6 and promoting deubiquitination of mislocalized substrates, SGTA antagonizes BAG6-mediated ubiquitination and proteasomal triage, biasing hydrophobic clients toward maturation rather than degradation. SGTA is predominantly cytoplasmic but accumulates in the nucleus during apoptosis.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 24; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Good. Review, notes and PN agree: cytosolic TPR co-chaperone for tail-anchored/hydrophobic clients, acting with BAG6 and ASNA1/TRC40 (GET) to deliver TA proteins to the ER; QC rheostat antagonizing RNF126/BAG6. Core MFs = molecular adaptor activity (GO:0060090), BAT3-complex binding (GO:1904288); core BP = GO:0006620 + GO:0071816 (TA insertion). GET role consistent with PN.
- **PN story / NEW pressure:** No genuinely new role. PN's GO:0006620 already in review (ACCEPT, core) and GOA-exact. PN's GO:0015031 protein transport is a parent of the review's more specific GO:0006620/GO:0071816 → already captured at finer grain. PN's GO:0031072 (HSP binding) is broader than the review's GO:0051879 (Hsp90 binding). Conclude: **already captured / over-reaches** — nothing to ADD.
- **Evidence alignment:** Review cites GET/BAG6 literature (e.g. PMID:23129660) and UniProt; PN row carries no extra reference titles, so no divergence to reconcile.
- **Verdict:** Consistent; PN adds breadth only, no new defensible term. **Recommended edits:** none required; treat GO:0015031 and GO:0031072 as broader-than-review and do not propagate (gene-level GO:0006620/GO:0071816/GO:0051879 already finer) [MAP].

## Full Consistency Review

- **UniProt:** O43765 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear|Chaperone|HSP70-HSP90 joint cochaperone|CC-TPR and SGTA dimerization domain`; `ER proteostasis|Protein transport|GET pathway component` ; **PN-node mapping:** mapped → GO:0031072 (HSP binding, more_specific_than_existing_goa), GO:0015031 (protein transport, new), GO:0006620 (post-translational ER targeting, already_in_goa_exact)
- **Consistency:** Good. Review, notes and PN agree: cytosolic TPR co-chaperone for tail-anchored/hydrophobic clients, acting with BAG6 and ASNA1/TRC40 (GET) to deliver TA proteins to the ER; QC rheostat antagonizing RNF126/BAG6. Core MFs = molecular adaptor activity (GO:0060090), BAT3-complex binding (GO:1904288); core BP = GO:0006620 + GO:0071816 (TA insertion). GET role consistent with PN.
- **PN story / NEW pressure:** No genuinely new role. PN's GO:0006620 already in review (ACCEPT, core) and GOA-exact. PN's GO:0015031 protein transport is a parent of the review's more specific GO:0006620/GO:0071816 → already captured at finer grain. PN's GO:0031072 (HSP binding) is broader than the review's GO:0051879 (Hsp90 binding). Conclude: **already captured / over-reaches** — nothing to ADD.
- **Mapping strategy:** Both PN projections that aren't already exact (GO:0015031, GO:0031072) are BROADER than the review's terms (TOMM20/HSPA8/RAB7A precedent: reject broader). PN already self-flags them new/more_specific but they should not displace the gene-level specific terms. No mapping change warranted.
- **Evidence alignment:** Review cites GET/BAG6 literature (e.g. PMID:23129660) and UniProt; PN row carries no extra reference titles, so no divergence to reconcile.
- **Verdict:** Consistent; PN adds breadth only, no new defensible term. **Recommended edits:** none required; treat GO:0015031 and GO:0031072 as broader-than-review and do not propagate (gene-level GO:0006620/GO:0071816/GO:0051879 already finer) [MAP].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/SGTA/SGTA-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR and SGTA dimerization domain containing
- UniProt: O43765
- In branches: CY, ER
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and SGTA dimerization domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family/domain/subtype label. It classifies PN members but is not itself a GO annotation target; any functional assertion should come from a parent role mapping or gene-specific review.
    - [type] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031072 heat shock protein binding]
        rationale: This PN type groups joint HSP70/HSP90 cochaperones. The shared mechanistic assertion is binding heat-shock-protein chaperones, while narrower domain labels remain non-mapping unless they carry an independent activity.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: ER proteostasis | Protein transport | GET pathway component
- UniProt: O43765
- In branches: CY, ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|GET pathway component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane]
        rationale: The PN GET-pathway group covers machinery for post-translational delivery of tail-anchored membrane proteins to the ER. GO does not model the GET pathway directly in the local cache, and the closest supported process term is post-translational targeting to the ER membrane.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|GET pathway component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
