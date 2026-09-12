## ACIN1

- **UniProt:** Q9UKV3 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway → Autophagosome closure maturation and lysosome fusion → "Specific function in autophagosome maturation and lysosome fusion unknown"` (1 row, ALP branch)
- **PN-node mapping:** leaf group = `no_mapping` ("unknown/residual" bucket); parent class = `context_only` / `too_broad_to_propagate` → GO:0016236 macroautophagy; branch = `no_mapping`. **No GO propagates to ACIN1 from PN.**

**Consistency (deep research ↔ review YAML ↔ PN ↔ mapping):** Consistent, and the review handled the tension well. The human review's core functions are RNA binding in the RNPS1–SAP18–ACIN1 **ASAP complex** (GO:0061574) / EJC-associated splicing (GO:0008380) and **caspase-activated apoptotic chromatin condensation** (GO:0030263). The PN row instead places ACIN1 in the **ALP branch** on the strength of *Drosophila* Acinus basal-autophagy work. The review's `description` and a `suggested_question` explicitly name this divergence and conclude human evidence supports RNA processing/apoptosis over a direct autophagy role.

**Does the PN taxonomy tell a story GO misses? (NEW-annotation pressure):** Yes — PN asserts a *candidate conserved autophagosome-maturation role* that is absent from human GOA. The review correctly does **not** mint a NEW autophagy term (`proposed_new_terms: []`); instead it captures the PN story as a `suggested_question` (is the *Drosophila* basal-autophagy role conserved?) and two `suggested_experiments` (autophagic-flux assay; RNA-target mapping). This is the right altitude: PN flags a hypothesis, not a GO-annotatable human fact. **No new annotation warranted now.**

**Does PN inclusion change mapping strategy?** No. ACIN1's own PN node is the residual "function unknown" group → correctly `no_mapping`; the class is correctly held at `context_only`/`too_broad_to_propagate`. The PN authors themselves signalled uncertainty (the group label literally says function "unknown"), so the conservative no-propagation call is well-aligned. ACIN1 is a good **negative control** for "membership ≠ GO assertion."

**Evidence alignment (did PN and the review pick the same papers?):** **No — deliberately divergent.** PN cites two *Drosophila* papers (Nagy et al., *acinus* endocytic/autophagic trafficking; Cdk5/Ser437 eLife). The review's `supported_by` cites **none** of these; it relies on human ASAP/EJC/apoptosis literature (PMID:12665594, 20966198, 16314458, 22388736, 27365209, 10490026). The divergence is itself the finding: PN's evidence is orthology-based and the human review intentionally does not import it as human evidence.

**Verdict:** Fully consistent; exemplary handling of an orthology-driven PN inclusion. No edits needed. *Template/positive-control case for the phase-1 review.*
