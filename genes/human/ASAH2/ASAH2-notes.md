# ASAH2 notes

## 2026-10-24 ORGANELLES batch 2 (mitochondrion rows)

- Rows: GO:0005739 IDA (PMID:10781606) and IEA (GO_REF:0000044, SL-0173). Both changed from UNDECIDED to MARK_AS_OVER_ANNOTATED, consistently.
- The IEA maps UniProt's "Mitochondrion {ECO:0000269|PubMed:10781606}". The same entry cautions [file:human/ASAH2/ASAH2-uniprot.txt "The localization to the mitochondrion could not be confirmed (PubMed:15845354)."].
- The 2000 study used an N-terminal GFP fusion [PMID:10781606 "the green fluorescent protein-ceramidase fusion protein presented a mitochondrial localization pattern"]. The cached abstract of the follow-up states that this construct was N-terminally truncated, and that full-length protein goes to the plasma membrane [PMID:15845354 "We found that the putative full-length human neutral ceramidase was transported to plasma membranes, but not to mitochondria, possibly via a classical ER/Golgi pathway"] [PMID:15845354 "The N-terminal-truncated mutant, previously reported as a human mitochondrial ceramidase, was also weakly expressed in HEK293 cells but mainly released into the medium"].
- ASAH2 is a type II signal-anchor protein (UniProt FT TRANSMEM 13..33, "Signal-anchor for type II membrane protein"). Its catalytic domain is lumenal or extracellular.
- Decision: the organelle claim is not supported for the native human protein, so both rows are MARK_AS_OVER_ANNOTATED. REMOVE was not used for two reasons: the IDA full text was not read, and UniProt notes reported mitochondrial pools for the mouse and rat orthologs. No sub-compartment is proposed. Added PMID:15845354 to references.
- Upstream: UniProt could drop SL-0173 for Q9NR71, or keep it only under the caution.
- Outcome: root; rows to MARK_AS_OVER_ANNOTATED.
