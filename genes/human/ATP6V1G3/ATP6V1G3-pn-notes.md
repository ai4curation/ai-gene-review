# ATP6V1G3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96LB4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1G3/ATP6V1G3-ai-review.yaml](ATP6V1G3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1G3/ATP6V1G3-ai-review.html](ATP6V1G3-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1G3/ATP6V1G3-notes.md](ATP6V1G3-notes.md)
- GOA TSV: present - [genes/human/ATP6V1G3/ATP6V1G3-goa.tsv](ATP6V1G3-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1G3/ATP6V1G3-uniprot.txt](ATP6V1G3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1G3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1G3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1G3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1G3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1G3 (V-type proton ATPase subunit G 3) is the kidney-enriched isoform of the "G" subunit of the peripheral (V1) domain of the vacuolar H+-ATPase (V-ATPase). The V-ATPase is a multisubunit rotary enzyme in which the cytosolic V1 complex hydrolyzes ATP and the membrane-integral V0 complex translocates protons, together acidifying intracellular compartments (endosomes, lysosomes, secretory vesicles) and, in specialized cells, the extracellular/luminal space. The G subunit is a component of the peripheral stalk (stator), forming an E-G heterodimer that connects the catalytic V1 head to the membrane-embedded V0 a-subunit; this stator stalk holds the catalytic AB heterohexamer stationary against the torque of the central rotor. Of the three human G paralogs (G1/G2/G3), G3 expression is restricted to and enriched in the kidney, with additional detection in inner-ear epithelium, and assembles into the tissue-specific proton pump (with a4, B1, C2, d2) that drives apical proton secretion by renal collecting-duct intercalated cells for systemic acid-base homeostasis. G3 directly binds the V0 a-subunit (a4/a1), providing a physical link between the V1 and V0 domains required for pump assembly and regulation.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 16

## PN Consistency Summary

- **Consistency:** CONFLICT on compartment. Review/notes establish G3 as the kidney-enriched (plus inner-ear) G isoform that assembles the tissue-specific pump (a4/B1/C2/d2) at the **apical plasma membrane** of collecting-duct intercalated cells for luminal acid secretion (IDA plasma membrane PMID:17360703; ATPase binding to a4/a1, IPI). The review explicitly KEEPs_AS_NON_CORE the IBA synaptic-vesicle/synaptic-vesicle-acidification annotations as generic family transfers irrelevant to G3, and asserts NO lysosomal role. PN places G3 under "lysosomal v-ATPase" and projects lysosomal lumen acidification — contradicting the plasma-membrane renal biology. PN Notes template ("pumps protons into the lysosome") mis-frames this isoform.
- **PN story / NEW pressure:** PN's lysosomal lumen acidification (new_to_goa) OVER-REACHES for G3; evidenced compartment is apical plasma membrane (GO:0005886, IDA, ACCEPT), function is renal luminal acid secretion. GO:0046612/GO:0007042 verified real but wrong specialization. **Lysosomal projection should NOT be propagated.**
- **Evidence alignment:** No overlap. PN cites generic reviews; review cites G3-specific PMID:17360703 (V1-V0 G-a linkage, kidney expression, plasma membrane) and PMID:12384298 (kidney-specific isoform). Review strongly better-evidenced.
- **Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this apical-plasma-membrane kidney isoform. **Recommended edits:** [MAP] exempt ATP6V1G3 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar V1 complex + plasma-membrane/renal acid-secretion terms already in the review.

## Full Consistency Review

- **UniProt:** Q96LB4 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V1 lysosomal v-ATPase proton pump component" (Nutrient sensing; Lysosomal acidification). **PN-node mapping:** leaf→GO:0046612 lysosomal V1 domain (more_specific_than_existing_goa); leaf→GO:0033176 V-type ATPase complex (entailed_by_goa_closure); type→GO:0007042 lysosomal lumen acidification (new_to_goa).
- **Consistency:** CONFLICT on compartment. Review/notes establish G3 as the kidney-enriched (plus inner-ear) G isoform that assembles the tissue-specific pump (a4/B1/C2/d2) at the **apical plasma membrane** of collecting-duct intercalated cells for luminal acid secretion (IDA plasma membrane PMID:17360703; ATPase binding to a4/a1, IPI). The review explicitly KEEPs_AS_NON_CORE the IBA synaptic-vesicle/synaptic-vesicle-acidification annotations as generic family transfers irrelevant to G3, and asserts NO lysosomal role. PN places G3 under "lysosomal v-ATPase" and projects lysosomal lumen acidification — contradicting the plasma-membrane renal biology. PN Notes template ("pumps protons into the lysosome") mis-frames this isoform.
- **PN story / NEW pressure:** PN's lysosomal lumen acidification (new_to_goa) OVER-REACHES for G3; evidenced compartment is apical plasma membrane (GO:0005886, IDA, ACCEPT), function is renal luminal acid secretion. GO:0046612/GO:0007042 verified real but wrong specialization. **Lysosomal projection should NOT be propagated.**
- **Mapping strategy:** Tissue-restricted plasma-membrane isoform; lysosomal projection over-broad (TOMM20/HSPA8/RAB7A precedent). **[MAP]** flag G3 as an exception — safe targets are vacuolar V1 domain/complex (GO:0000221/GO:0016471) + plasma-membrane acid-secretion context already in the review; the specific G3-a-subunit ATPase-binding (GO:0051117) is the mechanistically informative core, not lysosomal acidification.
- **Evidence alignment:** No overlap. PN cites generic reviews; review cites G3-specific PMID:17360703 (V1-V0 G-a linkage, kidney expression, plasma membrane) and PMID:12384298 (kidney-specific isoform). Review strongly better-evidenced.
- **Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this apical-plasma-membrane kidney isoform. **Recommended edits:** [MAP] exempt ATP6V1G3 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar V1 complex + plasma-membrane/renal acid-secretion terms already in the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/ATP6V1G3/ATP6V1G3-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: Q96LB4
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
- UniProt: Q96LB4
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
