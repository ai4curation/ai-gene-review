# TRAPPC5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8IUR0
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC5/TRAPPC5-ai-review.yaml](TRAPPC5-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC5/TRAPPC5-ai-review.html](TRAPPC5-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC5/TRAPPC5-notes.md](TRAPPC5-notes.md)
- GOA TSV: present - [genes/human/TRAPPC5/TRAPPC5-goa.tsv](TRAPPC5-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC5/TRAPPC5-uniprot.txt](TRAPPC5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRAPPC5 is the human Trs31 ortholog and a small TRAPP core subunit. It supports TRAPP complex architecture, complex-level RAB1 guanine-nucleotide exchange, and ER-to-Golgi vesicle-mediated transport. Autophagy-related effects are best understood through TRAPP/TRAPPII/TRAPPIII complex membership and ER-Golgi trafficking rather than an independent TRAPPC5-specific autophagy function.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 6; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Coherent. Notes, review, PN row ("TRAPP complex, core subunit"), and node mapping agree TRAPPC5 (Trs31 ortholog, small core subunit) acts via complex-level RAB1 GEF + ER-to-Golgi transport. Review carries GO:0030008 (IDA/IEA) and TRAPPII/TRAPPIII memberships. Notable, defensible deviation from raw GOA: the IBA GO:1990070 TRAPPI complex annotation is MARK_AS_OVER_ANNOTATED because mammalian TRAPP I existence is "in question" (PMID:21525244, PMID:27066478) — well argued, not a contradiction.
- **PN story / NEW pressure:** PN Notes mention ATG9/ATG2 trafficking. Review keeps autophagy as TRAPPIII-membership context only; TRAPPC5 has no gene-specific autophagy evidence. Defensible. Conclusion: already captured via complex membership; no NEW term.
- **Evidence alignment:** PN titles ("Membrane Trafficking in Autophagy"; PMID:27066478) both in review; review adds PMID:21525244 and Reactome. Generic protein-binding rows (PMID:25416956/28514442/31515488/32296183/33961781) over-annotated. No miscitation.
- **Verdict:** Consistent; ACCEPT mapping. Includes a sound TRAPPI-overannotation call beyond the PN scope.

## Full Consistency Review

- **UniProt:** Q8IUR0 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component` ; **PN-node mapping:** type-leaf mapped, scope=ok_for_propagation_to_go, GO:0030008 TRAPP complex (already_in_goa_exact)
- **Consistency:** Coherent. Notes, review, PN row ("TRAPP complex, core subunit"), and node mapping agree TRAPPC5 (Trs31 ortholog, small core subunit) acts via complex-level RAB1 GEF + ER-to-Golgi transport. Review carries GO:0030008 (IDA/IEA) and TRAPPII/TRAPPIII memberships. Notable, defensible deviation from raw GOA: the IBA GO:1990070 TRAPPI complex annotation is MARK_AS_OVER_ANNOTATED because mammalian TRAPP I existence is "in question" (PMID:21525244, PMID:27066478) — well argued, not a contradiction.
- **PN story / NEW pressure:** PN Notes mention ATG9/ATG2 trafficking. Review keeps autophagy as TRAPPIII-membership context only; TRAPPC5 has no gene-specific autophagy evidence. Defensible. Conclusion: already captured via complex membership; no NEW term.
- **Mapping strategy:** No change to node. Projected GO:0030008 (OLS-verified) already in GOA. One subtlety worth flagging: the review demotes TRAPPI (GO:1990070) as a mammalian artifact, but the PN node projects only the parent GO:0030008, so no conflict with the projection.
- **Evidence alignment:** PN titles ("Membrane Trafficking in Autophagy"; PMID:27066478) both in review; review adds PMID:21525244 and Reactome. Generic protein-binding rows (PMID:25416956/28514442/31515488/32296183/33961781) over-annotated. No miscitation.
- **Verdict:** Consistent; ACCEPT mapping. Includes a sound TRAPPI-overannotation call beyond the PN scope.
- **Recommended edits:** None required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC5/TRAPPC5-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: Q8IUR0
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
