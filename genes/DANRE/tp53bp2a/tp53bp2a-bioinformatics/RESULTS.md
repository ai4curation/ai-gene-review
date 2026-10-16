# tp53bp2a / tp53bp2b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/pair_analysis.py > genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt
records (tp53bp2a F1R419, 1060 aa; tp53bp2b F1QWN1, 1063 aa). Human TP53BP2 (Q13625, all isoforms)
comes from UniProt; gar and medaka proteins are the Ensembl canonical proteins of the orthologues
Ensembl Compara assigns (gar ENSLOCG00000015726, one gar gene for both copies; medaka
ENSORLG00000007284 for tp53bp2a and ENSORLG00000000954 for tp53bp2b, each one-to-one). Alignments are
Biopython global, BLOSUM62, gap open -10 / extend -0.5; identity = identical columns / alignment length.

## Protein

| Comparison | Identity |
|---|---|
| tp53bp2a vs tp53bp2b | 60.9% (1100 columns) |
| tp53bp2a / tp53bp2b vs human TP53BP2 (Q13625, 1128 aa) | 60.5% / 60.1% |
| tp53bp2a / tp53bp2b vs gar TP53BP2 | 62.7% / 58.9% |
| tp53bp2a vs its medaka orthologue / vs the other medaka copy | 61.9% / 53.5% |
| tp53bp2b vs its medaka orthologue / vs the other medaka copy | 61.6% / 57.3% |

Each zebrafish copy is closer to its own medaka orthologue than to the other medaka copy, as expected
if the duplication predates the zebrafish-medaka split. Both zebrafish entries are full-length
forms (closest to the 1128-aa and 1134-aa human isoforms, not to the 1005-aa isoform Q13625-2).

**Per region of human TP53BP2** (identical residues / region length):

| Region (UniProt feature of Q13625) | tp53bp2a | tp53bp2b | gar |
|---|---|---|---|
| ANK 1 (926-957) | 90.6% | 96.9% | 93.8% |
| ANK 2 (958-990) | 97.0% | 97.0% | 100% |
| ANK 3 (991-1024) | 100% | 97.1% | 100% |
| ANK 4 (1025-1067) | 93.0% | 90.7% | 90.7% |
| SH3 (1057-1119) | 65.1% | 68.3% | 81.0% |
| SH3-binding motif (866-875) | 90.0% | 100% | 100% |

The four ankyrin repeats are 90.6-100% identical to human TP53BP2 in both copies. Trp1098, whose
mutation abolishes APC2 binding in human ASPP2, is kept in both copies and in gar. The SH3 domain is
fully aligned (63/63) in both copies. The N-terminal ubiquitin-like Ras-associating domain annotated
on tp53bp2a (residues 23-86) aligns 63/64 to tp53bp2b with 64.1% identity; the two copies' ankyrin
repeats annotated on tp53bp2a are 97-100% identical to each other, and their SH3 domains 69.8%.
Both copies start with the same N-terminal sequence as human TP53BP2 (MMPMFLTVYLSN).

Most of the difference between the copies therefore lies outside the ankyrin repeats, in the long
proline-rich, disordered middle of the protein, which also differs between each copy and human.

**Relative rate (gar outgroup):** of 973 gar positions aligned in both copies, 115 changed only in
tp53bp2a and 124 only in tp53bp2b (chi2 = 0.34, not significant). Neither copy is evolving faster.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).**

| Stage | tp53bp2a | tp53bp2b |
|---|---|---|
| zygote | 26 | 15 |
| 128-cell to dome | 76-78 | 16-25 |
| 50% epiboly / shield | 91 / 88 | 4 / 2 |
| segmentation (1-25 somites) | 56-75 | 5-6 |
| pharyngula prim-5 to prim-25 | 39-51 | 6-9 |
| larval day 4-5 | 34-43 | 13-15 |

Both copies are present in the zygote (26 and 15 TPM), so both are maternally provided.
tp53bp2a dominates from gastrulation through larval stages (about 20-fold higher at 50% epiboly).
tp53bp2b is 16-25 TPM in the blastula, falls to 2-6 TPM from gastrulation to pharyngula, and rises
again to 11-15 TPM in hatching and larval stages.

