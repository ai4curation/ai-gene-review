# CSNK1D PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P48730
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CSNK1D/CSNK1D-ai-review.yaml](CSNK1D-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CSNK1D/CSNK1D-ai-review.html](CSNK1D-ai-review.html)
- Gene notes: present - [genes/human/CSNK1D/CSNK1D-notes.md](CSNK1D-notes.md)
- GOA TSV: present - [genes/human/CSNK1D/CSNK1D-goa.tsv](CSNK1D-goa.tsv)
- UniProt record: present - [genes/human/CSNK1D/CSNK1D-uniprot.txt](CSNK1D-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CSNK1D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CSNK1D.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CSNK1D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CSNK1D.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: Casein kinase I isoform delta (CK1delta) is a constitutively active, monomeric serine/threonine protein kinase of the casein kinase 1 (CK1) family. It uses ATP and is magnesium-dependent, and is operationally defined as a "casein kinase" by its preference for acidic substrates; it performs both primed (phospho-directed) and unprimed phosphorylation. Its activity is autoinhibited by C-terminal autophosphorylation and reactivated by phosphatase (PP1)-mediated dephosphorylation. CK1delta is a central component of the circadian clock, phosphorylating PERIOD proteins PER1 and PER2 to control their stability and nuclear entry and thereby set circadian period; missense variants (e.g. T44A, H46R) reduce kinase activity and cause familial advanced sleep phase syndrome and familial migraine. CK1delta also phosphorylates Dishevelled (DVL2/DVL3) and other components to modulate Wnt/beta-catenin signaling, acts at the centrosome and Golgi to promote microtubule nucleation, Golgi organization and primary (non-motile) ciliogenesis, and regulates the mitotic spindle. It phosphorylates a large and diverse set of additional substrates including p53/TP53, MDM2, YAP1, HIF1A, TOP2A, connexin-43/GJA1, PKD2, eIF6, DCK and tau/MAPT, linking it to DNA-damage responses, Hippo signaling, vesicle trafficking and (via tau hyperphosphorylation) neurodegeneration. It localizes to the cytoplasm/cytosol, nucleus, centrosome, perinuclear region, spindle and spindle microtubules, Golgi apparatus, ciliary basal body and plasma membrane, with correct localization dependent on kinase activity.
- Existing/core annotation action counts: ACCEPT: 80; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 15; MODIFY: 5

## PN Consistency Summary

- **Consistency:** GAP. The review treats CK1δ's COPII/SEC23 phosphorylation (Reactome GO:0048208 COPII vesicle coat assembly; R-HSA-5694441) as a generic, non-core **secretory** role and has NO autophagy annotation — it never mentions RAB1-directed autophagosome closure or COPII-regulated autophagophore membrane input. The PN frames the SAME COPII/RAB1 biology as autophagy-directed (RAB1 effector → phosphorylates COPII coat → autophagosome closure), citing CK1δ/Hrr25 autophagosome-completion papers absent from the review. So review and PN are not contradictory but interpret overlapping evidence (Golgi/COPII/RAB1) in different pathways; the autophagy reading is under-captured in the review.
- **PN story / NEW pressure:** PN asserts an autophagosome-closure/sealing role not in existing GO or the review. GO:0000045 "autophagosome assembly" verified real (OLS) and confirmed new_to_goa (no autophagy term in CSNK1D-goa.tsv). Defensible **ADD** if the Hrr25/CK1δ autophagosome-completion literature (Frontiers/JCB titles in PN row) holds for human CK1δ — but PN supplies only article titles, not verified PMIDs; much of the primary evidence is yeast Hrr25. Treat as defensible-but-needs-PMID-verification.
- **Evidence alignment:** No overlap. PN cites autophagosome-closure review + Ypt1/Rab1-Hrr25 JCB + CK1δ/Hrr25 autophagosome-completion Frontiers (titles only). Review cites COPII via Reactome (R-HSA-204005, R-HSA-5694441) only, framed as secretory. The autophagy PMIDs are missing from the review.
- **Verdict:** UNDER-CAPTURED autophagy role; PN ADD (GO:0000045) plausible but PMID-unverified. **Recommended edits:** [REF] resolve the PN row's title-only citations to PMIDs and confirm human (not just yeast Hrr25) evidence; [YAML] if confirmed, add GO:0000045 (involved_in) and reframe the SEC23/COPII annotations to note an autophagosome-membrane-input role alongside secretion.

## Full Consistency Review

- **UniProt:** P48730 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** row1 `ALP|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input|COPII vesicle component regulator`; row2 `ALP|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|...unknown` ; **PN-node mapping:** Sealing group→GO:0000045 autophagosome assembly (new_to_goa); all other ALP nodes no_mapping; ALP class context_only→GO:0016236.
- **Consistency:** GAP. The review treats CK1δ's COPII/SEC23 phosphorylation (Reactome GO:0048208 COPII vesicle coat assembly; R-HSA-5694441) as a generic, non-core **secretory** role and has NO autophagy annotation — it never mentions RAB1-directed autophagosome closure or COPII-regulated autophagophore membrane input. The PN frames the SAME COPII/RAB1 biology as autophagy-directed (RAB1 effector → phosphorylates COPII coat → autophagosome closure), citing CK1δ/Hrr25 autophagosome-completion papers absent from the review. So review and PN are not contradictory but interpret overlapping evidence (Golgi/COPII/RAB1) in different pathways; the autophagy reading is under-captured in the review.
- **PN story / NEW pressure:** PN asserts an autophagosome-closure/sealing role not in existing GO or the review. GO:0000045 "autophagosome assembly" verified real (OLS) and confirmed new_to_goa (no autophagy term in CSNK1D-goa.tsv). Defensible **ADD** if the Hrr25/CK1δ autophagosome-completion literature (Frontiers/JCB titles in PN row) holds for human CK1δ — but PN supplies only article titles, not verified PMIDs; much of the primary evidence is yeast Hrr25. Treat as defensible-but-needs-PMID-verification.
- **Mapping strategy:** GO:0000045 from the "Sealing of autophagophore membrane" group is appropriately specific (assembly, not autophagosome-lysosome fusion); the "unknown" leaf and COPII-regulator leaf are correctly no_mapping. Reasonable; not over-broad.
- **Evidence alignment:** No overlap. PN cites autophagosome-closure review + Ypt1/Rab1-Hrr25 JCB + CK1δ/Hrr25 autophagosome-completion Frontiers (titles only). Review cites COPII via Reactome (R-HSA-204005, R-HSA-5694441) only, framed as secretory. The autophagy PMIDs are missing from the review.
- **Verdict:** UNDER-CAPTURED autophagy role; PN ADD (GO:0000045) plausible but PMID-unverified. **Recommended edits:** [REF] resolve the PN row's title-only citations to PMIDs and confirm human (not just yeast Hrr25) evidence; [YAML] if confirmed, add GO:0000045 (involved_in) and reframe the SEC23/COPII annotations to note an autophagosome-membrane-input role alongside secretion.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CSNK1D/CSNK1D-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Regulation of autophagophore membrane composition | ER membrane input | COPII vesicle component regulator
- UniProt: P48730
- In branches: ALP
- Notes: RAB1 effector that is directed to autophagosomes by RAB1, then phosphorylates the COPII coat to promote autophagy. Important for autophagosome closure.
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - Ypt1/Rab1 regulates Hrr25/CK1δ kinase activity in ER–Golgi traffic and macroautophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - Frontiers | Casein Kinase 1 Family Member CK1δ/Hrr25 Is Required for Autophagosome Completion | Cell and Developmental Biology (frontiersin.org)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input|COPII vesicle component regulator
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups upstream regulators of COPII contribution to autophagophore membrane input. The two-member set does not support one crisp shared GO term beyond broad vesicle-coating or kinase context.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | Specific function in sealing of autophagophore membrane unknown
- UniProt: P48730
- In branches: ALP
- Notes: RAB1 effector that is directed to autophagosomes by RAB1, then phosphorylates the COPII coat to promote autophagy. Important for autophagosome closure.
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - Ypt1/Rab1 regulates Hrr25/CK1δ kinase activity in ER–Golgi traffic and macroautophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - Frontiers | Casein Kinase 1 Family Member CK1δ/Hrr25 Is Required for Autophagosome Completion | Cell and Developmental Biology (frontiersin.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|Specific function in sealing of autophagophore membrane unknown
        status=no_mapping scope= GO=[]
        rationale: This PN leaf is explicitly an unknown-function residual bucket and does not support a defensible shared GO mapping.
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
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
