# samsn1a / samsn1b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/samsn1a/samsn1a-bioinformatics/pair_analysis.py > genes/DANRE/samsn1a/samsn1a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt records
(samsn1a B3DH22, 621 aa; samsn1b A0A8M2BH30, 676 aa, RefSeq isoform X1). Human SAMSN1, SASH1 and
SASH3 are the reviewed UniProt entries. Gar and medaka proteins are the Ensembl canonical proteins of
the orthologues that Ensembl Compara assigns. Alignments: Biopython global, BLOSUM62, gap open -10,
extend -0.5; identity = identical columns / alignment length.

## Duplication node

Ensembl Compara places the samsn1a/samsn1b duplication at the Osteoglossocephalai node (a teleost
node) and gives one spotted gar orthologue (ENSLOCG00000000927) for both copies. Medaka has a single
one-to-one orthologue, assigned to samsn1a; Compara gives samsn1b no medaka orthologue.

## Protein

| Comparison | Identity |
|---|---|
| samsn1a vs samsn1b | 37.8% (727 columns) |
| samsn1a / samsn1b vs gar SAMSN1 (690 aa) | 43.3% / 46.4% |
| samsn1a / samsn1b vs human SAMSN1 (Q9NSI8, 373 aa) | 27.1% / 28.0% |
| samsn1a / samsn1b vs human SASH3 | 24.3% / 26.1% |
| samsn1a / samsn1b vs human SASH1 | 17.4% / 18.7% |
| samsn1a vs medaka orthologue (523 aa) | 40.0% |

Both zebrafish proteins and the gar protein are much longer than human SAMSN1 (621, 676 and 690 aa
against 373 aa), so most of the low full-length identity comes from length differences and fast-evolving
disordered regions.

Per region of human SAMSN1 (identical residues / region length):

| Region (UniProt features of Q9NSI8) | samsn1a | samsn1b | gar |
|---|---|---|---|
| SH3 domain (163-224) | 82.3% | 77.4% | 83.9% |
| SAM domain (241-305) | 52.3% | 60.0% | 61.5% |
| 14-3-3 interaction motif (20-25) | 5/6 | 5/6 | 6/6 |
| Disordered 1-72 | 51.4% | 41.7% | 55.6% |

The SH3 domain is the best-conserved part of both copies: 82.3% (samsn1a) and 77.4% (samsn1b)
identical to the human SAMSN1 SH3 domain. Both copies keep the SAM domain and the N-terminal 14-3-3
motif region.

**Relative rate (gar outgroup):** of 573 aligned gar positions, 96 changed only in samsn1a and 93 only
in samsn1b (chi2 = 0.05, not significant). Neither copy is evolving faster.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** samsn1a is off until the end of
segmentation (about 1 TPM from 20-25 somites to prim-25), then rises to 4 TPM at long-pec and 17-28 TPM
in 3-5 day larvae. samsn1b has a small gastrula peak (5 TPM at 50% epiboly and shield) and is then off
until larval stages (10-17 TPM).

**ZFIN curated wild-type in situ hybridization.** samsn1a: blood, macrophage and solid lens vesicle
at prim-5 (Covassin et al. 2006, ZDB-PUB-060927-11). samsn1b: epiphysis (pineal) from 14-19 somites to
high-pec, and retinal photoreceptor layer at day 5 (Thisse et al. 2004 direct data submission,
ZDB-PUB-040907-1). The two genes share no curated anatomy term.

**Bgee calls (only "expressed" calls are returned; absence is not proven absence).**
samsn1a: highest in granulocyte (94.6), spleen (94.5), head kidney (90.1), swim bladder (81.9) and
retina (80.9). samsn1b: highest in retina (89.3), granulocyte (88.4), gill (69.2), spleen (63.7), plus
in situ-derived pineal, epithalamus and photoreceptor-layer calls. Both copies have RNA-seq calls in
granulocyte, spleen and head kidney, as well as bone, intestine, larva, liver, muscle, gill, retina and
skin. RNA-seq calls only for samsn1a: brain, embryo, heart, swim bladder; only for samsn1b: gastrula,
tail, testis.

**Gar (pre-duplication state).** Gar SAMSN1 has 12 Bgee RNA-seq calls, highest in bone (92.3),
eye (91.6), gill (83.9), intestine (80.5) and mesonephros (77.2, the gar kidney), then heart, liver,
larva, skin, muscle, brain and embryo. Bgee returns no gar call for spleen or blood cells; the script
does not list which gar tissues were sampled, so this may reflect missing samples rather than absent
expression, and the ancestral hematopoietic expression cannot be assessed from these data.

samsn1a is the zygotic, larval and hematopoietic copy; samsn1b has a small gastrula peak and curated
pineal and photoreceptor in situ expression. Both copies have RNA-seq calls in granulocyte, spleen and
head kidney, so the hematopoietic domain is not cleanly partitioned.

## Synteny

samsn1a is on chr15 (29.56 Mb) and samsn1b on chr10 (38.42 Mb). For each copy the script took all
protein-coding genes within 1.5 Mb, asked Ensembl for their zebrafish paralogues with a teleost-level
node (Teleostei, Osteoglossocephalai or Clupeocephala), and checked where each partner lies.

- **samsn1a neighbourhood (63 genes):** 15 have a teleost-level paralogue, and 6 of those partners lie
  within 1.5 Mb of samsn1b: gdpd5b/gdpd5a, serpinh1b/serpinh1a, nrip1a/nrip1b, msi2b/msi2a, omgb/omga and
  ksr1b/ksr1a.
- **samsn1b neighbourhood (41 genes):** 18 have a teleost-level paralogue, and the same 6 pairs are
  recovered in the reverse direction. 12 of the 18 have their partner somewhere on chr15.

Six teleost-level ohnolog pairs flank both copies, in both directions of the search. This is
double-conserved synteny: the two copies sit in duplicated (ohnologous) segments of chr15 and chr10,
which supports a whole-genome (TGD) origin independently of the gene trees. No background expectation
was computed.
