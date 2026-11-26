# LOXL3 (donkey A0A9L0K7N3): re-review sequence and phylogenetic placement

Re-review analysis, 2026-10-21. The earlier files in this folder (`RESULTS.md`,
`align_to_human.py`, `alignment_output.txt`) are left unchanged.

## Methods

Script: `compare_sequences_rereview.py` (PEP 723 inline metadata; Biopython global
PairwiseAligner, BLOSUM62, gap open -10, extend -0.5, free end gaps).
Command (run in this folder):
`uv run --script compare_sequences_rereview.py ../LOXL3-uniprot.txt ../../../HORSE/LOXL3/LOXL3-uniprot.txt ../../../human/LOXL3/LOXL3-uniprot.txt`
Raw output: `compare_sequences_rereview_output.txt`.

Phylogenetic placement was read from the UniProt PANTHER cross-references and from
the repository PAINT table `interpro/panther/PTHR45817/PTHR45817-paint.tsv` and
member list `interpro/panther/PTHR45817/PTHR45817-entries.csv`.

## Results

### Gene-model structure

- Donkey A0A9L0K7N3 (824 aa) is identical to horse A0A9L0TKN1 (753 aa) at all 753 aligned positions. The only differences are two donkey-specific segments with no horse or human counterpart: donkey residues 1-52 (52 aa) and donkey residues 283-301 (19 aa, RKLRKRAAKASARRPKPLG).
- The same two segments are the only unaligned donkey residues against human P58215 (753 aa; 95.62% identity over 753 aligned pairs, 100% coverage of human). Horse and human are also 95.62% identical over their full lengths.
- The 52-aa N-terminal segment sits upstream of the methionine that corresponds to horse and human Met1, so the signal-peptide segment is internal in the donkey model. The 19-aa insertion lies inside the second SRCR domain (UniProt SRCR 223..353), where UniProt flags a missing conserved residue (PROSITE-ProRule PRU00196 caution).
- Both segments are therefore best explained as gene-model errors (an upstream start and a mis-called exon/splice boundary) in the Ensembl donkey prediction, not as donkey-specific biology. The expected donkey LOXL3 product is a 753-aa precursor identical in length to horse and human LOXL3.

### Catalytic residues

- Human copper-binding histidines His607, His609, His611 map to donkey His678, His680, His682; the lysine tyrosylquinone residues human Lys634 and Tyr670 map to donkey Lys705 and Tyr741. All five are conserved, and the catalytic domain is intact.

### Phylogenetic placement

- UniProt places donkey A0A9L0K7N3 in PANTHER PTHR45817:SF2 (LYSYL OXIDASE HOMOLOG 3), the same subfamily as human P58215, mouse Q9Z175 and zebrafish loxl3a/loxl3b in the family member list. Donkey LOXL3 is thus the 1:1 ortholog of human and mouse LOXL3, not a LOX/LOXL1/LOXL2/LOXL4 paralog.
- PAINT IBD assertions in PTHR45817 that cover the LOXL3 subfamily: protein-lysine 6-oxidase activity (GO:0004720) and extracellular region (GO:0005576) at node PTN002550804 (taxon:33213, Bilateria); collagen fibril organization (GO:0030199) and extracellular matrix (GO:0031012) at node PTN008698711 (taxon:7711, Chordata). Donkey descends from both nodes.
- PAINT has no IBD for inflammatory response, negative regulation of T-helper 17 cell lineage commitment, nucleus, elastic fiber or the developmental terms, although mouse Loxl3 carries experimental (IMP) annotations for several of them. Those terms reach donkey only through TreeGrafter or ARBA, not through a PAINT judgement.

## Interpretation

The donkey protein is a full-length LOXL3 ortholog with an intact, invariant catalytic
domain; transfer of the subfamily-level catalytic, extracellular and collagen-fibril
functions is supported by PANTHER SF2 membership and descent from the PAINT nodes.
The 52-aa N-terminal extension and the 19-aa SRCR2 insertion should not be taken as
real protein sequence.
