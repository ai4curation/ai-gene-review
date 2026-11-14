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

- GO:0015628 IDA PMID:9818381: review; IDA not supported: full text checked, no original secretion data. Same WRONG_EVIDENCE_CODE / CHECK defect as
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
the split, so both T2SS IBDs at this node leak to type IV pilus proteins. Recorded as GO_CENTRAL
WRONG_TERM / CHECK defects on the two IBA rows (the IBAs on XcpV itself are correct), raised to
CONFIRMED by the tree check below, which also reframes where the fault lies.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002446181 | GO:0015627 type II protein secretion system complex | 1 (sole seed) | 12 (9 taxa) in worklist; 49 proteins in current QuickGO | GO:0015627, IDA, PMID:8331069 | SOUND (term for XcpV); seed reference OVER-SPECIFIC; node scope questionable | XcpV is in the tip complex (PMID:19828448, PMID:30346996), but the cited paper shows only membrane localisation and PilD processing (abstract). About 14 of 49 leaves are named PilV/MshD/pilin, so the T2SS complex term is likely over-propagated to type IV pilus minor pilins. |
| PTN002446181 | GO:0015628 protein secretion by the type II secretion system | 1 (sole seed) | 12 (9 taxa) in worklist; 49 proteins in current QuickGO | GO:0015628, IDA, PMID:9818381 | SOUND (term for XcpV); evidence code WRONG; node scope questionable | xcpV mutant loses LasB secretion and is complemented (PMID:30346996). PMID:9818381 is a review, so IDA is invalid; re-key as IMP. Same PilV leakage concern at the node. |

## PANTHER tree check (2026-11-05)

Topology of PTN002446181 fetched with `projects/PSEUDOCAP/panther_tree.py node PTN002446181
--depth 6` and `family PTHR38779 --depth 3`. **PTN002446181 is the root of PTHR38779**: a
SPECIATION node (Eubacteria) with 12 reference-proteome leaves, all PTHR38779:SF2, and three
children.

| Child node | Event | Leaves | Subfamilies | Contents | Verdict |
|---|---|---|---|---|---|
| PTN002446182 | LEAF | 1 | SF2 | *Aquifex aeolicus* ppdD3, "Pilin" | not a T2SS protein |
| PTN002409471 | LEAF | 1 | SF2 | *Thermodesulfovibrio yellowstonii* THEYE_A0597, bare prepilin-type cleavage/methylation domain | not a T2SS protein |
| **PTN002215342** | SPECIATION (Proteobacteria) | 10 | SF2 | *Geobacter* GspI; PTN002215344 (Gammaproteobacteria, 9): *Shewanella* GspI, *Vibrio* EpsI, PTN002215341 (*Xanthomonas* XpsI/XcsI/XcsJ), PTN002446183 (**XcpV Q00516**, PA0680), PTN002215349 (*E. coli* GspI, *Yersinia* YPO0811) | every T2SS-named leaf in the family |

Two corrections to the earlier, name-based reading:

- **There is no GspI/PilV split in this tree.** No PilV or MshD protein is a leaf of PTHR38779's
  reference tree. Checking `node_leaves.tsv` against the tree, the 12 reference leaves are all
  present in the 49-protein QuickGO set (Q00516, Q9I5P5, P45760, P45775, Q74S14, Q8EKC4, Q8P5C1,
  Q8P5C2, P31738, Q74GC2, O67426, B5YJM5); the other 37, PilV/MshD names included (e.g. Q5F9E5
  NGO_0453), are non-reference members grafted into the family by sequence, which the tree cannot
  place. So the leakage is a family-assignment/grafting effect, not evidence that the annotated
  clade mixes two systems.
- **The node is nevertheless one level too high.** Being the family root, the IBD also covers the
  two deep generic prepilin branches, while every T2SS-named leaf sits in PTN002215342. That is a
  real, checkable node-placement error with an unambiguous target.

Verdict for both defects (GO:0015627 and GO:0015628): **CONFIRMED**, raised from SUSPECTED, with the
request changed from "move to a node confined to GspI proteins / add NOT for the PilV clade" to
"move both IBDs to **PTN002215342**". If grafted PilV/MshD members still receive the terms after the
move, the next thing to check is their PTHR38779:SF2 assignment, not the node. The XcpV IBA rows
themselves stay ACCEPT: XcpV is inside PTN002215342 and the terms are right for it.
