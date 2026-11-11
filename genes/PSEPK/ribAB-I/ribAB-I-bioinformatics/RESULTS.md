# Active-site check of the KT2440 GTP cyclohydrolase II-like domains

Question: do the C-terminal GTP cyclohydrolase II (GCHII) fold domains of
ribAB-I (Q88QH7, PP_0516) and ribAB-II (Q88GB1, PP_3813) keep the catalytic
residues of the monofunctional KT2440 RibA (Q88QH1, PP_0522)? Both proteins
carry the Pfam GTP_cyclohydro2 (PF00925) domain and the NCBIfam NF010626
(ribBA) match, which is what drives the GTP cyclohydrolase II (GO:0003935)
TreeGrafter annotation on them.

Method: `check_gtpchii_residues.py` (run from the repository root with
`uv run python genes/PSEPK/ribAB-I/ribAB-I-bioinformatics/check_gtpchii_residues.py`)
reads the sequences and the RibA HAMAP MF_00179 ACT_SITE and zinc BINDING
features from the cached UniProt files, aligns each query from the start of its
GCHII DOMAIN feature to the C-terminus against RibA (local alignment, BLOSUM62,
gap open -10, extend -0.5), and reports the query residue aligned to each RibA
catalytic position and every cysteine in the query GCHII region. Raw output is in
`results.json`.

## Results

| Reference residue (RibA) | Role (UniProt) | ribAB-I (Q88QH7) | ribAB-II (Q88GB1) |
|---|---|---|---|
| Cys54 | Zn(2+) ligand | Asp263 | Asp257 |
| Cys65 | Zn(2+) ligand | Pro274 | Ala268 |
| Cys67 | Zn(2+) ligand | Arg276 | Pro270 |
| Asp126 | proton acceptor | Ser332 | Gln332 |
| Arg128 | nucleophile | not aligned (gap) | not aligned (gap) |

- The GCHII region of ribAB-I contains a single cysteine (Cys250) and that of
  ribAB-II contains none, whereas ribA (PP_0522) retains all three zinc-binding cysteines (Cys54, Cys65, Cys67).
- The alignments cover RibA residues 6-170 (ribAB-I; 153 aligned positions, 50
  identical) and 6-174 (ribAB-II; 154 aligned positions, 48 identical), so the
  fold is recognisably related while the catalytic positions are substituted.

## Interpretation

Neither ribAB-I nor ribAB-II retains the zinc-binding cysteine triad or the
catalytic residues of GTP cyclohydrolase II, so their C-terminal domains are
predicted to be catalytically inactive, as described for proteobacterial RibBX
proteins (PMID:24097946). Their N-terminal DHBP synthase domains (HAMAP MF_00180,
NCBIfam TIGR00506) are unaffected by this analysis. This is sequence-based
inference; no KT2440 enzyme assay has been reported.
