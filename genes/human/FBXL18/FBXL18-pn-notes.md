# FBXL18 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96ME1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL18/FBXL18-ai-review.yaml](FBXL18-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL18/FBXL18-ai-review.html
- Gene notes: missing - genes/human/FBXL18/FBXL18-notes.md
- GOA TSV: present - [genes/human/FBXL18/FBXL18-goa.tsv](FBXL18-goa.tsv)
- UniProt record: present - [genes/human/FBXL18/FBXL18-uniprot.txt](FBXL18-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL18.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL18.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL18.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL18.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL18/FBXL18-deep-research-falcon.md](FBXL18-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL18 (F-box/LRR-repeat protein 18, FBL18) is a member of the FBXL subfamily of F-box proteins, with an N-terminal F-box domain followed by an extensive C-terminal leucine-rich repeat (LRR) array. It serves as the substrate-recognition subunit of a Cullin-RING (SCF; SKP1-CUL1-F-box) E3 ubiquitin ligase, docking onto SKP1/CUL1 via its F-box domain and recruiting substrates through its LRRs. FBXL18 deploys two distinct ubiquitination modes. In a degradative (K48-linked) mode it targets another F-box protein, FBXL7, for polyubiquitination and proteasomal degradation, recognizing an N-terminal FQ motif in FBXL7 and conjugating ubiquitin onto FBXL7 Lys109; because FBXL7 is pro-apoptotic, this turnover limits apoptosis. SCF^FBXL18 (reconstituted with SKP1-CUL1-RBX1) also mediates K48-linked degradation of the TFIIH subunit XPB/ERCC3 in a drug-triggered, CDK7- and XPB-Ser90-dependent manner (spironolactone-induced), thereby impairing nucleotide-excision repair and transcription and sensitizing cells to platinum agents. In a second, non-degradative (K63-linked) mode FBXL18 ubiquitinates signaling proteins to modulate their activity rather than degrade them: it promotes K63-linked ubiquitination of AKT (driving AKT-FOXO3a-Bim survival signaling in glioma and ovarian cancer) and of PTEN (inhibiting PTEN and activating PI3K/AKT in non-small-cell lung cancer), and is frequently upregulated and pro-oncogenic in these tumors. Consistent with these roles, FBXL18 has been annotated in both the cytoplasm (AKT/PTEN signaling) and the nucleus (XPB/TFIIH). It is broadly expressed with enhancement in brain.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 12

## PN Consistency Summary

- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL18 is the SCF(FBXL18) substrate receptor. Cache-verified core: K48-degradation of fellow F-box protein FBXL7 (FQ motif, Lys109; limits apoptosis — PMID:25654763, full text). Falcon adds K48 degradation of XPB/ERCC3 (reconstituted SCF^FBXL18) and a **non-degradative K63 mode** on AKT and PTEN (activating PI3K/AKT) — flagged UNVERIFIED (DOI-only leads, PTEN is a 2024 preprint). Dual-mode framing is internally consistent.
- **PN story / NEW pressure:** PN asserts generic adaptor MF (GO:1990756, verified real); GOA carries NO MF term at all (only BP/CC). Review uses GO:1990756 in core_functions (no MF to MODIFY). Correct. The K63 non-degradative mode is genuine NEW pressure not captured by GO:0031146/catabolic terms; the review handles it via a second core_function (MF still GO:1990756; BP GO:0051897 positive regulation of PI3K/AKT, verified real) rather than proposing an unverified MF — conservative and acceptable. No defensible additional real NEW GO term identified.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review uses PMID:25654763 (verified) + 33234069 (family) + falcon. Benign divergence; K63-mode primary papers not PubMed-verified in cache.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; adaptor-MF pattern correctly applied; degradative substrate (FBXL7) validated; K63 non-degradative mode noted but appropriately not over-asserted.

## Full Consistency Review

- **UniProt:** Q96ME1 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; F-box+LRR subtype/type `no_mapping`; class `context_only / too_broad / GO:0061630`; branch `no_mapping`. NB only IPR032675 auxiliary domain listed (no IPR001611), but IPR001810 F-box signature present.
- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL18 is the SCF(FBXL18) substrate receptor. Cache-verified core: K48-degradation of fellow F-box protein FBXL7 (FQ motif, Lys109; limits apoptosis — PMID:25654763, full text). Falcon adds K48 degradation of XPB/ERCC3 (reconstituted SCF^FBXL18) and a **non-degradative K63 mode** on AKT and PTEN (activating PI3K/AKT) — flagged UNVERIFIED (DOI-only leads, PTEN is a 2024 preprint). Dual-mode framing is internally consistent.
- **PN story / NEW pressure:** PN asserts generic adaptor MF (GO:1990756, verified real); GOA carries NO MF term at all (only BP/CC). Review uses GO:1990756 in core_functions (no MF to MODIFY). Correct. The K63 non-degradative mode is genuine NEW pressure not captured by GO:0031146/catabolic terms; the review handles it via a second core_function (MF still GO:1990756; BP GO:0051897 positive regulation of PI3K/AKT, verified real) rather than proposing an unverified MF — conservative and acceptable. No defensible additional real NEW GO term identified.
- **Mapping strategy:** Gene does not change the node. FBXL7 (and XPB) are validated K48 substrates → degradative adaptor MF grounded, not orphan. The K63 mode rests on unverified leads; group GO:1990756 still applies (substrate adaptor regardless of chain type). Catalysis correctly excluded from sub-nodes (RBX1 RING). Canonical SCF (reconstituted with CUL1/SKP1/RBX1) — no non-canonical flag.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review uses PMID:25654763 (verified) + 33234069 (family) + falcon. Benign divergence; K63-mode primary papers not PubMed-verified in cache.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; adaptor-MF pattern correctly applied; degradative substrate (FBXL7) validated; K63 non-degradative mode noted but appropriately not over-asserted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL18/FBXL18-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q96ME1
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR032675
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
