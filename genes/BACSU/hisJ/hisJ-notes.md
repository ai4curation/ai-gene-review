# hisJ (ytvP; UniProt name hisK) - Bacillus subtilis 168, O34411

## Provenance of this review

- Deep research providers were unavailable for this session (no API keys), so no
  `*-deep-research-<provider>.md` file exists. Evidence comes from the cached primary paper,
  the UniProt Swiss-Prot record and the PANTHER/PAINT family files.
- B. subtilis is not covered by the MOD-description deep-research recipe (only worm, fly, yeast).

## Key evidence

- [PMID:10322033 "A B. subtilis ytvP mutant was auxotrophic for histidine."]
- [PMID:10322033 "HolPase activity could not be detected in crude extracts of the ytvP mutant, while
  purified glutathione S-transferase-YtvP fusion protein exhibited strong HolPase activity."]
- [PMID:10322033 "HisJ constitutes a family of related enzymes that are not homologous to the HolPases
  of Escherichia coli, Salmonella typhimurium, and Haemophilus influenzae."]
- UniProt O34411: "Belongs to the PHP hydrolase family. HisK subfamily."; NCBIfam TIGR01856 hisJ_fam;
  InterPro IPR010140 Histidinol_P_phosphatase_HisJ; PANTHER PTHR21039:SF0 HISTIDINOL-PHOSPHATASE.
- PAINT node PTN000471366 (PTHR21039) carries GO:0004401 and GO:0000105, seeded by S. cerevisiae HIS2.
  `just paint-losses BACSU hisJ`: no IRD/IKR loss on the lineage.

## Interpretation

hisJ is the sole characterised histidinol-phosphate phosphatase of B. subtilis (step 8 of histidine
biosynthesis); loss of the gene removes detectable HolPase activity from extracts, so there is no
significant backup enzyme under the conditions tested. The cached abstract does not report kinetics,
metal requirements or localization. No GO cellular-component annotation exists; the enzyme is
presumably cytosolic, but no direct evidence was found, so no NEW CC row was proposed.
