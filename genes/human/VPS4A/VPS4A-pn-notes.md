# VPS4A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UN37
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/VPS4A/VPS4A-ai-review.yaml](VPS4A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/VPS4A/VPS4A-ai-review.html](VPS4A-ai-review.html)
- Gene notes: present - [genes/human/VPS4A/VPS4A-notes.md](VPS4A-notes.md)
- GOA TSV: present - [genes/human/VPS4A/VPS4A-goa.tsv](VPS4A-goa.tsv)
- UniProt record: present - [genes/human/VPS4A/VPS4A-uniprot.txt](VPS4A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/VPS4A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/VPS4A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS4A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS4A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: VPS4A is a conserved AAA-family ATPase that recognizes membrane-associated ESCRT-III assemblies through its MIT domain and uses ATP hydrolysis to remodel and disassemble ESCRT-III polymers. This recycling function supports ESCRT-dependent membrane remodeling in MVB/endosomal cargo sorting and related topologically equivalent events, including cytokinetic abscission, nuclear-envelope sealing, viral budding, plasma membrane repair, and exosome release. The core function is ATP-driven ESCRT-III remodeling/disassembly rather than generic protein binding or membership in the ESCRT-III complex itself.
- Existing/core annotation action counts: ACCEPT: 52; KEEP_AS_NON_CORE: 47; MARK_AS_OVER_ANNOTATED: 31; MODIFY: 9; UNDECIDED: 2

## PN Consistency Summary

- **Consistency:** CONTRADICTION on GO:0000815, and a labeling concern on goa_status. The review's central thesis (description + core_functions) is that VPS4A is the AAA ATPase that recognizes and *disassembles* ESCRT-III, NOT an ESCRT-III subunit; notes explicitly say "PN projection to GO:0000815 should not be added for VPS4A." The review instead asserts GO:1904903 ESCRT III complex disassembly (verified real via OLS) and GO:0016887 ATP hydrolysis. GOA contains no GO:0000815 or GO:0000045 — only GO:0016236 — so the projected goa_status "more_specific_than_existing_goa" is misleading (GO:0000815 would be a new, contested CC, not a refinement).
- **PN story / NEW pressure:** Mixed. PN's "ESCRT-III activity modulator" placement is biologically apt and matches the review's disassembly framing — but the microautophagy "ESCRT-III complex component" leaf miscategorizes VPS4A as a complex member. The accurate molecular story (ATP-driven ESCRT-III disassembly) is captured by the review's GO:1904903/GO:0016887; no new term needed.
- **Evidence alignment:** Partial. PN cites the MDPI autophagosome-closure review and PMID-bearing "CHMP2A as a regulator of phagophore closure" (Nat Commun). Review is built on VPS4-specific primary/structural literature (PMID:17928862, 18606141, 36604498, 20616062) not in PN.
- **Verdict:** ESCRT-III-modulator framing consistent; GO:0000815 projection contradicts the review (VPS4A disassembles, not member). **Recommended edits:** none to YAML; reclassify PN microautophagy leaf→GO:0000815 to context_only for VPS4A and drop/relabel the GO:0000815 and GO:0000045 projections.

## Full Consistency Review

- **UniProt:** Q9UN37 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 2 rows, ALP — (1) `Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex activity modulator`; (2) `Microautophagy → General microautophagy machinery → ESCRT-III complex component`. **PN-node mapping:** modulator leaf=context_only (GO:0000815, "should not project ESCRT-III membership to all members"); microautophagy-component leaf=mapped→GO:0000815; sealing group=mapped→GO:0000045; classes context_only (GO:0016236, GO:0016237). **Projected:** GO:0000045 (more_specific_than_existing_goa), GO:0000815 ESCRT III complex (more_specific_than_existing_goa).
- **Consistency:** CONTRADICTION on GO:0000815, and a labeling concern on goa_status. The review's central thesis (description + core_functions) is that VPS4A is the AAA ATPase that recognizes and *disassembles* ESCRT-III, NOT an ESCRT-III subunit; notes explicitly say "PN projection to GO:0000815 should not be added for VPS4A." The review instead asserts GO:1904903 ESCRT III complex disassembly (verified real via OLS) and GO:0016887 ATP hydrolysis. GOA contains no GO:0000815 or GO:0000045 — only GO:0016236 — so the projected goa_status "more_specific_than_existing_goa" is misleading (GO:0000815 would be a new, contested CC, not a refinement).
- **PN story / NEW pressure:** Mixed. PN's "ESCRT-III activity modulator" placement is biologically apt and matches the review's disassembly framing — but the microautophagy "ESCRT-III complex component" leaf miscategorizes VPS4A as a complex member. The accurate molecular story (ATP-driven ESCRT-III disassembly) is captured by the review's GO:1904903/GO:0016887; no new term needed.
- **Mapping strategy:** Change recommended. The microautophagy-component leaf→GO:0000815 should be context_only/no_mapping for VPS4A (as the sealing modulator leaf already correctly is), since VPS4A is not an ESCRT-III subunit. GO:0000815 over-reaches; this matches the rejected broader-projection precedent. GO:0000045 also unsupported here (review keeps autophagy rows MARK_AS_OVER_ANNOTATED / late-microautophagy UNDECIDED).
- **Evidence alignment:** Partial. PN cites the MDPI autophagosome-closure review and PMID-bearing "CHMP2A as a regulator of phagophore closure" (Nat Commun). Review is built on VPS4-specific primary/structural literature (PMID:17928862, 18606141, 36604498, 20616062) not in PN.
- **Verdict:** ESCRT-III-modulator framing consistent; GO:0000815 projection contradicts the review (VPS4A disassembles, not member). **Recommended edits:** none to YAML; reclassify PN microautophagy leaf→GO:0000815 to context_only for VPS4A and drop/relabel the GO:0000815 and GO:0000045 projections.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VPS4A/VPS4A-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex activity modulator
- UniProt: Q9UN37
- In branches: ALP
- Notes: VPS4A and VPS4B are AAA+ ATPases that work with ESCRT-III in membrane scission and autophagosome closure.
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - An autophagy assay reveals the ESCRT-III component CHMP2A as a regulator of phagophore closure | Nature Communications
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex activity modulator
        status=context_only scope=too_broad_to_propagate GO=[GO:0000815 ESCRT III complex]
        rationale: Reviewed as an ESCRT-III activity modulator. It is related to ESCRT-III but should not project ESCRT-III complex membership to all members.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Microautophagy | General microautophagy machinery | ESCRT-III complex component
- UniProt: Q9UN37
- In branches: ALP
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000815 ESCRT III complex]
        rationale: This leaf is a component bucket for ESCRT-III machinery used in microautophagy contexts. The shared GO assertion is ESCRT III complex membership.
    - [group] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
