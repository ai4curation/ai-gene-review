# RHOJ (Q9H4E5) evolutionary grounding

Script: `evolutionary_grounding.py` (PEP 723, stdlib only; run with
`uv run --script evolutionary_grounding.py`). Raw output: `RESULTS.txt`.
It queries the PANTHER geneinfo service and the UniProt REST API live, and
reads the repository's cached PAINT table
`interpro/panther/PTHR24072/PTHR24072-paint.tsv`.

## PANTHER placement

PANTHER places canonical human RHOJ Q9H4E5 (HGNC:688) in family PTHR24072 (RHO FAMILY GTPASE), subfamily PTHR24072:SF17 (RHO-RELATED GTP-BINDING PROTEIN RHOJ).

## G-domain completeness

The canonical 214-residue product has every G-domain motif and the C-terminal CAAX box:

| Motif | Position | Sequence |
|---|---|---|
| G1 P-loop | 28 | GDGAVGKT |
| G2 switch I | 52 | PTVFD |
| G3 switch II | 75 | DTAGQ |
| G4 guanine-base motif | 133 | TQID |
| G5 guanine-base motif | 175 | CSAL |
| CAAX box | 211 | CSII |

No catalytic or nucleotide-binding residue is lost. Nothing in the sequence suggests a pseudo-GTPase.

## PAINT nodes from which RHOJ inherits IBA annotations

| Node | GO term | Node taxon | Q9H4E5 is an IBD seed |
|---|---|---|---|
| PTN000632671 (family root) | GO:0005886 plasma membrane | (root) | yes |
| PTN000632671 | GO:0003924 GTPase activity | (root) | yes |
| PTN000632671 | GO:0005525 GTP binding | (root) | yes |
| PTN000632671 | GO:0007015 actin filament organization | (root) | no |
| PTN000632671 | GO:0007165 signal transduction | (root) | no |
| PTN008604840 | GO:0019901 protein kinase binding | taxon:2759 | no (Cdc42 seeds) |
| PTN008604842 | GO:0006897 endocytosis | taxon:33154 | no (Cdc42 seeds) |
| PTN008604842 | GO:0030010 establishment of cell polarity | taxon:33154 | no (Cdc42 seeds) |

## Interpretation

- RHOJ's own experimental annotations are among the seeds for GTPase activity, GTP binding and plasma membrane, which PAINT curators placed at the family root. These functions are therefore both measured on human RHOJ and inherited across the Rho family.
- Protein kinase binding, endocytosis and establishment of cell polarity come from deeper Cdc42-seeded nodes, PTN008604840 and PTN008604842, which RHOJ descends from. None of the seeds is RHOJ. These are inferences about RHOJ, not RHOJ-specific measurements.
