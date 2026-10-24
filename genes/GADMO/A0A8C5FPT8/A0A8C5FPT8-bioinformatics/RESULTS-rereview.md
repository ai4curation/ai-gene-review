# A0A8C5FPT8 (Atlantic cod tbc1d14) re-review sequence analysis

Script: `compare_sequences_rereview.py` (run with `uv run compare_sequences_rereview.py > RESULTS-rereview.txt`).
Raw output: `RESULTS-rereview.txt`; alignment: `panel_rereview.aln.fa` (MAFFT --auto).
Sequences were fetched live from UniProt REST; Ensembl transcript-to-gene mapping from Ensembl REST.

## 1. Gene-model identity

All ten Atlantic cod UniProt entries named tbc1d14 (A0A8C5FCB4, A0A8C4Z0Q4, A0A8C5A8S4, A0A8C5B8M0,
A0A8C4ZRU6, A0A8C5C0A0, A0A8C5FPT8, A0A8C5BG38, A0A8C5AUF9, A0A8C5BUI9) are transcripts of one
Ensembl gene, ENSGMOG00000018292 (chromosome 17). A0A8C5FPT8 (ENSGMOT00000039892, 709 aa) is one
alternative transcript model of that gene. None of the cod entries is reviewed.

A0A8C5FPT8 versus the sister model A0A8C5FCB4 (750 aa): 97.0% identity over 666 aligned positions. The two
differ at both ends:

- N-terminus: A0A8C5FPT8 starts MHFFLTRNYLLTGRASFWLTHSSSS..., which does not match the human TBC1D14
  N-terminus. Only 29 of human residues 1-50 align to it, against 48 for A0A8C5FCB4.
- C-terminus: A0A8C5FCB4 ends ...KWPQVLQTLQKDQERSSPVLRR, which matches human TBC1D14
  (...KWAQVLTALQKDSREMEKGSPSLRH). A0A8C5FPT8 departs after ...KWPQVR and ends in a 48-residue tail
  (TDRDGRTDGRGMAVTRFYFVSCDLRFGLRVWERLSVFIICMRVFYGGLAT) with no counterpart in the vertebrate
  orthologs. This looks like an alternative or read-through 3' exon.

The TBC domain, the TRAPP-binding region (human 120-223: 93 aligned, 44 identical in both cod models) and
the catalytic dyad positions are the same in A0A8C5FPT8 and A0A8C5FCB4. A0A8C5FPT8 is therefore a
near-complete alternative gene model. It has the core domains but neither the conserved N-terminal
segment nor the conserved C-terminal tail.

## 2. Orthology (TBC1D14 vs TBC1D12)

Identity of A0A8C5FPT8 to the panel:

| Sequence | Identity |
|---|---|
| TBC1D14: human, mouse, chicken, Xenopus, zebrafish, coelacanth | 60-66% |
| TBC1D12: human, mouse, Xenopus, zebrafish tbc1d12b | 54-58% |
| cod TBC1D12-like (LOC115530985, A0A8C5BBR7) | 51% |

In the neighbour-joining tree (identity distances, rooted on the cod TBC1D12-like protein), the two cod
tbc1d14 models fall inside the vertebrate TBC1D14 clade. That clade includes zebrafish tbc1d14 and
tetrapod TBC1D14, and the TBC1D12 orthologs form a separate clade.

PANTHER (via UniProt) puts tetrapod TBC1D14 in PTHR47219:SF21 ("TBC1 DOMAIN FAMILY MEMBER 14"), but puts
teleost and coelacanth tbc1d14, A0A8C5FPT8 included, in PTHR47219:SF15 ("TBC1 DOMAIN FAMILY MEMBER 12
ISOFORM X1"). The tree does not support that. The SF15 assignment of fish tbc1d14 looks like an HMM
subfamily mis-assignment, not orthology with TBC1D12. Cod has a separate TBC1D12-like gene.

## 3. Catalytic residues

Human TBC1D14 R472 and Q508 (the TBC arginine finger and glutamine finger, mutated in the RAQA mutant of
PMID:22613832) align to R457 and Q493 in A0A8C5FPT8 (R532/Q568 in A0A8C5FCB4). The catalytic residues
are retained, but retaining them does not show GAP activity. The human ortholog binds active Rab11
without acting as a GAP for it.

## Caveats

This is a single NJ tree on identity distances with a small taxon panel and no bootstrap support. The
TBC1D14/TBC1D12 split is clear from the identity values alone, but the internal branching order is not
claimed.
