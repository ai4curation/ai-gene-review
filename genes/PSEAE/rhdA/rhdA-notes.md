# rhdA (PA4956, Q9HUK9) notes

Principal cytoplasmic rhodanese (thiosulfate:cyanide sulfurtransferase, EC 2.8.1.1). No
deep-research provider was available; literature search by hand (PubMed metadata; full text of
PMID:17098912 in the cache, PMC1796984; abstract of PMID:15522204).

## Literature

- Cipollone et al. 2004 (PMID:15522204; abstract): recombinant RhdA transfers sulfur from
  thiosulfate to cyanide via a persulfide on Cys230 ["the titration of active Pa RhdA with cyanide
  indicates the presence of one extra sulfur bound to the Cys230 Sgamma atom per active enzyme
  molecule"]; Km thiosulfate 1.0 mM (pH 7.3), Km cyanide 14 mM, Vmax 750 umol/min/mg.
- Cipollone et al. 2007 (PMID:17098912; full text): fractionation with ICDH and beta-lactamase
  markers places RhdA in the cytoplasm; the deletion mutant keeps 12% of cytoplasmic rhodanese
  activity and is complemented ["remarkable differences were observed at the cytoplasmic level,
  with PAO1Δ rhdA showing 12% of wild-type activity"]; impaired growth under cyanogenic
  conditions and outcompeted by wild type.

## Review decisions

- GO:0004792 (EXP, IMP, IEA): ACCEPT, core. GO:0005737 (EXP, IEA): ACCEPT.
- GO:0016783 IBA: TOO_GENERAL (GO:0004792 is_a GO:0016783).
- Considered a NEW cyanide metabolic process (GO:0019499) term; not added, since the in vivo
  evidence is a growth phenotype and resting cells barely convert exogenous cyanide. Left as a
  suggested question.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000146159 | GO:0016783 sulfurtransferase activity | 10 | 44 (34 taxa) | GO:0004792, IMP, PMID:17098912 (PseudoCAP); also UniProt EXP PMID:15522204 | SOUND | Full text read: deletion drops cytoplasmic rhodanese activity to 12% and complementation restores it; with recombinant-enzyme kinetics this directly supports the activity. Generic node term suits a clade mixing TST and MPST enzymes. | Bovine TST P00586, E. coli SseA P31142 and YnjE P78067, mouse/rat MPST, zebrafish, yeast S000005777, Arabidopsis AT1G16460/AT1G79230 | Yes |

No PSEUDOCAP or GO_CENTRAL defect.
