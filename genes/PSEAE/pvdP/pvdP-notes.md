# pvdP (PA2386, Q9I188) — review notes

Reviewed to fill the pyoverdine periplasmic-maturation segment, which the
`pseudomonas_pyoverdine_precursor_supply` module explicitly scopes out and which blocks
building a maturation module.

## The cleanest gene of the four

544 residues, and everything agrees:

- `[PMID:24816606 "is a tyrosinase required for the maturation of the pyoverdine chromophore"]`
- `[PMID:24816606 "PvdP converts the nonfluorescent ferribactin, containing two iron binding groups, into a fluorescent pyoverdine"]` — by three consecutive oxidations.
- `[PMID:24816606 "capable of acting on large peptidic substrates"]` — it is the founding member of a tyrosinase family acting on peptides rather than free tyrosine.
- The record carries a **di-copper centre** (`Di-copper_centre_dom_sf`) with six `FT BINDING`
  features whose ligand is `Cu(2+)` — the canonical tyrosinase active site.
- A dedicated NCBIfam, `[file:PSEAE/pvdP/pvdP-uniprot.txt "DR   NCBIfam; NF051454; tyrosinase_PvdP; 1."]`
- `PE   1: Evidence at protein level`.

So `GO:0004503 tyrosinase activity` (IDA) is `ACCEPT` as the core function, and all four
`GO:0002049` rows `ACCEPT`.

## One `NEW` row: the periplasm

pvdP has **no cellular-component annotation at all**, which is a gap rather than a judgement
call, because the compartment is where the whole point of the pathway lies — maturation happens
after export. Two independent lines agree:

- `[PMID:24816606 "a periplasmic enzyme of previously unknown function"]`
- The record carries a **Tat signal peptide** —
  `[file:PSEAE/pvdP/pvdP-uniprot.txt "DR   NCBIfam; TIGR01409; TAT_signal_seq; 1."]` and
  `IPR019546 TAT_signal_bac_arc` — and the Tat system exports folded proteins to the periplasm.

Added as `GO:0030288 outer membrane-bounded periplasmic space`, coded `IC`: an inference drawn
from the author statement plus the targeting signal rather than from a localisation experiment
on this protein. The sibling `pvdN` carries the same term by IDA, which is the comparator.

A pleasing cross-connection: the Tat signal means PvdP is a Tat substrate, and `tatB`, reviewed
in batch 4, is a subunit of the translocase that exports it. The paper behind `tatB`'s IMP rows
(PMID:16621825) is a pyoverdine paper for exactly this reason — tat mutants make no pyoverdine
because the maturation enzymes never reach the periplasm.
