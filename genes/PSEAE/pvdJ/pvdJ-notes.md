# pvdJ (PA2400, Q9I181) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I181 --alias pvdJ`; accession matches the
worklist. Unreviewed TrEMBL entry. No deep-research provider was used. NCBI
E-utilities, Europe PMC and PubMed MCP search were unavailable; a search of the
local publication cache for "pvdJ" found no PAO1 pvdJ mutant study (hits were
P. syringae, P. putida, PA14 genomics and expression papers).

### Literature

- Two NRPS modules (C-A-PCP x2), PTHR45527:SF1; adjacent to pvdD (PA2399).
- PAO1 pyoverdine NRPSs [PMID:15271355 "Analysis of other IRCPs and the P. aeruginosa genome enabled the remaining pyoverdine NRPSs to be identified."]
  (abstract only; PvdJ is not named in the abstract).
- The PseudoCAP seed paper is about another species, read in full:
  [PMID:19854904 "To investigate the role of iron uptake mediated by the siderophore pyoverdine in the virulence of the plant pathogen Pseudomonas syringae pv. tabaci 6605, three predicted pyoverdine synthesis-related genes, pvdJ, pvdL, and fpvA, were mutated."];
  its pvdJ is described as a [PMID:19854904 "pyoverdine side chain peptide synthetase III"] (an L-Thr-L-Ser component).

### Decisions

- ACCEPT: pyoverdine biosynthetic process (IMP; claim true, evidence defect),
  cytosol (IBA), phosphopantetheine binding (IBA, IEA).
- MODIFY: catalytic activity (IMP, IEA) -> GO:1904091; obsolete GO:0043041 (IBA,
  IEA) -> GO:0002049.
- TOO_GENERAL: cytoplasm (IBA), secondary metabolite biosynthetic process (IEA).
- REMOVE: enterobactin biosynthetic process, enterobactin synthetase complex,
  2,3-dihydroxybenzoate-serine ligase activity (IBA from E. coli EntF at
  PTN002378853; P. aeruginosa makes no enterobactin).
- Counts: ACCEPT 4, MODIFY 4, TOO_GENERAL 2, REMOVE 3.

## PseudoCAP IBA-seed assessment

Node-level assessment for PTN002378821 is recorded in genes/PSEAE/pvdD/pvdD-notes.md
(PvdD has the direct PAO1 evidence); summary below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002378821 | GO:0044550 secondary metabolite biosynthetic process | 13 | 72 (22 taxa) | GO:0002049, IMP, PMID:19854904 (PseudoCAP) | WRONG | The mutant is P. syringae pv. tabaci 6605 pvdJ, not PAO1 PA2400; an IMP cannot rest on another species' mutant (PSEUDOCAP WRONG_EVIDENCE_CODE, CONFIRMED, full text read). The claim itself is true for PAO1 PvdJ on other grounds, so the error is in the evidence, not the term. | PvdD (PAO1 mutant, PMID:15271355) plus eleven non-Pseudomonas NRPS seeds (EntF, Aspergillus, S. pombe, M. tuberculosis) | Yes |

No GO_CENTRAL defect for PTN002378821. Separately, the EntF-seeded
enterobactin-specific IBDs at PTN002378853 reach PvdJ; they are REMOVEd here with
`propagation_review` and raised as a suggested question, not filed as a GO_CENTRAL
defect, because that node is not one PvdJ seeds.
