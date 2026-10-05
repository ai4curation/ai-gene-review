# olfm3a / olfm3b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/olfm3a/olfm3a-bioinformatics/pair_analysis.py > genes/DANRE/olfm3a/olfm3a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt
records (olfm3a A8KB73, 457 aa; olfm3b A0A8N7UT25, 457 aa). Human OLFM1/2/3 and mouse Olfm1 come
from UniProt; gar and medaka proteins are the Ensembl canonical proteins of the orthologs Ensembl
Compara assigns. Alignments as in the abi1 analysis (Biopython global, BLOSUM62, -10/-0.5).

## Protein

| Comparison | Identity |
|---|---|
| olfm3a vs olfm3b | 83.2% (457 columns) |
| olfm3a / olfm3b vs human OLFM3 canonical (Q96PB7, 478 aa) | 79.7% / 77.6% |
| olfm3a / olfm3b vs human OLFM3 isoform Q96PB7-3 (458 aa) | 83.8% / 81.0% |
| olfm3a / olfm3b vs human OLFM1 | 58.7% / 58.4% |
| olfm3a / olfm3b vs human OLFM2 | 59.0% / 58.5% |

Both zebrafish copies are OLFM3 orthologs, 83.2% identical to each other. Their N-termini match
the human 458-aa isoform Q96PB7-3 (N-terminal 60 residues 70.5% / 63.9% identical) rather than
the 478-aa canonical isoform (25.9%), so the two zebrafish entries represent the same splice form.

Per region of human OLFM3 (identical residues / region length):

| Region (UniProt features of Q96PB7) | olfm3a | olfm3b |
|---|---|---|
| Coiled coil (77-217) | 85.1% | 82.3% |
| Olfactomedin-like domain (218-470) | 86.6% | 85.0% |

All six cysteines of human OLFM3 are kept in both copies (olfm3b has two additional cysteines).
Both copies carry four N-glycosylation sequons at the same four positions. The two residues
that correspond to the calcium-site residues E404 and D453 of mouse Olfm1 are kept in both copies.
Both copies keep the coiled coil, the olfactomedin domain, all six human cysteines and the calcium-site residues.

**Gar.** The Ensembl canonical gar OLFM3 protein is only 375 aa and aligns to 179 of the 253
olfactomedin-domain residues, so it is probably an incomplete gene model; gar comparisons for this
pair are partial. **Relative rate (gar outgroup):** of 375 aligned gar positions, 21 changed only in
olfm3a and 32 only in olfm3b (chi2 = 2.28, not significant).

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** olfm3a is off until pharyngula and rises
to 9-11 TPM in 3-5-day larvae. olfm3b stays at 0-1 TPM at every stage through day 5.
olfm3a is the predominant larval copy; olfm3b is barely detected in whole embryos and larvae.

**Bgee calls (only "expressed" calls are returned; absence is not proven absence).**
olfm3a: brain 70.4, retina 53.3, larva 52.3, bone 45.1. olfm3b: brain 55.0, intestine 50.2,
early embryo 45.4, blastula 42.1, ovary 35.7, tail 28.7, bone 24.4. Only brain and bone have calls
for both; retina has a call for olfm3a only, intestine and ovary for olfm3b only. The microarray
has a probe for olfm3a only.

**Gar (pre-duplication state).** Gar OLFM3 has 10 Bgee calls, highest in brain (75.2), ovary
(71.7) and eye (65.0), then heart, mesonephros, larva, embryo, bone, testis and muscle. Brain,
eye and ovary expression therefore appear ancestral; in zebrafish the eye call is carried by
olfm3a and the ovary call by olfm3b, and both copies are called in brain.

## Interpretation

- Protein: both copies keep every feature examined. No evidence of protein-level divergence.
- Expression: olfm3a carries the larval neural (brain, retina) expression; olfm3b is low
  throughout development, with adult brain, intestine and ovary calls. The complementary retina
  and ovary calls, both present in gar, fit an expression partition, but the Bgee calls are
  thresholded, come from different sample sets, and no in situ data exist for either copy. A
  low-expressed copy on its way to loss would give a similar picture.

## Synteny

olfm3a is on chr24 (28.69 Mb) and olfm3b on chr2 (15.34 Mb). For each copy, the script took all
protein-coding genes within 1.5 Mb, asked Ensembl for their zebrafish paralogues with a
Clupeocephala (teleost-level) duplication node, and checked where the partner lies.

- **Conserved neighbour:** abca4a lies about 125 kb from olfm3a (chr24:28.56 Mb) and its teleost-level
  paralogue abca4b about 140 kb from olfm3b (chr2:15.20 Mb). This is the only neighbour pair found
  within 1.5 Mb in either direction (6 of 41 olfm3a neighbours and 7 of 41 olfm3b neighbours have a
  teleost-level paralogue).
- **Chromosome level:** 6 of the teleost-level paralogue pairs from the olfm3a neighbourhood have
  their partner on chr2 (including hs6st1b/hs6st1a, plppr4b/plppr4a and agl), and 4 from the
  olfm3b neighbourhood have their partner on chr24 (including hccs and tlcd4a).

The shared abca4 neighbour and several chr24/chr2 paralogue pairs support the two copies sitting
in duplicated (ohnologous) chromosome segments, independent of the gene-tree node. No background
expectation was computed.
