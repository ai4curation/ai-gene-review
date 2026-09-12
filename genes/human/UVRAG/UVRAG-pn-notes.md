# UVRAG PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9P2Y5
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UVRAG/UVRAG-ai-review.yaml](UVRAG-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UVRAG/UVRAG-ai-review.html](UVRAG-ai-review.html)
- Gene notes: present - [genes/human/UVRAG/UVRAG-notes.md](UVRAG-notes.md)
- GOA TSV: present - [genes/human/UVRAG/UVRAG-goa.tsv](UVRAG-goa.tsv)
- UniProt record: present - [genes/human/UVRAG/UVRAG-uniprot.txt](UVRAG-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UVRAG.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UVRAG.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UVRAG.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UVRAG.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UVRAG is a regulatory/adaptor subunit of the UVRAG-containing class III PI3K complex II (PI3KC3-C2) and a late autophagy/endolysosomal trafficking factor. It binds Beclin 1/PIK3C3 complex machinery, supports PI3P-dependent autophagosome maturation, and coordinates HOPS/class C VPS and SNARE-dependent fusion events at autophagosomes and endosomes. UVRAG also has supported but non-core roles in Golgi-ER retrograde trafficking, degradative endocytic traffic, cytokinesis, and autophagy-independent DNA repair/centrosome stability.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 24; MARK_AS_OVER_ANNOTATED: 26; MODIFY: 9; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research, review, and PN all place UVRAG as the regulatory/adaptor subunit defining the type II (UVRAG-containing) class III PI3K complex (PI3KC3-C2), driving autophagosome maturation and HOPS/SNARE-dependent late-endosome/lysosome fusion. The review's PN-core framing (autophagosome maturation, positive regulation of autophagy) matches the dossier Notes verbatim (mTOR-RUBCN regulation, HOPS recruitment).
- **PN story / NEW pressure:** GO:0034272 (verified real, non-obsolete) is the projected complex term. GOA currently has only the generic parent GO:0035032; the review MODIFYs GO:0035032 → GO:0034272 (and also narrows GO:0032991/GO:0043933 to GO:0034272). So the PN's more_specific_than_existing_goa status is exactly right and the review already proposes the same upgrade. Verdict: already captured by the review's proposed MODIFY; no new NEW term needed.
- **Evidence alignment:** PN cites PMID:18843052 (Atg14L/Rubicon reciprocal regulation), PMID:16799551-equivalent Beclin1-UVRAG work, plus the class-C VPS paper and review articles. Review uses the same anchors: PMID:18843052, PMID:16799551 (positive regulator of Beclin1-PI3KC3), PMID:24550300 (SNARE/C-Vps), PMID:28306502 (Pacer/HOPS), PMID:18552835. Excellent overlap.
- **Verdict:** Consistent and well-supported; the review's GO:0034272 MODIFY is the correct, verified specific complex term and aligns with the PN projection. Best-aligned gene of the set.

## Full Consistency Review

- **UniProt:** Q9P2Y5 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** ALP `…|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component` ; **PN-node mapping:** type mapped/ok_for_propagation GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II (more_specific_than_existing_goa); group context_only GO:0035032 (class III PI3K complex); class context_only GO:0016236 macroautophagy.
- **Consistency:** Strong agreement. Deep research, review, and PN all place UVRAG as the regulatory/adaptor subunit defining the type II (UVRAG-containing) class III PI3K complex (PI3KC3-C2), driving autophagosome maturation and HOPS/SNARE-dependent late-endosome/lysosome fusion. The review's PN-core framing (autophagosome maturation, positive regulation of autophagy) matches the dossier Notes verbatim (mTOR-RUBCN regulation, HOPS recruitment).
- **PN story / NEW pressure:** GO:0034272 (verified real, non-obsolete) is the projected complex term. GOA currently has only the generic parent GO:0035032; the review MODIFYs GO:0035032 → GO:0034272 (and also narrows GO:0032991/GO:0043933 to GO:0034272). So the PN's more_specific_than_existing_goa status is exactly right and the review already proposes the same upgrade. Verdict: already captured by the review's proposed MODIFY; no new NEW term needed.
- **Mapping strategy:** UVRAG genuinely sharpens the node — it is the defining type II component, so projecting the narrower GO:0034272 (vs the parent GO:0035032 the group keeps as context_only) is well justified, not over-reach. Scope ok_for_propagation at the leaf, context_only at the group, is the correct split (component leaves propagate complex membership; regulator/context group does not).
- **Evidence alignment:** PN cites PMID:18843052 (Atg14L/Rubicon reciprocal regulation), PMID:16799551-equivalent Beclin1-UVRAG work, plus the class-C VPS paper and review articles. Review uses the same anchors: PMID:18843052, PMID:16799551 (positive regulator of Beclin1-PI3KC3), PMID:24550300 (SNARE/C-Vps), PMID:28306502 (Pacer/HOPS), PMID:18552835. Excellent overlap.
- **Verdict:** Consistent and well-supported; the review's GO:0034272 MODIFY is the correct, verified specific complex term and aligns with the PN projection. Best-aligned gene of the set.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/UVRAG/UVRAG-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Class 3 PI3K complex 2, direct | Class 3 PI3K complex 2 component
- UniProt: Q9P2Y5
- In branches: ALP
- Notes: Member of class III PI3K complex 2 that is involved in endosome and autophagosome matureration and recruits the HOPS complex for lysosome fusion. Phosphorylation by mTOR promotes binding of UVRAG to RUBCN, preventing binding to HOPS and inhibiting autophagosome maturation.
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - role of autophagy in cardiovascular pathology | Cardiovascular Research | Oxford Academic (oup.com)
    - Beclin1-binding UVRAG targets the class C Vps complex to coordinate autophagosome maturation and endocytic trafficking | Nature Cell Biology
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
- GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
