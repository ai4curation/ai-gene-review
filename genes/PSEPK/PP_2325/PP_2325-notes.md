# PP_2325 curation notes

## Ketopantoate-reductase assignment

Q88KG5 is a 315-aa ApbA-fold oxidoreductase assigned to
PANTHER `PTHR21708:SF26` and InterPro `IPR051402` (KPR-related), rather than the
canonical PanE family `PTHR43765`/`IPR050838` represented by KT2440 PanE
Q88N64. The current enzyme name, EC 1.1.1.169, Rhea reaction, and pantothenate
pathway assignment are all computational transfers. [file:PSEPK/PP_2325/PP_2325-uniprot.txt
"DR   PANTHER; PTHR21708:SF26; 2-DEHYDROPANTOATE 2-REDUCTASE; 1."]

The experimentally studied *Pseudomonas aeruginosa* second ketopantoate
reductase copy, PaKPR2/PA1752 (Q9I2Y5), is in the same PANTHER subfamily.
OrtholugeDB identifies PP_2325 as the reciprocal-best-BLAST ortholog of PA1752
in KT2440. [OrtholugeDB PA1752 ortholog query](https://pseudoluge.pseudomonas.com/named/list/search?field=locus_tag&value=PA1752)
Structural and biochemical analysis found that PaKPR2 is inactive toward the
natural ketopantoate substrate and instead reduces multiple alpha-keto acids.
[PMID:38962820 "resulting in its inactivity toward the natural substrate
ketopantoate"]

This is strong evidence against treating the automated substrate-specific GO
annotation as established for PP_2325, but it is still ortholog transfer rather
than a direct assay of Q88KG5. The first-pass review should therefore remove the
specific ketopantoate/pantothenate assertions while describing the supported
core only as a KPR-related alpha-keto-acid oxidoreductase of unresolved native
substrate.

## OpenScientist report discrepancy

The gene-level OpenScientist report recapitulates the UniProt/KEGG PanE label
from generic ApbA-family signatures and approximately 27% identity to *E. coli*
PanE. It did not retrieve or evaluate the 2024 PaKPR2 biochemical study or the
OrtholugeDB reciprocal-best relationship to PA1752, and it explicitly notes
that there is no direct PP_2325 experiment.
[file:PSEPK/PP_2325/PP_2325-deep-research-openscientist.md "No direct
experimental characterization of PP_2325."]

For substrate-specific curation, the closer experimentally characterized
Pseudomonas ortholog is more informative than a distant generic family match.
The report is retained as retrieval provenance, but its PanE conclusion is not
adopted.
