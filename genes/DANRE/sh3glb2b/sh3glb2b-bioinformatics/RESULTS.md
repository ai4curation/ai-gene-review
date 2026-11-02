# sh3glb2a / sh3glb2b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/pair_analysis.py > genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt
records used for the reviews (sh3glb2a A0A8M1N8K5, 381 aa, RefSeq NP_001035087.2; sh3glb2b
A0A8M9Q303, 421 aa, RefSeq XP_021331719.1 "isoform X1") plus the sh3glb2b RefSeq NP isoform
(Q802U5, NP_957413.1, 373 aa). Human SH3GLB2 (Q9NR46) and SH3GLB1 (Q9Y371) come from UniProt;
gar and medaka proteins are the Ensembl canonical proteins of the orthologues that Ensembl
Compara assigns. Alignments: Biopython global, BLOSUM62, gap -10/-0.5; identity = identical
columns / alignment length. The script is the same as the mapre3a/mapre3b one with a
different CONFIG.

## Orthology (Ensembl Compara)

- sh3glb2a (ENSDARG00000008983, chr8) and sh3glb2b (ENSDARG00000035470, chr5) are
  within-species paralogues with the duplication node at Osteoglossocephalai.
- Both share one spotted gar orthologue (ENSLOCG00000006193) and the human orthologue SH3GLB2.
  Each has its own one-to-one medaka orthologue (ENSORLG00000016839 for sh3glb2a,
  ENSORLG00000014325 for sh3glb2b), so medaka kept both copies.

## Protein

| Comparison | Identity |
|---|---|
| sh3glb2a vs sh3glb2b (reviewed accessions) | 73.6% (421 columns) |
| sh3glb2a vs sh3glb2b NP isoform (Q802U5) | 70.4% (402 columns) |
| sh3glb2a / sh3glb2b vs human SH3GLB2 | 72.9% / 69.2% |
| sh3glb2a / sh3glb2b vs human SH3GLB1 | 58.2% / 55.3% |
| sh3glb2a / sh3glb2b vs gar SH3GLB2 orthologue | 74.9% / 73.7% |

Both copies are SH3GLB2 (endophilin-B2) orthologues, closer to SH3GLB2 than to SH3GLB1.
The reviewed sh3glb2b entry (isoform X1) is longer than sh3glb2a because it includes two
alternatively spliced insertions: about 15 residues inside the BAR domain after the
"SASA" motif and a proline/serine-rich stretch in the linker before the SH3 domain. These
insertions lower the whole-length identity; the domains themselves are about equally
conserved.

Per region of human SH3GLB2 (identical residues / region length):

| Region (UniProt features of Q9NR46) | sh3glb2a | sh3glb2b | gar |
|---|---|---|---|
| Membrane-binding amphipathic helix (1-27) | 85.2% | 85.2% | 33.3% |
| BAR domain (24-287) | 76.9% | 78.8% | 80.3% |
| Coiled coil (206-240) | 85.7% | 91.4% | 91.4% |
| SH3 domain (335-395) | 88.5% | 86.9% | 86.9% |

The low gar value for the N-terminal helix reflects a different N-terminus in the gar gene
model (only 21 of 27 positions align), not necessarily a real difference. Both zebrafish copies
end in the same C-terminal SH3 sequence as human SH3GLB2 (...GKVPVTYLELLS).
Both copies keep the N-terminal amphipathic helix, the full BAR domain and the SH3 domain of endophilin-B2.

**Relative rate (gar outgroup).** Of 374 gar positions aligned in both copies, 36 changed only
in sh3glb2a and 23 only in sh3glb2b (chi2 = 2.86, not significant at 0.05).

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** sh3glb2b is strongly maternal (71 TPM
in zygote, 69 at 2-cell) and stays at 10-15 TPM from segmentation through day 5. sh3glb2a is
low in zygote (2 TPM), rises to 27-28 TPM at blastula stages (so it is transcribed early), falls
to 2-3 TPM from 75% epiboly onward and stays at 2-4 TPM through day 5.
sh3glb2b is the predominant copy in the zygote and from segmentation onward; sh3glb2a is comparable to sh3glb2b only at blastula stages.

**Bgee calls (only "expressed" calls are returned; absence is not proven absence).**
sh3glb2a has 20 calls, sh3glb2b 27; every sh3glb2a entity also has a sh3glb2b call. The seven
entities called only for sh3glb2b (somite, presomitic and tail-bud paraxial mesoderm, cleaving
embryo, caudal fin, integument, mesonephros) come mostly from Affymetrix microarray data, and
sh3glb2a has no Affymetrix calls at all.
Adult tissues are shared: both copies are called in brain, retina, heart, muscle, gill, intestine, liver, spleen, testis and ovarian follicle.

**Gar (pre-duplication state).** Gar SH3GLB2 has 14 calls, highest in eye (94.6) and brain
(91.9), then larva, skin, embryo, liver, mesonephros, testis, ovary, bone, heart, gill, muscle
and intestine: broad, with neural maxima, like both zebrafish copies.

**ZFIN.** High-throughput in situ records (ZDB-PUB-040907-1): sh3glb2b in central nervous
system and eye/lens from 14-19 somites to long-pec; sh3glb2a annotated only as "whole
organism" (1-cell to pec-fin). No published expression study of either copy.

## Synteny

sh3glb2a is on chr8 (2.76 Mb) and sh3glb2b on chr5 (31.64 Mb). Method as for mapre3a/mapre3b:
neighbours within 1.5 Mb, their teleost-level (Teleostei, Osteoglossocephalai or Clupeocephala)
zebrafish paralogues, and where the partners lie.

- **Conserved neighbours:** three teleost-level paralogue pairs flank both copies, found in both
  directions: zdhhc12a/zdhhc12b, slc25a25a/slc25a25b and eeig1a/eeig1b, all within about 180 kb of
  sh3glb2a on chr8 and within about 200 kb of sh3glb2b on chr5.
- **Chromosome level:** 5 teleost-level pairs from the sh3glb2a neighbourhood have their partner on
  chr5, and 7 from the sh3glb2b neighbourhood have their partner on chr8.
Three neighbouring gene pairs (zdhhc12, slc25a25, eeig1) are duplicated alongside sh3glb2, so the two copies sit in paralogous chromosome segments.

## Interpretation

- Protein: both copies keep the endophilin-B architecture and evolve at statistically similar
  rates. No evidence of protein-level divergence.
- Expression: largely overlapping and broad in adults, like gar SH3GLB2; the main difference is
  quantitative (sh3glb2b higher in the zygote and from segmentation onward). This is
  compatible with dosage retention, redundancy, or quantitative subfunctionalization; no
  functional data exist for either copy.
