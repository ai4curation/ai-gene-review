# Are the NTCP sodium sites and substrate pocket conserved across the human SLC10 family?

**Headline:** SLC10A4 **retains every side-chain residue NTCP uses to coordinate
sodium**, so its orphan status is **not** explained by degeneration of the
ion-coupling site. This is the falsification of one hypothesis, not a positive
demonstration that SLC10A4 binds sodium or transports anything: the paralogue
models are apo and protein-only, and the ions are NTCP's, carried onto them by
superposition. Its bile-salt pocket is a split result:
the three polar anchors (N103, N262, Q264) are conserved while the hydrophobic
lining diverges, including T203→F281, which introduces a bulky aromatic.
SLC10A7 is the opposite: the sodium site is degenerate (3 of 12 conserved, the
NTCP carboxylate E257→F) *and* all three polar substrate anchors are lost, so it
is unlikely to be an NTCP-type sodium-coupled carrier at all. The myristoyl
(HBV preS1 anchor) pocket is NTCP-specific; no paralogue retains it.

This was run because two reviews in this batch rest on structural claims that
were otherwise only assertions: the SLC10A4 review accepts the uninformative
parent `GO:0022857` partly because "the fold and topology are demonstrably
retained", and the SLC10A7 review records an MF_DARK gap for an unidentified
substrate. The question is narrow and falsifiable: do the paralogues keep the
residues NTCP actually uses?

## Method

```bash
cd genes/human/SLC10A4/SLC10A4-bioinformatics
uv run python fetch_structures.py      # RCSB + AlphaFold DB downloads
uv run python pocket_conservation.py   # writes pocket_conservation.json
```

**1. Sites defined from experiment, not from memory.** Human NTCP/SLC10A1 has
11 cryo-EM entries; the ligand-bearing ones define the sites:

| PDB | Resolution | Ligand | Site |
|---|---|---|---|
| 7ZYI | 2.88 Å | NA ×2 | sodium |
| 9QZQ | 3.11 Å | NA ×2 | sodium |
| 7ZYI | 2.88 Å | CHO ×2 | **bile salt** — CHO is glycochenodeoxycholic acid, a genuine NTCP substrate |
| 8RQF | 3.41 Å | BJU ×1 | N-tetradecanoylglycine = the myristoyl-glycine of the HBV preS1 anchor |

7ZYI also holds 2 cholesterol (CLR) and a water, treated as non-site ligands.

A site is every NTCP residue with a heavy atom within 4.5 Å of a ligand atom,
and each contact is recorded as **side-chain** or **main-chain**. That
distinction changes interpretation: a substitution at a position whose only
contact is a backbone carbonyl is sequence-independent and therefore immaterial.
The NTCP chain is identified in each entry by sequence match to UniProt Q14973
(the entries also contain Fab/nanobody chains), and author numbering was
verified to index directly into the UniProt sequence — 293/293, 286/286, 301/301
— so positions below are UniProt numbering; the script aborts rather than
reporting them if that check fails.

**2. Fold comparison** by TM-align (`tmtools`) against the experimental NTCP
chain. **3. Residue correspondence** by global BLOSUM62 alignment of the full
UniProt sequences.

### Two method errors found and fixed

Both are recorded because each changed a reported number.

- **A geometric correspondence failed its own control.** The first
  implementation paired residues by mutual nearest-neighbour Cα after
  superposition. Put through the pipeline, the AFDB model of SLC10A1 *itself*
  mapped F128 onto G132 — a ~4-residue frame shift — because nearest-neighbour
  pairing slips where helices move between conformational states. Replaced by
  the sequence alignment, which recovers the control exactly (12/12 sodium,
  21/21 bile-salt, 6/6 myristoyl). The geometric result is not reported.
- **A bound ligand was missed.** The first pass took the ligand list from the
  RCSB entry-summary field `nonpolymer_bound_components`, which reports only
  `NA` for 7ZYI. The entry in fact contains two glycochenodeoxycholate
  molecules — the substrate pocket, i.e. the most relevant site for the
  question being asked. The script now enumerates HETATM components from the
  coordinates itself and prints them, so this cannot recur silently.

