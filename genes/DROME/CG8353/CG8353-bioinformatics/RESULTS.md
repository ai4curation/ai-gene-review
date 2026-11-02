# CG8353 (Q9VLR2) vs characterised PTHR11644:SF2 cytidine deaminases

Script: `compare_cda_sf2.py` (run with `uv run --no-project --with biopython --with requests python compare_cda_sf2.py`).
Raw output: `compare_cda_sf2_output.txt`. Sequences fetched live from UniProt REST and NCBI efetch (2026-10-21).

## Phylogenetic placement

PANTHER 19.0 classifications (`.cache/panther/PTHR19.0_*`) place Q9VLR2 in PTHR11644:SF2, the same subfamily as
human CDA (P32320), mouse Cda (P56389), yeast CDD1 (Q06549) and E. coli cdd (P0ABF6). The two neighbouring fly genes
CG8360 (Q9VLR3) and CG8349 (Q7KTJ2) are also in SF2. The PAINT IBD node PTN000182087 (cytidine deaminase activity,
cytosol, deoxycytidine catabolic process, uridine biosynthetic process) is ancestral to this subfamily
(`interpro/panther/PTHR11644/PTHR11644-paint.tsv`).

## Gene model

Both FlyBase/RefSeq CG8353 protein products (NP_609196.1 and NP_001260233.1) are 170 aa and identical to Q9VLR2, so
the benchmark accession is the complete canonical product of the gene, not a fragment or variant isoform.

## Catalytic residues

Global alignment (BLOSUM62) to human CDA P32320, at the positions curated in its UniProt features:

| protein | % identity | h54 N | h60 Y | h65 C (Zn) | h67 E (proton donor) | h99 C (Zn) | h102 C (Zn) |
|---|---|---|---|---|---|---|---|
| mouse Cda P56389 | 81.5 | N54 | Y60 | C65 | E67 | C99 | C102 |
| yeast CDD1 Q06549 | 45.3 | N50 | Y56 | C61 | E63 | C96 | C99 |
| E. coli cdd P0ABF6 | 34.3 | N89 | M97 | H102 | E104 | C129 | C132 |
| fly CG8353 Q9VLR2 | 45.4 | N67 | F73 | C78 | E80 | C112 | C115 |
| fly CG8360 Q9VLR3 | 46.5 | N64 | Y70 | C75 | E77 | C109 | C112 |
| fly CG8349 Q7KTJ2 | 44.7 | N162 | F168 | C173 | E175 | C207 | C210 |

CG8353 retains all three zinc-ligand cysteines (C78, C112, C115) and the catalytic glutamate E80 of the tetrameric
(Cys3) cytidine deaminase class, as in human CDA and yeast CDD1, rather than the His-Cys-Cys ligand set of the dimeric
E. coli enzyme. These positions match the PIRSR-derived Zn-binding and active-site features in the Q9VLR2 UniProt entry.
CG8353 is a single-domain 170 aa protein aligning across 141 columns of the 146 aa human enzyme, consistent with the
small-chain homotetrameric CDA architecture (NCBIfam TIGR01354 cyt_deam_tetra).

## Fly paralogs

Pairwise identity among the three fly SF2 paralogs is 49-54%, similar to their identity with human CDA (45-47%),
so CG8353 is one of three lineage-specific fly duplicates of a single CDA ortholog; none is singled out as the
direct ortholog by this analysis, and no fly paralog has been characterised biochemically.

## Limitations

Pairwise alignments only; no tree was built. The UniProt entry contains no signal peptide or transmembrane feature.
Residue retention is necessary but not sufficient for activity; no CG8353 enzyme assay exists.
