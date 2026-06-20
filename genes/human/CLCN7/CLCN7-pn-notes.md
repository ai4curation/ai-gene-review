# CLCN7 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P51798
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CLCN7/CLCN7-ai-review.yaml](CLCN7-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CLCN7/CLCN7-ai-review.html](CLCN7-ai-review.html)
- Gene notes: present - [genes/human/CLCN7/CLCN7-notes.md](CLCN7-notes.md)
- GOA TSV: present - [genes/human/CLCN7/CLCN7-goa.tsv](CLCN7-goa.tsv)
- UniProt record: present - [genes/human/CLCN7/CLCN7-uniprot.txt](CLCN7-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CLCN7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CLCN7.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CLCN7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CLCN7.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CLCN7 encodes ClC-7, a member of the CLC family that functions as an electrogenic 2Cl(-)/1H(+) antiporter (exchanger) rather than a passive chloride channel. It resides in the membranes of late endosomes and lysosomes, and in osteoclasts it localizes to the ruffled border bounding the resorption lacuna. ClC-7 forms an obligate heteromeric complex with the accessory beta-subunit OSTM1, which is required for ClC-7 protein stability and transport activity. By coupling chloride flux to the outwardly directed proton gradient, ClC-7 provides the counter-ion movement that allows the V-ATPase to acidify the lysosomal lumen and the osteoclast resorption space, and it raises luminal chloride concentration. Loss-of-function variants cause osteopetrosis (recessive OPTB4 and dominant Albers-Schonberg OPTA2) together with lysosomal storage and neurodegeneration, whereas certain gain-of-function variants cause a distinct hypopigmentation, organomegaly and delayed-myelination syndrome.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 11; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Strongly consistent. Deep-research notes, review YAML, and PN row all describe ClC-7 as the 2Cl(-)/1H(+) lysosomal antiporter (not a passive channel) that supports V-ATPase acidification. The single PN reference (PMID:18449189, "primary chloride permeation pathway in lysosomes") is the central paper in both the notes and the YAML. No contradictions.
- **PN story / NEW pressure:** PN emphasizes ClC-7's contribution to lysosomal acidification (GO:0007042), which is absent from existing GOA. The review captures the molecular mechanism (GO:0062158 antiporter; GO:1902600 proton transport) but does NOT annotate the acidification process itself. GO:0007042 is a defensible, verified ADD — directly supported by PMID:18449189 (siRNA knockdown diminishes lysosomal acidification). Note the literature nuance (normal steady-state pH in Clcn7-/- mice; PMID:32851177) means an `involved_in` (contributory), not causal, framing is appropriate.
- **Evidence alignment:** Full overlap on PMID:18449189. Review additionally cites PMID:21527911 (stoichiometry), PMID:32851177 (cryo-EM/complex). No divergence.
- **Verdict:** Consistent; **ADD** GO:0007042 lysosomal lumen acidification (involved_in) to the review.

## Full Consistency Review

- **UniProt:** P51798 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|Miscellaneous function - lysosomal acidification` ; **PN-node mapping:** the leaf and most ancestors are `no_mapping`; the `[type]` node "Lysosomal acidification" is `mapped`, `ok_for_propagation_to_go`, GO:0007042 lysosomal lumen acidification (verified real; not in GOA → `new_to_goa`).
- **Consistency:** Strongly consistent. Deep-research notes, review YAML, and PN row all describe ClC-7 as the 2Cl(-)/1H(+) lysosomal antiporter (not a passive channel) that supports V-ATPase acidification. The single PN reference (PMID:18449189, "primary chloride permeation pathway in lysosomes") is the central paper in both the notes and the YAML. No contradictions.
- **PN story / NEW pressure:** PN emphasizes ClC-7's contribution to lysosomal acidification (GO:0007042), which is absent from existing GOA. The review captures the molecular mechanism (GO:0062158 antiporter; GO:1902600 proton transport) but does NOT annotate the acidification process itself. GO:0007042 is a defensible, verified ADD — directly supported by PMID:18449189 (siRNA knockdown diminishes lysosomal acidification). Note the literature nuance (normal steady-state pH in Clcn7-/- mice; PMID:32851177) means an `involved_in` (contributory), not causal, framing is appropriate.
- **Mapping strategy:** No change needed. The PN node maps at the correct (`type`) altitude with conservative parents left unmapped. GO:0007042 is neither broader than the review nor a TOMM20-style over-reach; it is a genuine process gap.
- **Evidence alignment:** Full overlap on PMID:18449189. Review additionally cites PMID:21527911 (stoichiometry), PMID:32851177 (cryo-EM/complex). No divergence.
- **Verdict:** Consistent; **ADD** GO:0007042 lysosomal lumen acidification (involved_in) to the review.

**Recommended edits:** [YAML] Add an `existing_annotations`/`proposed_new_terms` entry or `core_functions.directly_involved_in` for GO:0007042 lysosomal lumen acidification (involved_in, supported_by PMID:18449189), framed as contributory.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CLCN7/CLCN7-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Lysosomal catabolism | Regulation of lysosomal environment | Lysosomal acidification | Miscellaneous function - lysosomal acidification
- UniProt: P51798
- In branches: ALP
- Notes: CLCN7 is a antiporter that transports 2 chloride ions into the lysosome in exchange for pumping one proton out. It helps to maintain ion homoeostasis in the lysosome during acidification.
- PN references (titles):
    - The Cl-/H+ antiporter ClC-7 is the primary chloride permeation pathway in lysosomes | Nature
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|Miscellaneous function - lysosomal acidification
        status=no_mapping scope= GO=[]
        rationale: Reviewed as an unknown or residual PN category. The label does not provide a shared GO-mappable biological process, molecular function, or cellular component.
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

## Projected GO annotations (1)
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