## Results

AlphaFold DB models (v6) for Q14973, Q12908, Q96EP9, Q3KNW5, Q0GE19.

### Sodium site (9QZQ, 12 positions)

Of these, 5 positions (101, 120, 258, 259, 260) contact sodium through
main-chain atoms only; substitutions there do not change the contact chemistry.

| Protein | identical | conservative | non-conservative | of which main-chain only | TM | RMSD (Å) |
|---|---|---|---|---|---|---|
| SLC10A1 (NTCP) — control | 12 | 0 | 0 | — | 0.973 | 1.09 |
| SLC10A2 (ASBT) | 10 | 1 | 1 | 1 | 0.877 | 2.42 |
| SLC10A4 | 11 | 0 | 1 | **1** | 0.876 | 2.59 |
| SLC10A6 (SOAT) | 11 | 0 | 1 | 1 | 0.879 | 2.73 |
| SLC10A7 | **3** | 5 | 4 | 2 | 0.766 | 3.66 |

**SLC10A4's single substitution is C260→S338, and position 260 is a main-chain
contact — so every side-chain sodium ligand is conserved.** The same applies to
the lone substitution in ASBT and SOAT, both experimentally sodium-coupled, which
is the positive control that makes these numbers mean something.

SLC10A4: `Q68→Q146 G101→G179 S105→S183 N106→N184 S119→S197 I120→I198
T123→T201 E257→E335 T258→T336 G259→G337 C260→S338* Q261→Q339`

SLC10A7: `Q68→T80* G101→P116~ S105→S120 N106→A121* S119→A135~ I120→I136
T123→S139~ E257→F263* T258→T264 G259→P265~ C260→A266* Q261→D267~`
— four non-conservative changes at side-chain-contacting positions, and the
identities matter more than the count: the carboxylate **E257 becomes
phenylalanine**, **N106 becomes alanine**, **Q68 becomes threonine**.

### Bile-salt pocket (7ZYI:CHO, 21 positions)

| Protein | identical | conservative | non-conservative | polar anchors N103 / N262 / Q264 |
|---|---|---|---|---|
| SLC10A1 (NTCP) — control | 21 | 0 | 0 | all three |
| SLC10A2 (ASBT) | 9 | 5 | 6 (1 main-chain only) | N262, Q264 kept; N103→T110 |
| SLC10A4 | 7 | 7 | 6 (1 main-chain only) | **all three kept** |
| SLC10A6 (SOAT) | 6 | 7 | 7 | — |
| SLC10A7 | 5 | 5 | 9 | **all three lost** (N103→V, N262→T, Q264→A) |

The three polar anchors are the defensible reduced set. The remaining 18
positions are an amphipathic hydrophobic wall where L/I/V/M/F interchanges carry
little interpretable meaning, and the bile salt itself is a model fitted into
sterol-shaped density, so the shell as a whole is a weaker diagnostic than the
ion site.

SLC10A4: `L31→V109~ V32→G110* M34→A112* L35→L113 I38→T116* N103→N181 L104→L182
I195→L273~ S199→L277* V202→L280~ T203→F281* S206→T284~ N262→N340 V263→V341
Q264→Q342 S267→T345~ T268→A346~ L287→L365 M290→A368* I291→L369~ L294→S372*`

So SLC10A4 keeps the polar recognition triad but remodels the hydrophobic
lining, with T203→F281 placing a bulky aromatic in the pocket and S199→L277 and
L294→S372 reversing polarity at two positions. ASBT — which *does* transport
bile salts — diverges at a comparable number of positions, which is the direct
demonstration that pocket divergence alone does not predict loss of transport.

### Myristoyl / preS1 pocket (8RQF, 6 positions)

| Protein | identical | conservative | non-conservative |
|---|---|---|---|
| SLC10A1 (NTCP) — control | 6 | 0 | 0 |
| SLC10A2 (ASBT) | 3 | 1 | 2 |
| SLC10A4 | 1 | 2 | 3 |
| SLC10A6 (SOAT) | 3 | 2 | 1 |
| SLC10A7 | 2 | 2 | 2 |

## Independent check against OpenScientist

