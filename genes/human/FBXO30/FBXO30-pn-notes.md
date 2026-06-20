# FBXO30 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8TB52
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO30/FBXO30-ai-review.yaml](FBXO30-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO30/FBXO30-ai-review.html
- Gene notes: missing - genes/human/FBXO30/FBXO30-notes.md
- GOA TSV: present - [genes/human/FBXO30/FBXO30-goa.tsv](FBXO30-goa.tsv)
- UniProt record: present - [genes/human/FBXO30/FBXO30-uniprot.txt](FBXO30-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO30.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO30.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO30.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO30.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO30/FBXO30-deep-research-falcon.md](FBXO30-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO30 (F-box only protein 30) is a 745-residue F-box "other" (FBXO) protein that serves as a substrate-recognition component of an SCF (SKP1-CUL1-F-box protein)-type, cullin-RING ligase 1 (CRL1) E3 ubiquitin ligase complex. Its C-terminal F-box domain (residues 610-658) docks onto SKP1, which together with CUL1 and the RING protein RBX1/ROC1 assembles the catalytic ligase; the catalytic ubiquitin-transfer activity resides in the RBX1/RING subunit rather than in FBXO30 itself. The N-terminal region carries a TRAF-type zinc finger (residues 48-109) whose solution structure has been determined and which is predicted to coordinate zinc as a structural feature. Within the assembled SCF complex FBXO30 selects specific substrate proteins for polyubiquitination and subsequent proteasomal degradation, with substrates that appear strongly context- and tissue-dependent. In human cells FBXO30 is predominantly cytoplasmic and has been reported to ubiquitinate retinoic acid receptor gamma (RARG), linking retinoic-acid signaling to positive regulation of BMP signaling in neural-tube development, and to promote proteasomal degradation of HIF-1A under normoxia, acting as a candidate tumor suppressor in clear-cell renal cell carcinoma. Studies of the rodent ortholog identify additional substrates, including the mitotic kinesin Eg5/KIF11 (mammary epithelial proliferation and spindle/centrosome homeostasis) and the stem-loop binding protein SLBP (oocyte meiotic chromosome condensation and segregation), and show dynamic nuclear/cytoplasmic/spindle-associated localization through the cell and meiotic cycle. By similarity, FBXO30 has also been implicated in muscle atrophy following denervation. The protein is widely but lowly expressed, is itself subject to auto-ubiquitination and possible neddylation, and a dedicated SCF complex variant (ComplexPortal CPX-7968) is annotated. Although several candidate substrates have now been reported, individual substrate-pathway links remain based on single studies and FBXO30 is still relatively poorly characterized.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 14; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep research (Falcon → RARG, HIF-1A human; Eg5/KIF11, SLBP mouse), UniProt and GOA concordant on SCF/CRL1 substrate-receptor role. Review MODIFY of GO:0061630 (InterPro IEA ubiquitin protein ligase activity) → GO:1990756 matches the PN group target precisely. TRAF-type ZnF GO:0008270 zinc binding kept non-core (structural). No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF, already captured (core_function MF = GO:1990756, verified). Falcon substrates (RARG/HIF-1A/Eg5/SLBP) are single-study leads; review correctly does NOT promote them to substrate-specific GO terms (proposed_new_terms empty). Conclusion: PN adaptor claim ALREADY CAPTURED; no defensible NEW term.
- **Evidence alignment:** PN cites only "15340381 / rev" (not in review refs). Review anchored on Falcon-sourced primary studies (Cheng 2019, Yuan 2023, Liu 2016, Jin 2019 — author-year, UNVERIFIED), the BioPlex interactome PMIDs (MYO6), and PMID:34445249. Divergence: PN reference disjoint; review's substrate evidence is lead-grade (Falcon DOIs not re-verified) but consistent with adaptor framing.
- **Verdict:** CONSISTENT — no changes needed.

## Full Consistency Review

- **UniProt:** Q8TB52 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (well-developed; relatively poorly characterized gene)
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|TRAF-type ZnF` (aux domain IPR001293) ; **PN-node mapping:** group=mapped GO:1990756; subtype/type/branch=no_mapping; class=context_only (GO:0061630).
- **Consistency:** Strong. Deep research (Falcon → RARG, HIF-1A human; Eg5/KIF11, SLBP mouse), UniProt and GOA concordant on SCF/CRL1 substrate-receptor role. Review MODIFY of GO:0061630 (InterPro IEA ubiquitin protein ligase activity) → GO:1990756 matches the PN group target precisely. TRAF-type ZnF GO:0008270 zinc binding kept non-core (structural). No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF, already captured (core_function MF = GO:1990756, verified). Falcon substrates (RARG/HIF-1A/Eg5/SLBP) are single-study leads; review correctly does NOT promote them to substrate-specific GO terms (proposed_new_terms empty). Conclusion: PN adaptor claim ALREADY CAPTURED; no defensible NEW term.
- **Mapping strategy:** Correct; gene does not change the node. GO:1990756 equals the review's core MF. The catalytic-ligase IEA (GO:0061630) is exactly the over-propagation the F-box pattern predicts, correctly MODIFIED here. Note GO:0061630 also appears as the class-level context_only target — at the gene level it is properly demoted, not propagated.
- **Evidence alignment:** PN cites only "15340381 / rev" (not in review refs). Review anchored on Falcon-sourced primary studies (Cheng 2019, Yuan 2023, Liu 2016, Jin 2019 — author-year, UNVERIFIED), the BioPlex interactome PMIDs (MYO6), and PMID:34445249. Divergence: PN reference disjoint; review's substrate evidence is lead-grade (Falcon DOIs not re-verified) but consistent with adaptor framing.
- **Verdict:** CONSISTENT — no changes needed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO30/FBXO30-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | TRAF-type ZnF
- UniProt: Q8TB52
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001293
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|TRAF-type ZnF
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
