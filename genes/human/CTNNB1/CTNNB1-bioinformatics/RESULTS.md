# CTNNB1: taxonomic census of the beta-catenin family (UniProt)

Script: `taxon_census.py` (stdlib only, UniProt REST API). Raw output: `census_output.txt`
(run 2026-10-01).

## Question

Is the beta-catenin family (as defined by PANTHER PTHR45976 "ARMADILLO SEGMENT
POLARITY PROTEIN", which contains human CTNNB1 as PTHR45976:SF4, and InterPro
IPR013284 "Beta-catenin") found outside animals, in particular in the unicellular
holozoans (choanoflagellates, filastereans, ichthyosporeans) or in *Dictyostelium*?

## Results

| Classification | Metazoa | non-Metazoa | Choanoflagellata | Filasterea | Ichthyosporea | *Dictyostelium* |
|---|---:|---:|---:|---:|---:|---:|
| PANTHER PTHR45976 | 4921 | 2 | 0 | 0 | 0 | 0 |
| InterPro IPR013284 | 4937 | 3 | 0 | 0 | 0 | 0 |

- The two non-metazoan PTHR45976 entries are single proteins from land-plant
  genome assemblies (*Sphagnum jensenii* A0ABP0VBH0, *Olea europaea* A0A8S0TRJ0).
  No other plant has one, so these are most likely contaminating animal sequences in
  the assemblies; this was not tested here.
- The extra IPR013284 entry is a chytrid "Vacuolar protein 8" (A0A139A5K2) that
  PANTHER puts in a different family (PTHR47249), so the InterPro signature
  picks up an unrelated ARM protein here.
- *Dictyostelium* Aardvark (Q54I71), the "beta-catenin homologue" of
  PMID:11130075, is placed by PANTHER in **PTHR22895 "ARMADILLO REPEAT-CONTAINING
  PROTEIN 6"**, not in the beta-catenin family.

## Interpretation (limits)

- By current HMM classifications, the beta-catenin family is restricted to animals,
  with no members in choanoflagellates, *Capsaspora* or ichthyosporeans. This agrees
  with gene-family reconstructions that list catenin beta as an animal-specific family
  (PMID:29848444).
- Aardvark is an armadillo-repeat protein that works with a *Dictyostelium*
  alpha-catenin ortholog (PMID:21393547). Database classification does not put it
  in the beta-catenin family. Whether it is a divergent ortholog, an older ARM
  paralog, or a convergent junction protein would need a proper phylogeny of
  ARM-repeat proteins, which was not done here.
- These are classification counts, not a phylogeny. A beta-catenin-like gene that
  is missing from UniProt or classified elsewhere would not be detected.
