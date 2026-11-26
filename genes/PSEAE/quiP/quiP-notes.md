# quiP (PA1032, Q9I4U2) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I4U2 --alias quiP` (first attempt hit a UniProt 429);
accession matches the worklist. Reviewed entry. No deep-research provider was used; literature
from the cached seed paper (full text). Reviewed together with pvdQ and PA0305 (shared node
PTN002151232; node-level record kept in `genes/PSEAE/pvdQ/pvdQ-notes.md`).

### Literature

- PMID:16461666 (Huang et al. 2006), full text cached and read.
  - Mutant: [PMID:16461666 "Transposon mutants of quiP were defective for growth when P.
    aeruginosa was cultured in medium containing decanoyl-HSL as a sole carbon and energy
    source."], complemented by plasmid quiP.
  - Activity: [PMID:16461666 "The results confirm that quiP encodes a protein with acyl-HSL
    acylase activity."] E. coli expressing quiP released near-stoichiometric HSL from C8-HSL and
    degraded C7 to C14 acyl-HSLs, not C4/C6.
  - Location is predicted only: [PMID:16461666 "PA1032 is predicted to be secreted into the
    periplasm based on its signal sequence"].
- The PseudoCAP row is coded IMP, but the decisive data are the heterologous-expression
  activity assay (whole cells, product HSL measured by LC/MS), which is closer to IDA. The
  evidence code understates the support; not worth a defect.

### Annotation decisions

- GO:0016811 (IBA, IMP, IEA): ACCEPT, core MF (no GO term for AHL acylase; one is proposed on
  the pvdQ review).
- GO:0016787 (IEA): TOO_GENERAL.
- GO:0017000 antibiotic biosynthetic process (IEA, InterPro S45): REMOVE (penicillin acylase
  mapping; QuiP is an AHL acylase).
- GO:0042597 periplasmic space (IEA): ACCEPT (signal peptide 1-26; family).
- Action counts: ACCEPT 4, TOO_GENERAL 1, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002151232 | GO:0016811 hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides | 3 | 21 (13 taxa) | GO:0016811, IMP, PMID:16461666 (PseudoCAP) | SOUND | Heterologous expression confers long-chain AHL acylase activity with HSL product measured (full text); mutant cannot grow on C10-HSL. | pvdQ Q9I194 (purified enzyme, IDA), PA0305 Q9I6I6 (purified enzyme, IDA) | Yes (see pvdQ notes for the node-level record) |

No PSEUDOCAP or GO_CENTRAL defect on quiP.
