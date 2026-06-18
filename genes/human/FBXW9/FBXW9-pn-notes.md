# FBXW9 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5XUX1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXW9/FBXW9-ai-review.yaml](FBXW9-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXW9/FBXW9-ai-review.html
- Gene notes: missing - genes/human/FBXW9/FBXW9-notes.md
- GOA TSV: present - [genes/human/FBXW9/FBXW9-goa.tsv](FBXW9-goa.tsv)
- UniProt record: present - [genes/human/FBXW9/FBXW9-uniprot.txt](FBXW9-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW9.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW9.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXW9/FBXW9-deep-research-falcon.md](FBXW9-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXW9 is a member of the F-box/WD40 (FBXW) family of proteins, containing an N-terminal F-box motif and a C-terminal beta-propeller built from seven WD40 repeats. F-box proteins serve as the interchangeable substrate-recognition subunits of SCF (SKP1-CUL1-F-box)-type cullin-RING E3 ubiquitin ligase complexes: the F-box motif binds SKP1 (which in turn bridges to CUL1 and the RBX1-bound catalytic RING), while the WD40 propeller engages substrate proteins and presents them for ubiquitination, marking them for proteasomal degradation. FBXW9 is itself non-catalytic: it acts as a substrate adaptor, with the ubiquitin-transfer (RING) activity contributed by RBX1 in the assembled SCF. FBXW9 has been shown experimentally to bind SKP1 (array MAPPIT screen with co-immunoprecipitation validation) and to co-purify with CUL1 in affinity purification-mass spectrometry of SCF assemblies, and ComplexPortal assigns it as the variable substrate-receptor subunit of an SCF complex variant. It is broadly expressed and undergoes N-terminal phosphorylation at several residues. FBXW9 remains poorly characterized at the level of direct biochemistry: no endogenous ubiquitination substrate has been validated by direct ubiquitination or degradation assays. Cancer-focused studies place FBXW9 transcription downstream of p53 (a direct p53 target gene) and of CREB in an IGFBP5-ROR1/HER2 signaling axis, and report cell-cycle/proliferation phenotypes on knockdown in breast cancer and invasion phenotypes in glioblastoma stem-like cells; however, candidate substrates such as TP53 remain predicted rather than biochemically demonstrated, so FBXW9's assigned molecular and process roles still rest largely on family-level inference.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 15

## PN Consistency Summary

- **Consistency:** Consistent. Deep research (falcon), review YAML, PN annotation, and node mapping all treat FBXW9 as an SCF/CRL1 substrate adaptor whose specific substrate(s) are NOT experimentally defined (TP53 is UbiBrowser-predicted only). The review is appropriately cautious: SCF membership ACCEPT, but GO:0031146 catabolic process is KEEP_AS_NON_CORE because no substrate is biochemically validated. No contradictions.
- **PN story / NEW pressure:** PN asserts the generic Cul1-receptor adaptor role. GOA currently lacks GO:1990756, so the projected term is correctly `new_to_goa`; the review proposes it under proposed_new_terms (GO:1990756, verified real via OLS). This is the flagged "member with NO validated substrate" case — adaptor activity is defensible from SKP1 binding (co-IP) + CUL1 AP-MS even without a known substrate. Conclusion: ADD GO:1990756 (already proposed by review); do not add any process/substrate term.
- **Evidence alignment:** PN cites PMID:15340381 ("/ rev", SCF family review). Review anchors on PMID:15520277 (F-box nomenclature), PMID:19159283 (array MAPPIT SKP1 + co-IP), and falcon (CUL1 AP-MS). Different family-review citations but same adaptor conclusion; no conflict.
- **Verdict:** CONSISTENT — no edits. Poorly-characterized but bona fide F-box receptor (no validated substrate); GO:1990756 ADD already proposed.

## Full Consistency Review

- **UniProt:** Q5XUX1 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40` ; **PN-node mapping:** group=mapped/ok_for_propagation_to_go GO:1990756; class=context_only/too_broad GO:0061630; subtype/type/branch=no_mapping
- **Consistency:** Consistent. Deep research (falcon), review YAML, PN annotation, and node mapping all treat FBXW9 as an SCF/CRL1 substrate adaptor whose specific substrate(s) are NOT experimentally defined (TP53 is UbiBrowser-predicted only). The review is appropriately cautious: SCF membership ACCEPT, but GO:0031146 catabolic process is KEEP_AS_NON_CORE because no substrate is biochemically validated. No contradictions.
- **PN story / NEW pressure:** PN asserts the generic Cul1-receptor adaptor role. GOA currently lacks GO:1990756, so the projected term is correctly `new_to_goa`; the review proposes it under proposed_new_terms (GO:1990756, verified real via OLS). This is the flagged "member with NO validated substrate" case — adaptor activity is defensible from SKP1 binding (co-IP) + CUL1 AP-MS even without a known substrate. Conclusion: ADD GO:1990756 (already proposed by review); do not add any process/substrate term.
- **Mapping strategy:** Correct and conservative. Group-level GO:1990756 matches the review's proposed MF; not broader/narrower. Class-level GO:0061630 correctly too_broad. No node change.
- **Evidence alignment:** PN cites PMID:15340381 ("/ rev", SCF family review). Review anchors on PMID:15520277 (F-box nomenclature), PMID:19159283 (array MAPPIT SKP1 + co-IP), and falcon (CUL1 AP-MS). Different family-review citations but same adaptor conclusion; no conflict.
- **Verdict:** CONSISTENT — no edits. Poorly-characterized but bona fide F-box receptor (no validated substrate); GO:1990756 ADD already proposed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXW9/FBXW9-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | WD40
- UniProt: Q5XUX1
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001680
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40
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
