# mon1 review notes

## Evidence summary

Aspergillus fumigatus Q4WHL1 is a conserved fungal Mon1/SAND-family protein in
PTHR13027:SF7, the same subfamily as S. cerevisiae MON1, S. pombe mon1,
Candida albicans MON1, Neurospora apg-13, A. nidulans monA, and Fusarium
FgMON1. The two fungal PAINT rows at `PTN000989606` assert `GO:0000329`
fungal-type vacuole membrane and `GO:0006623` protein targeting to vacuole from
the S. cerevisiae MON1 seed, and Q4WHL1 is under that fungal node.

The key budding-yeast source is PMID:12364329. It shows that Mon1 and Ccz1
physically interact as a stable complex and that mon1 and ccz1 mutants are
defective for Cvt, autophagy/pexophagy, CPY, ALP, MVB, and endocytic delivery
routes to the vacuole. Mechanistically, PMID:24413168 showed that both Mon1 and
Ccz1 longin-domain surfaces are needed for Rab7/Ypt7 exchange activity.

The closest filamentous-fungal Mon1 studies are not in A. fumigatus itself.
PMID:26657788 characterized FgMon1 in Fusarium graminearum and tied it to
FgRab7, vacuole fusion, autophagy, and endocytosis. PMID:32010467 characterized
Aspergillus MonA experimentally in A. nidulans and A. flavus and included
A. fumigatus Af293 Q4WHL1 in the Aspergillus MonA alignment; the paper found
that deleting monA in A. nidulans and A. flavus disrupts normal vacuole
morphology.

I did not find a direct A. fumigatus mon1 experimental publication in PubMed or
web searches for `Aspergillus fumigatus Mon1`, `AFUA_2G05010`, or
`Mon1 Ccz1 Aspergillus`. I also checked the Ccz1 question because Son and Park
reported in 2019 that standard searches could not find Ccz1 orthologs in
Aspergillus, Fusarium, or Penicillium. UniProt now lists Q4WNB8/AFUA_6G06910 as
an A. fumigatus `CCZ1/INTU/HSP4 first Longin domain-containing protein`, so
filamentous-fungal Ccz1 candidates are findable with newer remote-homology
methods, but direct A. fumigatus Mon1-Ccz1 binding and Rab7 GEF assays are
still the main open biology.

## Annotation decisions

- `GO:0000329 fungal-type vacuole membrane` and `GO:0006623 protein targeting to
  vacuole`: ACCEPT. Both are fungal PAINT calls from PTN000989606 and match the
  conserved Mon1 role in late fusion of cargo vesicles with fungal vacuoles.
- `GO:0005085 guanyl-nucleotide exchange factor activity` `contributes_to`:
  ACCEPT. The broad eukaryotic PAINT node fits Mon1's contributed role in a
  Rab7/Ypt7-directed GEF module, and FgMon1-FgRab7 data corroborate this role in
  a filamentous ascomycete.
- `GO:0005774 vacuolar membrane`: MODIFY to the accepted fungal-type vacuole
  membrane child term.
- `GO:0006623 protein targeting to vacuole` from IPR004353: ACCEPT because the
  InterPro family mapping reaches the same process as the accepted fungal PAINT
  call.
- `GO:0016192 vesicle-mediated transport`: MODIFY to `GO:0032511 late endosome
  to vacuole transport via multivesicular body sorting pathway`. The longin
  domain mappings are true but broader than the Mon1-specific
  endosome-to-vacuole role.
- `GO:0032585 multivesicular body membrane`: KEEP_AS_NON_CORE because it is a
  plausible inferred Mon1 location but has not been directly assayed in
  A. fumigatus.
- `GO:0035658 Mon1-Ccz1 complex`: ACCEPT as a broad PAINT transfer, with a
  caveat that the filamentous-fungal Ccz1 partner is diverged and still needs
  direct validation.
- Add `GO:0016236 macroautophagy` as a conservative NEW row: Mon1 contributes
  to the Rab7/Ypt7 activation/fusion machinery used by autophagosomes at the
  vacuole, and this role is experimentally supported in S. cerevisiae and
  F. graminearum.
