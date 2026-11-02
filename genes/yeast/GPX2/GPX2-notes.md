# GPX2 (YBR244W, P38143) notes

Review for the YeastPathways `glutathione_thioredoxin_redox_systems` module (YeastCyc reaction: H2O2 + 2 GSH -> GSSG + 2 H2O, EC 1.11.1.9). No paid deep research run; evidence from UniProt and cached abstracts.

- Named GPX2 as one of three GPx homologs; expression induced by oxidative stress via Yap1 [PMID:10480913 "The GPX2 gene expression was induced by oxidative stress, which was dependent upon the Yap1p."]
- gpx2 single null has no obvious phenotype [PMID:10480913 "null mutants of the GPX1 and GPX2 did not show any obvious phenotypes"]
- PHGPx activity with GSH in vitro [PMID:11445588 "Studies with cloned GPX1, GPX2, and GPX3 expressed heterologously in Escherichia coli confirmed that these genes encode proteins with PHGPx activity."]
- Key: actually an atypical 2-Cys peroxiredoxin using thioredoxin [PMID:16251189 "Here we show that GPX2 encodes an atypical 2-Cys peroxiredoxin which uses thioredoxin as an electron donor."]; GSH is a poor donor [PMID:16251189 "it showed remarkably less activity toward these peroxides in the presence of glutathione, glutathione reductase, and NADPH"]
- Localisation: cytoplasm + mitochondria (outer membrane cytosolic face, inner membrane matrix face); sporulation defect [PMID:21763276 "In mitochondria, Gpx2 was associated with the outer membrane of the cytoplasmic-side, as well as the inner membrane of the matrix-side."]
- UniProt now EC 1.11.1.24, caution about GPx name [UniProt:P38143].

## Curation conclusions
- Core MF: GO:0140824 thioredoxin-dependent peroxiredoxin activity. GSH peroxidase / PHGPx rows kept as non-core.
- YeastCyc assignment to EC 1.11.1.9 is historical-name driven; recommend EC 1.11.1.24 step. RCA "glutathione metabolic process" removed.
- PMID:11875065 (glutaredoxin paper) IDA for GSH peroxidase could not be checked (abstract-only); deferred.
