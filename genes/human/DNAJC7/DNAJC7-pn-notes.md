# DNAJC7 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q99615
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC7/DNAJC7-ai-review.yaml](DNAJC7-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC7/DNAJC7-ai-review.html](DNAJC7-ai-review.html)
- Gene notes: present - [genes/human/DNAJC7/DNAJC7-notes.md](DNAJC7-notes.md)
- GOA TSV: present - [genes/human/DNAJC7/DNAJC7-goa.tsv](DNAJC7-goa.tsv)
- UniProt record: present - [genes/human/DNAJC7/DNAJC7-uniprot.txt](DNAJC7-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC7.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC7.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC7 (also called Tpr2 or TTC2) is a cytoplasmic co-chaperone of the DnaJ/Hsp40 (DNAJC) family that uniquely combines two tetratricopeptide-repeat (TPR) clusters with a C-terminal J domain. The TPR domains bind the molecular chaperones HSP70 and HSP90 simultaneously, while the J domain stimulates the ATPase activity and polypeptide binding of HSP70, allowing DNAJC7 to couple and regulate the HSP70 and HSP90 chaperone machines. It acts as a "recycling" co-chaperone that mediates retrograde transfer of folding substrates from HSP90 back onto HSP70, optimizing the maturation of clients such as the glucocorticoid and progesterone steroid receptors and protein kinases (e.g. CHK1). It is predominantly cytoplasmic but also localizes to the nucleus and associates with the cytoskeleton/microtubules; it interacts with the 9-1-1 checkpoint clamp (RAD9A-HUS1-RAD1) and recruits the nuclear receptor NR1I3/CAR to the cytoplasm. Loss-of-function variants in DNAJC7 are a recognized cause of/risk factor for amyotrophic lateral sclerosis (ALS) with TDP-43 pathology.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 17; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Fully consistent and the most richly supported of the set. Deep research (notes), review and PN converge on DNAJC7/Tpr2: dual TPR clusters + C-terminal J domain that binds HSP70 and HSP90 simultaneously and, via its J domain, stimulates HSP70 ATPase, mediating retrograde HSP90→HSP70 substrate transfer (PMID:12853476 VERIFIED, 18620420 VERIFIED); ALS risk gene. Review core MFs are GO:0001671 ATPase activator activity and GO:0031072 heat shock protein binding (both ACCEPT) — exactly matching PN row2's GO:0031072 (already_in_goa_exact, confirmed in GOA). PN row1 additionally projects GO:0030544 Hsp70 protein binding (narrower); GOA has the parent GO:0031072 but not GO:0030544.
- **PN story / NEW pressure:** Row2 already captured (GO:0031072 = review core MF, in GOA). Row1's GO:0030544 (verified real) is a more-specific ADD candidate: Tpr2's TPR domains bind both HSP70 *and* HSP90, so the broader GO:0031072 (which the review correctly chose for the *dual* HSP70/HSP90 binding) is arguably the better umbrella; GO:0030544 captures only the HSP70 arm. Defensible as a supplementary ADD but the existing GO:0031072 better reflects the joint HSP70/HSP90 cochaperone biology. The ATPase-activator MF (GO:0001671) is the strongest core call and is captured by the review but NOT projected by either PN node.
- **Evidence alignment:** PN carries no row references. Review cites verified mechanistic literature (PMID:12853476, 18620420, 11573955, 8836031) + many HT IPI rows; no divergence from PN.
- **Verdict:** Fully consistent; row2 already captured, row1 GO:0030544 a defensible-but-secondary more-specific ADD. **Recommended edits:** [MAP] note that for DNAJC7 the broader GO:0031072 (joint HSP70/HSP90 binding) is the better umbrella than the HSP70-only GO:0030544; consider also projecting the well-supported GO:0001671 ATPase activator activity (review core MF, in GOA) from the J-domain node.

## Full Consistency Review

- **UniProt:** Q99615 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** two rows — row1 `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone`; row2 `Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and J domain containing` (branch CY) ; **PN-node mapping:** row1 type → mapped/ok GO:0030544 Hsp70 protein binding (more_specific_than_existing_goa); row2 subtype → no_mapping, type → mapped/ok GO:0031072 heat shock protein binding (already_in_goa_exact); ancestors no_mapping.
- **Consistency:** Fully consistent and the most richly supported of the set. Deep research (notes), review and PN converge on DNAJC7/Tpr2: dual TPR clusters + C-terminal J domain that binds HSP70 and HSP90 simultaneously and, via its J domain, stimulates HSP70 ATPase, mediating retrograde HSP90→HSP70 substrate transfer (PMID:12853476 VERIFIED, 18620420 VERIFIED); ALS risk gene. Review core MFs are GO:0001671 ATPase activator activity and GO:0031072 heat shock protein binding (both ACCEPT) — exactly matching PN row2's GO:0031072 (already_in_goa_exact, confirmed in GOA). PN row1 additionally projects GO:0030544 Hsp70 protein binding (narrower); GOA has the parent GO:0031072 but not GO:0030544.
- **PN story / NEW pressure:** Row2 already captured (GO:0031072 = review core MF, in GOA). Row1's GO:0030544 (verified real) is a more-specific ADD candidate: Tpr2's TPR domains bind both HSP70 *and* HSP90, so the broader GO:0031072 (which the review correctly chose for the *dual* HSP70/HSP90 binding) is arguably the better umbrella; GO:0030544 captures only the HSP70 arm. Defensible as a supplementary ADD but the existing GO:0031072 better reflects the joint HSP70/HSP90 cochaperone biology. The ATPase-activator MF (GO:0001671) is the strongest core call and is captured by the review but NOT projected by either PN node.
- **Mapping strategy:** Two-row treatment is correct (J-domain HSP70 system + HSP70-HSP90 integration). Neither node over-reaches. The PN's two-node split appropriately distinguishes the J-domain HSP70 role from the TPR-mediated HSP70/HSP90 bridging role.
- **Evidence alignment:** PN carries no row references. Review cites verified mechanistic literature (PMID:12853476, 18620420, 11573955, 8836031) + many HT IPI rows; no divergence from PN.
- **Verdict:** Fully consistent; row2 already captured, row1 GO:0030544 a defensible-but-secondary more-specific ADD. **Recommended edits:** [MAP] note that for DNAJC7 the broader GO:0031072 (joint HSP70/HSP90 binding) is the better umbrella than the HSP70-only GO:0030544; consider also projecting the well-supported GO:0001671 ATPase activator activity (review core MF, in GOA) from the J-domain node.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC7/DNAJC7-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q99615
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR and J domain containing
- UniProt: Q99615
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and J domain containing
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

## Projected GO annotations (2)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
