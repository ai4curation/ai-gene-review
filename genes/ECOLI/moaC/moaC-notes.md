# moaC (P0A738) notes, E. coli K-12

Deep research providers were unavailable for this gene (no API keys in this session), so no
`-deep-research-<provider>.md` file was generated. This review is built from the UniProt record
and the cached publications in `publications/`, most of which are abstract-only.

## Identity

- UniProt P0A738, cyclic pyranopterin monophosphate synthase, EC 4.6.1.17; synonym chlA3;
  b0783. Third gene of the moaABCDE operon. MoaC family (HAMAP MF_01224, TIGR00581, Pfam PF01967).
- Homohexamer, trimer of dimers; active site at the dimer interface
  [PMID:10903949 "The enzyme is organized into a tightly packed hexamer with 32 symmetry."].

## Function

- MoaC converts the MoaA product 3',8-cH2GTP to cPMP
  [PMID:25941396 "that of MoaC is to catalyze the rearrangement of 3',8-cH2GTP into cPMP (cPMP synthase)"].
  Kinetics (KM 0.21 uM, kcat 0.56 min-1) and alanine-scan mutants (D128A, K51A, H77A, E112A,
  K131A abolish activity) are in UniProt from this paper.
- Same division of labour in S. aureus [PMID:23627491 "Instead, 3′,8-cH2GTP is transferred to MoaC where a complex rearrangement reaction proceeds."].

## Curation decisions

- GO:0005515 (RplA co-purification, PMID:15690043): REMOVE per protein-binding policy.
- GO:0032991 and GO:0042802 (hexamer): KEEP_AS_NON_CORE; no specific complex term exists.
- GO:0061799 IDA/IEA and GO:0006777 IEA/IMP: ACCEPT. Core MF GO:0061799.
- Verdicts aligned with genes/PSEPK/moaC (ortholog Q88NC0) and genes/ECOLI/moaA.
