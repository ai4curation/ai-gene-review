# MITF (horse, F6ZKQ4): isoform identity and conservation

Script: `compare_isoforms.py` (PEP 723; run with `uv run --script compare_isoforms.py`).
Raw output: `compare_isoforms.out`. Sequences were fetched live from the UniProt REST API
(F6ZKQ4; all human O75030 isoforms; all horse TrEMBL entries with gene name MITF).
Global alignment, BLOSUM62, gap open -10, extend -0.5.

## Result

F6ZKQ4 (413 aa) aligns end to end, with no gaps, to human isoform M2 (O75030-10, 413 aa): 404/413 identical (97.8%).
Against human isoform M1 (O75030-9, 419 aa) the only gap is the 6-residue alternatively spliced segment TACIFP (horse lacks 'ACIFPT').
Against the human canonical isoform A1 (O75030, 526 aa) horse lacks the 107-residue isoform-A N-terminal region (two segments of 9 and 98 residues) plus the same 6-residue segment.

Interpretation: F6ZKQ4 is the horse melanocyte-type MITF-M product (first exon 1M from the melanocyte-specific promoter),
in its (-) splice form lacking the 6-aa exon-6A insert. It is not the UniProt canonical (MITF-A-type) product, and
no Swiss-Prot reviewed horse MITF entry exists. The horse TrEMBL entry K4FCY0 (419 aa) is identical to F6ZKQ4 apart from the 6-residue insert (MITF-M(+));
the longer horse models (A0A5F5PRV7 635 aa, A0A3Q2I515 519 aa, F7A3Z7 494 aa, and others) carry alternative N termini.

Motif checks on F6ZKQ4:
- bHLH-Zip block (human MITF-M equivalent ERRRRFNINDRIKELG...QARAH, 84 aa) present verbatim: True
- ERK site context SPMAML (human MITF-M Ser73) present: True
- C-terminal SSRRSSMS context (human MITF-M Ser409 region) present: True
- 6-aa alt-exon (+) insert ACIFPT present: False

Consequence for function transfer: the DNA-binding, dimerization and transactivation regions shared by all MITF isoforms
are intact. The isoform-A N terminus is absent; this is the region that in MITF-A (and the first 30 residues of TFEB) binds
the Rag GTPases and carries the mTORC1 phospho-degron (human isoform-A Ser-5). Lysosome-membrane recruitment and
Rag/mTORC1-dependent degradation established for MITF-A-type isoforms should therefore not be transferred to this product.
