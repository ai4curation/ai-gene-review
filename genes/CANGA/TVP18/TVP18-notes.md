# TVP18 notes

## Literature search

- PubMed and web searches on 2026-11-21 for `CAGL0K03025g`, `Q6FN38`,
  `Candida glabrata TVP18`, and `Nakaseomyces glabratus TVP18` found
  database records but no direct Candida glabrata TVP18 functional paper.
- The closest fungal primary literature remains indirect for this review:
  S. cerevisiae Tvp18 was discovered in Tlg2-containing Golgi/endosomal
  vesicles by immunoisolation proteomics [PMID:16107716 "Tvp38, Tvp23, Tvp18,
  Tvp15"], a follow-up paper placed Tvp18 in an interactive network with Tvp23,
  Tvp15, Yip4, and Yip5 [PMID:17178117 "Tvp23, Tvp18 and Tvp15 are in an
  interactive network"], and a Komagataella phaffii TVP18 knockout perturbed
  Golgi cisternae [PMID:33263222 "we identified three strains with irreversible
  perturbations in the stacking of the Golgi cisternae"].
- PANTHER places C. glabrata Q6FN38 in PTHR13314:SF2, the same
  TVP18/calcium-channel Flower homolog subfamily as S. cerevisiae TVP18,
  S. pombe tvp18, C. albicans TVP18, and Neurospora tvp-18.

## Review decisions

- `GO:0000139` Golgi membrane: accepted for the combined UniProt IEA because
  the row is concordant with UniProt's similarity-inferred Golgi membrane
  statement and the PAINT Golgi-membrane IBD at Ascomycota node
  `PTN001779222`.
- `GO:0016192` vesicle-mediated transport: accepted as a broad combined
  UniProt IEA that agrees with the PTHR13314 opisthokont PAINT node seeded by
  Drosophila `fwe` and S. cerevisiae TVP18.
- `GO:0016020` membrane: marked too general because InterPro's
  TVP18/calcium-channel Flower mapping is true but less informative than Golgi
  membrane.
- `GO:0003674` molecular_function and `GO:0008150` biological_process:
  accepted as CGD ND placeholders. The review cites homology, PAINT, and
  other-species evidence, but no paper assaying the C. glabrata gene product.
- PTHR13314 also places `GO:0005262` calcium channel activity on
  `PTN001779219`, the same opisthokont node used for the accepted
  `GO:0016192` assertion. I did not add that molecular function because the
  `GO:0005262` row is seeded only by Drosophila `fwe`, the fungal
  `PTN001779222` node carries only Golgi membrane, and the fungal TVP18 papers
  do not demonstrate calcium-channel activity.
