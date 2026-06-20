# ACIN1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKV3
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ACIN1/ACIN1-ai-review.yaml](ACIN1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ACIN1/ACIN1-ai-review.html](ACIN1-ai-review.html)
- Gene notes: present - [genes/human/ACIN1/ACIN1-notes.md](ACIN1-notes.md)
- GOA TSV: present - [genes/human/ACIN1/ACIN1-goa.tsv](ACIN1-goa.tsv)
- UniProt record: present - [genes/human/ACIN1/ACIN1-uniprot.txt](ACIN1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ACIN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ACIN1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ACIN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ACIN1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ACIN1/ACIN1-deep-research-falcon.md](ACIN1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ACIN1 encodes Acinus, a nuclear RNA-processing and apoptosis-associated protein. Its best-supported core functions are as an RNA-binding component of the ASAP complex and peripheral EJC-associated splicing machinery, where it participates in RNA splicing and regulation of mRNA processing, and as a caspase-activated factor that promotes apoptotic chromatin condensation. ACIN1 is localized mainly to the nucleus, nucleoplasm, and nuclear speckles. Drosophila Acinus literature links the ortholog to basal autophagy/autophagosome maturation, but current direct human evidence supports RNA processing and apoptosis more strongly than a direct human ACIN1 autophagy function.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 12; MODIFY: 3; REMOVE: 1

## PN Consistency Summary

- **Consistency (deep research ↔ review YAML ↔ PN ↔ mapping):** Consistent, and the review handled the tension well. The human review's core functions are RNA binding in the RNPS1–SAP18–ACIN1 **ASAP complex** (GO:0061574) / EJC-associated splicing (GO:0008380) and **caspase-activated apoptotic chromatin condensation** (GO:0030263). The PN row instead places ACIN1 in the **ALP branch** on the strength of *Drosophila* Acinus basal-autophagy work. The review's `description` and a `suggested_question` explicitly name this divergence and conclude human evidence supports RNA processing/apoptosis over a direct autophagy role.
- **Does the PN taxonomy tell a story GO misses? (NEW-annotation pressure):** Yes — PN asserts a *candidate conserved autophagosome-maturation role* that is absent from human GOA. The review correctly does **not** mint a NEW autophagy term (`proposed_new_terms: []`); instead it captures the PN story as a `suggested_question` (is the *Drosophila* basal-autophagy role conserved?) and two `suggested_experiments` (autophagic-flux assay; RNA-target mapping). This is the right altitude: PN flags a hypothesis, not a GO-annotatable human fact. **No new annotation warranted now.**
- **Evidence alignment (did PN and the review pick the same papers?):** **No — deliberately divergent.** PN cites two *Drosophila* papers (Nagy et al., *acinus* endocytic/autophagic trafficking; Cdk5/Ser437 eLife). The review's `supported_by` cites **none** of these; it relies on human ASAP/EJC/apoptosis literature (PMID:12665594, 20966198, 16314458, 22388736, 27365209, 10490026). The divergence is itself the finding: PN's evidence is orthology-based and the human review intentionally does not import it as human evidence.
- **Verdict:** Fully consistent; exemplary handling of an orthology-driven PN inclusion. No edits needed. *Template/positive-control case for the phase-1 review.*

## Full Consistency Review

- **UniProt:** Q9UKV3 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway → Autophagosome closure maturation and lysosome fusion → "Specific function in autophagosome maturation and lysosome fusion unknown"` (1 row, ALP branch)
- **PN-node mapping:** leaf group = `no_mapping` ("unknown/residual" bucket); parent class = `context_only` / `too_broad_to_propagate` → GO:0016236 macroautophagy; branch = `no_mapping`. **No GO propagates to ACIN1 from PN.**

**Consistency (deep research ↔ review YAML ↔ PN ↔ mapping):** Consistent, and the review handled the tension well. The human review's core functions are RNA binding in the RNPS1–SAP18–ACIN1 **ASAP complex** (GO:0061574) / EJC-associated splicing (GO:0008380) and **caspase-activated apoptotic chromatin condensation** (GO:0030263). The PN row instead places ACIN1 in the **ALP branch** on the strength of *Drosophila* Acinus basal-autophagy work. The review's `description` and a `suggested_question` explicitly name this divergence and conclude human evidence supports RNA processing/apoptosis over a direct autophagy role.

**Does the PN taxonomy tell a story GO misses? (NEW-annotation pressure):** Yes — PN asserts a *candidate conserved autophagosome-maturation role* that is absent from human GOA. The review correctly does **not** mint a NEW autophagy term (`proposed_new_terms: []`); instead it captures the PN story as a `suggested_question` (is the *Drosophila* basal-autophagy role conserved?) and two `suggested_experiments` (autophagic-flux assay; RNA-target mapping). This is the right altitude: PN flags a hypothesis, not a GO-annotatable human fact. **No new annotation warranted now.**

**Does PN inclusion change mapping strategy?** No. ACIN1's own PN node is the residual "function unknown" group → correctly `no_mapping`; the class is correctly held at `context_only`/`too_broad_to_propagate`. The PN authors themselves signalled uncertainty (the group label literally says function "unknown"), so the conservative no-propagation call is well-aligned. ACIN1 is a good **negative control** for "membership ≠ GO assertion."

**Evidence alignment (did PN and the review pick the same papers?):** **No — deliberately divergent.** PN cites two *Drosophila* papers (Nagy et al., *acinus* endocytic/autophagic trafficking; Cdk5/Ser437 eLife). The review's `supported_by` cites **none** of these; it relies on human ASAP/EJC/apoptosis literature (PMID:12665594, 20966198, 16314458, 22388736, 27365209, 10490026). The divergence is itself the finding: PN's evidence is orthology-based and the human review intentionally does not import it as human evidence.

**Verdict:** Fully consistent; exemplary handling of an orthology-driven PN inclusion. No edits needed. *Template/positive-control case for the phase-1 review.*

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/ACIN1/ACIN1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Specific function in autophagosome maturation and lysosome fusion unknown
- UniProt: Q9UKV3
- In branches: ALP
- Notes: Drosophila ACN promotes autophagosome maturation in basal autophagy.
- PN references (titles):
    - Drosophila acinus encodes a novel regulator of endocytic and autophagic trafficking | Development | The Company of Biologists
    - Stress-induced Cdk5 activity enhances cytoprotective basal autophagy in Drosophila melanogaster by phosphorylating acinus at serine437 | eLife (elifesciences.org)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Specific function in autophagosome maturation and lysosome fusion unknown
        status=no_mapping scope= GO=[]
        rationale: Reviewed as an unknown or residual PN category. The label does not provide a shared GO-mappable biological process, molecular function, or cellular component.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
