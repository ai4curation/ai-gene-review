# EDEM1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92611
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EDEM1/EDEM1-ai-review.yaml](EDEM1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EDEM1/EDEM1-ai-review.html
- Gene notes: present - [genes/human/EDEM1/EDEM1-notes.md](EDEM1-notes.md)
- GOA TSV: present - [genes/human/EDEM1/EDEM1-goa.tsv](EDEM1-goa.tsv)
- UniProt record: present - [genes/human/EDEM1/EDEM1-uniprot.txt](EDEM1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EDEM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EDEM1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EDEM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EDEM1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EDEM1/EDEM1-deep-research-falcon.md](EDEM1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EDEM1 (ER degradation-enhancing alpha-mannosidase-like protein 1) is a single-pass type II endoplasmic reticulum membrane protein of glycoside hydrolase family 47 (GH47), one of three mammalian Htm1/Mns1 homologues (EDEM1, EDEM2, EDEM3) acting in the ER-associated degradation of glycoproteins (gpERAD). EDEM1 extracts terminally misfolded glycoproteins, but not proteins undergoing productive folding, from the calnexin/calreticulin folding cycle and accelerates their clearance, delivering aberrant substrates to the SEL1L/HRD1 dislocation and ubiquitination machinery and, via Derlin-2/-3, to the p97/VCP retrotranslocation system. It recognizes non-native protein structure in a glycan-independent manner (acting in part as a lectin/holdase-like factor), binding both glycosylated and nonglycosylated misfolded substrates, and it requires its mannosidase-like domain for association with SEL1L. EDEM1 possesses low alpha-1,2-mannosidase activity, contributing to the second mannose-trimming step (Man8GlcNAc2 to Man7GlcNAc2) that exposes the alpha-1,6-mannose recognized by downstream lectins (OS-9/XTP3-B); its catalytic activity is weak relative to its recognition/delivery role and was historically debated. EDEM1 is induced by the IRE1-XBP1 branch of the unfolded protein response, resides in the ER membrane and concentrates in the ER-derived quality control compartment (ERQC), and promotes ER-to-cytosol retrotranslocation of substrates including the ricin A chain.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 9; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. EDEM1 = GH47 type-II ER membrane factor that recognizes terminally misfolded glycoproteins (glycan-independently) and delivers them to SEL1L/HRD1 ERAD; possesses weak alpha-1,2-mannosidase activity (second step Man8B→Man7). Critically, the **negated** (NOT) GO:0004571 IDA from PMID:12610306 (historical "no activity") is correctly retained as superseded by the positive IMP GO:0004571 (PMID:25092655). Review and notes both flag this NOT-vs-positive tension explicitly. No contradictions.
- **PN story / NEW pressure:** PN's mannose-trimming subtype → GO:1904382, which is `already_in_goa_exact` (TAS Reactome + matches review). EDEM1's contribution is already captured (GO:1904380, GO:1904382, GO:0036503, GO:0004571 IMP). No NEW term needed; review proposes none. Already captured.
- **Evidence alignment:** Strong overlap on the shared landmark PMID:25092655 (also EDEM2/EDEM3) and Reactome:R-HSA-6782685. Review adds extensive EDEM1-specific literature (PMID:12610306, 19524542, 21062743, 23233672, 24200403, 30374462, 32423001) beyond the PN row.
- **Verdict:** Consistent and well-curated; NOT-mannosidase tension handled correctly. subtype→GO:1904382 sound; group→GO:0006487 is a loose/broad fit for the degradation arm.

## Full Consistency Review

- **UniProt:** Q92611 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming` ; **PN-node mapping:** subtype "Mannose trimming"=mapped/ok GO:1904382 (mannose trimming in glycoprotein ERAD, `already_in_goa_exact`); group "N-glycosylation system"=mapped/ok GO:0006487 protein N-linked glycosylation (`new_to_goa`); intermediate type/class/branch=no_mapping.
- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. EDEM1 = GH47 type-II ER membrane factor that recognizes terminally misfolded glycoproteins (glycan-independently) and delivers them to SEL1L/HRD1 ERAD; possesses weak alpha-1,2-mannosidase activity (second step Man8B→Man7). Critically, the **negated** (NOT) GO:0004571 IDA from PMID:12610306 (historical "no activity") is correctly retained as superseded by the positive IMP GO:0004571 (PMID:25092655). Review and notes both flag this NOT-vs-positive tension explicitly. No contradictions.
- **PN story / NEW pressure:** PN's mannose-trimming subtype → GO:1904382, which is `already_in_goa_exact` (TAS Reactome + matches review). EDEM1's contribution is already captured (GO:1904380, GO:1904382, GO:0036503, GO:0004571 IMP). No NEW term needed; review proposes none. Already captured.
- **Mapping strategy:** subtype→GO:1904382 is exact and well-supported — keep. **Caveat on the catalytic MF:** EDEM1 is catalytic but WEAKLY so (weakest of the three EDEMs); the review correctly keeps GO:0004571 as a supporting (not dominant) function behind GO:0051787 misfolded protein binding (its defining CORE MF). The group→GO:0006487 protein N-linked glycosylation projection is broader/upstream (glycan installation) than EDEM1's degradative trimming role and is a loose fit — borderline over-reach for a degradation-arm factor.
- **Evidence alignment:** Strong overlap on the shared landmark PMID:25092655 (also EDEM2/EDEM3) and Reactome:R-HSA-6782685. Review adds extensive EDEM1-specific literature (PMID:12610306, 19524542, 21062743, 23233672, 24200403, 30374462, 32423001) beyond the PN row.
- **Verdict:** Consistent and well-curated; NOT-mannosidase tension handled correctly. subtype→GO:1904382 sound; group→GO:0006487 is a loose/broad fit for the degradation arm.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EDEM1/EDEM1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | N-glycan processing | Mannose trimming
- UniProt: Q92611
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904382 mannose trimming involved in glycoprotein ERAD pathway]
        rationale: Within the ER proteostasis branch, this PN subtype denotes mannose trimming used in glycoprotein quality control and ERAD triage. That is close enough for propagation to the GO mannose-trimming-in-ERAD process, but the PN subtype is framed as a proteostasis step rather than a formal GO process class.
    - [type] ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] ER proteostasis|Glycoproteostasis|N-glycosylation system
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006487 protein N-linked glycosylation]
        rationale: This PN group captures the ER N-glycosylation machinery that installs and processes N-linked glycans during proteostasis. GO protein N-linked glycosylation is the best current propagation target in the local cache.
    - [class] ER proteostasis|Glycoproteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0006487 protein N-linked glycosylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system
- GO:1904382 mannose trimming involved in glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
