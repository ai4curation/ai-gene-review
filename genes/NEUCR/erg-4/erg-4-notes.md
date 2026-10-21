## 2026-10-21 de-novo review

Deep research: `just deep-research-falcon NEUCR erg-4` could not generate a
provider file. The first attempt in this sparse worktree failed because
`scripts/deep_research_wrapper.py` was outside the sparse checkout; after adding
`scripts/` and `templates/`, the Falcon wrapper reached `deep-research-client`
but no provider was configured: `agentapi` was not on `PATH` and none of
`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, or `PERPLEXITY_API_KEY` was
set. No `erg-4-deep-research-falcon.md` file was written.

Reviewed local evidence:

- `Q9P3R1` is the Neurospora crassa Erg6/SMT-family sterol 24-C-methyltransferase
  encoded by `erg-4`/`NCU03006` [UniProt:Q9P3R1,
  "Name=erg-4 {ECO:0000303|PubMed:154056}; ORFNames=B24P7.240, NCU03006"].
- The original mutant paper reports that no tested sterol mutant made
  ergosterol and that `erg-4` lacks the C-24 methyltransferase step
  [PMID:154056, "None of the mutants was able to synthesize ergosterol"];
  [PMID:154056, "erg-4 has an inactive C-24 methyl transferase"].
- UniProt curates the Neurospora reaction as lanosterol + SAM -> eburicol,
  rather than the budding-yeast zymosterol + SAM -> fecosterol reaction
  [UniProt:Q9P3R1,
  "Reaction=lanosterol + S-adenosyl-L-methionine = eburicol + S-adenosyl-"].
- `Q9P3R1` is a reviewed `PTHR44068:SF1` member alongside S. cerevisiae ERG6,
  S. pombe erg6, C. albicans ERG6, A. fumigatus erg6, and additional fungal
  sterol C-24 methyltransferases. The PAINT activity/localization node
  `PTN002226525` and fungal process node `PTN000802684` therefore cover the
  Neurospora enzyme, but `GO:0003838` itself is scoped to RHEA:21128,
  zymosterol -> fecosterol, so this review proposes a lanosterol-specific
  molecular-function term for the Neurospora core function.

PubMed/NCBI search notes:

- Searched PubMed/NCBI on 2026-10-21 for `Neurospora crassa erg-4 sterol
  24-C-methyltransferase`, `Q9P3R1 erg-4 Neurospora sterol
  24-C-methyltransferase`, `NCU03006 sterol 24-C-methyltransferase Neurospora`,
  and newer `erg6`/`NCU03006` Neurospora papers.
- No newer paper with a direct Q9P3R1 enzyme assay or localization experiment
  was found.
- The later Neurospora azole-response papers use the yeast-style name `erg6`
  for `NCU03006`, and treat it as an azole-responsive ergosterol-biosynthesis
  gene, but they do not change the direct activity or localization review
  [PMID:23755044, "NCU03006"]; [PMID:29387050, "erg6 (NCU03006, encoding sterol
  C-24 methyl transferase)"]; [PMID:39892608, "the inhibition of ERG11/CYP51
  activated transcription factor NcSR, leading to the upregulation of erg11 and
  erg6"].
- Beware the old and new Neurospora names: recent papers' `erg4`/`Delta erg4`
  rows refer to the C-24(28) sterol reductase `NCU01333`, not to the old `erg-4`
  C-24 methyltransferase locus `NCU03006`.
