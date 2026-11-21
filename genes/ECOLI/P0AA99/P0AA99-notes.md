# P0AA99 (dpaA / LdtF / YafK) curation notes

## 2026-11-17 — experimental tether-hydrolase exemplar (PTHR36699:SF1)

P0AA99 is the experimentally characterised exemplar of the YafK/LdtF/DpaA
hydrolase subfamily (PANTHER PTHR36699:SF1) used to ground the hydrolysis step
of the tether-remodeling module. Two independent studies establish its core
activity. It is a murein hydrolase that cleaves Lpp from peptidoglycan
[PMID:33941679, "Here, using genetic and biochemical approaches, we show that
LdtF (formerly yafK), a newly identified paralog of l,d-transpeptidases in E.
coli, is a murein hydrolytic enzyme that catalyzes cleavage of Lpp from the PG
sacculus."], and the independent DpaA study reports the same reaction
[PMID:33947763, "We now show that LdtF hydrolyzes the Lpp-peptidoglycan linkage,
detaching Lpp from peptidoglycan, and have renamed LdtF to peptidoglycan
meso-diaminopimelic acid protein amidase A (DpaA)."]. The core molecular
function is therefore a peptidoglycan L,D-endopeptidase (GO:0061785), with the
precise tether-hydrolysis chemistry still lacking a dedicated GO term.

## Carboxypeptidase activity: a narrow Gly-specific activity, not the classical ld-CPase

The GO:0004180 carboxypeptidase annotation needs care, because the two words
"carboxypeptidase activity" cover two different reactions in the DpaA papers:

- DpaA does **not** have the classical ld-carboxypeptidase activity (removal of a
  terminal d-Ala): PMID:33947763 reports "DpaA did not show any ld-TPase or
  ld-CPase activity under any condition tested, despite a long incubation time
  (12 h)", and separately that "E. coli DpaA was not able to remove terminal
  d-alanine residues from PG stem peptides".
- DpaA **does** have a narrow meso-Dpm-Gly carboxypeptidase activity, removing a
  terminal glycine from TetraGly4 muropeptides: PMID:33947763, "These structures
  were hydrolyzed by DpaA particularly under acidic conditions via a meso-Dpm-Gly
  CPase activity." PMID:33941679 reports the same: "LdtF also exhibits
  glycine-specific carboxypeptidase activity on muropeptides containing a terminal
  glycine residue."

So the EcoCyc IDA for GO:0004180 keyed to PMID:33947763 is **correct** — the
Gly-specific CPase is demonstrated in that paper. There is no wrong-reference
source defect here; the "no ld-CPase" statement and the "meso-Dpm-Gly CPase"
statement are about different substrates and are not contradictory. The CPase is
kept as a non-core secondary activity of the exemplar; it is NOT generalised to
uncharacterised family members (see the PTHR36699 family review, where GO:0004180
is SUBFAMILY_ONLY, and the PP_1451 / PA14 LdtPae3 reviews, which mark it
over-annotated).

## Mechanistic note

DpaA lacks the active-site arginine conserved in true L,D-transpeptidases, which
the authors link to its hydrolytic (rather than transfer) activity; it also shows
no L,D-transpeptidase activity. The InterPro2GO mapping IPR005490 → GO:0016740
transferase activity is therefore wrong for DpaA (a pure hydrolase), and that row
is REMOVEd in the review.
