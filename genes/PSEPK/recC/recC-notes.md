# recC curation notes

- Q88DZ4 is the RecC subunit of the contiguous KT2440 `recD-recB-recC` locus. The target UniProt record assigns DNA binding, RecB-processivity stimulation, and signal recognition to RecC, while RecB and RecD provide the helicase motors [UniProtKB:Q88DZ4, "All subunits contribute to DNA-binding"; "RecC stimulates the ATPase and processivity of the RecB helicase"].
- The transferred ATP-binding and DNA-catalytic annotations were removed because the target record provides neither a nucleotide-binding site nor an intrinsic catalytic reaction for RecC. This is an explicit override of the transferred ATP-binding keyword, not an inference that every non-ATPase is unable to bind ATP.
- Pseudomonas RecBCD-like clones restore recombination and ATP-dependent nuclease activity but do not activate E. coli Chi [PMID:2559208, "proficiency and ATP-dependent nuclease activity, but neither Chi hotspot activity nor Chi-dependent DNA cleavage"]. The corresponding KT2440 regulatory signal is therefore left unresolved.
- P. syringae genetics is used as comparative pseudomonad evidence, not as a KT2440 experiment; null mutations in recC, recB, or recD cause UV/mitomycin-C sensitivity [PMID:20195537, "syringae, lead to growth inhibition at low temperature, and sensitivity to UV and mitomycin C"].

## 2026-11-09 re-review (Claude, AI-assisted)

- Brought into line with the E. coli RecC review (genes/ECOLI/recC). Correct-but-general terms are now MODIFY: `DNA binding` -> `DNA end binding` (GO:0045027), `DNA recombination` -> `double-strand break repair via homologous recombination` (GO:0000724, already carried) and `homologous recombination` (GO:0035825).
- `exodeoxyribonuclease V activity` changed from MARK_AS_OVER_ANNOTATED to a contribution (encoding superseded on 2026-11-10, see below) (RecC is required for the holoenzyme activity but lacks the RecB nuclease site); the InterPro2GO `enables` qualifier is recorded as a WRONG_QUALIFIER source defect.
- `DNA helicase activity` and `catalytic activity, acting on DNA` changed from REMOVE to MARK_AS_OVER_ANNOTATED: the holoenzyme claims are real, RecC only contributes. `ATP binding` stays REMOVE, now backed by a Walker A scan showing no motif in Q88DZ4 while KT2440 RecB (Q88DZ5, residue 21) and RecD (Q88DZ6, residue 221) both have one [file:analysis/module_audits/bacterial_recbcd_end_resection/WALKER_A_RESULTS.md].
- The HAMAP-derived UniProt FUNCTION sentence that RecC "recognizes the wild-type Chi sequence" is flagged as a source defect on the UniProt reference: Pseudomonas RecBCD does not act at E. coli Chi [PMID:2559208 "neither Chi hotspot activity nor Chi-dependent DNA cleavage"].

## 2026-11-10 PR #6235 follow-up (Claude, AI-assisted)

- `exodeoxyribonuclease V activity` (GO:0008854) now follows projects/SDH_GP2TERM_CONTRIBUTES_TO.md. The GOA `enables` IEA row is MODIFY with the same term, and a paired NEW row (IDA, PMID:2559208) carries `qualifier: contributes_to`. The InterPro2GO WRONG_QUALIFIER source defect is now CONFIRMED.
- The Walker A scan moved to `analysis/module_audits/bacterial_recbcd_end_resection/` (WALKER_A_RESULTS.md, walker_a_scan.py), because it covers both organisms.
