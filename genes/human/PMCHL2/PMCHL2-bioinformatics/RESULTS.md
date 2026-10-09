# PMCHL2 (Q9BQD1) vs parent pro-MCH (PMCH, P20382)

Script: `compare_to_pmch.py` (run `uv run python compare_to_pmch.py ../PMCHL2-uniprot.txt`;
identical to the PMCHL1 script). Raw output: `results_output.txt`. The target sequence is
read from the local UniProt file; PMCH and its feature table are fetched live from UniProt REST.

## Findings (from results_output.txt)

- Local BLOSUM62 alignment: Q9BQD1 residues 2-86 align to PMCH 81-165 at 83.5% identity (71/85).
- PMCH residues 1-80 have no counterpart in Q9BQD1. This region contains the PMCH signal
  peptide (1-21, 0/21 positions aligned) and the N-terminal part of the pro-region. Like
  PMCHL1, the ORF is a 5'-truncated copy of the C-terminal half of pro-MCH with a novel
  lysine-rich N-terminus (MLSQKTKKKH...; PMCHL1 has KPKKK at the same place).
- Target N-terminal 15 aa are highly charged (MLSQKTKKKHNFLNH); no N-terminal hydrophobic
  core (max 15-aa Kyte-Doolittle mean in the first 35 aa = 1.28, starting at residue 21,
  inside the copied pro-region, versus 2.13 at residue 10 for the PMCH signal peptide).
  Without a signal peptide the product would not enter the secretory pathway, so the
  prohormone-convertase processing and regulated secretion that release MCH/NEI from
  PMCH would not occur.
- Peptide regions are present but substituted:
  - NGE region (PMCH 110-128): N122->D43, Q127->L48.
  - NEI region (PMCH 131-143): I132->T53; the C-terminal amidated I143 is retained (I64),
    followed by GRR (65).
  - MCH region (PMCH 147-165): M150->T71, R160->Q81, P161->R82; the disulfide cysteines
    (PMCH C153/C162 -> Q9BQD1 C74/C83) are retained.

## Interpretation and limits

The MCH-like and NEI-like segments are present but substituted, and the product lacks the
signal peptide needed for secretory-pathway entry and prohormone processing. Receptor binding
of the variant peptide has not been tested here; the analysis shows only that the canonical
route to a secreted MCH-receptor ligand is absent from this ORF. Protein existence is
addressed by the literature (PMID:19068116).
