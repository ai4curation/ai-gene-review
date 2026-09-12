# FBXO47 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5MNV8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO47/FBXO47-ai-review.yaml](FBXO47-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO47/FBXO47-ai-review.html
- Gene notes: missing - genes/human/FBXO47/FBXO47-notes.md
- GOA TSV: present - [genes/human/FBXO47/FBXO47-goa.tsv](FBXO47-goa.tsv)
- UniProt record: present - [genes/human/FBXO47/FBXO47-uniprot.txt](FBXO47-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO47.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO47.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO47.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO47.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO47/FBXO47-deep-research-falcon.md](FBXO47-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO47 (F-box only protein 47) is a 452-residue F-box-domain-containing protein (F-box at residues 41-91, plus an FBXO47-specific armadillo-like region) belonging to the FBXO ("F-box only") subfamily of F-box proteins, which canonically act as substrate-recognition receptors that, together with SKP1, CUL1 and RBX1, assemble SCF (SKP1-cullin-F-box) E3 ubiquitin ligase complexes. FBXO47 is strongly enriched in testis (HPA testis-enriched; expressed in male germline cells) and was originally cloned from a testis library. Functional studies in mouse have established FBXO47 as a germ-cell protein essential for meiotic prophase I in spermatocytes: Fbxo47-null males are infertile with spermatocytes arresting around late zygotene/pachytene, showing incomplete homologous synapsis, persistent autosomal gamma-H2AX, and failure to form XY bodies. Mechanistically, FBXO47 acts at meiotic chromosome subcompartments through SKP1-associated regulation: it localizes to the nuclear periphery and co-localizes with the shelterin component TRF2, where it promotes telomere-inner nuclear membrane attachment by stabilizing TRF2 (impairing TRF2 ubiquitination) during the bouquet stage; FBXO47 also interacts with SKP1 and the axis protein HORMAD1, contributing to HORMAD1 turnover and meiotic double-strand-break/ recombination homeostasis, and has been proposed to act in a centromeric SCF module that preserves centromeric SKP1 to support centromere pairing. Notably, several of its documented activities involve preventing rather than promoting substrate degradation (TRF2, SKP1), so its in vivo role may diverge from a classical SCF substrate receptor that drives degradation. A curated SCF E3 ligase complex variant containing FBXO47 has been recorded (ComplexPortal CPX-8006). FBXO47 maps to 17q12; human genetics associates the locus with azoospermia, and a missense variant has been reported as a candidate in autosomal recessive intellectual disability.
- Existing/core annotation action counts: KEEP_AS_NON_CORE: 1; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent with a notable tension. Deep research (Falcon: Hua 2019, Guan 2022, Ma 2024) and review YAML agree FBXO47 is a testis/germ-cell F-box protein essential for meiotic prophase I (telomere-INM/TRF2 stabilization, HORMAD1, centromere pairing), where several activities PREVENT rather than promote degradation. Review keeps SCF complex membership (GO:0019005) as KEEP_AS_NON_CORE and marks the SCF-dependent catabolism (GO:0031146) UNDECIDED — honest given conflicting stabilizing/degradative evidence. PN node projects GO:1990756 adaptor activity, which the review also uses as core MF, so they agree at the MF label even though the in vivo role is unusual.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role; the meiotic prophase biology is NOT in GOA. Review sets directly_involved_in GO:0007129 homologous chromosome pairing at meiosis (OLS-verified) and proposes a label-only NEW term for telomere-INM/bouquet attachment (no GO ID invented — candidate, unverified). Conclusion: meiotic-prophase role is real and under-captured; **ADD** GO:0007129 (in review); the bouquet/telomere-INM term is a defensible candidate but currently unverified (label only).
- **Evidence alignment:** PN cites only "15340381 / rev." Review anchors on UniProt (by-similarity) and Falcon leads (Hua/Guan/Ma, UNVERIFIED, not in cache); PMID:34445249 NAS rated LOW_QUALITY for this gene. Divergence: review carries meiotic primaries as leads; neither side has cache-verified substrate-level PMIDs.
- **Verdict:** Consistent at MF label; meiotic biology appropriately added (GO:0007129) with honest UNDECIDED on SCF catabolism. ACCEPT review. **Recommended edits:** none required; optionally [REF] verify Hua 2019 / Guan 2022 / Ma 2024 PMIDs and [YAML] convert the label-only bouquet term to a real GO ID if one exists (e.g. via OLS) before promotion.

## Full Consistency Review

- **UniProt:** Q5MNV8 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** F-box subtype/type = no_mapping; group = mapped, ok_for_propagation_to_go, GO:1990756; class = context_only/too_broad (GO:0061630).
- **Consistency:** Mostly consistent with a notable tension. Deep research (Falcon: Hua 2019, Guan 2022, Ma 2024) and review YAML agree FBXO47 is a testis/germ-cell F-box protein essential for meiotic prophase I (telomere-INM/TRF2 stabilization, HORMAD1, centromere pairing), where several activities PREVENT rather than promote degradation. Review keeps SCF complex membership (GO:0019005) as KEEP_AS_NON_CORE and marks the SCF-dependent catabolism (GO:0031146) UNDECIDED — honest given conflicting stabilizing/degradative evidence. PN node projects GO:1990756 adaptor activity, which the review also uses as core MF, so they agree at the MF label even though the in vivo role is unusual.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role; the meiotic prophase biology is NOT in GOA. Review sets directly_involved_in GO:0007129 homologous chromosome pairing at meiosis (OLS-verified) and proposes a label-only NEW term for telomere-INM/bouquet attachment (no GO ID invented — candidate, unverified). Conclusion: meiotic-prophase role is real and under-captured; **ADD** GO:0007129 (in review); the bouquet/telomere-INM term is a defensible candidate but currently unverified (label only).
- **Mapping strategy:** Gene does not force a node change, but FBXO47 is a borderline case (stabilizing/non-degradative activities; F-box "other," no firmly validated degradative substrate in vivo). GO:1990756 is acceptable as the family-level MF but the review rightly avoids asserting canonical SCF-dependent degradation. The meiotic terms are correctly kept review-local, not propagated to the broad node.
- **Evidence alignment:** PN cites only "15340381 / rev." Review anchors on UniProt (by-similarity) and Falcon leads (Hua/Guan/Ma, UNVERIFIED, not in cache); PMID:34445249 NAS rated LOW_QUALITY for this gene. Divergence: review carries meiotic primaries as leads; neither side has cache-verified substrate-level PMIDs.
- **Verdict:** Consistent at MF label; meiotic biology appropriately added (GO:0007129) with honest UNDECIDED on SCF catabolism. ACCEPT review. **Recommended edits:** none required; optionally [REF] verify Hua 2019 / Guan 2022 / Ma 2024 PMIDs and [YAML] convert the label-only bouquet term to a real GO ID if one exists (e.g. via OLS) before promotion.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO47/FBXO47-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q5MNV8
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
