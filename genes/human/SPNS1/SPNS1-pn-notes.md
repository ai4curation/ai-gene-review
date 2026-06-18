# SPNS1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H2V7
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SPNS1/SPNS1-ai-review.yaml](SPNS1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/SPNS1/SPNS1-ai-review.html](SPNS1-ai-review.html)
- Gene notes: present - [genes/human/SPNS1/SPNS1-notes.md](SPNS1-notes.md)
- GOA TSV: present - [genes/human/SPNS1/SPNS1-goa.tsv](SPNS1-goa.tsv)
- UniProt record: present - [genes/human/SPNS1/SPNS1-uniprot.txt](SPNS1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SPNS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SPNS1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPNS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPNS1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: SPNS1 is a multi-pass lysosomal membrane protein in the major facilitator superfamily and Spinster family. Its core function is proton-gradient-dependent export of lysophospholipids, especially lysophosphatidylcholine (LPC) and lysophosphatidylethanolamine (LPE), from the lysosomal lumen to the cytosol. The exported lysophospholipids are reused in phospholipid salvage pathways and can support phosphatidylcholine synthesis, neutral-lipid storage, cholesterol homeostasis, and survival under nutrient limitation. SPNS1 deficiency causes lysosomal accumulation of LPC/LPE and related lysolipids, perturbs lysosomal function and lipid homeostasis, and is now linked to human multiorgan disease caused by biallelic loss-of-function variants.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 4; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent. Notes, review YAML and PN agree SPNS1 is a lysosomal proton-driven lysophospholipid (LPC/LPE) efflux transporter, and that "efflux of autophagy products" is biologically plausible. The review explicitly accepts the PN GO:0007041 projection as a `NEW` annotation and cites the PN mapping file. No contradictions.
- **PN story / NEW pressure:** PN asserts a lysosomal-export role not previously in GOA. GO:0007041 lysosomal transport is **verified real** (OLS: "movement into/out of/within a lysosome") and is genuinely absent from SPNS1 GOA (confirmed in goa.tsv) — the review correctly adds it as `NEW`. The review goes further with two `proposed_new_terms` (lysophospholipid:proton symporter activity; lysosomal lysophospholipid export), the right altitude for the precise cargo/direction the broad GO:0007041 misses. Conclude: **ADD GO:0007041 (done as NEW) + proposed_new_terms; defensible.**
- **Evidence alignment:** Partial overlap. PN cites the Spinster ALR/mTOR PNAS paper and a trafficking review (titles only). Review's core evidence is the direct human/mouse transporter literature (PMID:36161949, 37075117, 39739806, 40608416) — stronger, mechanism-level; the PN ALR/mTOR paper is not in review `supported_by` but is consistent.
- **Verdict:** Fully consistent; PN projection correctly actioned as NEW. No edits needed.

## Full Consistency Review

- **UniProt:** Q9H2V7 (Spinster homolog 1) · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway → Autophagic lysosome reformation → Efflux of autophagy products` (1 row, ALP) ; **PN-node mapping:** leaf group=`mapped`/`ok_for_propagation_to_go`→GO:0007041 lysosomal transport; class (ALR)=`context_only`/`too_broad`→GO:0007040; branch=`no_mapping`. **Projects GO:0007041 (new_to_goa).**
- **Consistency:** Consistent. Notes, review YAML and PN agree SPNS1 is a lysosomal proton-driven lysophospholipid (LPC/LPE) efflux transporter, and that "efflux of autophagy products" is biologically plausible. The review explicitly accepts the PN GO:0007041 projection as a `NEW` annotation and cites the PN mapping file. No contradictions.
- **PN story / NEW pressure:** PN asserts a lysosomal-export role not previously in GOA. GO:0007041 lysosomal transport is **verified real** (OLS: "movement into/out of/within a lysosome") and is genuinely absent from SPNS1 GOA (confirmed in goa.tsv) — the review correctly adds it as `NEW`. The review goes further with two `proposed_new_terms` (lysophospholipid:proton symporter activity; lysosomal lysophospholipid export), the right altitude for the precise cargo/direction the broad GO:0007041 misses. Conclude: **ADD GO:0007041 (done as NEW) + proposed_new_terms; defensible.**
- **Mapping strategy:** Gene does not change the node; GO:0007041 is appropriately broad (an over-broad "lysosomal transport" is acceptable here as the only fitting current term, and the review flags it as broad). Status/scope correct.
- **Evidence alignment:** Partial overlap. PN cites the Spinster ALR/mTOR PNAS paper and a trafficking review (titles only). Review's core evidence is the direct human/mouse transporter literature (PMID:36161949, 37075117, 39739806, 40608416) — stronger, mechanism-level; the PN ALR/mTOR paper is not in review `supported_by` but is consistent.
- **Verdict:** Fully consistent; PN projection correctly actioned as NEW. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/SPNS1/SPNS1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Efflux of autophagy products
- UniProt: Q9H2V7
- In branches: ALP
- Notes: Lysosome efflux permease that is essential for mTOR reactivation and ALR after prolonged starvation.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Spinster is required for autophagic lysosome reformation and mTOR reactivation following starvation | PNAS
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Efflux of autophagy products
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0007041 lysosomal transport]
        rationale: This PN leaf denotes export of degradation products from the autolysosome during late-stage autophagic lysosome reformation. The closest current GO process term is lysosomal transport, because the key shared semantics are transport across the lysosomal/autolysosomal membrane rather than a specific cargo chemistry.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0007041 lysosomal transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Efflux of autophagy products

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
