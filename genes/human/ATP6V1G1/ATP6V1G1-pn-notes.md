# ATP6V1G1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75348
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1G1/ATP6V1G1-ai-review.yaml](ATP6V1G1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1G1/ATP6V1G1-ai-review.html](ATP6V1G1-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1G1/ATP6V1G1-notes.md](ATP6V1G1-notes.md)
- GOA TSV: present - [genes/human/ATP6V1G1/ATP6V1G1-goa.tsv](ATP6V1G1-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1G1/ATP6V1G1-uniprot.txt](ATP6V1G1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1G1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1G1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1G1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1G1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1G1 encodes V-type proton ATPase subunit G 1 (118 amino acids, 13.8 kDa), a peripheral stalk component of the V1 catalytic domain of the vacuolar-type H+-ATPase (V-ATPase). The V-ATPase is a large multi-subunit complex that couples ATP hydrolysis to proton translocation across membranes, thereby acidifying lysosomes, endosomes, and other intracellular compartments. The V1 domain (peripheral, cytosolic) contains subunits A-H and is responsible for ATP hydrolysis; it couples to the membrane-embedded V0 domain through three peripheral EG heterodimeric stalks that act as the stator. Subunit G 1 forms these EG heterodimers with subunit E (ATP6V1E1 or ATP6V1E2), directly contacts the V0 subunit a, and is essential for maintaining V1-V0 connectivity. ATP6V1G1 is ubiquitously expressed; humans also have two paralogous G subunits (G2, G3) with more restricted expression. The protein is present at lysosomal and endosomal membranes as part of the assembled holoenzyme, at the apical plasma membrane in kidney tubular epithelial cells (thick ascending limb and distal convoluted tubule), and in the cytosol as part of the free, disassembled V1 complex. V-ATPase-mediated acidification of endosomes is required for efficient iron release from transferrin; consistent with this, genetic disruption of ATP6V1G1 causes intracellular iron depletion, impaired prolyl hydroxylase (PHD) activity, and consequent HIF1alpha stabilization.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 20; MARK_AS_OVER_ANNOTATED: 10

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep-research notes, review YAML, and PN annotation all describe G1 as a V1 peripheral-stalk (EG-heterodimer) subunit acidifying lysosomes/endosomes. PN's mTORC1/Ragulator framing matches the review's Reactome mTORC1 context annotations. No contradictions.
- **PN story / NEW pressure:** All three projected terms are VERIFIED real (OLS). GO:0033176 already in GOA/review (ACCEPT). GO:0046612 "lysosomal V1 domain" is a lysosome-specific refinement of the review's GO:0000221 *vacuolar* V1 / GO:0033180 generic V1 (siblings, not strictly subsumed) — defensible but a lateral re-specification, not a missing function. GO:0007042 lysosomal lumen acidification is NOT in this gene's review/GOA (it IS in the ATP6V1H review) → defensible ADD as a downstream BP of the assembled pump. Conclude: GO:0007042 = ADD candidate; GO:0046612 = already captured at function level (vacuolar/generic V1).
- **Evidence alignment:** Divergent reference sets — PN cites review-article titles (mTORC1/V-ATPase/neurodegeneration reviews) not present as PMIDs in the review; review is anchored on primary structural/functional papers (PMID:33065002 cryo-EM, PMID:17360703 G/a interaction, PMID:28296633 iron/HIF). Same biology, different (complementary) citations; no conflict.
- **Verdict:** Consistent. ADD GO:0007042 (lysosomal lumen acidification) to bring G1 in line with its paralog ATP6V1H; GO:0046612 already covered by existing V1-domain terms.

## Full Consistency Review

- **UniProt:** O75348 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (thorough; notes + 40+ annotations reviewed)
- **PN placement:** `Autophagy-Lysosome Pathway` two rows — `…|mTORC1 pathway, upstream|Nutrient sensing|V1 lysosomal v-ATPase proton pump component` and `…|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 …component` ; **PN-node mapping:** subtype→GO:0046612 (lysosomal V1 domain, mapped/ok); subtype→GO:0033176 (V-ATPase complex, mapped/ok); type→GO:0007042 (lysosomal lumen acidification, mapped/ok); class→GO:0010506 context_only/too_broad.
- **Consistency:** Strong agreement. Deep-research notes, review YAML, and PN annotation all describe G1 as a V1 peripheral-stalk (EG-heterodimer) subunit acidifying lysosomes/endosomes. PN's mTORC1/Ragulator framing matches the review's Reactome mTORC1 context annotations. No contradictions.
- **PN story / NEW pressure:** All three projected terms are VERIFIED real (OLS). GO:0033176 already in GOA/review (ACCEPT). GO:0046612 "lysosomal V1 domain" is a lysosome-specific refinement of the review's GO:0000221 *vacuolar* V1 / GO:0033180 generic V1 (siblings, not strictly subsumed) — defensible but a lateral re-specification, not a missing function. GO:0007042 lysosomal lumen acidification is NOT in this gene's review/GOA (it IS in the ATP6V1H review) → defensible ADD as a downstream BP of the assembled pump. Conclude: GO:0007042 = ADD candidate; GO:0046612 = already captured at function level (vacuolar/generic V1).
- **Mapping strategy:** Node mapping is appropriate; subtype is correctly leaf-restricted to V1. The lysosomal-specific CC terms are narrower than the review's vacuolar terms, so no broader-than-review over-reach (contrast TOMM20/HSPA8 precedent). Scope/status correct.
- **Evidence alignment:** Divergent reference sets — PN cites review-article titles (mTORC1/V-ATPase/neurodegeneration reviews) not present as PMIDs in the review; review is anchored on primary structural/functional papers (PMID:33065002 cryo-EM, PMID:17360703 G/a interaction, PMID:28296633 iron/HIF). Same biology, different (complementary) citations; no conflict.
- **Verdict:** Consistent. ADD GO:0007042 (lysosomal lumen acidification) to bring G1 in line with its paralog ATP6V1H; GO:0046612 already covered by existing V1-domain terms.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1G1/ATP6V1G1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: O75348
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
- UniProt: O75348
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
