# CHMP5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NZZ3
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHMP5/CHMP5-ai-review.yaml](CHMP5-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHMP5/CHMP5-ai-review.html](CHMP5-ai-review.html)
- Gene notes: present - [genes/human/CHMP5/CHMP5-notes.md](CHMP5-notes.md)
- GOA TSV: present - [genes/human/CHMP5/CHMP5-goa.tsv](CHMP5-goa.tsv)
- UniProt record: present - [genes/human/CHMP5/CHMP5-uniprot.txt](CHMP5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHMP5 encodes a SNF7-family ESCRT-III-associated regulatory protein that links LIP5/VTA1 to VPS4-dependent ESCRT-III recycling during endosomal multivesicular body sorting. CHMP5 is primarily cytosolic but functions at endosomal ESCRT assemblies, where CHMP5-LIP5/VTA1 interactions help tune VPS4 activation/disassembly and support MVB cargo sorting and lysosomal degradation of membrane proteins such as EGFR. Broader ESCRT contexts including cytokinesis, nuclear-envelope sealing, plasma membrane repair, viral budding, and autophagy are biologically plausible but secondary; infection-specific evidence supports CHMP5 involvement in anti-Shigella autophagy rather than a general CHMP5-specific autophagosome maturation mechanism.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 43; MARK_AS_OVER_ANNOTATED: 21; MODIFY: 4

## PN Consistency Summary

- **Consistency:** Consistent. The review frames CHMP5 not as a polymerizing core subunit but as a SNF7-family ESCRT-III-**associated regulator** that links LIP5/VTA1 to VPS4 disassembly. Its description explicitly says evidence does not support a "general CHMP5-specific autophagosome maturation mechanism." PN's component-bucket placement and the review's regulatory framing are compatible; the review is appropriately more cautious than the PN's blanket "ESCRT-III complex component" label.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real). CHMP5 support is family/regulatory-inheritance only (autophagosome maturation is IEA/GO_REF:0000117, KEEP_AS_NON_CORE). A gene-specific GO:0000045 assertion would be over-reach; the review already captures the autophagy context as non-core and asks (suggested_question) which CHMP5 autophagy annotations rest on direct closure/maturation assays. **PN over-reaches for CHMP5 — already captured; do not ADD.**
- **Evidence alignment:** Divergent. PN cites only the Cells "Key Regulators of Autophagosome Closure" review. Review cites primary ESCRT/regulatory literature (incl. PMID:36107470 ESCRT-III-MIT interactome [verified, not the PN review], PMID:17984323). No shared specific citations; same broad theme.
- **Verdict:** Consistent; review appropriately conservative on the PN autophagy projection. **Recommended edits:** none.

## Full Consistency Review

- **UniProt:** Q9NZZ3 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP → Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex component` AND `ALP → Microautophagy → General microautophagy machinery → ESCRT-III complex component` (2 rows; shared CHMP template)
- **PN-node mapping:** type → GO:0000815 ESCRT III complex (`already_in_goa_exact`); "Sealing" group → GO:0000045 autophagosome assembly (`more_specific_than_existing_goa`); classes `context_only`/`too_broad`; branch `no_mapping`.
- **Consistency:** Consistent. The review frames CHMP5 not as a polymerizing core subunit but as a SNF7-family ESCRT-III-**associated regulator** that links LIP5/VTA1 to VPS4 disassembly. Its description explicitly says evidence does not support a "general CHMP5-specific autophagosome maturation mechanism." PN's component-bucket placement and the review's regulatory framing are compatible; the review is appropriately more cautious than the PN's blanket "ESCRT-III complex component" label.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real). CHMP5 support is family/regulatory-inheritance only (autophagosome maturation is IEA/GO_REF:0000117, KEEP_AS_NON_CORE). A gene-specific GO:0000045 assertion would be over-reach; the review already captures the autophagy context as non-core and asks (suggested_question) which CHMP5 autophagy annotations rest on direct closure/maturation assays. **PN over-reaches for CHMP5 — already captured; do not ADD.**
- **Mapping strategy:** No change. CHMP5's regulatory (LIP5/VPS4) role differs from the structural "ESCRT-III complex component" leaf; class-level `context_only` is correct and the GO:0000815 leaf is the most CHMP5-defensible part of the projection.
- **Evidence alignment:** Divergent. PN cites only the Cells "Key Regulators of Autophagosome Closure" review. Review cites primary ESCRT/regulatory literature (incl. PMID:36107470 ESCRT-III-MIT interactome [verified, not the PN review], PMID:17984323). No shared specific citations; same broad theme.
- **Verdict:** Consistent; review appropriately conservative on the PN autophagy projection. **Recommended edits:** none.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CHMP5/CHMP5-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex component
- UniProt: Q9NZZ3
- In branches: ALP
- Notes: Component of the ESCRT-III complex, involved in autophagosome closure
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000815 ESCRT III complex]
        rationale: This PN type is a structural component class for ESCRT-III factors used in autophagophore sealing. The matching GO cellular-component term is ESCRT III complex, which is more precise than the broader late-fusion process mapping.
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
- UniProt: Q9NZZ3
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
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex component
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
