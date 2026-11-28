# HP_1507 start-site analysis: computed provenance

All values below were computed in this job from public records retrieved live
(UniProt REST, NCBI E-utilities on AE000511.1 / NC_000915.1, RCSB files.rcsb.org 8H52).
Retrieval date: 2026-11-26.

## 1. Records retrieved

| Record | Source | Length / coordinates |
|---|---|---|
| O26037 (O26037_HELPY) | UniProt REST | 385 aa, gene HP_1507, EMBL AE000511 / AAD08549.1 |
| AAD08549.1 | NCBI GenPept | `coded_by="AE000511.1:1580322..1581479"`, product "conserved hypothetical ATP-binding protein" |
| A0A2X5A3P4 | UniProt REST | entry **deleted** ("Not part of a reference proteome"); sequence via UniParc **UPI000D224D86**, 399 aa |
| WP_015056101.1 | NCBI protein | 399 aa, "saccharopine dehydrogenase family protein", EC 1.5.1.- |
| HP_RS07460 (old_locus_tag HP1507) | NC_000915.1 feature table | **1580280..1581479** (PGAP annotation) |
| 8H52 | RCSB PDB | H. pylori carboxyspermidine dehydrogenase + NADP, chain A residues 2-399, ligand NAP 501 (48 atoms) |

Neighbours in NC_000915.1: HP_RS07455 / HP1506 `gltS` (sodium/glutamate symporter) upstream,
HP_RS07465 / HP1508 `ccoG` downstream.

## 2. Decisive genomic test: in-frame walk upstream from the annotated GTG

Annotated start codon at 1580322 is **GTG**. Codons upstream, same frame, plus strand:

| offset | genome position | codon | aa | note |
|---|---|---|---|---|
| -1 | 1580319 | AGT | S | |
| -2 | 1580316 | GGC | G | |
| -3 | 1580313 | GTA | V | |
| -4 | 1580310 | GGC | G | |
| -5 | 1580307 | GGT | G | |
| -6 | 1580304 | GCT | A | |
| -7 | 1580301 | GGA | G | |
| -8 | 1580298 | ATT | I | |
| -9 | 1580295 | CAA | Q | |
| -10 | 1580292 | TTA | L | |
| -11 | 1580289 | GTA | V | |
| -12 | 1580286 | ACA | T | |
| -13 | 1580283 | CAT | H | |
| **-14** | **1580280** | **TTG** | (fMet) | **proposed start** |
| -15 | 1580277 | TCC | S | |
| ... | | | | |
| -31 | 1580229 | TAA | * | first in-frame stop |

**Result: 30 codons of open, in-frame upstream sequence. No stop codon between the
upstream TTG (1580280) and the annotated GTG (1580322).**

Translation of 1580280..1581479 (1200 nt, 400 codons including TAG stop), TTG read as initiator:

```
MHTVLQIGAGGVGSVVAHKMGMNRDVFKNIILASRSLDKCYAIKESMLKKGLGEIGVEQVDADDTQALVALIQKYKPKVVI
NVALPYQDLTIMQACLETKTHYIDTANYEHPDLAKFEYKEQWAFDRAYKEVGILGVLGAGFDPGVTNAYVAHAQKHHFDTI
HTLDILDCNAGDHKRPFATNFNPEINLREVSSKGRYYENGKWIETKPLEIKQVWAYPQIGEMDSYLLYHEELESLVKNIKG
LRRARFFMTFSQNYLTHMKCLENVGMLGIKEIEHQGVKIVPIQFLKTLLPDPATLAKDTTGKTNIGCYMTGIKNNQDKTLY
IYNVCDHKKCYEEVGSQAISYTTGVPAMCAAKMICNDTWSADHFRTGVFNIEELNTDPFMEELIKQGLPYEVIER
```

Predicted length **399 aa**. Byte-identical to RefSeq **WP_015056101.1** (verified in code: `True`).

Comparison with the NCTC11637 protein (UniParc UPI000D224D86, the 8H52 entity):
identity **395/399 = 99.0%**; mismatches at 132 (V/A), 133 (G/R), 156 (K/R), 370 (T/A).
**No mismatch falls inside the 14-residue extension.**

## 3. Ribosome-binding site (weak, non-discriminating)

Best ungapped duplex with the 16S 3' anti-SD `3'-AUUCCUCCACUAG-5'`, window -20..-1,
scoring G:C=3, A:U=2, G:U=1.

| Candidate start | -20..-1 | best motif | position | duplex score | spacer |
|---|---|---|---|---|---|
| TTG 1580280 (proposed) | AGTTAGAAAGTAGGTGTTCC | AGGUG | 1580271-1580275 | 13 | 4 nt |
| GTG 1580322 (O26037) | GAGCTGGTGGCGTAGGCAGT | GGUGG | 1580307-1580311 | 12 | 10 nt |

Neither matches a canonical AGGAGG. The GGUGG upstream of the annotated GTG lies *inside*
the proposed coding extension. **The RBS evidence does not settle the question; the in-frame
open upstream sequence and the orthology do.**

