# CG5611 (Q9VB17) active-site and family-placement check

Script: `active_site_check.py` (run with `uv run active_site_check.py`); raw output in
`active_site_check.out`. Sequences and feature positions are fetched live from UniProt.
Method: Biopython global pairwise alignment, BLOSUM62, gap open -10, extend -0.5.
Pairwise alignment at 25-35% identity is approximate; residue correspondences below are
a screening result, not a structure-based assignment.

## Family placement (UniProt PANTHER cross-references, queried 2026-10-20)

- Q9VB17 is classified in PANTHER PTHR43802:SF1 (IP11341P-RELATED).
- Q0IGX9 (cDNA clone IP11341p) has an identical 326-residue sequence; it is a second
  UniProt entry for the same product, not an isoform or fragment.
- Other SF1 members in model organisms: fly paralog Srlp/CG5844 (Q9VG69, 378 aa),
  C. elegans ech-3 (Q20376), Arabidopsis ECHIA (Q6NL24), zebrafish zgc:101569.
  No human or mouse protein is classified in PTHR43802.
- The DIOPT human "orthologs" listed by FlyBase are in different PANTHER families:
  ECHDC1 PTHR11941:SF27, ECHDC2 PTHR11941:SF44, ECH1 PTHR43149:SF1,
  ECHDC3 PTHR43602:SF1. They are therefore not suitable function donors.
- Reviewed SF1 members with experimental chemistry are bacterial and catalyse
  different reactions: Rhodococcus 6-oxocamphor hydrolase CamK (Q93TU6, C-C bond
  cleavage) and Syntrophus 6-oxocyclohex-1-ene-1-carbonyl-CoA hydrolase BamA (Q2LXU2).

## Active-site correspondences

| Reference | Reference position | CG5611 residue |
|---|---|---|
| rat ECHS1 P14604 (enoyl-CoA hydratase) | G141 (oxyanion hole, BINDING) | G148 |
| rat ECHS1 P14604 | E144 (catalytic Glu) | E151 |
| rat ECHS1 P14604 | E164 (SITE, important for catalysis) | N171 |
| CamK Q93TU6 | E124 (ACT_SITE nucleophile, by similarity) | E151 |
| CamK Q93TU6 | H145 (binding) | F169 |
| CamK Q93TU6 | D154 (binding) | D180 |

Identity over aligned columns: ECHS1 34.9%, CamK 24.7%, BamA 30.6%, Srlp 54.9%.

## Interpretation

CG5611 retains the oxyanion-hole glycine and the first catalytic glutamate of the
crotonase fold, but in this alignment the second catalytic glutamate of canonical
enoyl-CoA hydratase (ECHS1 E164) corresponds to asparagine. UniProt also reports no
PROSITE enoyl-CoA hydratase/isomerase signature for Q9VB17. Together with the chemically
heterogeneous SF1 membership, this does not support assigning enoyl-CoA hydratase
activity. The exact reaction remains unresolved; the closest family relative, Srlp, has
only localisation (mitochondrial matrix, IDA) and a hypoxia-response phenotype in GO.
