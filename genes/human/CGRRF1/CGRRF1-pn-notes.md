# CGRRF1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q99675
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CGRRF1/CGRRF1-ai-review.yaml](CGRRF1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CGRRF1/CGRRF1-ai-review.html](CGRRF1-ai-review.html)
- Gene notes: present - [genes/human/CGRRF1/CGRRF1-notes.md](CGRRF1-notes.md)
- GOA TSV: present - [genes/human/CGRRF1/CGRRF1-goa.tsv](CGRRF1-goa.tsv)
- UniProt record: present - [genes/human/CGRRF1/CGRRF1-uniprot.txt](CGRRF1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CGRRF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CGRRF1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CGRRF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CGRRF1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CGRRF1 (cell growth regulator with RING finger domain protein 1; also known as CGR19 and RNF197) is a 332-residue endoplasmic reticulum (ER) membrane-anchored protein with an N-terminal hydrophobic/transmembrane region and a C-terminal cytosolic RING-type zinc finger (residues ~274-309; NMR structure PDB 2EA5). Its domain architecture (a canonical C3HC4/C3H2C3 RING coupled to a transmembrane membrane anchor) is the hallmark of ER-resident RING-type E3 ubiquitin ligases that act in ER-associated degradation (ERAD), where they cooperate with E2 conjugating enzymes to ubiquitinate substrates destined for proteasomal degradation. CGRRF1 localizes to the ER and partially to the nucleus, is transcriptionally up-regulated by ER stress (thapsigargin, tunicamycin) downstream of the ATF6 branch of the unfolded protein response, and is ubiquitously expressed with highest levels in testis and cerebellum. It was originally discovered as CGR19, a p53-induced transcript whose overexpression inhibits growth of several cell lines, the basis of its historical description as a cell growth/cell cycle regulator. Although structurally classified among candidate ERAD E3 ligases, direct biochemical demonstration of its ubiquitin ligase activity is lacking: the one published in vitro autoubiquitination test (with the E2 UbcH5c/UBE2D3) was negative, and no physiological substrate has been defined.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Partial conflict / caveat. Deep-research, review, and PN agree CGRRF1 is an ER-membrane RING + transmembrane protein with the structural hallmarks of an ERAD E3 ligase (RING ZN_FING 274-309, PDB 2EA5; ER localization; ATF6/UPR-induced). BUT the review (and notes) emphasize a NEGATIVE result: the only published in vitro autoubiquitination assay (E2 UbcH5c/UBE2D3) showed NO E3 activity, and no substrate is known (PMID:27485036). The review therefore deliberately does NOT accept ubiquitin ligase activity as a curated function — it has no GO:0061630 in existing_annotations and frames E3 activity only structurally in core_functions + suggested_experiments. PN's RING-group projection of GO:0061630 thus conflicts with the review's explicit caution.
- **PN story / NEW pressure:** Over-reaches given negative biochemical evidence. PN projects GO:0061630 (real term) as new_to_goa from RING-group membership, but the catalytic activity is unproven (negative in vitro test, no substrate). This is a homology/architecture inference the review intentionally withheld. Recommend NOT propagating GO:0061630 as an asserted MF; at most an ISS/structural inference clearly flagged as unverified-by-assay. The review's well-supported content is ER localization (GO:0005783, IDA) and ER-stress/UPR induction.
- **Evidence alignment:** PN cites 19489725 (the ERAD-RING-ligase genome-wide screen = PMID:27485036, the review's central source) — good direct overlap. Review additionally uses PMID:8968090 (p53/CGR19 growth) and PMID:32296183 (HuRI). PN and review share the key ERAD-screen reference.
- **Verdict:** Caveated inconsistency — PN's GO:0061630 over-reaches relative to the review's deliberate non-acceptance (negative in vitro E3 assay). Defer to review's caution.

## Full Consistency Review

- **UniProt:** Q99675 (CGR19, RNF197) · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|RING|other|other` ; **PN-node mapping:** RING/other subtype+type no_mapping; RING group mapped → GO:0061630 ubiquitin protein ligase activity (ok_for_propagation, new_to_goa); class context_only (GO:0061630, too_broad).
- **Consistency:** Partial conflict / caveat. Deep-research, review, and PN agree CGRRF1 is an ER-membrane RING + transmembrane protein with the structural hallmarks of an ERAD E3 ligase (RING ZN_FING 274-309, PDB 2EA5; ER localization; ATF6/UPR-induced). BUT the review (and notes) emphasize a NEGATIVE result: the only published in vitro autoubiquitination assay (E2 UbcH5c/UBE2D3) showed NO E3 activity, and no substrate is known (PMID:27485036). The review therefore deliberately does NOT accept ubiquitin ligase activity as a curated function — it has no GO:0061630 in existing_annotations and frames E3 activity only structurally in core_functions + suggested_experiments. PN's RING-group projection of GO:0061630 thus conflicts with the review's explicit caution.
- **PN story / NEW pressure:** Over-reaches given negative biochemical evidence. PN projects GO:0061630 (real term) as new_to_goa from RING-group membership, but the catalytic activity is unproven (negative in vitro test, no substrate). This is a homology/architecture inference the review intentionally withheld. Recommend NOT propagating GO:0061630 as an asserted MF; at most an ISS/structural inference clearly flagged as unverified-by-assay. The review's well-supported content is ER localization (GO:0005783, IDA) and ER-stress/UPR induction.
- **Mapping strategy:** This gene argues for caution on the RING-group → GO:0061630 projection. Domain-based RING-group propagation is reasonable for ligases with positive evidence, but CGRRF1 is a counterexample (RING present, activity not demonstrated, one assay negative). Flag CGRRF1 as a RING-group member that should NOT auto-inherit GO:0061630 without experimental support; the type node is already no_mapping which is appropriate.
- **Evidence alignment:** PN cites 19489725 (the ERAD-RING-ligase genome-wide screen = PMID:27485036, the review's central source) — good direct overlap. Review additionally uses PMID:8968090 (p53/CGR19 growth) and PMID:32296183 (HuRI). PN and review share the key ERAD-screen reference.
- **Verdict:** Caveated inconsistency — PN's GO:0061630 over-reaches relative to the review's deliberate non-acceptance (negative in vitro E3 assay). Defer to review's caution.
- **Recommended edits:** Suppress/flag the RING-group GO:0061630 projection for CGRRF1 (unproven catalytic activity; one in vitro assay negative); if retained, mark as homology-only/unverified rather than ok_for_propagation. [MAP]

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CGRRF1/CGRRF1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | other | other
- UniProt: Q99675
- In branches: UPS
- Signature domains: IPR001841
- Auxiliary domains: (none)
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other
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

## Projected GO annotations (1)
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
