# ura4 (SPCC330.05c, UniProt P14965) notes

Naming trap: S. pombe ura4 = OMP decarboxylase, ortholog of S. cerevisiae URA3 (not URA4). Accession P14965 (PYRF_SCHPO) fetched correctly.

## Evidence
- OMP -> UMP + CO2 [file:SCHPO/ura4/ura4-uniprot.txt "Reaction=orotidine 5'-phosphate + H(+) = UMP + CO2;"].
- Cloned as OMPdecase gene; expressed in S. cerevisiae and E. coli [PMID:2834100 "URA4, the gene coding for orotidine monophosphate decarboxylase (OMPdecase), has been cloned from the fission yeast by homologous complementation"].
- Δura4 accumulates OMP and lyses on polypeptone; complemented by S. cerevisiae URA3 [PMID:23555823 "Finally, the induction of cell lysis in the ura4 deletion mutant was due to the accumulation of orotidine-5-monophosphate."; "cerevisiae URA3 gene (pREP2-URA3), which is a ura4 ortholog."].
- Found in heat-induced protein aggregate centres (mass spec of thermo-unstable proteins) [PMID:32075773 "Using mass spectrometry, we show that thermo-unstable endogenous proteins form PACs as well."]; abstract-only.

## Decisions
- 16 rows: 13 ACCEPT, 2 KEEP_AS_NON_CORE (nucleus HDA; protein aggregate center IDA), 1 MARK_AS_OVER_ANNOTATED (GO:0055086 ARBA).
- Core MF GO:0004590, BP 'de novo' UMP, cytosol; consistent with S. cerevisiae URA3 review.
