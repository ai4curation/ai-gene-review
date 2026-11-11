# TVP18 notes

## 2026-10-17 review

- Reviewed the seeded TVP18 GOA rows against `TVP18-ai-review.yaml`,
  `TVP18-uniprot.txt`, cached PMID:16107716, cached PMID:17178117, and
  `interpro/panther/PTHR13314/PTHR13314-paint.tsv`.
- PMID:16107716 directly supports Golgi/endosomal membrane localization: the
  paper identified YMR071C/Tvp18 in Tlg2 immunoisolates in the proteomic survey
  of Sed5- and Tlg2-containing yeast Golgi subcompartments.
- PMID:17178117 is abstract-only in the local cache but is directly about
  Tvp38, Tvp23, Tvp18, and Tvp15. Its visible abstract supports the follow-up
  localization and Yip1-family interaction context behind SGD's
  vesicle-mediated transport IGI rows, so these were accepted rather than
  overruled from incomplete full-text evidence.
- PAINT places `GO:0000139` on `PTN001779222`, with SGD TVP18 as the seed, and
  `GO:0016192` on `PTN001779219`, with both Drosophila `fwe` and SGD TVP18 as
  seeds. TVP18 appearing in the `WITH/FROM` list is therefore expected and was
  not treated as circular.
- The same PAINT table records `GO:0005262` calcium channel activity for
  `PTN001779219` seeded from Drosophila `fwe`; that molecular function is not
  in the current yeast TVP18 GOA snapshot and was not added as `NEW` because the
  yeast papers establish Golgi/endosomal localization, genetic interaction, and
  physical interaction, not channel activity.
- PubMed/web searches did not recover a newer direct yeast `TVP18`/`YMR071C`
  characterization beyond the two cached Inadome papers. Newer hits were
  database pages, broad screens, or indirect papers about related late-Golgi
  machinery rather than direct biochemical or cell-biological characterization
  of Tvp18.
