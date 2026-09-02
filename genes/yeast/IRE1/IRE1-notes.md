# IRE1 review notes

## 2026-09-02 Update: nuclear-localization annotation (GO:0005634, IDA, PMID:17035634)

Audited the existing review for oversights. The IDA annotation of GO:0005634 (nucleus)
from PMID:17035634 had been marked `UNDECIDED` with the stated reason "Unable to access
PMID:17035634 to verify the nuclear localization claim." This was incorrect: the
publication is cached in this repository (`publications/PMID_17035634.md`) and its
abstract directly and unambiguously supports the annotation.

Goffin et al. 2006 (Mol Biol Cell) show that Ire1p's cytoplasmic linker region contains
an 18-residue nuclear localization sequence (NLS) recognized by both importin alpha
(Kap60p) and multiple importin beta homologues, that this NLS drives Ran-GTPase-dependent
nuclear import of Ire1p (or an NLS-GFP reporter) in vivo, and that NLS-disrupting point
mutations impair ER-stress-induced HAC1 mRNA splicing:

[PMID:17035634 "The Ire1p transmembrane receptor kinase/endonuclease transduces the
unfolded protein response (UPR) from the endoplasmic reticulum (ER) to the nucleus in
Saccharomyces cerevisiae."]

[PMID:17035634 "This 18-residue sequence is capable of targeting green fluorescent
protein to the nucleus of yeast cells in a process requiring proteins involved in the
Ran GTPase cycle that facilitates nuclear import."]

[PMID:17035634 "The NLS-dependent nuclear localization of Ire1p would thus seem to be
central to its role in UPR signaling."]

Changed the annotation's `action` from `UNDECIDED` to `KEEP_AS_NON_CORE`: the nuclear
pool and NLS-dependent import are real and evidence-backed (so UNDECIDED, reserved for
cases where the evidence genuinely cannot be assessed, was not appropriate), but IRE1's
best-established, defining catalytic activities (kinase trans-autophosphorylation and
HAC1 pre-mRNA endoribonuclease splicing) are ER-membrane events, so nuclear import is
kept as a non-core regulatory/trafficking aspect rather than promoted into
`core_functions`.

All other existing annotations, `core_functions`, and the top-level `description` were
reviewed and found sound and well-supported; no other changes made.
