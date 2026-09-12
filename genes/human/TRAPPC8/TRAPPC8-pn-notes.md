# TRAPPC8 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y2L5
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC8/TRAPPC8-ai-review.yaml](TRAPPC8-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC8/TRAPPC8-ai-review.html](TRAPPC8-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC8/TRAPPC8-notes.md](TRAPPC8-notes.md)
- GOA TSV: present - [genes/human/TRAPPC8/TRAPPC8-goa.tsv](TRAPPC8-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC8/TRAPPC8-uniprot.txt](TRAPPC8-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC8.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC8.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRAPPC8 is the mammalian Trs85 ortholog and a TRAPPIII-associated TRAPP subunit. It contributes to TRAPPIII/RAB1 trafficking, ER-to-Golgi transport, ATG9 cycling required for autophagy initiation, and collagen-cargo secretion through TMEM131/TRAPP III context. Autophagophore recruitment is directly supported for TRAPPC8 by mammalian TBC1D14/TRAPPIII/ATG9 evidence.
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 3; NEW: 1

## PN Consistency Summary

- **Consistency:** Coherent and the strongest autophagy case. Notes, review, PN row ("TRAPP III, specific subunit"), and node mapping agree TRAPPC8 (Trs85 ortholog) is the TRAPPIII-specific subunit driving ATG9 cycling for autophagy initiation. Review adds GO:0006914 autophagy as **action: NEW** (IMP, PMID:26711178), modifies collagen biosynthetic process (GO:0032964) and COPII coat assembly to ER-to-Golgi transport, keeps Golgi organization non-core. No contradictions.
- **PN story / NEW pressure:** PN asserts ATG9/ATG2 trafficking + TRAPPIII autophagy — and unlike the core subunits this is directly supported for TRAPPC8 (PMID:26711178 "maintaining the cycling pool of ATG9 required for initiation of autophagy"; "first to clearly characterise a role for mammalian TRAPP, in particular TRAPPC8, in bulk macroautophagy"). The review's NEW GO:0006914 autophagy is fully defensible. Conclusion: ADD (already proposed as NEW in the review).
- **Evidence alignment:** Best overlap of the set: PN row uniquely lists PMID:26711178 (TBC1D14/TRAPP/ATG9), which the review uses as the load-bearing NEW-autophagy citation. Plus PMID:21525244, PMID:32095531 (TMEM131/collagen), PMID:27066478. No miscitation.
- **Verdict:** Consistent; ACCEPT mapping + endorse NEW autophagy (GO:0006914). Strongest PN-story-to-evidence match in the TRAPP set.

## Full Consistency Review

- **UniProt:** Q9Y2L5 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component` ; **PN-node mapping:** type-leaf mapped, scope=ok_for_propagation_to_go, GO:0030008 TRAPP complex (already_in_goa_exact)
- **Consistency:** Coherent and the strongest autophagy case. Notes, review, PN row ("TRAPP III, specific subunit"), and node mapping agree TRAPPC8 (Trs85 ortholog) is the TRAPPIII-specific subunit driving ATG9 cycling for autophagy initiation. Review adds GO:0006914 autophagy as **action: NEW** (IMP, PMID:26711178), modifies collagen biosynthetic process (GO:0032964) and COPII coat assembly to ER-to-Golgi transport, keeps Golgi organization non-core. No contradictions.
- **PN story / NEW pressure:** PN asserts ATG9/ATG2 trafficking + TRAPPIII autophagy — and unlike the core subunits this is directly supported for TRAPPC8 (PMID:26711178 "maintaining the cycling pool of ATG9 required for initiation of autophagy"; "first to clearly characterise a role for mammalian TRAPP, in particular TRAPPC8, in bulk macroautophagy"). The review's NEW GO:0006914 autophagy is fully defensible. Conclusion: ADD (already proposed as NEW in the review).
- **Mapping strategy:** No change to node. Projected GO:0030008 (OLS-verified) already in GOA; review also carries TRAPPIII (GO:1990072, whose OLS definition notes autophagy regulation). The PN component-bucket scope is narrower than the gene's NEW autophagy annotation — correctly leaving autophagy at the gene level rather than projecting it from the bucket.
- **Evidence alignment:** Best overlap of the set: PN row uniquely lists PMID:26711178 (TBC1D14/TRAPP/ATG9), which the review uses as the load-bearing NEW-autophagy citation. Plus PMID:21525244, PMID:32095531 (TMEM131/collagen), PMID:27066478. No miscitation.
- **Verdict:** Consistent; ACCEPT mapping + endorse NEW autophagy (GO:0006914). Strongest PN-story-to-evidence match in the TRAPP set.
- **Recommended edits:** Optionally make the NEW term more specific to the autophagophore-recruitment leaf (e.g. GO:0000045 autophagosome assembly, OLS-verified) if ATG9-cycling/initiation evidence is judged to support assembly rather than only broad autophagy; otherwise GO:0006914 stands.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC8/TRAPPC8-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: Q9Y2L5
- In branches: ALP
- Notes: TRAPP III complex, specific subunit. The TRAPP complex serves as a GEF for RAB1. Involved in ATG9 and ATG2 trafficking
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Frontiers | TRAPP Complexes in Secretion and Autophagy | Cell and Developmental Biology (frontiersin.org)
    - TBC1D14 regulates autophagy via the TRAPP complex and ATG9 traffic | The EMBO Journal (embopress.org)
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
