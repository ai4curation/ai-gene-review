# rfbD (E. coli K-12) curation notes

## 2026-11-10 review (dTDP-L-rhamnose biosynthesis module)

- Reviewed every GOA row against the cached publications and the UniProt record.
  Deep-research generation was not run (no provider API keys in this session); the
  review rests on UniProt curated text, cached abstracts/full texts and PANTHER/PAINT files.
- Consistent treatment across the four rfb-cluster genes (rfbA/B/C/D):
  core MF and GO:0019305 ACCEPT; cytosol ACCEPT; GO:0009243 O antigen biosynthesis
  KEEP_AS_NON_CORE (product-use context, O16 repeat unit contains L-rhamnose
  [PMID:7517391 "Four rhamnose pathway genes are identified by similarity to those of other strains"]);
  GO:0000271 and GO:0009103 MODIFY to GO:0009243.
- Most K-12 lines are O-antigen negative (rfb-50/rfb-51)
  [PMID:7512872 "the rough phenotype of this strain is due to the presence of one of two independent mutations in the rfb gene cluster"].
