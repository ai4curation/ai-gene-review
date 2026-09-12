# ATP6V1G2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O95670
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1G2/ATP6V1G2-ai-review.yaml](ATP6V1G2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1G2/ATP6V1G2-ai-review.html](ATP6V1G2-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1G2/ATP6V1G2-notes.md](ATP6V1G2-notes.md)
- GOA TSV: present - [genes/human/ATP6V1G2/ATP6V1G2-goa.tsv](ATP6V1G2-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1G2/ATP6V1G2-uniprot.txt](ATP6V1G2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1G2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1G2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1G2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1G2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1G2 encodes the brain/neuron-enriched isoform of the vacuolar H+-ATPase (V-ATPase) V1 "G" subunit. Together with the E subunit it forms the EG peripheral (stator) stalks of the peripheral V1 sector, which physically couple the catalytic A3B3 head to the membrane-integral V0 sector and resist the torque generated during rotary catalysis. As part of the assembled V-ATPase holoenzyme, ATP6V1G2 contributes to ATP-hydrolysis-driven proton translocation across membranes, acidifying intracellular compartments including synaptic vesicles, endosomes, lysosomes, clathrin-coated vesicles, and melanosomes. The G subunit itself is largely a helical/extended protein with a disordered central region and is a peripheral membrane component of the complex; it does not hydrolyze ATP on its own. ATP6V1G2 is one of three human G-subunit paralogs (with ubiquitous ATP6V1G1 and kidney-enriched ATP6V1G3) and is expressed predominantly in brain, where it is associated with synaptic-vesicle acidification.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 15; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** CONFLICT on compartment. Review/notes establish G2 as the brain/neuron-enriched G-subunit isoform whose core process is **synaptic vesicle lumen acidification** (GO:0097401, ACCEPT IBA+IEA) at the synaptic vesicle membrane (GO:0030672, GO:0098850, ACCEPT); also non-core melanosome (EXP PMID:17081065). The review asserts NO lysosomal role and MARKs_AS_OVER_ANNOTATED the macroautophagy NAS. PN places G2 under "lysosomal v-ATPase" and projects lysosomal lumen acidification — mismatched to the established synaptic-vesicle biology. PN Notes template ("pumps protons into the lysosome") mis-frames this neuronal isoform.
- **PN story / NEW pressure:** PN's lysosomal lumen acidification (new_to_goa) OVER-REACHES for G2; the evidenced acidification target is the synaptic vesicle lumen, already captured by GO:0097401 (more specific and correct). GO:0046612/GO:0007042 verified real but wrong specialization. **Lysosomal projection should NOT be propagated; the review already has the correct compartment-specific acidification term.**
- **Evidence alignment:** No overlap. PN cites generic V-ATPase/mTORC1 reviews; review cites G2-specific PMID:10202016 (MHC locus/identity, in notes), PMID:12384298 (brain tissue-specificity), PMID:17081065 (melanosome EXP), plus over-annotated interactome PMIDs. Review better-targeted.
- **Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this brain/synaptic-vesicle isoform; correct acidification term (GO:0097401) already present. **Recommended edits:** [MAP] exempt ATP6V1G2 from lysosomal-acidification/lysosomal-V1 projection; route to synaptic-vesicle acidification + vacuolar V1 complex terms already in the review.

## Full Consistency Review

- **UniProt:** O95670 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V1 lysosomal v-ATPase proton pump component" (Nutrient sensing; Lysosomal acidification). **PN-node mapping:** leaf→GO:0046612 lysosomal V1 domain (more_specific_than_existing_goa); leaf→GO:0033176 V-type ATPase complex (entailed_by_goa_closure); type→GO:0007042 lysosomal lumen acidification (new_to_goa).
- **Consistency:** CONFLICT on compartment. Review/notes establish G2 as the brain/neuron-enriched G-subunit isoform whose core process is **synaptic vesicle lumen acidification** (GO:0097401, ACCEPT IBA+IEA) at the synaptic vesicle membrane (GO:0030672, GO:0098850, ACCEPT); also non-core melanosome (EXP PMID:17081065). The review asserts NO lysosomal role and MARKs_AS_OVER_ANNOTATED the macroautophagy NAS. PN places G2 under "lysosomal v-ATPase" and projects lysosomal lumen acidification — mismatched to the established synaptic-vesicle biology. PN Notes template ("pumps protons into the lysosome") mis-frames this neuronal isoform.
- **PN story / NEW pressure:** PN's lysosomal lumen acidification (new_to_goa) OVER-REACHES for G2; the evidenced acidification target is the synaptic vesicle lumen, already captured by GO:0097401 (more specific and correct). GO:0046612/GO:0007042 verified real but wrong specialization. **Lysosomal projection should NOT be propagated; the review already has the correct compartment-specific acidification term.**
- **Mapping strategy:** Tissue-restricted neuronal isoform; lysosomal projection is over-broad (TOMM20/HSPA8/RAB7A precedent). **[MAP]** flag G2 as an exception — its acidification specialization is synaptic-vesicle (GO:0097401), not lysosomal; safe complex target is GO:0000221/GO:0016471 (already in review).
- **Evidence alignment:** No overlap. PN cites generic V-ATPase/mTORC1 reviews; review cites G2-specific PMID:10202016 (MHC locus/identity, in notes), PMID:12384298 (brain tissue-specificity), PMID:17081065 (melanosome EXP), plus over-annotated interactome PMIDs. Review better-targeted.
- **Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this brain/synaptic-vesicle isoform; correct acidification term (GO:0097401) already present. **Recommended edits:** [MAP] exempt ATP6V1G2 from lysosomal-acidification/lysosomal-V1 projection; route to synaptic-vesicle acidification + vacuolar V1 complex terms already in the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/ATP6V1G2/ATP6V1G2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: O95670
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
- UniProt: O95670
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
