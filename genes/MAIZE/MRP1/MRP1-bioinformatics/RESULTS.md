# MRP1 (Q6Y3I1) nucleotide-binding domain motif check

Script: `nbd_motifs.py` (run as `python3 -I nbd_motifs.py ../MRP1-uniprot.txt`).
Regex scan of the cached UniProt sequence (1477 aa) for ABC NBD motifs.

| motif | position | sequence |
|---|---|---|
| Walker A (NBD1) | 646-653 | GPVGSGKS |
| Walker A (NBD2) | 1266-1273 | GRTGSGKS |
| ABC signature (NBD1) | 736-740 | MSGGQ |
| ABC signature (NBD2) | 1369-1373 | WSAGQ |
| Walker B (NBD1) | 756-761 | VYLLDD |
| Walker B (NBD2) | 1389-1394 | ILVLDE |

Interpretation: both Walker A motifs match the UniProt ATP-binding features
(646..653 and 1266..1273). NBD2 has a Walker B ending in the catalytic glutamate
(ILVLDE), whereas the NBD1 Walker B ends in aspartate (VYLLDD), the degenerate-site
pattern typical of ABCC/MRP transporters. The NBD1 signature (MSGGQ) is canonical
and the NBD2 signature is a variant (WSAGQ). This fits the usual ABCC arrangement
of one consensus ATP-hydrolysis site (NBD2 Walker A/B with the NBD1 signature) and
one degenerate site. The scan is sequence-only; no hydrolysis was measured.
