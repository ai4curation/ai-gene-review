# PP_0661 (Q88Q37): comparison with characterized LysR regulators and genomic context

Script: `compare_lysr.py` (run with `uv run compare_lysr.py > compare_lysr_output.txt`).
Raw output: `compare_lysr_output.txt`. Sequences come from UniProt; gene
neighbourhoods and KO memberships come from KEGG REST at run time.

## Pairwise identity to Swiss-Prot LysR regulators

Local alignment, BLOSUM62, gap open -11 / extend -1:

| Reference | Identity | Aligned pairs |
|---|---|---|
| P24734 AmpR, P. aeruginosa PAO1 | 41.3% | 281 |
| P0A9F6 GcvA, E. coli K-12 | 38.9% | 288 |
| P0A9F9 MetR, E. coli K-12 | 28.2% | 248 |

PP_0661 is roughly equidistant (about 40% identity over the full length) from
AmpR and GcvA. Both belong to the same LysR subgroup (CDD cd08432,
PBP2_GcdR_TrpI_HvrB_AmpR_like). At this level of identity the effector and the
target genes cannot be transferred from either protein.

KEGG KO K03566 ("LysR family transcriptional regulator, glycine cleavage system
transcriptional activator") contains four KT2440 genes: PP_0661, PP_1393,
PP_3143 and PP_4107. So the GcvA-like KO assignment does not single out
PP_0661.

KEGG links two sets of KT2440 glycine cleavage system genes (the GcvA targets in
E. coli): K00605 gcvT (PP_0986, PP_5194), K02437 gcvH (PP_0989, PP_5193) and
K00281 gcvP (PP_0988, PP_5192). Neither set lies in the PP_0656-PP_0665 window
listed below. This analysis did not test which, if any, of the four K03566 regulators controls them.

## Genomic context

PP_0661 (769408..770292, + strand) lies in a cluster of sulfur amino acid and
threonine metabolism genes, all on the + strand from PP_0658 to PP_0662:
PP_0658 homocysteine S-methyltransferase family protein, PP_0659 cystathionine
gamma-synthase, PP_0660 S-methyl-L-methionine transporter, PP_0662 putative
threonine synthase. PP_0663, an AsnC-family transcriptional regulator,
immediately follows PP_0662, and PP_0664 homoserine dehydrogenase lies further
downstream. So this cluster contains a second, unrelated regulator family that
could also control these genes.

The only KT2440 gene in KEGG K01467 (class C beta-lactamase) is PP_2876, about
2.5 Mb away. Its neighbours (PP_2875, protein of unknown function; PP_2877,
SLC10-family transporter) include no LysR regulator. So PP_0661 does not have
the divergent ampR-ampC arrangement that defines AmpR in Enterobacteriaceae and
P. aeruginosa.

## Interpretation (inconclusive on the specific function)

- These results support a LysR-type DNA-binding transcription factor (HTH plus
  substrate-binding domain).
- They do not support the specific name "AmpR". The protein is no closer to
  AmpR than to GcvA, and it is not adjacent to the KT2440 ampC-like gene.
- Its position among methionine and threonine metabolism genes suggests, but
  does not show, that it regulates sulfur amino acid metabolism. A GcvA-like
  role in glycine cleavage regulation is the other homology-based hypothesis.
  No experiment has tested either.
