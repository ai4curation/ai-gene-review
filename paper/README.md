# AIGR paper: agentic review uncovers systematic errors in knowledge bases

Build: `make` (extracts corpus tables into `data/` (git-ignored, ~1.5 min), regenerates
`generated/` macros and tables and `figures/`, then runs latexmk). `make refresh` re-extracts.

**Rule:** every corpus number in the text is a macro from `generated/stats.tex` or a table
from `generated/tab_*.tex`, produced by `scripts/compute_stats.py`. Numbers taken from
project pages are marked `\proj{...}` and must be re-derived by a script before submission.

## Outline
1. Introduction: knowledge bases as infrastructure; write-once, read-rarely; errors are systematic
2. How annotations are made: EXP vs IBA vs IEA (and TAS/NAS/ISO/ND)
3. The agentic review system: document, action vocabulary, guardrails, gene selection
4. Corpus-wide results: actions by evidence class, code, IEA pipeline, aspect, taxon
5. Ten deep dives (one file each in `sections/deepdives/`)
6. Discussion, Methods, Supplement

## Open decisions
- Agent accuracy: expert adjudication of a stratified sample (needed for the title's claim)
- Gene selection is not random: stratify results by campaign type
- Deep-dive line-up (alternates: ND/dark proteome, organelles/CC, ML predictors trained on
  errors, FliI/SctN conserved-function recovery, whole-proteome P. putida)
- Extrapolate per-pipeline rejection rates to current UniProt-GOA volumes
- Target venue and length (main text vs supplement split of deep dives)
