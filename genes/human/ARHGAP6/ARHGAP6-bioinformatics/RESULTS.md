# ARHGAP6 bioinformatics: the RhoGAP catalytic arginine finger, with controls

## Question

ARHGAP6 is reported to have two separable activities: RhoA-GAP activity, and a
GAP-*independent* actin-remodelling / process-outgrowth activity. Both the
original functional study (PMID:10699171) and the later HERG study
(PMID:19038263) separate them with the same instrument -- an R433G mutant of the
catalytic arginine finger. So: **does ARHGAP6 actually carry that arginine, and
does the answer settle whether it is an active GAP?**

The second half of the question is the point. A retained catalytic residue is
not evidence of activity, and a substituted one is not proof of its absence.
The panel below was chosen to contain counterexamples in both directions.

## Method

`check_arginine_finger.py` computes everything from live primary sources; no
finding is hardcoded.

1. **Anchor.** ARHGAP1/p50RhoGAP (UniProtKB:Q07960), whose arginine finger is
   resolved in the RhoA transition-state complex **PDB 1TX4**.
2. **The anchor position is verified against the structure, not asserted.** The
   script downloads 1TX4, reads chain A's author-numbered
   CA residues, and requires that the +/-6 window around the literature position
   matches the corresponding UniProt window residue-for-residue. A mismatch is a
   non-zero exit, so an unverifiable position is never reported.
3. **Mapping.** Each panel member's UniProt-annotated Rho-GAP domain is aligned to
   the anchor's (global Needleman-Wunsch, BLOSUM62, gap -11/-1) and the residue in
   the anchor's arginine column is read off in the member's own numbering.
4. **Cross-check.** That call is compared against UniProt's own `Arginine finger`
   SITE feature. Agreement of two independent methods is the evidence.
5. **Curated activity.** QuickGO is queried live for each member's
   `GO:0005096` (GTPase activator activity) rows, **including the NOT qualifier**.

```
uv run check_arginine_finger.py             # regenerate this file
uv run check_arginine_finger.py --self-test # guards + controls
```

## Anchor verification (run 2026-09-18)

- `1TX4` chain A author residue **85** is **ARG**.
- Window around it: `TTEGIFRRSANTQ`
- UniProtKB:Q07960 (sequence version 1) window around
  position **282**: `TTEGIFRRSANTQ`
- The two windows are identical, so the structurally resolved arginine finger of
  p50RhoGAP is UniProt position **282** (the literature's "Arg85"
  is construct numbering, offset by
  197).

## Result (run 2026-09-18)

