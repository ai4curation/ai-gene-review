# CHMP7 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8WUX9
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHMP7/CHMP7-ai-review.yaml](CHMP7-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHMP7/CHMP7-ai-review.html](CHMP7-ai-review.html)
- Gene notes: present - [genes/human/CHMP7/CHMP7-notes.md](CHMP7-notes.md)
- GOA TSV: present - [genes/human/CHMP7/CHMP7-goa.tsv](CHMP7-goa.tsv)
- UniProt record: present - [genes/human/CHMP7/CHMP7-uniprot.txt](CHMP7-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP7.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP7.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHMP7 encodes an ESCRT-III-like / ESCRT-II-III hybrid protein that acts most specifically as an upstream adaptor for nuclear-envelope ESCRT recruitment. During late anaphase, LEMD2/LEM2 recruits CHMP7 to the reforming nuclear envelope and chromatin-disk periphery, where CHMP7 helps recruit downstream ESCRT-III components such as CHMP2A and IST1/CHMP8 to seal nuclear-envelope holes and coordinate spindle microtubule disassembly. CHMP7 also has evidence for CHMP4B-associated endosomal sorting, but this appears secondary to its better-defined nuclear-envelope repair/sealing role.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 46; MARK_AS_OVER_ANNOTATED: 11; MODIFY: 11

## PN Consistency Summary

- **Consistency:** Mostly consistent, with a real specificity tension. The review identifies CHMP7 as an ESCRT-II/ESCRT-III **hybrid** whose most specific role is **nuclear-envelope hole sealing** via LEMD2 binding and CHMP4B recruitment — not autophagosome closure. PN lumps CHMP7 into the generic ESCRT-III sealing/microautophagy component buckets. The review's autophagy entries (GO:0097352 IEA, KEEP_AS_NON_CORE) are flagged as "plausible secondary ESCRT pathway / broad location context." The PN-vs-review divergence is in emphasis (NE sealing vs autophagosome sealing), not factual contradiction.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real); for CHMP7 the support is family/membership-level, so a gene-specific assertion would over-reach. Notably the review's own NEW pressure is elsewhere — a suggested_question asks for a more specific GO term for ESCRT-mediated **nuclear-envelope hole sealing during anaphase** (proposed_new_terms is empty; that is a candidate, unverified gap). **PN over-reaches on autophagy for CHMP7 — already captured non-core; do not ADD GO:0000045.**
- **Evidence alignment:** Divergent. PN cites only the Cells "Key Regulators of Autophagosome Closure" review. Review cites primary ESCRT/NE-sealing literature (incl. PMID:36107470 ESCRT-III-MIT interactome [verified, not the PN review]). No shared specific citations.
- **Verdict:** Consistent; review correctly centers NE sealing and treats PN's autophagy placement as non-core. **Recommended edits:** none for autophagy; (optional, out-of-scope) the NE-hole-sealing GO gap the review flags is worth pursuing separately.

## Full Consistency Review

- **UniProt:** Q8WUX9 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP → Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex component` AND `ALP → Microautophagy → General microautophagy machinery → ESCRT-III complex component` (2 rows; shared CHMP template)
- **PN-node mapping:** type → GO:0000815 ESCRT III complex (`already_in_goa_exact`); "Sealing" group → GO:0000045 autophagosome assembly (`more_specific_than_existing_goa`); classes `context_only`/`too_broad`; branch `no_mapping`.
- **Consistency:** Mostly consistent, with a real specificity tension. The review identifies CHMP7 as an ESCRT-II/ESCRT-III **hybrid** whose most specific role is **nuclear-envelope hole sealing** via LEMD2 binding and CHMP4B recruitment — not autophagosome closure. PN lumps CHMP7 into the generic ESCRT-III sealing/microautophagy component buckets. The review's autophagy entries (GO:0097352 IEA, KEEP_AS_NON_CORE) are flagged as "plausible secondary ESCRT pathway / broad location context." The PN-vs-review divergence is in emphasis (NE sealing vs autophagosome sealing), not factual contradiction.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real); for CHMP7 the support is family/membership-level, so a gene-specific assertion would over-reach. Notably the review's own NEW pressure is elsewhere — a suggested_question asks for a more specific GO term for ESCRT-mediated **nuclear-envelope hole sealing during anaphase** (proposed_new_terms is empty; that is a candidate, unverified gap). **PN over-reaches on autophagy for CHMP7 — already captured non-core; do not ADD GO:0000045.**
- **Mapping strategy:** No change to the ALP node. CHMP7's distinctive function is nuclear-envelope/ESCRT-II-III hybrid, peripheral to the autophagosome-sealing node; GO:0000815 leaf is defensible, the "Sealing" group→GO:0000045 projection is a weak gene-specific fit (class `context_only` is the correct ceiling).
- **Evidence alignment:** Divergent. PN cites only the Cells "Key Regulators of Autophagosome Closure" review. Review cites primary ESCRT/NE-sealing literature (incl. PMID:36107470 ESCRT-III-MIT interactome [verified, not the PN review]). No shared specific citations.
- **Verdict:** Consistent; review correctly centers NE sealing and treats PN's autophagy placement as non-core. **Recommended edits:** none for autophagy; (optional, out-of-scope) the NE-hole-sealing GO gap the review flags is worth pursuing separately.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CHMP7/CHMP7-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex component
- UniProt: Q8WUX9
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
- UniProt: Q8WUX9
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
