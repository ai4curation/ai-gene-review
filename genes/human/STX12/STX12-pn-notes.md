# STX12 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q86Y82
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/STX12/STX12-ai-review.yaml](STX12-ai-review.yaml)
- AIGR review HTML: present - [genes/human/STX12/STX12-ai-review.html](STX12-ai-review.html)
- Gene notes: present - [genes/human/STX12/STX12-notes.md](STX12-notes.md)
- GOA TSV: present - [genes/human/STX12/STX12-goa.tsv](STX12-goa.tsv)
- UniProt record: present - [genes/human/STX12/STX12-uniprot.txt](STX12-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/STX12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/STX12.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/STX12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/STX12.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: STX12 encodes syntaxin-12/syntaxin-13, a syntaxin-family SNARE on endosomal, early endosomal, recycling endosomal, and Golgi membranes. Its core function is SNAP receptor/SNARE-mediated vesicle docking and membrane fusion in endosomal recycling and intracellular membrane traffic. Direct evidence also supports a role at LC3-positive phagophores/autophagosome assembly or maturation, likely as an autophagy-specific output of its SNARE trafficking activity. STX12 is distinct from ESCRT-III machinery.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 13; MODIFY: 2

## PN Consistency Summary

- **Consistency:** **CONTRADICTION flagged.** PN row 3 projects GO:0000815 ESCRT III complex **membership** as ok_for_propagation, but the review YAML and notes explicitly reject this ("The PN projection to GO:0000815 should not be added for STX12… it is not an ESCRT-III complex subunit"). STX12 is a syntaxin/SNARE that genetically/functionally intersects ESCRT-III (CHMP2B modifier) but is not a component. GOA has **no** GO:0000815 for STX12 (confirmed). The other PN mapping (GO:0000045) is fully consistent — review ACCEPTs GO:0000045 + GO:0000407 phagophore assembly site (IMP, PMID:24095276).
- **PN story / NEW pressure:** PN over-reaches on ESCRT-III membership. GO:0000815 is verified real but is a CC for the membrane-scission complex; STX12 is a modulator, not a subunit → projecting membership over-annotates. The autophagy-sealing story is already captured (GO:0000045, already_in_goa). Conclude: **PN GO:0000815 over-reaches; do NOT propagate to STX12.**
- **Evidence alignment:** Strong overlap on autophagy: PN's "Syntaxin 13… required for autophagosome maturation" = review PMID:24095276 (core). PN's MDPI "Key Regulators of Autophagosome Closure" review is not in `supported_by` (secondary). Review enriches with SNARE/endosomal-recycling evidence (UniProt, PMID:19546860).
- **Verdict:** Consistent on the autophagosome-assembly mapping; **PN row-3 ESCRT-III-component projection conflicts with the review and is an over-annotation.** No gene-YAML edit warranted (review already rejects it correctly); the fix belongs in the PN mapping. **Recommended edits:** none to STX12-ai-review.yaml; flag PN microautophagy "ESCRT-III complex component" node to exclude STX12 / reclassify as ESCRT-III modulator.

## Full Consistency Review

- **UniProt:** Q86Y82 (syntaxin-12/13) · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 3 rows, ALP. (1) `…Autophagosome closure maturation… → Sealing of autophagophore membrane → ESCRT-III complex activity modulator`; (2) `…Sealing… → Localization of the ESCRT-III complex`; (3) `…Microautophagy → General microautophagy machinery → ESCRT-III complex component`. **PN-node mapping:** sealing group=`mapped`→GO:0000045 autophagosome assembly; ESCRT-III-modulator leaf=`context_only`→GO:0000815; ESCRT-III-localization leaf=`no_mapping`; **microautophagy ESCRT-III-component leaf=`mapped`/`ok_for_propagation`→GO:0000815 ESCRT III complex (more_specific_than_existing_goa).**
- **Consistency:** **CONTRADICTION flagged.** PN row 3 projects GO:0000815 ESCRT III complex **membership** as ok_for_propagation, but the review YAML and notes explicitly reject this ("The PN projection to GO:0000815 should not be added for STX12… it is not an ESCRT-III complex subunit"). STX12 is a syntaxin/SNARE that genetically/functionally intersects ESCRT-III (CHMP2B modifier) but is not a component. GOA has **no** GO:0000815 for STX12 (confirmed). The other PN mapping (GO:0000045) is fully consistent — review ACCEPTs GO:0000045 + GO:0000407 phagophore assembly site (IMP, PMID:24095276).
- **PN story / NEW pressure:** PN over-reaches on ESCRT-III membership. GO:0000815 is verified real but is a CC for the membrane-scission complex; STX12 is a modulator, not a subunit → projecting membership over-annotates. The autophagy-sealing story is already captured (GO:0000045, already_in_goa). Conclude: **PN GO:0000815 over-reaches; do NOT propagate to STX12.**
- **Mapping strategy:** The microautophagy "ESCRT-III complex component" leaf should NOT include STX12 (analogous to the TOMM20/RAB7A "broader/wrong-bucket" precedent — here it's a misclassification of an ESCRT modulator as a component). Recommend the PN node exclude STX12 or relabel it as an ESCRT-III modulator (consistent with row-1 `context_only`).
- **Evidence alignment:** Strong overlap on autophagy: PN's "Syntaxin 13… required for autophagosome maturation" = review PMID:24095276 (core). PN's MDPI "Key Regulators of Autophagosome Closure" review is not in `supported_by` (secondary). Review enriches with SNARE/endosomal-recycling evidence (UniProt, PMID:19546860).
- **Verdict:** Consistent on the autophagosome-assembly mapping; **PN row-3 ESCRT-III-component projection conflicts with the review and is an over-annotation.** No gene-YAML edit warranted (review already rejects it correctly); the fix belongs in the PN mapping. **Recommended edits:** none to STX12-ai-review.yaml; flag PN microautophagy "ESCRT-III complex component" node to exclude STX12 / reclassify as ESCRT-III modulator.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/STX12/STX12-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex activity modulator
- UniProt: Q86Y82
- In branches: ALP
- Notes: Works with ESCRT-III complex (and is a genetic modifier for mutations in CHMP2B) for autophagosome closure, along with its binding partner VTI1A. Knockdown of STX12 or its binding partner VTI1A leads to accumulation of the autophagy marker LC3, affects autophagosome maturation, and blocks autophagic flux. Also, is a recycling endosome SNARE that regulates autophagosome closure and acts upstream of ESCRT-III.
- PN references (titles):
    - Syntaxin 13, a Genetic Modifier of Mutant CHMP2B in Frontotemporal Dementia, Is Required for Autophagosome Maturation - ScienceDirect
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | Localization of the ESCRT-III complex
- UniProt: Q86Y82
- In branches: ALP
- Notes: Works with ESCRT-III complex (and is a genetic modifier for mutations in CHMP2B) for autophagosome closure, along with its binding partner VTI1A. Knockdown of STX12 or its binding partner VTI1A leads to accumulation of the autophagy marker LC3, affects autophagosome maturation, and blocks autophagic flux. Also, is a recycling endosome SNARE that regulates autophagosome closure and acts upstream of ESCRT-III.
- PN references (titles):
    - Syntaxin 13, a Genetic Modifier of Mutant CHMP2B in Frontotemporal Dementia, Is Required for Autophagosome Maturation - ScienceDirect
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|Localization of the ESCRT-III complex
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups factors that affect ESCRT-III localization during sealing, but the current member set mixes endosomal sorting and SNARE trafficking genes rather than one clean shared autophagy-specific GO term.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Microautophagy | General microautophagy machinery | ESCRT-III complex component
- UniProt: Q86Y82
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

## Projected GO annotations (3)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
