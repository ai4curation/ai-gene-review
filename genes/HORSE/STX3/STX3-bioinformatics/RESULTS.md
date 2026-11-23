# Horse STX3 A0A3Q2H352: isoform/exon assignment

Script: `compare_isoform_segments.py` (run `uv run --script compare_isoform_segments.py`);
inputs are UniProt FASTA records in `sequences.fasta`; raw output in `output.txt`.

## Findings

- A0A3Q2H352 is 289 residues and carries the complete syntaxin architecture: the N-terminal Habc region, the SNARE motif and a C-terminal transmembrane anchor.
- Residues 1-226 (N-peptide, Habc domain and the N-terminal half of the SNARE motif up to the 0-layer glutamine region) are 99% identical to mouse Stx3 3A, mouse 3B and human STX3 isoform A.
- The SNARE-motif C-terminal half (residues 227-262, AMIDRIENNMDQSVGFVERAVADTKKAVKYQSEARR) is 100% identical to the mouse 3B-specific segment and only 47% identical to mouse 3A (56% to human isoform A). This is the exon-9B (retinal STX3B) sequence.
- The membrane-anchor segment (residues 263-289, KLIIIIVVVVVLLGILALVIGLSVGLK) is 96% identical to mouse 3A and 89% identical to human isoform A; it is the exon-10A anchor, not the 3B anchor (mouse 3B ends KIMIMICCIILAIILASTIGGIFA).
- The horse gene model therefore combines exon 9B with exon 10A. Human RNA-seq reports STX3A as exons 9A/10A and STX3B as exons 9B/10B; a 9B/10A junction is not one of the two major isoforms described, so this Ensembl model may be a minor splice form or a gene-model artefact. It cannot be decided from protein data alone.
- The other four horse STX3 TrEMBL entries (F7BC79, A0A3Q2H370, A0A5F5PZR6, F6ZUC9) diverge after the 0-layer (residue ~226) and lack a recognisable transmembrane anchor, so A0A3Q2H352 is the only horse STX3 model with an intact SNARE motif plus anchor. There is no reviewed (Swiss-Prot) horse STX3 entry.
