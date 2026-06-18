# VPS4B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75351
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/VPS4B/VPS4B-ai-review.yaml](VPS4B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/VPS4B/VPS4B-ai-review.html](VPS4B-ai-review.html)
- Gene notes: present - [genes/human/VPS4B/VPS4B-notes.md](VPS4B-notes.md)
- GOA TSV: present - [genes/human/VPS4B/VPS4B-goa.tsv](VPS4B-goa.tsv)
- UniProt record: present - [genes/human/VPS4B/VPS4B-uniprot.txt](VPS4B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/VPS4B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/VPS4B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS4B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS4B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: VPS4B is a conserved AAA-family ATPase that recognizes ESCRT-III assemblies through its MIT domain and uses ATP hydrolysis to remodel and disassemble ESCRT-III polymers. Direct biochemical evidence shows VPS4 binding to and disassembly of CHMP2A-CHMP3 helical tubes upon ATP hydrolysis. This core activity supports endosomal/MVB cargo sorting and related ESCRT membrane-remodeling outputs, including cytokinesis, viral budding, plasma membrane repair, and exosome secretion. The core function is ATP-dependent ESCRT-III remodeling/disassembly rather than generic protein binding or ESCRT-III complex membership.
- Existing/core annotation action counts: ACCEPT: 30; KEEP_AS_NON_CORE: 32; MARK_AS_OVER_ANNOTATED: 25; MODIFY: 6; NEW: 1; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** CONTRADICTION on GO:0000815, plus goa_status concern (identical to VPS4A). Review thesis: VPS4B is the AAA ATPase that binds inside CHMP2A-CHMP3 tubes and disassembles ESCRT-III on ATP hydrolysis (direct biochemistry, PMID:18687924), NOT an ESCRT-III subunit; notes state "PN projection to GO:0000815 should not be added for VPS4B." Review instead asserts GO:1904903 ESCRT III complex disassembly (verified) + GO:0016887. GOA has GO:0016236/0006914/0061738/0097352 but no GO:0000815 or GO:0000045, so projecting GO:0000815 as "more_specific_than_existing_goa" mislabels a contested new CC as a refinement.
- **PN story / NEW pressure:** Mixed. "ESCRT-III activity modulator" placement matches the review; the microautophagy "ESCRT-III complex component" leaf miscategorizes VPS4B as a member. Accurate story captured by GO:1904903/GO:0016887; no new term needed. (Review keeps the GOA late-endosomal-microautophagy row as UNDECIDED, autophagy/autophagosome-maturation/macroautophagy as MARK_AS_OVER_ANNOTATED.)
- **Evidence alignment:** Partial. PN cites the MDPI closure review + "CHMP2A as a regulator of phagophore closure" (Nat Commun). Review draws on VPS4B-specific primary work (PMID:18687924, 18606141, 15024011, 16757520, 20616062, 24105262) not in PN.
- **Verdict:** ESCRT-III-modulator framing consistent; GO:0000815 projection contradicts the review (VPS4B disassembles, not member). **Recommended edits:** none to YAML; reclassify PN microautophagy leaf→GO:0000815 to context_only for VPS4B and drop/relabel the GO:0000815 and GO:0000045 projections.

## Full Consistency Review

- **UniProt:** O75351 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 2 rows, ALP — (1) `Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex activity modulator`; (2) `Microautophagy → General microautophagy machinery → ESCRT-III complex component`. **PN-node mapping:** modulator leaf=context_only (GO:0000815); microautophagy-component leaf=mapped→GO:0000815; sealing group=mapped→GO:0000045; classes context_only (GO:0016236, GO:0016237). **Projected:** GO:0000045 (more_specific_than_existing_goa), GO:0000815 ESCRT III complex (more_specific_than_existing_goa).
- **Consistency:** CONTRADICTION on GO:0000815, plus goa_status concern (identical to VPS4A). Review thesis: VPS4B is the AAA ATPase that binds inside CHMP2A-CHMP3 tubes and disassembles ESCRT-III on ATP hydrolysis (direct biochemistry, PMID:18687924), NOT an ESCRT-III subunit; notes state "PN projection to GO:0000815 should not be added for VPS4B." Review instead asserts GO:1904903 ESCRT III complex disassembly (verified) + GO:0016887. GOA has GO:0016236/0006914/0061738/0097352 but no GO:0000815 or GO:0000045, so projecting GO:0000815 as "more_specific_than_existing_goa" mislabels a contested new CC as a refinement.
- **PN story / NEW pressure:** Mixed. "ESCRT-III activity modulator" placement matches the review; the microautophagy "ESCRT-III complex component" leaf miscategorizes VPS4B as a member. Accurate story captured by GO:1904903/GO:0016887; no new term needed. (Review keeps the GOA late-endosomal-microautophagy row as UNDECIDED, autophagy/autophagosome-maturation/macroautophagy as MARK_AS_OVER_ANNOTATED.)
- **Mapping strategy:** Change recommended (same as VPS4A). Microautophagy-component leaf→GO:0000815 should be context_only/no_mapping for VPS4B (consistent with the sibling modulator leaf), as VPS4B is not an ESCRT-III subunit. GO:0000815 over-reaches per the rejected broader-projection precedent; GO:0000045 also unsupported (review does not add it).
- **Evidence alignment:** Partial. PN cites the MDPI closure review + "CHMP2A as a regulator of phagophore closure" (Nat Commun). Review draws on VPS4B-specific primary work (PMID:18687924, 18606141, 15024011, 16757520, 20616062, 24105262) not in PN.
- **Verdict:** ESCRT-III-modulator framing consistent; GO:0000815 projection contradicts the review (VPS4B disassembles, not member). **Recommended edits:** none to YAML; reclassify PN microautophagy leaf→GO:0000815 to context_only for VPS4B and drop/relabel the GO:0000815 and GO:0000045 projections.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VPS4B/VPS4B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex activity modulator
- UniProt: O75351
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
- UniProt: O75351
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
