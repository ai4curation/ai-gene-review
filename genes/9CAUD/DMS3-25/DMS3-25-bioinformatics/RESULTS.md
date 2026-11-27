# DMS3-25 (A0SMN5): is it the Rip1 defence protein or the phage ring that activates Rip1?

## Question

PMID:41639445 (Patel et al., Nature 2026) describes Rip1, a 164-residue
prophage-encoded antiphage defence protein that is activated by the portal or
small terminase ring of an infecting phage and then assembles into a
membrane-disrupting pore. Two roles are therefore described in that paper, on
opposite sides of the defence: the defence protein itself, and the phage
assembly proteins that trigger it.

GOA carries two CACAO rows putting GO:0051607 defense response to virus on
A0SMN5 (DMS3-25, Pseudomonas phage DMS3) from this paper, with the qualifier
`acts_upstream_of_or_within_positive_effect`. That qualifier is right for the
triggering phage ring and wrong for the defence protein, so which of the two
A0SMN5 is decides whether the qualifier is correct. The cached publication is
abstract-only and the paper's abstract does not name DMS3, so the question was
settled from sequence and genome context instead.

## Methods

- `sequences.fasta` holds three sequences, each verbatim from its source:
  A0SMN5 (175 aa) copied from `../DMS3-25-uniprot.txt`, and the two chains of
  PDB 9OOX fetched from `https://www.rcsb.org/fasta/entry/9OOX`. 9OOX is the
  cryo-EM structure published in PMID:41639445: *Escherichia* phage HK446 Rip1
  (164 aa, chains L-W) bound to *Enterobacteria* phage T6 small terminase
  (chains A-K). The two chains are thus the defence protein and the activating
  ring, from the paper itself. The HK446 Rip1 chain corresponds to UniProt
  K7P861 (164 aa, `Uncharacterized protein`), identified by matching the
  `CAQCYESSVKSILQ` motif against all 60 HK446 entries in UniProtKB; the PDB
  construct differs from the native sequence only at residue 2 (G for S).
- `align_rip1.py` aligns A0SMN5 against each chain with Biopython's
  `PairwiseAligner` (global, BLOSUM62, gap open -11, extend -1) and lists the
  CxxC motifs of each sequence. Run with `uv run --with biopython python
  align_rip1.py`; output captured in `align_rip1.out`.
- Gene neighbourhood and strand read from the DMS3 reference genome
  NC_008717.1 feature table (NCBI efetch).

## Results

| comparison | alignment score | identity |
|---|---:|---|
| A0SMN5 vs 9OOX_2 (HK446 Rip1, defence protein) | 176.0 | 48/156 = 30.8% |
| A0SMN5 vs 9OOX_1 (T6 small terminase, activating ring) | -65.0 | 22/153 = 14.4% |

A0SMN5 aligns to Rip1 over its entire length with a positive score, and the
alignment is anchored by three co-linear blocks: the central helix
(`KRWEQEKERYQLH` against Rip1 `SKWEEEKKNYEMH`), the following
`GGLVYRIKP` against `VATVVYRLKK`, and the C-terminal cysteine module
(`ICADCYQKGIKTILQ` against `LCAQCYESSVKSILQ`, then `KCHPCN` against
`RCHRCN`). Both proteins carry exactly two CxxC motifs in that module and no
others: A0SMN5 `CADC`/`CHPC`, Rip1 `CAQC`/`CHRC`. The T6 small terminase has no
CxxC motif at all and its alignment to A0SMN5 scores negative, i.e. worse than
not aligning.

Genome context agrees. In NC_008717.1, A0SMN5 is `complement(12769..13296)`,
transcribed divergently from the head-DNA-packaging operon that runs beside it
on the forward strand (DMS3-26 terminase large subunit 13295..14947; DMS3-27
portal protein 14957..16537). A small terminase gene sits in-operon upstream of
the large subunit, which DMS3-25 does not; an accessory gene inserted in the
opposite orientation inside a structural module is the classic arrangement of a
prophage moron, which is what a prophage-encoded defence gene is. DMS3 forms
lysogens of *Pseudomonas aeruginosa* PA14 [PMID:18952788], so a DMS3 gene is a
prophage gene in the sense the Rip1 paper uses.

## Conclusion

A0SMN5 / DMS3-25 is a homologue of the Rip1 defence protein, not of the
activating phage ring. It is therefore the protein that executes the defence
response, and the GOA qualifier
`acts_upstream_of_or_within_positive_effect` on its GO:0051607 rows is wrong;
`involved_in` is correct.

Two limits on this conclusion. The identity is 30.8%, which establishes
homology and the family assignment but not that every mechanistic detail
reported for HK446 Rip1 holds for the DMS3 protein; and none of this is a
substitute for the paper's own DMS3 experiments, which the two IMP rows
(ECO:0001175 deletion mutation phenotypic evidence, ECO:0007089
loss-of-function mutant phenotype evidence) indicate exist but which could not
be read, the Nature full text being paywalled and absent from PMC and Europe
PMC.
