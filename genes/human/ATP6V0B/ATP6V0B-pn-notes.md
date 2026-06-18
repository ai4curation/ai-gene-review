# ATP6V0B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q99437
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1384)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0B/ATP6V0B-ai-review.yaml](ATP6V0B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0B/ATP6V0B-ai-review.html](ATP6V0B-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0B/ATP6V0B-notes.md](ATP6V0B-notes.md)
- GOA TSV: present - [genes/human/ATP6V0B/ATP6V0B-goa.tsv](ATP6V0B-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0B/ATP6V0B-uniprot.txt](ATP6V0B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATP6V0B/ATP6V0B-deep-research-cyberian.md](ATP6V0B-deep-research-cyberian.md)
- [genes/human/ATP6V0B/ATP6V0B-deep-research-falcon.md](ATP6V0B-deep-research-falcon.md)
- [genes/human/ATP6V0B/ATP6V0B-deep-research-openai.md](ATP6V0B-deep-research-openai.md)

## AIGR Review Snapshot

- Description: ATP6V0B encodes the human V-type proton ATPase V0 proteolipid subunit c''. It is a small multi-pass membrane component of the proton-translocating V0 sector, where it forms part of the c-ring rotor/pore with an essential conserved Glu98 residue required for H+ transport. ATP6V0B-containing V-ATPase complexes acidify lysosomes, endosomes, Golgi-derived compartments and other vesicles, thereby supporting endolysosomal pH homeostasis, membrane trafficking, protein degradation, autophagic flux and lysosome-associated nutrient signaling. In specialized cell contexts, V-ATPase complexes can also function at the plasma membrane to acidify the extracellular or phagosomal environment.
- Existing/core annotation action counts: ACCEPT: 37; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 2; NEW: 1; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Deep research (falcon/openai/cyberian), review, and PN agree: ATP6V0B is the V0 c'' proteolipid (5-TM, conserved Glu98 essential for H+ transport; PMID:9653649, PMID:33065002). Review ACCEPTs GO:0033179, GO:0007042, GO:0046961 rotational activity, and adds GO:0046610 (action NEW, RCA) — matching all three PN projections. No contradictions.
- **PN story / NEW pressure:** PN asserts lysosome-specific V0-domain componency (GO:0046610) not yet in GOA. Review adds it as a conservative compositional refinement (existing V0-domain + lysosomal-membrane + lysosomal acidification already present). GO:0046610 is a real term; this is component specificity, not a new process claim. **ADD GO:0046610 — implemented.**
- **Evidence alignment:** PN cites V-ATPase/mTORC1 review titles (Regulation of mTORC1 by amino acids; SEA/GATOR; Eukaryotic V-ATPase; Translational Neurodegeneration). Review's anchors (PMID:9653649 Glu98, PMID:33065002 structure) are gene-specific and stronger; PN's mTORC1 titles support the nutrient-sensing context but are not gene-specific. No conflict.
- **Verdict:** CONSISTENT — NEW GO:0046610 (verified real, conservative narrowing) appropriately added; all leaf/type projections align with review. No edits required.

## Full Consistency Review

- **UniProt:** Q99437 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V0 lysosomal v-ATPase proton pump component" (under Nutrient sensing and under Lysosomal acidification). **PN-node mapping:** leaf→GO:0046610 lysosomal V-type ATPase V0 domain (more_specific_than_existing_goa); leaf→GO:0033179 proton-transporting V-type ATPase V0 domain (already_in_goa_exact); type→GO:0007042 lysosomal lumen acidification (already_in_goa_exact).
- **Consistency:** Deep research (falcon/openai/cyberian), review, and PN agree: ATP6V0B is the V0 c'' proteolipid (5-TM, conserved Glu98 essential for H+ transport; PMID:9653649, PMID:33065002). Review ACCEPTs GO:0033179, GO:0007042, GO:0046961 rotational activity, and adds GO:0046610 (action NEW, RCA) — matching all three PN projections. No contradictions.
- **PN story / NEW pressure:** PN asserts lysosome-specific V0-domain componency (GO:0046610) not yet in GOA. Review adds it as a conservative compositional refinement (existing V0-domain + lysosomal-membrane + lysosomal acidification already present). GO:0046610 is a real term; this is component specificity, not a new process claim. **ADD GO:0046610 — implemented.**
- **Mapping strategy:** Gene genuinely belongs at the leaf (bona fide V0 c'' subunit). GO:0046610 is *narrower* than ATP6V0B's existing generic V0/lysosomal annotations and is well supported, so unlike the TOMM20/RAB7A "too-broad" rejections this projection is defensible. No mapping change needed.
- **Evidence alignment:** PN cites V-ATPase/mTORC1 review titles (Regulation of mTORC1 by amino acids; SEA/GATOR; Eukaryotic V-ATPase; Translational Neurodegeneration). Review's anchors (PMID:9653649 Glu98, PMID:33065002 structure) are gene-specific and stronger; PN's mTORC1 titles support the nutrient-sensing context but are not gene-specific. No conflict.
- **Verdict:** CONSISTENT — NEW GO:0046610 (verified real, conservative narrowing) appropriately added; all leaf/type projections align with review. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6V0B/ATP6V0B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: Q99437
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
- UniProt: Q99437
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
