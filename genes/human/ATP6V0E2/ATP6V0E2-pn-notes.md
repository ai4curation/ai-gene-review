# ATP6V0E2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NHE4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0E2/ATP6V0E2-ai-review.yaml](ATP6V0E2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0E2/ATP6V0E2-ai-review.html](ATP6V0E2-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0E2/ATP6V0E2-notes.md](ATP6V0E2-notes.md)
- GOA TSV: present - [genes/human/ATP6V0E2/ATP6V0E2-goa.tsv](ATP6V0E2-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0E2/ATP6V0E2-uniprot.txt](ATP6V0E2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0E2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0E2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0E2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0E2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V0E2 encodes the "e2" form of the V-type proton ATPase (V-ATPase) subunit e, a small (81 aa, ~9.2 kDa) integral membrane protein with two transmembrane helices. It is one of two e-subunit paralogs in human (e1 = ATP6V0E1, e2 = ATP6V0E2) and is an accessory membrane component of the V0 proton-translocation sector of the V-ATPase. The V-ATPase is a rotary proton pump composed of a peripheral, cytoplasmic V1 sector that hydrolyzes ATP and a membrane-integral V0 sector that translocates protons across the membrane; together they acidify and maintain the pH of intracellular compartments including lysosomes, endosomes, the Golgi, secretory vesicles, synaptic vesicles, clathrin-coated vesicles and phagosomes, and in some cell types the plasma membrane. As a V0 subunit, e2 contributes to the assembly and proton-pumping function of the holoenzyme; yeast complementation studies show the e-subunit is essential for proper pump function. Unlike the ubiquitously expressed e1, ATP6V0E2 has a more restricted tissue distribution with high expression in heart, brain and kidney.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Review and PN agree on the core identity: e2 is an accessory V0-sector membrane subunit (PMID:17350184 yeast complementation), part_of vacuolar V0 domain (GO:0000220/GO:0033179, both ACCEPT) and involved in proton transport/vacuolar acidification. The review carries multiple TAS lysosomal-membrane annotations (Reactome), so a lysosomal context is genuinely supported here (unlike the strictly plasma-membrane isoforms). PN-projection terms GO:0046610, GO:0007042, GO:0033179 all verified real via OLS. No contradictions. Minor: PN Notes text (shared template across the V-ATPase batch) is appropriate for e2 since it is a true V0 subunit.
- **PN story / NEW pressure:** PN asserts lysosomal V0-domain componency + lysosomal lumen acidification — more specific than the review's vacuolar-level terms. GO:0046610 (child of GO:0000220) and GO:0007042 (child of GO:0007035, which the review ACCEPTs as ISS) are defensible narrowings; e2 has lysosomal-membrane TAS support. The review did NOT add these. **ADD GO:0046610 + GO:0007042 — defensible (verified real), but mark as project-context narrowings of the already-accepted vacuolar terms.**
- **Evidence alignment:** PN cites only generic V-ATPase/mTORC1 review titles; review is better-sourced with the gene-specific PMID:17350184 (e-subunit essentiality) plus Reactome lysosomal reactions. Divergence is review-favorable; no conflict.
- **Verdict:** CONSISTENT — lysosomal projection defensible for this V0 subunit; PN terms verified real. Optional: add GO:0046610/GO:0007042 to review as conservative narrowings.

## Full Consistency Review

- **UniProt:** Q8NHE4 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V0 lysosomal v-ATPase proton pump component" (under Nutrient sensing; and under Lysosomal acidification). **PN-node mapping:** leaf→GO:0046610 lysosomal V0 domain (more_specific_than_existing_goa); leaf→GO:0033179 V0 domain (already_in_goa_exact); type→GO:0007042 lysosomal lumen acidification (more_specific_than_existing_goa). Higher ancestors no_mapping/context_only.
- **Consistency:** Review and PN agree on the core identity: e2 is an accessory V0-sector membrane subunit (PMID:17350184 yeast complementation), part_of vacuolar V0 domain (GO:0000220/GO:0033179, both ACCEPT) and involved in proton transport/vacuolar acidification. The review carries multiple TAS lysosomal-membrane annotations (Reactome), so a lysosomal context is genuinely supported here (unlike the strictly plasma-membrane isoforms). PN-projection terms GO:0046610, GO:0007042, GO:0033179 all verified real via OLS. No contradictions. Minor: PN Notes text (shared template across the V-ATPase batch) is appropriate for e2 since it is a true V0 subunit.
- **PN story / NEW pressure:** PN asserts lysosomal V0-domain componency + lysosomal lumen acidification — more specific than the review's vacuolar-level terms. GO:0046610 (child of GO:0000220) and GO:0007042 (child of GO:0007035, which the review ACCEPTs as ISS) are defensible narrowings; e2 has lysosomal-membrane TAS support. The review did NOT add these. **ADD GO:0046610 + GO:0007042 — defensible (verified real), but mark as project-context narrowings of the already-accepted vacuolar terms.**
- **Mapping strategy:** Gene legitimately supports both V0 leaves. Lysosomal projection is reasonable for e2 (broader tissue distribution: heart/brain/kidney; lysosomal Reactome+altname evidence). Projections narrow existing GOA, not over-broad. No node-mapping change needed.
- **Evidence alignment:** PN cites only generic V-ATPase/mTORC1 review titles; review is better-sourced with the gene-specific PMID:17350184 (e-subunit essentiality) plus Reactome lysosomal reactions. Divergence is review-favorable; no conflict.
- **Verdict:** CONSISTENT — lysosomal projection defensible for this V0 subunit; PN terms verified real. Optional: add GO:0046610/GO:0007042 to review as conservative narrowings.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/ATP6V0E2/ATP6V0E2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: Q8NHE4
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
- UniProt: Q8NHE4
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
