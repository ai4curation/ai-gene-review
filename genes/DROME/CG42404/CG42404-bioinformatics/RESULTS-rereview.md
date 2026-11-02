# CG42404 (Q9VFA8) vs DGCR2: domain architecture and conserved region (re-review, 2026-10-21)

Script: `compare_dgcr2_rereview.py` (run with `uv run compare_dgcr2_rereview.py`); raw output in
`compare_dgcr2_rereview.out`. Sequences and features were fetched live from UniProt REST; InterPro
matches were taken from the InterPro API (2026-10-21).

## Family placement

UniProt and InterPro place Q9VFA8, human DGCR2 (P98153) and mouse Dgcr2 (P98154) in the same PANTHER
family and the same (only) subfamily, PTHR15256:SF6 (INTEGRAL MEMBRANE PROTEIN DGCR2_IDD). The fly
PANTHER HMM match spans residues 2-734 of Q9VFA8; the human match spans residues 43-550 of P98153.

## Domain architecture

| Protein | Length | Signal | LDL-A | C-type lectin | VWFC | TM | Cytoplasmic region |
|---|---|---|---|---|---|---|---|
| fly CG42404 Q9VFA8 | 1133 | not annotated | absent | absent | 27-92 | 103-125 | ~1000 residues, mostly disordered |
| human DGCR2 P98153 | 550 | 1-20 | 28-68 | 115-241 | 270-333 | 350-368 | 369-550 |
| mouse Dgcr2 P98154 | 548 | 1-24 | 28-68 | 113-239 | 268-331 | 348-366 | 367-548 |

The fly product lacks the LDL-receptor class A module and the DGCR2-type C-type lectin-like domain
(no InterPro match for IPR002172, IPR001304 or IPR034010 in Q9VFA8). Its first ~26 residues
(MYFLALLAFIGNAKDG...) are hydrophobic and sit directly before the VWFC domain, but the UniProt record
carries no signal-peptide feature, so N-terminal processing and topology are unresolved.

## Conserved region

Local alignment (BLOSUM62, gap open -11/extend -1) aligns fly residues 28-200 to human DGCR2 270-455
(and mouse 268-453) with 34.7% identity over 167 aligned columns. The aligned block covers:

- the VWFC domain, including its cysteine framework;
- the transmembrane helix (fly 103-125 / human 350-368);
- a basic juxtamembrane stretch (fly `RLRQRK`, human `RLRQRR`);
- a proline-rich PPPYE motif (fly 193-197, human 446-450), a PPxY-type sequence.

Beyond fly residue ~200 the long fly cytoplasmic extension has no significant local alignment to DGCR2.

## Interpretation and limits

The conserved core shared by fly and vertebrate members is VWFC + single TM + juxtamembrane tail with a
PPxY-type motif. This supports a single-pass membrane protein. It does not establish any molecular
activity: the vertebrate C-type lectin and LDL-A modules, which are the most obvious candidate
ligand-binding parts of DGCR2, are absent from the fly product, so ligand-binding properties attributed
to those modules cannot be transferred. The PPxY motif is a sequence observation only; no binding partner
has been tested. Position 106 of Q9VFA8 is an unknown residue (X) inside the predicted TM segment,
reflecting an ambiguity in the deposited sequence.
