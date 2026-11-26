# rps-11 review notes

- 2026-10-28: fetch-gene via accession (`just fetch-gene worm Q20206 --alias rps-11`)
  because symbol search timed out at rest.uniprot.org; resolved Q20206, GeneID
  178083, WBGene00004480 as expected. GOA has 6 rows.
- Literature: see rps-11-deep-research-manual.md. Key worm papers: cryo-EM
  ribosome (PMID:39209556), rps-11 RNAi as protein-synthesis inhibition tool
  (PMID:30020921 "We inhibited protein synthesis by reducing ribosome biogenesis
  (rps-11/RPS11 RNAi)"), lifespan screen (PMID:17266679, abstract only), RNAi
  control in CAR-1 paper (PMID:16247027 "Depletions of six different ribosomal
  subunits (RPS-1, -3, -5, -11, -18, and -23) each resulted in penetrant
  sterility (unpublished data).").
- Decisions: structural constituent of ribosome ACCEPT (IBA, IEA); cytosolic
  small ribosomal subunit ACCEPT; ribosome IEA -> MODIFY to cytosolic small
  ribosomal subunit; translation IEA -> MODIFY to cytoplasmic translation;
  lifespan IMP -> KEEP_AS_NON_CORE (abstract-only, indirect consequence of
  reduced translation; defer to WormBase curator).
- No NEW terms: L2 arrest, sterility, stress resistance are necessity phenotypes.
- Curation gap (not a knowledge gap): rRNA binding is not annotated; uS17 binds
  18S rRNA family-wide but there is no worm data and no PAINT row, so not added.
