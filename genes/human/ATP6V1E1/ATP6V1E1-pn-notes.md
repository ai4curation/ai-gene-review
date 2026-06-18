# ATP6V1E1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P36543
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1E1/ATP6V1E1-ai-review.yaml](ATP6V1E1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1E1/ATP6V1E1-ai-review.html](ATP6V1E1-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1E1/ATP6V1E1-notes.md](ATP6V1E1-notes.md)
- GOA TSV: present - [genes/human/ATP6V1E1/ATP6V1E1-goa.tsv](ATP6V1E1-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1E1/ATP6V1E1-uniprot.txt](ATP6V1E1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1E1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1E1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1E1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1E1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1E1 encodes the E1 subunit (26 kDa) of the V1 peripheral sector of the vacuolar-type H+-ATPase (V-ATPase). Subunit E, together with subunit G, forms the three peripheral stalks of V1 that hold the catalytic head fixed against the torque of the rotating central rotor during ATP hydrolysis, enabling coupled proton translocation across organelle membranes. The V-ATPase is the primary driver of organellar acidification in eukaryotes, with key roles in lysosomal, endosomal, and Golgi pH homeostasis. In the kidney, ATP6V1E1 localizes to the apical membrane of cells in the thick ascending limb and distal convoluted tubule, where V-ATPase contributes to renal acid-base regulation. ATP6V1E1 binds aldolase (ALDOC), providing a potential coupling mechanism between glycolytic ATP supply and V-ATPase activity. Loss-of-function variants in ATP6V1E1 cause autosomal recessive cutis laxa type 2C (ARCL2C), a connective tissue disorder with skin laxity, hypotonia, and cardiovascular involvement, reflecting the ubiquitous importance of V-ATPase activity. The protein is expressed ubiquitously, with high levels in skin, and exists in three alternatively spliced isoforms.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 20; MARK_AS_OVER_ANNOTATED: 6; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Consistent. Notes ↔ review agree: E (with G) = peripheral-stalk stator; ALDOC/aldolase coupling (PMID:11399750); renal apical membrane (PMID:29993276, EXP/ACCEPT); ARCL2C disease (PMID:28065471); mTORC1 role as part of V1 (PMID:22053050, KEEP_AS_NON_CORE). PN's nutrient-sensing row is supported but appropriately non-core here. No PN/review contradiction.
- **PN story / NEW pressure:** No unmet PN pressure; review exceeds PN (aldolase/glycolysis coupling, renal acid-base) without conflict. GO:0007042 absent from E1 GOA (dossier: new_to_goa; confirmed 0 hits) — defensible ADD. GO:0046612 (verified real, OLS) absent — defensible more-specific ADD. Notable internal QC: review flags PMID:21784977 protein-binding annotation as a curation error → REMOVE (tristetraprolin/CCL3 paper, no ATP6V1E1 content) — a real data-quality catch, independent of PN.
- **Evidence alignment:** Minimal overlap. PN cites generic review titles; review anchors on E1-specific primaries: PMID:11399750 (aldolase), 20717956 (RAB11B trafficking), 28065471 (ARCL2C), 29993276 (renal), 8250920 (cloning), 33065002. PN evidence non-E1-specific.
- **Verdict:** Consistent / ADD GO:0007042 + GO:0046612 (verified, new to E1 GOA); review also makes an unrelated REMOVE for a mis-attributed citation. **Recommended edits:** [MAP] consider subtype complex GO:0033176 → GO:0046611 (already ACCEPTed for E1) for specificity.

## Full Consistency Review

- **UniProt:** P36543 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (large, mature; ~45 annotations, full core_functions; one REMOVE flagged)
- **PN placement:** `Autophagy-Lysosome Pathway|...|V1 lysosomal v-ATPase proton pump component` (two rows, identical pattern) ; **PN-node mapping:** subtype=mapped/ok GO:0046612 + GO:0033176; type=mapped/ok GO:0007042; ancestors no_mapping/context_only.
- **Consistency:** Consistent. Notes ↔ review agree: E (with G) = peripheral-stalk stator; ALDOC/aldolase coupling (PMID:11399750); renal apical membrane (PMID:29993276, EXP/ACCEPT); ARCL2C disease (PMID:28065471); mTORC1 role as part of V1 (PMID:22053050, KEEP_AS_NON_CORE). PN's nutrient-sensing row is supported but appropriately non-core here. No PN/review contradiction.
- **PN story / NEW pressure:** No unmet PN pressure; review exceeds PN (aldolase/glycolysis coupling, renal acid-base) without conflict. GO:0007042 absent from E1 GOA (dossier: new_to_goa; confirmed 0 hits) — defensible ADD. GO:0046612 (verified real, OLS) absent — defensible more-specific ADD. Notable internal QC: review flags PMID:21784977 protein-binding annotation as a curation error → REMOVE (tristetraprolin/CCL3 paper, no ATP6V1E1 content) — a real data-quality catch, independent of PN.
- **Mapping strategy:** E1 does not change node mapping. E1 GOA carries GO:0046611 (1 hit, lysosomal complex, ACCEPTed) but not GO:0033176, so the subtype-complex projection of GO:0033176 is broader than the lysosomal-specific term the review already supports.
- **Evidence alignment:** Minimal overlap. PN cites generic review titles; review anchors on E1-specific primaries: PMID:11399750 (aldolase), 20717956 (RAB11B trafficking), 28065471 (ARCL2C), 29993276 (renal), 8250920 (cloning), 33065002. PN evidence non-E1-specific.
- **Verdict:** Consistent / ADD GO:0007042 + GO:0046612 (verified, new to E1 GOA); review also makes an unrelated REMOVE for a mis-attributed citation. **Recommended edits:** [MAP] consider subtype complex GO:0033176 → GO:0046611 (already ACCEPTed for E1) for specificity.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1E1/ATP6V1E1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: P36543
- In branches: ALP
- Notes: Subunit of the V1 (cytosolic) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V1 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0046612 lysosomal proton-transporting V-type ATPase, V1 domain]
        rationale: This PN leaf is restricted to V1-sector lysosomal V-ATPase components. The GO lysosomal V1-domain component term is the direct target.
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

