# A0A8B6GS20 architecture and identity check (2026-10-21 re-review)

Scripts: `architecture_check.py` (output `architecture_check_output.txt`) and
`compare_mussel_entries.py` (output `compare_mussel_entries_output.txt`). Both fetch current
UniProt sequences and run Biopython local alignments (BLOSUM62, gap open -11, extend -1).
Run with `uv run <script>`.

## Results

- A0A8B6GS20 is 607 residues. Only target residues 362-588 align to human MTMR9 (Q96QG7),
  covering human residues 313-542 (41.3% of MTMR9) at 60.4% identity. The worm MTM-9 (Q965W9)
  alignment covers worm residues 342-562 (46.7% identity); the active paralog MTMR6 (Q9Y217)
  aligns at only 38.6% identity. The MTMR9 paralog group is the best match, which agrees with
  the PANTHER placement in PTHR10807:SF73 alongside C. elegans mtm-9.
- The N-terminal half of the MTMR9-type protein is absent: no counterpart of human MTMR9
  residues 1-312 (the PH-GRAM domain and the N-terminal half of the phosphatase-like domain).
- Target residues 1-361 are unrelated to myotubularins. They contain tandem repeats starting
  at residues 2, 174 and 272 (motif VCDRQL...EGWY), matching the D8C_UMOD Pfam domain
  (PF23283, two hits in UniProt). That domain is found in secreted and extracellular proteins
  (uromodulin/GP2/OIT3-like).
- Catalytic motif: the target segment at 377 (VHGSEGFDTT) aligns to the MTMR6 catalytic
  motif VHCSDGWDRT (catalytic Cys336, Arg342). The target has Gly at the Cys position and Thr
  at the Arg position. Human MTMR9 (IHGTEGTDST) and worm MTM-9 (IHGGDGLDST) carry the same
  kind of substitution. So the retained region has the MTMR9-type inactive site.
- Five other M. galloprovincialis entries from ORF MGAL_10B079678 are in SF73 (A0A8B6EPV9 593 aa,
  A0A8B6EME1 and A0A8B6ENJ7 563 aa, A0A8B6ELH7 502 aa). The ENJ7 and EPV9 models each cover
  98.7% of human MTMR9 in one alignment. A0A8B6GS20 residues 362-607 match their C-terminal
  246 residues at 97.2% identity.

## Interpretation

A0A8B6GS20 (ORF MGAL_10B089004) is a partial MTMR9 gene model. Its 3' part matches the
C-terminal ~45% of an MTMR9-type protein. Its 5' part encodes D8C_UMOD repeats from an
unrelated extracellular-protein module. The most likely explanation is a gene-model fusion
or a partial duplicate in this highly heterozygous WGS assembly; the 97.2% identity to the
full-length MGAL_10B079678 models fits an allelic haplotig or a recent partial copy. These
data cannot tell those apart. The encoded product as modelled lacks the GRAM domain and half
of the phosphatase-like fold, so it is unlikely to be a functional MTMR9 protein as written.
MTMR9-clade annotations on this accession describe the mussel MTMR9 gene rather than this
exact sequence model.

The analysis is limited: these are pairwise local alignments, not a phylogeny. Subfamily
placement rests on PANTHER (SF73 with worm mtm-9; human MTMR9 is in SF56).
