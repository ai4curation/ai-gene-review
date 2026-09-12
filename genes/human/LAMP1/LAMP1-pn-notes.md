# LAMP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P11279
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/LAMP1/LAMP1-ai-review.yaml](LAMP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/LAMP1/LAMP1-ai-review.html](LAMP1-ai-review.html)
- Gene notes: present - [genes/human/LAMP1/LAMP1-notes.md](LAMP1-notes.md)
- GOA TSV: present - [genes/human/LAMP1/LAMP1-goa.tsv](LAMP1-goa.tsv)
- UniProt record: present - [genes/human/LAMP1/LAMP1-uniprot.txt](LAMP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/LAMP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/LAMP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LAMP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LAMP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: LAMP1 encodes lysosome-associated membrane glycoprotein 1, an abundant heavily glycosylated single-pass membrane protein of lysosomes, late endosomes, and lysosome-related secretory granules. Its most informative current molecular function is direct inhibition of the lysosomal TMEM175 cation/proton channel, supporting lysosomal lumen acidification and hydrolase activity. LAMP1 also participates in lysosome-related immune granule contexts, TAPL/ABCB9 stabilization, Lassa virus receptor activity, and plasma membrane exposure during degranulation, but its core biology is centered on lysosomal and late-endosomal membrane function.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 35; MARK_AS_OVER_ANNOTATED: 7; MODIFY: 25; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Consistent. PN note ("LAMP1 recruits clathrin to tubules during ALR") is acknowledged in LAMP1-notes.md, which states the cached Rong et al. ALR abstract (PMID:22885770) supports clathrin/PI(4,5)P2 as ALR components but gives no LAMP1-specific statement. Review therefore does not add an ALR annotation and treats GO:0000421/GO:0044754 (autophagosome/autolysosome) as MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE. No contradiction.
- **PN story / NEW pressure:** PN asserts a LAMP1 ALR-morphology role absent from GO, but the node projects nothing and the review correctly judges the evidence insufficient. The review's own NEW pressure is elsewhere: a proposed_new_term "lysosomal proton channel inhibitor activity" (parent GO:0008200) for the TMEM175 mechanism (PMID:37390818). I verified via OLS that no such GO term exists, so this is a defensible new-term candidate, not already captured; the existing GO:0008200 ion channel inhibitor activity is the best current term and is ACCEPTed. Conclusion: ALR over-reaches; TMEM175-inhibitor new term is justified (candidate).
- **Evidence alignment:** PN cites one ALR review ("Membrane Trafficking in Autophagy"); review's load-bearing evidence is independent (PMID:37390818 TMEM175, PMID:23632890 NK granules, PMID:22641697 TAPL). Divergence is expected: PN row is search context, not the core LAMP1 function.
- **Verdict:** Consistent; PN ALR story correctly not propagated. TMEM175 proton-channel-inhibitor proposed new term is a real GO gap. No edits required.

## Full Consistency Review

- **UniProt:** P11279 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagic lysosome reformation|Regulation of autolysosome morphology` ; **PN-node mapping:** group `no_mapping`; parent class `context_only / too_broad_to_propagate / GO:0007040 lysosome organization`; branch `no_mapping`. No projected GO terms.
- **Consistency:** Consistent. PN note ("LAMP1 recruits clathrin to tubules during ALR") is acknowledged in LAMP1-notes.md, which states the cached Rong et al. ALR abstract (PMID:22885770) supports clathrin/PI(4,5)P2 as ALR components but gives no LAMP1-specific statement. Review therefore does not add an ALR annotation and treats GO:0000421/GO:0044754 (autophagosome/autolysosome) as MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE. No contradiction.
- **PN story / NEW pressure:** PN asserts a LAMP1 ALR-morphology role absent from GO, but the node projects nothing and the review correctly judges the evidence insufficient. The review's own NEW pressure is elsewhere: a proposed_new_term "lysosomal proton channel inhibitor activity" (parent GO:0008200) for the TMEM175 mechanism (PMID:37390818). I verified via OLS that no such GO term exists, so this is a defensible new-term candidate, not already captured; the existing GO:0008200 ion channel inhibitor activity is the best current term and is ACCEPTed. Conclusion: ALR over-reaches; TMEM175-inhibitor new term is justified (candidate).
- **Mapping strategy:** No change. `no_mapping` for the ALR-morphology container is correct (descendants mix components/regulators); the `context_only` lysosome-organization framing at the class level is right. LAMP1 does not justify upgrading the node to propagation.
- **Evidence alignment:** PN cites one ALR review ("Membrane Trafficking in Autophagy"); review's load-bearing evidence is independent (PMID:37390818 TMEM175, PMID:23632890 NK granules, PMID:22641697 TAPL). Divergence is expected: PN row is search context, not the core LAMP1 function.
- **Verdict:** Consistent; PN ALR story correctly not propagated. TMEM175 proton-channel-inhibitor proposed new term is a real GO gap. No edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/LAMP1/LAMP1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Regulation of autolysosome morphology
- UniProt: P11279
- In branches: ALP
- Notes: Recruits clathrin to tubules during ALR
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Regulation of autolysosome morphology
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
