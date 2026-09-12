# ATP6V0C PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P27449
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1380)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0C/ATP6V0C-ai-review.yaml](ATP6V0C-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0C/ATP6V0C-ai-review.html](ATP6V0C-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0C/ATP6V0C-notes.md](ATP6V0C-notes.md)
- GOA TSV: present - [genes/human/ATP6V0C/ATP6V0C-goa.tsv](ATP6V0C-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0C/ATP6V0C-uniprot.txt](ATP6V0C-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0C.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0C.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0C.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0C.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATP6V0C/ATP6V0C-deep-research-cyberian.md](ATP6V0C-deep-research-cyberian.md)
- [genes/human/ATP6V0C/ATP6V0C-deep-research-falcon.md](ATP6V0C-deep-research-falcon.md)
- [genes/human/ATP6V0C/ATP6V0C-deep-research-openai.md](ATP6V0C-deep-research-openai.md)
- [genes/human/ATP6V0C/ATP6V0C-deep-research-perplexity.md](ATP6V0C-deep-research-perplexity.md)

## AIGR Review Snapshot

- Description: ATP6V0C encodes the 16 kDa proteolipid subunit c of the V0 domain of vacuolar H+-ATPase (V-ATPase). This small (155 amino acid) integral membrane protein with four transmembrane helices is a core structural component of the proton-conducting c-ring rotor. Nine copies of ATP6V0C assemble with one copy of ATP6V0B (subunit c'') to form the complete c-ring within the V0 membrane domain. The c-ring rotates during ATP hydrolysis by the V1 domain, enabling proton translocation across membranes via a conserved glutamate residue (E139) that serves as the proton-binding site. ATP6V0C-containing V-ATPases acidify lysosomes, endosomes, Golgi, synaptic vesicles, and secretory granules, and in specialized cells (osteoclasts, kidney intercalated cells) also function at the plasma membrane. ATP6V0C is the binding target of the V-ATPase inhibitor bafilomycin A1. Heterozygous pathogenic variants in ATP6V0C cause early-onset epilepsy with or without developmental delay (EPEO3, OMIM 620465).
- Existing/core annotation action counts: ACCEPT: 53; KEEP_AS_NON_CORE: 10; MARK_AS_OVER_ANNOTATED: 1; NEW: 1; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Consistent. Four deep-research files (openai/falcon/perplexity/cyberian), review YAML, PN annotation, and PN-node mapping all describe ATP6V0C as the c-ring proteolipid of the V0 sector driving organelle/lysosomal acidification. Review ADDED GO:0046610 (action: NEW, part_of, TAS) as a lysosome-specific refinement and ACCEPTs GO:0007042 and GO:0033179. mTORC1/Wnt roles held non-core. No contradictions.
- **PN story / NEW pressure:** PN's lysosome-specific V0 term (GO:0046610) was not previously in GOA; review correctly ADDED it as a conservative refinement of existing generic GO:0033179 + lysosomal-membrane annotations, declining the broader "autophagy-initiation/mTORC1 process" reading. Acidification (GO:0007042) and generic V0 (GO:0033179) already captured. Verdict: one ADD (GO:0046610), rest already-captured — correctly handled, no over-reach.
- **Evidence alignment:** PN cites V-ATPase/mTORC1 reviews (amino-acid sensing, SEA/GATOR, V-ATPase structure, neurodegeneration). Review anchors the same complex/acidification claims to the primary structural paper (PMID:33065002) and the V-ATPase review (PMID:32001091), plus disease-variant work (PMID:36074901). Convergent; review evidence is more primary. Review also correctly REMOVEs two ATP-synthase mis-annotations (GO:0015986, GO:0046933).
- **Verdict:** Consistent; PN lysosomal-V0 projection correctly ADDED (NEW GO:0046610). No edits required.

## Full Consistency Review

- **UniProt:** P27449 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ALP|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component` (also `...|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0...`) ; **PN-node mapping:** subtype `mapped`→GO:0046610 lysosomal V0 domain (Pre-init leaf, more_specific_than_existing_goa) / GO:0033179 V0 domain (Lysosomal leaf, already_in_goa_exact); type `mapped`→GO:0007042 lysosomal lumen acidification (already_in_goa_exact). GO:0046610 verified real (OLS).
- **Consistency:** Consistent. Four deep-research files (openai/falcon/perplexity/cyberian), review YAML, PN annotation, and PN-node mapping all describe ATP6V0C as the c-ring proteolipid of the V0 sector driving organelle/lysosomal acidification. Review ADDED GO:0046610 (action: NEW, part_of, TAS) as a lysosome-specific refinement and ACCEPTs GO:0007042 and GO:0033179. mTORC1/Wnt roles held non-core. No contradictions.
- **PN story / NEW pressure:** PN's lysosome-specific V0 term (GO:0046610) was not previously in GOA; review correctly ADDED it as a conservative refinement of existing generic GO:0033179 + lysosomal-membrane annotations, declining the broader "autophagy-initiation/mTORC1 process" reading. Acidification (GO:0007042) and generic V0 (GO:0033179) already captured. Verdict: one ADD (GO:0046610), rest already-captured — correctly handled, no over-reach.
- **Mapping strategy:** Gene supports node mapping. Projected lysosome-specific component term is narrower than the existing generic V0/complex annotations — an appropriate refinement, not an over-broad process projection. The dossier's two leaves redundantly target the same protein with V0/lysosomal-V0 terms, consistent with review.
- **Evidence alignment:** PN cites V-ATPase/mTORC1 reviews (amino-acid sensing, SEA/GATOR, V-ATPase structure, neurodegeneration). Review anchors the same complex/acidification claims to the primary structural paper (PMID:33065002) and the V-ATPase review (PMID:32001091), plus disease-variant work (PMID:36074901). Convergent; review evidence is more primary. Review also correctly REMOVEs two ATP-synthase mis-annotations (GO:0015986, GO:0046933).
- **Verdict:** Consistent; PN lysosomal-V0 projection correctly ADDED (NEW GO:0046610). No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6V0C/ATP6V0C-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: P27449
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
- UniProt: P27449
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
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033179 proton-transporting V-type ATPase, V0 domain | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
