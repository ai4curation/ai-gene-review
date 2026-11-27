# thiD (PP_4782, Q88DP2) curation notes

## Sources

Deep-research providers were not available in this session; no
`-deep-research-<provider>.md` file was generated. Notes rest on the UniProt
record, cached publications and the repository's PTHR20858 family review. No
KT2440-specific publication on thiD was found in the cache (searched cached
titles for thiD, hydroxymethylpyrimidine/phosphomethylpyrimidine kinase,
thiamin(e) biosynthesis and Pseudomonas putida KT2440).

## Evidence

- Family: HMP/HMP-P kinase domain and ThiD/THI20 subfamily
  [file:PSEPK/thiD/thiD-uniprot.txt "InterPro; IPR004399; HMP/HMP-P_kinase_dom.";
  "PANTHER; PTHR20858:SF17; HYDROXYMETHYLPYRIMIDINE_PHOSPHOMETHYLPYRIMIDINE KINASE THI20-RELATED; 1."].
- Subfamily member biochemistry: Thi20 ThiD-like domain has HMP and HMP-P kinase
  activity [PMID:15967475 "incubation of Thi20 with HMP ... reveals that it has HMP
  kinase and HMP-P ... kinase activity"]; Thi20/Thi21 also HMP kinase
  [PMID:15614489 "we demonstrate that both Thi20p and Thi21p proteins also have HMP
  kinase activity."].
- Bacterial genetics: E. coli auxotrophs lacking phosphomethylpyrimidine kinase
  [PMID:6284709 "thiamine auxotrophs that had lost the enzymatic activity of either
  phosphomethylpyrimidine kinase or thiamine phosphate pyrophosphorylase"].
- Pathway: HMP-PP + thiazole-P -> TMP -> TPP [PMID:8432721].
- Genome context: PP_4782 (thiD) is adjacent to PP_4783 (thiE).
- UniProt protein name/EC and pathway lines are ARBA-derived (unvetted) and were not
  used as support. The E. coli ThiD bifunctionality paper (Mizote et al. 1999) is not
  cached and was not cited.

## Decisions (2026-11-12)

- GO:0003824 catalytic activity (ARBA): MODIFY -> GO:0008972 + GO:0008902.
- GO:0005829 cytosol (TreeGrafter): ACCEPT.
- GO:0008972 HMP-P kinase: ACCEPT, core.
- GO:0008902 HMP kinase: ACCEPT (salvage role; second core function).
- GO:0009228 / GO:0009229: ACCEPT both. GO:0009229 is not a descendant of GO:0009228
  (checked in the local GO sqlite: its parents are GO:0042357, GO:0042724, GO:0090407),
  so 0009228 is not "general" relative to 0009229; consistent with THI20/THI6.
