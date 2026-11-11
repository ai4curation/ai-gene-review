# pssA (Bacillus subtilis 168, P39823) notes

## Deep research status

`just deep-research-falcon BACSU P39823 --alias pssA` was run on 2026-11-09
and failed authentication ("falcon: 403 Failed to authenticate"). No provider
file exists and none was written by hand. `just mod-description-deep-research
BACSU pssA` reports no MOD provider for BACSU.

## Literature checked

- PMID:8002567 (abstract cached): the B. subtilis pss gene was cloned by
  complementing the temperature sensitivity of an E. coli pssA1 mutant; it
  encodes a 177-residue, very hydrophobic, multi-pass membrane protein with
  homology to yeast phosphatidylserine synthase and none to E. coli PssA;
  manganese-dependent PS synthase activity is found exclusively in the
  membrane fraction; overproduction raises phosphatidylethanolamine to 93% of
  phospholipid
  [PMID:8002567 "A manganese-dependent phosphatidylserine synthase activity, a characteristic of the B. subtilis enzyme, was found exclusively in the membrane fraction of E. coli (pssA1) cells harboring a B. subtilis pss plasmid."].
- PMID:27362352: UniProt cites it only for a disruption phenotype (cells
  appear normal, no effect on flotillin clusters).
- PMID:39693441: places Gram-positive PssA in the type-II (integral-membrane,
  CDP-alcohol phosphotransferase, metal-dependent) class.

## Interpretation

P39823 is the type-II phosphatidylserine synthase of B. subtilis (PTHR14269,
subfamily SF59; IPR004533; TIGR00473). The heterologous expression data
establish its activity; the pathway step is shared with E. coli PssA despite
unrelated folds.
