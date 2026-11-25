# ilvC (P05793, E. coli K-12) review notes

No provider deep research was run for this gene. These notes are my own,
from the cached publications, the UniProt record (`ilvC-uniprot.txt`) and the
existing reviews of the same step (`genes/PSEPK/ilvC`, `genes/yeast/ILV5`,
`genes/SCHPO/ilv5`). P05793 is the reference protein of PANTHER PTHR21371
(family review `interpro/panther/PTHR21371/PTHR21371-review.yaml`).

## Function

- Class II (long-form, 491 aa) ketol-acid reductoisomerase, EC 1.1.1.86:
  "a bifunctional enzyme that catalyzes two quite different reactions at a
  common active site; an isomerization consisting of an alkyl migration,
  followed by an NADPH-dependent reduction of a 2-ketoacid" [PMID:15654896].
  Converts (S)-2-acetolactate to (R)-2,3-dihydroxyisovalerate (valine branch)
  and 2-aceto-2-hydroxybutanoate to (2R,3R)-2,3-dihydroxy-3-methylpentanoate
  (isoleucine branch) [UniProt CATALYTIC ACTIVITY; the second reaction is
  HAMAP-rule evidence].
- Mg2+: "Starting with acetolactate, Mg2+ is the only divalent metal ion that
  will support enzyme catalysis" [PMID:2653423]; a hydroxide bridging two Mg2+
  ions initiates the isomerisation [PMID:27136273]; crystal structure with Mg2+
  and NADPH, tetramer in solution [PMID:23036858].
- NADPH: Arg68/Arg76 contact the 2'-phosphate; mutation reverses cofactor
  specificity [PMID:9015391]; engineered NADH-preferring variants used for
  isobutanol production [PMID:21515217].
- Secondary activity: "The reductase activity is shown to be relatively
  nonspecific and is capable of utilizing a variety of 2-ketoacids"
  [PMID:15654896], including 2-ketopantoate (UniProt kinetics: Km 0.17 mM,
  Vmax 0.196 vs 2.25 umol/min/mg for acetolactate). In vivo, "an E. coli ilvC
  panE double mutant completely lacking ketopantoate reductase activity" was
  needed to remove ketopantoate reductase activity [PMID:10553653], i.e. IlvC
  contributes alongside the dedicated PanE. Treated as a genuine secondary
  activity (KEEP_AS_NON_CORE) per the promiscuous-activity tiers.
- Genetics: classic ilv mutants [PMID:14832239, no abstract cached].
- Location: soluble/cytoplasmic (UniProt SUBCELLULAR LOCATION, ECO:0000305 of
  PMID:2653423); cytosol proteomics IDA [PMID:18304323; IlvC is not named in
  the cached text, which lists results in supplementary tables].

## Decisions consistent with sibling reviews

- Cofactor-binding rows (Mg, NADP) kept as non-core, as in KT2440 IlvC.
- Broad BCAA biosynthetic process accepted: IlvC acts in the shared trunk
  whose product 2-oxoisovalerate also feeds leucine; yeast ILV5 and pombe ilv5
  accept the same term.
- Oxidoreductase activity modified to ketol-acid reductoisomerase activity.
