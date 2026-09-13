# NCU04302 E2 subfamily comparison

Objective: compare the complete current target sequence with reviewed Ubc9 SUMO E2 references and the recorded ProtNLM ubiquitin-E2 paragraph donor. This provides sequence evidence for interpreting the conserved E2 fold; it is not a reconstructed phylogeny or an enzyme assay.

Inputs are frozen UniProt JSON files: target Q1K772, human Ubc9 P63279, fission-yeast Ubc9 P40984, and Arabidopsis UBC2 P42745. Reference JSONs were retrieved from `https://rest.uniprot.org/uniprotkb/{accession}.json` on 2026-09-09. Target/donor JSONs live one directory above.

Run `just run` in this directory. The generic command-line script accepts any query/reference UniProt JSONs and has PEP 723 pinned dependencies (Biopython 1.85). It uses global BLOSUM62 alignment, gap opening −10 and extension −0.5, choosing the first optimal alignment. Identity is the number of exact matches divided by positions containing residues in both sequences; coverage is that denominator divided by each input length. Complete alignments, sequence hashes and scores are saved, with an alternative-query/self-alignment control. Raw scores are not probabilities or statistical significance values.
