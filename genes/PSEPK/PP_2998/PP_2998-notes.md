# PP_2998 curation notes

## Ketopantoate-reductase assignment

Q88IK1 is a 315-aa ApbA-fold oxidoreductase assigned to
PANTHER `PTHR21708:SF26` and InterPro `IPR051402` (KPR-related), not to the
canonical PanE family `PTHR43765`/`IPR050838`. Its ketopantoate reaction and
pantothenate-pathway placement are computational transfers.
[file:PSEPK/PP_2998/PP_2998-uniprot.txt "DR   InterPro; IPR051402;
KPR-Related."]

The same broad PANTHER subfamily includes the experimentally characterized
*Pseudomonas aeruginosa* PaKPR2, which has lost activity toward ketopantoate and
instead reduces several alpha-keto acids. [PMID:38962820 "this structural
modification made the protein active against several important alpha-keto-acid
substrates"]

The broad family also contains proteins annotated as bona fide ketopantoate
reductases, and PP_2998 is not the reciprocal-best-BLAST KT2440 ortholog of
PaKPR2 in OrtholugeDB. [OrtholugeDB PA1752 ortholog query](https://pseudoluge.pseudomonas.com/named/list/search?field=locus_tag&value=PA1752)
The family-level evidence therefore does not resolve Q88IK1 substrate
specificity. The specific molecular-function and pantothenate-process
annotations should remain `UNDECIDED` pending direct biochemistry or a close
experimentally characterized ortholog.

## OpenScientist report discrepancy

The gene-level OpenScientist report assigns Q88IK1 as PanE from the electronic
UniProt/EC record, conserved fold features, and 28.9% identity to *E. coli*
PanE. It does not resolve the functional heterogeneity of `PTHR21708:SF26`, and
it explicitly acknowledges that no direct experiment has tested the KT2440
protein. [file:PSEPK/PP_2998/PP_2998-deep-research-openscientist.md "No direct
experimental data on the *P. putida* protein."]

Unlike PP_2325, Q88IK1 is not the reciprocal-best KT2440 ortholog of the
experimentally inactive PaKPR2. The available evidence therefore supports
neither confident acceptance nor confident removal of the substrate-specific
annotations. The report is retained as retrieval provenance, while the review
keeps those annotations `UNDECIDED` and records only the broad oxidoreductase
function as supported.
