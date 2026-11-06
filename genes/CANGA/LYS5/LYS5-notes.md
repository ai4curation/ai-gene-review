# CANGA LYS5 notes

## 2026-11-06 PTHR12215 audit

- `LYS5` / `CAGL0E05104g` / UniProt `Q6FV34` is the *Candida glabrata* ortholog in
  `PTHR12215:SF10`, the fungal/human broad-specificity Sfp-type
  phosphopantetheinyl-transferase subfamily. The local PANTHER entry is:
  `Q6FV34,L-aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase,protein,284593,...,LYS5,258,PTHR12215:SF10,...`.
- The current PAINT file places cytosol, `GO:0008897 holo-[acyl-carrier-protein]
  synthase activity`, and broad `GO:0051604 protein maturation` at the
  eukaryotic `PTN000259224` SF10 root; `PTN008534753` prunes cytosol from the
  sibling non-SF10 eukaryotic branch. The fungal `PTN000954835` node, seeded by
  SGD `LYS5`, PomBase `lys7`, and *A. fumigatus* `pptA`, adds
  `GO:0009085 L-lysine biosynthetic process`.
- This CGD record currently has only 5 GOA rows: InterPro magnesium ion binding,
  TreeGrafter cytosol, UniProt/ARBA/InterPro/Rhea/EC/PANTHER
  `GO:0008897`, and two CGD no-data placeholders for unknown location and
  biological process.
- The UniProt entry has a by-similarity function note and exact Rhea
  `EC=2.7.8.7` catalytic-reaction line, but no direct *C. glabrata* functional
  publication. Its only literature is the 2004 comparative yeast genome paper.
- Deep research: `just deep-research CANGA LYS5 --provider perplexity` failed
  because the only available deep-research provider in this environment was
  `claude_code`. A manual web/PubMed search for direct `Q6FV34`,
  `CAGL0E05104g`, `Candida glabrata LYS5`, and
  `Candida glabrata phosphopantetheinyl transferase` papers did not surface a
  direct *C. glabrata* LYS5 characterization after the genome paper.
- Ortholog literature: cached PMID:11717270 has full text for the
  *C. albicans* Lys2 activation study and shows that a `lys2` mutant extract
  containing Lys5p activates recombinant Lys2p only with CoA. Cached
  PMID:12892891 is abstract-only but directly reports cloned recombinant
  *C. albicans* Lys5p activating *C. albicans* Lys2p and, cross-species, *S.
  cerevisiae* and *S. pombe* AARs.
