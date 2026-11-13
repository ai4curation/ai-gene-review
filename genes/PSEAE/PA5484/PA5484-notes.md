# PA5484 (KinB, Q9HT87) review notes

No deep-research provider was available. Literature checked: cached PMID:9218420 (abstract only),
PMID:23024348 (full text); Europe PMC search "KinB AND aeruginosa AND phosphatase" (2026-11-05)
found no further biochemical papers. UniProt has no gene name; the protein is KinB in the literature.

## Function

- Autokinase and AlgB phosphotransferase [PMID:9218420 "COOH-terminal KinB protein was observed to undergo progressive"
  autophosphorylation; "rapidly transferred to purified AlgB. Substitutions of the residues conserved"].
- Inner-membrane topology with periplasmic N-terminus [PMID:9218420 "indicate that KinB localizes to the inner membrane and has a NH2-terminal"].
- Phospho-AlgB phosphatase, the dominant in vivo output [PMID:23024348 "Together, these data argue that KinB exhibits
  phosphatase activity and can directly dephosphorylate AlgB."]. P390S abolishes phosphatase but not autophosphorylation.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001293174 | GO:0000155 phosphorelay sensor kinase activity | 3 | 30 (13 taxa) | GO:0000155, IDA, PMID:9218420 (PseudoCAP) | SOUND | The abstract reports autophosphorylation of purified KinB and phosphotransfer to AlgB, abolished by substitution of conserved residues. The node term suits a sensor histidine kinase clade. | E. coli EnvZ (P0AEJ4), P. aeruginosa ParS (Q9I2U4) | Yes; EnvZ is a model sensor kinase. No defect. |

Other PseudoCAP row: IDA phosphatase activity (PMID:23024348) is sound but general; MODIFY to
GO:0004721 phosphoprotein phosphatase activity (substrate phospho-AlgB). No source defect.

No shared PAINT node with the other genes in this batch or with speE2/np20.
