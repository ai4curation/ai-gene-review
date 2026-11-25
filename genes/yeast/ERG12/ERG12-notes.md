# ERG12 (YMR208W) notes

UniProt P07277; mevalonate kinase, EC 2.7.1.36; GHMP kinase family; cytosolic [UniProt:P07277].

## Evidence journal
- Gene/enzyme: [PMID:1645230 "The nucleotide sequence of the ERG12 gene, encoding mevalonate kinase, from Saccharomyces cerevisiae is presented."]; identical to RAR1; feedback: [PMID:1645230 "its sensitivity to FFP could be a key regulatory mechanism in the sterol pathway of yeast"].
- Activity at native levels: [PMID:16477420 "This method has been successfully applied to S. cerevisiae strains containing a wild type level of mevalonate kinase."]
- Genetics: [PMID:200835 "phosphomevalonic kinase (erg 8), mevalonic kinase (erg12)"] ergosterol auxotrophs.
- Localisation: cytoplasm/nucleus (Huh 2003 GFP), cytosol (SWAT, PMID:26928762) [UniProt:P07277 "Cytoplasm, cytosol"].

## Decisions
- The PAINT IBAs from `PTN000048555` for mevalonate kinase activity, cytosol, and IPP
  biosynthesis via mevalonate are sound: ERG12 is in the single PTHR43290 mevalonate-kinase
  subfamily and retains the EC 2.7.1.36 reaction.
- The fungal `PTN000825284` ergosterol-biosynthesis IBA is sound for budding yeast; the
  PAINT node is seeded by S. cerevisiae ERG12, and Karst & Lacroute show that erg12 mutants
  are ergosterol auxotrophs lacking mevalonate kinase.
- The broad Huh 2003 and InterPro2GO cytoplasm rows should be refined to the cytosol
  already supported by SWAT, PAINT, UniProtKB-SubCell, and YeastPathways rows.
- The broad isoprenoid biosynthetic process rows are true but too general beside Erg12's
  direct `GO:0019287` mevalonate-to-IPP role.
- ATP binding, Mg2+ binding (ISS from rat MVK) and nucleus HDA are KEEP_AS_NON_CORE.

## 2026-10-31 rescue

- The original `codex/erg12-yeast-20261024` worktree had been left on an obsolete
  `origin/main` base with only truncated generated cache CSVs modified. The cache changes
  were discarded and the review branch was fast-forwarded to current `origin/main`.
- `just fetch-gene yeast ERG12` and `just fetch-gene-pmids yeast ERG12` found no GOA,
  UniProt, or publication-cache changes.
- Newer searches found metabolic-engineering uses of ERG12, but no post-2024 paper that
  changes the native mevalonate kinase, cytosol, IPP-biosynthesis, or ergosterol-biosynthesis
  calls in the cached evidence.
