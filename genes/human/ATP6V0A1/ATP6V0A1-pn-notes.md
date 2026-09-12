# ATP6V0A1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q93050
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1381)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0A1/ATP6V0A1-ai-review.yaml](ATP6V0A1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0A1/ATP6V0A1-ai-review.html](ATP6V0A1-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0A1/ATP6V0A1-notes.md](ATP6V0A1-notes.md)
- GOA TSV: present - [genes/human/ATP6V0A1/ATP6V0A1-goa.tsv](ATP6V0A1-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0A1/ATP6V0A1-uniprot.txt](ATP6V0A1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0A1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0A1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0A1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0A1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V0A1 encodes the a1 isoform of the V0 membrane sector of the vacuolar H+-ATPase. It is a multi-pass membrane subunit that helps assemble the proton-translocation sector of V-ATPase complexes on endolysosomal, synaptic vesicle, secretory vesicle, melanosomal, and specialized plasma membranes. By contributing to ATP-driven proton transport, ATP6V0A1 supports acidification of lysosomes, endosomes, synaptic vesicles, and related organelles; pathogenic variants impair endolysosomal acidification and cause severe neurodevelopmental disease with synaptic and autophagy defects.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 5; MODIFY: 1; NEW: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Consistent. Notes/review YAML, PN annotation, and PN-node mapping all describe ATP6V0A1 as the brain-enriched V0 a1-subunit of the lysosomal/synaptic-vesicle V-ATPase. Review ACCEPTs generic GO:0033179 ("already consistent with the PN projection") and ADDED GO:0046610 (action: NEW, IC, part_of) as the lysosome-specific refinement. No contradictions.
- **PN story / NEW pressure:** PN's lysosome-specific V0 term (GO:0046610) was more_specific_than_existing GOA; review correctly ADDED it, supported by ATP6V0A1 disease variants impairing lysosomal/endolysosomal acidification (PMID:33833240, 34909687). Generic V0 (GO:0033179) and acidification (GO:0007042) already captured. Verdict: one ADD (GO:0046610), rest already-captured — no over-reach.
- **Evidence alignment:** PN cites the same V-ATPase/mTORC1 review set as ATP6V0C. Review anchors claims to gene-specific disease/functional papers (PMID:33833240 ATP6V0A1 variants; PMID:34909687 endolysosome acidification; PMID:33065002 structure) — more primary and gene-specific than the PN row. Convergent direction.
- **Verdict:** Consistent; PN lysosomal-V0 projection correctly ADDED (NEW GO:0046610). Optional: harmonize NEW-row evidence code with ATP6V0C (IC vs TAS).

## Full Consistency Review

- **UniProt:** Q93050 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ALP|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component` (also `...|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0...`) ; **PN-node mapping:** subtype `mapped`→GO:0046610 lysosomal V0 domain (Pre-init leaf, more_specific_than_existing_goa) / GO:0033179 V0 domain (Lysosomal leaf, already_in_goa_exact); type `mapped`→GO:0007042 lysosomal lumen acidification.
- **Consistency:** Consistent. Notes/review YAML, PN annotation, and PN-node mapping all describe ATP6V0A1 as the brain-enriched V0 a1-subunit of the lysosomal/synaptic-vesicle V-ATPase. Review ACCEPTs generic GO:0033179 ("already consistent with the PN projection") and ADDED GO:0046610 (action: NEW, IC, part_of) as the lysosome-specific refinement. No contradictions.
- **PN story / NEW pressure:** PN's lysosome-specific V0 term (GO:0046610) was more_specific_than_existing GOA; review correctly ADDED it, supported by ATP6V0A1 disease variants impairing lysosomal/endolysosomal acidification (PMID:33833240, 34909687). Generic V0 (GO:0033179) and acidification (GO:0007042) already captured. Verdict: one ADD (GO:0046610), rest already-captured — no over-reach.
- **Mapping strategy:** Gene supports node mapping; projected lysosomal-V0 term is narrower than the existing generic V0/complex annotations — an appropriate refinement. Notably the review used evidence code IC for the NEW row (vs TAS in the parallel ATP6V0C review) — a minor cross-gene inconsistency in how the same PN-derived lysosomal-V0 refinement is coded.
- **Evidence alignment:** PN cites the same V-ATPase/mTORC1 review set as ATP6V0C. Review anchors claims to gene-specific disease/functional papers (PMID:33833240 ATP6V0A1 variants; PMID:34909687 endolysosome acidification; PMID:33065002 structure) — more primary and gene-specific than the PN row. Convergent direction.
- **Verdict:** Consistent; PN lysosomal-V0 projection correctly ADDED (NEW GO:0046610). Optional: harmonize NEW-row evidence code with ATP6V0C (IC vs TAS).
- **Recommended edits:** [YAML] Consider aligning the GO:0046610 NEW-row evidence code between ATP6V0A1 (IC) and ATP6V0C (TAS) for consistency across the V0 PN refinements (low priority; both are defensible).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6V0A1/ATP6V0A1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: Q93050
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
- UniProt: Q93050
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
