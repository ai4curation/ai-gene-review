# bir-1 review notes

## 2026-10-28 session

- `just fetch-gene worm bir-1` resolved G5EFA2 (Swiss-Prot, WormBase WBGene00000249, GeneID
  179597), 30 GOA rows. First attempt hit a UniProt 429 rate limit; retried successfully.
- Cached and read: PMID:12707312 (full text), PMID:12682297 (full text), PMID:10983970
  (abstract only), plus PMID:10209096 and PMID:17116281 (abstract only, fetched for the
  apoptosis and transcription questions). PMID:11402065 (ICP-1/CeINCENP localization, full
  text, already cached) used for the holocentric kinetochore point.
- Kept decisions consistent with the existing csc-1 and icp-1 reviews (same CPC, same
  ComplexPortal NAS rows): mitotic cell cycle -> sister chromatid segregation + cytokinesis;
  SAC and sister-chromatid-separation NAS rows marked over-annotated; spindle midzone rows
  refined to mitotic/meiotic spindle midzone; condensed chromosome refined to condensed
  nuclear chromosome.
- negative regulation of apoptotic process (IBA from Survivin/Deterin) removed: directly
  contradicted for BIR-1 [PMID:10209096 "inhibition of bir-1 expression did not increase cell
  death"]. Recorded as a missing-NOT source defect for PAINT.
- Post-embryonic phenotypes (Egl, Dpy, DTC migration) from larval RNAi [PMID:12682297] are
  pleiotropic downstream effects; marked over-annotated. Transcription (RNAPII) IDA rests on a
  heterologous MCF-7 luciferase reporter: kept as non-core.
- No molecular_function in core_functions: BIR-1 is a targeting subunit with no measured
  activity of its own beyond zinc-dependent binding to CSC-1 (protein binding is not
  informative). H3T3ph-binding by analogy with Survivin is not shown in C. elegans; raised as a
  question.
