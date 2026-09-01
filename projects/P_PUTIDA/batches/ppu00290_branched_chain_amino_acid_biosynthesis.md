---
title: "PSEPK ppu00290 branched-chain amino acid biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00290: branched-chain amino acid biosynthesis

- Reusable module: `modules/branched_chain_amino_acid_biosynthesis.yaml`
- KEGG ppu00290 candidates inspected: 18
- Selected pathway proteins reviewed: 11
- Biochemical activities covered: 8, including two heteromeric enzyme assemblies
- Excluded broad-map, catabolic-family, or unsupported paralog candidates: 7
- Gene-level provider: OpenScientist
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a multi-part module with the shared valine/isoleucine trunk and leucine branch.
- [x] Distinguish catalytic and regulatory subunits of acetohydroxy-acid synthase.
- [x] Fetch and review the 11 selected PSEPK proteins.
- [x] Review every GOA annotation for the selected genes.
- [x] Complete the OpenScientist module and gene research pass.
- [x] Complete initial module and gene validation.
- [x] Render module, gene, and project pages after research integration.
- [x] Open one draft PR for this module/pathway: [#2176](https://github.com/ai4curation/ai-gene-review/pull/2176).
- [x] Re-audit family grounding, PAINT nodes, module graph semantics, and non-core location evidence after merge.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK protein(s) | UniProt | Decision |
|---|---|---|---|---|
| 1 | L-threonine to 2-oxobutanoate for the isoleucine branch | `ilvA-I`, `ilvA-II` | Q88HB4, Q88CN1 | Covered by two full-length biosynthetic-family paralogs; relative in-vivo flux is unresolved |
| 2 | Acetohydroxy-acid formation | `ilvI` catalytic plus `ilvH` regulatory subunit | Q88DY8, Q88DY9 | Covered as a two-subunit complex |
| 3 | Acetohydroxy-acid reduction/rearrangement | `ilvC` | Q88DZ0 | Covered for the valine and isoleucine substrates |
| 4 | Dihydroxy-acid dehydration | `ilvD` | Q88CQ2 | Covered for the valine and isoleucine substrates |
| 5a | Committed leucine-branch condensation | `leuA` | Q88P28 | Covered |
| 5b | Isopropylmalate isomerization | `leuC`, `leuD` | Q88LE8, Q88LE7 | Covered as a two-subunit dehydratase |
| 5c | Leucine-branch 2-oxoacid formation | `leuB` | Q88LE5 | Covered |
| 6 | Terminal transamination for valine, leucine, and isoleucine | `ilvE` | Q88H54 | Covered by one shared BCAT |

The canonical pathway is satisfiable in KT2440. The shared IlvI/IlvH, IlvC,
and IlvD trunk handles both pyruvate-derived valine synthesis and the
2-oxobutanoate-derived isoleucine route. The IlvD valine intermediate also
feeds the LeuA/LeuC-LeuD/LeuB extension branch, after which IlvE supplies the
terminal transamination for all three products.

## Excluded Candidates

| Gene | Reason outside the curated core boundary |
|---|---|
| `PP_1157`, `PP_1394` | Additional AHAS-like large subunits with broad KEGG assignments and no current evidence that they replace the canonical `ilvI`/`ilvH` complex in BCAA biosynthesis |
| `alaA` | Glutamate-pyruvate aminotransferase, not the branched-chain amino-acid aminotransferase used for the three terminal reactions |
| `PP_2930` | L-serine ammonia-lyase in an ACC-deaminase/D-cysteine-desulfhydrase-related family, not the full-length biosynthetic IlvA family |
| `PP_3191`, `PP_4430` | Shorter serine/threonine-dehydratase-family proteins lacking the dual C-terminal ACT architecture and biosynthetic IlvA family signature of Q88HB4/Q88CN1 |
| `ldh` | Leucine dehydrogenase can interconvert leucine and its 2-oxoacid but is not needed to satisfy the canonical IlvE-dependent biosynthetic route |

## Module Decisions

- The module has six top-level parts and a three-reaction nested leucine branch;
  it is not a single-enzyme wrapper.
- IlvI and IlvH are separate annotons in one protein-complex step. Catalytic
  acetolactate synthase activity is assigned only to IlvI, while IlvH carries
  acetolactate synthase regulator activity. The complex node carries
  GO:0005948, while both molecular functions remain on the leaf annotons.
- LeuC and LeuD are separate annotons in the heteromeric isopropylmalate
  dehydratase step. Its complex node carries GO:0009316. Both gene reviews use
  `contributes_to_molecular_function` because the complete activity requires
  the LeuC-LeuD assembly; complex membership is accepted for LeuD and proposed
  for LeuC.
- IlvA-I and IlvA-II are exact PSEPK exemplars of
  `PANTHER:PTHR48078:SF11`. Either can satisfy the reaction at first-pass
  resolution; direct genetics or expression data are needed to partition their
  physiological roles. The official mitochondrial wording of the PANTHER label
  is not treated as a bacterial localization claim.
- Molecular functions occur only on leaf annotons, and each leaf has exact
  PSEPK UniProt exemplars.
- No module-level cytoplasm/cytosol assertions are made.
- KEGG membership alone is not used to promote paralogous AHAS or dehydratase
  proteins into the module core.

## Curation Notes

- The specific enzyme MFs are retained as core. Generic catalytic parents,
  broad process parents, duplicate cytoplasm/cytosol terms, cofactors, and
  complex-membership annotations are treated as secondary or redundant.
- `ilvH` does not itself catalyze acetolactate formation; its existing catalytic
  MF assignment is removed in favor of the specific regulator MF.
- `leuA` does not perform acetyl-CoA C-acetyltransferase chemistry; that
  thiolase-family annotation is removed while 2-isopropylmalate synthase is
  retained.
- The exact Q88CQ2 IlvD record assigns a 2Fe-2S cluster plus magnesium, so the
  reusable module records the required iron-sulfur cofactor generically rather
  than importing either that target-specific nuclearity or the 4Fe-4S cluster
  often described for other IlvD family members. Direct Q88CQ2 cofactor
  characterization remains a knowledge gap.
- For both IlvA paralogs, TreeGrafter serine/threonine-catabolic process calls
  are marked over-annotated rather than removed: threonine is broken down by
  the reaction, but the supported core physiological role is 2-oxobutanoate
  supply for isoleucine synthesis rather than a dedicated catabolic pathway.
- The module report and eight gene reports completed successfully. Requests for
  `ilvA-II`, `ilvD`, and `leuA` reached OpenScientist's 3600-second service
  ceiling and were cancelled without output. Their notes record the failures;
  no provider-named report was fabricated, and their reviews remain grounded
  in exact UniProt/family evidence plus the successful module report.

## Validation

Final LinkML, ontology-aware module-validator, and all 11 selected gene-review
validations pass after research integration. A full `just validate-all` run
also passed with 3693/3693 gene reviews valid, zero invalid files, zero errors,
and all 53 pathway markdown files with PMID references valid. Repository-wide
advisory warnings remain non-blocking and are unrelated to this batch.

## 2026-09-01 Repair Checkpoint

- Added reviewed non-KT2440 exemplars across the pathway so the reusable
  module is not grounded only by the PSEPK instance.
- Added five activity-specific PAINT IBD nodes whose experimental seed lists
  support the corresponding leaf functions. The IlvH catalytic PAINT
  assertion, the GO:0009099 process assertion at the same node, and the broad
  IlvD lyase node were inspected but deliberately not promoted. For
  PTN000767018, the local export does not establish Q88DY9 descent, and its
  catalytic assertion is inappropriate for the non-catalytic small subunit.
- Replaced affected legacy selectors with exact PANTHER subfamilies where
  local member containment is confirmed. IlvI retains the more precise
  `NCBIfam:TIGR00118`; IlvE records two exact PANTHER subfamilies because its
  reviewed bacterial exemplars occupy distinct lineages.
- Changed the IlvA-to-IlvIH relationship to `PROVIDES_INPUT_FOR`: IlvA supplies
  the isoleucine-specific 2-oxobutanoate input, while valine synthesis enters
  IlvI-IlvH from pyruvate without an IlvA prerequisite.
- Restored explicit supporting evidence for retained non-core localization
  annotations in ilvH, leuA, and leuB. The ilvD cytosol call remains non-core,
  with its reason explicitly limited to TreeGrafter propagation because no
  independent UniProt localization statement is available.
- Re-ran the PANTHER member refresh. It confirms the actual second IlvA
  accession, Q88CN1, in `PTHR48078:SF11`; no Q88CJ4 module member exists.
