# PRO2 (YOR323C, P54885) notes

- Gamma-glutamyl phosphate reductase (glutamate-5-semialdehyde dehydrogenase, EC 1.2.1.41), NADPH-dependent; product GSA cyclizes spontaneously to P5C [UniProt:P54885 "Catalyzes the NADPH dependent reduction of L-gamma-glutamyl"]. Aldehyde dehydrogenase superfamily.
- Gene identification by complementation [PMID:2824433 "PRO2 encoded gamma-glutamyl phosphate reductase"].
- Activity measured in reverse direction in yeast extracts; D154N Pro1 raises GPR activity 5-6 fold [PMID:12513997 "we measured the reverse reaction of γ-GPR by phosphate-dependent reduction of NADP + with GSA"].
- pro2 null requires most proline for growth; exclusively cytosolic by GFP [PMID:25112878 "Pro1p, Pro2p, and Pro3p were expressed exclusively in the cytosol"]. Nuclear HDA (Huh et al.) not supported by the targeted study.

## 2026-11-02 completion pass (module bacterial_glutamate_to_p5c_biosynthesis)

- Literature search: cached publications for every GOA reference were read
  (full text where `full_text_available: true`), together with the SGD
  description (`PRO2-deep-research-sgd.md`). No other deep-research provider
  file exists and no provider API keys were available in this session.
- Cytoplasm rows reworded: the high-throughput assays resolve "cytoplasm", which
  is correct; cytosol is carried separately by the targeted GFP IDA.
- Cofactor/co-substrate binding rows (ATP binding for PRO1, NADP binding for PRO2)
  are KEEP_AS_NON_CORE, matching the E. coli and P. putida proB/proA reviews.
