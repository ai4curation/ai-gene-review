# ATP6V1H PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UI12
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V1H/ATP6V1H-ai-review.yaml](ATP6V1H-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V1H/ATP6V1H-ai-review.html](ATP6V1H-ai-review.html)
- Gene notes: present - [genes/human/ATP6V1H/ATP6V1H-notes.md](ATP6V1H-notes.md)
- GOA TSV: present - [genes/human/ATP6V1H/ATP6V1H-goa.tsv](ATP6V1H-goa.tsv)
- UniProt record: present - [genes/human/ATP6V1H/ATP6V1H-uniprot.txt](ATP6V1H-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1H.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V1H.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1H.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V1H.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ATP6V1H encodes V-type proton ATPase subunit H (483 amino acids, ~57 kDa), the regulatory subunit H of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase). Subunit H is present as a single copy in the V1 complex and has a dual regulatory role: in the assembled V-ATPase holoenzyme it supports proton pump activity, while in the free cytosolic V1 complex (dissociated from V0 during regulated disassembly) it inhibits futile ATP hydrolysis. Beyond its structural role in the V-ATPase, subunit H directly binds to AP2M1 (the medium chain mu2 of adaptor protein complex 2) through armadillo repeat domains spanning residues 133-363, physically connecting the V-ATPase to the clathrin-mediated endocytic machinery. The protein was originally identified as Nef-binding protein 1 (NBP1) and is the human ortholog of yeast Vma13p. HIV-1 and SIV Nef exploit the subunit H-AP2M1 interaction to forcibly internalize CD4 from infected cell surfaces, but this reflects co-option of a normal cellular endocytic function. Two isoforms exist (Q9UI12-1 and Q9UI12-2); isoform 2 differs at residues 176-193. The protein localizes to lysosomal and endosomal membranes (as part of assembled V-ATPase), to the cytosol (as part of free V1 complex), and at clathrin-coated vesicle membranes. ATP6V1H is ubiquitously expressed.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 29; MARK_AS_OVER_ANNOTATED: 9; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Consistent on the core V-ATPase regulatory-subunit role. PN treats H purely as a "V1 proton-pump component"; the review adds a well-supported SECOND function (AP2M1/AP-2 binding → clathrin-mediated endocytosis, GO:0006897 / GO:0035615 clathrin-cargo adaptor; PMID:12032142) that the PN node does not represent. Not a contradiction, but the PN row under-describes H.
- **PN story / NEW pressure:** Projected terms VERIFIED real. GO:0046612 (lysosomal V1) is a lysosome-specific sibling of the review's vacuolar GO:0000221 — already captured at function level. GO:0007042 lysosomal lumen acidification IS already in the review (IBA + 2× NAS, ACCEPT) → "already_in_goa_exact," correctly. GO:0033176 already present (ACCEPT/entailed). No NEW pressure from the PN node; if anything the gene's endocytic-adaptor function is the under-captured story, and that is project-orthogonal (not part of the ALP V-ATPase row).
- **Evidence alignment:** As with G1, PN cites review-article titles (mTORC1/V-ATPase/neurodegeneration) absent from the review's PMID set; review is anchored on PMID:9442887 (Forgac review), PMID:33065002 (cryo-EM), PMID:12032142 (AP2M1). Same V-ATPase biology; the endocytic-adaptor literature is unique to the review.
- **Verdict:** Consistent, already captured (all three projected terms present or covered by siblings). No edits needed for the PN row; note that H's AP-2/endocytosis function lies outside the PN node and is fully handled in the review.

## Full Consistency Review

- **UniProt:** Q9UI12 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (very thorough; dual-function review, 60+ annotations)
- **PN placement:** `Autophagy-Lysosome Pathway` two rows — `…|mTORC1 pathway, upstream|Nutrient sensing|V1 lysosomal v-ATPase proton pump component` and `…|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 …component` ; **PN-node mapping:** subtype→GO:0046612 (lysosomal V1 domain, mapped/ok); subtype→GO:0033176 (V-ATPase complex, mapped/ok); type→GO:0007042 (lysosomal lumen acidification, mapped/ok); class→GO:0010506 context_only/too_broad.
- **Consistency:** Consistent on the core V-ATPase regulatory-subunit role. PN treats H purely as a "V1 proton-pump component"; the review adds a well-supported SECOND function (AP2M1/AP-2 binding → clathrin-mediated endocytosis, GO:0006897 / GO:0035615 clathrin-cargo adaptor; PMID:12032142) that the PN node does not represent. Not a contradiction, but the PN row under-describes H.
- **PN story / NEW pressure:** Projected terms VERIFIED real. GO:0046612 (lysosomal V1) is a lysosome-specific sibling of the review's vacuolar GO:0000221 — already captured at function level. GO:0007042 lysosomal lumen acidification IS already in the review (IBA + 2× NAS, ACCEPT) → "already_in_goa_exact," correctly. GO:0033176 already present (ACCEPT/entailed). No NEW pressure from the PN node; if anything the gene's endocytic-adaptor function is the under-captured story, and that is project-orthogonal (not part of the ALP V-ATPase row).
- **Mapping strategy:** No change to node mapping warranted from this gene. Projected CC terms are at/below review specificity; no broader-than-review over-reach.
- **Evidence alignment:** As with G1, PN cites review-article titles (mTORC1/V-ATPase/neurodegeneration) absent from the review's PMID set; review is anchored on PMID:9442887 (Forgac review), PMID:33065002 (cryo-EM), PMID:12032142 (AP2M1). Same V-ATPase biology; the endocytic-adaptor literature is unique to the review.
- **Verdict:** Consistent, already captured (all three projected terms present or covered by siblings). No edits needed for the PN row; note that H's AP-2/endocytosis function lies outside the PN node and is fully handled in the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/ATP6V1H/ATP6V1H-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V1 lysosomal v-ATPase proton pump component
- UniProt: Q9UI12
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
- UniProt: Q9UI12
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
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033176 proton-transporting V-type ATPase complex | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V1 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
