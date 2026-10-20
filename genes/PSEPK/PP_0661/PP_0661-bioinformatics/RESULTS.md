# PP_0661 (Q88Q37): comparison with characterized LysR regulators and genomic context

Script: `compare_lysr.py` (run with `uv run compare_lysr.py > compare_lysr_output.txt`).
Raw output: `compare_lysr_output.txt`. Sequences come from UniProt and gene
neighbourhoods from KEGG REST at run time.

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
target genes cannot be transferred from either protein. KEGG assigns PP_0661 to
K03566 (GcvA-like), which it also gives to three other KT2440 regulators
(PP_1393, PP_3143, PP_4107).

## Genomic context

PP_0661 (769408..770292, + strand) lies in a cluster of sulfur amino acid and
threonine metabolism genes, all on the + strand from PP_0658 to PP_0662:
PP_0658 homocysteine S-methyltransferase family protein, PP_0659 cystathionine
gamma-synthase, PP_0660 S-methyl-L-methionine transporter, PP_0662 putative
threonine synthase, with PP_0664 homoserine dehydrogenase further downstream.

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
  does not show, that it regulates sulfur amino acid metabolism. No experiment
  has tested this.
