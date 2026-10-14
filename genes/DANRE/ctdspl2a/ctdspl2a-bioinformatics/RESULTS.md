# ctdspl2a / ctdspl2b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/pair_analysis.py > genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached Swiss-Prot records
(ctdspl2a Q08BB5, 469 aa; ctdspl2b A4QNX6, 460 aa). Human CTDSPL2 (SCP4), CTDSP1, CTDSP2 and CTDSPL are
the reviewed UniProt entries. Gar and medaka proteins are the Ensembl canonical proteins of the
orthologues that Ensembl Compara assigns. Alignments: Biopython global, BLOSUM62, gap open -10, extend
-0.5; identity = identical columns / alignment length.

## Duplication node

Ensembl Compara places the ctdspl2a/ctdspl2b duplication at the Osteoglossocephalai node (a teleost
node) and gives one spotted gar orthologue (ENSLOCG00000013760) for both copies. Medaka keeps two
copies, each a one-to-one orthologue of one zebrafish copy (ENSORLG00000005035 for ctdspl2a,
ENSORLG00000006288 for ctdspl2b).

## Protein

| Comparison | Identity |
|---|---|
| ctdspl2a vs ctdspl2b | 70.9% (477 columns) |
| ctdspl2a / ctdspl2b vs human CTDSPL2 (Q05D32, 466 aa) | 73.2% / 69.7% |
| ctdspl2a / ctdspl2b vs gar CTDSPL2 (488 aa) | 74.4% / 71.0% |
| ctdspl2a / ctdspl2b vs medaka ctdspl2a orthologue | 75.7% / 69.0% |
| ctdspl2a / ctdspl2b vs medaka ctdspl2b orthologue | 72.2% / 71.4% |
| ctdspl2a / ctdspl2b vs human CTDSP1, CTDSP2, CTDSPL | 22-26% |

Per region of human CTDSPL2 (identical residues / region length):

| Region (UniProt features of Q05D32) | ctdspl2a | ctdspl2b | gar |
|---|---|---|---|
| FCP1 homology (phosphatase) domain 283-442 | 97.5% | 96.2% | 98.8% |
| Disordered N-terminal region 1-140 | 52.1% | 47.1% | 65.7% |
| Disordered region 220-240 | 42.9% | 52.4% | 66.7% |

**Catalytic motif.** The HAD-family DxDx(T/V) motif of human CTDSPL2 is DLDET at 293-297 (D293 and D295
are the catalytic aspartates). Both zebrafish copies carry the identical motif: DLDET at 296-300 in
ctdspl2a and 287-291 in ctdspl2b, aligned exactly to human D293-T297 (gar DLDET at 315). Both copies keep
the DxDx(T/V) catalytic motif (DLDET) and a phosphatase domain at least 96% identical to human CTDSPL2.
The divergence between the copies lies in the N-terminal regulatory region, which carries the nuclear
localization sequences in the human protein.

**Relative rate (gar outgroup):** of 441 aligned gar positions, 38 changed only in ctdspl2a and 38 only
in ctdspl2b (chi2 = 0.00). Neither copy is evolving faster.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** Both copies are maternally loaded and expressed
at every stage. ctdspl2a: 59 TPM at zygote, peak 246 TPM at 128-cell, 50-60 TPM through
segmentation and pharyngula, 34-38 TPM in larvae. ctdspl2b: 26 TPM at zygote, peak 96 TPM at 1k-cell,
about 20 TPM from gastrula onwards, 17-18 TPM in larvae. ctdspl2a is about two- to three-fold higher
than ctdspl2b at every stage, and the two profiles have the same shape.

**Bgee calls (only "expressed" calls are returned).** Each copy has 27 calls. Both copies are called,
with high scores, in early embryo, blastula, gastrula, ovarian follicle, testis, brain, eye and retina,
granulocyte, spleen, head kidney, gill, swim bladder, skin, muscle, bone, intestine and liver. The only
RNA-seq entity called for one copy alone is heart (ctdspl2a) and head (ctdspl2b); heart has an
Affymetrix-supported call for ctdspl2a and the cardiac ventricle is called for both copies.

**ZFIN.** No curated wild-type expression records exist for either gene.

**Gar (pre-duplication state).** Gar CTDSPL2 has 14 Bgee RNA-seq calls spanning brain, testis, bone,
intestine, eye, heart, skin, ovary, embryo, mesonephros, larva, muscle, liver and gill: a broadly
expressed gene, like both zebrafish copies.

Both copies are broadly co-expressed in every tissue and stage sampled, as is gar CTDSPL2; the only
consistent difference is that ctdspl2a is expressed at about two- to three-fold higher levels.

## Synteny

ctdspl2a is on chr25 (32.50 Mb) and ctdspl2b on chr7 (31.37 Mb). For each copy the script took all
protein-coding genes within 1.5 Mb, asked Ensembl for their zebrafish paralogues with a teleost-level
node (Teleostei, Osteoglossocephalai or Clupeocephala), and checked where each partner lies.

- **ctdspl2a neighbourhood (44 genes):** 18 have a teleost-level paralogue, and the partners of 6 lie
  within 1.5 Mb of ctdspl2b: eif3ja/eif3jb, apba2a/apba2b, tjp1b/tjp1a, tln2b/tln2a (plus an unnamed tln2
  gene model) and isl2a/isl2b. 16 have their partner somewhere on chr7.
- **ctdspl2b neighbourhood (60 genes):** 15 have a teleost-level paralogue, and the same pairs are
  recovered in the reverse direction.

Five named teleost-level ohnolog pairs flank both copies, in both directions of the search. This is
double-conserved synteny: the two copies sit in duplicated (ohnologous) segments of chr25 and chr7,
which supports a whole-genome (TGD) origin independently of the gene trees. No background expectation
was computed.
