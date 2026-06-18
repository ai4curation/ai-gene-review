# LMAN1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P49257
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/LMAN1/LMAN1-ai-review.yaml](LMAN1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/LMAN1/LMAN1-ai-review.html
- Gene notes: present - [genes/human/LMAN1/LMAN1-notes.md](LMAN1-notes.md)
- GOA TSV: present - [genes/human/LMAN1/LMAN1-goa.tsv](LMAN1-goa.tsv)
- UniProt record: present - [genes/human/LMAN1/LMAN1-uniprot.txt](LMAN1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/LMAN1/LMAN1-deep-research-falcon.md](LMAN1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: LMAN1 (Protein ERGIC-53; also Gp58, MR60, lectin mannose-binding 1) is a 510-residue type I single-pass transmembrane L-type (leguminous-type) lectin of the early secretory pathway. Its luminal carbohydrate-recognition domain binds high-mannose N-glycans in a calcium-dependent manner, making it a mannose-specific lectin (identical to the myelomonocytic lectin MR60); it is not a glycosidase and has no catalytic activity. ERGIC-53 cycles between the endoplasmic reticulum, the ER-Golgi intermediate compartment (ERGIC) and the cis-Golgi, exiting the ER in COPII-coated vesicles and returning by COPI-dependent retrograde traffic via a C-terminal dilysine/diphenylalanine motif. Together with its soluble co-receptor MCFD2 it forms an oligomeric cargo receptor (the LMAN1-MCFD2 complex; full-length cryo-EM resolves a disulfide-linked homotetramer, revising older homohexamer models) that selectively captures glycoprotein cargo in the ER and transports it to the Golgi; its best characterized cargoes are coagulation factors V and VIII, and additional secretory glycoproteins (e.g. alpha-1-antitrypsin, cathepsins) have been proposed. As an abundant, rapidly cycling cargo receptor ERGIC-53 also contributes, together with Surf4 and p24 family members, to maintaining the architecture of the ERGIC and Golgi by controlling COPI recruitment. Loss-of-function mutations in LMAN1 cause autosomal recessive combined deficiency of factors V and VIII (F5F8D1).
- Existing/core annotation action counts: ACCEPT: 39; KEEP_AS_NON_CORE: 19; MARK_AS_OVER_ANNOTATED: 8

## PN Consistency Summary

- **Consistency:** Deep research ↔ review ↔ PN annotation are internally consistent on identity: LMAN1 is correctly an L-type lectin cargo receptor (D-mannose binding GO:0005537), NOT a glycosidase/mannosidase — exactly matching the PN "Lectin chaperone" type. Review core = D-mannose binding + ER→Golgi transport (GO:0006888) of FV/FVIII via the LMAN1-MCFD2 cargo-receptor complex (GO:0062137). No contradictions.
- **PN story / NEW pressure:** No NEW GO pressure. The lectin/cargo-receptor functions are fully captured in existing GOA. Falcon additions (cryo-EM tetramer PMID:38493152, TPO cargo PMID:39499573, KKFF motif PMID:36594468) refine but do not require new terms. Conclude: already captured.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review evidence is extensive and PubMed-verified (PMID:12717434, 16304051, 36490287, 24498414, etc.). No shared-citation conflict; the divergence is conceptual (group GO term vs. lectin function), not bibliographic.
- **Verdict:** Review strong and PN-consistent on identity (lectin, not mannosidase). PN node correct to leave "Lectin chaperone" unmapped; the inherited group→GO:0006487 projection is an over-reach for a glycan-reader.

## Full Consistency Review

- **UniProt:** P49257 (Protein ERGIC-53 / MR60) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE, very thorough (~80 annotations; detailed notes + Falcon).
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** type "Lectin chaperone" no_mapping; group "N-glycosylation system" mapped→GO:0006487 (protein N-linked glycosylation, ok_for_propagation, new_to_goa); class/branch no_mapping.
- **Consistency:** Deep research ↔ review ↔ PN annotation are internally consistent on identity: LMAN1 is correctly an L-type lectin cargo receptor (D-mannose binding GO:0005537), NOT a glycosidase/mannosidase — exactly matching the PN "Lectin chaperone" type. Review core = D-mannose binding + ER→Golgi transport (GO:0006888) of FV/FVIII via the LMAN1-MCFD2 cargo-receptor complex (GO:0062137). No contradictions.
- **PN story / NEW pressure:** No NEW GO pressure. The lectin/cargo-receptor functions are fully captured in existing GOA. Falcon additions (cryo-EM tetramer PMID:38493152, TPO cargo PMID:39499573, KKFF motif PMID:36594468) refine but do not require new terms. Conclude: already captured.
- **Mapping strategy:** **The group projection GO:0006487 (protein N-linked glycosylation) over-reaches for LMAN1.** LMAN1 *reads* high-mannose N-glycans as a cargo receptor; it neither installs (GO:0006487 = attachment via Asn N4) nor processes/trims them. Marked `new_to_goa` — i.e. it would be a brand-new, unsupported assertion. The "N-glycosylation system" group conflates installers (OST), processors (MAN1B1/EDEM) and readers (lectins) under one biosynthesis term that only describes installation. Like the TOMM20/HSPA8/RAB7A precedents, this projected term is broader/wrong-branch relative to the review's actual function and should not propagate to LMAN1.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review evidence is extensive and PubMed-verified (PMID:12717434, 16304051, 36490287, 24498414, etc.). No shared-citation conflict; the divergence is conceptual (group GO term vs. lectin function), not bibliographic.
- **Verdict:** Review strong and PN-consistent on identity (lectin, not mannosidase). PN node correct to leave "Lectin chaperone" unmapped; the inherited group→GO:0006487 projection is an over-reach for a glycan-reader.
**Recommended edits:** [MAP] Do not propagate GO:0006487 (protein N-linked glycosylation) to LMAN1 from the "N-glycosylation system" group — LMAN1 binds/transports high-mannose glycoproteins, it does not perform N-linked glycosylation; flag the group node as over-broad (mixes installers/processors/readers).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/LMAN1/LMAN1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: P49257
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone
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

## Projected GO annotations (1)
- GO:0006487 protein N-linked glycosylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
