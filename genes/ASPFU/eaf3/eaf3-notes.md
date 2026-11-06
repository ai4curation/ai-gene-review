# ASPFU eaf3 notes

## 2026-11-06

- Seeded `genes/ASPFU/eaf3/` with `just fetch-gene ASPFU eaf3 --uniprot-id Q4WPW2`.
  The default exact-symbol UniProt query failed twice, first with a timeout and
  then with a UniProt `500`; the PANTHER `PTHR10880` member table listed
  `Q4WPW2` as the A. fumigatus Af293 `eaf3` entry.
- `just deep-research-falcon ASPFU eaf3` failed locally because `agentapi` was
  not on PATH, so no generated Falcon deep-research file was produced.
- Manual web searches for `Aspergillus fumigatus eaf3`, `AFUA_4G10660`,
  `Q4WPW2`, and A. fumigatus Rpd3S/NuA4 Eaf3 terminology did not surface a
  paper directly assaying A. fumigatus Eaf3. The A. fumigatus literature found
  for chromatin enzymes was about other regulators such as HosA/HosB/Hos3,
  Sas3, and SirE rather than AFUA_4G10660.
- UniProtKB `Q4WPW2` is reviewed and identifies AFUA_4G10660 as an MRG-family
  chromatin regulator with N-terminal Tudor-knot and C-terminal MRG domains,
  PANTHER `PTHR10880:SF15`, and a PROSITE-inferred nuclear localization. Its
  functional comment and NuA4 subunit assignment are both similarity-based
  rather than A. fumigatus-specific experimental evidence
  [`Q4WPW2`, `genes/ASPFU/eaf3/eaf3-uniprot.txt`].
- PANTHER classifies `Q4WPW2`, budding-yeast Eaf3 `Q12432`, fission-yeast
  Alp13/Eaf3 `O13953`, Candida albicans EAF3 `Q59K07`, Candida glabrata EAF3
  `Q6FN68`, and Emericella nidulans Eaf3 `Q5BBV4` in `PTHR10880:SF15` /
  "MSL COMPLEX SUBUNIT 3". The official family label is "MORTALITY FACTOR
  4-LIKE PROTEIN" [`interpro/panther/PTHR10880/PTHR10880-entries.csv`,
  `interpro/panther/panther.obo`].
- The current PAINT snapshot places `GO:0035267 NuA4 histone acetyltransferase
  complex`, `GO:1990841 promoter-specific chromatin binding`, and
  `GO:0006357 regulation of transcription by RNA polymerase II` on the broad
  `PTN000093963` eukaryotic MRG node, and places
  `GO:0032221 Rpd3S complex` on the fungal `PTN000853816` node. Separate animal
  `PTN000853767` MSL-complex annotations and the plant `PTN008955946`
  H3K36me3-reader annotation do not propagate to the fungal Eaf3 proteins
  [`interpro/panther/PTHR10880/PTHR10880-paint.tsv`].
- For fungal Eaf3/MRG proteins, the accepted PAINT complex calls should be the
  NuA4 row from `PTN000093963` and the Rpd3S row from `PTN000853816`. The
  plant-seeded `GO:1990841 promoter-specific chromatin binding` IBA should be
  treated skeptically because fungal Eaf3 proteins act as H3K36me-linked
  Rpd3S/NuA4 subunits rather than as CONSTANS/FT-promoter regulators like the
  source MRG1/MRG2 proteins in Arabidopsis.
