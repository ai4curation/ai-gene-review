# TRAPPC3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O43617
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC3/TRAPPC3-ai-review.yaml](TRAPPC3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC3/TRAPPC3-ai-review.html](TRAPPC3-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC3/TRAPPC3-notes.md](TRAPPC3-notes.md)
- GOA TSV: present - [genes/human/TRAPPC3/TRAPPC3-goa.tsv](TRAPPC3-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC3/TRAPPC3-uniprot.txt](TRAPPC3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRAPPC3 is the human Bet3 homolog and a core TRAPP-complex subunit. It contributes to complex-level RAB1 guanine-nucleotide exchange factor activity, TRAPP/TRAPPII/TRAPPIII complex architecture, and ER-to-Golgi vesicle-mediated transport. Autophagophore-recruitment effects are best understood through TRAPP complex membership and TRAPPIII/RAB1 context rather than independent TRAPPC3-specific autophagy activity.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 13; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Coherent. Notes, review, PN row ("TRAPP complex, core subunit"), and node mapping all agree TRAPPC3/Bet3 is a core TRAPP subunit contributing complex-level RAB1 GEF activity and ER-to-Golgi transport. Review carries GO:0030008 (IDA, IBA, IEA) plus contributes_to GO:0005085, consistent with PN. No contradictions; 13 generic protein-binding rows uniformly MARK_AS_OVER_ANNOTATED.
- **PN story / NEW pressure:** PN Notes mention ATG9/ATG2 trafficking. Review keeps autophagy as TRAPPIII-membership context only (no autophagy BP), citing PMID:27066478 "connection ... not clear." Defensible — no gene-specific autophagy evidence for the core subunit. Conclusion: already captured via complex membership.
- **Evidence alignment:** Strong overlap. PN titles ("Membrane Trafficking in Autophagy"; PMID:27066478) both present in review. Review adds substantial primary literature beyond the PN row (PMID:16828797 Bet3-Tpc6B structure, PMID:21525244, PMID:18930054, Reactome). No divergence/miscitation.
- **Verdict:** Consistent; ACCEPT mapping. Cleanest gene-level representation of the PN TRAPP-component leaf; review is more richly evidenced than the PN row.

## Full Consistency Review

- **UniProt:** O43617 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component` ; **PN-node mapping:** type-leaf mapped, scope=ok_for_propagation_to_go, GO:0030008 TRAPP complex (already_in_goa_exact)
- **Consistency:** Coherent. Notes, review, PN row ("TRAPP complex, core subunit"), and node mapping all agree TRAPPC3/Bet3 is a core TRAPP subunit contributing complex-level RAB1 GEF activity and ER-to-Golgi transport. Review carries GO:0030008 (IDA, IBA, IEA) plus contributes_to GO:0005085, consistent with PN. No contradictions; 13 generic protein-binding rows uniformly MARK_AS_OVER_ANNOTATED.
- **PN story / NEW pressure:** PN Notes mention ATG9/ATG2 trafficking. Review keeps autophagy as TRAPPIII-membership context only (no autophagy BP), citing PMID:27066478 "connection ... not clear." Defensible — no gene-specific autophagy evidence for the core subunit. Conclusion: already captured via complex membership.
- **Mapping strategy:** No change. GO:0030008 (OLS-verified) is already in GOA exactly; the projected term matches review. Scope correct.
- **Evidence alignment:** Strong overlap. PN titles ("Membrane Trafficking in Autophagy"; PMID:27066478) both present in review. Review adds substantial primary literature beyond the PN row (PMID:16828797 Bet3-Tpc6B structure, PMID:21525244, PMID:18930054, Reactome). No divergence/miscitation.
- **Verdict:** Consistent; ACCEPT mapping. Cleanest gene-level representation of the PN TRAPP-component leaf; review is more richly evidenced than the PN row.
- **Recommended edits:** None required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC3/TRAPPC3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: O43617
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
