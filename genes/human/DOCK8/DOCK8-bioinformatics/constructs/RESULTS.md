# Deposited DOCK8 library product

The DNA in Supplementary Table 1 cell L80 translates to an exact complete match to **Q8NF50-3, 2031 residues**, in forward frame 2 (zero based). The matching protein begins after two amino acids, with RA before the coding body and LI after it. None of the other three official DOCK8 product sequences matches completely. The table itself names a 2031-residue human isoform 3; this independent sequence match supplies the accession assignment.

The DOCK6 control, cell L78, matches the complete 2047-residue human Q96HP0 sequence in frame 0, after GRA and before LI. Both computations use the same parameterized program and the same genuine deposited workbook.

The DOCK8 result identifies the experimental library insert separately from the canonical reference sequence used in IntAct sequence/taxon ROGIDs. Supplementary Table 3 row 674 contains the positive GOLD DOCK8–LRCH2 association. Supplementary Table 2 row 103 contains negative RHOA/RAC1/CDC42 screen calls under the tested conditions. These different measurements do not imply universal inactivity of DOCK8 or functional equivalence of all natural products. No kinetic constant, direct binding affinity, intracellular interface or new physiological function is inferred from this sequence analysis.

Inputs are the [original supplementary workbook](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41556-020-0488-x/MediaObjects/41556_2020_488_MOESM3_ESM.xlsx), official UniProt Q8NF50 product FASTAs and Q96HP0 control FASTA. Exact retrieval URLs, dates and hashes are in `source-manifest.json`. `DOCK8.json` and `DOCK6-control.json` contain the actual results and selected workbook cells; their accompanying FASTAs contain the extracted DNA, including vector flanks. The analysis is deterministic, uses all three forward frames, and has no similarity threshold or random component.

## Analysis checklist

- [x] The analysis script takes input, gene, sequence and output paths as arguments and contains no expected identity or result.
- [x] The same script was run on another gene, DOCK6.
- [x] Both analyses completed successfully.
- [x] Direct JSON results and extracted DNA are included.
- [x] Source hashes, acquisition provenance, methods and limits are recorded.
