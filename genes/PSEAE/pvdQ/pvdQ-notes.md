# pvdQ (PA2385, Q9I194) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I194 --alias pvdQ` (first attempt hit a UniProt 429);
accession matches the worklist. Reviewed entry. No deep-research provider was used; literature
from the cached papers. Reviewed together with quiP (PA1032) and PA0305, which share the
PTN002151232 node.

### Literature

- PMID:16495538 (Sio et al. 2006), full text cached and read. Purified PvdQ deacylates
  long-chain AHLs [PMID:16495538 "In a bioassay, the purified acylase was shown to degrade AHLs
  with side chains ranging in length from 11 to 14 carbons at physiologically relevant low
  concentrations."]; GC/MS shows lauric acid release [PMID:16495538 "one can conclude that the
  PA2385 protein is an AHL acylase"]. No beta-lactam activity [PMID:16495538 "No activity was
  detected."].
- Pyoverdine maturation: [PMID:19787431 "suggesting a role for PvdQ in the periplasmic
  maturation of PVDI"]; [PMID:21892836 "Structural studies are also presented showing PvdQ
  covalently acylated with the acyl moiety substrate derived from the acyl-pyoverdine
  precursor"].
- Location: [PMID:22498339 "Epifluorescence and TIRF imaging on cells expressing labelled PvdQ
  showed that this enzyme was uniformly distributed in the periplasm"]. The PseudoCAP cytoplasm
  IDA from this paper is therefore wrong (it is PvdA that is cytoplasmic/membrane).
- Phenotypes (biofilm, swarming, antibiotic resistance) are linked by the authors to pyoverdine
  or AHL levels [PMID:19778968 "PvdQ plays a major role in swarming motility, in biofilm
  development and in infection that is more likely to be linked to the pyoverdine pathway"].
  The swarming paper PMID:18245294 used a PA14 mutant.
- GO has no AHL acylase term (EC 3.5.1.97); GO:0016811 is the most specific existing term. A
  new term is proposed.

### Annotation decisions

- GO:0016811 (IBA, IDA, IEA): ACCEPT, core MF.
- GO:0016787 (IEA): TOO_GENERAL.
- GO:0002049 pyoverdine biosynthetic process (IDA, 3x IMP): ACCEPT.
- GO:0005737 cytoplasm (IDA): REMOVE; PSEUDOCAP WRONG_TERM -> GO:0042597, CONFIRMED (abstract
  states periplasm).
- GO:0042597 periplasmic space (IEA): ACCEPT.
- GO:0017000 antibiotic biosynthetic process (IEA, InterPro S45): REMOVE.
- GO:0042802 identical protein binding (IPI): KEEP_AS_NON_CORE.
- GO:0044010, GO:0046677, GO:0071978 x2: MARK_AS_OVER_ANNOTATED (indirect phenotypes).
- Action counts: ACCEPT 8, TOO_GENERAL 1, REMOVE 2, KEEP_AS_NON_CORE 1,
  MARK_AS_OVER_ANNOTATED 4.

## PseudoCAP IBA-seed assessment

Node-level record for PTN002151232 (shared with quiP and PA0305) is kept here.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002151232 | GO:0016811 hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides | 3 | 21 (13 taxa) | GO:0016811, IDA, PMID:16495538 (PseudoCAP) | SOUND | Purified enzyme deacylates AHLs; fatty acid product shown by GC/MS (full text). | quiP Q9I4U2 (SOUND, heterologous activity in E. coli, full text), PA0305 Q9I6I6 (SOUND, purified enzyme kinetics, abstract) | Yes; each of the three seeds independently supports the node term, which suits an Ntn acylase clade of 21 leaves |

No GO_CENTRAL defect on this node. The only PSEUDOCAP defect on pvdQ is the non-seed cytoplasm
row.
