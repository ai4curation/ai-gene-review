# PA2078 (Q9I237) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I237 --alias PA2078`; accession matches the worklist.
Unreviewed entry. No deep-research provider; PubMed eutils and Europe PMC searches failed
during the session. Literature from the PseudoCAP seed paper (PMID:24980978, abstract only)
and the 2015 full-text follow-up (PMID:26154497, cached with `ai-gene-review fetch-pmid`).
Reviewed together with PA2077 (see `genes/PSEAE/PA2077/PA2077-notes.md`).

### Literature

- [PMID:24980978 "PA2078 encodes for the (7S,10S)-hydroperoxide diol synthase enzyme (7,10-DS)
  which allows the conversion of 10-H(P)OME into 7,10-DiHOME."]
- PMID:26154497: PA2078 has two CXXCH heme motifs, but mutating either heme site or the
  putative P450-like cysteine does not affect activity [PMID:26154497 "neither the proximal or
  distal heme groups, nor the cysteine putatively related to P450 enzymes are involved in the
  catalytic activity of PA2078"]. Periplasmic (signal peptide 1-23, PhoA fusion). Co-expression
  with PA2077 relieves PA2077 toxicity [PMID:26154497 "with PA2078 abolishing toxicity"].
- 10-H(P)OME and 7,10-DiHOME are isomers (both C18H34O4), so the 7,10-DS reaction is formally an
  intramolecular hydroxyl transfer (cf. GO:0052879, the fungal 8-hydroperoxide 8S-isomerase).

### Annotation decisions

- GO:0031408 oxylipin biosynthetic process (IMP, IBA): ACCEPT (catalyses the second step).
- NEW GO:0050486 intramolecular hydroxytransferase activity (IMP, PMID:24980978): parent of the
  analogous fungal hydroperoxide isomerase term; a specific term is proposed.
- GO:0004130 cytochrome-c peroxidase activity (IBA): MARK_AS_OVER_ANNOTATED (as PA2077; the
  hemes are not needed for the known activity).
- GO:0009055 electron transfer activity (IEA): MARK_AS_OVER_ANNOTATED.
- GO:0020037 heme binding (IEA): KEEP_AS_NON_CORE (CXXCH motifs present; hemes dispensable for
  activity).
- GO:0098869 cellular oxidant detoxification (IEA from GO:0004130): MARK_AS_OVER_ANNOTATED. PA2078
  does remove a toxic hydroperoxide, but the row rests on the untested peroxidase activity and the
  detoxification role is the authors' interpretation.
- NEW GO:0042597 periplasmic space (IC).
- Action counts: ACCEPT 2, KEEP_AS_NON_CORE 1, MARK_AS_OVER_ANNOTATED 3, NEW 2.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002826263 | GO:0031408 oxylipin biosynthetic process | 2 | 7 (3 taxa) | GO:0031408, IMP, PMID:24980978 | SOUND | Mutant cannot release 7,10-DiHOME; complementation shows PA2078 converts 10-H(P)OME to 7,10-DiHOME, the second step. | PA2077 (Q9I238; PseudoCAP IMP, SOUND) | Yes on the seeds, but the node term does not suit the clade |

The node-level GO_CENTRAL defect (term placed above the PA2077/PA2078 in-paralog duplication, so
it reaches PA0007, PA1941, Bradyrhizobium and Rhodopirellula proteins with no evidence) is
recorded once, on the PA2077 IBA row (`genes/PSEAE/PA2077/PA2077-ai-review.yaml`, PROBABLE). No
PSEUDOCAP defects.
