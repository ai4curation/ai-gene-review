# Gsta4 review notes

## Evidence summary
- [UniProtKB:P14942] UniProt describes Gsta4 as conjugating reduced glutathione to exogenous and endogenous hydrophobic electrophiles.
- [PMID:11018474] The fetched GOA file uses this publication for toxic-substance binding, kept as non-core context rather than the defining activity.

## Curation decisions
- Core function: glutathione S-transferase alpha-4 (glutathione transferase activity, GO:0004364).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-04

**GOA changes.** The refresh split the ISO glutathione transferase activity (GO:0004364, GO_REF:0000121) row by donor: one row from mouse Gsta4 (MGI:MGI:1309515, UniProt P24472) and a new seeded row from human GSTA4 (UniProtKB:O15217). No rows were retired. Total 19 rows.

**Actions.**
- New GO:0004364 ISO (donor human GSTA4, O15217): PENDING -> ACCEPT. Shared alpha-class catalytic activity, transferred from the one-to-one ortholog; rat tissue data show 4-HNE-specific GST A4-4 activity [PMID:9774145 "it also increased 4-hydroxynonenal specific GST A4-4 activity in the brain and lung mitochondrial matrix fraction"].
- Mouse-donor GO:0004364 ISO sibling: action unchanged (ACCEPT); reason now names the donor.
- No other action changed. IEP stimulus-response rows (herbicide, zinc, nicotine, lithium) remain MARK_AS_OVER_ANNOTATED: each is an expression change [PMID:20553223 "Zn and/or PQ exposure increased gene expression of DAT, CYP2E1, GSTA4-4, MT-I and MT-II"; PMID:18082333 "chronic lithium treatment not only increased GST M1 mRNA levels, but also increased GST M3, M5 and A4 mRNA levels"]. Their supporting quotes were replaced with the GSTA4-specific sentences (previous quotes were generic background lines).
- Toxic substance binding (IPI, PMID:11018474, abstract-only) remains MARK_AS_OVER_ANNOTATED: 4-HNE is the H-site substrate, already captured by GO:0004364 [PMID:11018474 "differential cell specific expressions of GST isoforms GSTP1-1 and GSTA4-4 were observed"].
- Rows that cited only the UniProt DR GO cross-reference line (which restates the annotation itself) now also cite the FUNCTION, SUBUNIT or SUBCELLULAR LOCATION CC lines; mitochondrion now also cites [PMID:9774145 "the brain mitochondrial matrix showed a markedly higher level of 4-hydroxynonenal specific GST activity and mGST A4-4 antibody-reactive protein than did the cytosolic fraction"].
- Description rewritten to remove curation commentary.

**Open questions.** Whether GSTA4-4's reversible retro-Michael chemistry (see suggested_questions) merits a homeostasis-type BP term remains open.
