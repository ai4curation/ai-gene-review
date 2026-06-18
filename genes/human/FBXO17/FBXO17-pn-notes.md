# FBXO17 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96EF6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO17/FBXO17-ai-review.yaml](FBXO17-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO17/FBXO17-ai-review.html
- Gene notes: missing - genes/human/FBXO17/FBXO17-notes.md
- GOA TSV: present - [genes/human/FBXO17/FBXO17-goa.tsv](FBXO17-goa.tsv)
- UniProt record: present - [genes/human/FBXO17/FBXO17-uniprot.txt](FBXO17-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO17.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO17.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO17/FBXO17-deep-research-falcon.md](FBXO17-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO17 (also FBG4, FBXO26) is a cytoplasmic F-box protein of the FBA/FBG (F-box-associated, "sugar-recognizing") lectin subfamily that also includes FBXO2, FBXO6, FBXO27 and FBXO44. It is built from an N-terminal F-box domain, which binds the adaptor SKP1 and thereby docks the protein into a canonical SCF (SKP1-CUL1-F-box, with RBX1) E3 ubiquitin-protein ligase complex, and a C-terminal FBA/G domain that functions as a carbohydrate-binding (lectin) module. Within the SCF complex FBXO17 acts as the interchangeable substrate-recognition subunit: it has no intrinsic catalytic activity, and ubiquitin transfer is carried out by an E2 enzyme recruited through the RBX1 RING subunit. The FBA/G domain uses a conserved hydrophobic pocket (the Ser-Trp pair around residues 257-258) to recognize glycans on target glycoproteins. Unlike the high-mannose-binding members FBXO2 and FBXO6, FBXO17 does not bind high-mannose glycans; instead it binds complex-type N-glycans on glycoproteins and sulfated glycans (e.g. heparin), placing it in the glycoprotein quality-control / glycoprotein catabolism arm of the ubiquitin-proteasome system. FBXO17 is expressed across several tissues with notable expression in liver, kidney, heart, skeletal muscle and brain. By selecting substrates and delivering them to the SCF machinery it contributes to SCF-dependent, proteasome-mediated protein turnover. Beyond a family-level lectin role, the best-validated FBXO17 substrate is a protein rather than a glycan: in lung epithelium SCF(FBXO17) binds and polyubiquitinates the kinase GSK3-beta (GSK3B), driving its proteasomal degradation and thereby dampening GSK3-beta-dependent pro-inflammatory cytokine production (IL-6, CXCL1). FBXO17 also has a documented non-canonical, SCF-independent mode in antiviral innate immunity: through its F-box-associated region (not its F-box) it binds the transcription factor IRF3 and recruits protein phosphatase 2A (PP2A) to promote IRF3 dephosphorylation, negatively regulating type I interferon signaling.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 10; MARK_AS_OVER_ANNOTATED: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Largely consistent, with a deliberate MF divergence. PN projects the generic adaptor MF (GO:1990756); the review instead makes GO:0030246 carbohydrate binding the core MF (NEW, IDA PMID:18203720) — correct for an FBA/lectin F-box, and a refinement of, not a contradiction with, the PN family story. DR (GSK3beta substrate, IRF3/PP2A non-canonical mode) ↔ YAML agree.
- **PN story / NEW pressure:** SPECIAL CASE re-examined. ERAD IBA (GO:0036503, verified real) is correctly MARK_AS_OVER_ANNOTATED: PMID:18203720 shows FBXO17 does NOT bind high-mannose glycans (only FBXO2/FBXO6 do GERAD), so the family ERAD propagation over-reaches — review call stands. Review ADDs GO:0030246 carbohydrate binding (verified real) — defensible, evidence-backed lectin MF absent from GOA. GO:0006516 glycoprotein catabolic process (verified real) ACCEPTed. Validated PROTEIN substrate exists (GSK3beta, Suber 2017) so not substrate-less.
- **Evidence alignment:** PN cites only 15340381. Review anchors on PMID:18203720 (HIGH, full text, the lectin/SCF characterization) plus many interactome PMIDs (all non-core protein binding) and Falcon GSK3beta/IRF3 leads (VERIFIED notes). Strong divergence in depth, no conflict.
- **Verdict:** Consistent; ERAD over-annotation call confirmed (no high-mannose binding). PN's generic GO:1990756 under-specifies the FBA lectin MF — review's GO:0030246 is the better gene-level MF.

## Full Consistency Review

- **UniProt:** Q96EF6 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|FBA` (lectin subfamily, aux domain IPR007397) ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Largely consistent, with a deliberate MF divergence. PN projects the generic adaptor MF (GO:1990756); the review instead makes GO:0030246 carbohydrate binding the core MF (NEW, IDA PMID:18203720) — correct for an FBA/lectin F-box, and a refinement of, not a contradiction with, the PN family story. DR (GSK3beta substrate, IRF3/PP2A non-canonical mode) ↔ YAML agree.
- **PN story / NEW pressure:** SPECIAL CASE re-examined. ERAD IBA (GO:0036503, verified real) is correctly MARK_AS_OVER_ANNOTATED: PMID:18203720 shows FBXO17 does NOT bind high-mannose glycans (only FBXO2/FBXO6 do GERAD), so the family ERAD propagation over-reaches — review call stands. Review ADDs GO:0030246 carbohydrate binding (verified real) — defensible, evidence-backed lectin MF absent from GOA. GO:0006516 glycoprotein catabolic process (verified real) ACCEPTed. Validated PROTEIN substrate exists (GSK3beta, Suber 2017) so not substrate-less.
- **Mapping strategy:** Gene refines the node's MF: PN's GO:1990756 is generic; for the FBA leaf the more informative MF is the lectin GO:0030246 (review) and the family adaptor role is still captured by the contributes_to GO:0061630. PN-projected GO:1990756 is broader than the review's chosen core MF — flag as the one place where PN altitude is less specific than the gene-level call.
- **Evidence alignment:** PN cites only 15340381. Review anchors on PMID:18203720 (HIGH, full text, the lectin/SCF characterization) plus many interactome PMIDs (all non-core protein binding) and Falcon GSK3beta/IRF3 leads (VERIFIED notes). Strong divergence in depth, no conflict.
- **Verdict:** Consistent; ERAD over-annotation call confirmed (no high-mannose binding). PN's generic GO:1990756 under-specifies the FBA lectin MF — review's GO:0030246 is the better gene-level MF.
- **Recommended edits:** none to FBXO17-ai-review.yaml (ERAD MARK_AS_OVER_ANNOTATED and NEW carbohydrate-binding are sound). [MAP] for the FBA subfamily, prefer GO:0030246 (lectin) as the informative MF at gene level rather than propagating the generic GO:1990756; do not propagate ERAD (GO:0036503) from the FBA node to FBXO17.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO17/FBXO17-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | FBA
- UniProt: Q96EF6
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR007397
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|FBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
