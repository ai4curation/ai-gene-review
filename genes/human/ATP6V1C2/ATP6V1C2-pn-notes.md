# ATP6V1C2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NEY4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1C2/ATP6V1C2-ai-review.yaml](ATP6V1C2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1C2/ATP6V1C2-ai-review.html](ATP6V1C2-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1C2/ATP6V1C2-notes.md](ATP6V1C2-notes.md)
- GOA TSV: present - [genes/human/ATP6V1C2/ATP6V1C2-goa.tsv](ATP6V1C2-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1C2/ATP6V1C2-uniprot.txt](ATP6V1C2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1C2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1C2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1C2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1C2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1C2 encodes the C2 subunit of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase), one of two human paralogs of subunit C (the other being ATP6V1C1). The V-ATPase is a multisubunit rotary proton pump in which a peripheral V1 complex hydrolyzes ATP to drive proton translocation through the membrane-embedded V0 complex, acidifying intracellular compartments (endosomes, lysosomes, Golgi, secretory vesicles) and, in some specialized cells, the extracellular space. Subunit C is present in a single copy per V1 complex and sits at the interface between the catalytic V1 head and the peripheral stator stalk, where it is required for assembly of the catalytic V1 sector. Subunit C is a key regulator of reversible V1-V0 assembly and disassembly: it dissociates from both V1 and V0 when the holoenzyme disassembles and re-binds during reassembly, making it a regulatory hub for controlling V-ATPase activity. ATP6V1C2 is a tissue-restricted isoform, originally reported as kidney- and placenta-enriched and broadly expressed in lung/kidney epithelia, in contrast to the ubiquitously expressed ATP6V1C1. It does not itself hydrolyze ATP or translocate protons but participates in the rotary catalytic mechanism as a structural and regulatory component of the V1 domain.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 13; MARK_AS_OVER_ANNOTATED: 4

## PN Consistency Summary

- **Consistency:** MOSTLY CONSISTENT. Review/notes describe C2 as a tissue-restricted (kidney/placenta/lung-epithelia) single-copy V1 subunit that is a regulatory hub for reversible V1-V0 assembly/disassembly; required for V1 assembly, contributes to GO:0046961. Crucially, C2 has DIRECT lysosomal-membrane proteomic evidence (PMID:17897319, placental lysosomal membranes — review ACCEPTs GO:0005765 lysosomal membrane). So unlike B1/G3, the lysosomal projection is genuinely supported for C2. PN-projected terms verified real (OLS). No contradiction; PN Notes template ("V1 cytosolic") fits C2.
- **PN story / NEW pressure:** PN asserts lysosomal lumen acidification (flagged new_to_goa) + lysosomal V1 domain. These narrow the review's vacuolar-level/lysosomal-membrane annotations. GO:0007042 is a child of GO:0007035 (not currently in C2's review) but is consistent with the accepted lysosomal-membrane localization. The review did NOT add GO:0007042 or GO:0046612. **ADD GO:0007042 + GO:0046612 — defensible given the lysosomal-membrane IDA-class evidence; verified real.**
- **Evidence alignment:** No overlap with PN's generic titles; review better-sourced with C2-specific PMID:12384298 (cloning, tissue-specificity), PMID:17897319 (lysosomal membrane), PMID:20093472 (Wnt/V-ATPase), PMID:21356312 (stalk isoforms). Divergence is review-favorable.
- **Verdict:** CONSISTENT — lysosomal projection supported by direct lysosomal-membrane evidence; PN terms verified real. Optional: add GO:0007042/GO:0046612 to review as narrowings.

## Full Consistency Review

- **UniProt:** Q8NEY4 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V1 lysosomal v-ATPase proton pump component" (Nutrient sensing; Lysosomal acidification). **PN-node mapping:** leaf→GO:0046612 lysosomal V1 domain (more_specific_than_existing_goa); leaf→GO:0033176 V-type ATPase complex (entailed_by_goa_closure); type→GO:0007042 lysosomal lumen acidification (new_to_goa).
- **Consistency:** MOSTLY CONSISTENT. Review/notes describe C2 as a tissue-restricted (kidney/placenta/lung-epithelia) single-copy V1 subunit that is a regulatory hub for reversible V1-V0 assembly/disassembly; required for V1 assembly, contributes to GO:0046961. Crucially, C2 has DIRECT lysosomal-membrane proteomic evidence (PMID:17897319, placental lysosomal membranes — review ACCEPTs GO:0005765 lysosomal membrane). So unlike B1/G3, the lysosomal projection is genuinely supported for C2. PN-projected terms verified real (OLS). No contradiction; PN Notes template ("V1 cytosolic") fits C2.
- **PN story / NEW pressure:** PN asserts lysosomal lumen acidification (flagged new_to_goa) + lysosomal V1 domain. These narrow the review's vacuolar-level/lysosomal-membrane annotations. GO:0007042 is a child of GO:0007035 (not currently in C2's review) but is consistent with the accepted lysosomal-membrane localization. The review did NOT add GO:0007042 or GO:0046612. **ADD GO:0007042 + GO:0046612 — defensible given the lysosomal-membrane IDA-class evidence; verified real.**
- **Mapping strategy:** Gene supports the V1 leaf and (via PMID:17897319) the lysosomal context. Projections are legitimate narrowings, not over-broad. No node-mapping change required; C2 is a positive case for the lysosomal projection.
- **Evidence alignment:** No overlap with PN's generic titles; review better-sourced with C2-specific PMID:12384298 (cloning, tissue-specificity), PMID:17897319 (lysosomal membrane), PMID:20093472 (Wnt/V-ATPase), PMID:21356312 (stalk isoforms). Divergence is review-favorable.
- **Verdict:** CONSISTENT — lysosomal projection supported by direct lysosomal-membrane evidence; PN terms verified real. Optional: add GO:0007042/GO:0046612 to review as narrowings.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/ATP6V1C2/ATP6V1C2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: Q8NEY4
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
- UniProt: Q8NEY4
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