## 4. Ortholog N-termini (UniProt annotated starts)

48 Helicobacter PF03435 proteins retrieved; aligned to the 399-aa reference by
Needleman-Wunsch (match +1, mismatch -1, gap -2).

| Accession | Organism | Length | % id to 399-aa HP_1507 | Annotated N-terminus (first 25 aa) |
|---|---|---|---|---|
| O26037 | H. pylori 26695 | 385 | 96.5 | `MVAHKMGMNRD...` (= position 15) |
| I0ESJ2 | H. cetorum MIT 99-5656 | 399 | 96.5 | `MHTVLQIGAGGVGSVVAHKMGMNRD` |
| Q17ZI8 | H. acinonychis Sheeba | 399 | 95.7 | `MHTVLQIGAGGVGSVVAHKMGMNRD` |
| B5Z9C5 | H. pylori G27 | 380 | 94.0 | `MGMNRD...` (= position 20) |
| I0EKU9 | H. cetorum MIT 00-7128 | 399 | 93.5 | `MHTVLQIGAGGVGGVVAHKMGLNRD` |
| A0AA90PPK2 | H. cappadocius | 399 | 75.7 | `MNAVLQIGAGGVGGVVAHKLAMNRE` |
| A0A3D8J7L2 | H. anseris | 399 | 74.2 | `MSTVLQIGAGGVGGVVAHKLAKNRE` |
| D3UGV5 | H. mustelae | 399 | 73.4 | `MSTVLQIGAGGVGGVVAHKLARNKQ` |
| A0ABM7SFN6 | H. gastrofelis | 403 | 73.4 | |
| A0A0K2YBB9 | H. heilmannii | 403 | 73.2 | `MLTVLQIGAGGVGRVVAHKLAQNRH` |
| E7ADD4 | H. felis | 403 | 72.4 | `MSVVLQIGAGGVGNVVAHKLCQNRQ` |
| A0A6J4D0M1 | H. suis | 403 | 71.2 | `MLTVLQIGAGGVGSVVAHKLCQNRD` |
| A0A3D8J1F2 | H. brantae | 394 | 71.9 | `MSVLQIGAGGVGGVVAHKLAMNAKT` |

**Only the two H. pylori UniProt entries lack the GxGxxG motif.** They are the outliers.

## 5. 8H52: NADP contacts from residues 1-14 and structural context

All protein atoms within 4.0 A of NAP 501 contributed by residues 1-14:

| Residue | Atom | Moiety | NAP atom | Distance (A) |
|---|---|---|---|---|
| Gly8 | CA | backbone | O4B | 3.95 |
| Ala9 | N | backbone | O3B | 3.29 |
| Ala9 | CA | backbone | O3B | 3.73 |
| Ala9 | C | backbone | O3B | 3.60 |
| Ala9 | O | backbone | O3B | 3.82 |
| Ala9 | CB | side chain | O3B | 3.83 |
| Gly10 | N | backbone | O5B | 3.76 |
| Gly10 | CA | backbone | O5B | 3.05 |
| Gly10 | C | backbone | O1N | 3.46 |
| Gly11 | N | backbone | O1N | 2.91 |
| Gly11 | CA | backbone | O1N | 3.72 |
| Gly11 | C | backbone | O1N | 3.99 |
| Val12 | N | backbone | O1N | 3.26 |
| Val12 | CB | side chain | O5D | 3.75 |
| Val12 | CG2 | side chain | O5D | 3.87 |

**Backbone 12 atoms, side chain 3 atoms (Ala9 CB, Val12 CB/CG2).**
Five residues contact NADP: Gly8, Ala9, Gly10, Gly11, Val12.
Gly13 and Ser14 have no atom within 4.0 A.

Secondary structure in 8H52:
- `SHEET 3 AA1 7 THR A 3 ILE A 7 1 N GLN A 6 O ALA A 33` : Thr3-Ile7 is strand 3 of a
  7-stranded sheet, parallel-paired to Ala33. Interior strand, not a terminal tail.
- `HELIX 1 AA1 GLY A 10 ASN A 23 1 14` : helix A runs Gly10-Asn23. The O26037 start
  (position 15) falls **inside** this helix.

Burial: residues 2-14 make **285 heavy-atom contacts (<4.5 A)** with **33 residues** of the
rest of the chain (20, 26-34, 39, 40, 43, 62, 68, 71, 72, 77-84, 92, 296, 338, 340, 344, 347,
348, 359). Per-residue minimum distance to the core 2.68-4.54 A.

NADP 2'-phosphate specificity patch (for context, outside the segment): Arg35 (NE 2.73 A),
Ser36 (OG 2.38 A), Lys39 (NZ 2.41 A).

## 6. Methods note

Alignments used a plain identity-scored Needleman-Wunsch implemented in the analysis, not a
substitution matrix; percentages are therefore conservative for the distant orthologs and
exact for the near-identical ones. Contact distances are heavy-atom Euclidean distances from
the deposited coordinates with altloc A retained. No structure refinement or re-fitting was done.
