# RUBCN PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92622
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RUBCN/RUBCN-ai-review.yaml](RUBCN-ai-review.yaml)
- AIGR review HTML: present - [genes/human/RUBCN/RUBCN-ai-review.html](RUBCN-ai-review.html)
- Gene notes: present - [genes/human/RUBCN/RUBCN-notes.md](RUBCN-notes.md)
- GOA TSV: present - [genes/human/RUBCN/RUBCN-goa.tsv](RUBCN-goa.tsv)
- UniProt record: present - [genes/human/RUBCN/RUBCN-uniprot.txt](RUBCN-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RUBCN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RUBCN.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RUBCN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RUBCN.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RUBCN encodes Rubicon, a RUN/RH-domain regulator that associates with the UVRAG-containing class III PI3K complex II and Rab7 to inhibit PIK3C3/VPS34 activity, endosome maturation, and autophagosome maturation. RUBCN is a negative PI3KC3-C2/autophagosome maturation regulator rather than an autophagy activator. It localizes mainly to late endosome/lysosome and early endosome compartments and also has non-core pathogen/innate-immune interaction biology described in UniProt.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 12; MODIFY: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent, with one nuance. Review + notes correctly emphasize Rubicon as a NEGATIVE regulator of PI3KC3-C2/autophagosome maturation (inhibits VPS34; PMID:19270696, 21062745). PN Notes say only "Member of class III PI3K complex 2 that binds to UVRAG and inhibits activity" — captures the inhibitory role. The PN component-membership framing (treating Rubicon as a structural C2 subunit) is the contestable point: Rubicon binds only a subpopulation of UVRAG complexes and is often described as an associated regulator rather than a stoichiometric core subunit. Flag, not a contradiction.
- **PN story / NEW pressure:** PN asserts GO:0034272 membership that is absent from GOA (`new_to_goa`). Review adds GO:0034272 part_of as action NEW (PMID:28306502... actually RUBCN cites discovery/RUN-domain papers) — matching the PN projection. Term verified real. Review also proposes PI3K inhibitor / negative-regulation MF terms beyond PN. Verdict: ADD GO:0034272 (review already did) — aligned with PN.
- **Evidence alignment:** PN cites Annual Review, a cardiovascular-autophagy review, and PMID:19270696 (Matsunaga). Review uses primary PMID:19270696, 21062745 (RUN domain/PI3KC3 inhibition), 20974968, 20943950 (Rab7 RH-domain). PMID:19270696 shared.
- **Verdict:** Consistent; NEW GO:0034272 matches PN projection (verified, new_to_goa). Open question whether `part_of` vs "associated inhibitory regulator" is the right relation for a subpopulation binder — already flagged in the review's suggested_questions; no edits required.

## Full Consistency Review

- **UniProt:** Q92622 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component` ; **PN-node mapping:** `type` leaf mapped, `ok_for_propagation_to_go` → GO:0034272 (class III PI3K complex, type II), goa_status `new_to_goa`; ancestors GO:0035032 / GO:0016236 context_only.
- **Consistency:** Mostly consistent, with one nuance. Review + notes correctly emphasize Rubicon as a NEGATIVE regulator of PI3KC3-C2/autophagosome maturation (inhibits VPS34; PMID:19270696, 21062745). PN Notes say only "Member of class III PI3K complex 2 that binds to UVRAG and inhibits activity" — captures the inhibitory role. The PN component-membership framing (treating Rubicon as a structural C2 subunit) is the contestable point: Rubicon binds only a subpopulation of UVRAG complexes and is often described as an associated regulator rather than a stoichiometric core subunit. Flag, not a contradiction.
- **PN story / NEW pressure:** PN asserts GO:0034272 membership that is absent from GOA (`new_to_goa`). Review adds GO:0034272 part_of as action NEW (PMID:28306502... actually RUBCN cites discovery/RUN-domain papers) — matching the PN projection. Term verified real. Review also proposes PI3K inhibitor / negative-regulation MF terms beyond PN. Verdict: ADD GO:0034272 (review already did) — aligned with PN.
- **Mapping strategy:** This gene supports (does not change) the existing C2-component → GO:0034272 mapping. Caveat: because Rubicon associates with only a UVRAG subpopulation and inhibits the complex, `part_of` GO:0034272 is defensible but borderline vs. an "associated regulator" reading; the review itself raises this as a suggested question. Ancestors correctly held too_broad. PN-projected term coincides with review (not broader/narrower).
- **Evidence alignment:** PN cites Annual Review, a cardiovascular-autophagy review, and PMID:19270696 (Matsunaga). Review uses primary PMID:19270696, 21062745 (RUN domain/PI3KC3 inhibition), 20974968, 20943950 (Rab7 RH-domain). PMID:19270696 shared.
- **Verdict:** Consistent; NEW GO:0034272 matches PN projection (verified, new_to_goa). Open question whether `part_of` vs "associated inhibitory regulator" is the right relation for a subpopulation binder — already flagged in the review's suggested_questions; no edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/RUBCN/RUBCN-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Class 3 PI3K complex 2, direct | Class 3 PI3K complex 2 component
- UniProt: Q92622
- In branches: ALP
- Notes: Member of class III PI3K complex 2 that binds to UVRAG and inhibits activity
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - role of autophagy in cardiovascular pathology | Cardiovascular Research | Oxford Academic (oup.com)
    - Two Beclin 1-binding proteins, Atg14L and Rubicon, reciprocally regulate autophagy at different stages | Nature Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II]
        rationale: This PN type denotes component membership in the direct class III PI3K complex 2 module used during autophagosome maturation and lysosome fusion. The corresponding GO complex term is the right propagation target.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
