# ATP6AP2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75787
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1378)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6AP2/ATP6AP2-ai-review.yaml](ATP6AP2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6AP2/ATP6AP2-ai-review.html](ATP6AP2-ai-review.html)
- Gene notes: present - [genes/human/ATP6AP2/ATP6AP2-notes.md](ATP6AP2-notes.md)
- GOA TSV: present - [genes/human/ATP6AP2/ATP6AP2-goa.tsv](ATP6AP2-goa.tsv)
- UniProt record: present - [genes/human/ATP6AP2/ATP6AP2-uniprot.txt](ATP6AP2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6AP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6AP2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6AP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6AP2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6AP2 encodes a single-pass membrane accessory protein of the vacuolar H+-ATPase system, also known as the renin/prorenin receptor. The protein localizes to endoplasmic reticulum, endosomal, lysosomal, Golgi, and plasma-membrane contexts, where it is cleaved into N- and C-terminal fragments. Its best-supported cell-biological role is to support V-ATPase assembly and endolysosomal acidification, which are required for lysosomal protein degradation, autophagy, glycosylation homeostasis, and neuronal viability. ATP6AP2 also has context-dependent receptor and adaptor roles in renin/prorenin signaling and Wnt/V-ATPase signaling.
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 35; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 10; NEW: 2

## PN Consistency Summary

- **Consistency:** Consistent. Deep research/notes, review YAML, PN annotation, and PN-node mapping all frame ATP6AP2 as an accessory/regulatory V-ATPase subunit driving endolysosomal acidification. Review ADDED GO:0060590 (ATPase regulator activity) and GO:0070072 (V-ATPase complex assembly) as NEW, and ACCEPTs GO:0007042. No contradictions; receptor/Wnt/RAS roles are correctly held KEEP_AS_NON_CORE.
- **PN story / NEW pressure:** PN asserts a lysosomal V-ATPase regulator MF (GO:0060590) not previously in GOA. Review correctly ADDED it (action: NEW, IMP), supported by assembly-factor interaction and acidification-loss phenotypes (PMID:29127204, 30985297, 32276428). GO:0007042 already captured (ACCEPT). Verdict: PN story correctly captured — one ADD (GO:0060590), one already-captured (GO:0007042), no over-reach.
- **Evidence alignment:** PN cites a single review (V-ATPase in neurodegeneration, biomedcentral). Review draws on primary functional papers (PMID:29127204 glycosylation/autophagy disorder; PMID:30985297 neurodegeneration; PMID:32276428 lysosomal-pH) for the same claims — broader, well-anchored evidence than the PN row, with directional agreement.
- **Verdict:** Consistent; PN regulator-activity projection correctly ADDED (NEW GO:0060590), acidification already captured. No edits required.

## Full Consistency Review

- **UniProt:** O75787 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ALP|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|Regulator of the lysosomal v-ATPase proton pump` (also `...|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|Regulator...`) ; **PN-node mapping:** subtype `mapped`→GO:0060590 ATPase regulator activity (new_to_goa); type `mapped`→GO:0007042 lysosomal lumen acidification (already_in_goa_exact). Both GO terms verified real (OLS).
- **Consistency:** Consistent. Deep research/notes, review YAML, PN annotation, and PN-node mapping all frame ATP6AP2 as an accessory/regulatory V-ATPase subunit driving endolysosomal acidification. Review ADDED GO:0060590 (ATPase regulator activity) and GO:0070072 (V-ATPase complex assembly) as NEW, and ACCEPTs GO:0007042. No contradictions; receptor/Wnt/RAS roles are correctly held KEEP_AS_NON_CORE.
- **PN story / NEW pressure:** PN asserts a lysosomal V-ATPase regulator MF (GO:0060590) not previously in GOA. Review correctly ADDED it (action: NEW, IMP), supported by assembly-factor interaction and acidification-loss phenotypes (PMID:29127204, 30985297, 32276428). GO:0007042 already captured (ACCEPT). Verdict: PN story correctly captured — one ADD (GO:0060590), one already-captured (GO:0007042), no over-reach.
- **Mapping strategy:** Gene supports node mapping. The MF projection (ATPase regulator activity, deliberately broad/safe) is conservative; review even raises whether a narrower "lysosomal V-ATPase accessory" term should exist (suggested_questions). The acidification process projection matches review scope. No TOMM20-style over-broadening.
- **Evidence alignment:** PN cites a single review (V-ATPase in neurodegeneration, biomedcentral). Review draws on primary functional papers (PMID:29127204 glycosylation/autophagy disorder; PMID:30985297 neurodegeneration; PMID:32276428 lysosomal-pH) for the same claims — broader, well-anchored evidence than the PN row, with directional agreement.
- **Verdict:** Consistent; PN regulator-activity projection correctly ADDED (NEW GO:0060590), acidification already captured. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6AP2/ATP6AP2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | Regulator of the lysosomal v-ATPase proton pump
- UniProt: O75787
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
- UniProt: O75787
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
