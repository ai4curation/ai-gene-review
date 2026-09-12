# ATP6V1F PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q16864
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1F/ATP6V1F-ai-review.yaml](ATP6V1F-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1F/ATP6V1F-ai-review.html](ATP6V1F-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1F/ATP6V1F-notes.md](ATP6V1F-notes.md)
- GOA TSV: present - [genes/human/ATP6V1F/ATP6V1F-goa.tsv](ATP6V1F-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1F/ATP6V1F-uniprot.txt](ATP6V1F-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1F.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1F.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1F.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1F.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1F encodes the F subunit (~13 kDa; 119 aa, 13,441 Da, historically called the "14-kDa subunit") of the V1 peripheral sector of the vacuolar-type H+-ATPase (V-ATPase). Together with subunit D, subunit F forms the central rotor of V1 that is driven by ATP hydrolysis in the catalytic A3B3 hexamer and transmits rotational energy to the V0 proteolipid c-ring to drive proton translocation across organelle membranes. ATP6V1F is the smallest subunit of V1 and is ubiquitously expressed, reflecting the housekeeping role of V-ATPase in acidifying lysosomes, endosomes, Golgi apparatus, and other organelles. The D-F central rotor assembly serves as the mechanical connection between the ATP-hydrolyzing head and the proton-translocating V0 membrane sector. In some cell types, the V-ATPase is targeted to the plasma membrane for extracellular acidification. The protein interacts directly with V0 d subunit (ATP6V0D1), cementing its position in the central stalk. Two alternatively spliced isoforms exist.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 11

## PN Consistency Summary

- **Consistency:** Consistent. Notes ↔ review agree: F = smallest V1 subunit (13 kDa), central-rotor with D, interacts directly with V0 d subunit (PMID:18752060); ubiquitous housekeeping. Review correctly ACCEPTs complex/MF/process core terms and marks generic membrane/monoatomic-ion/intracellular-pH terms over-annotated. No PN/review contradiction.
- **PN story / NEW pressure:** No over-reach, no unmet pressure. PN's mTORC1-upstream row is generic; the F review correctly does NOT add mTORC1/Ragulator annotations (no F-specific evidence) — defensible. GO:0007042 already in GOA (dossier: already_in_goa_exact; 2 hits) and ACCEPTed. GO:0046612 (verified real, OLS) absent from GOA — defensible more-specific ADD. GO:0033176 already in GOA (2 hits) ACCEPT.
- **Evidence alignment:** Minimal overlap. PN cites generic V-ATPase/mTORC1 review titles; review anchors on F-specific primaries: PMID:8581736 (14-kDa F cloning), 18752060 (central stalk/d-subunit, IDA), 33065002 (cryo-EM), 32001091 (= one PN review, overlap). PN evidence non-F-specific.
- **Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; no contradictions. **Recommended edits:** none required; mappings sound (broader GO:0033176 acceptable given F GOA lacks a lysosomal-specific complex term).

## Full Consistency Review

- **UniProt:** Q16864 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (mature; ~45 annotations, full core_functions)
- **PN placement:** `Autophagy-Lysosome Pathway|...|V1 lysosomal v-ATPase proton pump component` (two rows, identical pattern) ; **PN-node mapping:** subtype=mapped/ok GO:0046612 + GO:0033176; type=mapped/ok GO:0007042; ancestors no_mapping/context_only.
- **Consistency:** Consistent. Notes ↔ review agree: F = smallest V1 subunit (13 kDa), central-rotor with D, interacts directly with V0 d subunit (PMID:18752060); ubiquitous housekeeping. Review correctly ACCEPTs complex/MF/process core terms and marks generic membrane/monoatomic-ion/intracellular-pH terms over-annotated. No PN/review contradiction.
- **PN story / NEW pressure:** No over-reach, no unmet pressure. PN's mTORC1-upstream row is generic; the F review correctly does NOT add mTORC1/Ragulator annotations (no F-specific evidence) — defensible. GO:0007042 already in GOA (dossier: already_in_goa_exact; 2 hits) and ACCEPTed. GO:0046612 (verified real, OLS) absent from GOA — defensible more-specific ADD. GO:0033176 already in GOA (2 hits) ACCEPT.
- **Mapping strategy:** F does not change node mapping. F GOA lacks lysosomal-specific complex CC (GO:0046611 absent); review's most specific complex term is GO:0016471 (vacuolar V-ATPase complex, IDA/ACCEPT). The subtype-complex projection GO:0033176 is broader; GO:0046612 V1-domain target is correctly specific.
- **Evidence alignment:** Minimal overlap. PN cites generic V-ATPase/mTORC1 review titles; review anchors on F-specific primaries: PMID:8581736 (14-kDa F cloning), 18752060 (central stalk/d-subunit, IDA), 33065002 (cryo-EM), 32001091 (= one PN review, overlap). PN evidence non-F-specific.
- **Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; no contradictions. **Recommended edits:** none required; mappings sound (broader GO:0033176 acceptable given F GOA lacks a lysosomal-specific complex term).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1F/ATP6V1F-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: Q16864
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
- UniProt: Q16864
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
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
