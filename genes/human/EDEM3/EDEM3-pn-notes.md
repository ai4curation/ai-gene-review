# EDEM3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BZQ6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EDEM3/EDEM3-ai-review.yaml](EDEM3-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EDEM3/EDEM3-ai-review.html
- Gene notes: present - [genes/human/EDEM3/EDEM3-notes.md](EDEM3-notes.md)
- GOA TSV: present - [genes/human/EDEM3/EDEM3-goa.tsv](EDEM3-goa.tsv)
- UniProt record: present - [genes/human/EDEM3/EDEM3-uniprot.txt](EDEM3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EDEM3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EDEM3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EDEM3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EDEM3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EDEM3/EDEM3-deep-research-falcon.md](EDEM3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EDEM3 (ER degradation-enhancing alpha-mannosidase-like protein 3) is a soluble endoplasmic reticulum lumenal protein of glycoside hydrolase family 47 (GH47, EC 3.2.1.113), one of three mammalian Htm1/Mns1 homologues (EDEM1, EDEM2, EDEM3) acting in ER-associated degradation of glycoproteins (gpERAD). EDEM3 is an active, calcium-dependent alpha-1,2-mannosidase that accelerates glycoprotein ERAD by catalyzing the downstream mannose-trimming step from Man8GlcNAc2 to Man7GlcNAc2 and further trimming toward Man5GlcNAc2 isomers, generating the demannosylated glycans recognized by the downstream lectin OS-9. It acts mainly at the second trimming step (with EDEM1 contributing to a lesser extent), downstream of the first-step enzyme EDEM2, and, like EDEM1 but unlike EDEM2, it associates with the HRD1 adaptor SEL1L. Beyond misfolded ERAD substrates, EDEM3 may also trim N-glycans on general glycoproteins. It is unique among the EDEMs in containing a protease-associated (PA) domain of unknown function, is induced by the unfolded protein response, and is broadly expressed. Biallelic loss-of-function variants cause an autosomal-recessive congenital disorder of glycosylation (EDEM3-CDG / CDG2V) with neurodevelopmental delay.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. EDEM3 = soluble ER-lumenal, calcium-dependent GH47 alpha-1,2-mannosidase (EC 3.2.1.113) catalyzing the downstream step Man8→Man7 (and toward Man5), with a unique PA domain; binds SEL1L (like EDEM1, unlike EDEM2); biallelic LoF causes EDEM3-CDG/CDG2V. Unlike EDEM1/EDEM2, EDEM3 has **no** negated mannosidase annotation — catalytic activity is undisputed (IBA/IEA/ISS/IMP + EC/RHEA all positive). No contradictions; this matches the prompt's note that EDEM3 is the demonstrably catalytic EDEM.
- **PN story / NEW pressure:** subtype→GO:1904382 is `already_in_goa_exact` (TAS Reactome + review). EDEM3's role is fully captured (GO:0004571 across IBA/IEA/ISS/IMP/TAS; GO:1904380; GO:1904382; GO:0036503; GO:0097466). No NEW term needed; review proposes none. Already captured.
- **Evidence alignment:** Strong overlap on PMID:25092655 (shared) and Reactome:R-HSA-6782685. Review adds rich EDEM3-specific literature (original characterization PMID:16431915 with E147Q catalytic proof; ERp46/TXNDC5 redox partner PMID:29784879; domain dissection PMID:33671632; HCC/HBV PMID:39838427) well beyond the terse PN row.
- **Verdict:** Consistent and well-curated; the unambiguously catalytic EDEM. subtype→GO:1904382 sound and already captured; group→GO:0006487 is a loose/broad fit for the degradation arm.

## Full Consistency Review

- **UniProt:** Q9BZQ6 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming` ; **PN-node mapping:** subtype "Mannose trimming"=mapped/ok GO:1904382 (`already_in_goa_exact`); group "N-glycosylation system"=mapped/ok GO:0006487 protein N-linked glycosylation (`new_to_goa`); intermediate type/class/branch=no_mapping.
- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. EDEM3 = soluble ER-lumenal, calcium-dependent GH47 alpha-1,2-mannosidase (EC 3.2.1.113) catalyzing the downstream step Man8→Man7 (and toward Man5), with a unique PA domain; binds SEL1L (like EDEM1, unlike EDEM2); biallelic LoF causes EDEM3-CDG/CDG2V. Unlike EDEM1/EDEM2, EDEM3 has **no** negated mannosidase annotation — catalytic activity is undisputed (IBA/IEA/ISS/IMP + EC/RHEA all positive). No contradictions; this matches the prompt's note that EDEM3 is the demonstrably catalytic EDEM.
- **PN story / NEW pressure:** subtype→GO:1904382 is `already_in_goa_exact` (TAS Reactome + review). EDEM3's role is fully captured (GO:0004571 across IBA/IEA/ISS/IMP/TAS; GO:1904380; GO:1904382; GO:0036503; GO:0097466). No NEW term needed; review proposes none. Already captured.
- **Mapping strategy:** subtype→GO:1904382 exact and strongly supported — keep; EDEM3 is the prototypical "Mannose trimming" catalytic member. group→GO:0006487 protein N-linked glycosylation (`new_to_goa`) is broader/upstream (glycan biosynthesis) than EDEM3's degradative trimming and is a loose fit — borderline over-reach for a degradation-arm enzyme. The MF (GO:0004571) is correctly the clearest/strongest of the three EDEMs.
- **Evidence alignment:** Strong overlap on PMID:25092655 (shared) and Reactome:R-HSA-6782685. Review adds rich EDEM3-specific literature (original characterization PMID:16431915 with E147Q catalytic proof; ERp46/TXNDC5 redox partner PMID:29784879; domain dissection PMID:33671632; HCC/HBV PMID:39838427) well beyond the terse PN row.
- **Verdict:** Consistent and well-curated; the unambiguously catalytic EDEM. subtype→GO:1904382 sound and already captured; group→GO:0006487 is a loose/broad fit for the degradation arm.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EDEM3/EDEM3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | N-glycan processing | Mannose trimming
- UniProt: Q9BZQ6
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
