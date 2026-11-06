# sbp-1 review notes

## Session 1 (2026-10-28)

- `just fetch-gene worm sbp-1` resolved Q9XX00 (SRBPH_CAEEL), 32 GOA rows. First attempt hit
  a UniProt 429 rate limit; retry succeeded.
- No deep-research provider available; literature synthesis written by hand in
  `sbp-1-deep-research-manual.md`.
- Full text cached: PMID:15340492 (gene called lpd-1 there), 22035958, 28710073, 33370778,
  35140229. Abstract only: 12530969, 16799563, 19187779, 19632181, 19936816.

### Key judgements

- SBP-1 is a bHLH-Zip transcription factor (SREBP ortholog). MF core = GO:0000981 with
  GO:0000978. The IDA GO:0003700 (Grove 2009, abstract only) is refined to GO:0000981,
  which the gene already carries by IBA.
- Lipid process rows annotated by IMP as direct participation ("fatty acid biosynthetic
  process", "long-chain fatty acid metabolic process", "methyl-branched fatty acid
  biosynthetic process") are re-expressed as *regulation* terms: SBP-1 does no catalytic
  step; it controls transcription of elo-5/elo-6, fat-5/6/7, FAS, ACC etc.
  [PMID:15340492 "suggests that elo-5 and elo-6 are likely to be the targets of lpd-1"].
  Replacements: GO:0045723 positive regulation of fatty acid biosynthetic process;
  GO:1902324 positive regulation of methyl-branched fatty acid biosynthetic process.
- "regulation of gene expression" / "positive regulation of gene expression" refined to
  GO:0045944 (already carried by IMP from PMID:12530969).
- Protein binding (IPI, MDT-15) -> GO:0001223 transcription coactivator binding; MDT-15 is
  the Mediator ARC105/MED15 coactivator [PMID:16799563].
- Locomotion (oleate-rescuable consequence of lipid defects) marked over-annotated;
  growth, anoxia and zinc response kept as non-core. Lifespan (PMID:16799563): abstract
  does not mention lifespan; full text not cached -> UNDECIDED.
- ER membrane (IEA + ISS): consistent with two predicted TM helices and SREBP family
  biology; accepted as the precursor location, but no worm-specific experimental evidence.
- No NEW process terms proposed (CLAUDE.md NEW bar).

## Follow-up: description-source comparison (2026-10-30)

- UniProt FUNCTION names a role in the response to simulated microgravity with MDT-15
  (PubMed:32448509). Checked against the cached abstract [PMID:32448509 "RNAi knockdown of
  sbp-1 or mdt-15 induced a susceptibility to toxicity of simulated microgravity"; "intestinal
  MDT-15 acted upstream of SBP-1 to regulate the response to simulated microgravity"]. The
  claim is accurate, but it is a single RNAi stress-sensitivity study in which SBP-1 acts
  through its usual lipogenic target FAT-6. It is a context for the core MDT-15/SBP-1
  lipogenic activity, not a separate function, so it is not added to the description or as
  an annotation.
