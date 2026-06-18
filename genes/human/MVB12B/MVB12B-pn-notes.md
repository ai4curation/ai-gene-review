# MVB12B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H7P6
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MVB12B/MVB12B-ai-review.yaml](MVB12B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/MVB12B/MVB12B-ai-review.html](MVB12B-ai-review.html)
- Gene notes: present - [genes/human/MVB12B/MVB12B-notes.md](MVB12B-notes.md)
- GOA TSV: present - [genes/human/MVB12B/MVB12B-goa.tsv](MVB12B-goa.tsv)
- UniProt record: present - [genes/human/MVB12B/MVB12B-uniprot.txt](MVB12B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MVB12B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MVB12B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MVB12B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MVB12B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MVB12B is a metazoan ESCRT-I fourth subunit that complexes with TSG101, VPS28, and VPS37-family subunits. Its best-supported core cellular role is ESCRT-I-dependent sorting of ubiquitinated endosomal cargo into multivesicular bodies, supported by MABP acidic-phospholipid binding and ESCRT-I composition evidence. Viral budding and virus maturation reflect pathogen exploitation of ESCRT machinery rather than the main endogenous MVB12B function.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Two issues. (1) GO:0000813 ESCRT I complex is consistent (ACCEPTed). (2) The PN `new_to_goa` projection of GO:0000045 autophagosome assembly has no support in the MVB12B review or GOA, and parallels MVB12A where macroautophagy is MARK_AS_OVER_ANNOTATED — so PN over-reaches here. (3) Internal review bug: the GO:0043130 ubiquitin binding row is correctly flagged `negated: true` (GOA = `NOT|enables ... IDA PMID:20654576`, an experimental NOT call) yet given `action: UNDECIDED` with reason "cannot be confirmed... before accepting or removing." The curator experimentally established NON-binding; per project rules this NOT annotation should be ACCEPTed (retained), not left UNDECIDED.
- **PN story / NEW pressure:** PN asserts a brand-new autophagosome-assembly role for MVB12B (`new_to_goa`) via ESCRT-I sealing. No MVB12B-specific evidence supports it; the shared structural paper assays VPS28, and phagophore-closure ESCRT evidence (PMID:31519728) is for VPS37A. Conclusion: over-reaches; defer to expert question rather than annotate.
- **Evidence alignment:** Shared: PMID:32424346 (ESCRT-I scaffold) underpins both PN row and review CC/fission annotations; PMID:20654576 (MVB12A/B PTMs) is the basis of both the EGFR-context and the negated ubiquitin-binding row. Overlap strong; divergence only on autophagy inference.
- **Verdict:** ESCRT-I membership consistent; PN GO:0000045 (`new_to_goa`) over-reaches; review has a negation/action inconsistency. **Recommended edits:** in MVB12B YAML, change the GO:0043130 ubiquitin binding row from `action: UNDECIDED` to `ACCEPT` (retain the experimental NOT annotation; GOA NOT|enables IDA PMID:20654576) and fix the summary to reflect NON-binding rather than "cannot be confirmed." Flag the "Sealing" node so GO:0000045 is not auto-propagated to MVB12B.

## Full Consistency Review

- **UniProt:** Q9H7P6 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component` ; **PN-node mapping:** leaf `mapped / GO:0000813 ESCRT I complex`; "Sealing" group `mapped / ok_for_propagation / GO:0000045 autophagosome assembly`; class `context_only` GO:0016236. Projected: GO:0000813 (`already_in_goa_exact`), GO:0000045 (`new_to_goa`).
- **Consistency:** Two issues. (1) GO:0000813 ESCRT I complex is consistent (ACCEPTed). (2) The PN `new_to_goa` projection of GO:0000045 autophagosome assembly has no support in the MVB12B review or GOA, and parallels MVB12A where macroautophagy is MARK_AS_OVER_ANNOTATED — so PN over-reaches here. (3) Internal review bug: the GO:0043130 ubiquitin binding row is correctly flagged `negated: true` (GOA = `NOT|enables ... IDA PMID:20654576`, an experimental NOT call) yet given `action: UNDECIDED` with reason "cannot be confirmed... before accepting or removing." The curator experimentally established NON-binding; per project rules this NOT annotation should be ACCEPTed (retained), not left UNDECIDED.
- **PN story / NEW pressure:** PN asserts a brand-new autophagosome-assembly role for MVB12B (`new_to_goa`) via ESCRT-I sealing. No MVB12B-specific evidence supports it; the shared structural paper assays VPS28, and phagophore-closure ESCRT evidence (PMID:31519728) is for VPS37A. Conclusion: over-reaches; defer to expert question rather than annotate.
- **Mapping strategy:** Same as MVB12A — the "Sealing" node's blanket `ok_for_propagation` of GO:0000045 to every ESCRT-I-component leaf is too strong for MVB12B (membership ≠ demonstrated closure function). Recommend candidate-only propagation.
- **Evidence alignment:** Shared: PMID:32424346 (ESCRT-I scaffold) underpins both PN row and review CC/fission annotations; PMID:20654576 (MVB12A/B PTMs) is the basis of both the EGFR-context and the negated ubiquitin-binding row. Overlap strong; divergence only on autophagy inference.
- **Verdict:** ESCRT-I membership consistent; PN GO:0000045 (`new_to_goa`) over-reaches; review has a negation/action inconsistency. **Recommended edits:** in MVB12B YAML, change the GO:0043130 ubiquitin binding row from `action: UNDECIDED` to `ACCEPT` (retain the experimental NOT annotation; GOA NOT|enables IDA PMID:20654576) and fix the summary to reflect NON-binding rather than "cannot be confirmed." Flag the "Sealing" node so GO:0000045 is not auto-propagated to MVB12B.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/MVB12B/MVB12B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q9H7P6
- In branches: ALP
- Notes: Component of the ESCRT-I complex, involved in autophagosome closure
- PN references (titles):
    - A helical assembly of human ESCRT-I scaffolds reverse-topology membrane scission | Nature Structural & Molecular Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000813 ESCRT I complex]
        rationale: This leaf is restricted to ESCRT-I components used in autophagophore sealing. The shared GO assertion is ESCRT I complex membership.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
