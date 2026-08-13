---
title: "PSEPK ppu00620 methylglyoxal detoxification batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [gloA, gloB, PP_4040]
autolink_gene_symbols: false
---

# PSEPK ppu00620: methylglyoxal detoxification

- Batch sequence: 15
- Reusable module: `modules/methylglyoxal_detoxification.yaml`
- Correct boundary: two-step glutathione-dependent conversion of methylglyoxal to D-lactate
- Broad ppu00620 candidates inspected: 54
- Selected PSEPK proteins: 2 canonical enzymes plus 1 unresolved family candidate
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate methylglyoxal detoxification from the broad pyruvate-metabolism map.
- [x] Identify the canonical GloA-GloB route and verify endogenous glutathione supply.
- [x] Treat methylglyoxal synthase absence as not expected rather than a pathway hole.
- [x] Keep reductive and DJ-1-family candidate routes outside the canonical module.
- [x] Fetch and curate `gloA` and `gloB`.
- [x] Fetch and conservatively assess `PP_4040` without assuming substrate specificity.
- [x] Reconcile the pre-existing ppu00620 OpenScientist report with local UniProt, GOA, PANTHER, InterPro, and Rhea data.
- [x] Record the unsuccessful gene, generic-module, and UPA00619+PSEPK OpenScientist attempts without fabricating provider output.
- [x] Validate and render the module, genes, and project page.
- [ ] Open one PR for this module.
- [ ] Shepherd review and CI.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| 1 | S-lactoylglutathione formation | `gloA` / PP_3766 | Q88GF8 | Covered by GO:0004462, Rhea 19069, and PTHR10374:SF30 |
| 2 | S-lactoylglutathione hydrolysis | `gloB` / PP_4144 | Q88FF3 | Covered by reviewed HAMAP, GO:0004416, Rhea 21864, and PTHR43705:SF1 |

The two-reaction module is satisfiable. KT2440 also encodes GshA and GshB for
glutathione supply and several lactate dehydrogenases for downstream D-lactate
disposal; these are cross-module dependencies rather than additional parts.

## Annotation Decisions

- The exact existing catalytic molecular functions for GloA and GloB are accepted.
- Generic metal-ion binding on GloA is retained as non-core because metal
  dependence is real but the physiological Ni2+-versus-Zn2+ preference is unresolved.
- Zinc ion binding is proposed as a non-core `NEW` annotation for GloB because
  the reviewed HAMAP record specifies two zinc ions and their coordinating residues.
- Valid `GO:0051596 methylglyoxal catabolic process` is added to GloA and
  accepted on GloB; obsolete route-specific GO:0019243 is not authored.
- PP_0772 is a PTHR46233:SF3 metallo-beta-lactamase-superfamily protein, not a
  canonical GloB-family member; it remains outside the module because its
  physiological substrate is untested.
- PP_4040/Q88FP9 is a short, single-VOC-domain `PTHR33993:SF1` protein with no
  EC, Rhea, pathway, GOA, cofactor, or catalytic-residue assignment. It remains
  an unconfirmed glyoxalase-family candidate and does not satisfy either module
  step.

## Boundary Decisions

- GshA/GshB glutathione synthesis supplies the required cofactor but belongs to
  glutathione metabolism.
- D-lactate oxidation to pyruvate belongs to central carbon metabolism.
- No MgsA methylglyoxal synthase was identified in KT2440; methylglyoxal
  generation is not required to satisfy a defensive detoxification module.
- `yeaE`, `dkgB`, and DJ-1/ThiJ-family proteins are possible parallel routes and
  require separate biochemical resolution.
- `ycgM`/PP_5153 is a fumarylacetoacetase-family enzyme and is excluded.

## Knowledge Gaps

- PP_4040/Q88FP9 remains unresolved. Its short VOC-domain architecture and
  broad family labels do not establish methylglyoxal-glutathione
  hemithioacetal isomerization, hydroxyacylglutathione hydrolysis, or any other
  specific reaction.
- PP_0772/Q88PS6 remains outside the canonical module because its broad
  metallo-beta-lactamase-superfamily assignment does not establish
  S-lactoylglutathione hydrolysis.
- The physiological metal used by KT2440 GloA remains experimentally unresolved.

## Grounding

Both steps use exact PANTHER subfamilies, exact target UniProt entries, reviewed
cross-taxon *Pseudomonas* exemplars (`Q9HU72` and `Q9I2T1`), GO molecular
functions, and Rhea reactions. No PAINT PTN was found for either exact family,
so none is asserted. Molecular functions occur only on leaf annotons, and the
module contains no generic cytoplasm/cytosol assertion.

## Research Status

The OpenScientist report and artifacts are stored under
`projects/P_PUTIDA/deep-research/`. Functional expression studies support the
activity of a *P. putida* glyoxalase I (PMID:11461144; PMID:22358913), but those
historical studies do not tie the tested gene to PP_3766/Q88GF8. The exact
KT2440 assignment therefore rests on the Q88GF8 reaction and PTHR10374:SF30
evidence. The KT2440 GloB assignment has reviewed HAMAP support; E. coli work
also shows that GloB-dependent turnover need not determine acute methylglyoxal
tolerance (PMID:21143325).

The required new gene, reusable-module, and module+UPA00619+PSEPK research was
attempted at the client's maximum supported timeout but returned no reports.
The attempt log and conservative manual reconciliation are documented in
[`ppu00620_methylglyoxal_detoxification-deep-research-manual.md`](ppu00620_methylglyoxal_detoxification-deep-research-manual.md).

## Validation

The gene reviews passed schema, reference, GOA, best-practice, and
ontology-term validation; PP_4040 retains the expected warning for an empty
`core_functions` list because no specific activity is established. The module
passed LinkML and semantic validation with no warnings. Gene, module, and
project renderers completed successfully.
