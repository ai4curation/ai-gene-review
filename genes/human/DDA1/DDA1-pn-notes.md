# DDA1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BW61
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DDA1/DDA1-ai-review.yaml](DDA1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/DDA1/DDA1-ai-review.html
- Gene notes: missing - genes/human/DDA1/DDA1-notes.md
- GOA TSV: present - [genes/human/DDA1/DDA1-goa.tsv](DDA1-goa.tsv)
- UniProt record: present - [genes/human/DDA1/DDA1-uniprot.txt](DDA1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DDA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DDA1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDA1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/DDA1/DDA1-deep-research-falcon.md](DDA1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: DDA1 (DET1- and DDB1-associated protein 1) is a small, evolutionarily conserved subunit shared by numerous CUL4-RING (CRL4) E3 ubiquitin ligase complexes. It is an integral, core component of DCX/CRL4 complexes built on a core of DDB1, cullin-4 (CUL4A or CUL4B) and RBX1, where it functions as a scaffolding subunit that wraps around DDB1 and the substrate receptor (DCAF) to stabilize the assembled ligase and promote efficient, processive substrate ubiquitination. DDA1 is not itself a substrate receptor and does not provide the catalytic RING; rather it acts as an accessory/stabilizing module that rigidifies the complex and positions the substrate for ubiquitin transfer. It engages DDB1 with high affinity (Kd in the low-nanomolar range) through a conserved extreme N-terminal segment (approximately the first 28 residues) that docks into a groove on the BPA beta-propeller of DDB1, anchoring DDA1 within the assembled ligase. It has been structurally and biochemically characterized as part of the DDB1-DCAF15-DDA1 ligase that mediates aryl-sulfonamide (indisulam/E7820)-induced neosubstrate degradation of the splicing factor RBM39 (and its paralog RBM23), and it is also part of the DDD core complex (DET1-DDA1-DDB1) that recruits UBE2E-family E2 enzymes. DDA1 is additionally an integral, structurally resolved component of the CRL4(CSA) ligase, where it modestly stabilizes the CSA-DDB1 module and helps coordinate the ubiquitination dynamics that drive transcription-coupled nucleotide excision repair at RNA polymerase II stalled on DNA lesions. Through its presence across many CRL4 complexes DDA1 broadly supports CUL4-dependent protein polyubiquitination and proteasomal degradation, with downstream consequences for diverse substrates and pathways. It localizes to the nucleus where most CRL4 complexes act.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 8

## PN Consistency Summary

- **Consistency:** Consistent on biology — deep research, review and PN all describe DDA1 as a small shared CRL4 subunit that stabilizes the DDB1-DCAF assembly (not a receptor, not catalytic). Slight MF-vocabulary divergence: review assigns molecular_function GO:0005198 (structural molecule activity) with contributes_to GO:0061630, whereas PN maps the node to GO:0160072 (scaffold activity). No biological contradiction; both capture a non-catalytic structural/scaffolding role.
- **PN story / NEW pressure:** PN projects GO:0160072 (scaffold) as new_to_goa — confirmed absent from DDA1 GOA (goa.tsv has no MF scaffold/adaptor term). GO:0160072 is real (OLS: brings together a ubiquitin ligase and a ligase-substrate adaptor). DDA1 stabilizes/positions the DCAF receptor and the ligase, so a scaffold-class MF is defensible, though GO:0160072's exact definition (bridging ligase + adaptor) is a tighter fit for DDB1 than for the small accessory DDA1. Verdict: defensible ADD, but borderline — DDA1 is better described as a stabilizing/structural subunit than as the bridging scaffold itself.
- **Evidence alignment:** PN ref 17452440 = Pick et al. 2007 (DDD/DET1-DDA1-DDB1, UBE2E recruitment); the review cites this framework via PMID:16949367 and the falcon synthesis (Shabek 2018 structure, Schiffmacher 2024 CRL4(CSA)/TC-NER). Strong structural evidence (PMID:30564455, 31686031) underpins the stabilizing role. No conflict.
- **Verdict:** Consistent; GO:0160072 (scaffold) is a defensible-but-borderline add vs the review's GO:0005198. **Recommended edits:** [YAML] optionally add GO:0160072 to DDA1 core MF (or reconcile GO:0005198 vs GO:0160072) to align the review with the PN scaffold projection.

## Full Consistency Review

- **UniProt:** Q9BW61 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul4A/Cul4B receptor scaffold` ; **PN-node mapping:** group "Cul4A/Cul4B receptor scaffold"=mapped, ok_for_propagation, **GO:0160072** (ubiquitin ligase complex scaffold activity); projected goa_status=new_to_goa.
- **Consistency:** Consistent on biology — deep research, review and PN all describe DDA1 as a small shared CRL4 subunit that stabilizes the DDB1-DCAF assembly (not a receptor, not catalytic). Slight MF-vocabulary divergence: review assigns molecular_function GO:0005198 (structural molecule activity) with contributes_to GO:0061630, whereas PN maps the node to GO:0160072 (scaffold activity). No biological contradiction; both capture a non-catalytic structural/scaffolding role.
- **PN story / NEW pressure:** PN projects GO:0160072 (scaffold) as new_to_goa — confirmed absent from DDA1 GOA (goa.tsv has no MF scaffold/adaptor term). GO:0160072 is real (OLS: brings together a ubiquitin ligase and a ligase-substrate adaptor). DDA1 stabilizes/positions the DCAF receptor and the ligase, so a scaffold-class MF is defensible, though GO:0160072's exact definition (bridging ligase + adaptor) is a tighter fit for DDB1 than for the small accessory DDA1. Verdict: defensible ADD, but borderline — DDA1 is better described as a stabilizing/structural subunit than as the bridging scaffold itself.
- **Mapping strategy:** Node correctly distinguishes DDA1 ("receptor scaffold") from the substrate receptors (GO:1990756) and from catalysis — a good distinction. Status/scope appropriate. The review's GO:0005198 is arguably the more conservative MF; GO:0160072 leans into the scaffold framing.
- **Evidence alignment:** PN ref 17452440 = Pick et al. 2007 (DDD/DET1-DDA1-DDB1, UBE2E recruitment); the review cites this framework via PMID:16949367 and the falcon synthesis (Shabek 2018 structure, Schiffmacher 2024 CRL4(CSA)/TC-NER). Strong structural evidence (PMID:30564455, 31686031) underpins the stabilizing role. No conflict.
- **Verdict:** Consistent; GO:0160072 (scaffold) is a defensible-but-borderline add vs the review's GO:0005198. **Recommended edits:** [YAML] optionally add GO:0160072 to DDA1 core MF (or reconcile GO:0005198 vs GO:0160072) to align the review with the PN scaffold projection.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/DDA1/DDA1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B receptor scaffold
- UniProt: Q9BW61
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: (none)
- PN references (titles):
    - 17452440
- PN-node mapping records (path + ancestors):
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B receptor scaffold
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160072 ubiquitin ligase complex scaffold activity]
        rationale: This PN group captures cullin or cullin-associated scaffold roles in ubiquitin ligase complexes. The shared GO molecular-function target is ubiquitin ligase complex scaffold activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0160072 ubiquitin ligase complex scaffold activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B receptor scaffold

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
