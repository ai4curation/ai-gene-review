# TRAPPC4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y296
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC4/TRAPPC4-ai-review.yaml](TRAPPC4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC4/TRAPPC4-ai-review.html](TRAPPC4-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC4/TRAPPC4-notes.md](TRAPPC4-notes.md)
- GOA TSV: present - [genes/human/TRAPPC4/TRAPPC4-goa.tsv](TRAPPC4-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC4/TRAPPC4-uniprot.txt](TRAPPC4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRAPPC4/synbindin is a core TRAPP-complex subunit required for TRAPP assembly/stability, complex-level RAB1 guanine-nucleotide exchange, ER-to-Golgi trafficking, and autophagy. Human patient fibroblasts and yeast Trs23 models show both trafficking and autophagy defects when TRAPPC4/Trs23 levels are reduced.
- Existing/core annotation action counts: ACCEPT: 25; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 8; MODIFY: 4

## PN Consistency Summary

- **Consistency:** Coherent, with TRAPPC4 the strongest autophagy case among the core subunits. Notes, review, PN row ("TRAPP complex, core subunit"), and node mapping agree on core TRAPP membership + RAB1 GEF + ER-to-Golgi transport. Review additionally ACCEPTs GO:0006914 autophagy (IMP, PMID:31794024 patient fibroblasts + yeast Trs23). Neuronal synbindin annotations sensibly split KEEP_AS_NON_CORE (dendrite/synapse) vs MARK_AS_OVER_ANNOTATED (synaptic vesicle, active zone). No contradictions.
- **PN story / NEW pressure:** Unlike the other subunits, TRAPPC4 has gene-specific autophagy evidence (PMID:31794024 "basal autophagy defect and a delay in autophagic flux"), so the existing GO:0006914 autophagy already captures the PN autophagophore-recruitment story. The PN node deliberately does NOT project autophagy (component-bucket scope); the gene's own GOA already carries it. Conclusion: already captured; no NEW term needed.
- **Evidence alignment:** PN titles ("Membrane Trafficking in Autophagy"; PMID:27066478) both in review. Review adds the disease paper PMID:31794024 (load-bearing for autophagy + RAB1-GEF-essential claims) and the synbindin paper PMID:11018053 — beyond the PN row. No miscitation.
- **Verdict:** Consistent; ACCEPT mapping. Best-evidenced TRAPP subunit; autophagy correctly retained at gene level, not over-projected from the PN bucket.

## Full Consistency Review

- **UniProt:** Q9Y296 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component` ; **PN-node mapping:** type-leaf mapped, scope=ok_for_propagation_to_go, GO:0030008 TRAPP complex (already_in_goa_exact)
- **Consistency:** Coherent, with TRAPPC4 the strongest autophagy case among the core subunits. Notes, review, PN row ("TRAPP complex, core subunit"), and node mapping agree on core TRAPP membership + RAB1 GEF + ER-to-Golgi transport. Review additionally ACCEPTs GO:0006914 autophagy (IMP, PMID:31794024 patient fibroblasts + yeast Trs23). Neuronal synbindin annotations sensibly split KEEP_AS_NON_CORE (dendrite/synapse) vs MARK_AS_OVER_ANNOTATED (synaptic vesicle, active zone). No contradictions.
- **PN story / NEW pressure:** Unlike the other subunits, TRAPPC4 has gene-specific autophagy evidence (PMID:31794024 "basal autophagy defect and a delay in autophagic flux"), so the existing GO:0006914 autophagy already captures the PN autophagophore-recruitment story. The PN node deliberately does NOT project autophagy (component-bucket scope); the gene's own GOA already carries it. Conclusion: already captured; no NEW term needed.
- **Mapping strategy:** No change. Projected GO:0030008 (OLS-verified) is in GOA exactly. PN-node scope (component only) is appropriately narrower than the gene's autophagy annotation — correctly avoids over-projecting autophagy from the bucket.
- **Evidence alignment:** PN titles ("Membrane Trafficking in Autophagy"; PMID:27066478) both in review. Review adds the disease paper PMID:31794024 (load-bearing for autophagy + RAB1-GEF-essential claims) and the synbindin paper PMID:11018053 — beyond the PN row. No miscitation.
- **Verdict:** Consistent; ACCEPT mapping. Best-evidenced TRAPP subunit; autophagy correctly retained at gene level, not over-projected from the PN bucket.
- **Recommended edits:** None required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC4/TRAPPC4-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: Q9Y296
- In branches: ALP
- Notes: TRAPP complex, core subunit. The TRAPP complex serves as a GEF for RAB1. Involved in ATG9 and ATG2 trafficking
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Frontiers | TRAPP Complexes in Secretion and Autophagy | Cell and Developmental Biology (frontiersin.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030008 TRAPP complex]
        rationale: This PN leaf is a curated component bucket for TRAPP subunits used in autophagophore recruitment. The matching GO cellular-component term is TRAPP complex, and the member genes already converge strongly on that assignment in existing GOA.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0030008 TRAPP complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
