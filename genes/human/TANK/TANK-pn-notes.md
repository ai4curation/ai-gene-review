# TANK PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92844
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TANK/TANK-ai-review.yaml](TANK-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TANK/TANK-ai-review.html
- Gene notes: present - [genes/human/TANK/TANK-notes.md](TANK-notes.md)
- GOA TSV: present - [genes/human/TANK/TANK-goa.tsv](TANK-goa.tsv)
- UniProt record: present - [genes/human/TANK/TANK-uniprot.txt](TANK-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TANK.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TANK.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TANK.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TANK.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TANK (TRAF family member-associated NF-kappa-B activator; also known as I-TRAF) is a cytoplasmic adaptor/scaffold protein, lacking any catalytic activity, that organizes signaling complexes in the innate immune and NF-kappaB pathways. It was first identified as a TRAF-interacting protein that binds the TRAF-C domains of TRAF1, TRAF2 and TRAF3 and modulates TRAF-mediated signaling. Its best-established role is as one of three mutually exclusive adaptors (alongside SINTBAD/TBKBP1 and NAP1/AZI2) that constitutively bind the IKK-related kinases TBK1 and IKBKE (IKKepsilon) via a central TBK1-binding domain and bridge them into complexes that phosphorylate IRF3/IRF7, driving type I interferon production during antiviral innate immunity; TBK1 activation in response to virus or poly(I:C) depends on the TANK-TBK1 interaction. TANK is the non-catalytic subunit of the TBK1-IKKepsilon-TANK kinase complex. TANK also has a separable negative-regulatory function: in response to genotoxic stress or interleukin-1/LPS it scaffolds a deubiquitination complex containing ZC3H12A (MCPIP1) and the deubiquitinase USP10, promoting USP10-dependent deubiquitination of TRAF6 (and NEMO/IKBKG) and thereby restraining canonical NF-kappaB activation. TANK itself contains no deubiquitinase domain, so its activity in this complex is purely as an assembly scaffold. Phosphorylation of TANK by IKBKE disrupts its binding to TRAF2, providing a phospho-switch on its adaptor function. Structurally TANK contains an N-terminal coiled-coil, a TBK1/IKBKE-binding region, a TRAF-interaction motif (which engages the CD40-recognition site of TRAF3), and a C-terminal UBZ1-type zinc finger. TANK is targeted by viral proteases (encephalomyocarditis virus and Seneca Valley virus 3C proteases cleave it; vaccinia C6 binds it) as an immune-evasion strategy, underscoring its role in the antiviral interferon response.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 68; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Major divergence. The review and TANK-notes contain NO autophagy/mitophagy content at all — TANK is treated purely as (1) the non-catalytic adaptor/scaffold of the TBK1-IKKepsilon-TANK complex driving type I IFN (GO:0060090 molecular adaptor, ACCEPT; GO:0032481 positive regulation of type I IFN production), (2) a scaffold that activates USP10-dependent deubiquitination of TRAF6/NEMO to restrain NF-kB (GO:0035800 deubiquitinase activator activity), and (3) a TRAF1/2/3 binder. The PN's mitophagy story ("TANK-TBK1 complex phosphorylates OPTN in mitophagy") rests on a single PNAS paper (Richter/Heo 2016) and is absent from the review.
- **PN story / NEW pressure:** PN asserts a role (GO:0000423 mitophagy, new_to_goa) NOT in GOA and NOT in the review. This is an over-reach. TANK is the **regulatory/scaffold subunit** that bridges TBK1 — it does not itself perform mitophagy. The connection is indirect (TANK→TBK1→OPTN-P→mitophagy). At most this warrants a regulation term, and even that is thin: the PNAS paper foregrounds TBK1/OPTN, with TANK as part of the kinase complex. Bare GO:0000423 mitophagy involved_in is not defensible for TANK on current evidence; treat as candidate/context, not ADD.
- **Evidence alignment:** No overlap on the autophagy axis — PN's sole mitophagy ref (Richter/Heo PNAS) is not in the TANK review (the review's TBK1 interactions are IFN/NF-kB-context IPIs). The shared PNAS paper IS used in OPTN and TBK1 reviews, not TANK.
- **Verdict:** OVER-REACH — PN projects GO:0000423 mitophagy (new_to_goa) onto TANK with no support in review/notes; TANK is an indirect regulatory scaffold of TBK1. **Recommended edits:** [MAP] drop/demote TANK's "Autophagy receptor regulation|Mitophagy"→GO:0000423 projection (indirect, single-paper, regulatory-subunit role) — at most a regulation-of-mitophagy context, not a direct mitophagy annotation; do not add to the review without TANK-specific evidence.

## Full Consistency Review

- **UniProt:** Q92844 (I-TRAF) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (~1282 lines; ~25 IPI bare-protein-binding non-core)
- **PN placement:** ALP `Autophagy substrate selection|Autophagy receptor regulation|Mitophagy` + UPS `Ubiquitin and UBL binding|DUB cofactor|USP10|UBZ1-type ZnF` ; **PN-node mapping:** Receptor-regulation/Mitophagy→GO:0000423 (new_to_goa); UPS DUB-cofactor ancestors no_mapping (class context_only GO:0140036).
- **Consistency:** Major divergence. The review and TANK-notes contain NO autophagy/mitophagy content at all — TANK is treated purely as (1) the non-catalytic adaptor/scaffold of the TBK1-IKKepsilon-TANK complex driving type I IFN (GO:0060090 molecular adaptor, ACCEPT; GO:0032481 positive regulation of type I IFN production), (2) a scaffold that activates USP10-dependent deubiquitination of TRAF6/NEMO to restrain NF-kB (GO:0035800 deubiquitinase activator activity), and (3) a TRAF1/2/3 binder. The PN's mitophagy story ("TANK-TBK1 complex phosphorylates OPTN in mitophagy") rests on a single PNAS paper (Richter/Heo 2016) and is absent from the review.
- **PN story / NEW pressure:** PN asserts a role (GO:0000423 mitophagy, new_to_goa) NOT in GOA and NOT in the review. This is an over-reach. TANK is the **regulatory/scaffold subunit** that bridges TBK1 — it does not itself perform mitophagy. The connection is indirect (TANK→TBK1→OPTN-P→mitophagy). At most this warrants a regulation term, and even that is thin: the PNAS paper foregrounds TBK1/OPTN, with TANK as part of the kinase complex. Bare GO:0000423 mitophagy involved_in is not defensible for TANK on current evidence; treat as candidate/context, not ADD.
- **Mapping strategy:** This gene does NOT justify the node's mitophagy mapping for TANK. The PN node "Autophagy receptor regulation" projecting bare GO:0000423 (a process, not a regulation term) is the same scope drift seen for TBK1, but weaker here because TANK is one step further removed (regulatory adaptor of the kinase). KEY PATTERN: TANK is the regulatory adaptor (per the brief), not a receptor — cargo-adaptor MF does not apply; its MF is GO:0060090 molecular adaptor (already core).
- **Evidence alignment:** No overlap on the autophagy axis — PN's sole mitophagy ref (Richter/Heo PNAS) is not in the TANK review (the review's TBK1 interactions are IFN/NF-kB-context IPIs). The shared PNAS paper IS used in OPTN and TBK1 reviews, not TANK.
- **Verdict:** OVER-REACH — PN projects GO:0000423 mitophagy (new_to_goa) onto TANK with no support in review/notes; TANK is an indirect regulatory scaffold of TBK1. **Recommended edits:** [MAP] drop/demote TANK's "Autophagy receptor regulation|Mitophagy"→GO:0000423 projection (indirect, single-paper, regulatory-subunit role) — at most a regulation-of-mitophagy context, not a direct mitophagy annotation; do not add to the review without TANK-specific evidence.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/TANK/TANK-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Autophagy receptor regulation | Mitophagy
- UniProt: Q92844
- In branches: ALP, UPS
- Notes: TANK-TBK1 complex phosphorylates OPTN in mitophagy.
- PN references (titles):
    - Phosphorylation of OPTN by TBK1 enhances its binding to Ub chains and promotes selective autophagy of damaged mitochondria | PNAS
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: The PN receptor-regulation type for mitophagy captures factors that tune receptor activity within the mitophagy pathway. This supports propagation to mitophagy while preserving that the source is a regulatory sub-role.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DUB cofactor | USP10 | UBZ1-type ZnF
- UniProt: Q92844
- In branches: ALP, UPS
- Signature domains: IPR041641
- Auxiliary domains: IPR024581
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB cofactor|USP10|UBZ1-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB cofactor|USP10
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB cofactor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a cofactor, possible adaptor, or related-family bucket. The label is useful in PN but does not establish a safe direct GO propagation.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Mitophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
