# SEC62 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q99442
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SEC62/SEC62-ai-review.yaml](SEC62-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SEC62/SEC62-ai-review.html
- Gene notes: present - [genes/human/SEC62/SEC62-notes.md](SEC62-notes.md)
- GOA TSV: present - [genes/human/SEC62/SEC62-goa.tsv](SEC62-goa.tsv)
- UniProt record: present - [genes/human/SEC62/SEC62-uniprot.txt](SEC62-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SEC62.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SEC62.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SEC62.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SEC62.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SEC62/SEC62-deep-research-falcon.md](SEC62-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SEC62 (also TLOC1, translocation protein 1) is a multi-pass endoplasmic reticulum membrane protein and an auxiliary component of the Sec61 translocon. Together with SEC63 it forms the SEC62-SEC63 complex that promotes translocation of precursor polypeptides into the ER, with a particular role in the post-translational import of small presecretory proteins bearing short, weakly hydrophobic signal peptides. SEC62 acts as a membrane targeting receptor that positions newly synthesized precursors into the Sec61 channel and helps trigger channel opening for translocation into the ER lumen. SEC62 has two transmembrane helices with N- and C-terminal cytoplasmic domains and interacts with the translocon core (e.g. SEC61B). In addition to its translocation role, SEC62 functions as a receptor in recovery-phase ER-phagy (reticulophagy), interacting with autophagy LC3/GABARAP-family proteins to mediate selective degradation of ER following stress. SEC62 is broadly expressed and is amplified in several cancers.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research, notes, and review YAML all describe SEC62 as a Sec61-translocon-associated targeting receptor for small presecretory proteins (post-translational import) plus a recovery-phase ER-phagy receptor (GABARAP/LC3). PN's three rows (translocon component, ERphagy receptor, microreticulophagy) map cleanly onto the review's translocation core + non-core reticulophagy. No contradictions.
- **PN story / NEW pressure:** PN's two roles are already in GOA/review. Translocon: review has GO:0031204, GO:0006620, GO:0008320, GO:0015031. ERphagy: review keeps GO:0061709 (KEEP_AS_NON_CORE). The one PN-projected term absent from GOA is GO:0005784 Sec61 translocon complex (verified real; definition explicitly admits translocon-associated/TRAP proteins, so SEC62 qualifies). Defensible ADD as a CC. Conclude: ADD GO:0005784 (translocon-associated, not channel-core); ERphagy/transport already captured.
- **Evidence alignment:** Excellent overlap. PN row 2 titles ("Translocon component Sec62 acts in ER turnover during stress recovery"; "Selective Autophagy: ATG8...LIR...Cargo Receptors") match the review's reticulophagy framing (review cites PMID:31006538). Translocon evidence (PMID:22375059, 29719251, 32133789) is review-only but congruent. No divergence.
- **Verdict:** CONSISTENT. One actionable gap: add Sec61 translocon complex CC.

## Full Consistency Review

- **UniProt:** Q99442 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|SEC61 channel complex component`; also `ALP|Autophagy substrate selection|Selective autophagy receptor|ERphagy` and `ALP|Microautophagy|Microreticulophagy`; **PN-node mapping:** group mapped, ok_for_propagation_to_go, GO:0005784 (Sec61 translocon complex); class GO:0015031 (protein transport); ERphagy type mapped GO:0061709 (reticulophagy); microreticulophagy = context_only/too_broad.
- **Consistency:** Strong agreement. Deep research, notes, and review YAML all describe SEC62 as a Sec61-translocon-associated targeting receptor for small presecretory proteins (post-translational import) plus a recovery-phase ER-phagy receptor (GABARAP/LC3). PN's three rows (translocon component, ERphagy receptor, microreticulophagy) map cleanly onto the review's translocation core + non-core reticulophagy. No contradictions.
- **PN story / NEW pressure:** PN's two roles are already in GOA/review. Translocon: review has GO:0031204, GO:0006620, GO:0008320, GO:0015031. ERphagy: review keeps GO:0061709 (KEEP_AS_NON_CORE). The one PN-projected term absent from GOA is GO:0005784 Sec61 translocon complex (verified real; definition explicitly admits translocon-associated/TRAP proteins, so SEC62 qualifies). Defensible ADD as a CC. Conclude: ADD GO:0005784 (translocon-associated, not channel-core); ERphagy/transport already captured.
- **Mapping strategy:** Mapping is sound. GO:0005784 is appropriately specific (the dossier's `more_specific_than_existing_goa` is correct — GOA has only ER membrane/rough ER/ER). GO:0015031 protein transport is a defensibly broad class-level target (not over-reaching like the TOMM20/HSPA8 precedent, since it's flagged generic). Microreticulophagy correctly held context_only. No mapping change needed.
- **Evidence alignment:** Excellent overlap. PN row 2 titles ("Translocon component Sec62 acts in ER turnover during stress recovery"; "Selective Autophagy: ATG8...LIR...Cargo Receptors") match the review's reticulophagy framing (review cites PMID:31006538). Translocon evidence (PMID:22375059, 29719251, 32133789) is review-only but congruent. No divergence.
- **Verdict:** CONSISTENT. One actionable gap: add Sec61 translocon complex CC.
- **Recommended edits:** [YAML] Add GO:0005784 Sec61 translocon complex (part_of/located_in, translocon-associated) to SEC62 existing_annotations/core_functions, matching the PN-projected term and the verified GO definition (TRAP-inclusive).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SEC62/SEC62-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Protein transport | SEC61 channel complex component
- UniProt: Q99442
- In branches: ER, ALP
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|SEC61 channel complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005784 Sec61 translocon complex]
        rationale: This PN group denotes SEC61 translocon components. The GO Sec61 translocon complex term is the direct cellular-component target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | ERphagy
- UniProt: Q99442
- In branches: ER, ALP
- Notes: Receptor for selective autophagy. An ER-resident autophagy receptor. Contains a conserved LC3-interacting region in the C-terminal cytosolic domain that is required for its function in recovER-phagy, but is dispensable for its function in the protein translocation machinery. Active in ERphagy
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Translocon component Sec62 acts in endoplasmic reticulum turnover during stress recovery
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN uses the community label ERphagy for selective autophagy of the endoplasmic reticulum, while GO uses the synonym reticulophagy. Receptor members of this PN category are suitable for propagation to the GO reticulophagy process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Microautophagy | Microreticulophagy
- UniProt: Q99442
- In branches: ER, ALP
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Microautophagy|Microreticulophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061709 reticulophagy]
        rationale: This group is an ER-autophagy context, but the source label is microreticulophagy and the members mix core autophagy factors with SEC62. Reticulophagy is kept as context only pending a more specific GO term or gene-level review.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport
- GO:0005784 Sec61 translocon complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|SEC61 channel complex component
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
