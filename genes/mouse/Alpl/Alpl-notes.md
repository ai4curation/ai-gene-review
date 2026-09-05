# Alpl (mouse) — review notes

UniProt: P09242 (PPBT_MOUSE) · tissue-nonspecific alkaline phosphatase (TNAP) ·
MGI:MGI:87983 · PANTHER PTHR11596:SF74 · catalytic Ser110.

Reviewed as the load-bearing ortholog of human ALPL. 98 GOA annotations, the richest
record in the family, and the organism where most of what is believed about this enzyme
was actually established.

## Why this gene was worth reviewing

Almost every annotation I marked `KEEP_AS_NON_CORE` in the human ALPL review is an
orthology transfer of a mouse observation. Reviewing the source lets those be graded on
their real evidence instead of on their evidence code:

- **Mitochondrial localisation, phosphoamidase activity, futile creatine cycle,
  cold-induced thermogenesis** — all four are `IDA` here from PMID:33981039 (Sun et al.,
  Nature 2021) and all four are `ACCEPT`ed. The human rows stay non-core because they are
  ISS/IEA inferences; the mouse rows are the primary evidence. That asymmetry is
  deliberate and is now recorded on both sides.
  [PMID:33981039, "Unlike in other cells, TNAP in thermogenic fat cells is localized to
  the mitochondria, where futile creatine cycling occurs."]
- **Vitamin B6** — the knockout is lethal via seizures [PMID:7550313 title], which is the
  strongest in vivo evidence in the whole family that PLP hydrolysis matters.
- **Bone mineralization** — 11 rows from 8 studies, including the Phospho1/Alpl compound
  ablation that separates initiation inside matrix vesicles from propagation into matrix
  [PMID:14982838, "These data suggest that hypomineralization in TNAP-deficient mice
  results primarily from an inability of initial mineral crystals within MVs to
  self-nucleate and to proliferate beyond the protective confines of the MV membrane."]

## The two REMOVEs — fixing the family's worst error at its source

`GO:0140928 inhibition of non-skeletal tissue mineralization`, IDA **and** IMP, both from
PMID:21490328. This is the origin of the same claim in human and in 30+ other species by
Ensembl Compara orthology.

The paper shows the opposite of what the term asserts:
[PMID:21490328, "Overexpression of TNAP increased calcification of cultured aortas."]

The only inhibitory role it attributes is to PPi, not to the enzyme that destroys PPi:
[PMID:21490328, "The results show that smooth muscle NPP1 and TNAP control vascular
calcification through effects on synthesis and hydrolysis of ePP i , indicating an
important inhibitory role of locally produced PP i ."]

That closing sentence is almost certainly the origin of the error — read quickly it can be
taken as crediting TNAP. Enpp1 and Ank, the other arms of the same study, hold GO:0140928
legitimately. A `proposed_new_terms` entry for the promoting direction is included here as
well as in the human review, since GO has no term for it.

The two IMP rows carry `MGI:MGI:1856651` and `MGI:MGI:2385534` in WITH/FROM. Neither
resolved through MGI, Alliance or QuickGO during this review, so I have not asserted what
they are; the paper's genetic arms are the Enpp1-null and ank/ank strains.

## Citation problems found

Two more, both of the "enzyme used as a reagent or marker" kind that recurs throughout this
family:

1. **`GO:0046677 response to antibiotic`, IDA, PMID:2133555** → UNDECIDED. The paper is
   the mouse preimplantation embryo RT-PCR study. Nothing in the cached record mentions
   antibiotics, selection agents or drug treatment (`grep -iE "antibiotic|G418|geneticin|
   neomycin|puromycin"` returns nothing). This is the *second* bad annotation traced to
   PMID:2133555 — the first was the human ALPP IDA flagged as MISCITED in that review.
2. **`GO:0004035` + `GO:0005886`, IDA, PMID:10787428** → both ACCEPT, citation flagged.
   The paper localises Niemann-Pick C1 protein; alkaline phosphatase appears in it as the
   standard plasma-membrane marker enzyme for fractionation. The localisation row is
   actually well served by that (using an enzyme as a compartment marker presupposes its
   localisation); the *activity* row is a marker assay standing in for a characterisation.

## Judgement calls

- `GO:0055062 phosphate ion homeostasis` and `GO:0055074 calcium ion homeostasis` →
  KEEP_AS_NON_CORE. Both are framed at organismal scale; TNAP acts on the *local*
  extracellular PPi/Pi balance. Serum phosphate is normal or high in hypophosphatasia.
  TNAP handles phosphate esters, not calcium — the calcium effect is downstream.
- `GO:0016462 pyrophosphatase activity` (5 rows) → MODIFY to GO:0004427, same as human.
  The two ISO rows carry a `propagation_review` recording this as
  TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH with the source explicitly marked
  SUPPORTS_TRANSFER — the transfer is fine, the term is one level too high.
- `GO:0003006 developmental process involved in reproduction` (IGI) → KEEP_AS_NON_CORE.
  AP is a classic primordial germ cell marker, but an IGI to a very broad developmental
  term is thin, and nothing else in the record supports a reproductive role.

Three core functions recorded, matching the three genuinely separable roles: PPi hydrolysis
→ mineralization; PLP hydrolysis → vitamin B6 supply; phosphocreatine hydrolysis →
futile creatine cycle. The third has no counterpart in the human core functions, correctly.
