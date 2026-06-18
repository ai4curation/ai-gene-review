# AIP PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O00170
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1347)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/AIP/AIP-ai-review.yaml](AIP-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AIP/AIP-ai-review.html](AIP-ai-review.html)
- Gene notes: present - [genes/human/AIP/AIP-notes.md](AIP-notes.md)
- GOA TSV: present - [genes/human/AIP/AIP-goa.tsv](AIP-goa.tsv)
- UniProt record: present - [genes/human/AIP/AIP-uniprot.txt](AIP-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AIP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AIP.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AIP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AIP.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AIP/AIP-deep-research-falcon.md](AIP-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AIP (AH receptor-interacting protein, also known as XAP2/ARA9) is a ~37 kDa, 330-amino acid FKBP-type immunophilin homolog that functions primarily as a non-enzymatic co-chaperone/scaffold in the HSP90-AHR (aryl hydrocarbon receptor) cytosolic complex. It contains an N-terminal FKBP-type PPIase-like domain that is catalytically inactive (lacking PPIase enzymatic activity and FK506/rapamycin binding) and C-terminal TPR repeats (three TPR motifs plus a terminal alpha-7 helix) that mediate interactions with HSP90 and TOMM20. Cryo-EM structural analysis of the human agonist-bound AHR cytosolic complex (DOI:10.1038/s41467-022-34773-w) reveals AIP/XAP2 acting as a structural brace associated with the HSP90 dimer and the AHR client, with the HSP90 C-terminal MEEVD motif docked into the TPR domain of AIP. AIP has also been reported to facilitate TOMM20-dependent mitochondrial preprotein import and to suppress thermal aggregation of model substrates in vitro, consistent with a holdase-like assay result in this import context rather than a broad protein-folding chaperone role. Beyond the AHR complex, AIP also interacts with phosphodiesterases PDE4A5 and PDE2A3, linking it to localized cAMP regulation and modulation of AHR nuclear translocation. Proteomic studies show AIP co-localizes with HSPA9 in the mitochondrial chaperone network, consistent with mitochondrial chaperone-network association (DOI:10.18632/oncotarget.24183). Germline loss-of-function AIP variants predispose to pituitary neuroendocrine tumors (PitNETs) with incomplete penetrance (~12-30%), behaving as a tumor suppressor with a two-hit model (loss of heterozygosity in tumors). AIP mutations account for ~29% of childhood-onset GH-secreting pituitary tumors presenting as gigantism and ~9% of macroprolactinomas presenting before age 20 (DOI:10.1038/s41574-023-00948-8).
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 2; REMOVE: 2; UNDECIDED: 7

## PN Consistency Summary

- **Consistency:** Deep research (falcon), review, and PN node mapping agree AIP is a cytosolic TPR co-chaperone/scaffold in the HSP90-AHR complex with FKBP-fold. Sharp, intentional divergence on the PPIase projection: PN type/group map AIP to GO:0003755, but the review REMOVEs both GO:0003755 rows (IEA and IDA/PMID:14557246) because PMID:19375531 shows the FKBP-like domain is catalytically inactive. The review explicitly states the family-level PN PPIase projection "should not be propagated for AIP." Well-reasoned, not a defect.
- **PN story / NEW pressure:** PN cochaperone target GO:0031072 heat shock protein binding is broad; the review instead adopts the more specific GO:0051879 Hsp90 protein binding (replacing obsoleting GO:0051082 and as a core_function). No NEW GO term needed — co-chaperone function already captured. Verdict: already captured (with a more specific term than PN proposes).
- **Evidence alignment:** PN dossier lists no reference titles; review verifies PPIase-inactivity via PMID:19375531 and HSP90/TPR binding via PMID:19375531/28634279, plus cryo-EM DOI:10.1038/s41467-022-34773-w. Many generic protein-binding IPI rows held UNDECIDED. No citation conflicts.
- **Verdict:** Consistent; PN PPIase (GO:0003755) projection correctly overruled with direct biochemical evidence; cochaperone role captured more specifically as GO:0051879. **Recommended edits:** none required. Optional [MAP]: note FKBP-type PPIase group GO:0003755 over-projects to catalytically-dead members (AIP); flag for gene-level gating.

## Full Consistency Review

- **UniProt:** O00170 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two rows — `Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and PPIase domain containing` and `Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type` ; **PN-node mapping:** type (cochaperone) `mapped` GO:0031072 heat shock protein binding; PPIase type/group `mapped` GO:0003755 peptidyl-prolyl cis-trans isomerase activity (already_in_goa_exact); subtype/class/branch `no_mapping`.
- **Consistency:** Deep research (falcon), review, and PN node mapping agree AIP is a cytosolic TPR co-chaperone/scaffold in the HSP90-AHR complex with FKBP-fold. Sharp, intentional divergence on the PPIase projection: PN type/group map AIP to GO:0003755, but the review REMOVEs both GO:0003755 rows (IEA and IDA/PMID:14557246) because PMID:19375531 shows the FKBP-like domain is catalytically inactive. The review explicitly states the family-level PN PPIase projection "should not be propagated for AIP." Well-reasoned, not a defect.
- **PN story / NEW pressure:** PN cochaperone target GO:0031072 heat shock protein binding is broad; the review instead adopts the more specific GO:0051879 Hsp90 protein binding (replacing obsoleting GO:0051082 and as a core_function). No NEW GO term needed — co-chaperone function already captured. Verdict: already captured (with a more specific term than PN proposes).
- **Mapping strategy:** Gene does not change the node, but is a counterexample to the FKBP/PPIase-type GO:0003755 projection (mixed PPIase/PPIase-like bucket; subtype already correctly `no_mapping`). The GO:0031072 cochaperone mapping is defensible at family level but over-broad for AIP specifically.
- **Evidence alignment:** PN dossier lists no reference titles; review verifies PPIase-inactivity via PMID:19375531 and HSP90/TPR binding via PMID:19375531/28634279, plus cryo-EM DOI:10.1038/s41467-022-34773-w. Many generic protein-binding IPI rows held UNDECIDED. No citation conflicts.
- **Verdict:** Consistent; PN PPIase (GO:0003755) projection correctly overruled with direct biochemical evidence; cochaperone role captured more specifically as GO:0051879. **Recommended edits:** none required. Optional [MAP]: note FKBP-type PPIase group GO:0003755 over-projects to catalytically-dead members (AIP); flag for gene-level gating.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AIP/AIP-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR and PPIase domain containing
- UniProt: O00170
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and PPIase domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed TPR/PPIase-domain subtype. Although several members are active peptidyl-prolyl isomerases, the bucket also contains PPIase-like cochaperones, so subtype-level PPIase propagation would overstate the shared activity.
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

## PN row 2: Cytonuclear proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | FKBP type
- UniProt: O00170
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN type denotes FKBP-family peptidyl-prolyl isomerases. The matching GO molecular-function term is appropriate for propagation.
    - [group] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN group is the cytonuclear peptidyl-prolyl isomerase branch. The matching GO molecular-function term is appropriate for propagation.
    - [class] Cytonuclear proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
