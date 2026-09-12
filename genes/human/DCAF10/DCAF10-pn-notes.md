# DCAF10 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5QP82
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DCAF10/DCAF10-ai-review.yaml](DCAF10-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DCAF10/DCAF10-ai-review.html](DCAF10-ai-review.html)
- Gene notes: present - [genes/human/DCAF10/DCAF10-notes.md](DCAF10-notes.md)
- GOA TSV: present - [genes/human/DCAF10/DCAF10-goa.tsv](DCAF10-goa.tsv)
- UniProt record: present - [genes/human/DCAF10/DCAF10-uniprot.txt](DCAF10-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DCAF10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DCAF10.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DCAF10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DCAF10.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DCAF10 (DDB1- and CUL4-associated factor 10; also known as WD repeat-containing protein 32, WDR32) is a WD40-repeat protein predicted to fold into a beta-propeller. It is a member of the DCAF family of substrate-recognition receptors that dock onto the DDB1 adaptor of CRL4 (DDB1-CUL4-RBX1) cullin-RING E3 ubiquitin ligase complexes via a conserved WD40 surface. By analogy to other DCAFs, DCAF10 is thought to present specific substrates to the CRL4 ligase for ubiquitination, but it remains poorly characterized experimentally and no broadly validated endogenous substrate is established. Direct biochemical evidence supports its association with DDB1/CUL4, and it is defined as a component of CRL4-DCAF10 complexes (CUL4A and CUL4B variants). A single study in esophageal squamous cell carcinoma proposes that a CUL4A-DDB1-DCAF10 complex, stabilized by the deubiquitinase OTUD1, promotes degradation of the anti-apoptotic protein MCL1, but this substrate link has not been independently replicated. The N-terminal region is disordered and carries several phosphoserine and methylarginine sites identified in large-scale proteomics, with no functional characterization.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 8; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Consistent. Deep-research notes, review, and PN all describe DCAF10 as a poorly characterized (Pharos Tdark) WD40 substrate-recognition receptor that docks DDB1 of CRL4 via WDxR; direct evidence limited to DDB1/CUL4 co-purification (PMID:16949367, IDA/NAS); only proposed substrate is MCL1 from a single non-replicated ESCC/OTUD1 study (PMID:33898171). No contradictions.
- **PN story / NEW pressure:** Genuine ADD pressure. The review's core_function for DCAF10 carries NO molecular_function term (only a complex-membership description) and the existing GOA has no MF beyond bare protein binding (all MARK_AS_OVER_ANNOTATED). PN's projected GO:1990756 (verified real via OLS) is exactly the substrate-adaptor MF this receptor should carry by analogy with the DCAF family and is defensible even for a Tdark gene given direct DDB1/CUL4 association. Recommend ADD as inferred (ISS/IBA-style) MF. Distinct from COP1: DCAF10 is a pure substrate-adaptor (no catalytic RING) → GO:1990756, NOT GO:0061630.
- **Evidence alignment:** PN cites 17588513 (DCAF discovery review). Review's key gene-specific evidence is PMID:16949367 (founding DCAF paper) and PMID:33898171 (MCL1). Partial conceptual overlap (both family-level), no direct PMID match.
- **Verdict:** Consistent; mapping sound. NEW MF pressure is real and defensible — GO:1990756 should be added to the review.

## Full Consistency Review

- **UniProt:** Q5QP82 (WDR32) · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other` ; **PN-node mapping:** group node `Cul4A/Cul4B substrate receptor` mapped → GO:1990756 ubiquitin-like ligase-substrate adaptor activity (ok_for_propagation, new_to_goa); class context_only (GO:0061630, too_broad).
- **Consistency:** Consistent. Deep-research notes, review, and PN all describe DCAF10 as a poorly characterized (Pharos Tdark) WD40 substrate-recognition receptor that docks DDB1 of CRL4 via WDxR; direct evidence limited to DDB1/CUL4 co-purification (PMID:16949367, IDA/NAS); only proposed substrate is MCL1 from a single non-replicated ESCC/OTUD1 study (PMID:33898171). No contradictions.
- **PN story / NEW pressure:** Genuine ADD pressure. The review's core_function for DCAF10 carries NO molecular_function term (only a complex-membership description) and the existing GOA has no MF beyond bare protein binding (all MARK_AS_OVER_ANNOTATED). PN's projected GO:1990756 (verified real via OLS) is exactly the substrate-adaptor MF this receptor should carry by analogy with the DCAF family and is defensible even for a Tdark gene given direct DDB1/CUL4 association. Recommend ADD as inferred (ISS/IBA-style) MF. Distinct from COP1: DCAF10 is a pure substrate-adaptor (no catalytic RING) → GO:1990756, NOT GO:0061630.
- **Mapping strategy:** Correct. Group-level GO:1990756 is appropriate (substrate receptor, not catalytic), class-level GO:0061630 correctly held as too_broad. Projected term is neither broader nor narrower than warranted — it is the precise missing MF. No mapping change; this gene strengthens the node.
- **Evidence alignment:** PN cites 17588513 (DCAF discovery review). Review's key gene-specific evidence is PMID:16949367 (founding DCAF paper) and PMID:33898171 (MCL1). Partial conceptual overlap (both family-level), no direct PMID match.
- **Verdict:** Consistent; mapping sound. NEW MF pressure is real and defensible — GO:1990756 should be added to the review.
- **Recommended edits:** Add GO:1990756 (ubiquitin-like ligase-substrate adaptor activity) as the molecular_function on DCAF10's core_function, inferred by homology/DCAF-family membership. [YAML]

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/DCAF10/DCAF10-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | WD40 | other
- UniProt: Q5QP82
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN references (titles):
    - 17588513 rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
