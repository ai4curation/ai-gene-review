# na (narrow abdomen) review notes

UniProt A8JUW5 (Sodium leak channel NALCN), FBgn0002917 region; sole fly NALCN-family member (CG1517, Dmalpha1U).

## Literature journal

- Identity and expression: na corresponds to CG1517/Dmalpha1U and is expressed in the neuropil
  [PMID:12498692 "this conserved family's sole Drosophila member, a gene known both as CG1517 and as Dmalpha1U, is shown to correspond to the narrow abdomen (na) gene"]
  [PMID:12498692 "the channel is expressed in the neuropil of the central complex and optic lobe"].
- Light/locomotor phenotype: [PMID:12498692 "mutant flies have an inversion of relative locomotor activity in light versus dark"].
- Circadian output: NA acts in pacemaker neurons downstream of the clock
  [PMID:16364900 "Oscillations of the clock protein PERIOD are intact in na mutants, indicating an output role."]
  and pore residues are needed for rescue [PMID:16364900 "Pore residues are required for robust rescue consistent with NA action as an ion channel."]
  (abstract-only cache).
- DN1p neurons: [PMID:20362452 "Mutants of a novel ion channel, narrow abdomen (na), lack a robust increase in activity in response to light and show reduced anticipatory behavior and free-running rhythms"].
- Channel activity: NA carries a voltage-independent sodium leak in clock neurons
  [PMID:26276633 "In the morning, a voltage-independent sodium conductance via the NA/NALCN ion channel depolarizes these neurons."]
  [PMID:26276633 "Loss of function na mutants and NALCN knockout result in silent and hyperpolarized neurons."]
- Complex: [PMID:24223770 "Immunoprecipitation experiments also confirm that UNC79 and UNC80 form a complex with NA in the Drosophila brain."];
  loss of any of na/unc79/unc80 lowers all three proteins.
- Mid1 (CG33988) phenocopies na knockdown in locomotor and social clustering assays
  [PMID:24639627 "neurally induced RNAi knockdown of na and CG33988 similarly and significantly suppressed the social clustering"].
- Anesthesia: [PMID:17350263 "the anesthetic signature reflects an evolutionarily conserved role for the na orthologs"].
- Touch: RNAi screen hit in larval class II/III md neurons (PMID:23103192), not followed up.
- Stability: channel complex made in development persists into adults [PMID:28634443 "channel complex proteins produced during development persist in the Drosophila head with little decay for at least 5-7 days in adults"].

## Curation decisions

- Generic ion/cation channel activity rows -> MODIFY to GO:0005272 sodium channel activity (Flourakis 2015).
- Shared complex term GO:0034703 cation channel complex -> MODIFY to GO:0034706 sodium channel complex (same for unc79, unc80, Mid1).
- Rhythmic behavior / circadian behavior -> MODIFY to locomotor rhythm (already annotated).
- Nematode-derived IBA synaptic transmission terms marked as over-annotation.

## Deep research

`na-deep-research-falcon.md` (falcon) arrived after the review was first committed (the recipe reported a 600 s timeout, but the falcon job finished and wrote its report). It agrees with the review: it recommends annotating NA as the pore-forming subunit of a neuronal background channel that conducts a depolarizing Na+ leak across the plasma membrane, acting with UNC79/UNC80 and regulated by Nlf-1, with circadian pacemaker output as the best-demonstrated process. It notes that ion selectivity (PNa ≈ PLi > PK > PCs) has been measured only for vertebrate NALCN, not fly NA. No annotation decision changed.
