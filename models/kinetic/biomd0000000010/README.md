# biomd0000000010: Kholodenko 2000 MAPK cascade

- **Source:** BioModels [BIOMD0000000010](https://www.ebi.ac.uk/biomodels/BIOMD0000000010),
  "Kholodenko2000 - Ultrasensitivity and negative feedback bring oscillations in
  MAPK cascade"; curated BioModels entry. Publication PMID:10712587.
- **Retrieved:** 2026-11-23 from
  `https://www.ebi.ac.uk/biomodels/model/download/BIOMD0000000010?filename=BIOMD0000000010_url.xml`.
- **SHA-256 of `model.xml`:** `906964e07ffd570ad94a03c1222e230b54b913cd536b008392bfb6155930a966`
- **Licence:** CC0 1.0 (BioModels public domain dedication).
- **Species:** annotated to *Xenopus laevis* RAF1 (P09560), MEK1 (Q05116) and
  MAPK1 (P26696). The MAPKKK species are named "Mos" in the SBML but annotated
  to RAF1; the mapping follows the annotation.
- **Compared with:** `modules/erk_cascade.yaml`, on the RAF (MAP3K), MEK and ERK
  tiers. The reviewed bridge is [`mapping_to_modules.yaml`](mapping_to_modules.yaml).

## Result

All three edges the model asserts on those tiers agree with the module, with no
sign conflicts and nothing on either side alone. The module's ERK ⊣ RAF feedback
appears in the model as MAPK-PP in the MAPKKK-activation rate law (reaction J0),
`V1*MKKK/((1+(MAPK_PP/Ki)^n)*(K1+MKKK))` with `n = 1` as a local parameter:

```
= ERK -| RAF   (model reactions: J0)
= MEK -> ERK   (model reactions: J6, J7)
= RAF -> MEK   (model reactions: J2, J3)
```

The module's other edges (adaptor, SOS, RAS, DUSP, ERK output) involve entities
the model does not contain: dephosphorylation (J1, J4, J5, J8, J9) is written
with no phosphatase species. Those edges therefore fall outside the comparison.

To reproduce:

```bash
ai-gene-review compare-module-sbml \
    modules/erk_cascade.yaml \
    models/kinetic/biomd0000000010/model.xml \
    -m models/kinetic/biomd0000000010/mapping_to_modules.yaml
```
