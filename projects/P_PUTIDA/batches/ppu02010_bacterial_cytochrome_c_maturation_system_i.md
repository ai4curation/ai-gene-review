---
title: "PSEPK cytochrome c maturation system I"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ccmA, ccmB, ccmC, ccmD, ccmE, ccmF, ccmG, ccmH, cycH]
autolink_gene_symbols: false
---

# PSEPK cytochrome c maturation system I

This batch extracts the Ccm system I machinery from the broad `ppu02010` ABC-transporter bucket. The reusable biological boundary is covalent heme attachment to exported c-type apocytochromes, not generic ABC transport.

- Reusable module: `modules/bacterial_cytochrome_c_maturation_system_i.yaml`
- Reviewed proteins: 9
- Concrete grounding: exact PSEPK UniProt accessions on every module leaf
- Provider: OpenScientist gene, module, and module/pathway/taxon research

## Workflow

- [x] Define a species-neutral, multi-part system I maturation module.
- [x] Separate CcmABCD heme handling from unsupported literal heme-export claims.
- [x] Curate all existing GO annotations and core functions.
- [ ] Integrate completed OpenScientist artifacts.
- [x] Obtain annotation-reviewer audit and sign-off.
- [x] Validate and render all artifacts.
- [ ] Open one draft PR.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---:|---|---|---|---|
| 1 | ATP-dependent CcmAB heme-handling cycle | `ccmA`, `ccmB` | Q88EX5, Q88EX6 | Covered; transported substrate unresolved |
| 1 | CcmE heme loading | `ccmC`, `ccmD` | Q88EX7, Q88EX8 | Covered |
| 2 | Covalent heme chaperoning | `ccmE` | Q88EX9 | Covered |
| 3 | Apocytochrome disulfide reduction/redox preparation | `ccmG`, `ccmH` | Q88EY1, A0A140FWM4 | Covered; exact CcmH contribution unresolved |
| 4 | Heme ligation core | `ccmF`, `ccmH` | Q88EY0, A0A140FWM4 | Covered |
| 4 | Lineage-variable substrate presentation | `cycH` (CcmI-like) | A0A140FWM3 | Accessory role covered |

The PSEPK locus provides all conserved system I functions plus a CcmI-like CycH substrate-presentation factor. CcmH and CycH are distinct proteins and are not treated as alternative names for one product.

## Annotation Decisions

- CcmA retains ATP hydrolysis as its core MF; ATP binding is an uninformative parent.
- `ABC-type heme transporter activity`, `heme transmembrane transporter activity`, and inferred heme-transport processes are removed or downgraded where they encode the obsolete literal-export interpretation of CcmAB.
- CcmC, CcmE, and CcmF retain heme binding in their distinct loading, chaperoning, and ligation roles.
- CcmG retains disulfide oxidoreductase activity; generic oxidoreductase activity and broad cell-redox context are not core.
- CcmH is kept as a distinct CPKC-containing redox/assembly component without assigning an unsupported leaf MF; CycH is the separate CcmI-like TPR protein.
- Function-defining plasma-membrane or periplasm locations are accepted where they position the maturation activity; generic parent membrane and cell-envelope terms remain non-core or over-annotated.
- CycH receives a new cytochrome c biosynthetic process annotation from its CcmI-specific family assignment.

## Boundary

The module starts with CcmABCD-dependent heme handling and CcmE loading, includes reductive preparation of apocytochrome CXXCH motifs, and ends with CcmF/H-dependent heme ligation and optional CcmI-like substrate presentation. Sec-dependent apocytochrome export, DsbD-mediated upstream electron delivery, heme biosynthesis, respiratory-chain assembly, and downstream cytochrome function remain outside this module.

## Research Status

OpenScientist jobs were launched with 7200-second timeouts and are not interrupted by this curation workflow. Completed provider artifacts are integrated before publication; active or rejected jobs are reported on the PR.

## Validation

All nine gene reviews, the reusable module, and this project page are validated and rendered before publication. The GO cache is restored after focused validation.
