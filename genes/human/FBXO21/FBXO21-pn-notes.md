# FBXO21 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O94952
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO21/FBXO21-ai-review.yaml](FBXO21-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO21/FBXO21-ai-review.html
- Gene notes: missing - genes/human/FBXO21/FBXO21-notes.md
- GOA TSV: present - [genes/human/FBXO21/FBXO21-goa.tsv](FBXO21-goa.tsv)
- UniProt record: present - [genes/human/FBXO21/FBXO21-uniprot.txt](FBXO21-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO21.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO21.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO21.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO21.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO21/FBXO21-deep-research-falcon.md](FBXO21-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO21 (FBX21, KIAA0875; also reported as SIP/FBXO3B) is a 628-residue F-box protein that serves as the substrate-recognition subunit of a multi-subunit SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Through its N-terminal F-box domain (residues 28-84) it binds SKP1, coupling to CUL1 and the catalytic RING subunit RBX1, while its central and C-terminal regions provide substrate specificity. The best-characterized substrate is EID1 (EP300-interacting inhibitor of differentiation 1): FBXO21 binds the C-terminal region of EID1 and SCF(FBXO21) directly ubiquitylates EID1 to drive its proteasomal degradation predominantly in the cytoplasm (EID1 accumulates in both cytoplasm and nucleus upon FBXO21 loss), thereby influencing EID1-dependent transcriptional repression; a peptidic modular degron in EID1 is necessary and sufficient for SCF(FBXO21)-dependent polyubiquitylation. FBXO21 operates in two mechanistic modes. In the canonical proteolytic mode it directs K48-type proteasomal degradation of substrates including EID1, the PI3K regulatory subunit p85alpha (PIK3R1; degradation in acute myeloid leukemia shapes PI3K/AKT versus ERK signaling and AML cell survival/differentiation), and the multidrug-resistance transporter ABCB1/P-glycoprotein (whose turnover is blocked by Ser291-phosphorylated CD44). In a non-proteolytic signaling mode, SCF(FBXO21) catalyzes Lys29-linked ubiquitination of the kinase ASK1 (MAP3K5) that promotes ASK1 activation rather than degradation, driving ASK1-JNK/p38 and IRF3-dependent antiviral innate immune signaling and type I interferon (IFN-beta) and IL-6 induction after viral or nucleic-acid challenge. As an SCF adaptor, FBXO21 thus acts in the ubiquitin-proteasome system to mediate ubiquitin-dependent, SCF-type protein catabolism and, via atypical chain linkages, ubiquitin-dependent signal transduction. It is broadly expressed (tissue-enhanced in fallopian tube).
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 16; MODIFY: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review executes the canonical pattern: NAS GO:0004842 transferase MODIFY → GO:1990756 (verified real), matching the PN projection; REMOVEs a spurious IEA GO:0003677 DNA binding (YccV/IPR011722 fold artifact). DR ↔ YAML agree on EID1 (validated, PMID:26085330) plus ASK1/p85alpha/ABCB1 leads.
- **PN story / NEW pressure:** PN asserts the adaptor MF; review supplies it via MODIFY — already captured/improved, not over-reach. Extra biology beyond PN: non-proteolytic Lys29 ubiquitination of ASK1 driving innate-immune/IFN signaling (core_function directly_involved_in GO:0045087), and p85alpha/AML degradation — these go beyond simple catabolism but are anchored on the validated EID1 work plus Falcon leads. No additional verified NEW GO term needed beyond GO:1990756. Validated substrate (EID1) present — not substrate-less.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:26085330 (EID1, HIGH), 10531035 (family cloning, source of transferase NAS), 34445249 (SCF), interactome PMIDs (non-core), plus Falcon ASK1/p85alpha/ABCB1 leads. Expansion, no conflict.
- **Verdict:** Consistent; review implements PN adaptor mapping via MODIFY GO:0004842→GO:1990756 and correctly REMOVEs the IEA DNA-binding artifact.

## Full Consistency Review

- **UniProt:** O94952 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent. Review executes the canonical pattern: NAS GO:0004842 transferase MODIFY → GO:1990756 (verified real), matching the PN projection; REMOVEs a spurious IEA GO:0003677 DNA binding (YccV/IPR011722 fold artifact). DR ↔ YAML agree on EID1 (validated, PMID:26085330) plus ASK1/p85alpha/ABCB1 leads.
- **PN story / NEW pressure:** PN asserts the adaptor MF; review supplies it via MODIFY — already captured/improved, not over-reach. Extra biology beyond PN: non-proteolytic Lys29 ubiquitination of ASK1 driving innate-immune/IFN signaling (core_function directly_involved_in GO:0045087), and p85alpha/AML degradation — these go beyond simple catabolism but are anchored on the validated EID1 work plus Falcon leads. No additional verified NEW GO term needed beyond GO:1990756. Validated substrate (EID1) present — not substrate-less.
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 at correct altitude (= review's MODIFY target). Class GO:0061630 too_broad. The signaling/innate-immune dimension is captured in core_functions, not via the PN UPS node — appropriate.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:26085330 (EID1, HIGH), 10531035 (family cloning, source of transferase NAS), 34445249 (SCF), interactome PMIDs (non-core), plus Falcon ASK1/p85alpha/ABCB1 leads. Expansion, no conflict.
- **Verdict:** Consistent; review implements PN adaptor mapping via MODIFY GO:0004842→GO:1990756 and correctly REMOVEs the IEA DNA-binding artifact.
- **Recommended edits:** none to FBXO21-ai-review.yaml. [MAP] none — node mapping and review concur.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO21/FBXO21-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: O94952
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
