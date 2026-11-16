# ispH (lytB, b0029; UniProtKB:P62623) notes

## Identity and reaction

- IspH (LytB) catalyses the last MEP-pathway step, reductive dehydroxylation of HMBPP to a
  mixture of IPP and DMAPP. [PMID:11818558 "into a 5:1 mixture of [U-(13)C(5)]isopentenyl
  diphosphate and [U-(13)C(5)]dimethylallyl diphosphate by an E. coli strain
  engineered for the expression of the ispH (lytB) gene"]
- In vitro activity of the purified enzyme. [PMID:12571359 "enabled purified IspH
  protein to catalyze the conversion of 1-hydroxy-2-methyl-2-(E)-butenyl
  4-diphosphate into a 6:1 mixture of isopentenyl diphosphate and dimethylallyl
  diphosphate"]
- Genetics: essential; deletion viable only with mevalonate bypass [PMID:11418107];
  depletion causes lysis [PMID:11717301].
- IspH makes DMAPP directly, so E. coli does not depend on Idi for DMAPP.

## Cofactor

- [4Fe-4S] protein; requires a reducing system (flavodoxin/flavodoxin reductase/NADPH or
  photoreduced deazaflavin). [PMID:12706830 "Enzymatic activity required the presence of a reducing system such as
  flavodoxin/flavodoxin reductase/reduced nicotinamide adenine dinucleotide
  phosphate or the photoreduced deazaflavin radical."]
- Early EPR/structures saw a [3Fe-4S] cluster [PMID:15469281; PMID:19569147], later
  understood as an oxygen-degraded form; substrate complexes contain [4Fe-4S]
  [PMID:20080550 "While IspH protein crystallizes with substrate bound to a [4Fe-4S] cluster, crystals of IspH in
  complex with IPP, DMAPP or inorganic pyrophosphate feature [3Fe-4S] clusters."]
- Glu126 proton donor [PMID:22137895]; Cys12, Cys96, Cys197 cluster ligands [PMID:15469281].
- In vitro acetylene hydratase side activity on alkyne substrate analogues [PMID:22948824];
  not physiological, not in GOA.

## GO term issue

- GO:0051745 is defined with [2Fe-2S] ferredoxin as electron donor (RHEA:24488/24825),
  while the E. coli enzyme is reduced by flavodoxin in vitro and FldA is the essential
  flavodoxin in vivo (PMID:15978585). No flavodoxin-specific IspH term exists, and the
  label is carrier-neutral, so GO:0051745 is accepted; the definition gap is raised as a
  suggested question (unlike IspG, where a flavodoxin term GO:0141197 exists).
- Literature search: cached PMIDs plus 11717301, 11818558, 12198182, 15469281, 20080550,
  22137895, 22687151, 22948824 fetched with the repo tool.
