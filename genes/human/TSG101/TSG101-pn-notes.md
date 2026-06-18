# TSG101 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q99816
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TSG101/TSG101-ai-review.yaml](TSG101-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TSG101/TSG101-ai-review.html](TSG101-ai-review.html)
- Gene notes: present - [genes/human/TSG101/TSG101-notes.md](TSG101-notes.md)
- GOA TSV: present - [genes/human/TSG101/TSG101-goa.tsv](TSG101-goa.tsv)
- UniProt record: present - [genes/human/TSG101/TSG101-uniprot.txt](TSG101-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TSG101.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TSG101.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TSG101.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TSG101.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TSG101 encodes the UEV-domain ESCRT-I subunit that binds ubiquitin/PTAP-type motifs and scaffolds ESCRT-I with VPS28, VPS37-family subunits, and MVB12/UBAP-family subunits. Its conserved core role is ESCRT-I-mediated sorting of ubiquitinated endocytic cargo into multivesicular bodies and reverse-topology membrane fission. TSG101 also participates in ESCRT-I-dependent phagophore/autophagosome closure, best represented biologically as autophagosome assembly rather than generic macroautophagy. Viral budding, cytokinesis, exosome release, and transcription/cell-growth annotations are supported non-core or over-broad branches.
- Existing/core annotation action counts: ACCEPT: 44; KEEP_AS_NON_CORE: 35; MARK_AS_OVER_ANNOTATED: 41; MODIFY: 4; NEW: 1

## PN Consistency Summary

- **Consistency:** Strongly coherent. Notes, review, both PN rows, and node mappings agree: core = UEV-domain ESCRT-I adaptor (ubiquitin/PTAP binding), MVB cargo sorting, membrane fission, and ESCRT-I-dependent phagophore/autophagosome closure. Review ACCEPTs GO:0000813 ESCRT-I (multiple lines), retires ~30 generic protein-binding rows + transcription/cell-growth legacy terms, keeps viral budding/cytokinesis/exosome non-core. Negated GO:0061631 ubiquitin-conjugating-enzyme correctly ACCEPTed. No contradictions.
- **PN story / NEW pressure:** PN "Sealing of autophagophore membrane" group projects GO:0000045 autophagosome assembly as more_specific_than_existing_goa — and the review independently adds exactly this via **action: NEW** GO:0000045 (IMP, PMID:31519728 "core ESCRT-I components TSG101 and VPS28 ... required for autophagosome completion"; PMID:31010855). Review also MODIFYs the over-broad IEA GO:0016236 macroautophagy → GO:0000045. Conclusion: ADD — exact agreement between PN projection and review NEW term (OLS-verified GO:0000045).
- **Evidence alignment:** PN ALP row title (ESCRT-I helical-assembly Nat Struct Mol Biol) is structural context; the review's load-bearing closure citations PMID:31519728 and PMID:31010855 are the autophagy-specific support and align with the PN projection's intent. No miscitation found.
- **Verdict:** Consistent; ACCEPT both mappings and endorse NEW GO:0000045. PN projection and review converge precisely (GO:0000813 + GO:0000045).

## Full Consistency Review

- **UniProt:** Q99816 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** ALP row `Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component`; UPS row `Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex|UEV (Type 2)` ; **PN-node mapping:** ALP leaf mapped GO:0000813 ESCRT I complex (already_in_goa_exact); ALP "Sealing" group mapped GO:0000045 autophagosome assembly (more_specific_than_existing_goa); UPS subtype/type/group no_mapping; UPS class context_only GO:0140036 ubiquitin-modified protein reader activity
- **Consistency:** Strongly coherent. Notes, review, both PN rows, and node mappings agree: core = UEV-domain ESCRT-I adaptor (ubiquitin/PTAP binding), MVB cargo sorting, membrane fission, and ESCRT-I-dependent phagophore/autophagosome closure. Review ACCEPTs GO:0000813 ESCRT-I (multiple lines), retires ~30 generic protein-binding rows + transcription/cell-growth legacy terms, keeps viral budding/cytokinesis/exosome non-core. Negated GO:0061631 ubiquitin-conjugating-enzyme correctly ACCEPTed. No contradictions.
- **PN story / NEW pressure:** PN "Sealing of autophagophore membrane" group projects GO:0000045 autophagosome assembly as more_specific_than_existing_goa — and the review independently adds exactly this via **action: NEW** GO:0000045 (IMP, PMID:31519728 "core ESCRT-I components TSG101 and VPS28 ... required for autophagosome completion"; PMID:31010855). Review also MODIFYs the over-broad IEA GO:0016236 macroautophagy → GO:0000045. Conclusion: ADD — exact agreement between PN projection and review NEW term (OLS-verified GO:0000045).
- **Mapping strategy:** No change needed; this gene is the test case the projection got right. ESCRT-I leaf → GO:0000813 (exact, OLS-verified); Sealing group → GO:0000045 (correctly narrower than existing macroautophagy, avoiding the autophagosome-lysosome-fusion over-reach the rationale warns against). UPS-side no_mapping/context_only is appropriately conservative.
- **Evidence alignment:** PN ALP row title (ESCRT-I helical-assembly Nat Struct Mol Biol) is structural context; the review's load-bearing closure citations PMID:31519728 and PMID:31010855 are the autophagy-specific support and align with the PN projection's intent. No miscitation found.
- **Verdict:** Consistent; ACCEPT both mappings and endorse NEW GO:0000045. PN projection and review converge precisely (GO:0000813 + GO:0000045).
- **Recommended edits:** None required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TSG101/TSG101-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q99816
- In branches: ALP, UPS
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

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | ESCRT-I complex | UEV (Type 2)
- UniProt: Q99816
- In branches: ALP, UPS
- Signature domains: IPR008883, cd11685
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex|UEV (Type 2)
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
