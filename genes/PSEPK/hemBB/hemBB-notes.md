# hemBB assessment notes

## Identity and core reaction

Q88HN1 (PP_3322) is one of two KT2440 ALAD-family proteins assigned EC
4.2.1.24. UniProt predicts condensation of two 5-aminolevulinate molecules to
porphobilinogen, two Schiff-base active-site lysines, and an Mg2+-binding site
[file:PSEPK/hemBB/hemBB-uniprot.txt "RecName: Full=Delta-aminolevulinic acid dehydratase"]
[file:PSEPK/hemBB/hemBB-uniprot.txt 'ligand="Mg(2+)"'].
These are sequence/rule-based assignments rather than direct KT2440
biochemistry.

## OpenScientist assessment

The OpenScientist report correctly identifies Q88HN1/PP_3322 as an ALAD-family
candidate and recognizes that its metal dependence is a bioinformatic
prediction. It incorrectly describes PP_3322 as the single KT2440 hemB/PBGS
gene and does not consider the second ALAD-family protein, Q88IT6/PP_2913. The
report also presents unsaved target-sequence analysis and transfers oligomeric
state, metal behavior, essentiality, and antibacterial-target claims from other
proteins. These claims were not used as target evidence.

## Curation decisions

GO:0004655 is accepted as the predicted core molecular function. The imported
zinc-binding row is modified to GO:0000287 because the current UniProt feature
table predicts Mg2+ binding and lacks the catalytic zinc-ligand triad found in
the KT2440 HemB paralog. Generic metal binding is retained as non-core. Neither
review nor module asserts that HemBB is the physiologically dominant paralog.
