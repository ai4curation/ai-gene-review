# Horse LNPEP (A0A9L0TDM5) versus human LNPEP (Q9UIQ6)

Script: `compare_to_human.py` (PEP 723; run with `uv run --script compare_to_human.py`).
Raw output: `compare_to_human.out`.

## Method

Both sequences were fetched from the UniProt REST API and globally aligned
(Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5). Human motif
patterns (zinc-binding HEXXH-(18)-E, GAMEN exopeptidase motif, tankyrase-binding
RXXPDG) were located by regular expression in both sequences.

## Results

- Lengths: horse 1056 aa, human 1025 aa.
- Identity: 930 of 1025 aligned positions identical (90.7%); every human residue is aligned, so there are no deletions in horse relative to human.
- Length difference: the horse gene model carries an N-terminal extension of about 30 residues (MRKKYYLWKSRWVIFFRAQLSISLLQSFQPFHSKGT) before the sequence that aligns with the human initiator region (human MEPFTNDRLQLP...; horse ...SKGTDRLQLP...), plus a single-residue insertion near horse position 562. The extension lies in the cytosolic N-terminal region, upstream of the Phobius transmembrane helix (horse 140-161), and does not touch the catalytic ectodomain. It is most likely an upstream start codon or exon in the Ensembl gene model (ENSECAT00000084437.1) rather than a conserved protein feature; the benchmark accession should be read as the full-length LNPEP product with a probable N-terminal gene-model extension, not as a fragment.
- Zinc-binding motif HEXXH-(18)-E conserved: horse 494 HELAHQWFGNLVTMQWWNDLWLNE (human 464).
- GAMEN aminopeptidase motif conserved: horse 458 (human 428).
- Tankyrase-binding RXXPDG motif conserved in the cytosolic tail: horse 126 RQSPDG (human 96).
- PANTHER: both horse and human UniProt records place the protein in PTHR11533:SF42 (LEUCYL-CYSTINYL AMINOPEPTIDASE), the LNPEP subfamily of the M1 zinc metalloprotease family.

## Interpretation

Horse LNPEP is the 1:1 ortholog of human LNPEP by shared PANTHER subfamily
(PTHR11533:SF42) and high identity across the full length, with every catalytic
and regulatory motif identified in human retained. Transfer of the human
experimentally established metalloaminopeptidase activity, peptide-hormone and
neuropeptide catabolism, and plasma-membrane/vesicle localization is therefore
justified at the subfamily level. No horse-specific experimental data were found.
