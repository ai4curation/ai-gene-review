# VPS28 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UK41
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/VPS28/VPS28-ai-review.yaml](VPS28-ai-review.yaml)
- AIGR review HTML: present - [genes/human/VPS28/VPS28-ai-review.html](VPS28-ai-review.html)
- Gene notes: present - [genes/human/VPS28/VPS28-notes.md](VPS28-notes.md)
- GOA TSV: present - [genes/human/VPS28/VPS28-goa.tsv](VPS28-goa.tsv)
- UniProt record: present - [genes/human/VPS28/VPS28-uniprot.txt](VPS28-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/VPS28.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/VPS28.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS28.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS28.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: VPS28 is a conserved core subunit of human ESCRT-I. It pairs with TSG101, a VPS37 paralog, and an MVB12/UBAP-family subunit to organize ESCRT-I for ubiquitin-dependent endosomal cargo sorting, multivesicular body assembly, reverse-topology membrane remodeling, and phagophore/autophagosome closure. Unlike TSG101, VPS28 is not well supported as a direct ubiquitin-binding protein; its core role is ESCRT-I structural/scaffold assembly and membrane-site recruitment.
- Existing/core annotation action counts: ACCEPT: 31; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 18; MODIFY: 3; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research/notes, review, and PN all treat VPS28 as a constitutive structural/scaffold ESCRT-I subunit acting in MVB sorting plus ESCRT-I-dependent phagophore/autophagosome closure. The review adds nuance the PN does not contradict: VPS28 itself does not bind ubiquitin (TSG101 UEV does), so it MARKs GO:0043130 over-annotated.
- **PN story / NEW pressure:** ESCRT-I membership (GO:0000813) is already_in_goa. For the autophagy role, GOA only has broad GO:0016236 macroautophagy; the review MODIFYs that to GO:0000045 autophagosome assembly AND adds GO:0000045 as a NEW annotation (IMP, PMID:32424346 helical-interface mutant → closure defect). This matches the PN projection exactly. Verdict: PN story is real and the review correctly adds the more specific GO:0000045 (new to direct GOA).
- **Evidence alignment:** PN cites only PMID:32424346. Review's autophagy evidence pairs PMID:32424346 with PMID:31519728 (VPS37A directs ESCRT recruitment for phagophore closure) and PMID:20588296 — broader and concordant. ESCRT-I/MVB core uses PMID:11134028/11916981/18005716/20654576/21757351. Good overlap, review is richer.
- **Verdict:** Consistent and well-supported; the VPS28 review is the model case for this ESCRT-I leaf — GO:0000045 NEW is justified and matches the PN mapping.

## Full Consistency Review

- **UniProt:** Q9UK41 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** ALP `…|Sealing of autophagophore membrane|ESCRT-I complex component` ; **PN-node mapping:** leaf mapped/ok_for_propagation GO:0000813 ESCRT I complex (already_in_goa_exact); group mapped GO:0000045 autophagosome assembly (more_specific_than_existing_goa).
- **Consistency:** Strong agreement. Deep research/notes, review, and PN all treat VPS28 as a constitutive structural/scaffold ESCRT-I subunit acting in MVB sorting plus ESCRT-I-dependent phagophore/autophagosome closure. The review adds nuance the PN does not contradict: VPS28 itself does not bind ubiquitin (TSG101 UEV does), so it MARKs GO:0043130 over-annotated.
- **PN story / NEW pressure:** ESCRT-I membership (GO:0000813) is already_in_goa. For the autophagy role, GOA only has broad GO:0016236 macroautophagy; the review MODIFYs that to GO:0000045 autophagosome assembly AND adds GO:0000045 as a NEW annotation (IMP, PMID:32424346 helical-interface mutant → closure defect). This matches the PN projection exactly. Verdict: PN story is real and the review correctly adds the more specific GO:0000045 (new to direct GOA).
- **Mapping strategy:** VPS28 legitimately supports the ALP leaf (GO:0000813) and group (GO:0000045) projections — unlike UBAP1/UMAD1 it has direct VPS28 closure evidence (PMID:31519728, PMID:32424346). Scope ok_for_propagation is justified; PN-projected GO:0000045 is appropriately narrower than parent macroautophagy and aligns with the review.
- **Evidence alignment:** PN cites only PMID:32424346. Review's autophagy evidence pairs PMID:32424346 with PMID:31519728 (VPS37A directs ESCRT recruitment for phagophore closure) and PMID:20588296 — broader and concordant. ESCRT-I/MVB core uses PMID:11134028/11916981/18005716/20654576/21757351. Good overlap, review is richer.
- **Verdict:** Consistent and well-supported; the VPS28 review is the model case for this ESCRT-I leaf — GO:0000045 NEW is justified and matches the PN mapping.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VPS28/VPS28-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q9UK41
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
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
