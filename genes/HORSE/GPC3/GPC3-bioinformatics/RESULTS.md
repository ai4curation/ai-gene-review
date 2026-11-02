# Horse GPC3 (A0A3Q2L6D3) vs human GPC3 (P51654)

Script: `compare_sequences.py` (run with `uv run --script compare_sequences.py`); raw output in `alignment_output.txt`.
Inputs: `A0A3Q2L6D3.fasta`, `P51654.fasta` and `human-GPC3-P51654-uniprot.txt`, downloaded from UniProt REST on 2026-10-21.

## Phylogenetic placement

Both the horse entry and human P51654 carry the same PANTHER subfamily cross-reference, PTHR10822:SF4 (GLYPICAN-3). The horse gene also has VGNC symbol GPC3 and lies on chromosome X, which matches the X-linked human GPC3 locus. The horse protein is therefore the GPC3 ortholog, not another glypican paralog.

## Alignment

- The horse GPC3 protein is 580 aa long, the same length as human GPC3 (580 aa). The global alignment has no gaps: 558 of 580 paired residues are identical (96.21%).
- All 18 human cysteines are conserved, which keeps the glypican disulfide framework intact.
- The furin-like convertase site is conserved: the motif RQYR at 355-358 is present, followed by S359.
- The N-glycosylation asparagines N124, N241 and N418 are conserved.
- The heparan sulfate attachment serines S495 and S509 are conserved.
- The GPI-anchor amidated asparagine N554 is conserved, along with a C-terminal hydrophobic propeptide.

## Conclusion

The horse GPC3 entry is a full-length canonical product. It is not a fragment or an isoform, and it keeps every residue feature that the human GPC3 annotations rest on.
