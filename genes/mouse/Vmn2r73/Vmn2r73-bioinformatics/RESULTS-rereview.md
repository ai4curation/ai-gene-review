# Vmn2r73 re-review: A0A3B2WCZ5 versus the canonical D3Z7M3 product

Script: `compare_sequences_rereview.py` (PEP 723; run with `uv run --script compare_sequences_rereview.py`).
Raw output: `rereview_output.txt`. Both sequences and their TRANSMEM features are fetched directly from
UniProt REST; no prediction output is used.

## Identity

- A0A3B2WCZ5 is the 496-residue translation of Ensembl ENSMUST00000232965 (Vmn2r73-203), a
  non-canonical transcript of ENSMUSG00000070458.
- D3Z7M3 (851 residues) is the translation of ENSMUST00000077478 (Vmn2r73-201), which Ensembl flags
  as the canonical transcript of the gene. Neither entry is Swiss-Prot reviewed.

## Results

- Residues 1-429 of the target are identical to canonical residues 1-429 (signal peptide plus the
  Venus-flytrap ligand-binding region).
- Target residues 430-470 are identical to canonical residues 506-546 (41 aa), i.e. canonical
  residues 430-505 are skipped, consistent with an alternative splice junction inside the
  extracellular region that precedes the cysteine-rich domain.
- After target residue ~470 the sequence diverges into a short unique tail ending in
  SNMTSFLCLYICLLFRYGSVCEMSRRSICQ.
- UniProt records no TRANSMEM feature on A0A3B2WCZ5, against seven on D3Z7M3 (584-606 to 800-822).
- Kyte-Doolittle scan (window 19, threshold 1.6): the only hydrophobic windows in the target are
  residues 1-21 (signal peptide). The canonical C-terminal region 561-851, used as positive control,
  has 69 such windows.

## Interpretation

A0A3B2WCZ5 is an alternative gene model of Vmn2r73 that encodes only the extracellular part of the
receptor: signal peptide, Venus-flytrap ligand-binding domain and the nine-cysteine domain (Pfam
NCD3G, target 432-474), with no seven-transmembrane domain. If translated it would be predicted to be secreted or retained in the
secretory pathway, not to be a multi-pass membrane protein. Whether the transcript is translated or
is a target of nonsense-mediated decay is not established by sequence.
