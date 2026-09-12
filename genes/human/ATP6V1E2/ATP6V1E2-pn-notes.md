# ATP6V1E2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96A05
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1E2/ATP6V1E2-ai-review.yaml](ATP6V1E2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1E2/ATP6V1E2-ai-review.html](ATP6V1E2-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1E2/ATP6V1E2-notes.md](ATP6V1E2-notes.md)
- GOA TSV: present - [genes/human/ATP6V1E2/ATP6V1E2-goa.tsv](ATP6V1E2-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1E2/ATP6V1E2-uniprot.txt](ATP6V1E2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1E2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1E2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1E2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1E2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1E2 encodes the testis/sperm-enriched isoform of subunit E of the peripheral V1 sector of the vacuolar-type H(+)-ATPase (V-ATPase), a rotary proton pump. The V-ATPase comprises a cytoplasmic V1 complex that hydrolyzes ATP and a membrane-integral V0 complex that translocates protons across the membrane. Within V1, subunit E pairs with subunit G to form the EG heterodimers that constitute the three peripheral (stator) stalks. These stalks hold the (AB)3 catalytic head stationary against the torque generated when the central D/F rotor turns, coupling ATP hydrolysis in V1 to proton translocation through V0. ATP6V1E2 is the tissue-restricted paralog of the ubiquitously expressed ATP6V1E1; it is enriched in testis and sperm, where a V-ATPase containing this subunit is plausibly associated with the acrosome (a lysosome-related organelle). Its core molecular role is as a structural V1 peripheral-stalk component that enables ATP hydrolysis-driven, rotary proton transport, contributing to acidification of intracellular compartments.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 13; MARK_AS_OVER_ANNOTATED: 8

## PN Consistency Summary

- **Consistency:** CONFLICT on compartment. Review/notes establish E2 as the testis/sperm-enriched subunit-E paralog forming EG peripheral stalks; its plausible specialized compartment is the **acrosome** (acrosomal vesicle, GO:0001669, KEEP_AS_NON_CORE, orthology IEA) — a lysosome-related organelle, not the lysosome. The review carries no lysosomal annotation and MARKs_AS_OVER_ANNOTATED the macroautophagy NAS and five bare protein-binding IPIs. PN places E2 under "lysosomal v-ATPase" and projects lysosomal lumen acidification — mismatched to the sperm/acrosome biology. PN Notes template ("pumps protons into the lysosome") mis-frames this isoform.
- **PN story / NEW pressure:** PN's lysosomal lumen acidification (new_to_goa) OVER-REACHES for E2. GO:0046612/GO:0007042 verified real but wrong specialization; the evidenced organelle is acrosome (lysosome-related, not lysosome). E2 lacks direct human localization evidence at all (acrosome is IEA-only). **Lysosomal projection should NOT be propagated; if anything, an acrosome/lysosome-related-organelle framing is the honest one, but evidence is orthology-only.**
- **Evidence alignment:** No overlap. PN cites generic reviews; review cites E2-specific PMID:12036578 (testis-specific isoform) plus high-throughput interactome PMIDs (all over-annotated). Review better-targeted to the gene.
- **Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this testis/acrosome isoform (and acrosome itself is IEA-only). **Recommended edits:** [MAP] exempt ATP6V1E2 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar/catalytic V1 complex terms; keep acrosome as non-core.

## Full Consistency Review

- **UniProt:** Q96A05 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V1 lysosomal v-ATPase proton pump component" (Nutrient sensing; Lysosomal acidification). **PN-node mapping:** leaf→GO:0046612 lysosomal V1 domain (more_specific_than_existing_goa); leaf→GO:0033176 V-type ATPase complex (new_to_goa); type→GO:0007042 lysosomal lumen acidification (new_to_goa).
- **Consistency:** CONFLICT on compartment. Review/notes establish E2 as the testis/sperm-enriched subunit-E paralog forming EG peripheral stalks; its plausible specialized compartment is the **acrosome** (acrosomal vesicle, GO:0001669, KEEP_AS_NON_CORE, orthology IEA) — a lysosome-related organelle, not the lysosome. The review carries no lysosomal annotation and MARKs_AS_OVER_ANNOTATED the macroautophagy NAS and five bare protein-binding IPIs. PN places E2 under "lysosomal v-ATPase" and projects lysosomal lumen acidification — mismatched to the sperm/acrosome biology. PN Notes template ("pumps protons into the lysosome") mis-frames this isoform.
- **PN story / NEW pressure:** PN's lysosomal lumen acidification (new_to_goa) OVER-REACHES for E2. GO:0046612/GO:0007042 verified real but wrong specialization; the evidenced organelle is acrosome (lysosome-related, not lysosome). E2 lacks direct human localization evidence at all (acrosome is IEA-only). **Lysosomal projection should NOT be propagated; if anything, an acrosome/lysosome-related-organelle framing is the honest one, but evidence is orthology-only.**
- **Mapping strategy:** Like B1/G3, E2 is a tissue-restricted isoform whose specialized compartment is not the lysosome (TOMM20/HSPA8/RAB7A "too broad" precedent applies). **[MAP]** flag E2 as an exception to lysosomal projection; safe target is the generic catalytic/V1 complex term (GO:0033178, already in review). Acrosome remains non-core/IEA.
- **Evidence alignment:** No overlap. PN cites generic reviews; review cites E2-specific PMID:12036578 (testis-specific isoform) plus high-throughput interactome PMIDs (all over-annotated). Review better-targeted to the gene.
- **Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this testis/acrosome isoform (and acrosome itself is IEA-only). **Recommended edits:** [MAP] exempt ATP6V1E2 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar/catalytic V1 complex terms; keep acrosome as non-core.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/ATP6V1E2/ATP6V1E2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: Q96A05
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
- UniProt: Q96A05
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
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
