# LOC542140 (A0A804M424) bioinformatics results

Script: `pairwise_identity.py` (Biopython global alignment, BLOSUM62, gap open -10, extend -0.5;
sequences fetched live from UniProt and NCBI). Identity is expressed as identical aligned
residues divided by the query length (748 aa).

| Target | Length | Identical | Identity |
|---|---|---|---|
| ZmGT1 FJ573212 (ACL82964.1) | 746 | 745 | 99.6% |
| AtOPT3 O23482 | 737 | 601 | 80.3% |
| AtOPT6 Q9T095 | 736 | 397 | 53.1% |

Interpretation:

- A0A804M424 is the same protein as the published maize glutathione transporter ZmGT1
  (FJ573212, cultivar Nongda 108); the residual differences are consistent with cultivar polymorphism.
- A0A804M424 is far closer to AtOPT3 (80.3% identity) than to the yeast-tested glutathione
  transporter AtOPT6 (53.1%), placing ZmGT1 in the plant OPT3 clade.
- This is a pairwise similarity result only; no phylogenetic tree was built.
