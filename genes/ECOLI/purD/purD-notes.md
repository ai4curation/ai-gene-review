# purD (Escherichia coli K-12, UniProtKB:P15640) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurD is the glycinamide ribonucleotide (GAR) synthetase of Escherichia coli, a monomeric ATP-grasp enzyme that ligates glycine to 5-phosphoribosylamine with MgATP hydrolysis to form GAR, the second step of de novo IMP biosynthesis. The enzyme is highly specific for glycine and is encoded in the purHD operon.

### Core function evidence

- phosphoribosylamine-glycine ligase activity (GO:0004637):
  [PMID:2182115 "The purD gene of Escherichia coli encoding the enzyme glycinamide ribonucleotide (GAR) synthetase, which catalyzes the conversion of phosphoribosylamine (PRA), glycine, and MgATP to glycinamide ribonucleotide, MgADP, and Pi, has been cloned and sequenced."]

### Decisions other than ACCEPT

- GO:0005524 ATP binding (IDA, PMID:2182115): KEEP_AS_NON_CORE. ATP is a co-substrate of the ligase.
- GO:0005524 ATP binding (IEA, GO_REF:0000002): KEEP_AS_NON_CORE. ATP is a co-substrate of the ligase.
- GO:0006164 purine nucleotide biosynthetic process (NAS, PMID:2182115): MODIFY -> GO:0006189. Correct but general process; PurD acts specifically in de novo IMP biosynthesis.
- GO:0006974 DNA damage response (IEP, PMID:11967071): MARK_AS_OVER_ANNOTATED. Transcriptome-wide expression change after mitomycin C, not a role in the DNA damage response.
- GO:0009113 purine nucleobase biosynthetic process (IEA, GO_REF:0000002): MODIFY -> GO:0006189. Nucleobase-process term misclassifies a ribonucleotide pathway step.
- GO:0016879 ligase activity, forming carbon-nitrogen bonds (IEA, GO_REF:0000117): MODIFY -> GO:0004637. Correct but general ligase class.
- GO:0016887 ATP hydrolysis activity (IDA, PMID:2182115): KEEP_AS_NON_CORE. ATP hydrolysis drives the ligation.
- GO:0046872 metal ion binding (IEA, GO_REF:0000002): KEEP_AS_NON_CORE. ATP-grasp ligases bind divalent metal ions with ATP.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
