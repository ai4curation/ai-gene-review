---
title: "PSEPK ppu00543 alginate O-acetylation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00543: alginate O-acetylation

- Reusable module: `modules/alginate_o_acetylation.yaml`
- Correct boundary: post-polymerization O-acetylation of alginate by AlgI, AlgJ, AlgF, and AlgX
- Broad ppu00543 candidates inspected: 11
- Selected PSEPK proteins: 4
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate alginate O-acetylation from precursor synthesis, polymerization, export, and mannuronate epimerization.
- [x] Exclude four CysE-family serine O-acetyltransferases and the unrelated PP_2124 glycosyltransferase.
- [x] Fetch and curate `algI`, `algJ`, and `algX`; refine the existing `algF` review.
- [x] Integrate the OpenScientist report with local UniProt, GOA, PANTHER, and InterPro data.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | Inner-membrane acetyl-donor transfer | `algI` / PP_1280 | Q88ND2 | Covered by the exact AlgI family and a conservative broad acyltransferase molecular function |
| 2 | Periplasm-facing acetyl relay | `algJ` / PP_1279 | Q88ND3 | Covered by the AlgJ-specific SGNH family; precise relay chemistry remains a knowledge gap |
| 3 | Periplasmic accessory support | `algF` / PP_1278 | Q88ND4 | Covered by the exact AlgF family without inventing an enzyme activity |
| 4 | Terminal polymer O-acetylation | `algX` / PP_1282 | Q88ND0 | Covered by the AlgX-specific family, conserved catalytic domain, and GO:0016413 |

The four-part module is satisfiable in KT2440. The complete syntenic machinery
supports strong transfer from characterized *Pseudomonas aeruginosa* orthologs,
but the target strain still lacks a direct biochemical measurement of its
alginate acetylation state.

## Annotation Decisions

- `GO:0051979 alginic acid acetylation` is not a descendant of `GO:0042121
  alginic acid biosynthetic process` in the current GO release. It is therefore
  added as a separate exact annotation rather than used as a formal replacement.
- The broad biosynthesis row is retained as non-core pathway context for AlgI
  and AlgJ. It is accepted for AlgF because AlgF loss also impairs polymer
  production, and it remains accepted for dual-role AlgX.
- AlgI retains `GO:0016746 acyltransferase activity`; its immediate donor and
  acceptor are not defined precisely enough for a narrower term.
- No molecular function is asserted for AlgJ or AlgF. Their essential relay and
  accessory roles are represented through exact families, process, location,
  and role prose.
- AlgX receives `GO:0016413 O-acetyltransferase activity`, with alginate
  substrate specificity captured by GO:0051979 and the core-function text.
- AlgX also receives `GO:0030247 polysaccharide binding` from direct
  length-dependent polymannuronate-binding evidence and retains a separate
  chain-protection core function.

## Boundary Decisions

- Alg8, Alg44, AlgK, AlgE, AlgG, and AlgL belong to the separate alginate
  polymerization/export module.
- AlgA, AlgC-type phosphomannomutases, and AlgD supply GDP-mannuronate upstream.
- PP_0228, `cysE`/PP_0840, PP_1110, and PP_3136 perform serine O-acetylation in
  cysteine metabolism and are not alternate alginate acetylases.
- PP_2124 is a glycosyltransferase outside the alginate operon.

## Grounding

Each role is grounded to an exact KT2440 UniProt entry, an exact AlgI/AlgJ/AlgF
or AlgX InterPro family, and a reviewed *P. aeruginosa* exemplar. Molecular
functions are asserted only on the relevant leaf annotons. The module has no
module-level molecular-function or generic cytoplasm/cytosol assertion.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Primary studies PMID:12003941 and
PMID:8636017 establish the AlgI/J/F genetics, PMID:23779107 and PMID:25165982
establish AlgX catalysis and polymer binding, and PMID:31900562 connects AlgF
to the polymerization complex. The KT2440 AlgJ soluble domain itself was
crystallized in PMID:25165982. The absence of KT2440-specific polymer
acetylation measurements remains explicit.

## Validation

All four gene reviews passed schema, reference, GOA, best-practice, and
ontology-term validation without warnings. The module passed LinkML and
semantic validation; the only semantic warning is the expected unconfigured
`InterPro` prefix for family labels. Gene, module, and project renderers
completed successfully.
