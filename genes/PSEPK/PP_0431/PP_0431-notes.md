# PP_0431 assessment notes

## Identity and core reaction

Q88QQ7 (PP_0431) is a predicted HemJ-family, four-pass cell-membrane
protoporphyrinogen IX oxidase. UniProt assigns the acceptor-dependent RHEA:62000
reaction, one heme-b cofactor per subunit, and four transmembrane segments
[file:PSEPK/PP_0431/PP_0431-uniprot.txt "Catalyzes the oxidation of protoporphyrinogen IX to"]
[file:PSEPK/PP_0431/PP_0431-uniprot.txt "Binds 1 heme b (iron(II)-protoporphyrin IX) group per subunit."].
These are family/rule-based predictions rather than direct KT2440 biochemistry.

## OpenScientist assessment

The OpenScientist report correctly identifies the target, the HemJ-family
reaction, its membrane architecture, and the absence of a direct PP_0431 assay.
Its ortholog discussion supports the family assignment but does not establish
that PP_0431 is essential or the sole KT2440 protoporphyrinogen oxidase. The
report also overstates oxygen independence, the physiological electron
acceptor, and a specific lateral-transfer history. Those claims were not used
as target evidence.

## Curation decisions

GO:0070818 is accepted as the predicted core molecular function, and the
plasma-membrane annotation is accepted from the four-pass topology prediction.
The broad metal-binding row is modified to heme binding because UniProt predicts
one heme-b cofactor per subunit. GO:0006785 is proposed as a strongly supported
new endpoint process annotation because the protoporphyrin IX product directly
feeds ferrochelatase. The native membrane electron acceptor remains unresolved.
