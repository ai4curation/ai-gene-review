# PP_2482 curation notes

## 2026-07-20 OpenScientist report assessment

The generated OpenScientist report is retained unchanged as provider output but is
assessed as `MISCITED` for target-level curation. It declares Q88K11 canonical MoaA,
assigns exact GTP 3',8'-cyclase activity, and calls PP_2482 an essential,
nonredundant gate despite the distinct reviewed canonical KT2440 MoaA Q88E69 and
the unresolved PP_2482/PP_1969 paralog relationship. It also presents unsaved
residue, motif, and neighborhood analyses as decisive evidence. Those claims are
not propagated.

The conservative decision is unchanged: Q88K11 is a divergent MoaA-like
radical-SAM candidate whose physiological substrate, exact catalytic activity, and
necessity remain `UNDECIDED`. This conclusion is grounded in the target UniProt
record and the saved local sequence comparison; the provider report contributes
only its explicit statement that no direct PP_2482 experiment was found.

## 2026-10-15 Re-review of GO:0061798 after OpenScientist control batch

A blinded OpenScientist hypothesis run (batch openscientist-controls-2026-10-14,
local bioinformatics withheld) judged GO:0061798 supported
[file:PSEPK/PP_2482/PP_2482-hypotheses/function-hypothesis-go-0061798/openscientist.md,
"**Verdict: SUPPORTED.** The propagated GO:0061798 annotation is correct and at the appropriate granularity for PP_2482."].

Checked against repository data:

- UniProt Q88K11 carries PTHR22960:SF0, PF06463 and IPR010505, the same PANTHER
  subfamily as reviewed Q88E69.
- The run's cluster cysteines (C21/C25/C28, C253/C256/C270) match the local motif
  table in `genes/PSEPK/moaA/moaA-bioinformatics/moaA_features.tsv` (21; 25;253).
- The site mapping in `genes/PSEPK/PP_1969/PP_1969-bioinformatics/` (covers both
  paralogs) finds all seven GTP, four SAM and six cluster positions of Q88E69
  identical in Q88K11, except V266, which is Leu as in E. coli MoaA
  [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "The divergence of PP_1969 and PP_2482 from canonical KT2440 MoaA does not touch the annotated GTP-, SAM- or cluster-binding residues."].
- Run errors not imported: it says UniProt annotates binding sites at 21/25/28,
  but the Q88K11 record has no FT BINDING lines; and it calls PP_2483 a MocA,
  whereas the local MobA-like comparison finds PP_2483 closer to E. coli MobA
  despite its K07141 KO.

Decision: GO:0061798 UNDECIDED -> ACCEPT; GO:0006777 UNDECIDED -> ACCEPT (follows
from the activity); GO:0003824 UNDECIDED -> TOO_GENERAL. GO:0061799 stays REMOVE.

Not verified / leads only: the run's literature (PMID:25941396, PMID:30097104,
PMID:26575208, PMID:35480226, PMID:41183211) is not cached; AlphaFold pLDDT values
were not re-run. Paralog division of labour remains unknown.
