# EDEM2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BV94
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EDEM2/EDEM2-ai-review.yaml](EDEM2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EDEM2/EDEM2-ai-review.html
- Gene notes: present - [genes/human/EDEM2/EDEM2-notes.md](EDEM2-notes.md)
- GOA TSV: present - [genes/human/EDEM2/EDEM2-goa.tsv](EDEM2-goa.tsv)
- UniProt record: present - [genes/human/EDEM2/EDEM2-uniprot.txt](EDEM2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EDEM2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EDEM2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EDEM2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EDEM2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EDEM2/EDEM2-deep-research-falcon.md](EDEM2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EDEM2 (ER degradation-enhancing alpha-mannosidase-like protein 2) is a soluble, N-glycosylated endoplasmic reticulum lumenal protein of glycoside hydrolase family 47 (GH47), one of three mammalian Htm1/Mns1 homologues (EDEM1, EDEM2, EDEM3) acting in ER-associated degradation of glycoproteins (gpERAD). EDEM2 catalyzes the initiating mannose-trimming step of mammalian gpERAD, converting Man9GlcNAc2 to Man8GlcNAc2 isomer B, an activity that requires the conserved EF-hand glutamate (E117) and is thought to operate within a disulfide-linked complex with the thioredoxin-domain protein TXNDC11. By generating Man8GlcNAc2, EDEM2 acts upstream of EDEM1 and EDEM3, which further trim the glycan to expose the alpha-1,6-mannose recognized by the downstream lectin OS-9. EDEM2 recognizes and binds misfolded glycoproteins (e.g. misfolded alpha-1-antitrypsin), accelerates their degradation, and promotes ER-to-cytosol retrotranslocation of substrates such as the ricin A chain; unlike EDEM1 and EDEM3 it does not bind the HRD1 adaptor SEL1L. It is induced by the IRE1-XBP1 branch of the unfolded protein response and is broadly expressed. Its catalytic mannosidase activity was historically controversial, with early recombinant assays detecting no activity before endogenous-knockout analysis established its role as the first-step mannosidase.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 8; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. EDEM2 = soluble ER-lumenal GH47 protein that catalyzes the **first** trimming step Man9→Man8B (E117-dependent, in an obligate disulfide complex with TXNDC11), committing substrates to gpERAD upstream of EDEM1/EDEM3; does NOT bind SEL1L. The **negated** GO:0004571 IDA from PMID:15537790 (recombinant "no activity") is correctly retained as superseded by the positive GO:0004571 IMP (PMID:25092655) + E117Q mutant. Review and notes flag this explicitly. No contradictions.
- **PN story / NEW pressure:** subtype→GO:1904382 marked `more_specific_than_existing_goa`. Note GOA already has GO:1904380 (ER mannose trimming, IMP+TAS+IEA) but NOT GO:1904382 (the ERAD-specific child) for EDEM2 — so the PN projection of GO:1904382 to EDEM2 is a **defensible, more-specific real annotation** (EDEM2 demonstrably trims in the gpERAD pathway, PMID:25092655). GO:1904382 verified real (OLS, non-obsolete). This is the one genuine ADD candidate among the EDEMs. [REF/MAP]
- **Evidence alignment:** Strong overlap on PMID:25092655 (shared with EDEM1/3). Review adds the mechanistic TXNDC11 disulfide paper (PMID:32065582), folding-state dependence (PMID:30374462), and pathway model (PMID:39654396) beyond the PN row.
- **Verdict:** Consistent and well-curated; catalytic (first-step) EDEM, NOT-mannosidase handled correctly. subtype→GO:1904382 is a defensible more-specific ADD; group→GO:0006487 is a loose/broad fit.

## Full Consistency Review

- **UniProt:** Q9BV94 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming` ; **PN-node mapping:** subtype "Mannose trimming"=mapped/ok GO:1904382 (`more_specific_than_existing_goa`); group "N-glycosylation system"=mapped/ok GO:0006487 protein N-linked glycosylation (`more_specific_than_existing_goa`); intermediate type/class/branch=no_mapping.
- **Consistency:** Deep research ↔ review YAML ↔ PN annotation consistent. EDEM2 = soluble ER-lumenal GH47 protein that catalyzes the **first** trimming step Man9→Man8B (E117-dependent, in an obligate disulfide complex with TXNDC11), committing substrates to gpERAD upstream of EDEM1/EDEM3; does NOT bind SEL1L. The **negated** GO:0004571 IDA from PMID:15537790 (recombinant "no activity") is correctly retained as superseded by the positive GO:0004571 IMP (PMID:25092655) + E117Q mutant. Review and notes flag this explicitly. No contradictions.
- **PN story / NEW pressure:** subtype→GO:1904382 marked `more_specific_than_existing_goa`. Note GOA already has GO:1904380 (ER mannose trimming, IMP+TAS+IEA) but NOT GO:1904382 (the ERAD-specific child) for EDEM2 — so the PN projection of GO:1904382 to EDEM2 is a **defensible, more-specific real annotation** (EDEM2 demonstrably trims in the gpERAD pathway, PMID:25092655). GO:1904382 verified real (OLS, non-obsolete). This is the one genuine ADD candidate among the EDEMs. [REF/MAP]
- **Mapping strategy:** This gene **does** sharpen the node: EDEM2 is the catalytic first-step mannosidase, the clearest "Mannose trimming" exemplar. subtype→GO:1904382 is appropriate and adds specificity over existing GO:1904380. group→GO:0006487 protein N-linked glycosylation (`more_specific_than_existing_goa`) is broader/upstream than EDEM2's degradative trimming and is a loose fit — borderline over-reach for a degradation-arm enzyme.
- **Evidence alignment:** Strong overlap on PMID:25092655 (shared with EDEM1/3). Review adds the mechanistic TXNDC11 disulfide paper (PMID:32065582), folding-state dependence (PMID:30374462), and pathway model (PMID:39654396) beyond the PN row.
- **Verdict:** Consistent and well-curated; catalytic (first-step) EDEM, NOT-mannosidase handled correctly. subtype→GO:1904382 is a defensible more-specific ADD; group→GO:0006487 is a loose/broad fit.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EDEM2/EDEM2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | N-glycan processing | Mannose trimming
- UniProt: Q9BV94
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
- GO:0006487 protein N-linked glycosylation | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system
- GO:1904382 mannose trimming involved in glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
