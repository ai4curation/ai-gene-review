# FKBP5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q13451
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FKBP5/FKBP5-ai-review.yaml](FKBP5-ai-review.yaml)
- AIGR review HTML: present - [genes/human/FKBP5/FKBP5-ai-review.html](FKBP5-ai-review.html)
- Gene notes: present - [genes/human/FKBP5/FKBP5-notes.md](FKBP5-notes.md)
- GOA TSV: present - [genes/human/FKBP5/FKBP5-goa.tsv](FKBP5-goa.tsv)
- UniProt record: present - [genes/human/FKBP5/FKBP5-uniprot.txt](FKBP5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FKBP5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FKBP5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBP5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBP5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: FKBP5 (FKBP51) is a cytoplasmic immunophilin and HSP90 co-chaperone of the FKBP family. It contains two FKBP-type peptidyl-prolyl cis-trans isomerase (PPIase/rotamase) domains (active site inhibited by FK506 and rapamycin) and three C-terminal tetratricopeptide (TPR) repeats that bind the EEVD motif of HSP90. As a component of unligated steroid hormone receptor heterocomplexes (with HSP90 and HSP70), it acts as a negative regulator of glucocorticoid and progesterone receptor signaling, lowering receptor hormone-binding affinity and retaining the unliganded receptor in the cytoplasm; upon hormone binding it is displaced by its paralog FKBP4 (FKBP52). FKBP5 is a glucocorticoid-induced gene that forms an ultra-short negative feedback loop on the HPA axis, and FKBP5 genetic variation is associated with stress-related psychiatric disorders. Beyond steroid signaling, FKBP5 scaffolds the AKT1-PHLPP1 interaction to promote AKT1 dephosphorylation, negatively regulating PI3K/AKT signaling, and it engages numerous protein kinases as HSP90 clients and the IKBKB/IKBKE (IKK) machinery. It localizes mainly to the cytoplasm/cytosol with a nuclear pool.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 28; MODIFY: 7

## PN Consistency Summary

- **Consistency:** Good on the chaperone/enzyme core. Review, notes and PN agree: active FKBP PPIase (FK506/rapamycin-inhibited) + HSP90 co-chaperone in steroid-receptor heterocomplexes (negative regulator, FKBP4 antagonist) + AKT1-PHLPP1 scaffold (neg reg PI3K/AKT, GO:0051898 IDA). Core MFs GO:0003755, GO:0031072, GO:0030674 — catalytic vs scaffold both captured. One gap: PN row 3 documents an autophagy-enhancing/BECN1 role that has NO counterpart in the review (autophagy appears only as a reference title).
- **PN story / NEW pressure:** Two MF projections (GO:0003755, GO:0051879) are already in the review (GO:0051879 present ×14) → **already captured**. The autophagy/BECN1 story (FKBP5 enhances autophagy via BECN1) is real PN content but its node is deliberately context_only / too_broad_to_propagate (GO:0035032 PI3K-III complex, GO:0016236 macroautophagy) → PN projects no GO term, matching the TRAPP/overpropagation precedent. So no NEW GO term is asserted; over-reach correctly avoided.
- **Evidence alignment:** PN row 3 cites "FKBP5/FKBP51 enhances autophagy to synergize with antidepressant action" (tandfonline); this PMID is absent from the review. Review PI3K/AKT evidence (PMID:28147277, PMID:28363942) is FKBP5-specific and not in PN. Partial divergence on the autophagy paper.
- **Verdict:** Consistent on core; PN's autophagy role is documented but intentionally non-propagating, so no required edit. **Recommended edits:** none required; optionally note the FKBP5-autophagy/BECN1 paper in notes/references for completeness [REF]. Do not propagate GO:0035032/GO:0016236 (regulator, too broad) [MAP].

## Full Consistency Review

- **UniProt:** Q13451 (FKBP51) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear|Chaperone|HSP90 system|HSP90 cochaperone|CC-TPR and PPIase domain`; `Cytonuclear|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type`; `ALP|Autophagophore initiation|Class 3 PI3K complex 1|Modulator of BECN1 availability` ; **PN-node mapping:** mapped → GO:0051879 (Hsp90 binding, more_specific_than_existing_goa), GO:0003755 (PPIase, already_in_goa_exact); ALP node = context_only/too_broad_to_propagate (projects nothing)
- **Consistency:** Good on the chaperone/enzyme core. Review, notes and PN agree: active FKBP PPIase (FK506/rapamycin-inhibited) + HSP90 co-chaperone in steroid-receptor heterocomplexes (negative regulator, FKBP4 antagonist) + AKT1-PHLPP1 scaffold (neg reg PI3K/AKT, GO:0051898 IDA). Core MFs GO:0003755, GO:0031072, GO:0030674 — catalytic vs scaffold both captured. One gap: PN row 3 documents an autophagy-enhancing/BECN1 role that has NO counterpart in the review (autophagy appears only as a reference title).
- **PN story / NEW pressure:** Two MF projections (GO:0003755, GO:0051879) are already in the review (GO:0051879 present ×14) → **already captured**. The autophagy/BECN1 story (FKBP5 enhances autophagy via BECN1) is real PN content but its node is deliberately context_only / too_broad_to_propagate (GO:0035032 PI3K-III complex, GO:0016236 macroautophagy) → PN projects no GO term, matching the TRAPP/overpropagation precedent. So no NEW GO term is asserted; over-reach correctly avoided.
- **Mapping strategy:** Correct. Modulator-of-BECN1 node withheld from CC/BP propagation (regulator, not complex component); HSP-binding projection uses the narrower GO:0051879 (child of GO:0031072, OLS-verified) consistent with the review. No mapping change.
- **Evidence alignment:** PN row 3 cites "FKBP5/FKBP51 enhances autophagy to synergize with antidepressant action" (tandfonline); this PMID is absent from the review. Review PI3K/AKT evidence (PMID:28147277, PMID:28363942) is FKBP5-specific and not in PN. Partial divergence on the autophagy paper.
- **Verdict:** Consistent on core; PN's autophagy role is documented but intentionally non-propagating, so no required edit. **Recommended edits:** none required; optionally note the FKBP5-autophagy/BECN1 paper in notes/references for completeness [REF]. Do not propagate GO:0035032/GO:0016236 (regulator, too broad) [MAP].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/FKBP5/FKBP5-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | CC-TPR and PPIase domain containing
- UniProt: Q13451
- In branches: CY, ALP
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CC-TPR and PPIase domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed HSP90 cochaperone subtype with FKBP/PPIase-like members. The parent HSP90-cochaperone mapping captures the shared HSP90-binding role; a subtype-level PPIase mapping would overstate the activity for all members.
    - [type] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051879 Hsp90 protein binding]
        rationale: This PN type groups HSP90 cochaperones. Hsp90 protein binding is the most defensible shared GO molecular-function target for propagation.
    - [group] Cytonuclear proteostasis|Chaperone|HSP90 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Cytonuclear proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | FKBP type
- UniProt: Q13451
- In branches: CY, ALP
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

## PN row 3: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Modulator of class 3 PI3K complex 1 activity | Modulator of BECN1 availability
- UniProt: Q13451
- In branches: CY, ALP
- Notes: Enhances autophagy. Associates with BECN1 and influences its phosphorylation.
- PN references (titles):
    - Full article: FKBP5/FKBP51 enhances autophagy to synergize with antidepressant action (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity|Modulator of BECN1 availability
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0051879 Hsp90 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
