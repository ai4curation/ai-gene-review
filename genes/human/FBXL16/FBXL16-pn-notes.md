# FBXL16 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N461
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL16/FBXL16-ai-review.yaml](FBXL16-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL16/FBXL16-ai-review.html
- Gene notes: missing - genes/human/FBXL16/FBXL16-notes.md
- GOA TSV: present - [genes/human/FBXL16/FBXL16-goa.tsv](FBXL16-goa.tsv)
- UniProt record: present - [genes/human/FBXL16/FBXL16-uniprot.txt](FBXL16-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL16.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL16.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL16/FBXL16-deep-research-falcon.md](FBXL16-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL16 (F-box/LRR-repeat protein 16, C16orf22) is a member of the FBXL subfamily of F-box proteins, with an N-terminal (proline-rich/disordered) region, an F-box domain, and a C-terminal leucine-rich repeat (LRR) array. Its F-box motif mediates SKP1 binding, but unlike canonical F-box proteins FBXL16 shows no detectable CUL1 interaction in reported assays, suggesting it may act non-canonically rather than as a conventional SCF (SKP1-CUL1-F-box) substrate receptor. FBXL16 is a context-dependent regulator of protein stability acting in the cytoplasm, with two opposing modes: it promotes ubiquitination-dependent proteasomal degradation of some clients (e.g. the transcription factor HIF1alpha, where it limits HIF1alpha-driven epithelial-mesenchymal transition and angiogenesis as a tumor suppressor in triple-negative breast cancer, and the amyloid precursor protein APP, where neuronal/hippocampal FBXL16 reduces APP and improves cognition in Alzheimer's disease models), but it stabilizes other signaling regulators by decreasing their ubiquitination or antagonizing other ligases (e.g. IRS1, sustaining IGF1/IRS1/AKT signaling and sotorasib resistance in KRAS-mutant lung adenocarcinoma; and estrogen receptor alpha (ERalpha), c-MYC, SRC-3 and beta-catenin in ER-positive breast cancer, where it antagonizes FBXO45-mediated ERalpha degradation). Both the F-box and LRR domains are required for its substrate effects. It is expressed most highly in brain.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 12

## PN Consistency Summary

- **Consistency:** Mostly strong, with one real tension the review handles transparently. PN places FBXL16 as a canonical Cul1 substrate receptor, but falcon + review establish FBXL16 is **non-canonical**: it binds SKP1 but shows **no detectable CUL1 interaction** (Shah 2022), and acts in two opposing modes — degrading some clients (HIF1alpha PMID:34818544; APP) while **stabilizing** others (IRS1, ERalpha, c-MYC, beta-catenin, antagonizing FBXO45). Review verified-cache claim (HIF1alpha) is solid; the stabilizer mode rests on UNVERIFIED falcon DOI leads (flagged as such). Non-canonical caveat is consistently noted across description, GO:0031146 review, and core_functions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF (GO:1990756, verified real); GOA carries only `protein binding` (IPI, HIF1A). Review uses GO:1990756 in core_functions. The novel pressure is the **stabilizing/anti-degradative mode** with no GO MF — review proposes a new term "protein stabilization by inhibition of ubiquitin-dependent degradation" (candidate, UNVERIFIED — not yet a real GO ID; defensible but needs OLS/GO submission). Conclusion: degradative adaptor MF appropriately added; stabilizer activity is a genuine gap but the proposed term is a candidate, not yet real.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review uses PMID:34818544 (verified) + 33234069 (family) + falcon leads. Benign divergence; primary stabilizer-mode papers are not PubMed-verified in cache.
- **Verdict:** CONSISTENT-WITH-CAVEATS / ACCEPT degradative mapping. **Flag: non-canonical F-box (no detectable CUL1).** Proposed stabilizer term is candidate/unverified. **Recommended edits:** none to YAML [no change]; [MAP] annotate node that FBXL16 is non-canonical (SKP1+ / CUL1-negative) so GO:1990756 propagation is treated as tentative for this member.

## Full Consistency Review

- **UniProt:** Q8N461 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; F-box+LRR subtype/type `no_mapping`; class `context_only / too_broad / GO:0061630`; branch `no_mapping`. NB signature domain is IPR036047 (LRR fold), not the IPR001810 F-box used by siblings.
- **Consistency:** Mostly strong, with one real tension the review handles transparently. PN places FBXL16 as a canonical Cul1 substrate receptor, but falcon + review establish FBXL16 is **non-canonical**: it binds SKP1 but shows **no detectable CUL1 interaction** (Shah 2022), and acts in two opposing modes — degrading some clients (HIF1alpha PMID:34818544; APP) while **stabilizing** others (IRS1, ERalpha, c-MYC, beta-catenin, antagonizing FBXO45). Review verified-cache claim (HIF1alpha) is solid; the stabilizer mode rests on UNVERIFIED falcon DOI leads (flagged as such). Non-canonical caveat is consistently noted across description, GO:0031146 review, and core_functions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF (GO:1990756, verified real); GOA carries only `protein binding` (IPI, HIF1A). Review uses GO:1990756 in core_functions. The novel pressure is the **stabilizing/anti-degradative mode** with no GO MF — review proposes a new term "protein stabilization by inhibition of ubiquitin-dependent degradation" (candidate, UNVERIFIED — not yet a real GO ID; defensible but needs OLS/GO submission). Conclusion: degradative adaptor MF appropriately added; stabilizer activity is a genuine gap but the proposed term is a candidate, not yet real.
- **Mapping strategy:** Gene PARTLY strains the node. The group adaptor mapping (GO:1990756) is defensible for the degradative HIF1alpha/APP mode, but the "no CUL1 binding" finding means FBXL16 may not be a productive Cul1-SCF — flag as **non-canonical F-box** (per task brief). Adaptor MF is partly inferred (only HIF1alpha is cache-verified). Catalysis correctly excluded from sub-nodes.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review uses PMID:34818544 (verified) + 33234069 (family) + falcon leads. Benign divergence; primary stabilizer-mode papers are not PubMed-verified in cache.
- **Verdict:** CONSISTENT-WITH-CAVEATS / ACCEPT degradative mapping. **Flag: non-canonical F-box (no detectable CUL1).** Proposed stabilizer term is candidate/unverified. **Recommended edits:** none to YAML [no change]; [MAP] annotate node that FBXL16 is non-canonical (SKP1+ / CUL1-negative) so GO:1990756 propagation is treated as tentative for this member.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL16/FBXL16-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q8N461
- In branches: UPS
- Signature domains: IPR036047
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
