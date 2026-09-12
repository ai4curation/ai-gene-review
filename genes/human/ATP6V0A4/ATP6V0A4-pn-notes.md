# ATP6V0A4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9HBG4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1387)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0A4/ATP6V0A4-ai-review.yaml](ATP6V0A4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0A4/ATP6V0A4-ai-review.html](ATP6V0A4-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0A4/ATP6V0A4-notes.md](ATP6V0A4-notes.md)
- GOA TSV: present - [genes/human/ATP6V0A4/ATP6V0A4-goa.tsv](ATP6V0A4-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0A4/ATP6V0A4-uniprot.txt](ATP6V0A4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0A4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0A4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0A4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0A4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V0A4 encodes the a4 isoform of the membrane-integral a subunit of the V-type proton ATPase V0 sector. The protein is a multi-pass V-ATPase component that helps couple ATP hydrolysis in the V1 sector to proton translocation through V0. It is especially important in renal acid-base physiology, where a4-containing pumps are targeted to apical membranes of intercalated cells and other nephron segments to support urinary acidification, and it is also expressed in the inner ear where loss of function can contribute to sensorineural hearing loss. Like other V-ATPase a subunits, ATP6V0A4 participates in acidification of membrane-bounded compartments and specialized extracellular-facing membranes, with its best-supported human roles centered on kidney proton secretion and V-ATPase assembly/coupling.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 7; MODIFY: 6

## PN Consistency Summary

- **Consistency:** Deep research/notes, review, and PN diverge in emphasis. ATP6V0A4 is the a4 V0 a-subunit whose best-supported human biology is **renal apical-plasma-membrane** urinary acidification and inner-ear function (dRTA, hearing loss; PMID:10973252, PMID:14638902, PMID:12414817), NOT primarily lysosomal. The review does NOT add GO:0046610 or GO:0007042; it keeps lysosomal membrane KEEP_AS_NON_CORE (HDA, PMID:17897319) and explicitly questions the PN lysosomal projection.
- **PN story / NEW pressure:** PN projects the same lysosomal V0/acidification terms it gives the c''/d2 subunits, but a4 lacks direct isoform-specific lysosomal-acidification evidence. The review's restraint is correct: **the lysosomal projection over-reaches for a4** (the a-subunit isoforms are differentially targeted; a4 → apical PM, not lysosome). proposed_new_terms empty; lysosomal terms NOT added. **Over-reaches / correctly declined in review.**
- **Evidence alignment:** PN cites generic V-ATPase/mTORC1 titles (none a4-specific); review cites a rich a4-specific renal/inner-ear literature (PMID:10973252, 12649290, 14638902, 17360703, 12414817) entirely absent from the PN row. Clear divergence; review is far better sourced.
- **Verdict:** PN LYSOSOMAL PROJECTION OVER-REACHES for a4 (renal-apical, not lysosomal); review correctly declined. **Recommended edits:** [MAP] flag GO:0046610 + GO:0007042 leaf/type projections as not_for_propagation to ATP6V0A4 (no a4-specific lysosomal evidence; isoform is apical-PM targeted); keep GO:0033179 (V0 domain, already in GOA).

## Full Consistency Review

- **UniProt:** Q9HBG4 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V0 lysosomal v-ATPase proton pump component". **PN-node mapping:** leaf→GO:0046610 (more_specific_than_existing_goa); leaf→GO:0033179 (already_in_goa_exact); type→GO:0007042 lysosomal lumen acidification (more_specific_than_existing_goa).
- **Consistency:** Deep research/notes, review, and PN diverge in emphasis. ATP6V0A4 is the a4 V0 a-subunit whose best-supported human biology is **renal apical-plasma-membrane** urinary acidification and inner-ear function (dRTA, hearing loss; PMID:10973252, PMID:14638902, PMID:12414817), NOT primarily lysosomal. The review does NOT add GO:0046610 or GO:0007042; it keeps lysosomal membrane KEEP_AS_NON_CORE (HDA, PMID:17897319) and explicitly questions the PN lysosomal projection.
- **PN story / NEW pressure:** PN projects the same lysosomal V0/acidification terms it gives the c''/d2 subunits, but a4 lacks direct isoform-specific lysosomal-acidification evidence. The review's restraint is correct: **the lysosomal projection over-reaches for a4** (the a-subunit isoforms are differentially targeted; a4 → apical PM, not lysosome). proposed_new_terms empty; lysosomal terms NOT added. **Over-reaches / correctly declined in review.**
- **Mapping strategy:** This gene *should* change the node treatment: ATP6V0A4 is a weak/contraindicated member of the "lysosomal V0 component" leaf. GO:0046610/GO:0007042 are narrower than what a4 evidence supports and risk a false lysosome-specific claim — the TOMM20/RAB7A "leaf doesn't fit this member" pattern. The leaf mapping is fine for c''/d2 but should be flagged not-for-propagation to a4.
- **Evidence alignment:** PN cites generic V-ATPase/mTORC1 titles (none a4-specific); review cites a rich a4-specific renal/inner-ear literature (PMID:10973252, 12649290, 14638902, 17360703, 12414817) entirely absent from the PN row. Clear divergence; review is far better sourced.
- **Verdict:** PN LYSOSOMAL PROJECTION OVER-REACHES for a4 (renal-apical, not lysosomal); review correctly declined. **Recommended edits:** [MAP] flag GO:0046610 + GO:0007042 leaf/type projections as not_for_propagation to ATP6V0A4 (no a4-specific lysosomal evidence; isoform is apical-PM targeted); keep GO:0033179 (V0 domain, already in GOA).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6V0A4/ATP6V0A4-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: Q9HBG4
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
- UniProt: Q9HBG4
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
