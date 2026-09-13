# davD curation notes

- Reviewed UniProtKB assigns Q88RC0 by similarity to oxidation of
  5-oxopentanoate with NADP+
  [file:PSEPK/davD/davD-uniprot.txt, "Reaction=5-oxopentanoate + NADP(+) + H2O
  = glutarate + NADPH + 2 H(+)"].
- KT2440 fitness profiling connects `davD` to the 5AVA branch
  [PMID:31064836, "Only 3 genes shared fitness defects between 5AVA and
  l-lysine (davT, davD, and lghO)"].
- Succinate-semialdehyde dehydrogenase activity is removed because it specifies
  the wrong aldehyde substrate. The broader GABA-catabolism claim remains
  undecided because Q88RC0 has not been tested with succinate semialdehyde.
- The OpenScientist report generalized an NAD-dependent ortholog while the
  exact record assigns NADP dependence by similarity. Direct Q88RC0 cofactor
  preference has not been measured, so neither source establishes strict
  NAD-versus-NADP specificity.
- The electronic cytosol annotation is plausible but has no direct localization
  evidence [file:PSEPK/davD/davD-uniprot.txt, "GO; GO:0005829; C:cytosol"]. It
  is retained as non-core and omitted from the synthesized core function.
- Purified-enzyme substrate and cofactor panels would quantify discrimination
  against succinate semialdehyde and NAD+.
