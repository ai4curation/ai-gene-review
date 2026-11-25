# HYR1 / GPX3 / ORP1 (YIR037W, P40581) notes

Module context: `glutathione_thioredoxin_redox_systems`; YeastCyc places it on H2O2 + 2 GSH (EC 1.11.1.9).

- gpx3 is the peroxide-sensitive GPx mutant and the main GPx activity contributor [PMID:10480913 "The gpx3Delta mutant was hypersensitive to peroxides"; "Glutathione peroxidase activity decreased approximately 57 and 93% in the gpx3Delta and gpx1Delta/gpx2Delta/gpx3Delta mutants"]
- H2O2 sensor/transducer for Yap1 [PMID:12437921 "We identified the glutathione peroxidase (GPx)-like enzyme Gpx3 as a second component of the pathway, serving the role of sensor and transducer of the hydroperoxide signal to Yap1."]; thioredoxin reduces it [PMID:12437921 "Thioredoxin turns off the pathway by reducing both sensor and regulator."]
- Orp1 redox relay generalises to roGFP2 [PMID:19755417 "Orp1 mediates near quantitative oxidation of roGFP2 by H(2)O(2)"]
- PHGPx activity with GSH in vitro [PMID:11445588]
- Minor IMS pool [PMID:22984289 table entry "YIR037WHYR1Thiol peroxidase"]
- Peroxisomal matrix (UniProt from PMID:22659048) — the abstract only describes Gpx1 in peroxisomal matrix [PMID:22659048 "We found that Gpx1 was located in the peroxisomal matrix."]; left UNDECIDED.

## Conclusions
- Core MF GO:0140824; GSH-peroxidase/PHGPx non-core; RCA glutathione metabolic process removed.
- Suggested question: GO:0140442 peroxide sensor activity for the Yap1 relay (not proposed as NEW; definition is about change in the sensor's own activity).

## Huntington's disease model (SGD description follow-up)
- SGD says GPx activity is neuroprotective in Huntington's disease models. Source: a genome-wide overexpression suppressor screen in yeast expressing a mutant Htt fragment, where GPX1 and GPX3 (HYR1) were among the strongest suppressors [PMID:23974869 "Two of the most robust suppressors identified were GPX1 and GPX3, which encode antioxidant GPx enzymes"]. This is an overexpression effect in a heterologous disease model; it reflects the peroxidase activity and does not add a physiological role, so no annotation.
