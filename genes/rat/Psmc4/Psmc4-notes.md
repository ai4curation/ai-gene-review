# Psmc4 (rat) review notes

## Session 2026-10-28

- Fetched with `just fetch-gene rat Psmc4`; UniProt Q63570 (PRS6B_RAT) confirmed; 25 GOA rows.
- No deep-research API; literature summary in `Psmc4-deep-research-manual.md`.
- Psmc4 = Rpt3 = TBP7 = S6b. Base AAA ATPase of the 19S regulatory particle.
  [PMID:8607789 "rat TBP1, TBP7, MSS1, S4, and SUG1"]
- PMID:18986984 (full text): rat evidence is endogenous Rpt3 immunostaining at Htt
  inclusions in rat hippocampal neurons; the gradient/APIS work is in human 293T.
  [PMID:18986984 "Rpt4 and Rpt3 co-localize with poly(Q) inclusions."]
- PMID:37228199 abstract-only; free 19S near synapses, DUB-dependent AMPAR effects.
  Synaptic vesicle and AMPAR-regulation rows left UNDECIDED (cannot verify; the DUB
  activity is not a base-ATPase activity).
- Decisions on generality: proteasome complex / proteasome accessory complex rows
  MODIFY to base subcomplex (GO:0008540, already carried by IBA); cytoplasm -> cytosol,
  nucleus -> nucleoplasm (both already carried by ISO; nucleus is not covered by the
  root-organelle policy); proteasomal protein catabolic process -> proteasome-mediated
  ubiquitin-dependent protein catabolic process (already carried by IBA).
- GO:0036402 proteasome-activating activity now sits under polypeptide conformation
  isomerase activity (unfoldase), not under GO:0016887, so the ATP hydrolysis rows are not
  entailed by it and are accepted separately.
- Blastocyst development (ISO from mouse KO, PMID:10945464): necessity phenotype; kept
  as non-core with the acts_upstream_of_or_within qualifier. No NEW process terms.
