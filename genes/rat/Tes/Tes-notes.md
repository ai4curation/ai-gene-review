# Tes (rat, Q2LAP6) review notes

- 2026-10-28: `just fetch-gene rat Tes` resolved Q2LAP6 (TES_RAT, RGD:1566346, GeneID 500040); 13 GOA rows,
  all IBA/IEA/ISS/ISO (no rat experimental rows). No deep research run (no API keys); see
  `Tes-deep-research-manual.md` for the literature synthesis.
- Key rat paper PMID:21278383 (full text): Tes-Arp7A-Mena complex co-IP from rat testis, and localisation
  to the subacrosomal layer (acroplaxome) of round spermatids [PMID:21278383 "Arp7A, Tes, and Mena are complexed to each other in rat testes extracts"].
  GO has no acroplaxome CC term (searched `acrosom` in GO); not proposed as NEW.
- Decisions:
  - focal adhesion (IEA, ISO): ACCEPT, core location [PMID:12571287; PMID:12695497].
  - cytoplasm (IBA, IEA, ISS, ISO) and cytosol (ISO): KEEP_AS_NON_CORE; diffuse pool, protein shuttles among
    cytosol, stress fibres and FAs.
  - zinc ion binding (IEA, ISS, ISO): KEEP_AS_NON_CORE; structural Zn in LIM domains [PMID:21278383].
  - negative regulation of cell population proliferation (ISS, ISO): KEEP_AS_NON_CORE; overexpression growth
    suppression in tumour lines [PMID:11420696; PMID:12695497].
  - protein-containing complex (ISO): KEEP_AS_NON_CORE; rat co-IP supports it directly, no more specific GO
    complex term exists for Arp7A-Tes-Mena.
  - NEW: cytoskeletal protein binding (GO:0008092, IPI PMID:21278383) as the informative MF for the
    LIM-domain scaffold (Mena EVH1, zyxin, Arp7A). No NEW BP proposed (spreading/migration/stress fibre
    data are overexpression/knockdown phenotypes in non-rat cells).
