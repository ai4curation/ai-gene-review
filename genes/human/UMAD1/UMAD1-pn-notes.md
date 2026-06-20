# UMAD1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: C9J7I0
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UMAD1/UMAD1-ai-review.yaml](UMAD1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UMAD1/UMAD1-ai-review.html](UMAD1-ai-review.html)
- Gene notes: present - [genes/human/UMAD1/UMAD1-notes.md](UMAD1-notes.md)
- GOA TSV: present - [genes/human/UMAD1/UMAD1-goa.tsv](UMAD1-goa.tsv)
- UniProt record: present - [genes/human/UMAD1/UMAD1-uniprot.txt](UMAD1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UMAD1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UMAD1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UMAD1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UMAD1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UMAD1 is a poorly characterized 137 amino acid human protein containing a predicted C-terminal UMA domain. Its name and domain architecture place it in the UBAP1/MVB12-associated UMA-domain protein family, but current local evidence does not establish a specific ESCRT-I complex, endosomal sorting, autophagy, membrane fission, or viral budding function for UMAD1. UniProt lists no FUNCTION comment or GO cross-references for UMAD1, and GOA currently contains only broad IntAct protein-binding evidence from a large-scale binary interactome map.
- Existing/core annotation action counts: MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** MAJOR divergence. The PN annotation asserts UMAD1 is "Component of the ESCRT-I complex, involved in autophagosome closure" and projects GO:0000813 + GO:0000045. The review YAML and notes conclude the opposite: UMAD1 is poorly characterized, UniProt has no FUNCTION comment and zero GO/PAN-GO annotations, and the only GOA evidence is generic IPI protein binding (HuRI; GABARAPL1, TH isoform 3). The review explicitly declines any ESCRT-I/autophagy function.
- **PN story / NEW pressure:** The PN asserts a role (ESCRT-I membership + autophagosome assembly) not in GO and not supported by the review. PMID:32424346 lists UMAD1 only as a *possible* UMA-domain fourth subunit and notes some theoretical complexes may not form. Verdict: PN over-reaches — neither GO:0000813 nor GO:0000045 is defensible for UMAD1 on current evidence (would be a speculative NEW from name/domain only).
- **Evidence alignment:** PN cites PMID:32424346 (helical ESCRT-I scaffold). Review cites the same PMID plus PMID:32296183 (HuRI) and UniProt — and reads PMID:32424346 as explicitly NOT establishing a UMAD1 complex. Same papers, opposite conclusions.
- **Verdict:** CONTRADICTION — PN projects ESCRT-I + autophagosome-assembly membership that the review rejects as unsupported. Recommend the PN leaf not project GO terms onto UMAD1 (mark gene-level no_mapping/UNDECIDED) pending direct evidence.

## Full Consistency Review

- **UniProt:** C9J7I0 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** ALP `…|Sealing of autophagophore membrane|ESCRT-I complex component` ; **PN-node mapping:** leaf mapped/ok_for_propagation GO:0000813 ESCRT I complex; group mapped GO:0000045 autophagosome assembly (both flagged new_to_goa).
- **Consistency:** MAJOR divergence. The PN annotation asserts UMAD1 is "Component of the ESCRT-I complex, involved in autophagosome closure" and projects GO:0000813 + GO:0000045. The review YAML and notes conclude the opposite: UMAD1 is poorly characterized, UniProt has no FUNCTION comment and zero GO/PAN-GO annotations, and the only GOA evidence is generic IPI protein binding (HuRI; GABARAPL1, TH isoform 3). The review explicitly declines any ESCRT-I/autophagy function.
- **PN story / NEW pressure:** The PN asserts a role (ESCRT-I membership + autophagosome assembly) not in GO and not supported by the review. PMID:32424346 lists UMAD1 only as a *possible* UMA-domain fourth subunit and notes some theoretical complexes may not form. Verdict: PN over-reaches — neither GO:0000813 nor GO:0000045 is defensible for UMAD1 on current evidence (would be a speculative NEW from name/domain only).
- **Mapping strategy:** This gene should NOT drive the ALP leaf/group projection. UMAD1 is the weakest member of the ESCRT-I-component leaf (cf. UBAP1, VPS28); propagating GO:0000813/GO:0000045 to it on family-name grounds is exactly the kind of paralog/domain over-annotation to avoid.
- **Evidence alignment:** PN cites PMID:32424346 (helical ESCRT-I scaffold). Review cites the same PMID plus PMID:32296183 (HuRI) and UniProt — and reads PMID:32424346 as explicitly NOT establishing a UMAD1 complex. Same papers, opposite conclusions.
- **Verdict:** CONTRADICTION — PN projects ESCRT-I + autophagosome-assembly membership that the review rejects as unsupported. Recommend the PN leaf not project GO terms onto UMAD1 (mark gene-level no_mapping/UNDECIDED) pending direct evidence.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/UMAD1/UMAD1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: C9J7I0
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
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
