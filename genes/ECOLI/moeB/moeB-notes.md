# moeB (P12282) notes, E. coli K-12

Deep research providers were unavailable for this gene (no API keys in this session), so no
`-deep-research-<provider>.md` file was generated. This review is built from the UniProt record,
the PTHR10953 PAINT table and the cached publications in `publications/` (mostly abstract-only).

## Identity

- UniProt P12282, molybdopterin-synthase adenylyltransferase, EC 2.7.7.80; synonym chlN; b0826.
  HesA/MoeB/ThiF family, PANTHER PTHR10953:SF194; single ThiF (PF00899) domain, no rhodanese domain.

## Function

- ATP-dependent MoaD adenylation [PMID:11463785 "we have demonstrated the ATP-dependent formation of a complex of MoeB and MoaD adenylate that is stable to gel filtration"].
- No thioester and no MoeB-bound sulfur [PMID:11463785 "the formation of a thioester intermediate between MoeB and MoaD could not be observed"].
- Zinc site cysteines (C172/C175/C244/C247) required.

## PAINT reading (PTHR10953)

- PTN000102040 (deep E1/ThiF node): GO:0016779 IBD seeded by Uba4, MOCS3, MoeB, ThiF (sound, but
  general for MoeB -> MODIFY to GO:0061605); GO:0004792 IBD seeded by Uba4 only (rhodanese domain
  activity; over-propagated to single-domain MoeB -> REMOVE, source defect GO_CENTRAL).
- PTN000102608 (bacterial MoeB/ThiF node): GO:0005829 IBD (sound); GO:0008146 sulfotransferase IBD
  seeded by Mtb MoeZ P9WMN7 only (PAPS sulfate transfer; wrong term and wrong node -> REMOVE,
  source defect GO_CENTRAL).
- `just paint-losses ECOLI moeB`: no IRD/IKR on the lineage.
- Consistent with the PTHR10953 family review (PTN000102040 GO:0004792 TOO_DEEP; PTN000102608
  GO:0008146 WRONG_NODE).

## Other decisions

- GO:0008641 (InterPro IPR035985): REMOVE; GO definition requires thiolester formation.
- Bare GO:0005515 (DnaK, MoaD): REMOVE. Cytoplasm IBA: MODIFY to cytosol.
- Core MF GO:0061605; complex GO:1990133; cytosol. Same verdicts as genes/PSEPK/moeB.
