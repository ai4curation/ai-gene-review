# nuoF notes

- NuoF is the FMN-dependent catalytic input subunit of respiratory complex I;
  it performs the NADH-oxidation half-reaction before electrons enter the
  iron-sulfur relay [file:PSEPK/nuoF/nuoF-deep-research-openscientist.md
  "NuoF's specific contribution is the **NADH‑oxidation half‑reaction**"].

- The source GO:0008137 annotation uses `enables`. This review retains the
  complex-level term but proposes `contributes_to`, while adding GO:0003954 as
  the direct NuoF molecular function.

## 2026-11-02 rework to a full review

Deep-research providers other than the existing OpenScientist file are unavailable
in this environment (no API keys); literature reviewed manually from cached E. coli
publications and the Q88FH3 UniProt record (curated RuleBase function, PIRSR N3
ligands Cys361/364/367/408, NCBIfam TIGR01959, Pfam PF01512/PF10589, PROSITE
PS00644/PS00645). RecName and module-sidecar quotes removed.

- GO:0008137: MODIFY (identical term, qualifier-only change) -> ACCEPT, read as
  a contribution; subunit activity GO:0003954 kept as NEW (ISS from E. coli
  PMID:19061856).
- GO:0010181, GO:0051287, GO:0051539, GO:0045271 accepted on signatures + E. coli
  orthology. GO:1902600 kept as non-core.
- NEW (ISS): GO:0022904, GO:0005886.
- PANTHER: UniProt puts Q88FH3 in PTHR43578:SF3; PANTHER 19.0's own files put the
  E. coli / P. aeruginosa orthologues in PTHR11780:SF10. See the PTHR43578 family
  review.
