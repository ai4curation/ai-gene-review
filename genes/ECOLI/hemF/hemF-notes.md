# hemF (P36553, Escherichia coli K-12) curation notes

## Sources and deep research

- Deep research was unavailable (the `just deep-research` perplexity route failed in this
  environment: missing template in the sparse checkout and no provider access). The review rests
  on UniProt P36553, the GOA-cited publications in publications/, and the comparator reviews
  genes/PSEPK/hemF and genes/ECOLI/hemN.

## Evidence

- Cloned by complementation of yeast HEM13 [PMID:8300522 "Here we report the cloning of the hemF
  gene, encoding the aerobic coproporphyrinogen III oxidase from Escherichia coli, by functional
  complementation of a Saccharomyces cerevisiae HEM13 mutant."].
- Enzymology [PMID:12975365 "Molecular oxygen is essential for the enzymatic reaction."]; Mn
  restores activity after chelation [PMID:12975365 "Only the addition of manganese fully restored
  coproporphyrinogen III oxidase activity."]. Abstract only.
- Dimer [PMID:13129604 "behaved as a compact shaped dimer"].
- OxyR induction and requirement during H2O2 stress [PMID:25664592 "These data all indicate that
  during H2O2 stress the induced mangano-enzyme HemF becomes the critical coproporphyrinogen III
  oxidase."]. Either HemF or HemN suffices in unstressed aerobic cells [PMID:25664592 "Both of the
  ΔhemF and ΔhemN single mutants were able to grow at normal rates in the presence of oxygen"].

## Decisions

- GO:0033194 response to hydroperoxide (IEP, IMP): MODIFY to GO:0070301 cellular response to
  hydrogen peroxide. GO:0033194 is defined for hydroperoxides (monosubstitution products of HOOH);
  the stimulus in PMID:25664592 is H2O2 itself.
- GO:0046906 tetrapyrrole binding (IMP): KEEP_AS_NON_CORE (substrate/inhibitor binding entailed by
  activity).
- Homodimerization rows: KEEP_AS_NON_CORE, as in PSEPK/hemF.
- Porphyrin biosynthesis IEA: MODIFY to GO:0006785 heme B biosynthetic process.
