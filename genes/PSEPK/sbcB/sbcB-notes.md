# sbcB curation notes

Q88N51 has exact Exonuclease I chemistry (EC 3.1.11.1), 3'-to-5'
single-stranded DNA degradation, and an SSB-interaction prediction. The
InterPro-derived RNA exonuclease annotation was removed because it conflicts
with the substrate-specific record. A mismatch-repair role remains a candidate
module implementation, not a gene-level claim.

## OpenScientist adjudication

The OpenScientist report corroborated the Mg-dependent, processive 3'-to-5'
single-stranded-DNA exonuclease reaction and SSB interaction from the exact
record and characterized orthologs. Its mismatch-repair discussion is not
target-specific and includes evidence from non-Pseudomonas and eukaryotic ExoI
systems, so it does not justify adding mismatch repair as a core Q88N51
process.

The cached parent `PTHR11046` artifacts are retained as negative provenance:
the parent spans oligoribonuclease and Exonuclease I subfamilies, whereas
Q88N51 and the module's SbcB selector use the function-specific
`PTHR11046:SF11` Exonuclease I subfamily.
