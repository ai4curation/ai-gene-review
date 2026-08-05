# hemA assessment notes

## Identity and core reaction

Q88PW6 (PP_0732) is a glutamyl-tRNA reductase-family protein assigned EC
1.2.1.70 and RHEA:12344. The UniProt record supports NADPH-dependent reduction
of glutamyl-tRNA(Glu) to glutamate 1-semialdehyde, the first committed reaction
that diverts a translation substrate into tetrapyrrole precursor synthesis
[file:PSEPK/hemA/hemA-uniprot.txt "Catalyzes the NADPH-dependent reduction of glutamyl-tRNA(Glu)"].

The abstract of PMID:7883699 directly lists *Pseudomonas putida* among species
shown to use the tRNA-dependent HemA/HemL route to ALA
[PMID:7883699 "be used by Pseudomonas aeruginosa, Pseudomonas putida, Pseudomonas stutzeri,"].
This is species-level pathway evidence, not purified KT2440 Q88PW6 enzymology.

## OpenScientist assessment

The OpenScientist report correctly identified Q88PW6/PP_0732 and recovered the
species-level C5-route evidence. Its own limitations section states that no
purified-enzyme kinetics were found for the KT2440 protein. Claims about
heme-responsive turnover, a HemA-HemL channeling complex, and operon regulation
derive from other organisms or genomic inference and were not promoted to
KT2440 annotations. The report also gives an unsaved 52.5% pairwise alignment,
exact target-residue mapping, and codon-overlap measurements. Those calculations
are not reproducible from report artifacts and were not used as evidence. PMID:
7883699 supports P. putida use of the C5 route, while its complementation and
hemA-prf1 operon experiments concern P. aeruginosa rather than KT2440.

## Curation decisions

GO:0008883 is retained with the live QuickGO label "glutamyl-tRNA reductase
(NADP+) activity." GO:0033014 is accepted as the direct process term because
the C5 entry chemistry supplies the broader tetrapyrrole branch. The obsolete
route term GO:0019353 is not authored. NADP binding is retained as non-core
cofactor information.
