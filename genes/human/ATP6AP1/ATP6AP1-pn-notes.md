# ATP6AP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q15904
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1383)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6AP1/ATP6AP1-ai-review.yaml](ATP6AP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6AP1/ATP6AP1-ai-review.html](ATP6AP1-ai-review.html)
- Gene notes: present - [genes/human/ATP6AP1/ATP6AP1-notes.md](ATP6AP1-notes.md)
- GOA TSV: present - [genes/human/ATP6AP1/ATP6AP1-goa.tsv](ATP6AP1-goa.tsv)
- UniProt record: present - [genes/human/ATP6AP1/ATP6AP1-uniprot.txt](ATP6AP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6AP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6AP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6AP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6AP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6AP1 encodes V-type proton ATPase subunit S1, also known as Ac45, a single-pass glycoprotein accessory subunit of the vacuolar H+-ATPase. It is synthesized in the secretory pathway, localizes prominently to the ER and ER-Golgi intermediate compartment in hepatocytes, and is incorporated into the V0 sector of mature V-ATPase complexes in endolysosomal and specialized secretory membranes. ATP6AP1 supports V-ATPase assembly, targeting, stability, and activity, thereby contributing to acidification of lysosomes, endosomes, Golgi/secretory compartments, and specialized plasma-membrane domains. Through the lysosomal V-ATPase-Ragulator machinery it contributes to amino-acid-dependent mTORC1 signaling, and disruption of V-ATPase function secondarily affects iron handling and HIF1alpha regulation. Pathogenic ATP6AP1 variants cause an X-linked disorder with immunodeficiency, hepatopathy, cognitive or neurologic features, and abnormal protein glycosylation, consistent with tissue-specific defects in V-ATPase assembly and organelle homeostasis.
- Existing/core annotation action counts: ACCEPT: 26; KEEP_AS_NON_CORE: 13; MARK_AS_OVER_ANNOTATED: 11; MODIFY: 2; NEW: 1; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Deep research/notes, review, and PN agree: ATP6AP1/Ac45 is an accessory V0 assembly-hub/regulatory subunit (PMID:33065002, PMID:27231034). Review adds GO:0060590 (action NEW, IC) and ACCEPTs GO:0007042 — exactly matching both PN projections. Verified: GO:0060590 absent from goa.tsv (genuinely new); GO:0007042 present (NAS, ComplexPortal) confirming "already_in_goa_exact". No contradictions.
- **PN story / NEW pressure:** PN asserts a *regulator* MF not previously in GOA. Review correctly converts the legacy GO:0140677 (molecular function activator activity) → GO:0060590 and adds it as NEW core MF. GO:0060590 is a real term and the conservative right target (vs. uninformative protein binding, six of which are MARK_AS_OVER_ANNOTATED). **ADD GO:0060590 — implemented.**
- **Evidence alignment:** PN cites one title (Translational Neurodegeneration V-ATPase/lysosomal acidification review); review's supporting PMIDs (33065002 structural, 27231034 disease/localization, 22053050 mTORC1) are stronger and fully cover the claims. Minor: PN's single secondary-review citation is thinner than the review's primary set, but no conflict.
- **Verdict:** CONSISTENT — NEW GO:0060590 (verified real) appropriately added; PN leaf and acidification mappings align with review. No edits required.

## Full Consistency Review

- **UniProt:** Q15904 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two rows, both leaf "Regulator of the lysosomal v-ATPase proton pump": (1) `ALP|Pre-initiation autophagy signaling|mTORC1 upstream|Nutrient sensing|...` and (2) `ALP|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|...`. **PN-node mapping:** leaves = mapped, GO:0060590 ATPase regulator activity (new_to_goa); plus type-node GO:0007042 lysosomal lumen acidification (already_in_goa_exact).
- **Consistency:** Deep research/notes, review, and PN agree: ATP6AP1/Ac45 is an accessory V0 assembly-hub/regulatory subunit (PMID:33065002, PMID:27231034). Review adds GO:0060590 (action NEW, IC) and ACCEPTs GO:0007042 — exactly matching both PN projections. Verified: GO:0060590 absent from goa.tsv (genuinely new); GO:0007042 present (NAS, ComplexPortal) confirming "already_in_goa_exact". No contradictions.
- **PN story / NEW pressure:** PN asserts a *regulator* MF not previously in GOA. Review correctly converts the legacy GO:0140677 (molecular function activator activity) → GO:0060590 and adds it as NEW core MF. GO:0060590 is a real term and the conservative right target (vs. uninformative protein binding, six of which are MARK_AS_OVER_ANNOTATED). **ADD GO:0060590 — implemented.**
- **Mapping strategy:** Gene meaningfully supports the leaf mapping (it is the archetypal "regulator of lysosomal V-ATPase"). Projected GO:0060590 is neither broader nor narrower than the review's chosen core MF — they coincide. GO:0007042 type-node projection matches existing GOA. Mapping is appropriate; no change.
- **Evidence alignment:** PN cites one title (Translational Neurodegeneration V-ATPase/lysosomal acidification review); review's supporting PMIDs (33065002 structural, 27231034 disease/localization, 22053050 mTORC1) are stronger and fully cover the claims. Minor: PN's single secondary-review citation is thinner than the review's primary set, but no conflict.
- **Verdict:** CONSISTENT — NEW GO:0060590 (verified real) appropriately added; PN leaf and acidification mappings align with review. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6AP1/ATP6AP1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | Regulator of the lysosomal v-ATPase proton pump
- UniProt: Q15904
- In branches: ALP
- Notes: Adapter protein for v-ATPase and its regulators
- PN references (titles):
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|Regulator of the lysosomal v-ATPase proton pump
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0060590 ATPase regulator activity]
        rationale: This PN leaf contains ATP6AP-family regulators of the lysosomal V-ATPase. ATPase regulator activity is the safe shared molecular-function target.
    - [type] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class organizes upstream signaling inputs to autophagy initiation. Because the subtree contains generic insulin, AMPK, mTORC1, nutrient-sensing, and miscellaneous signaling components, class-level propagation to regulation of autophagy would over-annotate many genes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Lysosomal catabolism | Regulation of lysosomal environment | Lysosomal acidification | Regulator of the lysosomal v-ATPase proton pump
- UniProt: Q15904
- In branches: ALP
- Notes: Adapter protein for v-ATPase and its regulators
- PN references (titles):
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|Regulator of the lysosomal v-ATPase proton pump
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0060590 ATPase regulator activity]
        rationale: This PN subtype is a regulator of the lysosomal V-ATPase proton pump. ATPase regulator activity is the narrowest GO target that preserves the source mechanism without requiring a speculative complex-specific term.
    - [type] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0007042 lysosomal lumen acidification]
        rationale: This PN group directly names the lysosomal acidification mechanism. Propagation to the GO lysosomal lumen acidification term is an exact mechanistic match.
    - [group] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Lysosomal catabolism
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad lysosomal-degradation container. The subtree includes carbohydrate, lipid, protein, nuclease, phosphatase, sulfatase, and environment-regulation roles, so mapping should occur at the enzyme or process subtype level.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0060590 ATPase regulator activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|Regulator of the lysosomal v-ATPase proton pump
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0060590 ATPase regulator activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|Regulator of the lysosomal v-ATPase proton pump

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
