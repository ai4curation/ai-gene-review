# xcpW (PA3098, Q00517) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE xcpW`; accession Q00517 matches the worklist (rank 47,
PA3098). UniProt synonym pddD. No deep-research provider was used; manual notes from cached
publications, PubMed and the UniProt record. PMID:9282737, PMID:21245534 and PMID:1309616 were
cached with `ai-gene-review fetch-pmid` (abstract only). PMID:8331069 has a PMC id
(PMC204877) but the PubMed MCP full-text call returned an empty body.

### What XcpW is

- GspJ-family minor pseudopilin (UniProt "Belongs to the GSP J family"; NCBIfam TIGR01711,
  InterPro IPR010055, Pfam PF11612 T2SSJ, PANTHER PTHR39583:SF2).
- Prepilin-like precursor processed and N-methylated by PilD; inner membrane before and after
  processing [PMID:8331069 "Sequence analysis of XcpT-W has shown that these proteins, like mature
  pilin, contain N-methylphenylalanine as the N-terminal amino acid"; "the precursor forms of
  XcpT-W are located predominantly in the bacterial inner membrane, and their localization is not
  altered after PilD-mediated removal of the leader sequence"].
- Required for excretion: the four pdd genes (= xcpT-W) [PMID:1309616 "Site-specific mutations
  within these genes have shown that they are required for protein excretion"].
- Cross-links with PilA and XcpT [PMID:9282737 "XcpW and XcpU can also be crosslinked to form
  dimeric complexes with PilA"; "When expression of XcpT is increased, its homodimers, as well as
  XcpT/XcpW heterodimers, can be detected"].
- Tip complex XcpU-V-W-X; XcpW recruits XcpU [PMID:19828448 "Then the ternary complex recruits
  XcpU(H) through a direct interaction with XcpW(J)"].
- Structure: type IVa pilin fold; disordered C-terminal 31 residues dispensable for secretion
  [PMID:21245534 "Deletion of this unstructured region of XcpW(J) did not prevent type II secretion
  in vivo"].
- XcpVW is the core of the tip; xcpW mutant has reduced LasB secretion, complemented
  [PMID:30346996 "The absence of either XcpV or -W resulted in the non-functional T2SS"; "The
  supernatant of the xcpW mutant also had less LasB activity than the mutants of xcpU and -X"].

### PseudoCAP rows

- GO:0015628 IDA PMID:9818381: the paper is a review (FEMS Microbiol Rev 1998, PubMed type Review);
  IDA invalid. Same WRONG_EVIDENCE_CODE / CHECK defect as on xcpX and xcpS. Term correct; primary
  IMP evidence: PMID:30346996, PMID:1309616.
- GO:0015627 IDA PMID:8331069: the paper is primary research (not a review), but its abstract
  reports leader cleavage, N-methylation and inner-membrane fractionation of XcpT-W. That supports
  plasma membrane (UniProt already has EXP from it) but does not assay T2SS complex membership; the
  abstract presupposes it ("Four components of the apparatus of extracellular protein secretion").
  Full text not obtainable. Row accepted (term true; curator saw the full text); recorded a
  SUSPECTED WRONG_REFERENCE / CHECK defect suggesting re-keying to PMID:19828448.

### PAINT node identity

The worklist and `.cache/paint/seed_support.json` place the XcpW seeds at PTN002446812 (terms
GO:0015628, GO:0015627, and GO:0005886 from the UniProt EXP). Current GOA carries only a
GO:0015628 IBA on XcpW, from PTN002218419 with XcpW as WITH/FROM, and no GO:0015627 IBA. QuickGO
has no annotations citing PTN002446812, while PTN002218419 has 618 leaf proteins for GO:0015628,
542 GspJ/T2SS-named (`genes/PSEAE/xcpV/xcpV-bioinformatics/RESULTS.md`). Likely a PANTHER
version renumbering; not verified. The PAINT file for PTHR39583 is not cached in
`interpro/panther/`.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002446812 (PTN002218419 in current GOA) | GO:0015628 protein secretion by the type II secretion system | 1 (sole seed) | 12 (7 taxa) in worklist; 618 proteins under PTN002218419 in QuickGO | GO:0015628, IDA, PMID:9818381 | SOUND (term); evidence code WRONG | xcpW mutant loses secretion and is complemented (PMID:30346996); pdd mutants (PMID:1309616). PMID:9818381 is a review, so IDA is invalid; re-key as IMP. Node leaves are GspJ proteins; term suits the clade. |
| PTN002446812 | GO:0015627 type II protein secretion system complex | 1 (sole seed) | 12 (7 taxa) in worklist; none found in current QuickGO | GO:0015627, IDA, PMID:8331069 | SOUND (term); seed reference OVER-SPECIFIC | The cited paper shows inner-membrane localisation and PilD processing, not complex membership (abstract; full text unavailable). XcpW is in the tip complex (PMID:19828448, PMID:30346996), so the claim and the node term hold for GspJ; better reference PMID:19828448. |
