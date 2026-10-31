# Ank2 isoform U (M9MRX4): family placement and isoform coverage

Script: `analysis.py` (standard library only, queries PANTHER 19 and UniProt REST).
Raw output: `analysis-output.txt`.

## 1. PANTHER 19 placement

| Gene | PANTHER 19 family | Subfamily |
|---|---|---|
| Ank2 (FBgn0261788) | PTHR24123 | PTHR24123:SF141 |
| Ank (FBgn0011747) | PTHR24133 | PTHR24133:SF33 |
| ANK1 / ANK2 / ANK3 (human) | PTHR24133 | SF38 / SF36 / SF34 |

The bilaterian ankyrin PAINT node PTN002380879 is in PTHR24133 in PANTHER 19. It
contains human ANK1, ANK2 and ANK3 and fly Ank, but not fly Ank2. The fly Ank2 leaf
(PTN001948312) is in PTHR24123:SF141. There it sits in an ecdysozoan node
(PTN008606794) with C. elegans unc-44 and mask-1, and that node is sister to the
human ASB4/ASB10/ANKRD55 group. Our local `interpro/panther/PTHR24123/PTHR24123-paint.tsv`
still files PTN002380879 under PTHR24123, which reflects an older PANTHER release.

What this means:

* No PAINT/IBA annotation reaches Ank2. QuickGO shows the six PTN002380879 IBA
  rows only on fly Ank (Q0KIE7), and none on any Ank2 accession.
* The PANTHER split puts the two ecdysozoan neuronal giant ankyrins (fly Ank2 and worm
  unc-44) in a different family from the vertebrate ankyrins. Jegla et al. 2016
  (PMID:27911898) built a maximum-likelihood tree of the ankyrin family from the
  ankyrin repeats plus the ZU5-ZU5-UPA cassette, and it does not show this split.
  Ank2 also has the canonical ankyrin domain architecture (24 ANK repeats, ZU5-ZU5-UPA,
  death domain; see the UniProt features). We judge the split to be a tree artefact,
  probably caused by the giant isoform sequences, but we have not tested this.
* Because the PANTHER placement is unresolved, PAINT terms from human ANK1/2/3 are
  not transferred to Ank2 here. Every function claimed in the review rests on
  Drosophila Ank2 experiments.

## 2. Isoform coverage

* M9MRX4 (13,559 aa) and X2JCM1 (isoform AA, 11,634 aa, matching the 11,640-aa
  Ank2-XL of Stephan et al. 2015) share an identical N-terminal 11,629 aa. All of
  X2JCM1's 50-mer tiles occur exactly in M9MRX4. M9MRX4 therefore contains the
  whole Ank2-XL sequence, including the XL C-terminal microtubule-binding region
  (XL aa 10,702-11,005; PMID:25800091).
* M9MRX4 shares the first 2,400 aa with Ank2-L (Q7KU92, 4,083 aa). It also ends
  with Ank2-L's last 1,662 aa, and 80 of 81 Ank2-L 50-mer tiles occur exactly in
  it. The Ank2-L segment 1682-2089 that binds microtubules in vitro (PMID:18439405)
  sits at M9MRX4 1682-2089.
* Only 6 M9MRX4 50-mer tiles, near the XL/L junction (starting 11,601-11,851), are
  found in neither Ank2-L nor X2JCM1.

So M9MRX4 is the gene-centric model that combines the Ank2-XL giant exon with the
Ank2-L C-terminal tail. The analysis does not show whether this exact
splice form is made in vivo. It does show that both microtubule-binding regions
assayed experimentally are present in the M9MRX4 sequence.
