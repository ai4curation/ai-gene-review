# oprD (OccD1, P32722) review notes

No deep-research provider was available. Sources: UniProt P32722 (Swiss-Prot), cached abstracts of
PMID:2118530, 2109575, 8843159, 8012497, 2120174; full text of PMID:22272184 (Eren et al. 2012).

## Function

- Basic amino acid/peptide channel [file:PSEAE/oprD/oprD-uniprot.txt "Porin with a specificity for basic amino acids"];
  [PMID:2118530 "Wild type cells transported tripeptide Thr-Ser-Lys into the"].
- Carbapenem entry [PMID:22272184 "uptake of this antibiotic is only mediated by OccD1 and not by OccD2/D3"].
- Reported serine protease activity [PMID:8843159 "purified protein D2 hydrolyzed several synthetic peptides according to the"].

## PseudoCAP IBA-seed assessment

PTN002160747 (porin activity) is shared by oprD, oprE and opdP, all reviewed in this batch with consistent verdicts.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002160747 | GO:0015288 porin activity | 3 | 24 (6 taxa) | GO:0015288, IMP, PMID:2120174 (PseudoCAP); also UniProt IDA PMID:2118530 | INDIRECT-PHENOTYPE (PseudoCAP row) | Abstract: transductants lost four OM proteins (C, D2, E1, E2) at once, and the authors conclude only that at least one is a porin; the IMP cannot be attributed to OprD alone. The term is correct (UniProt IDA, structures, electrophysiology). PSEUDOCAP WRONG_EVIDENCE_CODE/CHECK, PROBABLE (same defect on oprE). | OpdP (Q9HVS0), OprE (G3XDA5) | Yes; OprD's own UniProt IDA (PMID:2118530) is the strongest seed. Node term suits the Occ channel clade. No GO_CENTRAL defect. |

This gene carries the most direct evidence for the shared node; no node-level GO_CENTRAL defect is
needed, so none is recorded on any of the three porins.