**Bgee calls** (only "expressed" calls are returned; absence is not proven absence). tp53bp2a has
27 calls, tp53bp2b 20. Of 19 entities called for both, tp53bp2a scores higher in 16 (median
difference 12.9). RNA-Seq calls for tp53bp2a only: camera-type eye, liver; for tp53bp2b only: tail.
Retina is called for both (tp53bp2b 87.9, its highest score; tp53bp2a 65.6). Gar TP53BP2 has 14
calls, all adult tissues and embryo/larva, from ovary and skin to brain and bone; broad expression is
therefore the ancestral state, and both zebrafish copies keep it.

**ZFIN curated expression.** Both copies carry the same set of annotations from one paper
(ZDB-PUB-140220-26, the Aspp2 growth study): RT-PCR in ten adult organs (brain, gill, heart,
intestine, kidney, liver, muscle, ovary, spleen, testis), RT-PCR from zygote to day 4, and
whole-organism in situ hybridization at six stages, with no restricted domain recorded. tp53bp2b
also has an RT-PCR row at 26+ somites from a second paper (ZDB-PUB-140821-3).

## Interpretation

- Protein: both copies keep the p53-binding ankyrin-SH3 module and the domain order of TP53BP2; no
  domain loss, no faster-evolving copy.
- Expression: both are broadly expressed in adults, like gar TP53BP2, and both are maternally
  provided. The clearest difference is quantitative and temporal: tp53bp2a is the main
  gastrula-to-larva copy, while tp53bp2b drops to near background during gastrulation and
  organogenesis. This is not a clean on/off split; no gar developmental time course was available.

## Synteny

tp53bp2a is on chr13 (0.65 Mb, near the chromosome end) and tp53bp2b on chr22 (28.8 Mb). For each
copy the script took all protein-coding genes within 1.5 Mb, asked Ensembl for their zebrafish
paralogues with a teleost-level duplication node (Teleostei, Osteoglossocephalai or Clupeocephala),
and checked where the partner lies.

- **No conserved neighbour pair** was found within 1.5 Mb in either direction (9 of 75 tp53bp2a
  neighbours and 16 of 40 tp53bp2b neighbours have a teleost-level paralogue).
- **Chromosome level:** one pair from the tp53bp2a neighbourhood has its partner on chr22
  (efemp1 / si:ch73-173h19.3, 6 Mb from tp53bp2b). The twelve chr22-to-chr13 hits from the
  tp53bp2b side are all members of one expanded pimr kinase family and are not informative.

Direct neighbour-to-neighbour paralogy therefore gives no support for the pair.

**Gar bridge (`gar_bridge.py`; output in `gar_bridge_output.txt`).** Run as
`uv run python genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/gar_bridge.py ENSLOCG00000015726 ENSDARG00000009136 ENSDARG00000054858 > genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/gar_bridge_output.txt`.
Gar TP53BP2 is on LG16. Of 67 protein-coding gar genes within 1 Mb, 60 have zebrafish orthologues.

- Near tp53bp2a (chr13, within 3 Mb): orthologues of 3 gar neighbours (polh, a GTPBP2 orthologue
  and xpo5, at 0.8-2.9 Mb).
- Near tp53bp2b (chr22, within 3 Mb): orthologues of 6 gar neighbours (sde2, mrps28 and four
  calpain genes, capn1b, capn2b, capn8 and capn2l, all at 26.3-26.4 Mb, about 2.4 Mb from
  tp53bp2b).
- No single gar neighbour has orthologues near both copies.
- The zebrafish chromosomes carrying the most orthologues of gar neighbours are chr13 (26 gar
  neighbours), chr11 (18), chr22 (14) and chr17 (13).

The gar TP53BP2 neighbourhood thus maps to both zebrafish chromosomes that carry a copy, with a
different set of ancestral neighbours kept near each copy. This is consistent with double conserved
synteny, but weaker than a textbook case: no neighbour family was kept in duplicate beside both
copies, the tp53bp2b-side neighbours are 2.4 Mb away, and the neighbourhood also maps to chr11 and
chr17.
