# ATP6V1C1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P21283
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1C1/ATP6V1C1-ai-review.yaml](ATP6V1C1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1C1/ATP6V1C1-ai-review.html](ATP6V1C1-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1C1/ATP6V1C1-notes.md](ATP6V1C1-notes.md)
- GOA TSV: present - [genes/human/ATP6V1C1/ATP6V1C1-goa.tsv](ATP6V1C1-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1C1/ATP6V1C1-uniprot.txt](ATP6V1C1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1C1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1C1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1C1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1C1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1C1 encodes the C1 subunit of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase). The V1 complex hydrolyzes ATP to drive proton translocation through the membrane-embedded V0 domain. Subunit C (C1) is a regulatory subunit present in a single copy per V1 complex, where it is necessary for assembly of the catalytic V1 sector and likely has a specific function in its catalytic activity. ATP6V1C1 is ubiquitously expressed in human tissues. The paralog ATP6V1C2 is expressed specifically in testes. V-ATPase acidifies lysosomes, endosomes, Golgi, and secretory vesicles; ATP6V1C1 is found at the lysosomal membrane and at synaptic vesicle and clathrin-coated vesicle membranes (by similarity). During regulated V1-V0 disassembly under nutrient starvation, the V1 complex including C1 is released into the cytosol.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 23; MARK_AS_OVER_ANNOTATED: 4

## PN Consistency Summary

- **Consistency:** Consistent. Notes ↔ review agree: single-copy regulatory C subunit, required for V1 catalytic-sector assembly, ubiquitous (paralog C2 = testis). Review correctly ACCEPTs complex/process/MF core terms and marks regulation-of-macroautophagy and exosome HDA as over-annotated. No PN/review contradiction.
- **PN story / NEW pressure:** No over-reach. The PN mTORC1-upstream row is generic; the C1 review correctly does NOT add mTORC1/Ragulator annotations (no C1-specific evidence). GO:0007042 absent from C1 GOA (dossier: new_to_goa; confirmed 0 hits) — defensible ADD. GO:0046612 (verified real, OLS) absent — defensible more-specific ADD. GO:0033176 already in GOA (1 hit) and ACCEPTed.
- **Evidence alignment:** Minimal overlap. PN cites generic V-ATPase/mTORC1 review titles; review anchors on C1-specific primaries: PMID:8250920 (C/D/E cloning), 12384298 (C/G/d isoforms), 16415858 (ARNO/Arf6 — correctly noted as V0 c-subunit not V1-C), 17897319 (lyso proteomics), 33065002. The 16415858 caveat (interaction attributed to other subunits) is a good catch unique to this review.
- **Verdict:** Consistent / ADD GO:0007042 + GO:0046612 (verified, new to C1 GOA); no contradictions. **Recommended edits:** none required; mappings sound.

## Full Consistency Review

- **UniProt:** P21283 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (mature; ~35 annotations, no core_functions block but full annotation review)
- **PN placement:** `Autophagy-Lysosome Pathway|...|V1 lysosomal v-ATPase proton pump component` (two rows, identical pattern) ; **PN-node mapping:** subtype=mapped/ok GO:0046612 + GO:0033176; type=mapped/ok GO:0007042; ancestors no_mapping/context_only.
- **Consistency:** Consistent. Notes ↔ review agree: single-copy regulatory C subunit, required for V1 catalytic-sector assembly, ubiquitous (paralog C2 = testis). Review correctly ACCEPTs complex/process/MF core terms and marks regulation-of-macroautophagy and exosome HDA as over-annotated. No PN/review contradiction.
- **PN story / NEW pressure:** No over-reach. The PN mTORC1-upstream row is generic; the C1 review correctly does NOT add mTORC1/Ragulator annotations (no C1-specific evidence). GO:0007042 absent from C1 GOA (dossier: new_to_goa; confirmed 0 hits) — defensible ADD. GO:0046612 (verified real, OLS) absent — defensible more-specific ADD. GO:0033176 already in GOA (1 hit) and ACCEPTed.
- **Mapping strategy:** C1 does not change node mapping. C1's GOA lacks lysosomal-specific CC (GO:0046611 absent), so the broader GO:0033176 subtype-complex target is the correct safest choice here; the V1-domain projection GO:0046612 adds lysosomal specificity. Both projections additive and appropriate.
- **Evidence alignment:** Minimal overlap. PN cites generic V-ATPase/mTORC1 review titles; review anchors on C1-specific primaries: PMID:8250920 (C/D/E cloning), 12384298 (C/G/d isoforms), 16415858 (ARNO/Arf6 — correctly noted as V0 c-subunit not V1-C), 17897319 (lyso proteomics), 33065002. The 16415858 caveat (interaction attributed to other subunits) is a good catch unique to this review.
- **Verdict:** Consistent / ADD GO:0007042 + GO:0046612 (verified, new to C1 GOA); no contradictions. **Recommended edits:** none required; mappings sound.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1C1/ATP6V1C1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: P21283
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
- UniProt: P21283
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
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
