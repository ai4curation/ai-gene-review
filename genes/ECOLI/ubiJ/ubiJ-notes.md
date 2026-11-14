# ubiJ (P0ADP7, E. coli K-12) review notes

## Sources
- No deep-research provider output exists (provider API keys unavailable in this session); built from the
  UniProt record, cached abstracts and the PTHR38693 PAINT file.
- Aussel et al. 2014 (PMID:24142253, abstract), Loiseau et al. 2017 (PMID:28559279, abstract), Hajj Chehade
  et al. 2019 (PMID:30686758, abstract only, not open access), crosslinking MS (PMID:34117231, full text).

## Findings
- yigP renamed ubiJ, required for aerobic Q8 synthesis [PMID:24142253 "Under aerobic conditions, an ubiJ
  mutant was found to be impaired for Q8 biosynthesis and for growth in rich medium but did not present any
  defect anaerobically."]
- C-terminal 50 aa suffice for complementation [PMID:24142253 "the C-terminal 50 amino acids, predicted to
  interact with lipids, were sufficient to restore Q8 biosynthesis and growth of the ubiJ mutant"].
- SCP2 domain binds UQ intermediates [PMID:30686758 "The SCP2 domain of UbiJ forms an extended hydrophobic
  cavity that binds UQ intermediates inside the 1-MDa Ubi complex."]

## Decisions
- Three bare protein-binding IPI rows removed (policy); complex membership GO:0110142 accepted.
- Cytoplasm EXP/IEA MODIFY to cytosol, matching ubiK.
- NEW GO:0019840 isoprenoid binding (IDA, PMID:30686758). Comparator: human COQ9, the lipid-presenting CoQ
  synthome factor, carries GO:0019840 by IDA. Suggest the module UbiJ annoton add this function (it currently
  has only a process).
