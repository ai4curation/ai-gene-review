# ruvC (E. coli K-12, P0A814) curation notes

Reviewed by Claude (AI-assisted) as the E. coli exemplar of the RuvC step of `modules/bacterial_ruvabc_holliday_junction_processing.yaml`.

- Provider deep research was not run (no provider API keys in this session).
- PMID:36000732 is a D. radiodurans RuvC paper, but its full text assays E. coli RuvC as the control [PMID:36000732, "Both DrRuvC and EcRuvC exhibited HJR activity over this substrate"], so the EXP row is valid.
- Nucleic acid binding (IEA) is modified to GO:0000400: RuvC forms specific junction complexes without metal [PMID:8195150, "RuvC efficiently forms specific complexes with four-way junctions in the absence of the cations"].
- Replication fork reversal (EXP, acts_upstream_of_or_within) is non-core: RuvC cleaves the reversed-fork junction rather than reversing the fork.
