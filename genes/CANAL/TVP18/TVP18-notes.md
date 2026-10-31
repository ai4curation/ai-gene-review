# TVP18 notes

## Literature search

- PubMed searches on 2026-10-17 for `TVP18 AND "Candida albicans"` and for the
  Candida locus aliases `orf19.4845`, `CaO19.4845`, and `C1_09800C` returned no
  direct C. albicans TVP18 papers.
- Searching PubMed for `TVP18` alone returned only three papers, all indirect
  for this review:
  - PMID:16107716 identified Tvp18 as one of several evolutionarily conserved
    membrane proteins recovered from Saccharomyces cerevisiae Tlg2-containing
    Golgi/endosomal vesicles [PMID:16107716 "We found six uncharacterized but
    evolutionarily conserved proteins and named them Svp26"].
  - PMID:17178117 followed up on S. cerevisiae Tvp38, Tvp23, Tvp18, and Tvp15
    as novel Golgi/endosome membrane proteins and their Yip-family interactions
    [PMID:17178117 "Immunoprecipitation of Tvp proteins indicated that Tvp23,
    Tvp18 and Tvp15 are in an interactive network with Yip1-family proteins,
    Yip4 and Yip5."].
  - PMID:33263222 knocked out the Komagataella phaffii TVP18 ortholog while
    screening secretory-pathway genes for effects on Golgi cisternae
    [PMID:33263222 "we identified three strains with irreversible perturbations
    in the stacking of the Golgi cisternae"].
- Web searches for `orf19.4845`, `CaO19.4845`, `CAALFM_C109800CA`, and
  `C1_09800C` did not reveal a newer direct C. albicans TVP18 functional paper.
  The only Candida-specific hit was an indirect chemogenomic library listing of
  the orf19.4845/TVP18 mutant.

## Review decisions

- `GO:0000139` Golgi membrane: accepted for both the fungal PAINT IBA from
  `PTN001779222` and the UniProt SubCell IEA.
- `GO:0016192` vesicle-mediated transport: accepted as a broad ancestral PAINT
  process from `PTN001779219`; no narrower Candida-specific process should be
  proposed without direct evidence for the fungal TVP18 role.
- `GO:0016020` membrane: marked too general because the InterPro mapping is
  true but less specific than the PAINT and UniProt Golgi membrane calls.
- `GO:0003674` molecular_function: retained as a non-core ND placeholder. The
  protein is a TVP18/calcium-channel-flower-family multipass membrane protein,
  but the fungal branch has no established molecular activity.
- PTHR13314 also places `GO:0005262` calcium channel activity at PTN001779219,
  the same opisthokont ancestor used for `GO:0016192`. I did not accept a
  calcium-channel activity for Candida TVP18 because that MF placement is seeded
  only by Drosophila `fwe`, while the corresponding calcium-import process
  `GO:0070588` is restricted to Eumetazoa node PTN000999743. The K. phaffii
  knockout abstract links TVP18-family Golgi-cisternae phenotypes to calcium
  concentration, homeostasis, or signalling, but still does not assay direct
  calcium channel activity in a fungal TVP18 protein [PMID:33263222].
