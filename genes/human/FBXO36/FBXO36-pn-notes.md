# FBXO36 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NEA4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO36/FBXO36-ai-review.yaml](FBXO36-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO36/FBXO36-ai-review.html
- Gene notes: missing - genes/human/FBXO36/FBXO36-notes.md
- GOA TSV: present - [genes/human/FBXO36/FBXO36-goa.tsv](FBXO36-goa.tsv)
- UniProt record: present - [genes/human/FBXO36/FBXO36-uniprot.txt](FBXO36-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO36.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO36.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO36.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO36.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO36/FBXO36-deep-research-falcon.md](FBXO36-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO36 (F-box only protein 36) is a small (188 aa) F-box protein that serves as a substrate-recognition component of an SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex (a Cullin-RING ligase 1, CRL1). It contains a single F-box domain (residues 91-137) through which it docks onto the adaptor SKP1, which in turn bridges to the scaffold CUL1; the catalytic RING subunit RBX1 recruits the ubiquitin-charged E2 enzyme. Within such complexes, the F-box protein contributes substrate selectivity rather than catalytic activity, directing assembly of polyubiquitin chains on bound substrates to target them for proteasomal degradation. FBXO36 belongs to the "FBXO" (F-box only, lacking recognizable C-terminal substrate-binding domains such as WD40 or LRR) class and remains very poorly characterized: no endogenous substrate, catalytic context, or subcellular localization has been experimentally validated. The strongest direct functional data come from a high-content siRNA screen of ubiquitin-pathway regulators of TNF signaling, in which FBXO36 depletion increased TNF-induced nuclear NF-kappa-B accumulation, prolonged late-stage I-kappa-B and JNK phosphorylation, sensitized cells to TNF+cycloheximide apoptosis, and raised steady-state beta-catenin levels; these phenotypes were interpreted as FBXO36 being a candidate modifier of SCF-dependent (e.g. SCF-betaTrCP) ubiquitin signaling, although no direct FBXO36 substrate was established. FBXO36 has also been noted among F-box genes with testis-enriched expression and appears in lower-confidence human genetic associations (a rare-variant lipoprotein-trait signal, lung-adenocarcinoma prognosis) that require replication. It is broadly but lowly expressed and has two annotated splice isoforms.
- Existing/core annotation action counts: ACCEPT: 2

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research (Falcon), review YAML, PN annotation, and PN-node mapping all converge on "poorly characterized FBXO-class SCF substrate receptor, no validated endogenous substrate." Review ACCEPTs the two ComplexPortal NAS annotations (GO:0019005, GO:0031146) and sets core MF = GO:1990756, matching the projected term. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic substrate-receptor role, already captured. The strongest functional lead (TNF/NF-kappaB RNAi screen; beta-catenin/SCF-betaTrCP modifier) is correctly held as UNVERIFIED, perturbation-level, no direct substrate — not promoted to a NEW term. proposed_new_terms = []. Conclusion: **already captured**; no defensible NEW term.
- **Evidence alignment:** PN cites only "15340381 / rev" (a generic F-box review citation). Review's anchor PMID is PMID:34445249 (ComplexPortal NAS) plus UniProt and Falcon leads — divergent identifiers but same family-level framing; no substrate-level evidence on either side. PN's 15340381 is not in the review references (minor divergence, both generic).
- **Verdict:** Consistent, mapping correct, no NEW pressure. ACCEPT as-is. **Recommended edits:** none.

## Full Consistency Review

- **UniProt:** Q8NEA4 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** F-box subtype/type = no_mapping (defer to parent); group "Cul1 substrate receptor" = mapped, ok_for_propagation_to_go, GO:1990756; class = context_only/too_broad (GO:0061630).
- **Consistency:** Fully consistent. Deep research (Falcon), review YAML, PN annotation, and PN-node mapping all converge on "poorly characterized FBXO-class SCF substrate receptor, no validated endogenous substrate." Review ACCEPTs the two ComplexPortal NAS annotations (GO:0019005, GO:0031146) and sets core MF = GO:1990756, matching the projected term. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic substrate-receptor role, already captured. The strongest functional lead (TNF/NF-kappaB RNAi screen; beta-catenin/SCF-betaTrCP modifier) is correctly held as UNVERIFIED, perturbation-level, no direct substrate — not promoted to a NEW term. proposed_new_terms = []. Conclusion: **already captured**; no defensible NEW term.
- **Mapping strategy:** Gene does not change the node. GO:1990756 (verified real, OLS: "ubiquitin-like ligase-substrate adaptor activity," F-box/BTB adaptors) is the correct, appropriately-scoped MF for an uncharacterized F-box receptor and matches the review core MF. Not over-broad. Mapping status/scope correct.
- **Evidence alignment:** PN cites only "15340381 / rev" (a generic F-box review citation). Review's anchor PMID is PMID:34445249 (ComplexPortal NAS) plus UniProt and Falcon leads — divergent identifiers but same family-level framing; no substrate-level evidence on either side. PN's 15340381 is not in the review references (minor divergence, both generic).
- **Verdict:** Consistent, mapping correct, no NEW pressure. ACCEPT as-is. **Recommended edits:** none.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO36/FBXO36-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q8NEA4
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: (none)
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other
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
