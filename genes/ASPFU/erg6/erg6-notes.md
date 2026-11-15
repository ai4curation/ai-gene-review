## 2026-11-06 de-novo review

Deep research via `just deep-research-falcon ASPFU erg6 --fallback perplexity-lite`
failed in this worktree: `falcon` was unavailable because `agentapi` was not on
`PATH`, and the fallback provider was also unavailable. No
`erg6-deep-research-falcon.md` or `erg6-deep-research-perplexity-lite.md` file
was written, so this review used PubMed/web search, cached publications,
UniProt, and the PTHR44068 family review directly.

Reviewed local evidence:

- `Q4W9V1` is the reviewed A. fumigatus Af293 Erg6/SMT-family sterol
  24-C-methyltransferase encoded by `erg6`/`AFUA_4G03630` [UniProt:Q4W9V1,
  "Name=erg6 {ECO:0000303|PubMed:16110826}; ORFNames=AFUA_4G03630"].
- UniProt curates the exact A. fumigatus Erg6 reaction as lanosterol + SAM to
  eburicol [UniProt:Q4W9V1, "Reaction=lanosterol +
  S-adenosyl-L-methionine = eburicol + S-adenosyl-"].
- Xie et al. 2024 is the key primary paper. It generated tetracycline-repressible
  and inducible `erg6` mutants, showed severe growth/viability defects when
  `erg6` was repressed, measured ergosterol depletion with lanosterol
  accumulation after `erg6` repression, and localized native Erg6-GFP to
  BODIPY-positive lipid droplets [PMID:38769341, "Repression of A. fumigatus
  erg6 expression in a conditional mutant blocks ergosterol biosynthesis
  resulting in abundant accumulation of lanosterol, the proposed substrate of
  Erg6."]; [PMID:38769341, "This finding indicated that Erg6-GFP co-localized
  with lipid droplets in actively growing hyphae."].
- Birstonas et al. 2025 identifies the sterol/azole transcription factor RttA.
  Loss of RttA reduces `erg6` expression and accumulates lanosterol, supporting
  the same A. fumigatus pathway placement from an independent regulatory
  perturbation [PMID:40937856, "In agreement, the lack of rttA led to a
  substantial accumulation of the Erg6 substrate lanosterol."].
- `Q4W9V1` is a reviewed `PTHR44068:SF1` member alongside S. cerevisiae ERG6,
  S. pombe erg6, C. albicans ERG6, and Neurospora erg-4. The PAINT
  `PTN002226525` sterol-SMT node supports the `GO:0003838` and ER IBAs, and
  `PTN000802684` supports the fungal ergosterol-biosynthesis IBA for Aspergillus.

PubMed/web search notes:

- Web and PubMed searches on 2026-11-06 for A. fumigatus `erg6`,
  `AFUA_4G03630`, and sterol C-24 methyltransferase found no 2026 paper that
  supersedes the direct 2024 Erg6 genetics/localization study.
- The 2025 RttA paper is newer and useful for regulatory context, but it treats
  Erg6 as the established lanosterol C-24 methyltransferase rather than
  changing its core activity.
- The broad viability, virulence, and azole phenotypes in PMID:38769341 and
  PMID:40937856 were not proposed as new GO process annotations: they follow
  from Erg6-dependent sterol composition rather than from Erg6 directly executing
  growth, virulence, or stress-response programs.
