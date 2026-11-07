# AIGR paper: agentic review uncovers systematic errors in knowledge bases

Build: `make` (extracts corpus tables into `data/` (git-ignored, ~1.5 min), regenerates
`generated/` macros and tables and `figures/`, then runs latexmk). `make refresh` re-extracts.

**Rule:** every corpus number in the text is a macro from `generated/stats.tex` or a table
from `generated/tab_*.tex`, produced by `scripts/compute_stats.py`. Numbers taken from
project pages are marked `\proj{...}` and must be re-derived by a script before submission.

## Outline

2. How annotations are made: EXP vs IBA vs IEA (and TAS/NAS/ISO/ND)
3. The agentic review system: document, action vocabulary, guardrails, gene selection
4. Corpus-wide results: actions by evidence class, code, IEA pipeline, aspect, taxon
5. Eleven deep dives (one file each in `sections/deepdives/`): readout-to-function distance;
   IBA and bad seeds; projection to non-model taxa; keywords and the SPKW retirement; domain
   mappings and TFs; pseudoenzymes and complex subunits; enzyme specificity; sign errors;
   term obsoletion; evidence trail; wrong entity. Protein binding is a Methods note.
6. Discussion, Methods, Supplement

## Open decisions
- Agent accuracy: expert adjudication of a stratified sample (needed for the title's claim)
- Gene selection is not random: stratify results by campaign type
- Promote 'predictors inherit the errors' (eggNOG, BioReason, ProtNLM) from Discussion to a
  12th deep dive? Other alternates: ND/dark proteome, organelles/CC, whole-proteome P. putida
- Extrapolate per-pipeline rejection rates to current UniProt-GOA volumes
- Target venue and length (main text vs supplement split of deep dives)
