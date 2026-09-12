# VPS37A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NEZ2
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/VPS37A/VPS37A-ai-review.yaml](VPS37A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/VPS37A/VPS37A-ai-review.html](VPS37A-ai-review.html)
- Gene notes: present - [genes/human/VPS37A/VPS37A-notes.md](VPS37A-notes.md)
- GOA TSV: present - [genes/human/VPS37A/VPS37A-goa.tsv](VPS37A-goa.tsv)
- UniProt record: present - [genes/human/VPS37A/VPS37A-uniprot.txt](VPS37A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/VPS37A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/VPS37A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS37A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS37A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: VPS37A is a VPS37-family ESCRT-I subunit that complexes with TSG101, VPS28, and MVB12/UBAP-family subunits. It supports ubiquitin-dependent endosomal cargo sorting into multivesicular bodies and has a directly tested role in phagophore closure, where its PUEV-containing N terminus recruits ESCRT machinery for autophagosome completion.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 5; MODIFY: 4; NEW: 1

## PN Consistency Summary

- **Consistency:** Strongly consistent. VPS37A is the one VPS37 paralog with direct mammalian phagophore-closure evidence (PMID:31519728), and the review uniquely adds GO:0000045 as a NEW annotation (plus MODIFY of GO:0006612/GO:0016236→GO:0000045). PN's two projections (GO:0000813 ESCRT-I; GO:0000045 autophagosome assembly) match the review exactly. The UEV/UPS placement aligns with ESCRT-I/ubiquitin cargo sorting (review accepts GO:0043162, GO:0036258, GO:0000813).
- **PN story / NEW pressure:** Already captured. PN asserts phagophore sealing → the review independently makes GO:0000045 a NEW term (verified real via OLS) supported by VPS37A-on-phagophore + VPS28/CHMP2A recruitment evidence. No additional new term warranted; PN adds nothing the review lacks.
- **Evidence alignment:** Strong overlap. PN cites the ESCRT-I scaffold paper (=PMID:32424346) and "VPS37A directs ESCRT recruitment for phagophore closure" (=PMID:31519728), both load-bearing in the review. PN's MDPI "Key Regulators of Autophagosome Closure" review is not cited; the review uses primary literature instead.
- **Verdict:** Fully consistent; PN projections match the review's accepted/NEW terms. No edits needed.

## Full Consistency Review

- **UniProt:** Q8NEZ2 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 3 rows, ALP+UPS — (1) ALP `Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-I complex component`; (2) ALP same group → `Localization of the ESCRT-III complex`; (3) UPS `Ubiquitin and UBL binding → trafficking → ESCRT-I complex → UEV (Type 2)`. **PN-node mapping:** ESCRT-I-component leaf=mapped→GO:0000813; sealing group=mapped→GO:0000045; ESCRT-III-localization leaf=no_mapping; macroautophagy class + UPS nodes=context_only/no_mapping. **Projected:** GO:0000045 (more_specific_than_existing_goa), GO:0000813 (already_in_goa_exact).
- **Consistency:** Strongly consistent. VPS37A is the one VPS37 paralog with direct mammalian phagophore-closure evidence (PMID:31519728), and the review uniquely adds GO:0000045 as a NEW annotation (plus MODIFY of GO:0006612/GO:0016236→GO:0000045). PN's two projections (GO:0000813 ESCRT-I; GO:0000045 autophagosome assembly) match the review exactly. The UEV/UPS placement aligns with ESCRT-I/ubiquitin cargo sorting (review accepts GO:0043162, GO:0036258, GO:0000813).
- **PN story / NEW pressure:** Already captured. PN asserts phagophore sealing → the review independently makes GO:0000045 a NEW term (verified real via OLS) supported by VPS37A-on-phagophore + VPS28/CHMP2A recruitment evidence. No additional new term warranted; PN adds nothing the review lacks.
- **Mapping strategy:** No change. VPS37A is the strongest evidence anchor for the sealing-group→GO:0000045 mapping; its direct IMP/PMID:31519728 data justify the group projection for this gene. ESCRT-III-localization leaf no_mapping is correct (mixed gene set). Unlike the TOMM20/HSPA8 over-reach pattern, this projection is narrower than GOA and the review agrees.
- **Evidence alignment:** Strong overlap. PN cites the ESCRT-I scaffold paper (=PMID:32424346) and "VPS37A directs ESCRT recruitment for phagophore closure" (=PMID:31519728), both load-bearing in the review. PN's MDPI "Key Regulators of Autophagosome Closure" review is not cited; the review uses primary literature instead.
- **Verdict:** Fully consistent; PN projections match the review's accepted/NEW terms. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VPS37A/VPS37A-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q8NEZ2
- In branches: ALP, UPS
- Notes: Component of the ESCRT-I complex, involved in autophagosome closure. Specifically called out for directing recruitment of ESCRT machinery to autophagophore. Also, localizes to phagophore and recruits ESCRT machinery for phagophore closure
- PN references (titles):
    - A helical assembly of human ESCRT-I scaffolds reverse-topology membrane scission | Nature Structural & Molecular Biology
    - VPS37A directs ESCRT recruitment for phagophore closure | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | Localization of the ESCRT-III complex
- UniProt: Q8NEZ2
- In branches: ALP, UPS
- Notes: Component of the ESCRT-I complex, involved in autophagosome closure. Specifically called out for directing recruitment of ESCRT machinery to autophagophore. Also, localizes to phagophore and recruits ESCRT machinery for phagophore closure
- PN references (titles):
    - A helical assembly of human ESCRT-I scaffolds reverse-topology membrane scission | Nature Structural & Molecular Biology
    - VPS37A directs ESCRT recruitment for phagophore closure | Journal of Cell Biology | Rockefeller University Press (rupress.org)
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

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | ESCRT-I complex | UEV (Type 2)
- UniProt: Q8NEZ2
- In branches: ALP, UPS
- Signature domains: cd11685
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

## Projected GO annotations (3)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
