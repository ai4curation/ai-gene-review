# PRAME curation notes

Deep research (falcon/perplexity-lite) unavailable; notes from UniProt P78395 and cached papers.

- CRL2 substrate receptor [PMID:21822215 "identified PRAME as a substrate recognition subunit of a Cullin2-based E3 ubiquitin ligase"];
  Sec C-end degron QC of truncated selenoproteins [PMID:26138980].
- Chromatin at NFY promoters/enhancers (ChIP-seq, PMID:21822215).
- RAR repressor via EZH2/Polycomb [PMID:16179254 "PRAME binds to RAR in the presence of RA, preventing ligand-induced receptor activation"].
- Golgi relocalization after PAMP/IFNg in HL60/U937 (PMID:23460923); "PRAME is an intracellular protein found in both the nuclear and cytoplasmic compartments".
- Membrane antigen claim (PMID:16620968, CLL immunostaining) and HPA PM IF - inconsistent with topology (no SP/TM).

Localization conclusion: intracellular (nucleus/chromatin and cytoplasm; Golgi on stimulation). Plasma
membrane annotations marked over-annotated; no extracellular exposure - targetable only as HLA-peptide.

## 2026-11-18 ORGANELLES Golgi batch 3 (Golgi apparatus rows)

- Both GO:0005794 rows (EXP PMID:23460923 and the IEA SubCell mapping of the same curated item) stay KEEP_AS_NON_CORE; reasons rewritten to record the check.
- PMID:23460923 (full text cached, PMC3584020): endogenous PRAME forms polarised cytoplasmic foci in HL60 and U937 cells after LPS or PGN with IFN-gamma, and co-stains with the 58K Golgi marker [PMID:23460923 "staining of HL60 cells with the 58K Golgi marker confirmed that these structures appear to be linked to the Golgi network"]. Endogenous protein in its native cells with a marker, so the root holds; the pool is stimulus-induced and no PRAME activity is shown there ("functional consequences of the association of PRAME with the Golgi remains to be determined"), so non-core.
- No sub-compartment row: one marker line, one condition; the authors' trans-Golgi suggestion rests on the polarised pattern only.
