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

- Reusable module: [bacterial cytochrome c maturation system I](../../../modules/bacterial_cytochrome_c_maturation_system_i.yaml)
- Reviewed proteins: 9
- Concrete grounding: exact PSEPK UniProt accessions on every module leaf
- Provider: OpenScientist gene, module, and module/pathway/taxon research

## Workflow

- [x] Define a species-neutral, multi-part system I maturation module.
- [x] Separate CcmABCD heme handling from unsupported literal heme-export claims.
- [x] Curate all existing GO annotations and core functions.
- [x] Integrate generic and module/pathway/taxon OpenScientist artifacts.
- [x] Obtain annotation-reviewer audit and sign-off.
- [x] Validate and render all artifacts.
- [x] Merge initial curation PR [#2526](https://github.com/ai4curation/ai-gene-review/pull/2526) after three formal review rounds.

## Satisfiability

| Order | Role | PSEPK implementation | UniProt | Decision |
|---:|---|---|---|---|
| 1a | CcmCDE heme transfer and holo-CcmE formation | `ccmC`, `ccmD`, `ccmE` | Q88EX7, Q88EX8, Q88EX9 | Covered |
| 1b | ATP-dependent holo-CcmE processing | `ccmA`, `ccmB` | Q88EX5, Q88EX6 | Covered; transported substrate unresolved |
| 2 | Apocytochrome disulfide reduction/redox preparation | `ccmG`, `ccmH` | Q88EY1, A0A140FWM4 | Covered; architecture-dependent direct substrates retained as a caveat |
| 3 | CcmF/CcmH holocytochrome-c synthase complex | `ccmF`, `ccmH` | Q88EY0, A0A140FWM4 | Covered at complex level |
| 3 optional | Lineage-dependent CcmI/CycH-family maturation support | `cycH` | A0A140FWM3 | Accessory process role covered; direct activity unresolved |

The PSEPK locus provides all conserved system I functions plus a lineage-variable CycH-family accessory. CcmH and CycH are distinct proteins and are not treated as alternative names for one product.

## Annotation Decisions

- CcmA retains ATP hydrolysis as its core MF; ATP binding remains a valid, distinct non-core MF.
- `ABC-type heme transporter activity`, `heme transmembrane transporter activity`, and inferred heme-transport processes are removed where they encode the obsolete literal-export interpretation of CcmAB. The contradictory Rhea/EC heme-export mappings in the unreviewed UniProt records are treated as legacy mappings because direct experiments show CcmAB is dispensable for heme export and instead supports CcmE processing.
- CcmC, CcmE, and CcmF retain heme binding in their distinct loading, chaperoning, and ligation roles.
- CcmG retains disulfide oxidoreductase activity and both membrane-anchor and periplasmic-domain locations. Its module connection to CcmH represents redox cooperation: literature supports direct apocytochrome reduction and resolution of CcmH-linked intermediates rather than one invariant substrate order.
- CcmH is kept as a distinct CPKC-containing redox/assembly component without assigning an unsupported leaf MF; CycH is the separate CycH-family TPR protein.
- Function-defining plasma-membrane or periplasm locations are accepted where they position the maturation activity; generic parent membrane and cell-envelope terms remain non-core or over-annotated.
- CycH receives a conservative new cytochrome c biosynthetic process annotation by ISS from PTHR47870:SF4 and the characterized Bradyrhizobium CycH phenotype (PMID:8231805). Because the subfamily also contains NrfG-family maturation accessories, it supports a shared process role rather than strict one-to-one orthology; no direct MF is assigned.
- GO:0004408 (holocytochrome-c synthase activity) was verified and considered for CcmF, but is not assigned because available evidence supports the CcmF/H ligation machinery without establishing that activity for CcmF alone.
- CcmE retains GO:0017003 because it directly participates in covalent protein-heme linkage; GO:1903607 is used for the other components to identify the product biosynthetic pathway, not as an asserted child of GO:0017004.
- Additional PANTHER fetches PTHR34128, PTHR42852, and PTHR43499 are retained as audit caches but are not module selectors because they do not identify the exact CycH leaf family used here.

## Boundary

The module starts with CcmCDE-dependent heme transfer and holo-CcmE formation,
followed by ATP-dependent CcmAB energy coupling for processing and release. A
CcmG/CcmH thiol-redox branch converges with holo-CcmE at the CcmF/CcmH
holocytochrome-c synthase complex. CcmH is therefore represented in both redox
preparation and ligation, while the CcmI/CycH-family factor is optional.
Sec-dependent apocytochrome export, DsbD-mediated upstream electron delivery,
heme biosynthesis, respiratory-chain assembly, and downstream cytochrome
function remain outside this module.

## Research Status

- Generic module research: [OpenScientist report](../../../modules/bacterial_cytochrome_c_maturation_system_i-deep-research-openscientist.md).
- PSEPK module and pathway research: [OpenScientist report](../deep-research/PSEPK__bacterial_cytochrome_c_maturation_system_i__ppu02010-deep-research-openscientist.md).
- Both jobs use a 7200-second provider allowance and are left running through quiet periods. Provider claims are checked against primary literature, GO, UniProt, and local PANTHER data before affecting the module.
- The taxon-aware run completed in 846 seconds. It confirms complete coverage by
  the nine selected proteins, the PP_5748 CcmH/PP_4320 CcmI-CycH distinction,
  and the external DsbD paralog ambiguity. Its proposed heme-transporter
  annotations for CcmABC are rejected because they conflict with direct
  experiments and the reviewed GOA decisions.
- The generic run completed in 2,202 seconds. It supports the physical CcmABCD
  assembly, CcmE handoff, CcmG/CcmH redox relay, and CcmF/CcmH ligation model.
  Its membrane-trafficking language is interpreted as intramachinery heme
  handling and does not override the evidence against literal CcmAB heme export.

## Wave 124 repair audit

- The mandatory annotation-reviewer pass covered all 46 imported GOA rows plus
  the one proposed CycH process row across `ccmA`, `ccmB`, `ccmC`, `ccmD`,
  `ccmE`, `ccmF`, `ccmG`, `ccmH`, and `cycH`. The GOA-to-review comparison has
  no missing or extra imported rows and no `PENDING` or `UNDECIDED` actions.
- The prior gene-level decisions remain supported, including rejection of the
  literal CcmAB heme-export model and retention of exact ATPase, heme-binding,
  disulfide-oxidoreductase, and maturation-process claims. No gene review edit
  was required.
- The reusable module now has three substantive root operations and two valid
  routes: the canonical CcmABCDEFGH route with or without the optional
  CcmI/CycH-family accessory.
- GO:0018063 provides the specific module-level cytochrome c-heme linkage
  boundary. GO:0004408 is asserted for the terminal CcmF/CcmH complex, not for
  CcmF or CcmH alone. All molecular functions remain on terminal annotons.
- Repetitive plasma-membrane, membrane, periplasm, and cell-envelope location
  assertions were removed from the reusable module. Topology remains explicit
  in role descriptions and in the reviewed PSEPK gene records.
- PANTHER terms are retained only where the official label and PSEPK
  representative-member containment are exact. CcmA, CcmC, CcmE, and CcmG use
  verified InterPro families because their available PANTHER labels are broad
  or misleading for the intended role.
- No PTN is asserted in the module. Available canonical PAINT nodes support
  generic process, location, or broad oxidoreductase claims rather than the
  exact mechanistic leaves modeled here; several current GOA PTN identifiers
  are also absent from the local canonical PAINT index.

## Validation

All nine gene reviews, the reusable module, its two logical routes, and this
project page are validated and rendered before publication. The GO cache is
restored after focused validation.
