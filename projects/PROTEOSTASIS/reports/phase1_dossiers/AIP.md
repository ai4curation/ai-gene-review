# PN dossier: AIP

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
