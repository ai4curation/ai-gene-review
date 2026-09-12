# ATP6V0D2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N8Y2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1385)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP6V0D2/ATP6V0D2-ai-review.yaml](ATP6V0D2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP6V0D2/ATP6V0D2-ai-review.html](ATP6V0D2-ai-review.html)
- Gene notes: present - [genes/human/ATP6V0D2/ATP6V0D2-notes.md](ATP6V0D2-notes.md)
- GOA TSV: present - [genes/human/ATP6V0D2/ATP6V0D2-goa.tsv](ATP6V0D2-goa.tsv)
- UniProt record: present - [genes/human/ATP6V0D2/ATP6V0D2-uniprot.txt](ATP6V0D2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0D2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP6V0D2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0D2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP6V0D2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATP6V0D2/ATP6V0D2-deep-research-falcon.md](ATP6V0D2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATP6V0D2 encodes the d2 isoform of the V0 d subunit of the vacuolar H+-ATPase (V-ATPase). The V-ATPase is a multisubunit enzyme consisting of a peripheral V1 domain that hydrolyzes ATP and a membrane-integral V0 domain responsible for proton translocation. The d subunit is part of the V0 domain and plays a central role in coupling ATP hydrolysis to proton transport by directly interacting with the D and F subunits of the V1 central stalk. ATP6V0D2 shows tissue-restricted expression, predominantly in kidney intercalated cells and osteoclasts, where V-ATPases function at the plasma membrane for urinary acidification and bone resorption, respectively. In clear-cell renal carcinoma models, ATP6V0D2 has also been reported to promote late autophagy by increasing lysosomal acidification and by facilitating autophagosome-lysosome fusion through RAB7/HOPS/SNARE machinery, suggesting a context-dependent role in lysosomal degradative flux in addition to its established V-ATPase subunit function.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 11; NEW: 2; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Deep research (falcon), review, and PN agree: ATP6V0D2 is the d2 isoform of the V0 d subunit (PMID:18752060), tissue-restricted (kidney intercalated cells, osteoclasts; PMID:15800125), with newer ccRCC evidence for late-autophagy lysosomal acidification + RAB7/HOPS fusion (PMID:39477683). Review adds GO:0007042 (NEW, NAS) and GO:0046610 (NEW, IC) — matching both PN projections. No contradictions.
- **PN story / NEW pressure:** PN asserts lysosomal acidification + lysosomal V0-domain componency. For d2 these are genuinely new specificity beyond existing GO:0007035/GO:0033179, and PMID:39477683 gives gene-specific lysosomal-acidification support. Both terms verified real. The review flags appropriate caution (suggested_questions: should GO:0046610 propagate or await direct d2 lysosomal-complex evidence). **ADD GO:0007042 + GO:0046610 — implemented, with honest IC/uncertainty framing.**
- **Evidence alignment:** PN cites generic V-ATPase/mTORC1 review titles; review adds the gene-specific PMID:18752060, PMID:15800125, PMID:39477683 absent from the PN reference list — a divergence where the review is better-sourced. No conflict.
- **Verdict:** CONSISTENT — both NEW terms (verified real) appropriately added as conservative narrowings; PN projections align with review. No edits required.

## Full Consistency Review

- **UniProt:** Q8N8Y2 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two ALP leaves "V0 lysosomal v-ATPase proton pump component". **PN-node mapping:** leaf→GO:0046610 (more_specific_than_existing_goa); leaf→GO:0033179 (already_in_goa_exact); type→GO:0007042 lysosomal lumen acidification (more_specific_than_existing_goa).
- **Consistency:** Deep research (falcon), review, and PN agree: ATP6V0D2 is the d2 isoform of the V0 d subunit (PMID:18752060), tissue-restricted (kidney intercalated cells, osteoclasts; PMID:15800125), with newer ccRCC evidence for late-autophagy lysosomal acidification + RAB7/HOPS fusion (PMID:39477683). Review adds GO:0007042 (NEW, NAS) and GO:0046610 (NEW, IC) — matching both PN projections. No contradictions.
- **PN story / NEW pressure:** PN asserts lysosomal acidification + lysosomal V0-domain componency. For d2 these are genuinely new specificity beyond existing GO:0007035/GO:0033179, and PMID:39477683 gives gene-specific lysosomal-acidification support. Both terms verified real. The review flags appropriate caution (suggested_questions: should GO:0046610 propagate or await direct d2 lysosomal-complex evidence). **ADD GO:0007042 + GO:0046610 — implemented, with honest IC/uncertainty framing.**
- **Mapping strategy:** Gene supports the leaf (true V0 d2 subunit). GO:0046610 narrows existing annotations; GO:0007042 narrows GO:0007035 vacuolar acidification — both defensible narrowings, not over-broad. Note d2's strongest isoform-specific biology is *plasma-membrane* proton secretion (kidney/osteoclast), so lysosomal projection is real-but-context-dependent; review correctly keeps it as a conservative addition, not the sole core.
- **Evidence alignment:** PN cites generic V-ATPase/mTORC1 review titles; review adds the gene-specific PMID:18752060, PMID:15800125, PMID:39477683 absent from the PN reference list — a divergence where the review is better-sourced. No conflict.
- **Verdict:** CONSISTENT — both NEW terms (verified real) appropriately added as conservative narrowings; PN projections align with review. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP6V0D2/ATP6V0D2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Nutrient sensing | V0 lysosomal v-ATPase proton pump component
- UniProt: Q8N8Y2
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
- UniProt: Q8N8Y2
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
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
- GO:0033179 proton-transporting V-type ATPase, V0 domain | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|V0 lysosomal v-ATPase proton pump component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
