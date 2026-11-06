# EMENI eaf3 notes

## 2026-11-06

- Seeded `genes/EMENI/eaf3/` with
  `just fetch-gene EMENI eaf3 --uniprot-id Q5BBV4`. The reviewed UniProtKB
  entry identifies `Q5BBV4` as the Aspergillus nidulans FGSC A4 /
  Emericella nidulans eaf3 protein encoded by ORF `AN1976`.
- `just deep-research-falcon EMENI eaf3` failed locally because `agentapi` was
  not on PATH, so no generated Falcon deep-research file was produced.
- Manual web searches for `Aspergillus nidulans eaf3`,
  `Emericella nidulans eaf3`, `AN1976`, `ANIA_01976`, `Q5BBV4`, and
  A. nidulans Rpd3S/NuA4 Eaf3 terminology did not surface a paper directly
  assaying A. nidulans Eaf3. The A. nidulans chromatin literature found in
  the search results concerned other KDAC or co-repressor complexes rather
  than AN1976/eaf3.
- UniProtKB `Q5BBV4` is reviewed and identifies `AN1976` as an MRG-family
  chromatin regulator with an N-terminal Tudor-knot/chromo-like module, a
  C-terminal MRG domain, PANTHER `PTHR10880:SF15`, and a PROSITE-inferred
  nuclear localization. Its functional comment and NuA4 subunit assignment
  are both similarity-based rather than A. nidulans-specific experimental
  evidence [`Q5BBV4`, `genes/EMENI/eaf3/eaf3-uniprot.txt`].
- PANTHER classifies `Q5BBV4`, Aspergillus fumigatus eaf3 `Q4WPW2`,
  budding-yeast Eaf3 `Q12432`, fission-yeast Alp13/Eaf3 `O13953`, Candida
  albicans EAF3 `Q59K07`, and Candida glabrata EAF3 `Q6FN68` in
  `PTHR10880:SF15` / "MSL COMPLEX SUBUNIT 3". The official family label is
  "MORTALITY FACTOR 4-LIKE PROTEIN" [`interpro/panther/PTHR10880/PTHR10880-entries.csv`,
  `interpro/panther/PTHR10880/PTHR10880-metadata.yaml`].
- The current PAINT snapshot places `GO:0035267 NuA4 histone acetyltransferase
  complex`, `GO:1990841 promoter-specific chromatin binding`, and
  `GO:0006357 regulation of transcription by RNA polymerase II` on the broad
  `PTN000093963` eukaryotic MRG node, and places
  `GO:0032221 Rpd3S complex` on the fungal `PTN000853816` node. Separate
  animal `PTN000853767` MSL-complex annotations and the plant
  `PTN008955946` H3K36me3-reader annotation do not propagate to the fungal
  Eaf3 proteins [`interpro/panther/PTHR10880/PTHR10880-paint.tsv`].
- For fungal Eaf3/MRG proteins, the accepted PAINT complex calls should be the
  NuA4 row from `PTN000093963` and the Rpd3S row from `PTN000853816`. The
  plant-seeded `GO:1990841 promoter-specific chromatin binding` IBA should be
  treated skeptically because fungal Eaf3 proteins act as H3K36me-linked
  Rpd3S/NuA4 subunits rather than as CONSTANS/FT-promoter regulators like the
  source MRG1/MRG2 proteins in Arabidopsis.
- The `GO:1990841` row is therefore a plant-function overpropagation rather
  than a loss of H3K36 methyl-lysine reading in fungal Eaf3 proteins. This
  review modifies it to `GO:0140003 histone H3K36me3 reader activity` based on
  S. pombe Clr6S / S. cerevisiae Rpd3S chromodomain and H3K36me3
  peptide-binding evidence, not on the separate plant-seeded
  `PTN008955946` PAINT node.
