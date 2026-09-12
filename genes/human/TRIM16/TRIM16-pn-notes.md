# TRIM16 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O95361
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRIM16/TRIM16-ai-review.yaml](TRIM16-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TRIM16/TRIM16-ai-review.html
- Gene notes: present - [genes/human/TRIM16/TRIM16-notes.md](TRIM16-notes.md)
- GOA TSV: present - [genes/human/TRIM16/TRIM16-goa.tsv](TRIM16-goa.tsv)
- UniProt record: present - [genes/human/TRIM16/TRIM16-uniprot.txt](TRIM16-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM16.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM16.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRIM16 (estrogen-responsive B box protein, EBBP) is a cytoplasmic member of the TRIM/RBCC family that is atypical in lacking a canonical N-terminal RING domain: its architecture comprises B-box zinc finger(s), a coiled-coil that mediates homodimerization (and heterodimerization with other TRIMs such as MID1, TRIM24 and PML), and a C-terminal B30.2/SPRY domain. Despite lacking a RING, TRIM16 has been reported to act as an atypical E3 ubiquitin ligase that autoubiquitinates via its B-boxes. Its principal modern function is in selective autophagy of damaged endomembranes: TRIM16 serves as a scaffold/receptor that, in a ULK1-dependent manner, interacts with galectin-3 (LGALS3) to sense and direct autophagy of damaged lysosomes and phagosomes (lysophagy), and it assembles core autophagy machinery (BECN1, ATG16L1, SQSTM1/p62 and LC3B/MAP1LC3B) to drive autophagic clearance of protein aggregates. Through these activities it regulates the p62-KEAP1-NRF2 axis (modulating NRF2 ubiquitination and stability) and protects cells against oxidative-stress-induced death following endomembrane damage; it is itself phosphorylated by ULK1. TRIM16 localizes mainly to the cytoplasm/cytosol (and has been observed in nuclear PML bodies). It was originally characterized as the estrogen-responsive B box protein with reported roles in keratinocyte differentiation, retinoid (retinoic acid receptor) signaling, interleukin-1beta production (binding IL-1 and the NALP1 NACHT domain), and tumor suppression (inhibiting cytoplasmic vimentin and nuclear E2F1 in neuroblastoma).
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 20; NEW: 2

## PN Consistency Summary

- **Consistency:** Consistent, and the RING-less caveat is correctly recognized on BOTH sides. PN explicitly labels TRIM16 `TRIM / unclassified | ringless & SPRY`, and the review/notes repeatedly flag that TRIM16 LACKS a canonical RING and only autoubiquitinates atypically via its B-boxes (PMID:22629402). PN, review and notes agree the modern core function is galectin-3/ULK1-dependent lysophagy + aggrephagy scaffolding (PMID:27693506). No contradictions on biology.
- **PN story / NEW pressure:** Strong, defensible ADD pressure: the autophagy role is genuinely absent from GOA (confirmed — TRIM16 GOA has NO autophagy term). The review already adds it as two NEW annotations (GO:0006914 autophagy + GO:0030674 protein-macromolecule adaptor activity). PN's lysophagy node elevates the cargo-adaptor MF GO:0160247 (verified real) over bare protein binding — exactly the prescribed pattern, and more specific than the review's GO:0030674. **Important ontology correction:** the PN-node rationale claims "the current GO cache lacks a dedicated lysophagy process term" — this is WRONG: GO:0062093 lysophagy EXISTS (verified, def "selective autophagy in which a damaged lysosome is degraded by macroautophagy"). So a lysophagy **process** term is available in addition to the cargo-adaptor MF.
- **Evidence alignment:** Strong overlap. PN cites the LIR/cargo-receptor review and the TRIM16-galectin-3 paper (= PMID:27693506, review HIGH) and 33791238 (TRIM review). Review refs (PMID:27693506, 22629402, 25127057) cover lysophagy + atypical ligase + LC3B.
- **Verdict:** Consistent; lysophagy ADD warranted; RING-less caveat correctly handled. **Recommended edits:** [MAP] fix the Lysophagy node rationale — GO:0062093 lysophagy exists; add it as the process target alongside GO:0160247. [YAML] upgrade the review's NEW GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity, and add GO:0062093 lysophagy (involved_in, PMID:27693506) as the specific process. [YAML] retain GO:0061630 only as the atypical B-box autoubiquitination capture (do not assert RING catalytic ligase function).

## Full Consistency Review

- **UniProt:** O95361 (EBBP) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (thorough)
- **PN placement:** 2 rows — `ALP|Autophagy substrate selection|Selective autophagy receptor|Lysophagy`; `UPS|E3 ubiquitin and UBL ligases|RING|TRIM / unclassified|ringless & SPRY`. **PN-node mapping:** Lysophagy type → mapped/ok GO:0160247 autophagy cargo adaptor activity (new_to_goa); RING group → mapped/ok GO:0061630 ubiquitin protein ligase activity (already_in_goa_exact); E3-ligase ancestors = context_only/no_mapping.
- **Consistency:** Consistent, and the RING-less caveat is correctly recognized on BOTH sides. PN explicitly labels TRIM16 `TRIM / unclassified | ringless & SPRY`, and the review/notes repeatedly flag that TRIM16 LACKS a canonical RING and only autoubiquitinates atypically via its B-boxes (PMID:22629402). PN, review and notes agree the modern core function is galectin-3/ULK1-dependent lysophagy + aggrephagy scaffolding (PMID:27693506). No contradictions on biology.
- **PN story / NEW pressure:** Strong, defensible ADD pressure: the autophagy role is genuinely absent from GOA (confirmed — TRIM16 GOA has NO autophagy term). The review already adds it as two NEW annotations (GO:0006914 autophagy + GO:0030674 protein-macromolecule adaptor activity). PN's lysophagy node elevates the cargo-adaptor MF GO:0160247 (verified real) over bare protein binding — exactly the prescribed pattern, and more specific than the review's GO:0030674. **Important ontology correction:** the PN-node rationale claims "the current GO cache lacks a dedicated lysophagy process term" — this is WRONG: GO:0062093 lysophagy EXISTS (verified, def "selective autophagy in which a damaged lysosome is degraded by macroautophagy"). So a lysophagy **process** term is available in addition to the cargo-adaptor MF.
- **Mapping strategy:** CRITICAL — do NOT assign catalytic ligase MF on biological grounds, since TRIM16 is RING-less; but here the RING node's GO:0061630 is already_in_goa_exact via the EC/IEA + an EXP autoubiquitination annotation, so it is retained as an atypical-ligase capture rather than a PN-driven new catalytic claim. The PN correctly routes the headline biology through the cargo-adaptor MF (GO:0160247), not through catalytic ligase. Node is sound; only the "lysophagy term absent" rationale needs fixing, and the process term should be added.
- **Evidence alignment:** Strong overlap. PN cites the LIR/cargo-receptor review and the TRIM16-galectin-3 paper (= PMID:27693506, review HIGH) and 33791238 (TRIM review). Review refs (PMID:27693506, 22629402, 25127057) cover lysophagy + atypical ligase + LC3B.
- **Verdict:** Consistent; lysophagy ADD warranted; RING-less caveat correctly handled. **Recommended edits:** [MAP] fix the Lysophagy node rationale — GO:0062093 lysophagy exists; add it as the process target alongside GO:0160247. [YAML] upgrade the review's NEW GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity, and add GO:0062093 lysophagy (involved_in, PMID:27693506) as the specific process. [YAML] retain GO:0061630 only as the atypical B-box autoubiquitination capture (do not assert RING catalytic ligase function).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/TRIM16/TRIM16-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Lysophagy
- UniProt: O95361
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. An E3 ubiquitin ligase. TRIM16, interacted with Galectin-3 in a ULK1-dependent manner. TRIM16, through integration of Galectin- and ubiquitin-based processes, coordinated recognition of membrane damage with mobilization of the core autophagy regulators ATG16L1, ULK1, and Beclin 1 in response to damaged endomembranes.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - TRIMs and Galectins Globally Cooperate and TRIM16 and Galectin-3 Co-direct Autophagy in Endomembrane Damage Homeostasis - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Lysophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160247 autophagy cargo adaptor activity]
        rationale: The PN lysophagy receptor class denotes factors that recognize damaged lysosomal cargo and couple it to autophagic clearance. Since the current GO cache lacks a dedicated lysophagy process term, autophagy cargo adaptor activity is the most specific supported target.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | TRIM / unclassified | ringless & SPRY
- UniProt: O95361
- In branches: ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR003877, IPR006574
- PN references (titles):
    - 33791238 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / unclassified|ringless & SPRY
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / unclassified
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0160247 autophagy cargo adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Lysophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
