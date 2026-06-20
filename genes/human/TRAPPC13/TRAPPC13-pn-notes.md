# TRAPPC13 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: A5PLN9
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC13/TRAPPC13-ai-review.yaml](TRAPPC13-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC13/TRAPPC13-ai-review.html](TRAPPC13-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC13/TRAPPC13-notes.md](TRAPPC13-notes.md)
- GOA TSV: present - [genes/human/TRAPPC13/TRAPPC13-goa.tsv](TRAPPC13-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC13/TRAPPC13-uniprot.txt](TRAPPC13-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC13.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC13.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRAPPC13/C5orf44 is a Trs65-related large TRAPP subunit curated in human TRAPPII and TRAPPIII complex contexts. Its main role is contribution to TRAPP complex RAB1/Rab GEF trafficking and ER-to-Golgi vesicle-mediated transport, rather than independent GEF activity, COPII coat assembly, generic protein binding, or a direct TRAPPC13-specific autophagy function.
- Existing/core annotation action counts: ACCEPT: 5; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Coherent. Notes, review YAML, PN annotation, and node mapping all agree TRAPPC13 (Trs65 homolog) is a large TRAPP subunit acting via complex-level RAB1 GEF/ER-to-Golgi trafficking, not an independent autophagy effector. PN row labels it "TRAPP III, specific subunit"; review carries both TRAPPII (GO:1990071) and TRAPPIII (GO:1990072) memberships with an explicit caveat about source-dependent partition — a documented nuance, not a contradiction. No PMIDs misattributed.
- **PN story / NEW pressure:** PN Notes assert ATG9/ATG2 trafficking + TRAPP-III autophagy role. Review correctly resists converting this into a TRAPPC13-specific autophagy BP: the cited TRAPP review states the mammalian TRAPP-III/autophagy link "is currently not clear" (PMID:27066478). No defensible gene-specific NEW autophagy term; the PN autophagy context is already captured by TRAPPIII membership (GO:1990072, whose OLS definition itself notes it "regulates autophagy"). Conclusion: already captured.
- **Evidence alignment:** PN titles = "Membrane Trafficking in Autophagy", the TRAPP review (PMID:27066478, in review), and "TRAPPC13 modulates autophagy and the response to Golgi stress" (a TRAPPC13-specific JCS paper NOT cited in the review). Otherwise overlapping.
- **Verdict:** Consistent; ACCEPT mapping. Minor gap: a TRAPPC13-specific autophagy/Golgi-stress paper in the PN row is absent from review references.

## Full Consistency Review

- **UniProt:** A5PLN9 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component` ; **PN-node mapping:** type-leaf mapped, scope=ok_for_propagation_to_go, GO:0030008 TRAPP complex (entailed_by_goa_closure)
- **Consistency:** Coherent. Notes, review YAML, PN annotation, and node mapping all agree TRAPPC13 (Trs65 homolog) is a large TRAPP subunit acting via complex-level RAB1 GEF/ER-to-Golgi trafficking, not an independent autophagy effector. PN row labels it "TRAPP III, specific subunit"; review carries both TRAPPII (GO:1990071) and TRAPPIII (GO:1990072) memberships with an explicit caveat about source-dependent partition — a documented nuance, not a contradiction. No PMIDs misattributed.
- **PN story / NEW pressure:** PN Notes assert ATG9/ATG2 trafficking + TRAPP-III autophagy role. Review correctly resists converting this into a TRAPPC13-specific autophagy BP: the cited TRAPP review states the mammalian TRAPP-III/autophagy link "is currently not clear" (PMID:27066478). No defensible gene-specific NEW autophagy term; the PN autophagy context is already captured by TRAPPIII membership (GO:1990072, whose OLS definition itself notes it "regulates autophagy"). Conclusion: already captured.
- **Mapping strategy:** No change needed. Projected GO:0030008 (OLS-verified) is entailed by GOA closure (review carries the subclasses GO:1990071/1990072). Component-bucket scope is correct and not over-broad.
- **Evidence alignment:** PN titles = "Membrane Trafficking in Autophagy", the TRAPP review (PMID:27066478, in review), and "TRAPPC13 modulates autophagy and the response to Golgi stress" (a TRAPPC13-specific JCS paper NOT cited in the review). Otherwise overlapping.
- **Verdict:** Consistent; ACCEPT mapping. Minor gap: a TRAPPC13-specific autophagy/Golgi-stress paper in the PN row is absent from review references.
- **Recommended edits:** Consider adding the PN-listed "TRAPPC13 modulates autophagy and the response to Golgi stress" (J Cell Sci) to references and assess whether it strengthens (or still does not justify) a gene-specific autophagy annotation.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC13/TRAPPC13-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: A5PLN9
- In branches: ALP
- Notes: TRAPP III complex, specific subunit. The TRAPP complex serves as a GEF for RAB1. Involved in ATG9 and ATG2 trafficking
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Frontiers | TRAPP Complexes in Secretion and Autophagy | Cell and Developmental Biology (frontiersin.org)
    - TRAPPC13 modulates autophagy and the response to Golgi stress | Journal of Cell Science | The Company of Biologists
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
- GO:0030008 TRAPP complex | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
