# FBXO25 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8TCJ0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO25/FBXO25-ai-review.yaml](FBXO25-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO25/FBXO25-ai-review.html
- Gene notes: missing - genes/human/FBXO25/FBXO25-notes.md
- GOA TSV: present - [genes/human/FBXO25/FBXO25-goa.tsv](FBXO25-goa.tsv)
- UniProt record: present - [genes/human/FBXO25/FBXO25-uniprot.txt](FBXO25-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO25.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO25.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO25/FBXO25-deep-research-falcon.md](FBXO25-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO25 (F-box only protein 25, FBX25) is a member of the FBXO ("F-box only") class of F-box proteins. It serves as a substrate-recognition (adaptor) subunit of a SKP1-CUL1-F-box (SCF)-type E3 ubiquitin-protein ligase complex, in which it assembles with SKP1, CUL1 and the catalytic RING subunit RBX1. The C-terminal F-box motif mediates binding to SKP1 (an atypical serine in the F-box, Ser244, is required for this interaction), thereby linking specific substrates to the cullin-RING catalytic core for ubiquitination and proteasomal degradation; FBXO25 itself does not possess the catalytic ubiquitin-transfer activity, which resides in the RING/E2 module. FBXO25 is broadly expressed with notable expression in brain and testis, and a region in its N-terminus binds beta-actin. The protein localizes to the nucleus where it concentrates in discrete SKP1-colocalized subnuclear (dot-like) domains termed FBXO25-associated nuclear domains (FANDs) that co-localize with the proteasome and ubiquitinated proteins (their integrity depends on actin polymerization and RNA polymerase I activity), and is excluded from the nucleolus. Its best-validated endogenous substrate is the ETS transcription factor ELK-1: SCF(FBXO25) binds ELK-1 and promotes its ubiquitination and proteasome-dependent degradation, dampening mitogen-induced ELK-1 target genes such as c-fos and egr-1. FBXO25 has also been reported to promote histone H2B K120 monoubiquitination (with downstream H3K4me3 and activation of the osteogenic factor OSX/SP7) during osteogenic differentiation, and other reported substrate/process associations (HAX1, NRF1/NFE2L1, and handling of expanded-polyglutamine huntingtin) point to roles in SCF-dependent protein turnover, but most of these remain thinly characterized. A chromosomal translocation disrupting FBXO25 has been linked to X-linked intellectual disability, and the gene has been associated with ADHD-related phenotypes and cardiomyocyte hypertrophy in model systems.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 6; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep research (Falcon → ELK-1 as best-validated substrate; FAND nuclear puncta; H2BK120ub/osteogenesis), UniProt, GOA and review all concordant. Review MODIFY of GO:0004842 (NAS transferase, PMID:10531035) → GO:1990756 matches the PN group target. NOT-nucleolus IDA (PMID:16278047) correctly accepted. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF, already captured (core_function MF = GO:1990756, verified). ELK-1 substrate and FAND compartment exceed GOA but review correctly keeps them as core_function descriptions without proposing substrate-specific NEW terms (proposed_new_terms empty). Conclusion: PN adaptor claim ALREADY CAPTURED.
- **Evidence alignment:** PN cites only "15340381 / rev" (not in review refs). Review anchored on the FBXO25 characterization paper (PMID:16278047), the founding family paper (PMID:10531035), and PMID:34445249, with Falcon supplying ELK-1. Divergence: PN reference disjoint from and thinner than review's; both support adaptor framing.
- **Verdict:** CONSISTENT — no changes needed.

## Full Consistency Review

- **UniProt:** Q8TCJ0 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (well-developed; 3 isoforms tracked)
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** group=mapped GO:1990756; subtype/type/branch=no_mapping; class=context_only (GO:0061630).
- **Consistency:** Strong. Deep research (Falcon → ELK-1 as best-validated substrate; FAND nuclear puncta; H2BK120ub/osteogenesis), UniProt, GOA and review all concordant. Review MODIFY of GO:0004842 (NAS transferase, PMID:10531035) → GO:1990756 matches the PN group target. NOT-nucleolus IDA (PMID:16278047) correctly accepted. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF, already captured (core_function MF = GO:1990756, verified). ELK-1 substrate and FAND compartment exceed GOA but review correctly keeps them as core_function descriptions without proposing substrate-specific NEW terms (proposed_new_terms empty). Conclusion: PN adaptor claim ALREADY CAPTURED.
- **Mapping strategy:** Correct; gene does not change the node. GO:1990756 equals the review's core MF (not broader/narrower). Note FBXO25 has a real cytoplasm IBA the review downgraded to non-core (experimental localization is nuclear) — does not affect the MF mapping.
- **Evidence alignment:** PN cites only "15340381 / rev" (not in review refs). Review anchored on the FBXO25 characterization paper (PMID:16278047), the founding family paper (PMID:10531035), and PMID:34445249, with Falcon supplying ELK-1. Divergence: PN reference disjoint from and thinner than review's; both support adaptor framing.
- **Verdict:** CONSISTENT — no changes needed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO25/FBXO25-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q8TCJ0
- In branches: UPS
- Signature domains: IPR036047
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
