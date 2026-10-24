# Aldh7a1 (mouse, Q9DBF1): ortholog comparison

Date: 2026-10-20

## Inputs and method

- `orthologs.fasta`: canonical UniProt sequences downloaded with
  `curl "https://rest.uniprot.org/uniprotkb/stream?query=accession:Q64057+OR+accession:Q2KJC9+OR+accession:Q803R9+OR+accession:Q28GS6+OR+accession:P49419+OR+accession:Q9DBF1&format=fasta"`
  (the zebrafish accession Q803R9 returned no entry and is absent).
- `compare_orthologs.py`: global pairwise alignment of each ortholog to mouse
  Q9DBF1 (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5).
  Raw output: `compare_orthologs.out`.
- PANTHER 19.0 subfamily assignments were read from the release classification
  files under `.cache/panther/PTHR19.0_*`, and PAINT IBD rows from
  `interpro/panther/PTHR43521/PTHR43521-paint.tsv`.

## Results

| Ortholog | Identity to mouse | Catalytic Glu296 / Cys330 | Residue at mouse 130 |
|---|---|---|---|
| human P49419 | 0.883 (539 columns) | E296 / C330 | S130 |
| cow Q2KJC9 | 0.868 | E296 / C330 | S130 |
| rat Q64057 | 0.941 | E296 / C330 | R130 |
| Xenopus Q28GS6 | 0.810 | E268 / C302 | H102 |

Mouse window 125-135 is `IQLLGRLVSLE`; human is `IQVLGSLVSLE`.

Mouse R130 aligns to human Ser130 (Ser102 in the 511-residue human isoform 2
numbering), the residue annotated in human P49419 as phosphorylated by AMPK. In
human cells, phosphorylation at this site controls ALDH7A1 membrane recruitment
(PMID:31492851, PMID:40233740). Mouse and rat carry Arg and Xenopus carries His
at this position, so this AMPK site is not conserved in mouse.

Both catalytic residues (Glu296 and Cys330) are conserved in all orthologs
compared.

PANTHER 19.0 puts mouse Q9DBF1 in PTHR43521:SF1. Rat, cow, chicken, Xenopus,
Drosophila, C. elegans, Dictyostelium, Arabidopsis ALDH7B4 and several bacterial
members are also in SF1. Human P49419 is the only listed SF5 member. Mouse and
human are 88% identical across the full length, so this split looks like a
subfamily-HMM classification artifact, not functional divergence. The PAINT node
PTN000192435 contains both mouse and human and carries the IBDs for GO:0004043
and GO:0019477, seeded by MGI:108186, human P49419 and zebrafish. It also
carries IBDs for GO:0008802 and for the locations mitochondrion, cytosol,
nucleus, Golgi membrane and plasma membrane. No IBD at this node covers
ferroptosis, energy homeostasis or the membrane-transport regulation terms.

## Interpretation limits

This is a pairwise comparison, not a phylogeny. A missing phosphosite shows the
human regulatory switch is absent in mouse. It does not show that mouse Aldh7a1
is never recruited to membranes, because other mechanisms could do this.
