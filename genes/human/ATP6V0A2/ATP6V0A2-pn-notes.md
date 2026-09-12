# ATP6V0A2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y487
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1388)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0A2/ATP6V0A2-ai-review.yaml](ATP6V0A2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0A2/ATP6V0A2-ai-review.html](ATP6V0A2-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0A2/ATP6V0A2-notes.md](ATP6V0A2-notes.md)
- GOA TSV: present - [genes/human/ATP6V0A2/ATP6V0A2-goa.tsv](ATP6V0A2-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0A2/ATP6V0A2-uniprot.txt](ATP6V0A2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0A2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0A2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0A2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0A2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATP6V0A2/ATP6V0A2-deep-research-manual.md](ATP6V0A2-deep-research-manual.md)

## AIGR Review Snapshot

- Description: ATP6V0A2 encodes the a2 isoform of the V-type proton ATPase 116 kDa a-subunit, an integral membrane component of the V0 proton-translocation sector of the V-ATPase. The protein helps assemble and position V-ATPase activity in acidic intracellular compartments, especially early endosomes and Golgi/endolysosomal membranes, where the complex acidifies organelle lumens to support membrane trafficking, protein degradation, lysosomal function, and Golgi-dependent glycosylation. ATP6V0A2 also participates in endosomal pH-sensing through an acidification-dependent interaction with ARNO/PSCD2, and disruption of V-ATPase function affects intracellular iron availability and HIF prolyl hydroxylation. Biallelic ATP6V0A2 variants cause autosomal recessive cutis laxa type 2A and wrinkly skin syndrome with glycosylation defects.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 1; NEW: 2; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Consistent. Notes, review, PN row, and PN-node mapping all converge on the V0-sector lysosomal V-ATPase identity. The review adds exactly the three projected terms at their mapped levels and explicitly declines to promote the broader nutrient-sensing/autophagy context. No contradictions.
- **PN story / NEW pressure:** The lysosomal-specific terms were genuinely absent from ATP6V0A2 GOA (which had only broader GO:0007035 vacuolar acidification and GO:0033179/GO:0000220 V0-domain). Review adds GO:0007042 lysosomal lumen acidification (NEW) and GO:0046610 lysosomal V0 domain (NEW). I verified both are real, non-obsolete GO terms via OLS. These are defensible ADDs (more specific children of existing annotations), supported by V0-subunit identity plus lysosomal-membrane proteomics (PMID:17897319). The PN nutrient-sensing/mTORC1 story correctly does NOT generate a NEW term — review leaves it as a suggested_question/experiment only.
- **Evidence alignment:** Divergent by design. PN cites review-article titles (mTORC1, SEA/GATOR, V-ATPase structure, neurodegeneration); the review's load-bearing PMIDs are independent primary/structural sources (16415858 ARNO endosome, 33065002 human V-ATPase cryo-EM, 32001091, 17897319 lysosomal proteomics, 28296633 iron/HIF). Only the V-ATPase-structure theme overlaps conceptually.
- **Verdict:** Consistent; both lysosomal NEW terms are verified real, defensible ADDs; PN nutrient-sensing context correctly not propagated. No edits required.

## Full Consistency Review

- **UniProt:** Q9Y487 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two ALP rows — `ALP|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component` and `ALP|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component` ; **PN-node mapping:** V0 subtype leaves `mapped/ok_for_propagation` → GO:0046610 (lysosomal V0 domain) and GO:0033179 (V0 domain); Lysosomal-acidification type `mapped/ok_for_propagation` → GO:0007042; mTORC1/nutrient-sensing ancestors `no_mapping`; Pre-initiation class `context_only/too_broad` (GO:0010506).
- **Consistency:** Consistent. Notes, review, PN row, and PN-node mapping all converge on the V0-sector lysosomal V-ATPase identity. The review adds exactly the three projected terms at their mapped levels and explicitly declines to promote the broader nutrient-sensing/autophagy context. No contradictions.
- **PN story / NEW pressure:** The lysosomal-specific terms were genuinely absent from ATP6V0A2 GOA (which had only broader GO:0007035 vacuolar acidification and GO:0033179/GO:0000220 V0-domain). Review adds GO:0007042 lysosomal lumen acidification (NEW) and GO:0046610 lysosomal V0 domain (NEW). I verified both are real, non-obsolete GO terms via OLS. These are defensible ADDs (more specific children of existing annotations), supported by V0-subunit identity plus lysosomal-membrane proteomics (PMID:17897319). The PN nutrient-sensing/mTORC1 story correctly does NOT generate a NEW term — review leaves it as a suggested_question/experiment only.
- **Mapping strategy:** No change warranted. Subtype-level `ok_for_propagation` and the conservative `no_mapping`/`context_only` ancestors are right; broad mTORC1 container is correctly not propagated (matches TOMM20/HSPA8 "too broad" precedent).
- **Evidence alignment:** Divergent by design. PN cites review-article titles (mTORC1, SEA/GATOR, V-ATPase structure, neurodegeneration); the review's load-bearing PMIDs are independent primary/structural sources (16415858 ARNO endosome, 33065002 human V-ATPase cryo-EM, 32001091, 17897319 lysosomal proteomics, 28296633 iron/HIF). Only the V-ATPase-structure theme overlaps conceptually.
- **Verdict:** Consistent; both lysosomal NEW terms are verified real, defensible ADDs; PN nutrient-sensing context correctly not propagated. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6V0A2/ATP6V0A2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: Q9Y487
- In branches: ALP
- Notes: Subunit of the V0 (lysosomal membrane bound) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0046610 lysosomal proton-transporting V-type ATPase, V0 domain]
        rationale: This PN leaf is restricted to V0-sector lysosomal V-ATPase components. The GO lysosomal V0-domain component term is the direct target.
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

## PN row 2: Autophagy-Lysosome Pathway | Lysosomal catabolism | Regulation of lysosomal environment | Lysosomal acidification | V0 lysosomal v-ATPase proton pump component
- UniProt: Q9Y487
- In branches: ALP
- Notes: Subunit of the V0 (lysosomal membrane bound) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0033179 proton-transporting V-type ATPase, V0 domain]
        rationale: This PN subtype denotes the V0-sector component of the lysosomal V-type ATPase. The GO V0-domain component term is the appropriate propagation target.
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
- GO:0046610 lysosomal proton-transporting V-type ATPase, V0 domain | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033179 proton-transporting V-type ATPase, V0 domain | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
