# cyk-4 review notes

- 2026-10-28: Created review of Q9XUS9 (fetch-gene resolved correctly; 31 GOA rows).
- Literature done manually (see cyk-4-deep-research-manual.md); no deep-research provider run.
- Key decisions:
  - Bare protein binding with ZEN-4 (two rows) -> MODIFY to kinesin binding (GO:0019894)
    [PMID:11782313 "The N terminus of CYK-4 binds the central region of ZEN-4, including the neck linker."].
  - Protein binding with ECT-2 -> REMOVE; GEF activator activity (GO:0160124) not justified because
    in vitro stimulation was not detected [PMID:26252513].
  - Diacylglycerol binding IEA -> MARK_AS_OVER_ANNOTATED; the RacGAP1 C1 domain is atypical and binds
    phosphoinositides in human [PMID:23235882].
  - mitotic sister chromatid segregation (LEM-3 paper) -> MARK_AS_OVER_ANNOTATED; indirect via
    LEM-3 midbody recruitment [PMID:29463814].
  - spindle -> MODIFY spindle midzone; spindle midzone assembly -> MODIFY mitotic version;
    signal transduction -> MODIFY Rho protein signal transduction.
- No NEW annotations. Considered microtubule bundle formation (GO:0001578) but centralspindlin
  bundling is already captured by mitotic spindle midzone assembly; not added.
- PMID:17848508 and PMID:11782313 are abstract-only; deferred to curators.
