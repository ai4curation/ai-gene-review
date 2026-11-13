# purT (Escherichia coli K-12, UniProtKB:P33221) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurT is the formate-dependent glycinamide ribonucleotide (GAR) transformylase of Escherichia coli, a cytosolic ATP-grasp enzyme that uses ATP and free formate, via a formyl phosphate intermediate, to formylate GAR to FGAR in de novo IMP biosynthesis. It is an alternative to the folate-dependent PurN; only purN purT double mutants require purines. Purified PurT also shows side reactions with acetate and carbamoyl phosphate.

### Core function evidence

- phosphoribosylglycinamide formyltransferase 2 activity (GO:0043815):
  [PMID:8117714 "catalyzes the production of beta-formyl GAR from formate, ATP, and beta-GAR"]

### Decisions other than ACCEPT

- GO:0000166 nucleotide binding (IEA, GO_REF:0000104): MODIFY -> GO:0005524. Correct but general; the nucleotide bound is ATP.
- GO:0000287 magnesium ion binding (IEA, GO_REF:0000002): KEEP_AS_NON_CORE. ATP-grasp enzyme with Mg2+-dependent ATP use.
- GO:0004644 phosphoribosylglycinamide formyltransferase activity (IEA, GO_REF:0000002): REMOVE. Folate-dependent PurN chemistry assigned to PurT.
- GO:0005515 protein binding (IPI, PMID:15690043): REMOVE. Bare protein binding from a high-throughput interaction screen.
- GO:0005515 protein binding (IPI, PMID:24561554): REMOVE. Bare protein binding from a high-throughput interaction screen.
- GO:0005524 ATP binding (IEA, GO_REF:0000120): KEEP_AS_NON_CORE. ATP is a co-substrate of the PurT reaction.
- GO:0008776 acetate kinase activity (EXP, PMID:9184151): MARK_AS_OVER_ANNOTATED. Acetate kinase is a measurable side reaction of the PurT active site, not a physiological role.
- GO:0008776 acetate kinase activity (IDA, PMID:8117714): MARK_AS_OVER_ANNOTATED. Acetate kinase is a measurable side reaction of the PurT active site, not a physiological role.
- GO:0008776 acetate kinase activity (IEA, GO_REF:0000116): MARK_AS_OVER_ANNOTATED. Acetate kinase is a measurable side reaction of the PurT active site, not a physiological role.
- GO:0009152 purine ribonucleotide biosynthetic process (IEA, GO_REF:0000002): MODIFY -> GO:0006189. Correct but general process.
- GO:0016742 hydroxymethyl-, formyl- and related transferase activity (IEA, GO_REF:0000002): REMOVE. Formyltransferase class implies folate-type transfer chemistry that PurT does not use.
- GO:0016879 ligase activity, forming carbon-nitrogen bonds (IEA, GO_REF:0000117): MODIFY -> GO:0043815. Correct but general ligase class.
- GO:0046872 metal ion binding (IEA, GO_REF:0000002): MODIFY -> GO:0000287. Correct but general; the metal is magnesium.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
