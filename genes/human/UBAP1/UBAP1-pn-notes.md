# UBAP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NZ09
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UBAP1/UBAP1-ai-review.yaml](UBAP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UBAP1/UBAP1-ai-review.html](UBAP1-ai-review.html)
- Gene notes: present - [genes/human/UBAP1/UBAP1-notes.md](UBAP1-notes.md)
- GOA TSV: present - [genes/human/UBAP1/UBAP1-goa.tsv](UBAP1-goa.tsv)
- UniProt record: present - [genes/human/UBAP1/UBAP1-uniprot.txt](UBAP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UBAP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UBAP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UBAP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UBAP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UBAP1 is an endosome-specific ESCRT-I fourth-subunit variant in TSG101-VPS28-VPS37A-UBAP1 complexes. Its core functions are ubiquitin binding through UBA/SOUBA domains, recognition/sorting of ubiquitinated endosomal cargo into multivesicular bodies, and endosome-specific ESCRT-I complex membership. General ESCRT-I membrane-fission annotations from MVB12A/VPS37B structural work should not be treated as direct UBAP1 evidence.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Deep research (notes), review YAML, and PN annotation agree that UBAP1 is the endosome-specific fourth ESCRT-I subunit (TSG101-VPS28-VPS37A-UBAP1) doing ubiquitin binding + MVB cargo sorting. One internal tension: the PN places UBAP1 under autophagophore-sealing, but the review deliberately argues the autophagy/membrane-fission evidence (PMID:32424346) used VPS37B-MVB12A ESCRT-I, not UBAP1, and so MARK_AS_OVER_ANNOTATED membrane fission. Defensible and well-sourced.
- **PN story / NEW pressure:** ESCRT-I membership (GO:0000813), ubiquitin binding (GO:0043130), and MVB catabolism (GO:0043162) are all already captured. The PN-projected GO:0000045 autophagosome assembly is new_to_goa but the review does NOT add it for UBAP1 (no UBAP1-specific phagophore-closure evidence). Verdict: already captured for the endosomal role; autophagosome-assembly over-reaches for UBAP1.
- **Evidence alignment:** PN cites only PMID:32424346 (the membrane-scission structure paper). Review's core ESCRT-I evidence is PMID:21757351 (UBAP1 endosome-specific ESCRT-I) + PMID:22405001 (SOUBA), and it treats PMID:32424346 as the over-annotation source — direct divergence in how the shared paper is used.
- **Verdict:** Internally consistent and defensible; flag that the PN autophagosome-sealing placement / GO:0000045 projection is not supported by UBAP1-specific evidence (review correctly withholds it).

## Full Consistency Review

- **UniProt:** Q9NZ09 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** ALP `…|Sealing of autophagophore membrane|ESCRT-I complex component` + UPS `…|trafficking|ESCRT-I complex|UBA (UBAP1)` ; **PN-node mapping:** leaf mapped/ok_for_propagation GO:0000813 ESCRT I complex; group mapped GO:0000045 autophagosome assembly; UPS nodes no_mapping/context_only.
- **Consistency:** Deep research (notes), review YAML, and PN annotation agree that UBAP1 is the endosome-specific fourth ESCRT-I subunit (TSG101-VPS28-VPS37A-UBAP1) doing ubiquitin binding + MVB cargo sorting. One internal tension: the PN places UBAP1 under autophagophore-sealing, but the review deliberately argues the autophagy/membrane-fission evidence (PMID:32424346) used VPS37B-MVB12A ESCRT-I, not UBAP1, and so MARK_AS_OVER_ANNOTATED membrane fission. Defensible and well-sourced.
- **PN story / NEW pressure:** ESCRT-I membership (GO:0000813), ubiquitin binding (GO:0043130), and MVB catabolism (GO:0043162) are all already captured. The PN-projected GO:0000045 autophagosome assembly is new_to_goa but the review does NOT add it for UBAP1 (no UBAP1-specific phagophore-closure evidence). Verdict: already captured for the endosomal role; autophagosome-assembly over-reaches for UBAP1.
- **Mapping strategy:** UBAP1 does not justify the ALP group's GO:0000045 projection — the review's evidence argument is that autophagic ESCRT-I uses MVB12A/VPS37B not UBAP1. PN-projected GO:0000045 is therefore broader/mis-attributed for this gene (TOMM20/HSPA8-style over-reach). GO:0000813 leaf mapping is correct.
- **Evidence alignment:** PN cites only PMID:32424346 (the membrane-scission structure paper). Review's core ESCRT-I evidence is PMID:21757351 (UBAP1 endosome-specific ESCRT-I) + PMID:22405001 (SOUBA), and it treats PMID:32424346 as the over-annotation source — direct divergence in how the shared paper is used.
- **Verdict:** Internally consistent and defensible; flag that the PN autophagosome-sealing placement / GO:0000045 projection is not supported by UBAP1-specific evidence (review correctly withholds it).

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/UBAP1/UBAP1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q9NZ09
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

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | ESCRT-I complex | UBA (UBAP1)
- UniProt: Q9NZ09
- In branches: ALP, UPS
- Signature domains: IPR049467, IPR015940
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex|UBA (UBAP1)
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
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
