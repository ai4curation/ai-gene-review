# Q7VZI5 (BP0922) — PTHR43709 comparison (2026-10-21)

Script: `compare_prpf_family.py` (run with `uv run --script compare_prpf_family.py`);
raw output in `results.json`. Sequences and PANTHER/NCBIfam cross-references were
fetched live from UniProt REST. Identity is from a global BLOSUM62 alignment,
counted over the shorter sequence.

## Percent identity of Q7VZI5 to PTHR43709 members

| Accession | Protein | PANTHER SF | NCBIfam | % id to Q7VZI5 |
|---|---|---|---|---|
| Q7VW94 | B. pertussis BP2370, prp-operon PrpF | SF2 | TIGR02334 | 36.1 |
| Q8EJW4 | S. oneidensis PrpF (characterised) | SF2 | TIGR02334 | 36.8 |
| Q937N7 | C. necator PrpF | SF2 | TIGR02334 | 36.6 |
| Q0QLE6 | E. barkeri Mii, 3-methylitaconate isomerase (characterised) | SF2 | - | 43.7 |
| A0A0U2X0E4 | U. maydis Adi1, aconitate delta-isomerase | SF2 | - | 35.5 |
| O07931 | B. subtilis YraM | SF2 | - | 39.2 |
| P0AAV8 | E. coli YbhH | SF3 | NF033377 | 39.4 |
| Q0KJL4 | Novosphingobium LigU, oxalomesaconate delta-isomerase | SF3 | NF033377 | 44.8 |
| Q88JY0 | P. putida GalD, 4-oxalomesaconate tautomerase | SF3 | NF033377 | 44.3 |

The three PrpF proteins (TIGR02334 matches) are 78-80% identical to one another,
including the B. pertussis prp-operon paralog BP2370. Q7VZI5 is about 36% identical
to all of them and does not match TIGR02334. Its identity to every characterised
member of the family, in either subfamily, falls between 35% and 45%, with no clear
nearest neighbour. Mii is at 43.7%, and LigU and GalD (SF3) are at 44-45%.

## Active-site residues of S. oneidensis PrpF mapped onto each sequence

These are PrpF Lys73, Cys107, Lys281 and His317, which contact trans-aconitate in the
PrpF crystal structure (PMID:17567742).

| Accession | K73 | C107 | K281 | H317 |
|---|---|---|---|---|
| Q7VZI5 | K65 | C99 | **R266** | H301 |
| Q7VW94 | K70 | C104 | K278 | H314 |
| Q0QLE6 (Mii) | K62 | C96 | **M263** | H300 |
| SF3 members | K | C | K | H |

The proposed catalytic Lys/Cys pair is conserved across the family, Q7VZI5 included.
This is consistent with a DapF-fold isomerase. One carboxylate-binding lysine is an
arginine in Q7VZI5 and a methionine in Mii. The family keeps the catalytic machinery
but varies its substrate-binding residues.

## Genomic context (UniProt REST, proteome UP000002676)

- B. pertussis carries a canonical prp cluster: BP2368 prpC, BP2369 aconitate
  hydratase (AcnD-type), BP2370 PrpF (TIGR02334), BP2371 prpD.
- BP0922 sits in a different cluster. Its neighbours are BP0918 (MmgE/PrpD-family
  protein), BP0919 (succinate-semialdehyde dehydrogenase), BP0920 (exported
  FAD-binding protein), BP0921 ("citrate utilization protein B"), BP0923
  ("phosphosulfolactate synthase"-like), BP0924 (transcriptional regulator) and BP0925
  (fumarylacetoacetate-family hydrolase).

## Interpretation

- Q7VZI5 is not the PrpF ortholog of B. pertussis. BP2370 is. Q7VZI5 is a divergent
  paralog inside PTHR43709:SF2, a subfamily that also contains enzymes with different
  substrates (PrpF, Mii, Adi1).
- Nothing in these data assigns a substrate. A methylitaconate delta-isomerase
  (Mii-like) activity cannot be transferred, because 43.7% identity sits within the
  same range as the unrelated SF3 tautomerases. Propionate catabolism cannot be
  transferred either, because the methylcitrate-cycle isomerase role belongs to BP2370.
- What is supported is a family-level activity: an isomerase of the DapF fold with
  the conserved catalytic Lys/Cys pair. The substrate is unknown.
- Limitations: this is pairwise analysis only. No tree was built and no PAINT node
  placement was inspected for Q7VZI5.

## Hydropathy of Q7VZI5

Kyte-Doolittle, 19-residue window: the maximum over the whole sequence is 1.52 and
the maximum over the first 40 residues is 0.55. No window passes the usual
transmembrane threshold of about 1.6, and the N-terminus is not hydrophobic. There is
no sign of a signal peptide or a transmembrane segment. That fits a soluble protein,
in the same way the soluble, crystallised PrpF protein of S. oneidensis is one. This
is a crude screen, not SignalP or Phobius.
