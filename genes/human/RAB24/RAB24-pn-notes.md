# RAB24 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q969Q5
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RAB24/RAB24-ai-review.yaml](RAB24-ai-review.yaml)
- AIGR review HTML: present - [genes/human/RAB24/RAB24-ai-review.html](RAB24-ai-review.html)
- Gene notes: present - [genes/human/RAB24/RAB24-notes.md](RAB24-notes.md)
- GOA TSV: present - [genes/human/RAB24/RAB24-goa.tsv](RAB24-goa.tsv)
- UniProt record: present - [genes/human/RAB24/RAB24-uniprot.txt](RAB24-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RAB24.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RAB24.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RAB24.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RAB24.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RAB24 encodes an atypical Rab-family small GTPase that is predominantly GTP-bound and has low intrinsic GTPase activity. Its best-supported protein-homeostasis role is at late basal autophagy: RAB24 targets to autophagic vacuoles/autophagosome membranes and is required for maturation and/or clearance of late autophagic compartments under nutrient-rich basal conditions, without being required for short starvation-induced autophagosome formation. Broader cytosolic, membrane, endocytic, and mouse-oocyte/spindle annotations are secondary contexts rather than the core RAB24 function.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 8; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Consistent. Notes, review, and PN agree RAB24 is an atypical, predominantly GTP-bound Rab acting in late/basal autophagic-compartment maturation/clearance (PMID:26325487), not in starvation-induced formation. PN explicitly flags the leaf as "function unknown" and no-mapping; review used it as context only. No contradictions.
- **PN story / NEW pressure:** None. PN makes no positive functional assertion (residual "unknown" node, no projected GO). Review independently MODIFYs generic GO:0006914 autophagy → GO:0097352 autophagosome maturation based on primary evidence — finer than anything PN asserts. Verdict: already captured / PN adds no pressure.
- **Evidence alignment:** Minimal overlap. PN cites one review ("Membrane Trafficking in Autophagy"); review uses primary PMID:26325487, 10660536 (atypical Rab biochem), 16034420 (rabenosyn-5). Several generic protein-binding IPI rows (interactome papers) marked over-annotated; HTP mitochondrion and Reactome secretory-granule rows marked over-annotated — reasonable.
- **Verdict:** Consistent; PN "unknown/no-mapping" placement is honest and the review supplies the specific autophagosome-maturation call. No NEW pressure, mapping correct. No edits required.

## Full Consistency Review

- **UniProt:** Q969Q5 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Specific function in autophagosome maturation and lysosome fusion unknown` ; **PN-node mapping:** `group` = no_mapping (unknown/residual category, no GO-mappable shared function); `class` = context_only, too_broad_to_propagate → GO:0016236 macroautophagy; `branch` = no_mapping. No GO projected.
- **Consistency:** Consistent. Notes, review, and PN agree RAB24 is an atypical, predominantly GTP-bound Rab acting in late/basal autophagic-compartment maturation/clearance (PMID:26325487), not in starvation-induced formation. PN explicitly flags the leaf as "function unknown" and no-mapping; review used it as context only. No contradictions.
- **PN story / NEW pressure:** None. PN makes no positive functional assertion (residual "unknown" node, no projected GO). Review independently MODIFYs generic GO:0006914 autophagy → GO:0097352 autophagosome maturation based on primary evidence — finer than anything PN asserts. Verdict: already captured / PN adds no pressure.
- **Mapping strategy:** This gene does not change the node. no_mapping is appropriate for a residual "unknown" category; the review's GO:0097352 is far narrower than the class-level context GO:0016236 and is correctly derived from the paper, not from node propagation. Good restraint — projecting macroautophagy here would over-annotate (TRAPP precedent).
- **Evidence alignment:** Minimal overlap. PN cites one review ("Membrane Trafficking in Autophagy"); review uses primary PMID:26325487, 10660536 (atypical Rab biochem), 16034420 (rabenosyn-5). Several generic protein-binding IPI rows (interactome papers) marked over-annotated; HTP mitochondrion and Reactome secretory-granule rows marked over-annotated — reasonable.
- **Verdict:** Consistent; PN "unknown/no-mapping" placement is honest and the review supplies the specific autophagosome-maturation call. No NEW pressure, mapping correct. No edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/RAB24/RAB24-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Specific function in autophagosome maturation and lysosome fusion unknown
- UniProt: Q969Q5
- In branches: ALP
- Notes: Necessary for maturation and clearance of autophagic structures in basal autophagy.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
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
