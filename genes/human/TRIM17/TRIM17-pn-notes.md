# TRIM17 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y577
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRIM17/TRIM17-ai-review.yaml](TRIM17-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TRIM17/TRIM17-ai-review.html
- Gene notes: present - [genes/human/TRIM17/TRIM17-notes.md](TRIM17-notes.md)
- GOA TSV: present - [genes/human/TRIM17/TRIM17-goa.tsv](TRIM17-goa.tsv)
- UniProt record: present - [genes/human/TRIM17/TRIM17-uniprot.txt](TRIM17-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRIM17.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIM17.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRIM17 (terf, testis RING finger protein; RNF16) is a RING-type E3 ubiquitin ligase of the TRIM/RBCC family with the canonical architecture of an N-terminal RING-HC zinc finger (conferring E3 ubiquitin ligase activity, EC 2.3.2.27), a B-box, a coiled-coil and a C-terminal B30.2/SPRY domain; it is expressed almost exclusively in testis and undergoes autoubiquitination. TRIM17 is a key regulator of neuronal apoptosis: it ubiquitinates and degrades the anti-apoptotic protein MCL1 to initiate neuronal death, and it controls NFAT transcription factors (NFATC3/NFATC4) by preventing their nuclear localization and thereby inhibiting their transcriptional activity. It also modulates selective autophagy in a target-selective manner: it inhibits autophagic degradation of diverse substrates while contributing to autophagy of midbodies, with its autophagy-inhibitory activity involving MCL1, which TRIM17 assembles into complexes with the autophagy regulator BECN1. Additional reported activities include stimulating proteasomal degradation of the kinetochore protein ZWINT to negatively regulate cell proliferation, antagonizing other TRIM ligases (it prevents TRIM28 from ubiquitinating the anti-apoptotic BCL2A1, and decreases TRIM41-mediated degradation of ZSCAN-family substrates to promote alpha-synuclein/SNCA transcription in neurons), and being stabilized through interaction with TRIM44. TRIM17 localizes to the cytoplasm and lysosome.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent. PN (selective-autophagy receptor for midbodies + genuine RING E3), review and notes agree: TRIM17 has a real RING-HC domain, autoubiquitinates (PMID:19358823), degrades MCL1 to drive neuronal apoptosis, and acts in **target-selective** autophagy — broadly INHIBITING autophagic degradation while contributing to midbody autophagy via MCL1/BECN1 scaffolding (PMID:27562068). Functional RING → catalytic ligase MF correct. No contradictions; the nuance that TRIM17 is mostly an autophagy *inhibitor* is captured in both.
- **PN story / NEW pressure:** PN routes midbody autophagy through the cargo-adaptor MF GO:0160247 (verified real) because GO has NO dedicated "midbody autophagy" process term (confirmed — searchClasses returns nothing). The review already captures this MF as GO:0030674 protein-macromolecule adaptor activity (ACCEPT, IPI PMID:25127057) and GO:0006914 autophagy (ACCEPT) — so the role IS in GOA at the generic level, and GO:0160247 is the more specific upgrade (hence PN's "more_specific_than_existing_goa"). Defensible refinement, not a brand-new role. No new GO process term mintable for midbody autophagy.
- **Evidence alignment:** Strong overlap. PN cites the LIR/cargo-receptor review and the midbody paper (= PMID:27562068, review HIGH) and 33791238/19489725 (TRIM/E3 reviews). Review refs (PMID:27562068, 25127057, 19358823) cover the autophagy + ligase arms; the MCL1/neuronal-apoptosis primary paper (PMID:22023800, in notes) is not a cited reference in the review.
- **Verdict:** Consistent; cargo-adaptor MF upgrade warranted; RING ligase already captured. **Recommended edits:** [YAML] upgrade the GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity (supported by PMID:27562068/25127057), scoped to midbody autophagy. [REF] consider adding PMID:22023800 (MCL1/ZWINT, neuronal apoptosis) to references to support the core MCL1-degradation function.

## Full Consistency Review

- **UniProt:** Q9Y577 (terf/RNF16) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE
- **PN placement:** 2 rows — `ALP|Autophagy substrate selection|Selective autophagy receptor|Midbody autophagy`; `UPS|E3 ubiquitin and UBL ligases|RING|TRIM / class IV|SPRY`. **PN-node mapping:** Midbody-autophagy type → mapped/ok GO:0160247 autophagy cargo adaptor activity (more_specific_than_existing_goa); RING group → mapped/ok GO:0061630 ubiquitin protein ligase activity (already_in_goa_exact); E3-ligase ancestors = no_mapping/context_only.
- **Consistency:** Consistent. PN (selective-autophagy receptor for midbodies + genuine RING E3), review and notes agree: TRIM17 has a real RING-HC domain, autoubiquitinates (PMID:19358823), degrades MCL1 to drive neuronal apoptosis, and acts in **target-selective** autophagy — broadly INHIBITING autophagic degradation while contributing to midbody autophagy via MCL1/BECN1 scaffolding (PMID:27562068). Functional RING → catalytic ligase MF correct. No contradictions; the nuance that TRIM17 is mostly an autophagy *inhibitor* is captured in both.
- **PN story / NEW pressure:** PN routes midbody autophagy through the cargo-adaptor MF GO:0160247 (verified real) because GO has NO dedicated "midbody autophagy" process term (confirmed — searchClasses returns nothing). The review already captures this MF as GO:0030674 protein-macromolecule adaptor activity (ACCEPT, IPI PMID:25127057) and GO:0006914 autophagy (ACCEPT) — so the role IS in GOA at the generic level, and GO:0160247 is the more specific upgrade (hence PN's "more_specific_than_existing_goa"). Defensible refinement, not a brand-new role. No new GO process term mintable for midbody autophagy.
- **Mapping strategy:** No node change needed. Cargo-adaptor MF over bare protein binding is the prescribed pattern and matches the review. Genuine RING → GO:0061630 already_in_goa_exact, correctly retained. Caution: TRIM17's autophagy role is predominantly inhibitory/selective; the cargo-adaptor MF should be scoped to the midbody-autophagy contribution, not read as a general pro-autophagy receptor.
- **Evidence alignment:** Strong overlap. PN cites the LIR/cargo-receptor review and the midbody paper (= PMID:27562068, review HIGH) and 33791238/19489725 (TRIM/E3 reviews). Review refs (PMID:27562068, 25127057, 19358823) cover the autophagy + ligase arms; the MCL1/neuronal-apoptosis primary paper (PMID:22023800, in notes) is not a cited reference in the review.
- **Verdict:** Consistent; cargo-adaptor MF upgrade warranted; RING ligase already captured. **Recommended edits:** [YAML] upgrade the GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity (supported by PMID:27562068/25127057), scoped to midbody autophagy. [REF] consider adding PMID:22023800 (MCL1/ZWINT, neuronal apoptosis) to references to support the core MCL1-degradation function.
- **2026-06-18 follow-up:** Implemented the scoped YAML recommendation by adding GO:0160247 as a NEW midbody-selective autophagy cargo-adaptor recommendation, but retained GO:0030674 as the core MF after review feedback because TRIM17's dominant autophagy role is inhibitory/context-dependent. PMID:22023800 was added as a medium-relevance ZWINT/proliferation reference with an explicit caveat that the cached abstract does not support the MCL1 apoptosis claim.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/TRIM17/TRIM17-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Midbody autophagy
- UniProt: Q9Y577
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Normally acts as a prominent inhibitor of bulk autophagy via stabilizing interactions between autophagy factor Beclin1 and anti-autophagy Mcl-1. TRIM17 is specifically required for the promotion and the removal of midbodies, remnants of the cell division machinery that are known autophagy targets via its interaction with p62/SQSTM1 and LC3B.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - TRIM17 contributes to autophagy of midbodies while actively sparing other targets from degradation
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Midbody autophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160247 autophagy cargo adaptor activity]
        rationale: Midbody-autophagy receptors such as SQSTM1 link ubiquitinated midbody material to the autophagy machinery. GO does not currently expose a dedicated midbody-autophagy process term in the local ontology cache, so the receptor activity term is the best available mapping target.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | TRIM / class IV | SPRY
- UniProt: Q9Y577
- In branches: ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR003877, IPR006574
- PN references (titles):
    - 33791238 / rev
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / class IV|SPRY
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / class IV
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
- GO:0160247 autophagy cargo adaptor activity | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Midbody autophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
