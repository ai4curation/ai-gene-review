# PA5542 (Q9HT32, PIB-1) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL, with PDB 8RLJ/8RLK/8RLL),
cached PMID:25185138 (abstract only) and PMID:39097051 (abstract only, fetched for this review).
PubMed searches through the MCP ("PA5542 imipenemase", 2026-11-05) returned no hits (search service
failing), so the literature beyond these two papers was not surveyed.

## Function

- Purified PA5542 hydrolyses imipenem; zinc stimulates it
  [PMID:25185138 "Spectrophotometric analyses showed that PA5542 is a Zn(2+)-dependent imipenemase."].
- Knockout raises, overexpression lowers carbapenem susceptibility
  [PMID:25185138 "Lack of PA5542 increases P. aeruginosa 59.20 susceptibility to carbapenems and its overexpression reduces E. coli susceptibility to these β-lactams."].
- Structures place PIB-1 in class C beta-lactamases; carbapenems but not cephalosporins are degraded;
  metal ions do not bind the active site but promote more active trimers
  [PMID:39097051 "These crystal structures show that it belongs to the Class C β-lactamase group"].
- Sequence: SignalP signal peptide 1-25; PF00144 domain 94-408; S-x-x-K motif SVVK at residue 131
  (checked on the UniProt sequence). PANTHER PTHR43283:SF14.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN009168613 | GO:0016787 hydrolase activity | 3 | 68 (26 taxa) | GO:0008800 beta-lactamase activity, IDA, PMID:25185138 (PseudoCAP) | SOUND | Purified enzyme hydrolyses imipenem in a spectrophotometric assay (abstract); confirmed by the 2024 structural/functional paper. The generic hydrolase node term suits a PF00144 clade of penicillin-binding-fold hydrolases. | E. coli PBP4B/YfeW P77619 (IDA DD-carboxypeptidase, PMID:16402224); B. subtilis AmiE/YbbE O05213 (EXP N-acetylmuramyl-L-alanine amidase, PMID:20400549) | Yes; both other seeds carry experimental hydrolase descendants. No GO_CENTRAL defect. |

Defects recorded: PSEUDOCAP 0; GO_CENTRAL 0.
