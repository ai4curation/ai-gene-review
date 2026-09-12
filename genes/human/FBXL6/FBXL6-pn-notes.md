# FBXL6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N531
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL6/FBXL6-ai-review.yaml](FBXL6-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL6/FBXL6-ai-review.html
- Gene notes: missing - genes/human/FBXL6/FBXL6-notes.md
- GOA TSV: present - [genes/human/FBXL6/FBXL6-goa.tsv](FBXL6-goa.tsv)
- UniProt record: present - [genes/human/FBXL6/FBXL6-uniprot.txt](FBXL6-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL6.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL6.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL6/FBXL6-deep-research-falcon.md](FBXL6-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL6 (F-box/LRR-repeat protein 6, FBL6) is a member of the FBXL subfamily of F-box proteins, characterized by an N-terminal F-box domain (residues ~10-162) followed by a C-terminal region of ~11 leucine-rich repeats (LRRs). It functions as the substrate-recognition subunit of an SCF (SKP1-CUL1-F-box) E3 ubiquitin ligase complex: the F-box domain docks the protein onto SKP1 (and through it CUL1 and the catalytic RING subunit RBX1), while the LRR region binds substrate proteins, frequently in a phosphodegron-dependent manner. FBXL6 catalyzes both degradative and non-degradative ubiquitination depending on the substrate. In hepatocellular carcinoma it promotes K48-linked degradation of phosphorylated p53 (recognizing p53 phosphorylated on Ser315 and ubiquitinating Lys291/Lys292), thereby relieving tumor-suppressive signaling, and degrades the ETS transcription factor ETV6/TEL and cyclin A2 (CCNA2). Conversely it mediates K63-linked, non-degradative ubiquitination that stabilizes or activates clients including the chaperone HSP90AA1 (sustaining c-MYC), the GTPase KRAS (ubiquitinating Lys128 to enhance RAF binding and MEK/ERK/mTOR signaling), and transketolase (TKT, recruited after VRK2 phosphorylation of Thr287, driving ROS-mTOR signaling, PD-L1 induction, and immune evasion). FBXL6 is broadly but weakly expressed across tissues (low tissue specificity) and is frequently overexpressed in hepatocellular carcinoma and acute myeloid leukemia, where it represents a tumor dependency, particularly in FLT3-ITD-mutated AML. The SCF mechanistic framework implies cytosolic and nuclear sites of action depending on substrate; explicit subcellular localization has not been firmly mapped experimentally.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review, PN annotation, and node mapping agree FBXL6 is an SCF substrate receptor. Deep research (falcon, UNVERIFIED) reports oncogenic substrates (phospho-p53, ETV6, CCNA2 degradative; HSP90AA1, KRAS, TKT non-degradative). These are not in the cache/PMID-verified, so the review correctly treats them as leads and does NOT add substrate-specific GO terms. No internal contradiction.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. GOA has catalytic `GO:0004842 (TAS, PMID:10531035)` + generic `proteolysis (TAS)` + `protein binding (SKP1)` only — no validated substrate, no SCF-process IDA. Review MODIFY's GO:0004842→GO:1990756 (verified real) and MARK_AS_OVER_ANNOTATED on generic proteolysis. Note the falcon substrates also include K63 non-degradative ubiquitination, which `GO:0031146` (proteasomal catabolism) does NOT cover — but since unverified, no new term is warranted. Conclusion: adaptor MF correctly captured; substrate functions remain inferred-only.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses PMID:10531035, 33234069 (family reviews), SKP1 interactome PMIDs, and falcon leads. No PMID overlap with the PN placeholder; divergence benign.
- **Verdict:** CONSISTENT / ACCEPT mapping (adaptor MF inferred-only). No YAML edits required. Substrate claims are appropriately held as unverified leads.

## Full Consistency Review

- **UniProt:** Q8N531 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; class `context_only / too_broad / GO:0061630`.
- **Consistency:** Consistent. Review, PN annotation, and node mapping agree FBXL6 is an SCF substrate receptor. Deep research (falcon, UNVERIFIED) reports oncogenic substrates (phospho-p53, ETV6, CCNA2 degradative; HSP90AA1, KRAS, TKT non-degradative). These are not in the cache/PMID-verified, so the review correctly treats them as leads and does NOT add substrate-specific GO terms. No internal contradiction.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. GOA has catalytic `GO:0004842 (TAS, PMID:10531035)` + generic `proteolysis (TAS)` + `protein binding (SKP1)` only — no validated substrate, no SCF-process IDA. Review MODIFY's GO:0004842→GO:1990756 (verified real) and MARK_AS_OVER_ANNOTATED on generic proteolysis. Note the falcon substrates also include K63 non-degradative ubiquitination, which `GO:0031146` (proteasomal catabolism) does NOT cover — but since unverified, no new term is warranted. Conclusion: adaptor MF correctly captured; substrate functions remain inferred-only.
- **Mapping strategy:** Gene does not change the node. **FLAG (per batch pattern): F-box member with NO validated substrate in existing_annotations — adaptor MF is inferred from family/domain, not from a curated FBXL6 substrate.** Group GO:1990756 still defensible on domain grounds (canonical F-box + SKP1 IPI). Scope/status correct.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses PMID:10531035, 33234069 (family reviews), SKP1 interactome PMIDs, and falcon leads. No PMID overlap with the PN placeholder; divergence benign.
- **Verdict:** CONSISTENT / ACCEPT mapping (adaptor MF inferred-only). No YAML edits required. Substrate claims are appropriately held as unverified leads.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL6/FBXL6-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q8N531
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
