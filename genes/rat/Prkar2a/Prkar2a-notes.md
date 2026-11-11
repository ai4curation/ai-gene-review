# Prkar2a (rat) review notes

## 2026-10-28 session

- Fetched with `just fetch-gene rat Prkar2a`; UniProt P12368 (KAP2_RAT) confirmed;
  51 GOA rows. PMID:21177871 cached with full text; PMID:14569017 full text; the
  other cited papers are abstract-only.
- No deep-research provider run (no keys); see `Prkar2a-deep-research-manual.md`.

### Key judgments

- Core MF is cAMP-dependent protein kinase inhibitor activity (GO:0004862) plus
  cAMP binding (GO:0030552) and PKA catalytic subunit binding (GO:0034236)
  [PMID:21177871 "RII subunits bind to the catalytic subunits and potently inhibit
  their activity"]. The broader GO:0008603 regulator rows are MODIFIED to GO:0004862.
- AKAP docking via the D/D domain is the defining RII function; no AKAP-binding MF
  term exists, so GO:0019904 protein domain specific binding is retained
  [PMID:17081990 "A stable, hydrophobic docking groove is formed by the helical
  interface of two RIIalpha protomers."]. GO:0044877 protein-containing complex
  binding (same paper) is MODIFIED to GO:0019904.
- GO:0036094 small molecule binding (PMID:21177871) records binding of the synthetic
  compound FMP-API-1; MODIFIED to cAMP binding, which the same paper measures. The
  SPR experiments state human RIIalpha (1-404 numbering), so the rat attribution is
  flagged as a SUSPECTED source defect (CHECK).
- GO:0031588 nucleotide-activated protein kinase complex (AMPK-type definition) is
  MODIFIED to GO:0005952 cAMP-dependent protein kinase complex.
- GO:0007189 (IBA) MODIFIED to GO:0141156 cAMP/PKA signal transduction, the cassette
  in which RIIalpha is the cAMP sensor.
- Oocyte meiosis and germinal vesicle ISO rows (with/from RGD:14184392) could not be
  traced; UNDECIDED. PKA maintains meiotic arrest, which sits awkwardly with a
  "positive regulation" term [PMID:16816331 "We conclude that an active PKA prevents
  growing oocytes from resuming meiosis."].
- beta-2 adrenergic receptor binding IPI (PMID:20395454): abstract describes a
  multiprotein complex with AKAP150, not direct RII-receptor contact; UNDECIDED.
- Bare protein binding rows removed per policy.
