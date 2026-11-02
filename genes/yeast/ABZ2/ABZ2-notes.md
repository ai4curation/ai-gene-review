# ABZ2 (YMR289W, Q03266) notes

- ADC lyase, EC 4.1.3.38, PLP-dependent, class IV aminotransferase fold [UniProt:Q03266].
- "The presence of Abz2p catalyzed the conversion of ADC into PABA in a time-dependent manner." [PMID:17873082]
- "ABZ2 was able to rescue the p-aminobenzoate auxotrophy of an Escherichia coli pabC mutant" [PMID:17873082]
- The enzyme is a homodimer: "only fractions containing the dimeric Abz2p were enzymatically active" [PMID:17873082].
- It is the founder of a fungal ADC lyase group with no significant homology to the bacterial or plant enzymes [PMID:17873082].
- It is cytoplasmic by GFP [PMID:17873082, PMID:14562095].

## Curation decisions
- I added GO:0008153 (4-aminobenzoate biosynthetic process) as NEW, with IDA from PMID:17873082. Abz2p catalyses the last step of that process, so this is participation, not mere requirement. ABZ1 already carries the term.
- GO:0003824 (catalytic activity) is changed to GO:0008696.
- The chorismate metabolic process row is marked over-annotated, because the substrate is ADC, not chorismate.
- The folate cycle row is removed.
- The folic acid biosynthesis rows (IMP and RCA) are changed to GO:0046654.
