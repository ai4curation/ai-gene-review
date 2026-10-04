# Are the NTCP sodium sites and preS1 pocket conserved across the human SLC10 family?

**Headline:** SLC10A4 **retains** the sodium-coordinating machinery of the SLC10
fold essentially intact (11 of 12 ligand-contacting positions identical to NTCP),
so its orphan status is **not** explained by structural degeneration of the
translocation pathway. SLC10A7 is the opposite case: only 3 of 12 sodium-site
positions are conserved, including loss of the NTCP active-site glutamate
(E257→F), which argues it is not a sodium-coupled carrier of the NTCP/ASBT type.
The myristoyl (HBV preS1 anchor) pocket is NTCP-specific: no other human
paralogue retains it.

This analysis was run because two reviews in this batch rest on structural
claims that were otherwise only assertions: the SLC10A4 review accepts the
uninformative parent `GO:0022857` partly on the grounds that "the fold and
topology are demonstrably retained", and the SLC10A7 review records an MF_DARK
gap for an unidentified substrate. The question asked here is narrow and
falsifiable: do the paralogues keep the residues that NTCP actually uses?

## Method

Reproduce with:

```bash
cd genes/human/SLC10A4/SLC10A4-bioinformatics
uv run python fetch_structures.py      # RCSB + AlphaFold DB downloads
uv run python pocket_conservation.py   # writes pocket_conservation.json
```

**1. Sites defined from experiment, not from memory.** Human NTCP/SLC10A1 has 11
cryo-EM entries; three carry a bound ligand, and those define the sites:

| PDB | Resolution | Ligand | Site |
|---|---|---|---|
| 7ZYI | 2.88 Å | NA (2 copies) | sodium |
| 9QZQ | 3.11 Å | NA (2 copies) | sodium |
| 8RQF | 3.41 Å | BJU (1 copy) | N-tetradecanoylglycine = the myristoyl-glycine of the HBV preS1 anchor |

A site is every NTCP residue with a heavy atom within 4.5 Å of a ligand atom.
The NTCP chain is picked out of each entry by sequence match to UniProt Q14973
(the entries also contain Fab and nanobody chains). Author numbering was
verified to index directly into the UniProt sequence — 293/293, 286/286 and
301/301 residues match — so the positions below are UniProt numbering and the
script aborts rather than reporting them if that check fails.

Sodium-contacting residues recovered: **Q68, Y69, M72, G97, C98, S99, S105,
N106, S119, I120, M122, T123, E257, T258, G259, C260, Q261** (union of 7ZYI and
9QZQ). Myristoyl-pocket residues: **F128, L131, G132, D152, V154, Y156**.

**2. Fold comparison** by TM-align (`tmtools`) of each AlphaFold DB model
against the experimental NTCP chain.

**3. Residue correspondence** by global BLOSUM62 alignment of the full UniProt
sequences.

**A method control decided step 3.** The AFDB model of SLC10A1 itself was put
through the same pipeline. A first implementation derived the correspondence
geometrically, from mutual nearest-neighbour Cα pairs after superposition; it
failed this control, mapping the control model's F128 onto G132 — a ~4-residue
frame shift — because nearest-neighbour pairing slips where helices move between
conformational states. It was replaced by the sequence alignment, which recovers
the control exactly (13/13, 12/12 and 6/6 positions identical). The geometric
result is not reported.

## Results

AlphaFold DB models (v6) for Q14973, Q12908, Q96EP9, Q3KNW5, Q0GE19.

### Sodium site (9QZQ, 12 contacting positions)

| Protein | identical | conservative | non-conservative | TM-score | RMSD (Å) |
|---|---|---|---|---|---|
| SLC10A1 (NTCP) — control | 12 | 0 | 0 | 0.973 | 1.09 |
| SLC10A2 (ASBT) | 10 | 1 | 1 | 0.877 | 2.42 |
| SLC10A4 | **11** | 0 | 1 | 0.876 | 2.59 |
| SLC10A6 (SOAT) | 11 | 0 | 1 | 0.879 | 2.73 |
| SLC10A7 | **3** | 5 | 4 | 0.766 | 3.66 |

