# Atg18a PROPPIN phosphoinositide-binding motif check

Script: `proppin_motifs.py` (Biopython global pairwise alignment, BLOSUM62, gap open -10,
extend -0.5; sequences fetched live from UniProt REST). Raw output: `proppin_motifs_output.txt`.
Run with the project's shared Python: `python -I proppin_motifs.py`.

Question: does fly Atg18a keep the PROPPIN [F/L]RRG motif that forms the two phosphoinositide
binding sites in WIPI2, Atg18 and the rest of the family?

## Result (2026-11-16 run)

| Protein | Accession | Residues aligned to WIPI2 FRRG241-244 | Own motif |
|---|---|---|---|
| human WIPI2 (reference) | Q9Y4P8 | FRRG 241-244 | FRRG |
| human WIPI1 | Q5MNZ9 | LYEFRRGMKR | FRRG 225 |
| human WDR45/WIPI4 | Q9Y484 | LVELRRGTDP | LRRG 231 |
| yeast Atg18 | P43601 | IYQFRRGT-Y | FRRG 284 |
| fly Atg18a isoform E | M9PER1 | LFELRRGLKR | LRRG 222 |
| fly Atg18a isoform A | Q9VSF0 | LFELRRGLKR | LRRG 222 |
| fly Atg18b | Q9VIE1 | VQEFRRGVS- | FRRG 208 |
| fly CG11975 | Q9VHJ2 | VSELRRGSNH | LRRG 224 |

Identity to WIPI2 over the WIPI2 length: Atg18a 53% (isoform E), Atg18b 45%, CG11975 26%;
WIPI1 56%, WIPI4 23%, yeast Atg18 31%.

## Interpretation

- Fly Atg18a keeps the arginine pair of the motif (LRRG). Phe to Leu at the first position is
  also seen in human WIPI4 and in fly CG11975 (table above); WIPI4 binds PI3P, so the substitution does not
  argue against phosphoinositide binding. This is consistent with the PI3P- and
  PI(3,5)P2-binding IBA rows; it is sequence evidence only, not a binding assay.
- Atg18a is the fly protein closest to WIPI1/WIPI2; Atg18b is a second, more divergent
  WIPI1/2-like paralog; CG11975 is the WIPI3/4-like member. This matches the grouping stated in
  PMID:24374083.
