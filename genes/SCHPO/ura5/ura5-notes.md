# ura5 (SPBC725.15, UniProt O94331) notes

ura5 = orotate phosphoribosyltransferase; numbering coincides with S. cerevisiae URA5 (also OPRTase; budding yeast has URA5 + URA10 paralogs, pombe has one). Accession O94331 (PYRE_SCHPO) fetched correctly.

## Evidence
- Orotate + PRPP -> OMP + PPi [file:SCHPO/ura5/ura5-uniprot.txt "Reaction=orotidine 5'-phosphate + diphosphate = orotate + 5-phospho-"].
- 5-FOA-resistant mutants map to ura4 or ura5; ura5 cloned as the OPRTase gene [PMID:22198627 "we first determined that 5FOA(R) strains carry mutations in either of two genes; ura4(+) and ura5(+)."].
- Cytosol (+ nucleus) [PMID:16823372].

## Decisions
- 12 rows: 10 ACCEPT, 1 KEEP_AS_NON_CORE (nucleus HDA), 1 MODIFY (pyrimidine ribonucleoside biosynthetic process IBA -> 'de novo' UMP; OMP is a nucleotide), consistent with yeast URA5/URA10 reviews.
- Core MF GO:0004588, BP 'de novo' UMP, cytosol.
