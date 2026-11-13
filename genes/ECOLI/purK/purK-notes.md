# purK (Escherichia coli K-12, UniProtKB:P09029) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurK is the N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) synthetase of Escherichia coli, a homodimeric ATP-grasp enzyme that uses MgATP and bicarbonate to carboxylate the exocyclic amine of aminoimidazole ribonucleotide (AIR), forming N5-CAIR. PurE then rearranges N5-CAIR to CAIR; together the two enzymes perform AIR carboxylation, step 6 of de novo IMP biosynthesis. PurK has no counterpart in animals.

### Core function evidence

- 5-(carboxyamino)imidazole ribonucleotide synthase activity (GO:0034028):
  [PMID:8117684 "PurK is shown, by NMR spectroscopy, to catalyze the conversion of AIR in the presence of HCO3- and ATP to ADP, P(i), and the carbamate of AIR (designated N5-CAIR)."]

### Decisions other than ACCEPT

- GO:0004638 phosphoribosylaminoimidazole carboxylase activity (IBA, GO_REF:0000033): MODIFY -> GO:0034028. PurK makes N5-CAIR; it does not carboxylate AIR to CAIR directly.
- GO:0004638 phosphoribosylaminoimidazole carboxylase activity (IDA, PMID:8117684): MODIFY -> GO:0034028. PurK makes N5-CAIR; it does not carboxylate AIR to CAIR directly.
- GO:0004638 phosphoribosylaminoimidazole carboxylase activity (IEA, GO_REF:0000002): MODIFY -> GO:0034028. PurK makes N5-CAIR; it does not carboxylate AIR to CAIR directly.
- GO:0005524 ATP binding (IDA, PMID:19053251): KEEP_AS_NON_CORE. ATP is a co-substrate, seen bound in the crystal structure.
- GO:0005524 ATP binding (IDA, PMID:8117684): KEEP_AS_NON_CORE. ATP is required for the PurK reaction.
- GO:0005524 ATP binding (IEA, GO_REF:0000002): KEEP_AS_NON_CORE. ATP is a co-substrate, seen bound in the crystal structure.
- GO:0006144 purine nucleobase metabolic process (IBA, GO_REF:0000033): MODIFY -> GO:0006189. Nucleobase-process term misclassifies a ribonucleotide pathway step.
- GO:0016879 ligase activity, forming carbon-nitrogen bonds (IEA, GO_REF:0000117): MODIFY -> GO:0034028. Correct but general ligase class.
- GO:0046872 metal ion binding (IEA, GO_REF:0000002): MODIFY -> GO:0000287. Two Mg2+ ions are bound in the active site.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
