# PA4506 (Q9HVR5) review notes

No deep-research provider was available; notes compiled from the UniProt entry and the cached full text of PMID:25338022.

- Pletzer et al. 2014 (PA14): operon PA14_58440-58490 = dppBCDF; [PMID:25338022 "two encoding the hydrophilic nucleotide- and ATP-binding proteins PA14_58470 (dppD) and PA14_58490 (dppF)"].
- PAO1 mapping: [PMID:25338022 "The protein sequences from PAO1 are homologous to the following proteins from PA14: DppBCDF (PA4503–PA4506)"]. PA4506 = DppF.
- Evidence: [PMID:25338022 "In order to investigate the substrate profile of the ABC transporter DppBCDF, a deletion mutant of the dppBCDF operon was constructed"]; [PMID:25338022 "Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system"]. No biochemical assay of DppF.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN001952620 | GO:0022857 transmembrane transporter activity | 5 | 106 (40 taxa) | GO:0071916, IDA, PMID:25338022 (PseudoCAP) | E. coli GsiA P75796, SapF P0AAH8, DppF P37313, OppF P77737 | Yes | SOUND | Term right for the ATPase subunit of the Dpp importer; evidence is a PA14 operon-deletion growth phenotype, so IMP not IDA (evidence-code defect). Broad node term suits a mixed peptide/glutathione/putrescine ABC ATPase clade. |

Defects: PSEUDOCAP WRONG_EVIDENCE_CODE IDA->IMP (CONFIRMED, full text). No GO_CENTRAL defect. Actions: 6 ACCEPT, 4 TOO_GENERAL.