| protein | acc (sv) | Rho-GAP domain | residue in the anchor's arginine column | UniProt `Arginine finger` site | agree? | call | curated GO:0005096 |
|---|---|---|---|---|---|---|---|
| ARHGAP6 | O43182 (sv3) | 401-602 | R433 | R433 | yes | RETAINED | enables (IBA, GO_REF:0000033, GO_Central); enables (IEA, GO_REF:0000107, Ensembl); enables (TAS, Reactome:R-HSA-8981637, Reactome); enables (TAS, Reactome:R-HSA-9018806, Reactome) |
| Arhgap6 (mouse) | O54834 (sv3) | 403-604 | R435 | R435 | yes | RETAINED | enables (IBA, GO_REF:0000033, GO_Central); enables (IDA, PMID:10699171, MGI); enables (IDA, PMID:25211221, MGI) |
| ARHGAP1 | Q07960 (sv1) | 244-431 | R282 | R282 | yes | RETAINED | enables (IBA, GO_REF:0000033, GO_Central); enables (IDA, PMID:8253717, MGI); enables (IDA, PMID:8288572, MGI); enables (IEA, GO_REF:0000120, UniProt); enables (TAS, PMID:8288572, PINC); enables (TAS, Reactome:R-HSA-9013022, Reactome); enables (TAS, Reactome:R-HSA-9013111, Reactome); enables (TAS, Reactome:R-HSA-9013161, Reactome); enables (TAS, Reactome:R-HSA-9013437, Reactome); enables (TAS, Reactome:R-HSA-9014295, Reactome); enables (TAS, Reactome:R-HSA-9017488, Reactome); enables (TAS, Reactome:R-HSA-9018745, Reactome); enables (TAS, Reactome:R-HSA-9018806, Reactome); enables (TAS, Reactome:R-HSA-9693282, Reactome) |
| ARHGAP36 | Q6ZRI8 (sv1) | 226-426 | T258 | T258 | yes | **SUBSTITUTED (R->T)** | enables (IBA, GO_REF:0000033, GO_Central) |
| ARHGAP11B | Q3KRB8 (sv1) | 49-250 | R87 | R87 | yes | RETAINED | **NOT**|enables (IDA, PMID:25721503, UniProt); **NOT**|enables (IDA, PMID:27957544, UniProt); enables (TAS, Reactome:R-HSA-8981637, Reactome) |
| ARHGAP35 | Q9NRY4 (sv3) | 1249-1436 | R1284 | R1284 | yes | RETAINED | enables (IBA, GO_REF:0000033, GO_Central); enables (IDA, PMID:19673492, UniProt); enables (IEA, GO_REF:0000120, UniProt); enables (TAS, Reactome:R-HSA-416559, Reactome); enables (TAS, Reactome:R-HSA-9013437, Reactome); enables (TAS, Reactome:R-HSA-9014295, Reactome); enables (TAS, Reactome:R-HSA-9014434, Reactome); enables (TAS, Reactome:R-HSA-9017488, Reactome); enables (TAS, Reactome:R-HSA-9018806, Reactome) |
| OCRL | Q01968 (sv3) | 721-901 | Q757 | Q757 | yes | **SUBSTITUTED (R->Q)** | enables (IDA, PMID:12915445, FlyBase) |
| INPP5B | P32019 (sv4) | 821-993 | Q852 | Q852 | yes | **SUBSTITUTED (R->Q)** | _none_ |

## Interpretation

**ARHGAP6 retains the arginine finger.** The alignment to the structurally
resolved anchor and UniProt's own SITE feature independently place it at
**R433**, and that is the residue PMID:19038263 names when it states that
"Mutation of the conserved arginine at position 433 to a glycine (R433G)
abolishes the rhoGAP activity of ARHGAP6". Three independent lines -- structure-
anchored alignment, UniProt feature, and a published point mutant -- agree on the
same position, which is as well-grounded as this kind of call gets.

**But retention does not establish activity, and the panel shows why.** In this
superfamily the residue column and the curated-activity column come apart in both
directions:

- *Residue intact, activity curated absent.* ARHGAP11B keeps the arginine finger
  and nonetheless carries curated `NOT|enables GO:0005096` annotations. Retention
  is compatible with a protein that has been experimentally shown not to be a GAP.
- *Residue substituted, activity curated present.* ARHGAP36 -- ARHGAP6's closest
  paralog, sharing InterPro IPR037863 (RHOGAP6/36) -- has a threonine in the
  arginine column, yet carries a positive `enables GO:0005096`. OCRL, whose
  RhoGAP-like domain is the textbook dead one, substitutes a glutamine and still
  carries a positive IDA.

So the residue check is **consistent with** ARHGAP6 being a real RhoA GAP and it
removes one way the GAP claim could have been wrong, but on its own it settles
nothing. What actually supports the GAP call is the functional evidence: the
R433G mutant fails to clear stress fibres while wild-type ARHGAP6 clears them
(PMID:10699171).

**The same panel is what makes the separability claim interesting rather than
trivial.** Because R433G is a clean loss-of-GAP reagent, the phenotypes that
survive it are evidence of a genuinely GAP-independent output -- process outgrowth
(PMID:10699171) and HERG downregulation (PMID:19038263, where the R433G mutant
reduces HERG current as well as wild-type). That is an argument from a mutant that
works, not from a residue that is present.

## Caveats

- The dead controls are dead by *literature reputation* plus residue substitution;
  the positive GO rows they carry (OCRL IDA, ARHGAP36 IBA) are exactly the
  discrepancy being displayed, not an endorsement of those annotations. This
  script does not adjudicate them and no conclusion here depends on doing so.
- Domain boundaries are UniProt's. A member whose Rho-GAP domain is unannotated
  would be reported as `n/a` rather than guessed.