Two OpenScientist hypothesis jobs were run on the same questions **without**
being given this analysis (the local result is deliberately held out, per the
project's blinded-comparison convention). Reports:
`genes/human/SLC10A4/SLC10A4-hypotheses/structure-na-site-retention/openscientist.md`
and `genes/human/SLC10A7/SLC10A7-hypotheses/structure-translocation-pathway/openscientist.md`.

**They agree on both verdicts.** For SLC10A4 it returned **REFUTED** on the same
grounds — the sodium sphere is retained, the orphan phenotype cannot be
attributed to site degeneration — and independently named N103, N262 and Q264 as
the polar pocket anchors and flagged T203→F281 as the one substitution of
concern. For SLC10A7 it returned **partially supported**, splitting fold
(retained) from carrier identity (refuted), and reached the same conclusion that
the Na1 primary ligand is lost.

Two of its points corrected this analysis and are folded in above: that 7ZYI
contains bound bile salts (which the first pass missed), and that contacts made
through backbone atoms are sequence-independent (which is why SLC10A4's C260→S
is immaterial).

One genuine disagreement, left open: for SLC10A7's Q68, the run reports the
residue as **deleted into an indel**, whereas the alignment here maps it to
T80. Both readings agree the Na1 primary ligand is gone; they differ on whether
by substitution or deletion, which is an alignment-register question that only
an experimental SLC10A7 structure can settle.

## Interpretation, and what this does not show

**For SLC10A4 the hypothesis is refuted.** The proposition was that loss of the
sodium and bile-acid machinery explains why no substrate has been found. The
side-chain ion ligands are retained and the polar substrate anchors are
retained. What that licenses is narrow, and the distinction is the whole point:

- Supported: *SLC10A4's orphan status should not be explained by loss of the
  NTCP sodium-coordinating residues.*
- Not supported: *SLC10A4 has a working sodium site or bile-salt pocket.* A
  protein can keep the ligand set and still fail to transport, through the
  pocket, substrate access, gating, localization, regulation, oligomerization,
  or the coupling between ion and substrate movement.

Two readings remain open: a genuine sodium-coupled carrier whose cargo has not been offered to it,
or a remodelled pocket (T203→F281 and the polarity reversals) with a different
or narrower specificity. The structural argument the SLC10A4 review already
makes — that `GO:0022857` is the honest level and should not be deepened on the
strength of failed substrate screens — is now supported by coordinates rather
than by sequence similarity alone.

**For SLC10A7 the result supports the review independently.** A protein that has
lost both the NTCP carboxylate sodium ligand and all three polar substrate
anchors is unlikely to run NTCP-type symport, which fits a Golgi protein whose
only reported transport assay was negative for bile acids and steroid sulfates.

**Hard limits.** (i) Every paralogue here is a predicted model; only NTCP has
experimental coordinates, and those models are apo — AlphaFold predicted no ion
or ligand for any of them, so every ion and bile salt shown or measured against
is NTCP's own, projected by superposition. A distance from a paralogue side
chain to "the sodium" is therefore a statement about geometric plausibility
after superposition, never a predicted interaction. (ii) A conserved site is not activity and a degenerate
site is not proof of its absence — ASBT's own pocket divergence makes the first
point concretely, and coordination could be rebuilt by residues that do not
align to NTCP's contacts, which is all this inspects. (iii) Contact sets depend
on the 4.5 Å cutoff and on the captured conformational state; the two sodium
entries agree on 7 positions and differ on the rest, which is why both are
reported. (iv) None of this is experimental evidence for a GO annotation: no
review action was changed on it, and it is cited as a `file:` reference
supporting structural premises argued on other grounds. (v) The myristoyl pocket
is **not** the mouse HBV-restriction determinant — mouse Ntcp's restriction maps
to residues 84–87 of the first extracellular loop, which is not among the BJU
contacts — so the two are distinct aspects of receptor function.

## Files

- `fetch_structures.py` — downloads, provenance in `downloads.json`
- `pocket_conservation.py` — site definition, alignment, per-residue calls
- `pocket_conservation.json` — full output, every position, with contact type
- `structures/` — downloaded coordinates (not committed)
