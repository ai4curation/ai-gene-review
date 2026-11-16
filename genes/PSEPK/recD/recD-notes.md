# recD curation notes

- Q88DZ6 is the canonical RecBCD RecD subunit in the contiguous KT2440 `recD-recB-recC` locus. Its target record explicitly assigns ssDNA-dependent ATPase and 5-prime-to-3-prime helicase activity [UniProtKB:Q88DZ6, "ssDNA-dependent ATPase and 5'-3' helicase activity"].
- Generic helicase activity and single-stranded DNA helicase activity are true but non-core views rather than errors; GO:0043139 captures the defining motor polarity. Exonuclease V activity is a contribution, not an `enables` activity, because RecD stimulates the RecBC nuclease while RecB contains the nuclease active site [UniProtKB:Q88DZ6, "assembled RecBC greatly stimulates nuclease activity and augments holoenzyme processivity"].
- P. syringae recD mutants are DNA-damage sensitive, unlike E. coli recD mutants, and ATP-dependent RecD function is required in that pseudomonad [PMID:20195537, "sensitive to DNA-damaging agents and fail to grow at 4 degrees C"; "the ATP-dependent functions of both RecB and RecD are essential"]. This is comparative evidence and is not represented as a direct KT2440 experiment.
- PTHR43788:SF6 includes canonical RecD and standalone RecD2/HelB proteins. The module therefore uses the RecBCD-specific NCBIfam:TIGR01447 selector and requires cognate RecB-RecC genomic or complex context.

## 2026-11-09 rework (Claude, AI-assisted)

- Correct-but-general rows now use MODIFY with a specific replacement the gene already
  carries (or ssDNA binding for DNA binding): helicase activity and ATP hydrolysis ->
  GO:0043139; double-strand break repair and DNA recombination -> GO:0000724; DNA
  binding -> GO:0003697. Earlier KEEP_AS_NON_CORE choices on these rows conflicted with
  the "correct but general is MODIFY" rule.
- GO:0008854 exodeoxyribonuclease V activity: relation-only MODIFY recording that RecD
  contributes_to rather than enables the holoenzyme reaction; WRONG_QUALIFIER source
  defect filed against the InterPro2GO IPR006344 mapping. Same decision on E. coli RecD.
- GO:0017116 (TreeGrafter, graft node PTN002465246 under PTN008452915) accepted: its
  definition (ATP hydrolysis in the presence of ssDNA driving unwinding) fits RecD, and
  the IBD is seeded by E. coli RecD and human HELB (Q8NG08, which is HELB, not PIF1).
- Q88DZ6 is not a leaf of the cached PTHR43788 tree, so this entry has no IBA rows; the
  HELB-seeded process IBDs at PTN008452915 (GO:0006261, GO:1903775, GO:2000042) that
  reach E. coli RecD do not appear here.
- P. syringae RecD is required for recombination and repair
  [PMID:20195537 "More importantly, we now demonstrate that an inactive RecDK229Q subunit (i.e., RecBCDK229Q enzyme) or an inactive RecB subunit (i.e., RecBK28QCD) also makes the P. syringae RecBCD enzyme inefficient in homologous recombination (Table 3)."].

## 2026-11-10 PR #6235 follow-up (Claude, AI-assisted)

- GO:0008854 now follows projects/SDH_GP2TERM_CONTRIBUTES_TO.md. The GOA `enables` IEA row is MODIFY with the same term, and a paired NEW row (IDA, PMID:2559208) carries `qualifier: contributes_to`. The activity was measured on the cloned P. putida RecBCD-like enzyme. The subunit-level contributes_to relation is inferred from E. coli reconstitution (PMID:1618858).
