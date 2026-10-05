# SLC10A7 does not retain the NTCP sodium-coordinating residues

**Headline:** of the 12 residues that contact bound sodium in the human
NTCP/SLC10A1 cryo-EM structure 9QZQ, only **3** are conserved in SLC10A7, with
four non-conservative substitutions — including replacement of the NTCP
carboxylate **E257 by phenylalanine** and of **N106 by alanine**. The C-terminal
register is the weak point and the residue identities, not the superposition
distances, carry the argument there: the equivalents of 257 and 261 sit 19-23 Å
from their counterparts, which is alignment uncertainty rather than a measured
displacement. Separately,
all three polar anchors of the NTCP bile-salt pocket are lost (N103→V118,
N262→T268, Q264→A270). The SLC10 fold is still recognisable (TM-score 0.766
against the experimental NTCP chain), but neither the ion-binding chemistry nor
the substrate recognition chemistry is. This is independent structural support for the
review's position that SLC10A7's molecular function must stay at the
substrate-agnostic parent, and against reading it as an NTCP-type sodium-coupled
bile-salt carrier.

## Provenance

This is the SLC10A7 slice of a family-wide analysis; the pipeline, the method
control and the full limits section live with it, in
`genes/human/SLC10A4/SLC10A4-bioinformatics/` (`RESULTS.md`, `fetch_structures.py`,
`pocket_conservation.py`, `pocket_conservation.json`). Nothing is duplicated
here beyond the SLC10A7 numbers.

Sites were defined empirically, as every NTCP residue with a heavy atom within
4.5 Å of a bound ligand: sodium in PDB 7ZYI (2.88 Å) and 9QZQ (3.11 Å),
glycochenodeoxycholate — a conjugated bile salt and genuine NTCP substrate — in
7ZYI, and N-tetradecanoylglycine (the myristoyl-glycine of the HBV preS1 anchor)
in 8RQF (3.41 Å). Each contact is additionally recorded as side-chain or
main-chain, since a substitution at a backbone-only contact is
sequence-independent. Author numbering in all three chains indexes exactly into UniProt
Q14973 (293/293, 286/286, 301/301). SLC10A7 is represented by its AlphaFold DB
v6 model (Q0GE19); it has no experimental structure.

## Result

Sodium site, 9QZQ, 12 positions, NTCP → SLC10A7:

```
Q68→T80*   G101→P116~  S105→S120   N106→A121*  S119→A135~  I120→I136
T123→S139~ E257→F263*  T258→T264   G259→P265~  C260→A266*  Q261→D267~
```

`*` non-conservative, `~` conservative. Totals: 3 identical, 5 conservative,
4 non-conservative. TM-score 0.766, RMSD 3.66 Å.

Family context from the same run (sodium site, identical / conservative /
non-conservative out of 12):

| Protein | id | cons | non-cons | TM | note |
|---|---|---|---|---|---|
| SLC10A1 (NTCP) | 12 | 0 | 0 | 0.973 | method control (AFDB vs its own structure) |
| SLC10A2 (ASBT) | 10 | 1 | 1 | 0.877 | positive control, Na⁺-coupled |
| SLC10A6 (SOAT) | 11 | 0 | 1 | 0.879 | positive control, Na⁺-coupled |
| SLC10A4 | 11 | 0 | 1 | 0.876 | orphan, ligands retained (its one change is a main-chain contact) |
| **SLC10A7** | **3** | 5 | 4 | 0.766 | **site degenerate** |

SLC10A7 is the only human family member whose sodium site is not conserved. The
two paralogues with demonstrated sodium-coupled transport keep it, and even the
orphan SLC10A4 keeps it — which is what makes the SLC10A7 result interpretable
rather than merely a low number.

Bile-salt pocket (7ZYI, glycochenodeoxycholate, 21 positions): SLC10A7 scores 5
identical, 5 conservative, 9 non-conservative, and loses all three polar anchors
(N103→V118, N262→T268, Q264→A270). SLC10A4 keeps all three; ASBT, which does
transport bile salts, keeps two. So SLC10A7 is the only family member to have
lost both the ion site and the substrate recognition triad.

In the myristoyl/preS1 pocket (8RQF, 6 positions) SLC10A7 scores 2 identical,
2 conservative, 2 non-conservative; no human paralogue retains that pocket,
which is NTCP-specific.

## Independent check

An OpenScientist hypothesis job was run on the same question without being given
this analysis (`SLC10A7-hypotheses/structure-translocation-pathway/openscientist.md`).
It returned "partially supported", splitting the fold claim (retained — the
panel/core architecture and a traversable cavity are present) from the
NTCP-type-carrier claim (refuted — the sodium sphere is degraded), which matches
the result above. It differs on one detail, left open here: it reads SLC10A7's
Q68 position as deleted into an indel rather than substituted to T80. Both
readings agree the Na1 primary ligand is gone.

## What this does and does not license

It supports two statements already made in the SLC10A7 review on other grounds:
that the `GO:0022857` parent should not be deepened to a substrate-specific
child, and that the unidentified-substrate gap is real rather than a gap in the
literature search. It also makes the Golgi localization and the negative
bile-acid/steroid-sulfate transport assay structurally coherent.

It is **not** experimental evidence and no review action was changed because of
it. A degenerate site is not proof that no ion is bound — coordination could be
rebuilt by residues that do not align to NTCP's own ligand contacts, which is
all this analysis inspects — and the SLC10A7 coordinates are predicted, not
observed. The decisive experiment remains the one in the review's
`suggested_experiments`: identify the transported solute directly.
