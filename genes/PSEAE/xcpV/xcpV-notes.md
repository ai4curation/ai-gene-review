# xcpV (PA3099, Q00516) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE xcpV`; accession Q00516 matches the worklist (rank 51,
PA3099). UniProt synonym pddC. No deep-research provider was used; manual notes from cached
publications, PubMed and the UniProt record. PMID:8331069 full text could not be obtained (PMC204877
returns an empty body through the PubMed MCP).

### What XcpV is

- GspI-family minor pseudopilin (UniProt "Belongs to the GSP I family"; NCBIfam TIGR01707,
  InterPro IPR010052/IPR003413, Pfam PF02501 T2SSI, PANTHER PTHR38779:SF2). 129 aa, leader 1..6,
  TM 7..27.
- PilD-processed and N-methylated; inner membrane [PMID:8331069 "Sequence analysis of XcpT-W has
  shown that these proteins, like mature pilin, contain N-methylphenylalanine as the N-terminal
  amino acid"; "the precursor forms of XcpT-W are located predominantly in the bacterial inner
  membrane"].
- Required for excretion (pddC) [PMID:1309616 "Site-specific mutations within these genes have
  shown that they are required for protein excretion"].
- Complexes with His-XcpT [PMID:9282737 "an oligohistidine-tagged XcpT was shown to form
  stoichiometric complexes with PilA, and with XcpT, U, V and W"].
- Nucleator of the tip complex [PMID:19828448 "We propose a model in which XcpV(I) is the nucleator
  that first binds XcpX(K) and XcpW(J) at different sites"].
- XcpVW core; xcpV mutant has the lowest LasB secretion and is complemented [PMID:30346996 "The
  absence of either XcpV or -W resulted in the non-functional T2SS"; "The supernatant of the xcpV
  mutant, containing secreted proteins, displayed the lowest LasB activity, suggesting that the
  secretion of LasB was significantly compromised."].

### PseudoCAP rows

- GO:0015628 IDA PMID:9818381: review; IDA invalid. Same WRONG_EVIDENCE_CODE / CHECK defect as
  xcpX, xcpS, xcpW. Term correct; primary IMP: PMID:30346996, PMID:1309616.
- GO:0015627 IDA PMID:8331069: primary paper, but the abstract shows processing, methylation and
  inner-membrane fractionation only, not complex membership. Accepted (term true), SUSPECTED
  WRONG_REFERENCE / CHECK defect suggesting PMID:19828448. Same treatment as xcpW.

### PAINT node breadth (bioinformatics)

`xcpV-bioinformatics/node_leaves.py` lists the QuickGO leaves of the seed nodes for all three Xcp
genes reviewed in this session (xcpS, xcpW, xcpV) and classifies them by name; see
`xcpV-bioinformatics/RESULTS.md`. For PTN002446181 (GO:0015627): 49 proteins, 14 T2SS-named,
14 named PilV/MshD/pilin (including N. gonorrhoeae PilV NGO_0453, a type IV pilus minor pilin), 21
generic prepilin-domain names. GspI and PilV are homologous minor pilins; the node appears to span
the split, so both T2SS IBDs at this node leak to type IV pilus proteins. Recorded as SUSPECTED
GO_CENTRAL WRONG_TERM / CHECK defects on the two IBA rows (the IBAs on XcpV itself are correct).
Name-based only; I did not inspect the tree topology.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002446181 | GO:0015627 type II protein secretion system complex | 1 (sole seed) | 12 (9 taxa) in worklist; 49 proteins in current QuickGO | GO:0015627, IDA, PMID:8331069 | SOUND (term for XcpV); seed reference OVER-SPECIFIC; node scope questionable | XcpV is in the tip complex (PMID:19828448, PMID:30346996), but the cited paper shows only membrane localisation and PilD processing (abstract). About 14 of 49 leaves are named PilV/MshD/pilin, so the T2SS complex term is likely over-propagated to type IV pilus minor pilins. |
| PTN002446181 | GO:0015628 protein secretion by the type II secretion system | 1 (sole seed) | 12 (9 taxa) in worklist; 49 proteins in current QuickGO | GO:0015628, IDA, PMID:9818381 | SOUND (term for XcpV); evidence code WRONG; node scope questionable | xcpV mutant loses LasB secretion and is complemented (PMID:30346996). PMID:9818381 is a review, so IDA is invalid; re-key as IMP. Same PilV leakage concern at the node. |
