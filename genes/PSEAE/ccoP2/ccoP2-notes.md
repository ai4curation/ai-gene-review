# ccoP2 (PA1555, Q9I3G2) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I3G2 --alias ccoP2` (symbol fetch hit
UniProt rate limits). Accession Q9I3G2 matches the worklist (rank 323).
Unreviewed TrEMBL entry, 308 aa. Reviewed together with ccoP1 (Q9I3G5); the
two genes are the only seeds of the same PAINT node, and the full clade
analysis is in `genes/PSEAE/ccoP1/ccoP1-notes.md`. No deep-research provider
was used; PubMed searches returned API errors on 2026-11-05.

### Identity

- CcoP/FixP family (NCBIfam TIGR00782; Pfam FixP_N and two Cytochrome_CBB3
  domains; PANTHER PTHR33751:SF1), two N-terminal TM helices (Phobius 7-25,
  57-76), two heme c sites. Diheme cytochrome c (electron-entry) subunit of the
  cbb3-2 oxidase (ccoN2 Q9I3G0, ccoO2 Q9I3G1, ccoQ2 E1JGJ7, ccoP2 Q9I3G2).

### Literature

- Comolli and Donohue 2004 (PMID:14763990; abstract only):
  [PMID:14763990 "Cbb3-2 appeared to play a more significant role under oxygen
  limitation by nature of its increased abundance and expression compared to
  highly aerated cultures, and the regulation of the cbb3-2 operon by the
  putative iron-sulphur protein Anr."] Abstract frames the work as loss of
  whole isoforms; the same GO:0004129 IMP (20190311) is on all eight cbb3
  subunits in the cached PseudoCAP file.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002435498 | GO:0004129 cytochrome-c oxidase activity | 2 | 32 (12 taxa) | GO:0004129, IMP, PMID:14763990 (PseudoCAP) | OVER-SPECIFIC | Same call as ccoP1: CcoP2 is a subunit of the cbb3-2 oxidase and contributes to its activity, but it is the electron-entry diheme cytochrome c, not the catalytic subunit, and the row repeats an operon-level phenotype on every subunit. PSEUDOCAP WRONG_QUALIFIER (PROBABLE). | ccoP1 Q9I3G5 only (same paper, same issue) | No; see ccoP1. The node is a broad c-type cytochrome clade (cytochromes c4/c552/c554, bc1 QcrC, PvcD). The GO_CENTRAL WRONG_TERM defect (REPOINT to GO:0009055) is recorded once on `genes/PSEAE/ccoP1/ccoP1-ai-review.yaml` and not duplicated here. |

Defects filed here: PSEUDOCAP WRONG_QUALIFIER (PROBABLE) on the IMP row only.

## Decisions summary

- ACCEPT: cytochrome-c oxidase activity (IBA, IMP; as contributes_to in
  core_functions), electron transfer activity, heme binding, plasma membrane.
- MODIFY: oxidative phosphorylation -> aerobic electron transport chain.
- KEEP_AS_NON_CORE: proton transmembrane transport.
