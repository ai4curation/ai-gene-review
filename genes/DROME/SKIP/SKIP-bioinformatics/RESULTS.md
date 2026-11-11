# SKIP (FBgn0051163) isoform comparison

Script: `compare_isoforms.py` (stdlib only; queries the UniProt REST API for all
UniProtKB entries cross-referenced to FlyBase FBgn0051163). Raw output: `output.txt`.

## Question

Diao et al. 2009 (PMID:19463952) mapped binding of the Shal (Kv4) K+ channel to the
eight C-terminal residues that are unique to the short isoform SKIP3 (SAM1 domain plus
a 61-residue C-terminal tail). Does the product reviewed here, A0A0B4K6C1 (1034 aa,
NP_001247234.1), carry those residues?

## Results (from output.txt)

| accession | length | shared N-terminal prefix with A0A0B4K6C1 | last 8 residues | last 8 present in A0A0B4K6C1 |
|---|---|---|---|---|
| A0A0B4KH49 | 128 | 120 | VSLAFNLY | False |
| Q8SZS0 (SKIP1, PB/PC) | 952 | 120 | SGPLKSST | True |
| A0A0B4KHM3 | 1027 | 880 | SGPLKSST | True |
| A0A0B4K6C1 | 1034 | 1034 | SGPLKSST | True |
| Q0KI30 | 1064 | 483 | SGPLKSST | True |
| A0A0B4KHV7 | 1080 | 120 | QDDRLEDQ | False |

A0A0B4KH49 (128 aa) is identical to A0A0B4K6C1 over its first 120 residues (the SAM1
region) and then ends in an eight-residue tail, VSLAFNLY, that does not occur in
A0A0B4K6C1. This matches the published description of SKIP3, which shares all of its
sequence with SKIP1 except the C-terminal eight residues that are needed for Shal binding.
A0A0B4KH49 is therefore the SKIP3 product, and the Shal-binding octapeptide is absent
from A0A0B4K6C1.

A0A0B4K6C1 is a long isoform like SKIP1: N-terminal SAM1, central disordered region, SH3
domain and C-terminal SAM2 (UniProt FT DOMAIN lines). Shal binding and Shal-inactivation
regulation demonstrated for SKIP3 cannot be transferred to it.

## Caveats

The identification of A0A0B4KH49 as SKIP3 rests on the sequence architecture described in
the paper (120 shared + 8 unique residues). The paper's own SKIP3 cDNA sequence was not
retrieved for a direct comparison.
