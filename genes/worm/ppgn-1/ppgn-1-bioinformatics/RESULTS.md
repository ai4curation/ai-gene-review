# ppgn-1 (G5EDB6) — catalytic motif analysis

## Question

The GO annotations for ppgn-1 (Y38F2AR.7, *C. elegans* paraplegin subfamily) are all
IBA/IEA — propagated from the m-AAA protease family, with no *C. elegans* experimental
support. A legitimate worry for any family propagation is that the target is a
**pseudoenzyme**: a fold-retaining paralog that has lost the catalytic residues (cf.
human AFG3L1P pseudogene, or the peptidase-dead YME1L variants). If ppgn-1 had lost its
Walker A/B or HExxH residues, the enzymatic annotations (metalloendopeptidase, ATP
binding, ATP hydrolysis, ATP-dependent peptidase) would be over-annotations for this
specific protein even though they are correct for the family.

## Method

`analyze_motifs.py` parses the amino-acid sequence directly from `../ppgn-1-uniprot.txt`
(nothing hard-coded) and scans for the three diagnostic motifs of an m-AAA protease:

- **Walker A / P-loop** (`G-x(4)-G-K-[S/T]`) — binds the β/γ phosphates of ATP.
- **Walker B** (`hhhh-D-E`) — the Asp/Glu that coordinate Mg²⁺ and activate water for ATP hydrolysis.
- **HExxH** — the M41/FtsH zinc-binding catalytic motif (two His coordinate the catalytic Zn²⁺; the Glu polarises the attacking water).

Run with `uv run python analyze_motifs.py`.

## Result (reproducible)

```
length: 747 aa
Walker A (P-loop, ATP binding):            FOUND at 325 -> GPPGCGKT
Walker B (Mg-ATP hydrolysis):              FOUND at 380 -> IIYIDE
HExxH (M41 zinc-binding catalytic motif):  FOUND at 555 -> HEAGH
HExxH context [555..589]: HEAGHALVGWMLEHTDALLKVTIIPRTSAALGFAQ
```

All three catalytic elements are intact and in the expected order (AAA+ ATPase module
N-terminal, M41 peptidase module C-terminal), consistent with the domain architecture
UniProt/InterPro annotate (AAA+ core IPR003959; Peptidase M41 IPR000642). The HExxH lies
within the M41 domain and is followed downstream by an acidic residue (…MLEHT**D**),
consistent with a complete FtsH-type Zn²⁺ active site.

## Interpretation

At the sequence level ppgn-1 is a **catalytically competent** m-AAA protease subunit, not
a degenerate pseudoenzyme: it retains the residues required for both ATP binding/hydrolysis
and zinc-dependent peptide-bond cleavage. This supports (for this specific protein, not
merely by family membership) the molecular-function annotations `ATP binding`,
`ATP hydrolysis activity`, `metalloendopeptidase activity`, and `ATP-dependent peptidase
activity`.

## Caveats / what this does NOT show

- Motif presence proves catalytic *potential*, not that the enzyme is active *in vivo*,
  what its physiological substrates are, or which partner subunit(s) it assembles with.
- It does not establish whether ppgn-1 is catalytically required in a complex or serves a
  more structural role alongside the *C. elegans* AFG3L2-type subunit (spg-7). Mammalian
  m-AAA complexes tolerate one catalytically dead subunit within an otherwise active
  hexamer.
- Sub-mitochondrial topology (matrix-facing catalytic domains flanked by two TM helices)
  is inferred from UniProt Phobius predictions, not experimentally mapped here.
