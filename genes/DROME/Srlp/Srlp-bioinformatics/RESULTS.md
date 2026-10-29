# Srlp (Q9VG69, CG5844) active-site and family-placement check

Script: `active_site_check.py` (run with `uv run active_site_check.py`); raw output in
`active_site_check.out`. Sequences, PANTHER cross-references and feature positions are fetched
live from UniProt (run 2026-10-21). Method: Biopython global pairwise alignment, BLOSUM62, gap
open -10, extend -0.5. At 27-35% identity a pairwise alignment is approximate, so the residue
correspondences below are a screen, not a structure-based assignment.

## Family placement

- Q9VG69 is classified in PANTHER PTHR43802:SF1 (IP11341P-RELATED), the same subfamily as the fly
  paralog CG5611 (Q9VB17), C. elegans ech-3 (Q20376), Arabidopsis Q6NL24, Rhodococcus 6-oxocamphor
  hydrolase CamK (Q93TU6) and Syntrophus BamA (Q2LXU2).
- Rat mitochondrial enoyl-CoA hydratase ECHS1 (P14604) is in a different PANTHER family,
  PTHR11941:SF54. ECHS1 is therefore an outgroup used only to locate the crotonase catalytic
  positions, not a function donor.
- Identity over aligned columns: CG5611 54.9%, ech-3 45.3%, ECHS1 34.1%, Q6NL24 31.4%,
  CamK 29.4%, BamA 27.0%.

## Active-site correspondences

| Reference | Reference position | Srlp residue |
|---|---|---|
| rat ECHS1 P14604 | G141 (substrate binding, oxyanion hole region) | N155 (G156 adjacent) |
| rat ECHS1 P14604 | E144 (first catalytic Glu, literature numbering) | E158 |
| rat ECHS1 P14604 | E164 (SITE, important for catalytic activity) | M185 |
| CamK Q93TU6 | E124 (ACT_SITE, nucleophile) | E158 |
| CamK Q93TU6 | H145 (substrate binding) | gap |
| CamK Q93TU6 | D154 (substrate binding) | D187 |
| CamK Q93TU6 | E244 (substrate binding) | E334 |
| Q6NL24 | H135 (SITE, important for catalytic activity) | N178 |

## N-terminus

The first 30 residues (MLRKFGGLLAQQVGQQARFTAASRTFSSTK) contain 5 Arg/Lys and no Asp/Glu,
a composition typical of a cleavable mitochondrial presequence. This is consistent with the
experimental mitochondrial-matrix localisation (PMID:26362788). No targeting predictor was run.

## Interpretation

Srlp has the crotonase (ClpP/crotonase) fold. It keeps the first catalytic glutamate (E158),
but at the position of the second catalytic glutamate of canonical enoyl-CoA hydratase
(ECHS1 E164) it has methionine. The paralog CG5611 has the same pattern (Glu retained,
second Glu replaced by Asn), so the loss looks like a feature of this SF1 lineage rather than
a single-gene change. Because SF1 contains enzymes with chemically different reactions
(CamK cleaves a C-C bond; BamA is a 6-oxocyclohex-1-ene-1-carbonyl-CoA hydrolase), and because the canonical
hydratase second Glu is missing, sequence evidence does not support assigning enoyl-CoA
hydratase activity or any other specific reaction to Srlp. Whether Srlp is catalytic at all
is unknown.
