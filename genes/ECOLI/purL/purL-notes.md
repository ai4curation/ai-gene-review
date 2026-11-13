# purL (Escherichia coli K-12, UniProtKB:P15254) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurL is the large single-chain formylglycinamide ribonucleotide (FGAM) synthetase of Escherichia coli, a 1295-residue cytosolic monomer that uses an internal glutaminase domain and ATP to convert formylglycinamide ribonucleotide (FGAR) into formylglycinamidine ribonucleotide (FGAM), the fourth step of de novo IMP biosynthesis. Ammonia can replace glutamine as nitrogen donor in vitro. The E. coli gene was historically named purG.

### Core function evidence

- phosphoribosylformylglycinamidine synthase activity (GO:0004642):
  [PMID:2659070 "The purL gene of Escherichia coli encoding the enzyme formylglycinamidine ribonucleotide (FGAM) synthetase which catalyzes the conversion of formylglycinamide ribonucleotide (FGAR), glutamine, and MgATP to FGAM, glutamate, ADP, and Pi has been cloned and sequenced."]

### Decisions other than ACCEPT

- GO:0005524 ATP binding (IDA, PMID:2659070): KEEP_AS_NON_CORE. ATP is a substrate of the FGAM synthetase reaction.
- GO:0005524 ATP binding (IEA, GO_REF:0000104): KEEP_AS_NON_CORE. ATP is a substrate of the FGAM synthetase reaction.
- GO:0005737 cytoplasm (IBA, GO_REF:0000033): MODIFY -> GO:0005829. Correct but general location; the gene also carries the more specific cytosol term.
- GO:0005737 cytoplasm (IDA, PMID:2659070): MODIFY -> GO:0005829. Correct but general location; the gene also carries the more specific cytosol term.
- GO:0005737 cytoplasm (IEA, GO_REF:0000120): MODIFY -> GO:0005829. Correct but general location; the gene also carries the more specific cytosol term.
- GO:0006164 purine nucleotide biosynthetic process (IBA, GO_REF:0000033): MODIFY -> GO:0006189. Correct but general process; PurL acts specifically in de novo IMP biosynthesis.
- GO:0006164 purine nucleotide biosynthetic process (IEA, GO_REF:0000117): MODIFY -> GO:0006189. Correct but general process; PurL acts specifically in de novo IMP biosynthesis.
- GO:0006541 L-glutamine metabolic process (IDA, PMID:2659070): KEEP_AS_NON_CORE. Glutamine is the amide-nitrogen donor of the reaction.
- GO:0016887 ATP hydrolysis activity (IDA, PMID:2659070): KEEP_AS_NON_CORE. ATP hydrolysis drives the amidine-forming ligation.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
