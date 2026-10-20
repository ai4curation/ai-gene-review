# S0EDH7 (FFUJ_06423) notes

## Re-review 2026-10-01 (GOA refresh)

- Current GOA snapshot has no rows for S0EDH7; nothing to review or retire.
- core_functions audit: the previous core function asserted GO:0004672 protein kinase
  activity + GO:0006468 protein phosphorylation and cited the ProtNLM predictions review
  with a quote ("both assessed as COR") that is not in that file - the predictions
  review actually assesses both ProtNLM predictions as UNC. Only fold-level kinase-like
  signatures exist (IPR011009, Gene3D 1.10.510.10, SSF56112; no Pfam-level kinase
  family), and the PKL fold includes small-molecule kinases (APH/choline kinase-like).
  Broadened the MF to GO:0016301 kinase activity, dropped the protein phosphorylation
  BP, added a knowledge gap, replaced the non-verbatim quote, and reworded the
  description accordingly.
