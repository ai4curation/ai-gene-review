# AS1 (O80931) review notes

## Session 2026-10-28

- Fetched with `just fetch-gene ARATH AS1`; UniProt id O80931 confirmed (AS1_ARATH, At2g37630).
  45 GOA rows. No deep-research API keys: literature synthesis in `AS1-deep-research-manual.md`.
- Full text available for PMID:18203921, PMID:23271976, PMID:18003921, PMID:21950734,
  PMID:27334696, PMID:23133401 and the Y1H papers PMID:25533953, PMID:31806676 (partial
  PMID:25352272). Others abstract-only.
- Key mechanistic point: AS1 alone does not bind DNA in EMSA; the AS1-AS2 heterodimer does
  [PMID:18203921 "When translated separately, neither AS1 nor AS2 was able to bind fragment X
  in vitro"]. Core MF therefore recorded as contributes_to DNA-binding transcription factor
  activity / cis-regulatory region binding.
- AS1 represses KNOX and abaxial genes but also activates FT with CO [PMID:21950734], so
  GO:0006355 is refined to both negative and positive regulation of transcription.
- Defense: AS1 is a NEGATIVE regulator of necrotroph (fungal) resistance [PMID:18003921]; the
  "defense response to fungus" row is sign-corrected to GO:1905035 negative regulation of
  antifungal innate immune response (GO has no "negative regulation of defense response to
  fungus" class; checked with OAK descendants of GO:1900150).
- GO:0008356 asymmetric cell division (PMID:15608337) appears to conflate leaf-level
  asymmetry ("asymmetric leaves", "asymmetry in cell division patterns") with the cellular
  process; abstract-only so MARK_AS_OVER_ANNOTATED plus a source defect query (CHECK).
- response to virus (PMID:18794352): AS1 is the host target hijacked by betaC1; that is not
  AS1 performing an antiviral response. Abstract-only: MARK_AS_OVER_ANNOTATED.
- No NEW process terms proposed (fruit patterning in PMID:23133401 and flowering in
  PMID:21950734 are genetic/expression evidence; recorded in core_functions description
  and questions instead).
- Protein binding (GO:0005515) rows removed per policy; the partner information (AS2, HDA6,
  HIRA, CO) is captured in core_functions.
