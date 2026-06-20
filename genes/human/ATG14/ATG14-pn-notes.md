# ATG14 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6ZNE5
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATG14/ATG14-ai-review.yaml](ATG14-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATG14/ATG14-ai-review.html](ATG14-ai-review.html)
- Gene notes: present - [genes/human/ATG14/ATG14-notes.md](ATG14-notes.md)
- GOA TSV: present - [genes/human/ATG14/ATG14-goa.tsv](ATG14-goa.tsv)
- UniProt record: present - [genes/human/ATG14/ATG14-uniprot.txt](ATG14-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATG14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATG14.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATG14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATG14.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATG14/ATG14-deep-research-falcon.md](ATG14-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATG14/Barkor/ATG14L is the autophagy-specific regulatory and membrane-adaptor subunit of the human class III PI3K complex I (PI3KC3-C1). It targets the PIK3C3/VPS34-PIK3R4/VPS15-BECN1 complex to ER-associated omegasome/phagophore membranes for local PI3P production and autophagosome assembly, and it also promotes later STX17-SNAP29/VAMP8-dependent autophagosome-endolysosome fusion. Its main cellular roles are autophagy initiation and autophagosome maturation rather than class I PI3K/AKT signaling.
- Existing/core annotation action counts: ACCEPT: 45; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 24; MODIFY: 12; REMOVE: 3

## PN Consistency Summary

- **Consistency:** Strongly consistent. The PN dual placement (early PI3KC3-C1 component + late STX17-SNAP29/VAMP8 fusion regulator) is exactly the two-function picture the review builds: PI3KC3-C1 recruitment/PI3P production AND ATG14-promoted autophagosome-endolysosome tethering/fusion (GO:0016240, GO:0097352 accepted; PMID:25686604). The projected GO:0034271 is precisely the review's MODIFY target — every GO:0035032 row is MODIFY→GO:0034271. No contradiction.
- **PN story / NEW pressure:** Already captured. The projected GO:0034271 is the review's own replacement term (not broader — it is *narrower* than existing GOA, the good direction). The late-fusion SNARE-regulator placement is already covered by accepted GO:0016240/GO:0097352. No new term warranted; PN adds no role the review lacks.
- **Evidence alignment:** Partial overlap. PN cites the Nature paper "ATG14 promotes membrane tethering and fusion of autophagosomes to endolysosomes" = review's PMID:25686604 (heavily used). PN's two review-article citations (Annual Review; tandfonline) are not in the review, which instead uses primary literature (PMID:20713597, 21518905, 40442316, etc.). Convergent on the load-bearing paper.
- **Verdict:** Fully consistent; PN projection matches the review's own MODIFY. No edits needed.

## Full Consistency Review

- **UniProt:** Q6ZNE5 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 2 rows, ALP — (1) `Autophagophore initiation and elongation → Class 3 PI3K complex 1, direct → Class 3 PI3K complex 1 component`; (2) `Autophagosome closure maturation and lysosome fusion → Autophagosome-lysosome docking → Lysosome-autophagosome SNARE complex regulator`. **PN-node mapping:** component leaf=mapped→GO:0034271 (PI3KC3 type I); SNARE-regulator leaf=no_mapping; ancestors context_only (GO:0035032, GO:0061909, GO:0016236). **Projected:** GO:0034271 (more_specific_than_existing_goa).
- **Consistency:** Strongly consistent. The PN dual placement (early PI3KC3-C1 component + late STX17-SNAP29/VAMP8 fusion regulator) is exactly the two-function picture the review builds: PI3KC3-C1 recruitment/PI3P production AND ATG14-promoted autophagosome-endolysosome tethering/fusion (GO:0016240, GO:0097352 accepted; PMID:25686604). The projected GO:0034271 is precisely the review's MODIFY target — every GO:0035032 row is MODIFY→GO:0034271. No contradiction.
- **PN story / NEW pressure:** Already captured. The projected GO:0034271 is the review's own replacement term (not broader — it is *narrower* than existing GOA, the good direction). The late-fusion SNARE-regulator placement is already covered by accepted GO:0016240/GO:0097352. No new term warranted; PN adds no role the review lacks.
- **Mapping strategy:** No change needed. ATG14 strengthens the GO:0034271 mapping (it is the defining C1 subunit). The SNARE-regulator leaf's no_mapping is correct — ATG14's fusion role is already individually annotated, so leaf-level propagation would be redundant. This is the inverse of the TOMM20/HSPA8 over-reach pattern: here the projection is narrower than GOA, and the review agrees.
- **Evidence alignment:** Partial overlap. PN cites the Nature paper "ATG14 promotes membrane tethering and fusion of autophagosomes to endolysosomes" = review's PMID:25686604 (heavily used). PN's two review-article citations (Annual Review; tandfonline) are not in the review, which instead uses primary literature (PMID:20713597, 21518905, 40442316, etc.). Convergent on the load-bearing paper.
- **Verdict:** Fully consistent; PN projection matches the review's own MODIFY. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/ATG14/ATG14-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Class 3 PI3K complex 1 component
- UniProt: Q6ZNE5
- In branches: ALP
- Notes: Member of class III PI3K complex 1 that produces PI(3)P at the site of phagophore nucleation. Targets the complex to the ER membrane. Also homooligomerizes and binds to STX17 in the STX17-SNAP29-VAMP8 SNARE complex to regulate autophagosome-lysosome fusion.
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Full article: Autophagy pathway: Cellular and molecular mechanisms (tandfonline.com)
    - ATG14 promotes membrane tethering and fusion of autophagosomes to endolysosomes | Nature
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I]
        rationale: This PN type is a curated component class for the direct autophagy- promoting class III PI3K complex 1. Propagation to the matching GO cellular-component term is appropriate, although the source is a component-role category rather than the complex term itself.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Autophagosome-lysosome docking | Lysosome-autophagosome SNARE complex regulator
- UniProt: Q6ZNE5
- In branches: ALP
- Notes: Member of class III PI3K complex 1 that produces PI(3)P at the site of phagophore nucleation. Targets the complex to the ER membrane. Also homooligomerizes and binds to STX17 in the STX17-SNAP29-VAMP8 SNARE complex to regulate autophagosome-lysosome fusion.
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Full article: Autophagy pathway: Cellular and molecular mechanisms (tandfonline.com)
    - ATG14 promotes membrane tethering and fusion of autophagosomes to endolysosomes | Nature
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking|Lysosome-autophagosome SNARE complex regulator
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups regulators placed around the lysosome-autophagosome SNARE complex, but the current member set mixes broad trafficking, ubiquitin, and autophagy-fusion factors rather than one clean shared GO term for SNARE-complex regulation.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking
        status=context_only scope=too_broad_to_propagate GO=[GO:0061909 autophagosome-lysosome fusion]
        rationale: Reviewed as an autophagosome-lysosome docking context. The subtree mixes component buckets and modulators, so generic fusion propagation should come only from narrower reviewed mechanism leaves.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
