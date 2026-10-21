# erg6 (AFUA_4G03630; UniProt Q4W9V1) notes

## 2026-10-21 de novo review

- `just deep-research-falcon ASPFU erg6` could not run to completion. The sparse
  worktree initially lacked `scripts/` and `templates/`; after those cones were
  added, the provider failed because `agentapi` was absent and no `OPENAI_API_KEY`,
  `EDISON_API_KEY`, `ASTA_API_KEY`, or `PERPLEXITY_API_KEY` was configured.
- PANTHER PTHR44068 places Q4W9V1 in `PTHR44068:SF1`, the fungal Erg6/SMT
  subfamily. `interpro/panther/PTHR44068/PTHR44068-paint.tsv` puts
  `GO:0003838`, `GO:0005783`, and `GO:0016126` on eukaryotic node
  `PTN002226525`, and places the fungal `GO:0006696` term on `PTN000802684`.
  Those node placements agree with the local `genes/yeast/ERG6` and
  `genes/SCHPO/erg6` reviews: Erg6/erg6 is a SAM-dependent sterol
  24-C-methyltransferase in ergosterol biosynthesis.
- The Aspergillus enzyme sits at a different point in the sterol pathway than
  budding-yeast Erg6. UniProt lists the direct reaction as lanosterol + SAM to
  eburicol [UniProt:Q4W9V1 "Reaction=lanosterol + S-adenosyl-L-methionine =
  eburicol + S-adenosyl-L-homocysteine + H(+)"]. Xie et al. directly support
  the pathway block:
  [PMID:38769341 "Repression of A. fumigatus erg6 expression in a conditional
  mutant blocks ergosterol biosynthesis resulting in abundant accumulation of
  lanosterol"]. Elsaman et al. independently use Erg6A depletion and put the
  reaction at the lanosterol-to-eburicol step [PMID:39060235 "Partial repression
  of Erg6A, which converts lanosterol into eburicol, increases azole resistance."].
- The two `GO:0005739 mitochondrion` rows are bad propagation. The seeded ISS row
  and the UniProt SubCell IEA both trace to `UniProtKB:P32352`; the Q4W9V1
  UniProt record makes that explicit for both "Microsome" and "Mitochondrion".
  P32352 is the budding-yeast Erg2 sterol C8 isomerase, not an Erg6/SMT-family
  protein. The direct Aspergillus localization data put Erg6 on lipid droplets:
  [PMID:38769341 "the GFP-labeled puncta overlapped with the red BODIPY staining
  completely"].
- PubMed/NCBI searches for `Aspergillus fumigatus` with `erg6`, `sterol
  24-C-methyltransferase`, `24-SMT`, and eburicol found the older pathway papers
  already cited by UniProt plus the direct 2017 microsomal 24-SMT paper
  [PMID:28224386 "Microsomal 24-SMT activity was assayed in presence of
  α-bisabolol as an inhibitor, lanosterol as a substrate and [methyl-H3]
  AdoMet"]. The newest direct Erg6 papers were the two 2024 Nat Commun studies.
  Later 2025-2026 matches focused on Erg6 regulation or upstream lanosterol
  synthase rather than changing the Erg6 activity/localization call.
