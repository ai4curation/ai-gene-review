# nuoJ (E. coli K-12, P0AFE0) notes

## 2026-10-23 review session

- Deep-research providers are unavailable in this environment (no API keys), so
  no `-deep-research-*.md` file exists. Literature was reviewed manually from
  cached publications and the UniProt record.
- Key genetics: chromosomal point mutants assemble normally but lose coupled
  activity; Val65 mutants lose proton translocation
  [PMID:15736965 "mutants of the Val-65 residue that is located in the most conserved transmembrane segment significantly lost the coupled electron-transfer activities and exhibited diminished membrane potential and proton translocation"].
- Structure: NuoJ resolved in the E. coli membrane domain and borders the N/K/J/A
  channel [PMID:21822288 "The fourth probable proton-translocation channel is at the interface of subunits N, K, J and A."];
  Thermus Nqo10/11 form the second E-channel half-channel [PMID:23417064 "the second half-channel in Nqo10/11"].
- Membership in affinity-purified complex [PMID:17722886 "The preparation is pure and monodisperse and comprises all known subunits and cofactors."].
- Decisions: GO:0003954 -> GO:0008137, membrane -> plasma membrane, NADH
  dehydrogenase complex -> complex I (MODIFY); all others ACCEPT. No GO:0050136
  row for this gene.
