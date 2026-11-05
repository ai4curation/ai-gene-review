# bfd (PA3530, Q9HY80) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HY80 --alias bfd`; accession matches the worklist.
No deep-research provider used. PMID:17915950 (the only GOA-cited paper) is abstract-only (no PMC
copy). Later Bfd papers (PMID:19575528, 22812654, 26368531, 28318006, 30183257, 35327558) are not
cached; their findings are taken from the curated Swiss-Prot record (ECO:0000269 statements).

### Literature

- Bfd is a 73-residue [2Fe-2S] protein [PMID:17915950 "Biochemical and spectroscopic investigations demonstrated that the bfd gene encodes a 73-amino acid protein (pa-Bfd) that incorporates a [2Fe-2S]2+/+ center"].
- Electron transfer from Bfd to heme oxygenase is sluggish, so FPR, not Bfd, is the HemO partner [PMID:17915950 "In comparison, electron transfer from pa-Bfd to pa-HO is sluggish"].
- Bfd binds bacterioferritin BfrB (up to 12 per 24-mer) and is required for mobilizing Fe from the
  BfrB core; mobilization needs the [2Fe-2S] cluster (UniProt CC FUNCTION, PubMed:19575528,
  22812654, 26368531, 28318006, 30183257). The bfd mutant accumulates unmobilizable iron in BfrB
  under low iron (UniProt CC DISRUPTION PHENOTYPE, PubMed:28318006).
- Induced by iron starvation (PMID:12207696, via UniProt CC INDUCTION).

### Annotation decisions

- ACCEPT: GO:0051537 (IDA, IBA).
- No NEW rows proposed. The iron-mobilization role (bacterioferritin iron release, intracellular
  iron ion homeostasis) is well supported by later papers but they are not cached here; recorded
  for a future pass.
- Action counts: ACCEPT 2. No source defects.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002205442 | GO:0051537 2 iron, 2 sulfur cluster binding | 2 | 12 (12 taxa) | GO:0051537, IDA, PMID:17915950 (PseudoCAP) | SOUND | Abstract states outright that Bfd incorporates a [2Fe-2S] centre (spectroscopy); confirmed by later structures. | E. coli Bfd P0AE56 (IDA PMID:8639572, PMID:8954950) | Yes |

Node term suits the clade: the 12 leaves are Bfd-family proteins carrying the Fer2_BFD
(BFD-like [2Fe-2S]-binding) domain with its conserved cysteines.
