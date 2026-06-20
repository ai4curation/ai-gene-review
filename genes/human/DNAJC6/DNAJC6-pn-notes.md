# DNAJC6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75061
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC6/DNAJC6-ai-review.yaml](DNAJC6-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC6/DNAJC6-ai-review.html](DNAJC6-ai-review.html)
- Gene notes: present - [genes/human/DNAJC6/DNAJC6-notes.md](DNAJC6-notes.md)
- GOA TSV: present - [genes/human/DNAJC6/DNAJC6-goa.tsv](DNAJC6-goa.tsv)
- UniProt record: present - [genes/human/DNAJC6/DNAJC6-uniprot.txt](DNAJC6-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC6.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC6.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC6 (auxilin, auxilin-1) is a neuronally enriched DnaJ/HSP40 co-chaperone that drives the HSC70/HSPA8-dependent uncoating of clathrin-coated vesicles. It is a multidomain protein comprising an N-terminal PTEN-like tensin-type phosphatase domain and a C2 domain (a phosphoinositide-binding membrane-targeting module that is thought to be catalytically degenerate), a long disordered clathrin-binding region, and a C-terminal J domain. Auxilin binds clathrin cages stoichiometrically (one per triskelion) and, through its J domain, recruits HSPA8/HSC70 and stimulates its ATPase activity to dismantle the clathrin lattice, thereby promoting clathrin-mediated endocytosis and the recycling/uncoating of synaptic vesicles at nerve terminals. Loss-of-function mutations cause autosomal-recessive juvenile- and early-onset Parkinson disease (PARK19A/PARK19B) through impaired synaptic vesicle endocytosis in dopaminergic neurons.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 12; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Consistent, with one MF-specificity nuance. Deep research (notes), review and PN converge on DNAJC6/auxilin as the neuronal clathrin-uncoating co-chaperone: binds clathrin cages (1 per triskelion) and, via its C-terminal J domain, recruits HSPA8/HSC70 and stimulates its ATPase to dismantle the coat; PARK19 disease gene (PMID:18489706 VERIFIED, 20160091 VERIFIED, 29735704). The review's chaperone-binding core MF is GO:0031072 heat shock protein binding (ISS, ACCEPT) plus clathrin binding/clathrin heavy chain binding (GO:0030276/GO:0032050). PN projects the **narrower** GO:0030544 Hsp70 protein binding — and since auxilin binds specifically HSPA8/HSC70 (an Hsp70), GO:0030544 is in fact MORE accurate than the review's GO:0031072; GOA currently has only GO:0031072. (GO:0030544 is_a GO:0031072.)
- **PN story / NEW pressure:** GO:0030544 (verified real) is not yet in GOA or the review (which uses the parent GO:0031072). This is a legitimate **ADD** / refinement: auxilin's documented partner is HSPA8/HSC70, so the specific Hsp70 protein binding term is defensible and more informative. goa_status=more_specific_than_existing_goa is exactly right.
- **Evidence alignment:** PN carries no row references. Review/notes cite the verified uncoating literature (PMID:18489706, 20160091) + CLTC/LRRK2 (PMID:29735704). Strong, no divergence from PN.
- **Verdict:** Consistent and well-supported; PN's GO:0030544 is a defensible more-specific ADD over the review/GOA's GO:0031072. **Recommended edits:** [YAML][MAP] consider replacing/supplementing GO:0031072 heat shock protein binding with the more specific GO:0030544 Hsp70 protein binding in the review core MF (auxilin's documented partner is HSPA8/HSC70), aligning with the PN projection.

## Full Consistency Review

- **UniProt:** O75061 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch CY) ; **PN-node mapping:** type → mapped/ok_for_propagation_to_go GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa); all ancestor nodes no_mapping.
- **Consistency:** Consistent, with one MF-specificity nuance. Deep research (notes), review and PN converge on DNAJC6/auxilin as the neuronal clathrin-uncoating co-chaperone: binds clathrin cages (1 per triskelion) and, via its C-terminal J domain, recruits HSPA8/HSC70 and stimulates its ATPase to dismantle the coat; PARK19 disease gene (PMID:18489706 VERIFIED, 20160091 VERIFIED, 29735704). The review's chaperone-binding core MF is GO:0031072 heat shock protein binding (ISS, ACCEPT) plus clathrin binding/clathrin heavy chain binding (GO:0030276/GO:0032050). PN projects the **narrower** GO:0030544 Hsp70 protein binding — and since auxilin binds specifically HSPA8/HSC70 (an Hsp70), GO:0030544 is in fact MORE accurate than the review's GO:0031072; GOA currently has only GO:0031072. (GO:0030544 is_a GO:0031072.)
- **PN story / NEW pressure:** GO:0030544 (verified real) is not yet in GOA or the review (which uses the parent GO:0031072). This is a legitimate **ADD** / refinement: auxilin's documented partner is HSPA8/HSC70, so the specific Hsp70 protein binding term is defensible and more informative. goa_status=more_specific_than_existing_goa is exactly right.
- **Mapping strategy:** No change to node breadth. Unlike rejected broad cases (TOMM20/HSPA8/RAB7A), here the PN projection is *narrower and more specific* than existing GOA/review and is well-supported — a genuine refinement, not an over-reach.
- **Evidence alignment:** PN carries no row references. Review/notes cite the verified uncoating literature (PMID:18489706, 20160091) + CLTC/LRRK2 (PMID:29735704). Strong, no divergence from PN.
- **Verdict:** Consistent and well-supported; PN's GO:0030544 is a defensible more-specific ADD over the review/GOA's GO:0031072. **Recommended edits:** [YAML][MAP] consider replacing/supplementing GO:0031072 heat shock protein binding with the more specific GO:0030544 Hsp70 protein binding in the review core MF (auxilin's documented partner is HSPA8/HSC70), aligning with the PN projection.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC6/DNAJC6-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: O75061
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