## PN row 2: Autophagy-Lysosome Pathway | Lysosomal catabolism | Regulation of lysosomal environment | Lysosomal acidification | V1 lysosomal v-ATPase proton pump component
- UniProt: P36543
- In branches: ALP
- Notes: Subunit of the V1 (cytosolic) component of the lysosomal v-ATPase. The V0 and V1 components of the v-ATPase assemble during amino acid starvation creating the active v-ATPase that pumps protons into the lysosome for acidification. The v-ATPase also engages in amino acid-dependent interactions with the Ragulator complex. In the presence of amino acids, the v-ATPase-Ragulator complex undergoes a conformational change that results in Ragulator exerting its GEF activity on RAGA/B.
- PN references (titles):
    - Regulation of mTORC1 by amino acids - ScienceDirect
    - Cells | Free Full-Text | SEA and GATOR 10 Years Later | HTML (mdpi.com)
    - Eukaryotic V-ATPase: Novel structural findings and functional insights - ScienceDirect
    - The emerging roles of vacuolar-type ATPase-dependent Lysosomal acidification in neurodegenerative diseases | Translational Neurodegeneration | Full Text (biomedcentral.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0033176 proton-transporting V-type ATPase complex]
        rationale: This PN subtype denotes the V1-sector component of the lysosomal V-ATPase. In the current GO cache, the broader V-type ATPase complex is the safest validated target for this component role.
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
- GO:0046612 lysosomal proton-transporting V-type ATPase, V1 domain | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V1 lysosomal v-ATPase proton pump component
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
