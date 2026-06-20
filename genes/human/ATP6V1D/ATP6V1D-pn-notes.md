# ATP6V1D PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y5K8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1D/ATP6V1D-ai-review.yaml](ATP6V1D-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1D/ATP6V1D-ai-review.html](ATP6V1D-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1D/ATP6V1D-notes.md](ATP6V1D-notes.md)
- GOA TSV: present - [genes/human/ATP6V1D/ATP6V1D-goa.tsv](ATP6V1D-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1D/ATP6V1D-uniprot.txt](ATP6V1D-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1D.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1D.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1D encodes the D subunit (28 kDa) of the V1 peripheral sector of the vacuolar-type H+-ATPase (V-ATPase). Subunit D forms the central rotor of V1 together with subunit F; ATP hydrolysis by the catalytic A3B3 hexamer drives rotation of the D-F stalk, which is mechanically coupled to the V0 proteolipid c-ring to translocate protons across organelle membranes. The human V-ATPase complex is responsible for acidifying lysosomes, endosomes, the Golgi apparatus, and other intracellular compartments, and in specialized cell types for extracellular acidification at the plasma membrane. Beyond proton pumping, the V1 D subunit directly contacts the Ragulator scaffold on lysosomes, and V-ATPase activity is required for amino acid-sensitive mTORC1 activation via an inside-out signaling mechanism. ATP6V1D additionally interacts with SNX10 and localizes to the centrosome and cilium base, where the V-ATPase is required for ciliogenesis. The protein is ubiquitously expressed in human tissues.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 27; MARK_AS_OVER_ANNOTATED: 13

## PN Consistency Summary

- **Consistency:** Consistent and information-rich. Notes ↔ review agree: D = central-rotor subunit (with F), directly contacts Ragulator p18/p14 (PMID:22053050 RESULTS), plus secondary ciliogenesis role via SNX10 (PMID:21844891). PN's mTORC1/nutrient-sensing row is directly substantiated here (GO:0071230 ACCEPT; GO:1904263, GO:0160124 KEEP_AS_NON_CORE). No contradictions.
- **PN story / NEW pressure:** No unmet pressure on PN's stated story. The review goes BEYOND PN with two non-PN roles (ciliogenesis GO:0060271/GO:0061512; centrosome GO:0005813) — these are not PN claims and need no PN action. GO:0007042 already in GOA (dossier: already_in_goa_exact; 2 hits) ACCEPT. GO:0046612 (verified) absent from GOA — defensible more-specific ADD.
- **Evidence alignment:** Divergent sources, convergent conclusion. PN cites review titles; review anchors on D-specific primaries: PMID:18752060 (d-subunit/central stalk, IDA), 22053050 (Zoncu — direct D-Ragulator), 21844891 (SNX10/cilia), 33065002. PN's mTORC1-review evidence is the weaker counterpart of the review's Zoncu primary (which here even resolves the D-p18 contact).
- **Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; review exceeds PN scope (cilia) without conflict. **Recommended edits:** [MAP] align subtype complex target GO:0033176 → GO:0046611 (lysosomal V-ATPase complex, already ACCEPTed for D).

## Full Consistency Review

- **UniProt:** Q9Y5K8 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (large, mature; ~65 annotations, full core_functions)
- **PN placement:** `Autophagy-Lysosome Pathway|...|V1 lysosomal v-ATPase proton pump component` (two rows, identical pattern) ; **PN-node mapping:** subtype=mapped/ok GO:0046612 + GO:0033176; type=mapped/ok GO:0007042; ancestors no_mapping/context_only.
- **Consistency:** Consistent and information-rich. Notes ↔ review agree: D = central-rotor subunit (with F), directly contacts Ragulator p18/p14 (PMID:22053050 RESULTS), plus secondary ciliogenesis role via SNX10 (PMID:21844891). PN's mTORC1/nutrient-sensing row is directly substantiated here (GO:0071230 ACCEPT; GO:1904263, GO:0160124 KEEP_AS_NON_CORE). No contradictions.
- **PN story / NEW pressure:** No unmet pressure on PN's stated story. The review goes BEYOND PN with two non-PN roles (ciliogenesis GO:0060271/GO:0061512; centrosome GO:0005813) — these are not PN claims and need no PN action. GO:0007042 already in GOA (dossier: already_in_goa_exact; 2 hits) ACCEPT. GO:0046612 (verified) absent from GOA — defensible more-specific ADD.
- **Mapping strategy:** D does not change node mapping but, like A, demonstrates the review already carries the more-specific GO:0046611 "lysosomal V-ATPase complex" (IDA, ACCEPT) and GO:0016471 vacuolar complex — so the subtype-complex projection GO:0033176 is broader than what the review supports.
- **Evidence alignment:** Divergent sources, convergent conclusion. PN cites review titles; review anchors on D-specific primaries: PMID:18752060 (d-subunit/central stalk, IDA), 22053050 (Zoncu — direct D-Ragulator), 21844891 (SNX10/cilia), 33065002. PN's mTORC1-review evidence is the weaker counterpart of the review's Zoncu primary (which here even resolves the D-p18 contact).
- **Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; review exceeds PN scope (cilia) without conflict. **Recommended edits:** [MAP] align subtype complex target GO:0033176 → GO:0046611 (lysosomal V-ATPase complex, already ACCEPTed for D).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1D/ATP6V1D-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: Q9Y5K8
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
- UniProt: Q9Y5K8
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
