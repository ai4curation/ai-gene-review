# apg-13 / MON1 review notes

## Summary

Neurospora Q870Q4 is a conserved fungal Mon1/SAND-family protein in
PTHR13027:SF7. The `apg-13` symbol is potentially misleading: PubMed hits for
Neurospora `atg-13` describe NCU04840, the Atg13/Atg1-complex subunit, not
NCU09220/Q870Q4. I did not treat those autophagy-initiation papers as direct
evidence for this review.

The most important curated rows are the two PTHR13027 fungal PAINT calls at
`PTN000989606`, which assign `GO:0000329 fungal-type vacuole membrane` and
`GO:0006623 protein targeting to vacuole` from the experimentally characterized
S. cerevisiae MON1 seed. In the PANTHER entries file, Q870Q4 sits in the same
`PTHR13027:SF7` Mon1 homolog subfamily as S. cerevisiae MON1, S. pombe mon1,
Candida albicans MON1, and multiple filamentous-fungal MON1 proteins.

## Literature checked

PMID:12364329 is the key S. cerevisiae paper behind the fungal PAINT placement.
Its abstract reports that Mon1 and Ccz1 mutants block vacuolar import of Ape1,
autophagy, pexophagy, and several biosynthetic routes that deliver hydrolases
to the vacuole, and that subcellular fractionation/co-IP show a stable
Ccz1-Mon1 complex.

PMID:26657788 characterizes FgMon1 in Fusarium graminearum. This is not a PAINT
seed in the current `PTHR13027-paint.tsv`, but it is useful Sordariomycetes
support: the paper reports a conserved Mon1 trafficking domain, FgMon1
vacuolar/cytosolic localization, a fragmented-vacuole phenotype in the mutant,
defective autophagy, and rescue of the FgMon1 mutant by constitutively active
FgRab7.

PMID:35793146 characterizes VmMon1-Ccz1 in Valsa mali. Only the abstract is
cached, but the newer fungal result is consistent with conserved Mon1-Ccz1
function in conidiation, autophagy, and virulence.

Web/PubMed searches for `"NCU09220"`, `"Q870Q4"`, and Neurospora MON1 did not
find a direct N. crassa experimental paper. The main Neurospora autophagy hit,
PMID:25333968, is about female development and lists `atg-13 | 04840`, which is
not this Mon1-family gene.

## Annotation decisions

- The PAINT fungal vacuole membrane and protein targeting to vacuole rows are
  accepted as core inherited Mon1 functions from `PTN000989606`.
- The Opisthokonta `GO:0035658 Mon1-Ccz1 complex` and
  `GO:0005085 guanyl-nucleotide exchange factor activity` `contributes_to`
  rows are accepted as broader, well-scoped PAINT calls.
- `GO:0005774 vacuolar membrane` is correct but less specific than the accepted
  fungal-type vacuole membrane child, so it is marked `MODIFY`.
- The InterPro longin-domain `GO:0016192 vesicle-mediated transport` row is
  marked `MODIFY` toward late endosome-to-vacuole MVB transport because the
  existing term is true but too broad.
- The SubCell `GO:0032585 multivesicular body membrane` row is retained as
  defensible non-core context; it should not displace the fungal vacuole membrane
  and protein-targeting PAINT rows as core assertions.
- Add `GO:0006914 autophagy` as a conservative new annotation: Mon1-Ccz1 performs
  a conserved Rab7/Ypt7 activation step needed for autophagosome-vacuole fusion,
  and that role is experimentally visible in yeast and filamentous fungi.
