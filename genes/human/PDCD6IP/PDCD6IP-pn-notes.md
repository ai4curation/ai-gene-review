# PDCD6IP PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8WUM4
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/PDCD6IP/PDCD6IP-ai-review.yaml](PDCD6IP-ai-review.yaml)
- AIGR review HTML: present - [genes/human/PDCD6IP/PDCD6IP-ai-review.html](PDCD6IP-ai-review.html)
- Gene notes: present - [genes/human/PDCD6IP/PDCD6IP-notes.md](PDCD6IP-notes.md)
- GOA TSV: present - [genes/human/PDCD6IP/PDCD6IP-goa.tsv](PDCD6IP-goa.tsv)
- UniProt record: present - [genes/human/PDCD6IP/PDCD6IP-uniprot.txt](PDCD6IP-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/PDCD6IP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/PDCD6IP.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PDCD6IP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PDCD6IP.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: PDCD6IP encodes ALIX/AIP1, a Bro1-domain ESCRT accessory adaptor that links cargo/adaptors and membrane-remodeling sites to CHMP4/ESCRT-III. ALIX supports MVB/late-endosomal cargo sorting, exosome biogenesis with the syndecan-syntenin pathway, basal autophagic flux and endolysosomal trafficking through ATG12-ATG3-associated regulation, and CEP55-dependent midbody cytokinesis. Viral budding is a well-supported pathogen-exploitation context, while endogenous ALIX roles center on ESCRT adaptor activity in endolysosomal, exosome, and cytokinetic membrane-remodeling pathways.
- Existing/core annotation action counts: ACCEPT: 28; KEEP_AS_NON_CORE: 25; MARK_AS_OVER_ANNOTATED: 32; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Largely consistent. The PN note (ALIX/ATG12-ATG3 recruits ESCRT-III for autophagosome closure) aligns with the review, which ACCEPTs GO:0016236 macroautophagy (ISS) on the strength of PMID:25686249 (ALIX required for basal autophagic flux). The autophagy-closure framing is supported. The leaf being `no_mapping` (heterogeneous members) is consistent with the review not asserting an autophagy-specific ESCRT-III-localization MF for ALIX.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (`more_specific_than_existing_goa` — GOA/review have the broader GO:0016236 macroautophagy). For ALIX this is more defensible than for the MVB12 subunits because the gene-specific basal-autophagy evidence (PMID:25686249) exists, but the cited support is for basal autophagic flux/late-endosome function rather than phagophore sealing specifically. Conclusion: GO:0000045 is a plausible candidate (not pure over-reach), but the review's macroautophagy ACCEPT already captures the role; adding autophagosome assembly should be expert-gated, not auto-propagated.
- **Evidence alignment:** Shared: PMID:25686249 (ATG12-ATG3–ALIX) is a PN reference and the review's macroautophagy anchor. PN also cites closure-regulator and exosome/autophagy reviews; review independently supports MVB/exosome/cytokinesis (PMID:12860994, PMID:22660413, PMID:18641129). Good overlap on the autophagy link.
- **Verdict:** Consistent; PN autophagosome-assembly projection is a reasonable candidate but the curated macroautophagy ACCEPT already covers it. No edits required.

## Full Consistency Review

- **UniProt:** Q8WUM4 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|Localization of the ESCRT-III complex` ; **PN-node mapping:** leaf `no_mapping` (members mix endosomal-sorting + SNARE genes); "Sealing" group `mapped / ok_for_propagation / GO:0000045 autophagosome assembly`; class `context_only` GO:0016236. Projected: GO:0000045 (`more_specific_than_existing_goa`).
- **Consistency:** Largely consistent. The PN note (ALIX/ATG12-ATG3 recruits ESCRT-III for autophagosome closure) aligns with the review, which ACCEPTs GO:0016236 macroautophagy (ISS) on the strength of PMID:25686249 (ALIX required for basal autophagic flux). The autophagy-closure framing is supported. The leaf being `no_mapping` (heterogeneous members) is consistent with the review not asserting an autophagy-specific ESCRT-III-localization MF for ALIX.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (`more_specific_than_existing_goa` — GOA/review have the broader GO:0016236 macroautophagy). For ALIX this is more defensible than for the MVB12 subunits because the gene-specific basal-autophagy evidence (PMID:25686249) exists, but the cited support is for basal autophagic flux/late-endosome function rather than phagophore sealing specifically. Conclusion: GO:0000045 is a plausible candidate (not pure over-reach), but the review's macroautophagy ACCEPT already captures the role; adding autophagosome assembly should be expert-gated, not auto-propagated.
- **Mapping strategy:** Node scoping is sound. The `no_mapping` leaf correctly avoids over-claiming; the "Sealing" group projecting GO:0000045 is acceptable as candidate for ALIX given basal-autophagy evidence, but should remain `more_specific` candidate rather than displacing the curated macroautophagy call.
- **Evidence alignment:** Shared: PMID:25686249 (ATG12-ATG3–ALIX) is a PN reference and the review's macroautophagy anchor. PN also cites closure-regulator and exosome/autophagy reviews; review independently supports MVB/exosome/cytokinesis (PMID:12860994, PMID:22660413, PMID:18641129). Good overlap on the autophagy link.
- **Verdict:** Consistent; PN autophagosome-assembly projection is a reasonable candidate but the curated macroautophagy ACCEPT already covers it. No edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/PDCD6IP/PDCD6IP-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | Localization of the ESCRT-III complex
- UniProt: Q8WUM4
- In branches: ALP
- Notes: Binds to ATG13-ATG3 complexes to recruit ESCRT-III for autophagosome closure
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - Synergies in exosomes and autophagy pathways for cellular homeostasis and metastasis of tumor cells | Cell & Bioscience | Full Text (biomedcentral.com)
    - ATG12–ATG3 interacts with Alix to promote basal autophagic flux and late endosome function | Nature Cell Biology
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

## Projected GO annotations (1)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
