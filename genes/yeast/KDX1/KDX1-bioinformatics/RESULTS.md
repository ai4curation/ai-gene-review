# KDX1 motif correspondence to SLT2

Analysis date: 2026-09-20 (local); source retrievals were 2026-09-21 UTC.

**The canonical SLT2 ATP-site Lys54 aligns to Arg54 in KDX1. The neighboring
Lys55 is retained, but it is not the same aligned position as canonical Lys54.**
Thus the earlier statement that KDX1 retains the invariant ATP-site lysine merely
because its UniProt record annotates Lys55 as an ATP-binding residue is not supported
by this comparison.

## Method and provenance

The biological comparator is experimentally characterized SLT2/MPK1, **Q00772**
(UniProt sequence version 2). The target is cached KDX1/MLP1, **P36005**, copied
unchanged from `../KDX1-uniprot.txt`. Exact snapshots, retrieval URLs/timestamps and
SHA256 hashes are in `data/provenance.json`; each computed output independently
records its input and sequence hashes. **P41808 is SMK1**, not SLT2, as its fetched
UniProt header explicitly states.

`compare_sequences.py` uses Biopython 1.85 `PairwiseAligner`, global alignment,
BLOSUM62, gap-open -10, and gap-extension -0.5. The requested SLT2 positions are
passed on the command line. The script reads both sequences, computes the alignment,
and derives target positions/residues from aligned blocks. It does not encode the
expected residue identities. The complete alignment and JSON output are in
`results/slt2-kdx1-alignment.txt` and `results/slt2-kdx1.json`.

## Observed mapping

| Element | SLT2 position/residue | KDX1 position/residue |
|---|---|---|
| Canonical beta3 lysine | K54 | R54 |
| Adjacent lysine | K55 | K55 |
| Catalytic-loop histidine | H151 | H151 |
| Catalytic-loop arginine | R152 | C152 |
| Catalytic-loop aspartate | D153 | D153 |
| DFG aspartate | D171 | N171 |
| Activation-loop threonine | T190 | K190 |
| Activation-loop tyrosine | Y192 | Y192 |

SLT2 positions 47–59 are `EDTTVAIKKVTNV`; KDX1 positions 47–59 are
`EETHVAIRKIPNA`. The alignment places the two beta3 lysines in separate columns:
the first changes to arginine, while the second remains lysine.

The DFG aspartate-to-asparagine change and absence of the aligned activation-loop
threonine are also observed directly. Retention of Tyr192 is compatible with the
reported monophosphorylated Mlp1 mechanism; lack of the canonical dual-phosphorylation
motif does not mean that Mlp1 cannot be phosphorylated.

## Interpretation and limits

The functional importance of SLT2 K54 is independently grounded in
[PMID:20641022](https://pubmed.ncbi.nlm.nih.gov/20641022/), whose full text describes
the catalytically inactive `mpk1-K54R` mutant. The target sequence contains arginine
at that aligned position in addition to the NFG change. Target-specific studies
describe Mlp1 as a pseudokinase with a noncatalytic transcriptional role
([PMID:18268013](https://pubmed.ncbi.nlm.nih.gov/18268013/),
[PMID:35420390](https://pubmed.ncbi.nlm.nih.gov/35420390/)). These observations support
the established inactivity interpretation rather than the claim that a retained
kinase fold proves catalytic function.

This alignment does **not** establish whether KDX1 can bind ATP, exclude every
possible residual phosphotransfer reaction, reconstruct a PAINT node, or establish
orthology on its own. In particular, the adjacent Lys55 annotation is neither proof
nor disproof of nucleotide binding. The comparison only checks sequence-coordinate
claims; ATP binding remains a distinct experimental question.

## Independent input and checks

The same script was run with SMK1 P41808 as the target. It mapped SLT2 K54 to SMK1
K69, demonstrating that target positions are computed rather than assumed equal to
reference positions. All output for this check is retained in
`results/slt2-smk1.json` and `results/slt2-smk1-alignment.txt`. This check is not used
as biological evidence about KDX1.

- [x] Script inputs, coordinate queries and output paths are command-line arguments;
  no sequences, expected residue identities or expected mappings are hardcoded.
- [x] Script was executed successfully on a different target gene (SMK1).
- [x] Both analyses completed and the full alignments and computed mappings were inspected.
- [x] Direct output files and exact input snapshots are retained in this folder.
- [x] Dependency version, alignment parameters, source provenance and biological
  limits are documented.

Reproduce with `just all` from this directory; see [README.md](README.md).
