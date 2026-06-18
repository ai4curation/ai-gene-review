# CDK5R1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q15078
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CDK5R1/CDK5R1-ai-review.yaml](CDK5R1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CDK5R1/CDK5R1-ai-review.html](CDK5R1-ai-review.html)
- Gene notes: present - [genes/human/CDK5R1/CDK5R1-notes.md](CDK5R1-notes.md)
- GOA TSV: present - [genes/human/CDK5R1/CDK5R1-goa.tsv](CDK5R1-goa.tsv)
- UniProt record: present - [genes/human/CDK5R1/CDK5R1-uniprot.txt](CDK5R1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CDK5R1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CDK5R1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDK5R1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDK5R1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CDK5R1 encodes the neuronal CDK5 activator p35 and its calpain-cleaved p25 fragment. Its core function is to bind and activate CDK5 as a regulatory subunit of the protein kinase 5 complex, thereby supporting neuronal development, neurite and axon growth, cortical lamination, dendritic-spine and cytoskeletal regulation, and p25-linked neurodegenerative stress signaling. p35 is myristoylated and membrane/neuronal process-associated, while p25 is more stable and relocalizes CDK5 activity to cytoplasmic, nuclear, and perinuclear compartments. CDK5R1 may contribute to induced autophagy indirectly through CDK5 activation, although direct human autophagy evidence is centered on CDK5 phosphorylation of SH3GLB1/endophilin B1 rather than CDK5R1-specific assays.
- Existing/core annotation action counts: ACCEPT: 61; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 19; MODIFY: 8

## PN Consistency Summary

- **Consistency:** Consistent. Same "unknown" residual bucket and same Drosophila eLife paper as CDK5, justified only by CDK5R1's role as the CDK5 activator. The review keeps the lone autophagy row (GO:0016241 regulation of macroautophagy, NAS, PMID:21499257) as KEEP_AS_NON_CORE, with the explicit reasoning that the human paper assayed CDK5→SH3GLB1, not a CDK5R1 perturbation — so CDK5R1's autophagy involvement is *inferred* via complex membership, not directly tested. This honest "complex-level context" framing matches PN's no_mapping/unknown placement exactly. No contradiction.
- **PN story / NEW pressure:** Already captured; PN over-reaches no further than CDK5. The defensible-but-indirect GO:0016241 is present (held non-core). No human evidence supports a CDK5R1-specific autophagosome-maturation term, so no ADD. The conserved Acinus hypothesis is routed to a suggested_question/experiment (CDK5R1-specific depletion/rescue in induced-autophagy assays).
- **Evidence alignment:** Divergent in the same way as CDK5. PN cites the Drosophila Cdk5-Acinus-S437 eLife paper; the review's autophagy row rests on human PMID:21499257 (SH3GLB1), which PN does not cite, plus its own notes flagging the inference gap. Convergent on neither autophagy paper directly, but the review is the more cautious.
- **Verdict:** Fully consistent; correctly more conservative than CDK5 (KEEP_AS_NON_CORE vs ACCEPT) given the inference is one step removed. No edits needed.

## Full Consistency Review

- **UniProt:** Q15078 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 1 row, ALP — `Autophagosome closure maturation and lysosome fusion → "Specific function in autophagosome maturation and lysosome fusion unknown"`. **PN-node mapping:** leaf group=no_mapping; class=context_only→GO:0016236; branch=no_mapping. **No GO propagates.** PN Notes: activator of CDK5 required for phosphorylation of ACN (acinus).
- **Consistency:** Consistent. Same "unknown" residual bucket and same Drosophila eLife paper as CDK5, justified only by CDK5R1's role as the CDK5 activator. The review keeps the lone autophagy row (GO:0016241 regulation of macroautophagy, NAS, PMID:21499257) as KEEP_AS_NON_CORE, with the explicit reasoning that the human paper assayed CDK5→SH3GLB1, not a CDK5R1 perturbation — so CDK5R1's autophagy involvement is *inferred* via complex membership, not directly tested. This honest "complex-level context" framing matches PN's no_mapping/unknown placement exactly. No contradiction.
- **PN story / NEW pressure:** Already captured; PN over-reaches no further than CDK5. The defensible-but-indirect GO:0016241 is present (held non-core). No human evidence supports a CDK5R1-specific autophagosome-maturation term, so no ADD. The conserved Acinus hypothesis is routed to a suggested_question/experiment (CDK5R1-specific depletion/rescue in induced-autophagy assays).
- **Mapping strategy:** No change. no_mapping is correct — CDK5R1 is a regulatory subunit whose only autophagy link is via CDK5; propagating GO:0016236 would be doubly indirect. CDK5R1's inclusion in the node adds no new GO-mappable shared function.
- **Evidence alignment:** Divergent in the same way as CDK5. PN cites the Drosophila Cdk5-Acinus-S437 eLife paper; the review's autophagy row rests on human PMID:21499257 (SH3GLB1), which PN does not cite, plus its own notes flagging the inference gap. Convergent on neither autophagy paper directly, but the review is the more cautious.
- **Verdict:** Fully consistent; correctly more conservative than CDK5 (KEEP_AS_NON_CORE vs ACCEPT) given the inference is one step removed. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CDK5R1/CDK5R1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Specific function in autophagosome maturation and lysosome fusion unknown
- UniProt: Q15078
- In branches: ALP
- Notes: Activator of CDK5 required for phosphorylation of ACN
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
