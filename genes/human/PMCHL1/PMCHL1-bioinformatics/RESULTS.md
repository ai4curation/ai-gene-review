# PMCHL1 (Q16048) vs parent pro-MCH (PMCH, P20382)

Script: `compare_to_pmch.py` (run `uv run python compare_to_pmch.py ../PMCHL1-uniprot.txt`).
Raw output: `results_output.txt`. The target sequence is read from the local UniProt file;
PMCH and its feature table are fetched live from UniProt REST.

## Findings (from results_output.txt)

- Local BLOSUM62 alignment: Q16048 residues 2-86 align to PMCH 81-165 at 81.2% identity (69/85).
- PMCH residues 1-80 have no counterpart in Q16048. This region contains the PMCH signal
  peptide (1-21, 0/21 positions aligned) and the N-terminal part of the pro-region. The
  86-aa ORF is a 5'-truncated copy of the C-terminal half of pro-MCH with a novel
  N-terminus (MLSQKPKKKH..., the putative NLS of VMCH-p8).
- Target N-terminal 15 aa are highly charged (MLSQKPKKKHNFLNH); no N-terminal hydrophobic
  core (max 15-aa Kyte-Doolittle mean in the first 35 aa = 1.28, starting at residue 21,
  i.e. inside the copied pro-region, versus 2.13 at residue 10 for the PMCH signal peptide).
  Without a signal peptide the product would not enter the secretory pathway, so the
  prohormone-convertase processing and regulated secretion that release MCH/NEI from
  PMCH would not occur.
- Peptide regions are present but substituted:
  - NGE region (PMCH 110-128): 1 substitution (N122->D43).
  - NEI region (PMCH 131-143): I132->T53 and I143->V64. PMCH I143 is the C-terminal
    amidated residue of NEI (UniProt MOD_RES "Isoleucine amide"); the Gly-Arg-Arg amidation/
    cleavage signal that follows it is retained (GRR at 65).
  - MCH region (PMCH 147-165): M150->T71, R152->S73, R160->Q81, P161->S82; the disulfide
    cysteines (PMCH C153/C162 -> Q16048 C74/C83) are retained.
- Dibasic sites KR (50) and RR (66) are retained.

## Interpretation and limits

The MCH-like and NEI-like segments are present but (i) carry substitutions inside the
mature peptide sequences and (ii) sit in a product that lacks the signal peptide needed for
secretory-pathway entry and prohormone processing. This analysis does not test receptor
binding of the variant peptide; it shows only that the canonical route to a secreted
MCH-receptor ligand is absent from this ORF. Whether any protein is made at all is a
separate question addressed by the literature (PMID:19068116: no endogenous protein detected).
