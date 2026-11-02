# Construct sequence results

The PMID:32203420 supplementary workbook's DOCK7 row labels a human isoform 2 reagent, but its deposited 5,257-nucleotide sequence yields a longest 1,749-residue ORF. The matched blocks correspond to current Q96N67 residues 363–922 and 954–2140, followed by LI. It is therefore not the complete current canonical protein or a sequence-identical full-length natural isoform. This discrepancy limits product assignment; it does not establish that a positive interaction was false or prove which reagent was used in every experiment. The DOCK6 control yields all 2,047 canonical residues followed by LI, demonstrating that the extractor can recover a full-length protein from another row of the same workbook.

The human historical DQ118679.1/AAZ38451.1 CDS used in PMID:23718289 is 1,992 residues and is labelled partial in ENA. It matches current Q96N67 exactly except for absent residues 1–108, 923–953 and 1419–1427. Accordingly, the study's DHR2s 1530–1970 corresponds to current canonical 1678–2118, and DHR2c 1688–1992 corresponds to 1836–2140. The tested C-terminal fragments are human DOCK7 sequence; the paper's historical full-length label does not make the 1,992-residue template a current natural full-length product. The 632-residue natural product is outside this assayed DHR2 scope.

The exact-sequence comparison script also returns complete equality for independent DOCK6 FASTA versus its official UniProt sequence. No function prediction is encoded by the sequence programs.

- [x] Both scripts use explicit inputs and derive their output from the supplied data; conclusions are outside code.
- [x] Both scripts were executed on DOCK6 as an independent-gene control.
- [x] Analyses completed successfully, with direct machine outputs retained here.
- [x] Source hashes, database identifiers, workbook coordinates and comparison conventions are recorded.
- [x] The distinction between deposited DNA, historical clone labels and actual experimental product identity is explicit.

These checks establish the deposited-sequence relationships only. Full historical construct authentication and activity of untested natural products remain unresolved.
