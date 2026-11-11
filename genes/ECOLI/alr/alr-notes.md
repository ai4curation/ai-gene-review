# alr (Escherichia coli K-12, P0A6B4) notes

## Provenance

- Provider deep research (`just deep-research`) was **not** run for this gene; no
  `alr-deep-research-*.md` file exists. These notes summarise manual reading of
  the cached publications (all abstract-only) and the UniProt record.
- `just paint-losses ECOLI alr`: no IRD or IKR loss on the lineage.

## Literature summary

- Activity: Alr interconverts L- and D-alanine
  [PMID:18434499 "Alanine racemase (Alr) is an important enzyme that catalyzes the interconversion of L-alanine and D-alanine, an essential building block in the peptidoglycan biosynthesis."].
  Kinetics in both directions were measured on the E. coli biosynthetic enzyme
  [PMID:18434499 "decrease the turnover numbers in both D- to L-Ala and L- to D-Ala directions"];
  UniProt records Km 0.31 mM (D-Ala) and 1 mM (L-Ala) from this study
  [file:ECOLI/alr/alr-uniprot.txt "KM=0.31 mM for D-alanine"].
- Structure: native, D-cycloserine-bound and mutant crystal structures
  [PMID:18434499 "we fully analyzed the crystal structures of the native, the D-cycloserine-bound, and four mutants (P219A, E221A, E221K, and E221P) of biosynthetic Alr from Escherichia coli (EcAlr)"].
  The active site uses residues from the opposite monomer
  [PMID:18434499 "cooperation of the positively charged Arg280 and Arg300 on the opposite monomer"].
  PLP is bound to Lys34 [file:ECOLI/alr/alr-uniprot.txt "N6-(pyridoxal phosphate)lysine"].
- Oligomeric state: monomer-dimer equilibrium, dimerization constant correlates
  with Vmax [PMID:20971724 "All alanine racemases were proved to be in a dynamic equilibrium between monomeric and dimeric form with every methods used in this study."].
- Physiology: E. coli has two racemases (alr, dadX); only the double mutant is
  D-alanine requiring [PMID:11267762 "A D-alanine requiring double knock-out mutant of E. coli (alr, dadX) was constructed"].
  UniProt: [file:ECOLI/alr/alr-uniprot.txt "Provides the D-alanine required for cell wall biosynthesis."]
- PMID:4594607 (Wijsman 1972, alanine racemase mutant): cached record has no
  abstract; not readable here. IMP row accepted in deference to the curator.

## Curation decisions

- Core: alanine racemase activity; D-alanine biosynthetic process and
  peptidoglycan biosynthetic process (D-Ala supply step, same treatment as murI);
  cytosol (IBA; consistent with function, no signal peptide).
- PLP binding (IBA/IDA/IEA) and homodimerization (IEA/IPI): KEEP_AS_NON_CORE.
- catalytic activity IEA: MODIFY to alanine racemase activity.
