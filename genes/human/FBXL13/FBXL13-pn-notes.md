# FBXL13 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NEE6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL13/FBXL13-ai-review.yaml](FBXL13-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL13/FBXL13-ai-review.html
- Gene notes: missing - genes/human/FBXL13/FBXL13-notes.md
- GOA TSV: present - [genes/human/FBXL13/FBXL13-goa.tsv](FBXL13-goa.tsv)
- UniProt record: present - [genes/human/FBXL13/FBXL13-uniprot.txt](FBXL13-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL13.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL13.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL13/FBXL13-deep-research-falcon.md](FBXL13-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL13 (F-box and leucine-rich repeat protein 13; also Dynein regulatory complex subunit 6, DRC6) is a multi-domain protein with an N-terminal region, an F-box domain, and an extensive C-terminal leucine-rich repeat (LRR) array. It has two distinct, tissue-dependent roles. As an SCF (SKP1-CUL1-F-box) E3 ubiquitin ligase substrate-recognition subunit, FBXL13 docks onto SKP1/CUL1 through its F-box domain and uses its LRRs to recruit substrates; it localizes to the centrosome (diffusely cytoplasmic with clear centrosomal enrichment), where it binds centrosomal proteins (Centrin-2, Centrin-3 via its N-terminus, CEP152, and CEP192 via its C-terminal region) and specifically targets CEP192 (notably the CEP192 isoform 3) for SCF/F-box-dependent polyubiquitination and proteasomal degradation, binding the N-terminal region of CEP192; the bound Centrins are not detectably degraded. By fine-tuning CEP192 abundance it downregulates centrosomal gamma-tubulin recruitment, modulates microtubule nucleation/regrowth, restrains centrosome overduplication, and promotes cell migration. Independently, in motile cilia and flagella FBXL13/DRC6 is a structural component of the nexin-dynein regulatory complex (N-DRC), a regulator of axonemal dynein activity and ciliary/flagellar beating; within the N-DRC its lysine-rich C-terminus contributes to the electrostatic distal link between neighbouring doublet microtubules. The ciliary role is less firmly established functionally: in mice Fbxl13/Drc6 knockouts show normal spermatogenesis, sperm morphology and motility and normal tracheal multicilia, suggesting the N-DRC role is dispensable or redundant under tested conditions. It is expressed broadly with enrichment in testis and stomach and in ciliated tissues.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 14

## PN Consistency Summary

- **Consistency:** Strong. Falcon deep research, review YAML, and PN node mapping agree FBXL13 is an SCF substrate receptor that degrades CEP192 at the centrosome (PMID:29348145), plus a moonlighting N-DRC/DRC6 axonemal structural role (PMID:37258679). No contradictions. The dual identity (centrosomal SCF vs ciliary structural subunit) is handled by KEEP_AS_NON_CORE on all N-DRC terms — coherent with PN's UPS-only framing.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF (GO:1990756, verified real). GOA carries NO MF term for FBXL13 at all (only BP/CC). The review adds GO:1990756 in core_functions (no existing MF to MODIFY). Not over-reaching. The ciliary structural role (GO:0005198 structural molecule activity) is a genuine second MF the PN UPS lens does not capture, but it is correctly off-mapped as non-core. Conclusion: adaptor MF appropriately ADDED; no defensible UPS NEW-term gap.
- **Evidence alignment:** PN reference is only "15340381/rev" (family placeholder, PMID:15340381). The review does not cite it; its PMIDs (29348145, 33234069, 37258679) are gene-specific and richer. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; adaptor-MF pattern correctly applied; substrate (CEP192) validated.

## Full Consistency Review

- **UniProt:** Q8NEE6 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; F-box+LRR subtype/type `no_mapping`; class `context_only / too_broad / GO:0061630`; branch `no_mapping`.
- **Consistency:** Strong. Falcon deep research, review YAML, and PN node mapping agree FBXL13 is an SCF substrate receptor that degrades CEP192 at the centrosome (PMID:29348145), plus a moonlighting N-DRC/DRC6 axonemal structural role (PMID:37258679). No contradictions. The dual identity (centrosomal SCF vs ciliary structural subunit) is handled by KEEP_AS_NON_CORE on all N-DRC terms — coherent with PN's UPS-only framing.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF (GO:1990756, verified real). GOA carries NO MF term for FBXL13 at all (only BP/CC). The review adds GO:1990756 in core_functions (no existing MF to MODIFY). Not over-reaching. The ciliary structural role (GO:0005198 structural molecule activity) is a genuine second MF the PN UPS lens does not capture, but it is correctly off-mapped as non-core. Conclusion: adaptor MF appropriately ADDED; no defensible UPS NEW-term gap.
- **Mapping strategy:** Gene does not change the node. F-box catalysis correctly excluded from sub-nodes (RBX1 RING). One caveat: CEP192 is a validated substrate, so FBXL13 is NOT an orphan adaptor — adaptor MF is experimentally grounded, not inferred-only. PN-projected GO:1990756 matches review core_functions exactly (not broader/narrower).
- **Evidence alignment:** PN reference is only "15340381/rev" (family placeholder, PMID:15340381). The review does not cite it; its PMIDs (29348145, 33234069, 37258679) are gene-specific and richer. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; adaptor-MF pattern correctly applied; substrate (CEP192) validated.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL13/FBXL13-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q8NEE6
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001611, IPR032675
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR
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
