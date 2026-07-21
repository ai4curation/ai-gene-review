# hemL assessment notes

## Identity and core reaction

Q88DP0 (PP_4784) is a HemL-family glutamate-1-semialdehyde 2,1-aminomutase
assigned EC 5.4.3.8. UniProt supports the PLP-dependent conversion of
glutamate-1-semialdehyde to 5-aminolevulinate and a cytoplasmic homodimer
[file:PSEPK/hemL/hemL-uniprot.txt "RecName: Full=Glutamate-1-semialdehyde 2,1-aminomutase"]
[file:PSEPK/hemL/hemL-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"].

The abstract of PMID:7883699 directly lists *Pseudomonas putida* among species
shown to use the tRNA-dependent HemA/HemL route to ALA
[PMID:7883699 "be used by Pseudomonas aeruginosa, Pseudomonas putida, Pseudomonas stutzeri,"].
This is species-level pathway evidence, not purified KT2440 Q88DP0 enzymology.

## OpenScientist assessment

The OpenScientist report correctly identifies Q88DP0/PP_4784, the HemL reaction,
and the P. putida C5 route. It explicitly notes that target-specific enzymology,
structure, essentiality, regulation, and channeling evidence were not found.
Nevertheless, it presents an unsaved 63.4% alignment, exact target-residue
mapping, and ortholog-derived structure and essentiality conclusions as if they
were established for KT2440. Those details are not reproducible from the report
artifacts and were not used as target evidence.

## Curation decisions

GO:0042286 captures the core reaction and GO:0033014 captures direct
tetrapyrrole precursor synthesis. PLP binding remains valid non-core cofactor
information, and cytoplasm is retained from the UniProt assignment. No
target-specific essentiality, HemA-HemL complex, or active-site-residue claim
was added.
