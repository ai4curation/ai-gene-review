# guca1c / guca1d (zGCAP3 / zGCAP4) pair analysis

Scripts (run from the repo root; all data fetched at run time):

- `pair_analysis.py` -> `output.txt`: ZFIN name mapping, identities (UniProt, Ensembl), human GUCA1C landmarks,
  relative-rate test, E-ERAD-475 time course, Bgee calls (zebrafish + spotted gar), local synteny.
- `expression_compare.py guca1c guca1d` -> `expression_output.txt`: ZFIN curated wild-type expression and Bgee calls.
- `photoreceptor_scrna.py guca1a guca1b guca1c guca1d guca1e guca1g gnat2 gnat1` -> `scrna_output.txt`:
  reanalysis of the adult photoreceptor scRNA-seq matrix of Ogawa & Corbo 2021 (GEO GSE175929).

## 0. Names

ZFIN aliases: guca1c = gcap3, guca1d = gcap4, guca1aa = gcap1 (formerly guca1a), guca1b = gcap2,
guca1ab.1 = gcap5 (formerly guca1e), guca1g = gcap7. So zGCAP3 = guca1c and zGCAP4 = guca1d in all papers
cited here. The authors' scRNA GTF places guca1c on chr15 and guca1d on chr21, matching Ensembl.

## 1. Protein identity

- guca1c vs guca1d: 75.5% over 188 columns (46 differing columns).
- To human GUCA1C (O95843): guca1c 40.7%, guca1d 42.6%. To human GUCA1A: 41.3% and 45.8%.
- To spotted gar GCAP3 (ENSLOCG00000009269): guca1c 68.9%, guca1d 71.4%.
- Medaka orthologs: guca1c-medaka 85.2%, guca1d-medaka 84.1%; cross comparisons 77.8-78.3%, so the two
  orthogroups are each shared with medaka (one-to-one orthologs of each copy), as expected for a duplication
  before the zebrafish-medaka split.
- Relative-rate test against gar: 16 changes unique to guca1c, 12 unique to guca1d (chi2 = 0.57, not
  significant). Neither copy is evolving detectably faster.

## 2. Functional residues

- All 14 Ca2+-coordinating positions annotated on human GUCA1C (EF2, EF3 and EF4 loops) align to residues
  compatible with Ca2+ binding in both zebrafish copies: loop positions 1, 3, 5 and 12 are D/D/D/E (EF2),
  D/D/N/E (EF3) and D/N/E/E (EF4) in both. EF2 position 3 is D in both zebrafish copies and both medaka copies
  but N in human and gar; EF3 position 7 is K in all fish (S in human).
- Gly2 (N-myristoylation) is present in both copies and both medaka orthologs. The Ensembl gar model starts
  "SRMGAYGS", apparently an N-terminal extension in the gene model; the MG motif is present internally.
- The EF-hands are 16-22/36 identical to human in each copy; no copy-specific loss of a conserved landmark.

Conclusion: both copies keep the full GCAP architecture and Ca2+-binding sites. The published tenfold
difference in Ca2+ sensitivity (PMID:21829700) is not explained by any loss of a binding-site residue that
this comparison can see.

## 3. Expression

**Whole embryo (E-ERAD-475, TPM medians).** Both zero until hatching; at 3-5 dpf guca1c 3 TPM and guca1d 5-8 TPM.

**Bgee.** guca1c: in situ calls (retinal outer nuclear and photoreceptor layers; also white matter / cranial
nerve II from a large-scale pharyngula in situ screen) and a larval RNA-seq call. guca1d: RNA-seq calls in
retina (86.8), larva, and low calls in granulocyte, head kidney and bone. Spotted gar GCAP3: camera-type eye
97.7, with low calls in skin, brain and larva. The ancestral (gar) gene is eye-dominant, like both copies.

**ZFIN curated.** guca1c 37 records (retina, cone photoreceptors, plus antibody-based records in plexiform and
ganglion cell layers, rods and ciliary/corneal epithelium from two antibody studies); guca1d 5 records (retina,
retinal cone cell, photoreceptors; in situ and RT-PCR). The imbalance reflects how often each copy was studied.

**Adult photoreceptor scRNA-seq (GSE175929), marker-based cell assignment.**

| gene | rod | UV cone | blue cone | green cone | red cone |
|---|---|---|---|---|---|
| guca1c (fraction >0 / CP10K) | 0.99 / 28.5 | 1.00 / 57.0 | 1.00 / 56.6 | 1.00 / 73.3 | 1.00 / 75.3 |
| guca1d | 0.38 / 1.9 | 0.80 / 3.5 | 0.88 / 5.1 | 0.98 / 6.8 | 0.95 / 6.8 |

- The rod/cone ratio is 0.43 for guca1c and 0.34 for guca1d, the same as for the cone transducin gnat2 (0.38),
  whereas rod genes are 30-80-fold enriched in rods (gnat1 83, guca1b 49, guca1a 32). So the rod signal of both
  copies is at the ambient-RNA level of this matrix: both are cone-specific.
- Both copies are in every cone type. guca1c is about ten times more abundant than guca1d in every cone type.
  guca1d is about half as abundant in UV cones as in red and green cones, while guca1c varies less; this matches
  the published in situ result that zGCAP4 is weak in short single (UV) cones.
- No other GCAP gene is expressed in cones at comparable levels (guca1ab.1/gcap5 is UV-enriched at 2.5 CP10K).

Caveat: marker-based assignment of all 12,833 barcodes, not the authors' filtered clusters; ambient RNA and doublets
are not removed.

## 4. Synteny

guca1c is on chr15 (2.88 Mb) and guca1d on chr21 (22.91 Mb). Within 1.5 Mb of guca1c, 18 of 76 protein-coding genes
have a teleost-level (Osteoglossocephalai/Clupeocephala) zebrafish paralogue; two of them have their partner within
1.5 Mb of guca1d (tgfb1a/tgfb1b and lpar6a/lpar6b), and the reverse scan from guca1d finds the same two pairs. Further
teleost-level pairs link the two chromosomes more loosely (for example cldna/cldnb and nectin3b on chr21 with a
paralogue on chr15; the long list of or62 olfactory-receptor pairs reflects a gene family, not synteny). This is a
small duplicated block: consistent with a teleost genome duplication, but weaker than a typical ohnolog block.
