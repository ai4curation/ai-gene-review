# sakA re-review notes

## 2026-11-02 PTHR24055 fungal HOG MAPK review

- `sakA` encodes the Hog1/Sty1-family stress-activated MAPK in Aspergillus
  fumigatus. The protein is a canonical MAPK in the broad `PTHR24055`
  family: the root `PANTHER:PTN000622075` placements for Ser/Thr kinase
  chemistry, cytoplasm, and nucleus all fit SakA and are directly reinforced by
  A. fumigatus literature.
- The fungal stress-MAPK node `PANTHER:PTN001172058` is also appropriate for
  SakA. It is the fungal Hog1/Sty1 branch, not a whole-family MAPK node, and
  the short donor list is not a weakness under the IBA review policy. SakA is a
  direct experimental descendant for the oxidative-stress placement, and the
  osmosensory and stress-activated MAPK cascade placements match the same HOG
  clade.
- PMID:16702099 is abstract-only in the local cache but directly tested a
  `sakA` mutant: the abstract reports reduced growth and increased inhibition
  in the presence of hydrogen peroxide, menadione, or SDS. That supports the
  A. fumigatus oxidative-stress IMP row and corroborates the oxidative-stress
  IBA.
- PMID:26878695 is also abstract-only locally, but its abstract is direct and
  gene-specific: `sakA` and double `mpkC sakA` mutants were hypersensitive to
  osmotic, oxidative, and cell-wall stresses; SakA::GFP and MpkC::GFP
  translocated to the nucleus under osmotic and cell-wall stress; loss of SakA
  reduced MpkA phosphorylation; and the double mutant attenuated fungal burden
  in a neutropenic mouse infection model.
- The older MpkC paper PMID:16998074 included the sakA/hogA deletion strain and
  compared `sakA` and `mpkC` expression after hypertonic and oxidative stress,
  but it is primarily an `mpkC` carbon-source paper. I retained the AspGD
  osmotic-stress rows because they are plausible full-text curations and are
  now corroborated by the 2016 SakA/MpkC paper, the SchA paper, and the 2017
  osmotic-stress transcriptome paper.
- PMID:22678624, supporting the heat-response IMP row, is abstract-only and its
  visible SakA-specific result is increased SakAp after cold, nystatin, and DMSO
  treatment rather than the exact heat-response assay behind AspGD's
  annotation. I left `GO:0034605 cellular response to heat` `UNDECIDED`, by the
  same standard used for the abstract-only AspGD thermal-stress rows on
  `ASPFU/mpkA`.
- Newer papers reinforce SakA as the main A. fumigatus HOG effector rather than
  changing the core annotation set. PMID:27706915 shows independent and
  collaborative SakA/MpkC control of the transient osmotic-stress transcriptome;
  PMID:30538182 ties SakA and MpkC to PKA-dependent glycogen/trehalose
  mobilization for cell-wall carbohydrate supply; PMID:31134001 validates
  stress-dependent physical associations between SakA and MpkC and,
  during cell-wall stress, SakA with MpkA and the PtcB phosphatase; and
  PMID:32743127 links SakA/MpkC to adhesion, cell-surface composition,
  extracellular-matrix production, and biofilm formation.
- `just deep-research-falcon ASPFU sakA` failed in this environment because
  `agentapi` was not in `PATH` and the Falcon provider was unavailable. I used
  this notes file instead of creating a provider-named deep-research artifact.

## 2026-11-02 follow-up

- Reconciled the `GO:0034605 cellular response to heat` IMP row with the
  curated UniProt record rather than leaving it `UNDECIDED`: the `CC:PTM`
  statement explicitly includes high-temperature stress among conditions that
  modulate SakA phosphorylation, and `CC:DISRUPTION PHENOTYPE` records conidial
  heat sensitivity for the sakA/mpkC deletion study. The row is therefore
  supportable as `KEEP_AS_NON_CORE`; `ASPFU/mpkA` should be rechecked by the
  same standard before treating its abstract-only heat-stress rows as truly
  unresolved.
