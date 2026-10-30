# Modern PP_1703 CDS check

The exact KT2440 interval AE015451.2:1899450–1903475 contains one 4,026-nt CDS for PP_1703. Bacterial-code translation gives 1,341 residues and a terminal TGA, no internal stop, and exact identity to both AAN67324.2 and Q88M71. These are linked representations of the same genomic model, not three independent experimental replicates. The primary genomic continuity supports accepting that model despite the two historical KT2442 ORFs. See README.md for the historical termination difference and limits; expression of a complete native polypeptide was not assayed here.

## Methods and checks

Python/Biopython 1.85 from the repository's uv environment. `check_modern_cds.py` parses the genomic feature, extracts its actual DNA, translates with the specified code, and compares with the two protein inputs. It reports mismatches with the aligned historical coding segment. No alignment or sequence replacement is inferred across different reading frames. Source hashes are in the JSON result and original download URLs in modern-source-provenance.json.

- [x] The new analysis script has explicit input and output arguments; no target sequence, expected equality, or residue result is hardcoded.
- [x] Tested with a different protein input (Q88M69 NirB) as a specificity control: genomic translation versus that UniProt sequence is false, while comparison with the correct GenPept record remains true. The control does not represent a second biological fusion experiment.
- [x] The exact-locus calculation and supplied just recipe complete successfully.
- [x] Original primary bytes and direct calculated results are preserved in this directory.
- [x] Interpretation, source provenance, KT2442/KT2440 distinctions, and uncertainty are explicit in README.md and this report.

The older historical bridge script remains unchanged. This follow-up checks the modern model directly; it does not reinterpret the historical biological assays as full-fusion enzymology.
