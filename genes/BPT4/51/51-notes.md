# Bacteriophage T4 Gene 51 (gp51) — Curation Notes

## Summary of Gene Function
Bacteriophage T4 gene `51` encodes the baseplate hub assembly chaperone gp51 (UniProt `P17173`, 249 amino acids, ~29.3 kDa). Classical T4 morphogenesis genetics identified gene 51 among the essential "group II" baseplate hub genes (alongside genes 5, 26, 27, 28, and 29) required for formation of the central hub/plug of the T4 tail baseplate.

## Catalytic/Chaperone Activity and Absence from Mature Virions
- **Hub Assembly Chaperone**: Unlike stoichiometric structural subunits of the hub (such as gp5, gp27, and gp29), classic in vitro complementation and dilution-kinetics experiments (Snustad 1968; Kozloff 1981; Matsui et al. 1997; Leiman et al. 2010, PubMed 21129200) showed that gp51 acts catalytically or as a transient assembly chaperone at extremely low intracellular copy numbers (~35 molecules per infected cell, due to translational repression by an RNA hairpin spanning the gene 51 Shine-Dalgarno sequence and initiation codon).
- **Non-Structural Role**: Authoritative reviews and high-resolution cryo-EM reconstructions of the T4 baseplate (PubMed 27193680) confirm that gp51 is absent from the mature assembled baseplate and virion, functioning in the infected *Escherichia coli* cytoplasm to promote maturation and assembly of the central baseplate hub precursor.

## Annotation Review Notes
- `GO:0098003` (`viral tail assembly`, IEA from `GO_REF:0000043`): Directly supported by genetic, biochemical, and morphogenesis evidence establishing that gp51 is an essential chaperone required for formation of the central hub of the T4 tail baseplate (`ACCEPT`).
- **Omission of `molecular_function` in `core_functions`**: Although classic dilution-kinetics studies described gp51 as acting "catalytically" (i.e. sub-stoichiometrically) and UniProt describes it as a hub assembly chaperone, neither a specific enzymatic reaction nor direct polypeptide-folding chaperone activity (`GO:0044183`) has been biochemically demonstrated for gp51 (see `suggested_questions`). Therefore `molecular_function` is intentionally left unset in `core_functions`, with the core role captured by `directly_involved_in: GO:0098003` (`viral tail assembly`).
