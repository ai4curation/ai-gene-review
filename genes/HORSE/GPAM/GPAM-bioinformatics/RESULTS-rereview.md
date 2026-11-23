# GPAM (horse A0A9L0TTC1): gene-model and phylogenetic re-review (2026-10-20)

Script: [compare_horse_models_rereview.py](compare_horse_models_rereview.py) (run with
`uv run --with biopython python compare_horse_models_rereview.py`). Raw output:
[results-rereview.json](results-rereview.json); sequences: [models-rereview.fasta](models-rereview.fasta).
Each sequence was fetched from UniProt REST and globally aligned (BLOSUM62, gap open -10,
extend -0.5, free end gaps) to human GPAT1 Q9HCL2 (828 aa). Feature positions are human coordinates.

## Identity of the benchmark accession

The UniProt horse reference proteome (UP000002281) lists A0A9L0TCA8 (828 aa) as the gene-centric canonical GPAM product; A0A9L0TTC1 is labelled "Isoform of A0A9L0TCA8".
Ensembl gene ENSECAG00000014742 (GPAM) has nine protein-coding transcripts; A0A9L0TTC1 is the product of ENSECAT00000105322 (790 aa), which is not the Ensembl canonical transcript.

| Accession | Length | Identity to human (aligned) | Human coverage | Human gaps | Segment 370-407 |
|---|---|---|---|---|---|
| A0A9L0TCA8 (UniProt canonical) | 828 | 94.4% | 100% | none | 38/38 |
| A0A9L0TTC1 (benchmark) | 790 | 94.2% | 95.4% | 370-407 | 0/38 |
| A0A9L0TA25 (Ensembl canonical) | 900 | 94.4% | 100% | none (+72 extra residues) | 38/38 |
| mouse Q61586 | 827 | 92.9% | 99.9% | 683 | 37/38 |
| rat P97564 | 828 | 91.7% | 100% | none | 37/38 |

The benchmark accession is an alternative gene model (splice isoform) of horse GPAM that lacks an
in-frame 38-residue segment corresponding to human residues 370-407. All other features checked are
retained: the HXXXXD catalytic motif (human 230-235, 6/6 identical), the six CoA-binding residues
(278, 279, 288, 293, 328, 462; 6/6) and the mitochondrial-localization region (80-120; 39/41).

The missing segment is conserved in human, mouse, rat and the canonical horse product, and in the
human cryo-EM structure (PDB 8E4Y, as reported in the human UniProt record) it contains resolved
secondary structure in the catalytic domain (helix 380-390, strand 396-400, helices 401-403 and
406-415). Whether the shortened protein folds and is catalytically active has not been tested; no
transcript-level or proteomic evidence for this isoform was examined here.

## Phylogenetic placement

UniProt assigns A0A9L0TTC1 to PANTHER PTHR12563:SF16 (GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE 1,
MITOCHONDRIAL), the same subfamily as human GPAM (Q9HCL2). In the cached PAINT annotations for
PTHR12563, node PTN000970957 (taxon 6072, Eumetazoa) carries IBD assertions for glycerol-3-phosphate
O-acyltransferase activity (GO:0004366), mitochondrion (GO:0005739), glycerophospholipid metabolic process
(GO:0006650) and triglyceride biosynthetic process (GO:0019432), seeded by human GPAM, mouse and rat
GPAT1/GPAT2 and other metazoan members. Horse GPAM is a eutherian descendant of that node. PAINT
did not place any plasma-membrane term on this node.
