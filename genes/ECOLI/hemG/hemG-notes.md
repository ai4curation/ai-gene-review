# hemG (P0ACB4, Escherichia coli K-12) curation notes

## Sources and deep research

- Deep research was unavailable (the `just deep-research` perplexity route failed in this
  environment). The review rests on UniProt P0ACB4, the GOA-cited publications, and the PAINT
  file interpro/panther/PTHR38030/PTHR38030-paint.tsv (node PTN002445460, seeds P0ACB4 and
  Q4QIU7, IBDs for GO:0010181, GO:0070819, GO:0006783).

## Evidence

- Mutant SASX38: heme-deficient, normal ferrochelatase [PMID:390093 "Since it possessed normal
  ferrochelatase activity, it was assumed to be deficient in protoporphyrinogen oxidase activity."].
- Cloning by complementation [PMID:7788523 "By complementation analysis using VSR751, we isolated and
  identified this gene."].
- Enzymology: menadione-dependent, FMN flavodoxin, not O2-dependent [PMID:19583219 "These findings
  reveal a previously unidentified class of PPO enzymes that do not utilize oxygen as an electron
  acceptor"].
- Electron flow to respiratory chains [PMID:20484676 "Four electron transport chains from HemG via
  diverse quinones to Cyo, Cyd, Nar, and Frd were reconstituted in vitro from purified components."].
- Membrane-fraction, menaquinone-dependent activity [PMID:365243 "The activity was located exclusively
  in the membrane fraction of cell-free extracts."].

## GO terms checked (QuickGO)

- GO:0004729 protoporphyrinogen oxidase activity, oxygen as acceptor: "3 O2 + protoporphyrinogen IX =
  3 H2O2 + protoporphyrin IX".
- GO:0070819 protoporphyrinogen oxidase activity, quinone as acceptor: "protoporphyrinogen IX + 3 a
  quinone = protoporphyrin IX + 3 a quinol" (EC 1.3.5.3). Both are is_a GO:0070818.

## Decisions

- GO:0004729 (InterPro2GO from IPR044264): MODIFY to GO:0070819; source defect against the
  interpro2go mapping (IPR044264 is mapped to both).
- GO:0005515 FrdA IPI: REMOVE per protein-binding policy.
- plasma membrane (IEA) and membrane (IDA PMID:365243): MODIFY to GO:0009898 cytoplasmic side of
  plasma membrane (peripheral, soluble flavodoxin with no signal peptide; cytoplasmic substrate;
  FrdA association).
- electron transfer activity (IEA flavodoxin CS): KEEP_AS_NON_CORE.
