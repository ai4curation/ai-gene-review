# SPG11 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96JI7
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SPG11/SPG11-ai-review.yaml](SPG11-ai-review.yaml)
- AIGR review HTML: present - [genes/human/SPG11/SPG11-ai-review.html](SPG11-ai-review.html)
- Gene notes: present - [genes/human/SPG11/SPG11-notes.md](SPG11-notes.md)
- GOA TSV: present - [genes/human/SPG11/SPG11-goa.tsv](SPG11-goa.tsv)
- UniProt record: present - [genes/human/SPG11/SPG11-uniprot.txt](SPG11-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SPG11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SPG11.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPG11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPG11.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: SPG11 encodes spatacsin, a large cytoplasmic/peripheral membrane-associated protein that functions with SPG15/spastizin and AP-5 in endolysosomal membrane remodeling. The strongest protein-homeostasis evidence supports a core role in autophagic lysosome reformation, lysosomal tubulation, lysosome membrane recycling, and ER-linked lysosome trafficking/organization. SPG11 also has supported neuronal axonal/synaptic transport contexts, but its principal described cellular role is endolysosomal membrane remodeling.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 18; MARK_AS_OVER_ANNOTATED: 5; MODIFY: 7; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Consistent. Notes, review YAML and PN all center on ALR/lysosomal membrane remodeling. Review correctly treats the PN row as search context (its own notes say "this row is search context unless backed by primary literature"). No contradictions; neuronal axonal/synaptic rows kept as non-core, matching the deep-research framing.
- **PN story / NEW pressure:** PN's "ALR" story IS captured in GOA-equivalent terms the review accepts/adds: GO:0007040 lysosome organization, GO:0097212 lysosomal membrane organization, GO:0097753 membrane bending (all verified real, used as core). The review additionally proposes two genuinely new terms — "autophagic lysosome reformation" (parent GO:0007040) and "lysosome membrane recycling" (parent GO:0097212) — as `proposed_new_terms`, which is the right altitude since no exact ALR GO term exists. Conclude: **already captured at the available altitude; ADD only as proposed_new_terms (not mintable now).**
- **Evidence alignment:** Strong overlap. PN cites the JCI ALR paper = review's PMID:25365221 (ACCEPT, core). Review adds extensive endolysosomal evidence (PMID:40175557 structure, 29949766, 37871017, 23825025) PN does not list — divergence is enrichment, not conflict.
- **Verdict:** Fully consistent, well-curated. No edits needed.

## Full Consistency Review

- **UniProt:** Q96JI7 (spatacsin) · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway → Autophagic lysosome reformation → "Specific function in autophagic lysosome reformation unknown"` (1 row, ALP) ; **PN-node mapping:** group=`no_mapping` (function explicitly "unknown"); class (ALR)=`context_only`/`too_broad_to_propagate`→GO:0007040 lysosome organization; branch=`no_mapping`. **No GO propagates to SPG11 from PN.**
- **Consistency:** Consistent. Notes, review YAML and PN all center on ALR/lysosomal membrane remodeling. Review correctly treats the PN row as search context (its own notes say "this row is search context unless backed by primary literature"). No contradictions; neuronal axonal/synaptic rows kept as non-core, matching the deep-research framing.
- **PN story / NEW pressure:** PN's "ALR" story IS captured in GOA-equivalent terms the review accepts/adds: GO:0007040 lysosome organization, GO:0097212 lysosomal membrane organization, GO:0097753 membrane bending (all verified real, used as core). The review additionally proposes two genuinely new terms — "autophagic lysosome reformation" (parent GO:0007040) and "lysosome membrane recycling" (parent GO:0097212) — as `proposed_new_terms`, which is the right altitude since no exact ALR GO term exists. Conclude: **already captured at the available altitude; ADD only as proposed_new_terms (not mintable now).**
- **Mapping strategy:** This gene does not change the node. The PN class-level GO:0007040 exactly matches the review's chosen core term, so node status (`no_mapping` leaf, `context_only` class) is appropriate; no broader/narrower conflict.
- **Evidence alignment:** Strong overlap. PN cites the JCI ALR paper = review's PMID:25365221 (ACCEPT, core). Review adds extensive endolysosomal evidence (PMID:40175557 structure, 29949766, 37871017, 23825025) PN does not list — divergence is enrichment, not conflict.
- **Verdict:** Fully consistent, well-curated. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/SPG11/SPG11-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Specific function in autophagic lysosome reformation unknown
- UniProt: Q96JI7
- In branches: ALP
- Notes: Important for autophagic-lysosome reformation
- PN references (titles):
    - JCI - Spastic paraplegia proteins spastizin and spatacsin mediate autophagic lysosome reformation
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Specific function in autophagic lysosome reformation unknown
        status=no_mapping scope= GO=[]
        rationale: This PN group explicitly states that the specific role within autophagic lysosome reformation is unknown. That makes GO propagation unsafe until a narrower mechanistic interpretation is available.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
