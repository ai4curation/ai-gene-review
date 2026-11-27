# ppc1 (Q9USK7, SPCC4B3.18) notes

Role: phosphopantothenoylcysteine synthetase (PPCS); module `coenzyme_a_biosynthesis`.
Fetch: `just fetch-gene SCHPO ppc1` FAILED (UniProt entry YJ2I_SCHPO is still "Uncharacterized protein C4B3.18" with no gene name); refetched with `-u Q9USK7`.

## Evidence
- [PMID:23091701 "We isolated a novel S. pombe temperature-sensitive strain ppc1-537 mutated in the catalytic region of phosphopantothenoylcysteine synthetase (designated Ppc1), which is essential for CoA synthesis."]
- [PMID:23091701 "The mutant becomes auxotrophic to pantothenate at permissive temperature, displaying greatly decreased levels of CoA, acetyl-CoA and histone acetylation."]
- [PMID:23091701 "It is similar to human PPCS (amino acid identity 42%) and budding yeast Cab2 (identity 45%)."]
- Whole-cell GFP localisation (cytoplasm + nucleus) [PMID:23091701].
- UniProt PANTHER family PTHR12290 carries the name "CORNICHON-RELATED" (a PANTHER family-name quirk); the module correctly uses subfamily PTHR12290:SF2.
- Nucleotide specificity (ATP vs CTP) unknown for the S. pombe enzyme.

## Decisions
- Nucleus rows non-core (nuclear phenotypes are secondary to low acetyl-CoA). All MF/BP/cytoplasm rows accepted.
- Core: GO:0004632 / GO:0015937 / GO:0005829 — matches S. cerevisiae CAB2 review (no CoA-SPC complex term: no S. pombe evidence).
