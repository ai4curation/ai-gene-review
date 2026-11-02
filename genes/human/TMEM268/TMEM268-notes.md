# TMEM268 (human, Q5VZI3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of fly CG18507
(M9PBB3). PANTHER PTHR31193 has a single subfamily, SF1 "TRANSMEMBRANE PROTEIN 268",
containing human TMEM268, mouse Tmem268 (Q8R239), bovine TMEM268 (Q5EA48) and fly
CG18507 (interpro/panther/PTHR31193/PTHR31193-entries.csv). No PAINT node exists, and
UniProt reports "PAN-GO; Q5VZI3; 0 GO annotations based on evolutionary models".
No ProtNLM2 file was consulted.

Deep research: `just deep-research-falcon human TMEM268 --fallback perplexity-lite`
failed (Edison auth 403, then perplexity-lite timed out at 600 s); a retry with
`--provider perplexity-lite` also timed out. The review therefore rests on the two
primary papers (both full text cached) and the UniProt record.

### Evidence, by species

Human (experimental):
- Localization: ER and plasma membrane by immunofluorescence in BGC823 cells
  [PMID:30361615 "Immunofluorescence assay demonstrated that the TMEM268 protein was mainly present in the endoplasmic reticulum and plasma membrane"].
- ITGB4 binding: GST pull-down, endogenous co-IP and domain mapping (TMEM268 104-342 to ITGB4 1356-1756)
  [PMID:30361615 "The endogenous co-immunoprecipitation (Co-IP) assay revealed that TMEM268 coprecipitated with ITGB4"].
- ITGB4 stabilization: knockout increases ITGB4 polyubiquitination and proteasomal degradation (MG-132 blocks it) and lowers surface ITGB4
  [PMID:30361615 "Mechanistically, TMEM268 interacts with ITGB4; TMEM268 deletion promotes ITGB4 degradation via the protease pathway."].
- CD11b (ITGAM) binding: HEK293T co-IP and endogenous co-IP in THP-1; binds the CD11b C-terminal tail 1105-1152
  [PMID:38730209 "Similarly, the endogenous Co-IP assay also verified that TMEM268 coprecipitated with CD11b in THP-1 cells"].

Mouse (ortholog, same subfamily):
- Tmem268-/- BMDMs: CD11b degraded faster by the endosomal-lysosomal pathway; reduced phagocyte adhesion and migration; worse CLP sepsis
  [PMID:38730209 "These data suggest that Tmem268 knockout promotes CD11b degradation via the endosomal–lysosomal pathway but not autophagy"].

Fly CG18507: no experimental data. Transfer to the fly would rest on SF1 membership alone.

### Decisions
- IPI protein binding (ITGAM): MODIFY to integrin binding GO:0005178.
- plasma membrane EXP and IEA: ACCEPT.
- NEW: ER membrane (IDA, PMID:30361615), integrin binding to ITGB4 (IPI, PMID:30361615),
  protein stabilization (IMP, PMID:30361615; CD11b part is mouse evidence). The stabilization
  passes the participation test because TMEM268 binds its client integrins directly.
- Not annotated: cell adhesion and migration, tumour growth, cell cycle, cytoskeleton
  organization, antibacterial defense and sepsis outcomes. These are downstream phenotypes
  of losing integrins.
