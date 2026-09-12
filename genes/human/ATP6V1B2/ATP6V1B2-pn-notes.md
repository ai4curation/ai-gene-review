# ATP6V1B2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P21281
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1B2/ATP6V1B2-ai-review.yaml](ATP6V1B2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1B2/ATP6V1B2-ai-review.html](ATP6V1B2-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1B2/ATP6V1B2-notes.md](ATP6V1B2-notes.md)
- GOA TSV: present - [genes/human/ATP6V1B2/ATP6V1B2-goa.tsv](ATP6V1B2-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1B2/ATP6V1B2-uniprot.txt](ATP6V1B2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1B2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1B2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1B2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1B2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1B2 encodes the non-catalytic B subunit (brain isoform, B2) of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase). The V1 complex hydrolyzes ATP to power proton translocation through the membrane-embedded V0 domain. Three non-catalytic B2 subunits alternate with three catalytic A subunits (ATP6V1A) to form the catalytic AB heterohexameric ring of V1. ATP6V1B2 is the ubiquitously expressed isoform of the B subunit, in contrast to the kidney-specific B1 isoform (ATP6V1B1). V-ATPase acidifies lysosomes, endosomes, Golgi, and secretory vesicles in all cell types; in specialized cells including renal intercalated cells and melanocytes, it is found at the apical plasma membrane and in melanosomes respectively. ATP6V1B2 can partially compensate for ATP6V1B1 in renal intercalated cells under baseline conditions but not under conditions of acid load. Dominant mutations in ATP6V1B2 cause two allelic syndromes: DDOD (dominant deafness-onychodystrophy syndrome, MIM:124480) and Zimmermann-Laband syndrome type 2 (ZLS2, MIM:616455).
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 32; MARK_AS_OVER_ANNOTATED: 7

## PN Consistency Summary

- **Consistency:** Consistent. Deep research/notes ↔ review agree: non-catalytic B (brain) subunit of V1, required for assembly, ubiquitous; melanosome and renal apical roles are correctly KEEP_AS_NON_CORE. PN frames B2 generically as a "V1 lysosomal v-ATPase proton pump component," which the review supports (GO:0000221 V1 domain ACCEPT; GO:0007035/1902600 ACCEPT).
- **PN story / NEW pressure:** No over-reach, no unmet pressure. PN's mTORC1-upstream row is generic to all V1 subunits; the B2 review does NOT add mTORC1-specific annotations (unlike A/D/E1), and correctly does not invent them — defensible, since no B2-specific mTORC1 evidence exists. GO:0007042 is absent from B2's GOA (dossier: more_specific_than_existing_goa; confirmed 0 GOA hits) — a defensible ADD. GO:0046612 (verified real) also absent — defensible more-specific ADD.
- **Evidence alignment:** Minimal overlap. PN cites generic V-ATPase/mTORC1 review titles; review anchors on B2-specific primaries: PMID:2145275 (brain B-isoform cloning), 12643545 (melanosome), 29993276 (renal), 33065002 (cryo-EM), 32001091 (= one PN review, overlap). PN evidence is non-B2-specific; review evidence is gene-specific and stronger.
- **Verdict:** Consistent / ADD GO:0007042 + GO:0046612 (both verified, both genuinely new to B2 GOA); no contradictions. **Recommended edits:** none required; mappings sound as-is.

## Full Consistency Review

- **UniProt:** P21281 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (mature; ~50 annotations curated)
- **PN placement:** `Autophagy-Lysosome Pathway|...|V1 lysosomal v-ATPase proton pump component` (two rows, identical pattern to other V1 subunits) ; **PN-node mapping:** subtype=mapped/ok GO:0046612 + GO:0033176; type=mapped/ok GO:0007042; ancestors no_mapping/context_only.
- **Consistency:** Consistent. Deep research/notes ↔ review agree: non-catalytic B (brain) subunit of V1, required for assembly, ubiquitous; melanosome and renal apical roles are correctly KEEP_AS_NON_CORE. PN frames B2 generically as a "V1 lysosomal v-ATPase proton pump component," which the review supports (GO:0000221 V1 domain ACCEPT; GO:0007035/1902600 ACCEPT).
- **PN story / NEW pressure:** No over-reach, no unmet pressure. PN's mTORC1-upstream row is generic to all V1 subunits; the B2 review does NOT add mTORC1-specific annotations (unlike A/D/E1), and correctly does not invent them — defensible, since no B2-specific mTORC1 evidence exists. GO:0007042 is absent from B2's GOA (dossier: more_specific_than_existing_goa; confirmed 0 GOA hits) — a defensible ADD. GO:0046612 (verified real) also absent — defensible more-specific ADD.
- **Mapping strategy:** B2 does not change node mapping. Note B2 lacks the lysosomal-specific complex terms (GO:0046611/0033176 absent from its GOA), so the subtype-complex projection of GO:0033176 here is genuinely additive (entailed_by_goa_closure per dossier) rather than redundant — appropriate.
- **Evidence alignment:** Minimal overlap. PN cites generic V-ATPase/mTORC1 review titles; review anchors on B2-specific primaries: PMID:2145275 (brain B-isoform cloning), 12643545 (melanosome), 29993276 (renal), 33065002 (cryo-EM), 32001091 (= one PN review, overlap). PN evidence is non-B2-specific; review evidence is gene-specific and stronger.
- **Verdict:** Consistent / ADD GO:0007042 + GO:0046612 (both verified, both genuinely new to B2 GOA); no contradictions. **Recommended edits:** none required; mappings sound as-is.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1B2/ATP6V1B2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: P21281
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
- UniProt: P21281
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
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
