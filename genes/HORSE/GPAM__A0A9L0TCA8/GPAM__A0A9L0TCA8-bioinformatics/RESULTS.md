# GPAM horse canonical (A0A9L0TCA8): conservation and phylogenetic placement (2026-10-20)

Script: [compare_gpat1.py](compare_gpat1.py) (run with `uv run --no-project --with biopython python compare_gpat1.py`).
Raw output: [results.json](results.json). Sequences were fetched from UniProt REST and globally aligned
(BLOSUM62, gap open -10, extend -0.5, free end gaps) to human GPAT1 Q9HCL2 (828 aa). Feature positions are
human coordinates taken from the human Swiss-Prot record.

## Sequence conservation

| Accession | Species | Length | Identity (aligned) | Human coverage | Human gaps | HXXXXD 230-235 | CoA-binding (6) | Mito region 80-120 |
|---|---|---|---|---|---|---|---|---|
| A0A9L0TCA8 | horse | 828 | 94.4% | 100% | none | HRSHID 6/6 | 6/6 | 39/41 |
| Q61586 | mouse | 827 | 92.9% | 99.9% | 683 | HRSHID 6/6 | 6/6 | 39/41 |
| P97564 | rat | 828 | 91.7% | 100% | none | HRSHID 6/6 | 6/6 | 39/41 |

Horse A0A9L0TCA8 is a full-length GPAT1: it aligns gap-free over all 828 human residues, is more similar to human
GPAT1 than the experimentally studied mouse and rat orthologs are, and keeps the HXXXXD catalytic motif and all
six CoA-binding residues identical.

## Phylogenetic placement

UniProt assigns A0A9L0TCA8 to PANTHER PTHR12563:SF16 (GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE 1, MITOCHONDRIAL),
the same subfamily as human GPAM (Q9HCL2) and mouse Gpam.

In the cached PAINT annotations for PTHR12563, node PTN000970957 (taxon 6072, Eumetazoa) carries IBD assertions
for glycerol-3-phosphate O-acyltransferase activity (GO:0004366), mitochondrion (GO:0005739), glycerophospholipid
metabolic process (GO:0006650) and triglyceride biosynthetic process (GO:0019432). Its seeds include human GPAM
(Q9HCL2), mouse Gpam (MGI:109162) and mouse Gpat2 (MGI:2684962). Horse GPAM is a eutherian descendant of this node.

PAINT placed no plasma-membrane term on any PTHR12563 node. The separate metazoan node PTN002488810 carries
peroxisomal membrane, glycerone-phosphate O-acyltransferase activity and ether lipid biosynthesis, which belong
to the GNPAT/DHAPAT branch and were not assigned to the GPAT1/GPAT2 node.
