# PA0305 (HacB, Q9I6I6) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I6I6 --alias PA0305`; accession matches the worklist.
Unreviewed entry (name from ProtNLM). No deep-research provider was used; literature from the
cached seed paper (abstract only; PubMed MCP gave no full text). Reviewed together with pvdQ and
quiP (shared node PTN002151232; node-level record kept in `genes/PSEAE/pvdQ/pvdQ-notes.md`).

### Literature

- PMID:21372094 (Wahjudi et al. 2011), abstract only. Purified PA0305 is processed into alpha
  and beta subunits with the catalytic serine at the beta N-terminus, and degrades AHLs
  [PMID:21372094 "Using a biosensor assay, PA0305his was shown to degrade AHLs with acyl side
  chains ranging in length from 6 to 14 carbons."], with kinetics for C8-HSL and 3-oxo-C12-HSL;
  the authors name it HacB.
- PMID:16461666 (Huang et al. 2006, full text): a PA0305 transposon mutant grew normally on
  C10-HSL, so PA0305 is not the acylase for AHL growth; in that study's E. coli expression the
  QuiP activity was reported, not PA0305's.
- Location: UniProt periplasm is an ARBA prediction. The sequence begins
  MKRTLTVIAVAVAAAAAGGAWYLH, a short basic stretch followed by a hydrophobic segment, consistent
  with a Sec signal peptide as in its periplasmic paralogs PvdQ and QuiP (own inspection, not a
  SignalP run). Accepted as a family-level location.

### Annotation decisions

- GO:0016811 (IBA, IDA, IEA): ACCEPT, core MF.
- GO:0016787 (IEA): TOO_GENERAL.
- GO:0017000 antibiotic biosynthetic process (IEA): REMOVE.
- GO:0042597 periplasmic space (IEA): ACCEPT.
- Action counts: ACCEPT 4, TOO_GENERAL 1, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002151232 | GO:0016811 hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides | 3 | 21 (13 taxa) | GO:0016811, IDA, PMID:21372094 (PseudoCAP) | SOUND | Abstract reports purified enzyme degrading C6-C14 AHLs with kcat/Km values. | pvdQ Q9I194 (IDA), quiP Q9I4U2 (IMP; heterologous activity) | Yes (see pvdQ notes for the node-level record) |

No PSEUDOCAP or GO_CENTRAL defect on PA0305.
