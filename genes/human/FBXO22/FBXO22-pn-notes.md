# FBXO22 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NEZ5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO22/FBXO22-ai-review.yaml](FBXO22-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO22/FBXO22-ai-review.html
- Gene notes: missing - genes/human/FBXO22/FBXO22-notes.md
- GOA TSV: present - [genes/human/FBXO22/FBXO22-goa.tsv](FBXO22-goa.tsv)
- UniProt record: present - [genes/human/FBXO22/FBXO22-uniprot.txt](FBXO22-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO22.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO22.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO22.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO22.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO22/FBXO22-deep-research-falcon.md](FBXO22-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO22 (F-box only protein 22, FBX22p44) is a 403-residue F-box protein that serves as the substrate-recognition receptor of a SCF (SKP1-CUL1-F-box)-type CUL1-RING E3 ubiquitin ligase complex. It binds the SCF core through an N-terminal F-box motif (residues ~21-67) that docks onto SKP1, while a C-terminal FIST-C/substrate-binding region engages target proteins; in the assembled SCF, the catalytic RING subunit RBX1 recruits the ubiquitin-charged E2, so FBXO22 itself contributes substrate selection rather than catalysis. Through this adaptor role FBXO22 directs polyubiquitination and proteasomal degradation of a defined set of substrates and thereby influences chromatin/transcriptional regulation, the DNA-damage and senescence response, oxidative-stress signaling, nutrient sensing, immune-checkpoint control, and antiviral defense. Documented substrates include the histone demethylases KDM4A/JMJD2A (controlling H3K9 and H3K36 methylation) and KDM4B (when KDM4B is complexed with tamoxifen-bound estrogen receptor, governing selective-estrogen-receptor- modulator pharmacology in breast cancer), methylated TP53 (in complex with KDM4A, at late senescence), the transcription factor BACH1 (upon oxidative-stress-induced exposure of its degron), nuclear (but not cytoplasmic) PTEN (ubiquitinated at Lys221), the immune-checkpoint ligand PD-L1 (CD274; degradation sensitizes cells to DNA-damaging therapy), the co-chaperone BAG3 (via an ERK-dependent phosphodegron, S377), the kinase MTOR (both K27-linked ubiquitination at Lys2066 upon amino-acid depletion to inhibit mTORC1, and degradation of the Ser2448-phosphorylated form), the transcription factor KLF4, and sarcomeric proteins; it also degrades the SARS-CoV-2 3C-like proteinase NSP5 via K48-linked chains to restrict viral replication. Many of these recognition events are post-translational-mark dependent (methylation marks, or phosphodegrons such as ERK-phosphorylated S377 of BAG3), consistent with a C-terminal substrate-binding region that reads modified degrons. A surface cysteine (Cys326) in the C-terminal domain can be covalently engaged by small molecules, making FBXO22 a recruitable E3 for targeted protein degradation. FBXO22 is broadly expressed with enrichment in liver and cardiac muscle and localizes to both the cytoplasm and nucleus, with its subcellular distribution modulated by EIF2AK4/GCN2-dependent phosphorylation at Thr-127. Biallelic loss-of-function causes Tayoun-Maawali syndrome (TYMAS), an autosomal-recessive multisystem developmental disorder.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 18; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep research (Falcon), UniProt, GOA, and review YAML all agree FBXO22 is the SCF/CRL1 substrate receptor (substrates KDM4A/B, methylated TP53, BACH1, nuclear PTEN K221, PD-L1, BAG3, MTOR, NSP5). Review MODIFY of GO:0004842 (TAS transferase) → GO:1990756 exactly matches the PN group target. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role, already captured by the review (core_function MF = GO:1990756, verified real, def. "Usually mediated by F-box…proteins"). The rich substrate biology vastly exceeds GOA but the review correctly declines substrate-specific NEW terms (proposed_new_terms empty). Conclusion: PN adaptor claim ALREADY CAPTURED; substrate detail belongs in core_functions, not new GO.
- **Evidence alignment:** PN cites only "15340381 / rev" (PMID:15340381, an F-box family review; not in this review's reference list). Review is anchored on substrate-specific primary papers (PMID:37979583 MTOR, PMID:39223933 NSP5) plus founding F-box papers (PMID:10531035/10531037) and PMID:34445249. Divergence: PN's single review reference is thinner than and disjoint from the review's evidence base, but both support the same adaptor framing.
- **Verdict:** CONSISTENT — no changes needed. Exemplary application of the F-box adaptor pattern.

## Full Consistency Review

- **UniProt:** Q8NEZ5 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (well-developed; ~30 annotations reviewed)
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO:1990756 (ubiquitin-like ligase-substrate adaptor activity); subtype/type/branch=no_mapping; class=context_only (GO:0061630, too_broad).
- **Consistency:** Strong. Deep research (Falcon), UniProt, GOA, and review YAML all agree FBXO22 is the SCF/CRL1 substrate receptor (substrates KDM4A/B, methylated TP53, BACH1, nuclear PTEN K221, PD-L1, BAG3, MTOR, NSP5). Review MODIFY of GO:0004842 (TAS transferase) → GO:1990756 exactly matches the PN group target. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role, already captured by the review (core_function MF = GO:1990756, verified real, def. "Usually mediated by F-box…proteins"). The rich substrate biology vastly exceeds GOA but the review correctly declines substrate-specific NEW terms (proposed_new_terms empty). Conclusion: PN adaptor claim ALREADY CAPTURED; substrate detail belongs in core_functions, not new GO.
- **Mapping strategy:** Correct. This gene does not change the node; it is the canonical exemplar of the MODIFY-catalytic-MF→GO:1990756 pattern. GO:1990756 is neither broader nor narrower than the review's chosen core MF — they are identical. Class-level GO:0061630 correctly held as context_only/too_broad.
- **Evidence alignment:** PN cites only "15340381 / rev" (PMID:15340381, an F-box family review; not in this review's reference list). Review is anchored on substrate-specific primary papers (PMID:37979583 MTOR, PMID:39223933 NSP5) plus founding F-box papers (PMID:10531035/10531037) and PMID:34445249. Divergence: PN's single review reference is thinner than and disjoint from the review's evidence base, but both support the same adaptor framing.
- **Verdict:** CONSISTENT — no changes needed. Exemplary application of the F-box adaptor pattern.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO22/FBXO22-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q8NEZ5
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
