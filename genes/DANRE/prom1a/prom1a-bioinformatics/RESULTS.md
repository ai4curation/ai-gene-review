# prom1a / prom1b pair analysis

Scripts (run from the repo root; all data fetched at run time):

- `pair_analysis.py` -> `output.txt`: identities (UniProt, Ensembl), human PROM1 topology and landmarks,
  relative-rate test, E-ERAD-475 time course, Bgee calls (zebrafish + spotted gar), local synteny.
- `expression_compare.py prom1a prom1b` -> `expression_output.txt`: ZFIN curated wild-type expression and Bgee calls.
- `photoreceptor_scrna.py prom1a prom1b gnat1 gnat2` -> `scrna_output.txt`: reanalysis of the adult photoreceptor
  scRNA-seq matrix of Ogawa & Corbo 2021 (GEO GSE175929).

## 1. Protein identity

- prom1a (Q9W735, 826 aa) vs prom1b (A0A8M2BI60, RefSeq isoform X8, 867 aa): 54.4% over 867 columns. Using the
  Ensembl canonical proteins (849 and 853 aa): 56.0%.
- To human PROM1 (O43490): prom1a 41.2%, prom1b 39.0% (41-43% and 38-40% across the seven human isoforms).
- To spotted gar PROM1 (ENSLOCG00000003057): prom1a 60.3%, prom1b 60.8%.
- Medaka: prom1a-medaka ortholog 62.5%, prom1b-medaka ortholog 67.4%; cross comparisons 53.7-56.9%, so each
  copy has its own medaka ortholog.
- Relative-rate test against gar: 107 changes unique to prom1a and 118 unique to prom1b (chi2 = 0.54, not
  significant). Neither copy is evolving detectably faster.

## 2. Topology and landmarks

- All five transmembrane segments of human PROM1 align without gaps in both copies; the two small cytoplasmic
  loops are the most conserved regions (64-81% identical to human); the large extracellular loops are 36-44% identical
  in both copies and in gar.
- The C-terminal cytoplasmic tail (human 814-865) is poorly aligned in both zebrafish proteins (17-23 of 52
  positions aligned) but largely aligned in gar (44/52); the zebrafish isoforms used here differ at the C terminus
  (the published record notes many splice variants).
- Of the eight annotated human N-glycosylation asparagines, three are kept in each copy (not the same three: prom1a
  keeps 548/580/730, prom1b 580/729/730; gar 220/580/730). Sequon counts: prom1a 13, prom1b 9, gar 14, human 9.
- Human cysteines: 15 of 22 kept in each copy (17 in gar); the changes are mostly shared with gar.
- The human CORD12/STGD4 residue R373 is A in prom1a, E in prom1b and N in gar: not conserved in fish.

Conclusion: both copies keep the full prominin architecture; no copy-specific loss of a conserved landmark is
visible.

## 3. Expression

**Whole embryo (E-ERAD-475, TPM medians).** prom1a is maternal (11-12 TPM from 2-cell to dome) and zygotic
throughout (1-5 TPM during segmentation and pharyngula), rising to about 14-15 TPM at 3-5 dpf. prom1b is absent
before segmentation, low (0.3-2 TPM) until hatching, then rises to 26-49 TPM at 3-5 dpf, above prom1a.

**Bgee (RNA-seq-supported anatomical entities).** prom1a has 46 calls, including early embryo, blastula, ovarian
follicle, testis, muscle, heart, intestine, gill, spleen, head kidney, skin, retina and brain. prom1b has 5 calls:
retina, larva, brain, embryo and bone. Spotted gar PROM1: eye (96.8), ovary, larva, brain, embryo, bone, testis,
mesonephros, skin, muscle, liver, intestine and heart. The broad, gonad- and epithelium-including gar pattern is
matched by prom1a; prom1b is limited to the eye/retina and brain subset.

**ZFIN curated.** prom1a 49 records; prom1b 34. Shared: brain, cerebellum, epiphysis, eye, otic vesicle, retina (inner
and outer nuclear layers), hypothalamus, several brain nuclei. prom1a only: forebrain and dorsal-telencephalon
proliferative regions, lens and lens epithelium, olfactory epithelium, gill, intestine, kidney, muscle, ovary,
maternal (4-cell) RT-PCR. prom1b only: hindbrain proliferative region, griseum centrale, valvula cerebelli, retinal
pigmented epithelium, optic furrow.

**Adult photoreceptor scRNA-seq (GSE175929), marker-based cell assignment.**

| gene (fraction >0 / CP10K) | rod | UV cone | blue cone | green cone | red cone |
|---|---|---|---|---|---|
| prom1a | 0.42 / 1.7 | 0.31 / 0.4 | 0.40 / 0.6 | 0.67 / 0.7 | 0.58 / 0.6 |
| prom1b | 0.75 / 6.5 | 0.54 / 1.1 | 0.57 / 1.2 | 0.88 / 1.9 | 0.88 / 2.1 |

Both copies are detected in rods and in every cone type, with prom1b three to four times more abundant than prom1a.
Both are rod-enriched (rod/cone ratio 3.0 for prom1a and 4.2 for prom1b, against 0.38 for the cone gene gnat2, which
marks the ambient level in the rod group). Caveat: marker-based assignment of all barcodes, not the authors' clusters.

## 4. Synteny

prom1a is on chr14 (46.46 Mb) and prom1b on chr1 (22.71 Mb). Within 1.5 Mb of prom1a, 18 of 61 protein-coding genes
have a teleost-level (Osteoglossocephalai/Clupeocephala) zebrafish paralogue, and 6 of those partners lie within
1.5 Mb of prom1b: anxa5a/b, fgfbp1a/b, fgfbp2a/b, tapt1a/b, ldb2a/b and qdpra/qdprb.1. The reverse scan (from prom1b,
53 genes, 12 with a teleost-level paralogue) finds the same six pairs next to prom1a. The two copies therefore sit in
a duplicated block with at least six other retained gene pairs, consistent with a whole-genome duplication
(the gar side of the block was not checked).
