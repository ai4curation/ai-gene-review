# FBXO8 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NRD0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO8/FBXO8-ai-review.yaml](FBXO8-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO8/FBXO8-ai-review.html
- Gene notes: missing - genes/human/FBXO8/FBXO8-notes.md
- GOA TSV: present - [genes/human/FBXO8/FBXO8-goa.tsv](FBXO8-goa.tsv)
- UniProt record: present - [genes/human/FBXO8/FBXO8-uniprot.txt](FBXO8-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO8.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO8.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO8/FBXO8-deep-research-falcon.md](FBXO8-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO8 (F-box only protein 8; also FBS, FBX8, "F-box/SEC7 protein") is a 319 aa member of the F-box "other" (FBXO) family. Through its F-box domain (residues ~68-111) it binds SKP1 and serves as the substrate-recognition subunit of an SCF (SKP1-CUL1-F-box) / CRL1 E3 ubiquitin-protein ligase complex, in which the catalytic RING subunit is RBX1; F-box proteins such as FBXO8 confer substrate specificity rather than carrying catalytic ligase activity themselves. As an SCF receptor, FBXO8 recruits target proteins for poly-ubiquitination and proteasomal degradation; documented/reported substrates include the detoxification enzyme GSTP1 (FBXO8-mediated degradation linked to suppression of colorectal cancer progression), the small GTPase ARF6 (reported ubiquitination, with consequences for cell invasion), and the oncogenic transcription factor MYC (reported in breast cancer). FBXO8 generally behaves as a tumor suppressor: it is downregulated in hepatocellular carcinoma where low expression predicts worse survival and its re-expression suppresses proliferation, migration, invasion and lung metastasis. Distinctively among F-box proteins, FBXO8 also contains a C-terminal SEC7 domain (residues ~146-276), the module that in canonical ARF guanine-nucleotide exchange factors catalyzes GDP-to-GTP exchange; for FBXO8 the available evidence is most consistent with a Sec7-like domain that mediates ARF6 binding and plasma-membrane localization rather than demonstrated GEF catalysis (loss of FBXO8 confers resistance to the trafficking inhibitor brefeldin A). Through these activities FBXO8 sits at the interface of SCF-type ubiquitination and ARF6-dependent membrane trafficking and invasion. FBXO8 is broadly expressed across human tissues.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 6

## PN Consistency Summary

- **Consistency:** Consistent. DR ↔ YAML ↔ PN agree FBXO8 is an SCF/CRL1 F-box substrate receptor; review ACCEPTs the SCF complex (GO:0019005) and SCF-dependent catabolism (GO:0031146), and uses GO:1990756 as the core MF, matching the PN projection. No contradictions; the unusual SEC7/ARF6 angle is kept non-core (predicted GEF, not demonstrated).
- **PN story / NEW pressure:** PN asserts only the family adaptor MF, which is the recurring correct call. GO:1990756 is verified real (def: "Usually mediated by F-box ... proteins"). It is NOT in GOA for FBXO8 (its only MF annotation is GO:0005085 GEF, IEA). So the adaptor MF is a defensible ADD, but note FBXO8 has NO existing catalytic ligase/transferase MF to MODIFY — GO:1990756 currently lives only in `core_functions`, not as a NEW `existing_annotation`. Validated protein substrate exists (GSTP1, PMID:31024008), so this is not a substrate-less F-box.
- **Evidence alignment:** PN cites only 15340381 (family review). Review is far richer: PMID:31024008 (GSTP1 substrate), PMID:34445249 (SCF/ComplexPortal), PMID:10945468 (cloning), plus Falcon ARF6/Sec7 leads. Divergence is expansion, not conflict.
- **Verdict:** Consistent; PN adaptor mapping (GO:1990756) appropriate and matches review core function.

## Full Consistency Review

- **UniProt:** Q9NRD0 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 ubiquitin-like ligase-substrate adaptor activity (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent. DR ↔ YAML ↔ PN agree FBXO8 is an SCF/CRL1 F-box substrate receptor; review ACCEPTs the SCF complex (GO:0019005) and SCF-dependent catabolism (GO:0031146), and uses GO:1990756 as the core MF, matching the PN projection. No contradictions; the unusual SEC7/ARF6 angle is kept non-core (predicted GEF, not demonstrated).
- **PN story / NEW pressure:** PN asserts only the family adaptor MF, which is the recurring correct call. GO:1990756 is verified real (def: "Usually mediated by F-box ... proteins"). It is NOT in GOA for FBXO8 (its only MF annotation is GO:0005085 GEF, IEA). So the adaptor MF is a defensible ADD, but note FBXO8 has NO existing catalytic ligase/transferase MF to MODIFY — GO:1990756 currently lives only in `core_functions`, not as a NEW `existing_annotation`. Validated protein substrate exists (GSTP1, PMID:31024008), so this is not a substrate-less F-box.
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 is at the right altitude (matches review core MF). Class-level GO:0061630 correctly held as too_broad.
- **Evidence alignment:** PN cites only 15340381 (family review). Review is far richer: PMID:31024008 (GSTP1 substrate), PMID:34445249 (SCF/ComplexPortal), PMID:10945468 (cloning), plus Falcon ARF6/Sec7 leads. Divergence is expansion, not conflict.
- **Verdict:** Consistent; PN adaptor mapping (GO:1990756) appropriate and matches review core function.
- **Recommended edits:** [YAML] consider adding GO:1990756 as a NEW `existing_annotation` (MF) to make the adaptor activity an explicit annotation, not only a `core_functions` entry (FBXO8 currently has no curated SCF-adaptor MF in GOA; the only MF is the IEA GEF term, kept non-core). [MAP] none.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO8/FBXO8-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q9NRD0
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
