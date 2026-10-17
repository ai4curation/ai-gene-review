# MON1 review notes

## Evidence summary

C. albicans MON1 (UniProtKB:Q5A723) is a reviewed Swiss-Prot protein classified
in PANTHER family `PTHR13027` ("SAND PROTEIN-RELATED") and in the fungal MON1
subfamily `PTHR13027:SF7` ("VACUOLAR FUSION PROTEIN MON1 HOMOLOG"). The cached
PANTHER rows include Q5A723 in that subfamily and show a fungal PAINT ancestor,
`PTN000989606`, with two IBD rows seeded only by SGD:S000003092: `GO:0000329`
fungal-type vacuole membrane and `GO:0006623` protein targeting to vacuole.

No PubMed record was found for `Candida albicans` plus `MON1`, `orf19.8109`, or
`CCZ1 MON1` searches. The Candida review therefore rests on the GOA rows from
CGD/GO_Central/UniProt/InterPro, the reviewed UniProt classification, the local
PANTHER membership and PAINT rows, and the S. cerevisiae experimental literature
that seeds the fungal PAINT node.

Wang et al. established the direct yeast source evidence for the fungal PAINT
vacuolar-delivery rows: "Both Mon1 and Ccz1 are required for protein delivery
through the Cvt pathway and other vacuole trafficking processes including the
CPY and ALP pathways and endocytosis"; they also found that "Ccz1 and Mon1 form
a stable protein complex that binds the vacuole membrane" [PMID:14662743].

Cabrera et al. refined the biochemical interpretation by showing that both
subunits contribute to Ypt7 nucleotide exchange and that membrane association
potentiates the GEF: "Mon1-Ccz1 activity requires residues within the predicted
longin domains of both subunits" and the complex "activates Ypt7 via a common
interface, has highest activity on membranes" [PMID:24413168].

## Annotation decisions

- `GO:0000329 fungal-type vacuole membrane` and `GO:0006623 protein targeting to
  vacuole`: ACCEPT. Both trace to the fungal PAINT node `PTN000989606`.
- `GO:0035658 Mon1-Ccz1 complex` and `GO:0005085 guanyl-nucleotide exchange
  factor activity`: ACCEPT. These trace to broader opisthokont PAINT nodes and
  match the conserved complex and contributed Rab7/Ypt7 GEF function.
- `GO:0005774 vacuolar membrane`: TOO_GENERAL because it is true but less
  specific than the fungal-type vacuole membrane IBA in the same review.
- `GO:0016192 vesicle-mediated transport`: MODIFY to `GO:0032511 late endosome
  to vacuole transport via multivesicular body sorting pathway`, rather than
  retain the generic InterPro longin-domain process.
- `GO:0032585 multivesicular body membrane`: ACCEPT as a conserved prevacuolar
  endosome location.
- CGD ND rows on `molecular_function` and `cellular_component`: REMOVE as stale
  root placeholders because specific MF and CC assertions now exist for MON1.
