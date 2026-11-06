# sec2 review notes

## 2026-11-06

### PTHR14430 and PAINT

`sec2` is the long fission-yeast member of PTHR14430. The family has two PAINT
nodes relevant to this review:

- `PTN000374167`: Opisthokonta `GO:0005085` guanyl-nucleotide exchange factor
  activity, supported by fission Sec2, budding-yeast SEC2 and animal Rab3/Rab8
  GEFs.
- `PTN001024876`: fungal `GO:0051286` cell tip, supported by PomBase `sec2` and
  CGD `SEC2`.

Both nodes are retained. `PomBase:SPAC23C4.10` in the WITH/FROM list is expected
for an IBA whose target also has direct experimental evidence.

### Literature read

PMID:20130084 is the Yang and Neiman Spo13 study. It establishes Spo13 as a
short Sec2-GEF-domain paralog specialized for the meiotic spindle pole body and
explicitly notes that SPAC23C4.10 is the long, bona fide Sec2-like paralog.

PMID:27630265 is the main Sec2 paper in the cached set. It directly localizes
Sec2-GFP to vegetative growing tips and the medial division region, to meiotic
spindle poles as meiosis proceeds, and finally to closed forespore membranes. It
also places Sec2 in the Ypt3-Sec2-Ypt2 Rab cascade: GTP-bound Ypt3 recruits
Sec2, and Sec2 and Ypt2 fail to localize to the vegetative cell tip or division
region in the ypt3 mutant.

The broad literature search did not turn up a newer primary Sec2 paper that
overrides these PomBase rows. Later sporulation reviews restate the Sec2/Ypt2
model.

### Annotation decisions

The vegetative `GO:0051285` cell cortex of cell tip, HDA `GO:0051286` cell tip,
`GO:0032153` cell division site and `GO:0071341` medial cortical node rows are
accepted as active exocytic sites. The `GO:0005628` prospore membrane and
`GO:0035974` meiotic spindle pole body rows are correct but non-core because
they describe sporulation-specific reuse of the Sec2 module.

The CACAO row to `GO:0090619` is biologically plausible but cites
PMID:27630562, which is a human cerebral perfusion MRI paper. I kept the
sporulation-specific localization as non-core and recorded a confirmed CACAO
`WRONG_REFERENCE` source defect rather than deleting the row.
