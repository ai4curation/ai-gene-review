# pvdO (PA2390, Q9I185) — review notes

Reviewed alongside `pvdN` and `pvdP` to fill the periplasmic-maturation segment of the
pyoverdine pathway.

## What is established

284 residues, `PE   1: Evidence at protein level`, and a genuine formylglycine-generating-enzyme
fold: `Pfam PF03781 FGE-sulfatase`, `IPR005532 SUMF_dom`, `IPR051043
Sulfatase_Mod_Factor_Kinase`, with six `FT BINDING` features whose ligand is `Ca(2+)` — the
metal site of that fold. There is also a dedicated NCBIfam,
`[file:PSEAE/pvdO/pvdO-uniprot.txt "DR   NCBIfam; NF051459; pyoverdine_PvdO; 1."]`

Its role in the pathway is the **final oxidation of the chromophore**:

`[PMID:30386787 "a mutant strain lacking the putative oxidoreductase PvdO produced the dihydropyoverdines, indicating that PvdP catalyzes only the initial hydroxylation and first oxidation, whereas the final oxidation depends on PvdO"]`

and it sits in the maturation operon:
`[PMID:30386787 "Three of these periplasmic enzymes, PvdM, PvdN, and PvdO, are usually encoded in an operon."]`
`[PMID:30386787 "Interposon mutagenesis of the corresponding genes in P. aeruginosa indicated essential roles of these genes in pyoverdine biosynthesis"]`

So the three `GO:0002049` IMP rows are `ACCEPT`.

## `GO:0120147` formylglycine-generating oxidase activity

An IBA from `PTN001139750`, whose donors include human SUMF1 (`Q8NBK3`) and a mouse entry —
the sulfatase-maturating clade. The fold inference is sound: PvdO really is an FGE-domain
protein with the Ca²⁺ site.

What does not transfer is the **specific reaction**. Formylglycine-generating oxidase activity
is the oxidation of a cysteine to formylglycine in the active site of a *sulfatase*. PvdO's
demonstrated role is oxidising dihydropyoverdine — a siderophore, not a sulfatase — and the
review calls it a "putative oxidoreductase" rather than an FGE. No formylglycine-generating
activity has been assayed for this protein.

`MARK_AS_OVER_ANNOTATED` rather than `REMOVE`: the term is not entirely wrong, because the fold
and the oxidative chemistry class are right and the mechanism may well be homologous, and
removing it would overrule a PAINT node judgement on a protein whose activity nobody has
measured. But it names a substrate PvdO does not act on, so it overstates what is known.

GO has no term for the chromophore-oxidation step PvdO actually performs. That is recorded as a
question rather than proposed as a new term: the review's own language is "putative
oxidoreductase" and "the final oxidation", which is not a precise enough reaction to write a
definition from. Two new terms are already proposed elsewhere in this campaign; a third on
weaker ground would be worse than a recorded gap.