SLC10A2 and SLC10A6 are the internal positive controls: both are experimentally
established sodium-coupled transporters, and both conserve the site. That is
what makes SLC10A7's divergence interpretable rather than just a number.

### SLC10A4 — sodium site retained

```
Q68→Q146  G101→G179  S105→S183  N106→N184  S119→S197  I120→I198
T123→T201 E257→E335  T258→T336  G259→G337  C260→S338* Q261→Q339
```
(`*` non-conservative). Only one substitution, C260→S338, and cysteine→serine is
the mildest possible change at that position. Every residue that NTCP uses to
coordinate sodium — including the Q68/N106/S105 cluster and the E257/Q261 pair —
is present in SLC10A4 at the aligned position.

### SLC10A7 — sodium site degenerate

```
Q68→T80*  G101→P116~ S105→S120  N106→A121* S119→A135~ I120→I136
T123→S139~ E257→F263* T258→T264  G259→P265~ C260→A266* Q261→D267~
```
Four non-conservative substitutions at sodium-contacting positions, and the
identity of the losses matters more than the count: the glutamate **E257 is
replaced by phenylalanine**, trading a carboxylate for an aromatic side chain;
the asparagine **N106 becomes alanine**; and **Q68 becomes threonine**. Two
glycines become prolines (G101→P, G259→P), which constrains backbone geometry in
the region. The fold is still recognisably SLC10 (TM 0.766), but the ion-binding
chemistry is not.

### Myristoyl / preS1 pocket (8RQF, 6 positions)

| Protein | identical | conservative | non-conservative |
|---|---|---|---|
| SLC10A1 (NTCP) — control | 6 | 0 | 0 |
| SLC10A2 (ASBT) | 3 | 1 | 2 |
| SLC10A4 | 1 | 2 | 3 |
| SLC10A6 (SOAT) | 3 | 2 | 1 |
| SLC10A7 | 2 | 2 | 2 |

No paralogue retains the pocket. SLC10A4 is the most diverged (F128→L, G132→V,
Y156→L).

## Interpretation, and what this does not show

**For SLC10A4, the hypothesis this analysis set out to test is refuted.** The
proposition was that loss of the sodium and bile-acid machinery explains why no
substrate has been found. It does not: the sodium site is intact. Two readings
remain open — SLC10A4 may be a genuine sodium-coupled carrier whose cargo has
not yet been offered to it, or it may retain the site as an evolutionary relic.
Either way, the structural argument that the SLC10A4 review already makes —
that the uninformative parent `GO:0022857` is the honest level and should not be
deepened on the basis of failed substrate screens — is now supported by
coordinates rather than by sequence similarity alone.

**For SLC10A7, the structural result supports the review's position
independently.** A protein lacking the NTCP carboxylate and amide sodium ligands
is unlikely to run NTCP-type symport, which fits a Golgi protein whose only
reported transport assay was negative for bile acids and steroid sulfates, and
whose annotated biology is calcium homeostasis and glycosylation.

**Hard limits.** (i) These are predicted models for every paralogue; only NTCP
has experimental coordinates. (ii) A conserved site is not activity, and a
degenerate site is not proof of its absence — ion coordination can be
reconstituted by residues this analysis does not consider, since it reports only
positions aligned to NTCP's own ligand contacts. (iii) 4.5 Å contact sets depend
on the chosen cutoff and on which conformational state was captured; the two
sodium entries agree on 7 of their positions and differ on the rest, which is
why both are reported. (iv) Nothing here is experimental evidence for a GO
annotation: no action in any review was changed on the strength of this
analysis, and it is cited as a `file:` reference supporting the structural
premises of arguments made on other grounds. (v) The myristoyl pocket is not the
mouse HBV-restriction determinant — mouse Ntcp's restriction maps to residues
84–87 of the first extracellular loop, which is not among the BJU contacts — so
these are two distinct aspects of receptor function and should not be conflated.

## Files

- `fetch_structures.py` — downloads, with provenance in `downloads.json`
- `pocket_conservation.py` — site definition, alignment, per-residue calls
- `pocket_conservation.json` — full machine-readable output, all positions
- `structures/` — downloaded coordinates (not committed)
