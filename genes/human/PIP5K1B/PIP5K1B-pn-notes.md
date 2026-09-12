# PIP5K1B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O14986
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/PIP5K1B/PIP5K1B-ai-review.yaml](PIP5K1B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/PIP5K1B/PIP5K1B-ai-review.html](PIP5K1B-ai-review.html)
- Gene notes: present - [genes/human/PIP5K1B/PIP5K1B-notes.md](PIP5K1B-notes.md)
- GOA TSV: present - [genes/human/PIP5K1B/PIP5K1B-goa.tsv](PIP5K1B-goa.tsv)
- UniProt record: present - [genes/human/PIP5K1B/PIP5K1B-uniprot.txt](PIP5K1B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/PIP5K1B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/PIP5K1B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PIP5K1B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PIP5K1B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: PIP5K1B encodes phosphatidylinositol 4-phosphate 5-kinase type 1 beta, a membrane-associated lipid kinase whose core function is ATP-dependent phosphorylation of PI4P to generate PI(4,5)P2/PIP2. PI(4,5)P2 supports membrane signaling, actin remodeling, adhesion, vesicle trafficking, and autophagic lysosome reformation. Broader WNT/PI3K pathway signaling and uropod localization are secondary contexts relative to the PI4P 5-kinase/PIP2 biosynthetic role.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 13; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 4; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent. Notes, review, and PN agree the core MF is PI4P 5-kinase (GO:0016308 → PI(4,5)P2), and that the PN/ALR role rests on Rong et al. (PMID:22885770), not on the PN row alone. Review correctly treats PN node as too broad to be evidence.
- **PN story / NEW pressure:** PN asserts an ALR/autolysosome-membrane role absent from prior GO. Review adds GO:0007040 lysosome organization (action NEW, IMP, PMID:22885770) as the best available broad term, and proposes a genuinely novel "autophagic lysosome reformation" child term. OLS search confirms no existing GO term for autophagic lysosome reformation — so the proposed_new_term is warranted (candidate). Verdict: ADD broad GO:0007040 (done) + propose ALR term (done).
- **Evidence alignment:** Minimal PN overlap. PN cites one review ("Membrane Trafficking in Autophagy"); review anchors on primary PMID:22885770 (Rong et al.) plus PMID:8955136 (PIP5KIbeta identity) and Reactome. The url: ref to nature.com/ncb2557 duplicates PMID:22885770.
- **Verdict:** Consistent; PN ALR story correctly drives a NEW broad lysosome-organization annotation and a justified proposed ALR term (no existing GO equivalent). No edits required. Minor: url:nature.com/ncb2557 reference duplicates PMID:22885770.

## Full Consistency Review

- **UniProt:** O14986 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagic lysosome reformation|Regulation of autolysosome membrane composition` ; **PN-node mapping:** `group` = no_mapping (broad container); `class` (Autophagic lysosome reformation) = context_only, too_broad_to_propagate → GO:0007040 lysosome organization; `branch` = no_mapping. No GO projected.
- **Consistency:** Consistent. Notes, review, and PN agree the core MF is PI4P 5-kinase (GO:0016308 → PI(4,5)P2), and that the PN/ALR role rests on Rong et al. (PMID:22885770), not on the PN row alone. Review correctly treats PN node as too broad to be evidence.
- **PN story / NEW pressure:** PN asserts an ALR/autolysosome-membrane role absent from prior GO. Review adds GO:0007040 lysosome organization (action NEW, IMP, PMID:22885770) as the best available broad term, and proposes a genuinely novel "autophagic lysosome reformation" child term. OLS search confirms no existing GO term for autophagic lysosome reformation — so the proposed_new_term is warranted (candidate). Verdict: ADD broad GO:0007040 (done) + propose ALR term (done).
- **Mapping strategy:** This gene does not change the node mapping; the node correctly stays context_only and projects nothing. The review's GO:0007040 matches the PN node's context-GO exactly (not broader/narrower) but is sourced from the primary ALR paper rather than node propagation — methodologically sound.
- **Evidence alignment:** Minimal PN overlap. PN cites one review ("Membrane Trafficking in Autophagy"); review anchors on primary PMID:22885770 (Rong et al.) plus PMID:8955136 (PIP5KIbeta identity) and Reactome. The url: ref to nature.com/ncb2557 duplicates PMID:22885770.
- **Verdict:** Consistent; PN ALR story correctly drives a NEW broad lysosome-organization annotation and a justified proposed ALR term (no existing GO equivalent). No edits required. Minor: url:nature.com/ncb2557 reference duplicates PMID:22885770.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/PIP5K1B/PIP5K1B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Regulation of autolysosome membrane composition
- UniProt: O14986
- In branches: ALP
- Notes: Phosphorylates PI(4)P to generate PI(4,5)P2, which is required for tubule formation from autolysosomes during ALR
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Regulation of autolysosome membrane composition
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
