# A0A2G9RZF1 bioinformatics: identity of the 156-aa CUB ORF (re-review, 2026-10-21)

Scripts (reproducible; need `curl` and HMMER3 `phmmer`):

- `fetch_and_phmmer.sh` fetches the query and a panel of 17 CUB proteins from UniProt
  and runs phmmer (output `phmmer_panel.out`, `phmmer_panel_summary.tsv`).
- `refseq_compare.sh` fetches the complete bullfrog TLL1 (XP_073462190.1, 1005 aa)
  and BMP1 (XP_073478370.1, 1020 aa) RefSeq models from the chromosome-level
  annotation and runs phmmer (output `phmmer_refseq.out`, `phmmer_refseq_summary.tsv`).
- `cub5_identity.py` counts identical aligned positions in every phmmer domain
  alignment above 100 bits (`cub5_identity.tsv`, `cub5_identity_refseq.tsv`).

## Result 1: the ORF is the C-terminal CUB5 of a tolloid

In every full-length tolloid in the panel the query's best domain hit is the
last CUB domain (CUB5), and the alignment runs to the protein's C-terminus. For
human TLL1 (1013 aa) query 30-156 aligns to 886-1012 at 229.3 bits. Hits to
CUB1-CUB4 of the same proteins and to PCOLCE1/2, MFRP, NETO1/2 and cubilin CUB
domains all score 80 bits or less.

| Target (UniProt) | PANTHER subfamily | bits | identity |
|---|---|---|---|
| Q8JI28 TLL1_XENLA | SF45 | 260.4 | 110/127 (86.6%) |
| O43897 TLL1_HUMAN | SF45 | 229.3 | 99/127 (78.0%) |
| Q62381 TLL1_MOUSE | SF45 | 217.0 | 94/127 (74.0%) |
| P13497 BMP1_HUMAN | SF53 | 208.5 | 86/126 (68.3%) |
| P98063 BMP1_MOUSE | SF53 | 207.9 | 86/126 (68.3%) |
| O57382 TLL2_XENLA | SF45 | 203.7 | 85/126 (67.5%) |
| Q9Y6L7 TLL2_HUMAN | SF45 | 196.9 | 85/128 (66.4%) |

Identity tracks the species tree within the TLL1 orthogroup (frog > mammal TLL1)
and is lower for every BMP1 and TLL2 paralog. That is the pattern of a TLL1
ortholog, not just a best hit.

## Result 2: it matches the complete bullfrog TLL1 gene model almost exactly

| RefSeq model | bits (CUB5) | identity | target span |
|---|---|---|---|
| XP_073462190.1 tolloid-like protein 1 (1005 aa) | 287.7 | 126/127 (99.2%) | 879-1005 |
| XP_073478370.1 bone morphogenetic protein 1 (1020 aa) | 164.1 | 71/139 (51.1%) | 893-1018 |

A0A2G9RZF1 residues 30-156 are therefore the last 127 residues (CUB5) of
bullfrog TLL1. Residues 1-29 do not align to either model. They are probably an
intronic or untranslated read-through from the fragmented draft gene model.

## Interpretation

- A0A2G9RZF1 is a fragmentary gene model of bullfrog TLL1. It is 156 aa against
  1005 aa for the complete product (about 13% of the protein). It lacks the
  signal peptide, the prodomain, the astacin-like zinc metalloprotease domain
  (and with it every catalytic residue), CUB1-CUB4 and both EGF-like domains.
- UniProt's PANTHER placement (PTHR24251:SF37 "CUB DOMAIN-CONTAINING PROTEIN")
  is a fragment artefact. The tolloid subfamily HMMs (SF45 holds TLL1 and TLL2;
  SF53 holds BMP1) model the full multi-domain protein, so a lone CUB domain
  falls into a heterogeneous single-CUB bin. Note that UniProt places the
  neighbouring fragments on scaffold KV928989 in SF45 (A0A2G9RZH1) and SF53
  (A0A2G9RZI6), which is no more reliable for subfamily assignment.
- The fragment has no catalytic activity of its own. Any function annotation
  belongs to the TLL1 gene.
