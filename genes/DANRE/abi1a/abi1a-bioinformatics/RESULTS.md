# abi1a / abi1b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/abi1a/abi1a-bioinformatics/pair_analysis.py > genes/DANRE/abi1a/abi1a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt
records (abi1a A0A8M3AND6, 522 aa; abi1b A0A286YAJ7, 507 aa). Human ABI1/2/3 come from UniProt;
spotted gar and medaka orthologs are the Ensembl canonical proteins of the orthologs Ensembl
Compara assigns. Global alignments: Biopython PairwiseAligner, BLOSUM62, gap open -10 /
extend -0.5; identity = identical columns / alignment length.

## Protein

| Comparison | Identity |
|---|---|
| abi1a vs abi1b | 79.2% (543 columns) |
| abi1a vs human ABI1 (Q8IZP0, 508 aa) | 81.6% |
| abi1b vs human ABI1 | 77.5% |
| abi1a / abi1b vs human ABI2 | 62.5% / 57.6% |
| abi1a / abi1b vs human ABI3 | 36.1% / 36.5% |
| abi1a / abi1b vs gar ABI1 (ENSLOCG00000007606, 625-aa canonical) | 72.5% / 68.8% |

abi1a (522 aa) is 81.6% identical to human ABI1 and abi1b (507 aa) is 77.5%; the two zebrafish copies are 79.2% identical.
Both are clearly ABI1 rather than ABI2 or ABI3 orthologs.

Per region of human ABI1 (identical residues / region length):

| Region (human ABI1 numbering) | abi1a | abi1b | gar |
|---|---|---|---|
| WAVE-binding N-terminus (18-79) | 95.2% | 91.9% | 95.2% |
| t-SNARE-like coiled coil (45-107) | 100% | 100% | 100% |
| central disordered, proline-rich (159-421) | 76.8% | 70.7% | 88.2% |
| SH3 (446-505) | 90.0% | 91.7% | 91.7% |

The N-terminal WAVE-binding region, the coiled-coil domain and the SH3 domain are conserved in both copies,
and the divergence is concentrated in the disordered linker. Tyrosines at the positions of human
Y53, Y213 (the ABL phosphorylation site) and Y455 are kept in both copies and in gar. abi1b has a
13-residue N-terminal extension before the residue aligned to human ABI1 Met1 (a predicted
"isoform X1" start; not verified).

**Relative rate (gar outgroup).** Of 480 gar positions aligned in both copies, 17 changed only in
abi1a and 28 only in abi1b (chi2 = 2.69, not significant). Neither copy has evolved significantly
faster.

**Medaka.** Identity cannot resolve which medaka copy matches which zebrafish copy here: the
Ensembl canonical proteins differ in length (641 vs 496 aa), and both zebrafish copies are more
similar to the 496-aa medaka protein.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** The two copies are expressed at different
times:

| Stage | abi1a | abi1b |
|---|---|---|
| zygote | 7 | 8 |
| 128-cell | 5 | 28 |
| 1k-cell | 4 | 26 |
| dome | 2 | 16 |
| 50% epiboly | 6 | 11 |
| shield | 13 | 9 |
| 75% epiboly | 26 | 6 |
| 1-4 somites to day 5 | 22-36 | 3-7 |

abi1b is the predominant maternal and cleavage-stage transcript, and abi1a predominates from mid-gastrulation onward.

**Bgee calls (only "expressed" calls are returned, so absence means no call, not proven
absence).** abi1a: 25 calls, including RNA-Seq calls in gill, intestine, granulocytes, skin,
spleen, swim bladder, liver, eye, head kidney, muscle and testis, as well as brain, retina and
embryo. abi1b: 8 calls, all in early embryo, blastula, gastrula, larva, retina, brain, ovarian
follicle and bone. No anatomical entity has an RNA-Seq call for abi1b only. The zebrafish
microarray (Affymetrix) has data for abi1a only, so the microarray calls cannot be compared.

**Gar (pre-duplication state).** Gar ABI1 has 14 Bgee expressed calls (skin, eye, liver, larva,
mesonephros, testis, intestine, brain, bone, heart, embryo, ovary, gill, muscle), with scores of
63-88. Broad adult expression therefore looks ancestral; abi1a resembles gar in breadth,
while abi1b is restricted to early embryo, neural tissue and ovary.

## Interpretation

- The protein is conserved in both copies in every region known to carry function (WAVE-complex
  assembly, SH3). No evidence of protein-level divergence.
- Expression differs: abi1b is the maternal copy and abi1a the zygotic, broadly expressed copy.
  This is consistent with an expression partition, but whether gar ABI1 is maternally loaded is
  not known (the gar data have no cleavage-stage samples), so the split cannot yet be called a
  partition of an ancestral pattern rather than a gain in one copy.

## Synteny

abi1a is on chr24 (5.94 Mb) and abi1b on chr2 (9.87 Mb). For each copy, the script took all
protein-coding genes within 1.5 Mb, asked Ensembl for their zebrafish paralogues with a
Clupeocephala (teleost-level) duplication node, and checked where the partner lies.

- Within 1.5 Mb of the other copy: **no** such paralogue pairs in either direction (40 neighbours
  of abi1a, 3 with a teleost-level paralogue; 66 neighbours of abi1b, 17 with one).
- On the other copy's chromosome: all 3 teleost-level paralogues of abi1a's neighbours lie on chr2
  (kmt2ca/kmt2cb, agtr1b/agtr1a and one unnamed pair), but 12.8-53 Mb away; 1 of the 17 from
  abi1b's neighbourhood lies on chr24.

There is no conserved microsynteny around this pair; the chromosome-level signal (chr24/chr2
pairs such as kmt2c and agtr1) is weak and was not tested against a background expectation.
