# GOX1598 (Q5FQK7) — AKR catalytic tetrad and cofactor-site mapping

## Question

UniProtKB Q5FQK7 (`Q5FQK7_GLUOX`, locus GOX1598 of *Gluconobacter oxydans* 621H)
is an unreviewed TrEMBL entry with **no GO annotations at all** and no
publication about the protein. Its only functional signal is signature-based:
Pfam PF00248 (Aldo_ket_red) over residues 29-353, SUPFAM SSF51430, CDD cd19094
(AKR_Tas-like), Gene3D 3.20.20.100 and PANTHER PTHR43364:SF4.

A fold assignment alone does not say whether the protein is a working enzyme.
The question this analysis answers is narrow and checkable: **does Q5FQK7 retain
the catalytic residues that reviewed, experimentally characterised aldo-keto
reductases (AKRs) use?**

## Method

`map_akr_catalytic_sites.py` downloads UniProt flat files for Q5FQK7 and for five
reviewed AKRs that carry curated `ACT_SITE`, `SITE` and `BINDING` features,
aligns each reference pairwise to Q5FQK7 (Biopython `PairwiseAligner`, global,
BLOSUM62, gap open -11 / extend -1) and reports, for every curated feature
position, which Q5FQK7 residue it maps onto and whether the residue is identical.

No residue number is hard-coded: the positions come from the references' own
curated UniProt features, and the mapping comes from the alignment. Positions
that fall in a gap are reported as gaps.

References used (the first four are PANTHER PTHR43364:SF4, the same subfamily as
Q5FQK7; AKR1B1 is the superfamily structural archetype, included as an
out-of-subfamily control):

| Accession | Protein | Length | % identity to Q5FQK7 |
|---|---|---|---|
| P0A9T4 | *E. coli* Tas, NADP(H)-dependent aldo-keto reductase | 346 | **50.4** |
| O43488 | Human AKR7A2, aflatoxin B1 aldehyde reductase | 359 | 38.4 |
| P46336 | *B. subtilis* IolS aldo-keto reductase | 310 | 32.8 |
| P77256 | *E. coli* YdjG, NADH-specific methylglyoxal reductase | 326 | 32.7 |
| P15121 | Human AKR1B1 aldose reductase | 316 | 28.1 |

Reproduce with `uv run python map_akr_catalytic_sites.py`; raw output is in
`run.out`, machine-readable mappings in `results.json`, alignments in
`alignments.txt`.

## Result 1: the AKR catalytic tetrad is complete and unmutated

Every curated catalytic position of every reference maps onto an **identical**
residue in Q5FQK7, and all five references agree on the same four Q5FQK7
positions:

| AKR catalytic role | Curated reference positions | Q5FQK7 |
|---|---|---|
| Proton-donor Tyr (`ACT_SITE`) | Tas Y53, AKR7A2 Y77, IolS Y58, YdjG Y59, AKR1B1 Y49 | **Tyr67** |
| Lys that lowers the Tyr pKa (`SITE`) | YdjG K85, IolS K84, AKR7A2 K105, AKR1B1 K78 | **Lys101** |
| Asp of the catalytic tetrad (cofactor `BINDING`) | AKR1B1 D44, AKR7A2 D72, YdjG D54 | **Asp62** |
| His of the catalytic tetrad (substrate `BINDING`) | AKR7A2 H141 (AKR1B1 W112 → Trp148 adjacent) | **His147** |

So the Asp-Tyr-Lys-His tetrad that performs hydride transfer and proton donation
in characterised AKRs is present at Asp62/Tyr67/Lys101/His147 of Q5FQK7, within a
Pfam-matched AKR domain (29-353). There is no evidence here of a fold-retaining
pseudoenzyme.

The cofactor pocket core is likewise conserved: the `BINDING` positions
AKR1B1 T20 → Thr34, AKR1B1/IolS S160+N161 → Ser196+Asn197, IolS/YdjG Q175/Q189 →
Gln221, and Tas/IolS K244/K214 → Lys260 are all identical.

## Result 2: the analysis does **not** resolve cofactor preference or substrate

Two negative results matter as much as the positive one, and both bound what can
be annotated:

- **NAD vs NADP is undecided.** The conserved positions listed above are
  conserved whether the reference binds NADP(+) (Tas, IolS, AKR7A2, AKR1B1) or
  NAD(+) (YdjG). The AKR1B1 C-terminal positions that discriminate the
  2'-phosphate (K263, S264, R269, E272, N273) map to **non-identical** residues
  in Q5FQK7 (Pro316, Phe317, Ile322, Ala325, Thr326), and AKR7A2 R250 maps to
  Thr273. The pocket is intact but its specificity cannot be read off this
  alignment.
- **No substrate can be assigned.** The AKR7A2 substrate-binding residues other
  than His141 (Y260, R263, R359) map to non-identical residues or to a gap
  (Gly285, Asp288, gap), and AKR1B1's substrate residue C299 maps to Thr343.
  PTHR43364:SF4 is itself substrate-heterogeneous — it contains aflatoxin B1
  aldehyde reductases (AKR7A2/A3), a methylglyoxal reductase (YdjG), IolS, Tas
  and a dozen uncharacterised bacterial members — so subfamily membership
  transfers no substrate either.

The closest reviewed relative, *E. coli* Tas at 50.4% identity, has a solved
structure and is described as an NADP(H)-dependent aldo-keto reductase
[PMID:14517983], but its own physiological substrate is likewise not established.

## Conclusion

Q5FQK7 is, on sequence evidence, a complete and catalytically plausible
NAD(P)(H)-dependent aldo-keto reductase of the AKR superfamily. That supports an
annotation at the level of the reaction class (a CH-OH/NAD(P) oxidoreductase) and
no further: the cofactor, the substrate and the physiological role remain unknown
and need experiment, not more sequence analysis.
