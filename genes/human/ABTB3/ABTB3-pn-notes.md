# ABTB3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: A6QL63
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1332)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ABTB3/ABTB3-ai-review.yaml](ABTB3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ABTB3/ABTB3-ai-review.html](ABTB3-ai-review.html)
- Gene notes: present - [genes/human/ABTB3/ABTB3-notes.md](ABTB3-notes.md)
- GOA TSV: present - [genes/human/ABTB3/ABTB3-goa.tsv](ABTB3-goa.tsv)
- UniProt record: present - [genes/human/ABTB3/ABTB3-uniprot.txt](ABTB3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ABTB3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ABTB3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABTB3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABTB3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ABTB3/ABTB3-deep-research-manual.md](ABTB3-deep-research-manual.md)

## AIGR Review Snapshot

- Description: ABTB3 encodes a conserved ankyrin repeat- and BTB/POZ domain-containing protein, also known as BTBD11. The best characterized functional evidence comes from the mouse ortholog Btbd11, which is enriched at glutamatergic postsynaptic densities in cortical and hippocampal inhibitory interneurons. Btbd11 contains a conserved C-terminal PDZ-binding motif that binds PSD-95 (DLG4), promotes PSD-95 stabilization at glutamatergic synapses, and supports excitatory synaptic input onto parvalbumin-positive interneurons. Human ABTB3 is predicted to share this synaptic scaffold/stabilizer role by orthology, but direct human functional assays and CUL3 substrate-adaptor activity have not been established.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 1; NEW: 2

## PN Consistency Summary

- **Consistency:** **CONTRADICTION (PN projection rejected by review).** The PN node projects the same Cul3-adaptor term (GO:1990756) as for paralog ABTB2, purely on BTB-BACK/ankyrin domain architecture. Deep research, notes, and review YAML all converge instead on a **synaptic scaffold/stabilizer** role: mouse ortholog Btbd11 binds PSD-95 via a C-terminal PDZ-binding motif, stabilizes PSD-95, and supports glutamatergic input onto PV interneurons (PMID:37261953). The review explicitly declines GO:1990756: "the available ABTB3/Btbd11 evidence does not show CUL3 binding, CRL3 complex membership, a ubiquitinated substrate, or substrate-adaptor activity."
- **PN story / NEW pressure:** PN asserts ubiquitin-ligase adaptor activity with **no gene-level support** for this gene — a domain-architecture inference. The actual GO captures the real biology (GO:0030165 PDZ domain binding ACCEPT; GO:0098978 glutamatergic synapse ACCEPT) and the review adds orthology-supported NEW terms GO:0050821 protein stabilization and GO:0035249 synaptic transmission, glutamatergic. The Cul3-adaptor story over-reaches and is correctly not added.
- **Evidence alignment:** PN row references (PMID:15071497, 23912815 — generic Cul3/BTB reviews) do not overlap the review's primary evidence (PMID:37261953, the Btbd11 synaptic study). Complete divergence in evidence base, reflecting the domain-only vs functional-evidence split.
- **Verdict:** PN Cul3-adaptor projection over-reaches (domain-only, contradicted by synaptic-function evidence); review correctly rejects GO:1990756. **Recommended edits:** [MAP] Suppress GO:1990756 projection for ABTB3 (no CUL3/CRL3/substrate evidence); retain the group mapping for genes with direct support (e.g. ABTB2).

## Full Consistency Review

- **UniProt:** A6QL63 (=BTBD11) · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant|ankyrin, transmembrane` ; **PN-node mapping:** group `Cul3 substrate receptor`=mapped→**GO:1990756 ubiquitin-like ligase-substrate adaptor activity** (new_to_goa); class=context_only (too_broad→GO:0061630); subtype/type/branch=no_mapping.
- **Consistency:** **CONTRADICTION (PN projection rejected by review).** The PN node projects the same Cul3-adaptor term (GO:1990756) as for paralog ABTB2, purely on BTB-BACK/ankyrin domain architecture. Deep research, notes, and review YAML all converge instead on a **synaptic scaffold/stabilizer** role: mouse ortholog Btbd11 binds PSD-95 via a C-terminal PDZ-binding motif, stabilizes PSD-95, and supports glutamatergic input onto PV interneurons (PMID:37261953). The review explicitly declines GO:1990756: "the available ABTB3/Btbd11 evidence does not show CUL3 binding, CRL3 complex membership, a ubiquitinated substrate, or substrate-adaptor activity."
- **PN story / NEW pressure:** PN asserts ubiquitin-ligase adaptor activity with **no gene-level support** for this gene — a domain-architecture inference. The actual GO captures the real biology (GO:0030165 PDZ domain binding ACCEPT; GO:0098978 glutamatergic synapse ACCEPT) and the review adds orthology-supported NEW terms GO:0050821 protein stabilization and GO:0035249 synaptic transmission, glutamatergic. The Cul3-adaptor story over-reaches and is correctly not added.
- **Mapping strategy:** This gene shows the Cul3-substrate-receptor group mapping does **not** safely propagate to all BTB-BACK-ankyrin members. GO:1990756 should be **suppressed for ABTB3** pending direct CUL3/CRL3 evidence — a per-gene exception within an otherwise valid group mapping (contrast ABTB2, where it is supported). Precedent: reject a projected term lacking gene-level support.
- **Evidence alignment:** PN row references (PMID:15071497, 23912815 — generic Cul3/BTB reviews) do not overlap the review's primary evidence (PMID:37261953, the Btbd11 synaptic study). Complete divergence in evidence base, reflecting the domain-only vs functional-evidence split.
- **Verdict:** PN Cul3-adaptor projection over-reaches (domain-only, contradicted by synaptic-function evidence); review correctly rejects GO:1990756. **Recommended edits:** [MAP] Suppress GO:1990756 projection for ABTB3 (no CUL3/CRL3/substrate evidence); retain the group mapping for genes with direct support (e.g. ABTB2).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABTB3/ABTB3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul3 substrate receptor | BTB-BACK, variant | ankyrin, transmembrane
- UniProt: A6QL63
- In branches: UPS
- Signature domains: IPR000210, IPR047824
- Auxiliary domains: IPR002110
- PN references (titles):
    - 15071497 / rev
    - 23912815 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant|ankyrin, transmembrane
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
