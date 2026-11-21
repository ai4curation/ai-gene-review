# MON1 review notes

## Evidence summary

Candida glabrata MON1, UniProtKB:Q6FU19, is a reviewed Swiss-Prot
vacuolar-fusion protein in PANTHER family `PTHR13027` ("SAND
PROTEIN-RELATED") and the Mon1 subfamily `PTHR13027:SF7` ("VACUOLAR
FUSION PROTEIN MON1 HOMOLOG"). The local PANTHER entries place Q6FU19 in the
same subfamily as S. cerevisiae MON1, S. pombe mon1, C. albicans MON1,
N. crassa apg-13, and A. fumigatus mon1.

No C. glabrata- or N. glabratus-specific MON1 paper was found in PubMed/web
searches for `Q6FU19`, `CAGL0F07051g`, `"Candida glabrata" MON1`, and
`"Nakaseomyces glabratus" MON1`. The current CGD `ND` rows therefore remain
accurate as no-direct-data placeholders: all specific MON1 molecular-function
and cellular-component assertions in this review come from orthology,
UniProtKB-SubCell, InterPro, or UniProt's combined automated annotation.

The key fungal PAINT node is `PTN000989606`, which assigns `GO:0000329
fungal-type vacuole membrane` and `GO:0006623 protein targeting to vacuole`
to fungal Mon1 proteins from the SGD MON1 experimental seed. Wang et al.
showed in S. cerevisiae that "Subcellular fractionation and
co-immunoprecipitation experiments confirm that Mon1 and Ccz1 physically
interact as a stable protein complex termed the Ccz1-Mon1 complex" and that
Mon1 and Ccz1 are required late in several routes that deliver cargo to the
vacuole [PMID:12364329].

The broader eukaryotic and opisthokont PAINT nodes for `GO:0005085
guanyl-nucleotide exchange factor activity` and `GO:0035658 Mon1-Ccz1
complex` also fit the C. glabrata protein. Nordmann et al. identified the
assembled complex as the Ypt7/Rab7 GEF, Cabrera et al. showed that residues in
both longin-domain subunits contribute to Ypt7 nucleotide exchange on
membranes, and newer membrane reconstitution work by Borchers et al. mapped
Mon1 Rab5-dependent activation/autoinhibition rather than a separate
GEF-inhibitor activity [PMID:20797862; PMID:24413168; PMID:37463208].

## Annotation decisions

- `GO:0000329 fungal-type vacuole membrane`, `GO:0006623 protein targeting to
  vacuole`, `GO:0035658 Mon1-Ccz1 complex`, and `GO:0005085
  guanyl-nucleotide exchange factor activity` are accepted as the conserved
  Mon1-Ccz1 module.
- Generic `GO:0005774 vacuolar membrane` is modified to the fungal-type
  vacuole membrane child term, while `GO:0032585 multivesicular body membrane`,
  `GO:0005768 endosome`, and `GO:0005829 cytosol` are kept as plausible but
  non-core localization transfers.
- `GO:0016192 vesicle-mediated transport` is modified to `GO:0032511 late
  endosome to vacuole transport via multivesicular body sorting pathway`,
  matching the conserved MVB/endosome-to-vacuole route more closely than the
  generic longin-domain InterPro2GO parent.
- The autophagy, macroautophagy, Cvt, and protein targeting to vacuolar
  membrane rows are kept as route-specific conserved contexts that use
  Mon1-Ccz1/Ypt7, not as the core molecular activity itself.
- The phosphatidylserine, phosphatidylinositol-5-phosphate, and
  phosphatidylinositol-3-phosphate binding rows are kept as secondary
  membrane-recruitment properties; `GO:1990624 guanyl nucleotide exchange factor
  inhibitor activity` is marked over-annotated because the yeast source
  describes intramolecular autoinhibition by Mon1's own N-terminus.
