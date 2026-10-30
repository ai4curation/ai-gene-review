# exoc3l2a / exoc3l2b orthology, protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/pair_analysis.py > genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt
records (exoc3l2a A0A8N7TEH3, 932 aa; exoc3l2b A0A8M9Q5H9, isoform X1, 917 aa). Human EXOC3-family
proteins are the reviewed UniProt entries. Gar, medaka and the other zebrafish family members are
Ensembl canonical proteins. Alignments: Biopython global, BLOSUM62, gap open -10, extend -0.5;
identity = identical columns / alignment length.

## Orthology: EXOC3L2, not EXOC3L4

The pair was drawn from the PANTHER TGD table, which lists EXOC3L4 as the human ortholog of both
genes. PANTHER's HMM places the zebrafish proteins in TNFAIP2-named subfamilies (SF18 and SF17),
while human EXOC3L2 is in SF7 and human EXOC3L4 in SF14 (UniProt cross-references in `output.txt`,
section 1). ZFIN names the genes after EXOC3L2, and Ensembl Compara calls human EXOC3L2 (and mouse
Exoc3l2) a one-to-many ortholog of each copy.

| Protein | exoc3l2a | exoc3l2b |
|---|---|---|
| human EXOC3L2 (Q2M3D2) | 35.3% | 35.9% |
| human EXOC3L4 (Q17RC7) | 21.8% | 21.9% |
| human TNFAIP2 / M-Sec (Q03169) | 20.9% | 21.2% |
| human EXOC3L1 (Q86VI1) | 20.7% | 21.5% |
| human EXOC3 / Sec6 (O60645) | 19.7% | 20.6% |
| zebrafish exoc3l4 | 22.2% | 21.5% |
| zebrafish tnfaip2a / tnfaip2b | 18.2% / 17.3% | 20.5% / 18.1% |
| zebrafish exoc3, exoc3l1 | 20.9%, 20.8% | 21.2%, 20.8% |
| gar ortholog (ENSLOCG00000014731) | 47.5% | 56.2% |
| medaka ortholog of exoc3l2a / of exoc3l2b | 60.2% / 48.6% | 53.3% / 64.3% |

The two zebrafish proteins are 50.9% identical to each other, 35-36% identical to human EXOC3L2 and only 19.7-21.9% identical to human EXOC3 (the Sec6 ortholog), EXOC3L1, EXOC3L4 and TNFAIP2.
Zebrafish also has its own exoc3l4, tnfaip2a, tnfaip2b and exoc3l1 genes, each about 17-22% identical
to either copy. The gar and medaka orthologs show the same pattern (34.9-38.5% to EXOC3L2,
19.4-23.6% to the others). The synteny below adds that the exoc3l2a neighbourhood has human
orthologues near EXOC3L2 on chromosome 19 (MARK4 0.13 Mb away) and none near EXOC3L4 or TNFAIP2 on
chromosome 14. Both copies are EXOC3L2 co-orthologs. The PANTHER EXOC3L4 label is not supported.

## Protein

- **Identity between the copies:** 50.9% over 992 columns. This is low for a teleost-duplicate pair,
  and both copies are only 35-36% identical to human EXOC3L2, so the whole EXOC3L2 lineage evolves fast.
- **Domains.** Pfam Sec6 (PF06046) spans residues 270-719 of human EXOC3L2. Identity to human per region:

| Region of human EXOC3L2 | exoc3l2a | exoc3l2b | gar |
|---|---|---|---|
| N-terminal, 1-269 | 43.5% (244/269 aligned) | 43.1% (242/269) | 46.1% (253/269) |
| Sec6 domain, 270-719 | 43.1% (445/450 aligned) | 44.4% (444/450) | 41.6% (449/450) |
| C-terminal, 720-802 | 37.3% | 32.5% | 39.8% |

  Both copies keep a full-length Sec6 domain and the N-terminal region; neither is truncated.
- **Patient-variant sites.** The reported human variants (p.Leu41Gln, p.Arg72*; PMID:30327448) do
  not match the canonical UniProt isoform, which has Gly41 and Ala72, so they are numbered on a
  different transcript. The script's site check is therefore not informative and I do not use it.
