# Mtmr12 (Q5FVM6, rat Swiss-Prot canonical) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output and prediction files were not opened or used.

**Setup.** Folder created with `just fetch-gene rat Q5FVM6 --alias Mtmr12__Q5FVM6` (9 GOA rows, all
cellular component). `just deep-research-falcon rat Mtmr12__Q5FVM6 --fallback perplexity-lite`
failed (falcon and the perplexity-lite fallback both exited with an error; no deep-research file was
written). Review based on the cached full texts of PMID:23818870 and PMID:12847286, the abstract of
PMID:11504939, the UniProt record, the PTHR10807 PAINT file, and QuickGO queries.

**Identity and evolutionary grounding.** Q5FVM6 (748 aa, cDNA BC089876) is in PANTHER
PTHR10807:SF37 with human Q9C0I1 and mouse Q80TA6 (one-to-one orthologs). Its CX5R region is
EENASDL instead of MTM1's CSDGWDR, so the catalytic Cys and Arg are absent
(`genes/rat/Mtmr12/Mtmr12-bioinformatics/RESULTS-rereview.md`). PAINT: cytoplasm from PTN000743854
and membrane from PTN000086845. PTN000086845 also carries GO:0004438 PI3P phosphatase activity and
GO:0046856, which SF37 members do not receive; I treat that omission as deliberate and transfer no
catalytic terms.

**What is experimental, and in which species** (none in rat):
- Human: 3-PAP recombinant protein catalytically inactive [PMID:11504939]; coprecipitates MTM1 and
  MTMR2 (not MTMR6), is cytosolic/punctate vesicles, relocates MTM1 to cytoplasm (COS-7, K562)
  [PMID:12847286]; direct GST pull-down with MTM1 [PMID:23818870].
- Mouse: endogenous co-IP with MTM1 from tibialis anterior; colocalization at triads, partly with
  RyR1, not alpha-actinin; MTMR12 reduced in Mtm1-KO muscle; MTMR12 knockdown in C2C12 lowers MTM1
  [PMID:23818870].
- Zebrafish: morphants have lower MTM1 protein and a CNM-like muscle phenotype [PMID:23818870].
  The phenotypes are not annotated as process participation.
- Rat: only large-scale phosphoproteomics (Ser602, PMID:22673903 in UniProt); no functional work.

**Row decisions.**
- cytoplasm x4 (IBA, IEA, ISO, ISS): ACCEPT.
- membrane IBA: KEEP_AS_NON_CORE; peripheral, indirect association; no specific membrane shown.
- sarcoplasmic reticulum x3 (IEA, ISO from MGI EXP, ISS): ACCEPT.
- sarcomere IEA: MODIFY -> GO:0030314 junctional membrane complex (triad junction), since the mouse
  data say "restricted to triads" with no Z-line colocalization. GO:0030314 is not under sarcomere
  (OLS ancestors: sarcoplasm, protein-containing complex), so lateral correction. It is not in the
  location enum for core_functions, so it is only in the MODIFY replacement.
- NEW GO:0019902 phosphatase binding and NEW GO:0050821 protein stabilization (ISS, from
  PMID:23818870). Comparator check (QuickGO 2026-10-21): human MTMR9 (Q96QG7), the other inactive
  adapter subunit, carries GO:0019903 (IPI, IBA) and GO:0050821 (IDA). Human MTMR12 has only
  GO:0005515 IPI, GO:0019211 TAS, and CC terms, so the absence on MTMR12 is a missing informative
  annotation rather than a convention. Participation: MTMR12 is the partner whose complex formation
  protects MTM1, not a substrate. No PAINT phosphatase-binding node covers SF37, but no MTMR12 has an
  experimental phosphatase-binding annotation that could have seeded one.
- Not proposed: GO:0019211 phosphatase activator activity (PMID:23818870 argues against an effect on
  enzymatic activity); phosphatidylinositol dephosphorylation (catalysis is MTM1's).

**Other literature noted, not used.** The sibling folder's falcon report mentions a 2024 Hepatology
study (DOI 10.1097/HEP.0000000000000865) linking MTMR12 variants to alpha1-antitrypsin Z liver
disease as a modifier; human variant association, not used for annotation.
