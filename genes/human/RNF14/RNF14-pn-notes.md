# RNF14 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UBS8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RNF14/RNF14-ai-review.yaml](RNF14-ai-review.yaml)
- AIGR review HTML: present - [genes/human/RNF14/RNF14-ai-review.html](RNF14-ai-review.html)
- Gene notes: present - [genes/human/RNF14/RNF14-notes.md](RNF14-notes.md)
- GOA TSV: present - [genes/human/RNF14/RNF14-goa.tsv](RNF14-goa.tsv)
- UniProt record: present - [genes/human/RNF14/RNF14-uniprot.txt](RNF14-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RNF14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RNF14.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF14.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RNF14 (E3 ubiquitin-protein ligase RNF14; legacy name ARA54, androgen receptor-associated protein 54) is a cytosolic, ribosome-associated RING-in-between-RING (RBR)-type E3 ubiquitin ligase (EC 2.3.2.31). It contains an N-terminal RWD domain and a C-terminal TRIAD/RBR module (RING1, IBR, atypical RING2) and works with E2 enzymes of the UBE2D/UBE2E families. Its principal characterized function is in the RNF14-RNF25 translational quality-control pathway acting on stalled and collided ribosomes. Recruited to stalled ribosomes by the ribosome-collision sensor GCN1, RNF14 catalyzes atypical Lys-6 (K6)-linked ubiquitination of translation factors eEF1A (EEF1A1) and eRF1 (ETF1) and of ribosomal proteins, marking them for proteasomal degradation. It is specifically required to resolve reactive-aldehyde (e.g. formaldehyde)-induced RNA-protein crosslinks that stall ribosomes, by K6-ubiquitinating the crosslinked species for extraction by the VCP/p97 unfoldase and subsequent degradation. Independently of this co-translational surveillance role, RNF14 also acts in the nucleus as a transcriptional coregulator. It promotes Wnt/TCF-beta-catenin-mediated transcription via interaction with TCF7/TCF7L1/TCF7L2, and acts as a coactivator for androgen- (and to a lesser extent progesterone-) dependent transcription via interaction with the androgen receptor. It is widely expressed and undergoes RING-dependent autoubiquitination.
- Existing/core annotation action counts: ACCEPT: 27; KEEP_AS_NON_CORE: 20; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN concur: RBR-type E3 (RWD + TRIAD/RING1-IBR-RING2), GCN1-recruited, K6-linked ubiquitination of eEF1A/eRF1 on stalled ribosomes, plus reactive-aldehyde RNA-protein crosslink resolution (GO:0160127), and the AR/Wnt nuclear moonlighting role (kept non-core). The PN correctly distinguishes the **catalytic ligase MF** (GO:0061630 at the RBR group) from process. No contradictions.
- **PN story / NEW pressure:** GO:0061630 (verified real), GO:0016567 — both already in GOA + review (multiple IDA, Cys-220/Cys-417 mutagenesis). GO:0006515 (verified real) is new_to_goa; RNF14 genuinely acts in stalled-ribosome QC so it is a defensible higher-level ADD, but broader than the review's precise set (GO:0072344, GO:0085020 K6, GO:0160127, GO:0006511). Conclude: ligase MF + ubiquitination already captured; GO:0006515 defensible-but-broader ADD.
- **Evidence alignment:** PN RBR row cites "PMID 17367545 / rev" — this PMID is NOT in the review's references. Review's RQC evidence (PMID:36638793, 37651229, 37951215/16, 27863242) is HIGH/VERIFIED and richer than the PN row. Divergence: the single PN-cited RBR PMID is uncited in the review (likely an older RBR-family review; low impact since ligase MF is independently well-supported).
- **Verdict:** Fully consistent; PN ligase MF (GO:0061630) and ubiquitination already captured, GO:0006515 a defensible-but-broader ADD. No YAML change needed.

## Full Consistency Review

- **UniProt:** Q9UBS8 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE (thorough; core ligase + RQC, AR/Wnt as non-core moonlighting)
- **PN placement:** 3 rows — `Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes`; `UPS|E3 ubiquitin and UBL ligases|RBR|RWD`; `UPS|Ubiquitin and UBL binding|E3 ligase|RBR / with UBD|RWD`. **PN-node mapping:** RQC-type→mapped GO:0016567 protein ubiquitination (already_in_goa); RQC-group→GO:0006515 (new); RBR-group→mapped GO:0061630 ubiquitin protein ligase activity (already_in_goa); UBL-binding E3-group→GO:0061630 (already_in_goa); RBR/RWD subtype/type no_mapping (covered by parent). Projected: GO:0006515 (new), GO:0016567, GO:0061630×2 (all in GOA).
- **Consistency:** Excellent. Deep research, review and PN concur: RBR-type E3 (RWD + TRIAD/RING1-IBR-RING2), GCN1-recruited, K6-linked ubiquitination of eEF1A/eRF1 on stalled ribosomes, plus reactive-aldehyde RNA-protein crosslink resolution (GO:0160127), and the AR/Wnt nuclear moonlighting role (kept non-core). The PN correctly distinguishes the **catalytic ligase MF** (GO:0061630 at the RBR group) from process. No contradictions.
- **PN story / NEW pressure:** GO:0061630 (verified real), GO:0016567 — both already in GOA + review (multiple IDA, Cys-220/Cys-417 mutagenesis). GO:0006515 (verified real) is new_to_goa; RNF14 genuinely acts in stalled-ribosome QC so it is a defensible higher-level ADD, but broader than the review's precise set (GO:0072344, GO:0085020 K6, GO:0160127, GO:0006511). Conclude: ligase MF + ubiquitination already captured; GO:0006515 defensible-but-broader ADD.
- **Mapping strategy:** Correctly resolves RNF14 as the catalytic ligase (GO:0061630), not a generic UBD reader — group-level mapping appropriate; subtype/type no_mapping avoids double-counting. RQC-group→GO:0006515 broader than terms already present. No node change warranted.
- **Evidence alignment:** PN RBR row cites "PMID 17367545 / rev" — this PMID is NOT in the review's references. Review's RQC evidence (PMID:36638793, 37651229, 37951215/16, 27863242) is HIGH/VERIFIED and richer than the PN row. Divergence: the single PN-cited RBR PMID is uncited in the review (likely an older RBR-family review; low impact since ligase MF is independently well-supported).
- **Verdict:** Fully consistent; PN ligase MF (GO:0061630) and ubiquitination already captured, GO:0006515 a defensible-but-broader ADD. No YAML change needed.
- **Recommended edits:** none required. [REF] (optional) check PN-cited PMID:17367545 (RBR row) — absent from review; verify whether it adds RNF14-specific support or is a family review. [MAP] GO:0006515 broader than the exact RQC terms already annotated.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/RNF14/RNF14-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | ubiquitination of eEF1A on stalled ribosomes
- UniProt: Q9UBS8
- In branches: TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016567 protein ubiquitination]
        rationale: This PN RQC type is a specific ubiquitination bucket for eEF1A on stalled ribosomes. Protein ubiquitination is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RBR | RWD
- UniProt: Q9UBS8
- In branches: TR, UPS
- Signature domains: IPR044066
- Auxiliary domains: IPR006575
- PN references (titles):
    - 17367545 / rev
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RBR|RWD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RBR
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase | RBR / with UBD | RWD
- UniProt: Q9UBS8
- In branches: TR, UPS
- Signature domains: IPR006575
- Auxiliary domains: IPR044066
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RBR / with UBD|RWD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RBR / with UBD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group captures ubiquitin/UBL-binding factors that are E3 ligases. The shared molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0016567 protein ubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RBR
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
