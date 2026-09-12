# CDK5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q00535
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CDK5/CDK5-ai-review.yaml](CDK5-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CDK5/CDK5-ai-review.html](CDK5-ai-review.html)
- Gene notes: present - [genes/human/CDK5/CDK5-notes.md](CDK5-notes.md)
- GOA TSV: present - [genes/human/CDK5/CDK5-goa.tsv](CDK5-goa.tsv)
- UniProt record: present - [genes/human/CDK5/CDK5-uniprot.txt](CDK5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CDK5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CDK5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDK5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDK5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CDK5 encodes a proline-directed serine/threonine kinase activated by CDK5R1/p35, CDK5R1/p25, and CDK5R2/p39 family regulators, with major functions in neuronal development, neurite and axon growth, cytoskeletal and dendritic-spine dynamics, synaptic vesicle cycling, synaptic plasticity, and p25-linked neurodegenerative apoptosis as a stress/disease context. Human CDK5 also regulates induced neuronal autophagy through phosphorylation of SH3GLB1/endophilin B1.
- Existing/core annotation action counts: ACCEPT: 76; KEEP_AS_NON_CORE: 30; MARK_AS_OVER_ANNOTATED: 38; MODIFY: 5

## PN Consistency Summary

- **Consistency:** Consistent and well-handled. PN places CDK5 in the residual "function unknown" autophagy-maturation bucket on the strength of the *Drosophila* Cdk5-Acinus basal-autophagy work (same eLife paper underpinning ACIN1's PN row). The review does not import that as a human fact; instead it anchors a human autophagy role on CDK5→SH3GLB1/endophilin B1 phosphorylation (GO:0016241 regulation of macroautophagy, ACCEPT, PMID:21499257). The notes (line 2860) explicitly state the Drosophila Cdk5-Acinus evidence was treated as context-only. No contradiction.
- **PN story / NEW pressure:** Already captured / PN over-reaches on the Acinus angle. PN's "unknown" autophagy-maturation placement is genuinely unknown for human CDK5; the review correctly mints no maturation term and routes the conserved-Acinus hypothesis into a suggested_question + suggested_experiment (does human CDK5 phosphorylate ACIN1 at the S437-equivalent?). The defensible human autophagy term GO:0016241 is already present. No ADD warranted.
- **Evidence alignment:** Deliberately divergent. PN cites only the Drosophila eLife Cdk5-Acinus-S437 paper; the review's autophagy support is the human/neuron PMID:21499257 (endophilin B1), which PN does not cite. The divergence is the finding: PN's evidence is orthology-based, the review uses human evidence and quarantines the fly paper as a hypothesis.
- **Verdict:** Fully consistent; exemplary handling of an orthology-driven "unknown" placement (parallels ACIN1). No edits needed.

## Full Consistency Review

- **UniProt:** Q00535 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 1 row, ALP — `Autophagosome closure maturation and lysosome fusion → "Specific function in autophagosome maturation and lysosome fusion unknown"`. **PN-node mapping:** leaf group=no_mapping ("unknown/residual"); class=context_only→GO:0016236; branch=no_mapping. **No GO propagates.** PN Notes: Drosophila Cdk5 phosphorylates ACN (acinus) at S437, stabilizing it and promoting basal autophagy.
- **Consistency:** Consistent and well-handled. PN places CDK5 in the residual "function unknown" autophagy-maturation bucket on the strength of the *Drosophila* Cdk5-Acinus basal-autophagy work (same eLife paper underpinning ACIN1's PN row). The review does not import that as a human fact; instead it anchors a human autophagy role on CDK5→SH3GLB1/endophilin B1 phosphorylation (GO:0016241 regulation of macroautophagy, ACCEPT, PMID:21499257). The notes (line 2860) explicitly state the Drosophila Cdk5-Acinus evidence was treated as context-only. No contradiction.
- **PN story / NEW pressure:** Already captured / PN over-reaches on the Acinus angle. PN's "unknown" autophagy-maturation placement is genuinely unknown for human CDK5; the review correctly mints no maturation term and routes the conserved-Acinus hypothesis into a suggested_question + suggested_experiment (does human CDK5 phosphorylate ACIN1 at the S437-equivalent?). The defensible human autophagy term GO:0016241 is already present. No ADD warranted.
- **Mapping strategy:** No change. The leaf's no_mapping is the correct conservative call — the node label literally says "function unknown," so propagating GO:0016236 macroautophagy would be TRAPP-like over-propagation. CDK5's inclusion does not justify upgrading the node; its real human autophagy role (SH3GLB1) is already individually annotated and is regulation, not maturation.
- **Evidence alignment:** Deliberately divergent. PN cites only the Drosophila eLife Cdk5-Acinus-S437 paper; the review's autophagy support is the human/neuron PMID:21499257 (endophilin B1), which PN does not cite. The divergence is the finding: PN's evidence is orthology-based, the review uses human evidence and quarantines the fly paper as a hypothesis.
- **Verdict:** Fully consistent; exemplary handling of an orthology-driven "unknown" placement (parallels ACIN1). No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CDK5/CDK5-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Specific function in autophagosome maturation and lysosome fusion unknown
- UniProt: Q00535
- In branches: ALP
- Notes: Ser/Thr kinase. In Drosophila, phosphorylates ACN thereby stabilizing it and promoting basal autophagy
- PN references (titles):
    - Stress-induced Cdk5 activity enhances cytoprotective basal autophagy in Drosophila melanogaster by phosphorylating acinus at serine437 | eLife (elifesciences.org)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Specific function in autophagosome maturation and lysosome fusion unknown
        status=no_mapping scope= GO=[]
        rationale: Reviewed as an unknown or residual PN category. The label does not provide a shared GO-mappable biological process, molecular function, or cellular component.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