- **Relative rate (gar outgroup).** Of 829 gar positions aligned in both copies, 138 changed only in
  exoc3l2a and 71 only in exoc3l2b (chi2 = 21.48, P < 0.05). exoc3l2a has evolved about twice as fast
  as exoc3l2b since the duplication. Consistent with this, exoc3l2b is closer to gar (56.2% vs 47.5%).
  exoc3l2a is the faster-evolving copy.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** Both copies are essentially off through
gastrulation (exoc3l2b 0.3-0.5 TPM in blastula), come on during segmentation/pharyngula, and reach
7-13 TPM in 3-5-day larvae. exoc3l2a starts a little earlier (0.4-2 TPM from 1-4 somites; exoc3l2b
from 20-25 somites). The whole-embryo profiles of the two copies are similar in level and timing.

**Bgee (only "expressed" calls; absence is not proven absence).** 16 calls for exoc3l2a and 17 for
exoc3l2b, 14 of them shared (intestine, pharyngeal gill, head kidney, heart, liver, zone of skin,
bone, muscle, tail, larva, blastula, granulocyte, head, testis). exoc3l2a only: swim bladder
(its highest score, 92.7) and early embryo. exoc3l2b only: mesonephros, spleen, ovary. Gar (14 calls)
is expressed in intestine, gill, mesonephros, embryo, testis, liver, heart, skin, eye, larva, bone,
ovary, muscle and brain. At bulk-tissue level the adult profiles of the two copies overlap broadly
and both resemble gar. These calls are not cell-type resolved and cannot show an endothelial versus
neural-crest split.

**ZFIN curated wild-type expression.** exoc3l2a: no rows. exoc3l2b: four rows, all from
ZDB-PUB-100518-8 (PMID:20463035; the paper calls the gene "sec6"): neural crest (5-9 somites),
dorsal hindbrain and pharyngeal arches (prim-5 to protruding-mouth), and whole embryo (RT-PCR).
The published endothelial in situ for exoc3l2a (PMID:40613926) is not yet in ZFIN.

## Synteny

exoc3l2a is on chr5 (36.75 Mb) and exoc3l2b on chr15 (20.14 Mb). For each copy, the script took all
protein-coding genes within 1.5 Mb, asked Ensembl for their zebrafish paralogues with a teleost-level
duplication node (Osteoglossocephalai, Clupeocephala or Teleostei), and checked where the partner lies.
It also located the human and gar orthologues of the neighbours.

- **Paralogous neighbours next to both copies.** ppp1r14aa lies 0.02 Mb from exoc3l2a and its
  Osteoglossocephalai-level paralogue ppp1r14ab 0.01 Mb from exoc3l2b. dlb lies 0.06 Mb from exoc3l2a
  and its paralogue dlc 0.27 Mb from exoc3l2b. Further teleost-level pairs link the two chromosomes
  at 3-7 Mb (mark4a/mark4b and ckma/ckmb about 3.4 Mb from exoc3l2b; usf1/usf1l, ubash3bb/ubash3ba,
  bco2b/bco2a and sdhdb/sdhda about 6.7-7.0 Mb from exoc3l2a).
- **Gar.** 13 of the exoc3l2a neighbours and 5 of the exoc3l2b neighbours have their gar orthologue
  within 5 Mb of the single gar exoc3l2 gene on LG2 (for example mark4 0.08 Mb, ckm 0.12 Mb and
  capns1 0.19 Mb from it for exoc3l2a; spint2 0.05 Mb and plekhg2 0.11 Mb for exoc3l2b).
- **Human.** Three exoc3l2a neighbours have human orthologues within 5 Mb of EXOC3L2 at 19q13.32
  (MARK4, KPTN, SLC8A2). None of either neighbourhood maps near EXOC3L4 or TNFAIP2 on chromosome 14.

Two copies on different chromosomes, flanked by paralogous neighbours from a teleost-level
duplication, with both neighbourhoods mapping to one gar region: this is double conserved synteny
and supports a TGD origin, in agreement with the Compara duplication node (Osteoglossocephalai).
