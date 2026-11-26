# BDKRB2 review notes

Automated deep research was attempted with Falcon and the `perplexity-lite` fallback, but neither
provider was available in this runtime, so this review used the seeded GOA rows, cached PubMed and
Reactome records, the kallikrein-kinin module, and the local ACE and BDKRB1 reviews.

## Core biology

- BDKRB2 is the constitutive B2 bradykinin receptor, a seven-transmembrane GPCR that binds intact
  kinins. Two 1992 human cloning papers showed high-affinity bradykinin binding and functional
  receptor expression [PMID:1314587; PMID:1329734].
- The receptor couples to Gq/phosphatidylinositol/Ca2+ signaling after bradykinin stimulation
  [PMID:1329734; PMID:10653985] and can also activate arachidonate release in transfected cells
  [PMID:8302267].
- Human ACE and BDKRB2 can form a plasma-membrane complex: ACE and B2R coimmunoprecipitated,
  colocalized by microscopy, showed FRET, and cointernalized after agonist stimulation
  [PMID:17077303]. This is specific evidence for the non-core `protease binding` row.
- BDKRB2 can also heterodimerize with AGTR1, increasing Gq/Gi activation and changing receptor
  sequestration [PMID:10993080]. This is genuine receptor crosstalk but secondary to bradykinin
  reception.

## GO-CAM notes

- The BDKRB2 bradykinin receptor activity, plasma membrane location and vasodilation context in
  GO-CAM `6246724f00000632` are consistent with this review.
- Final GO-CAM consistency PR: change the BDKRB2 activity consistency from no gene review to
  consistent after this review merges, but keep the existing model-level issue that a direct
  `has_input` edge from BDKRB2 receptor activity to KNG1 conflates the KNG1 precursor with the
  released bradykinin ligand.
