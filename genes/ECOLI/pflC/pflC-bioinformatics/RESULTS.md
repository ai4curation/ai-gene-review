# Genome context and sequence comparison of E. coli K-12 GRE activase paralogs

Covers the three uncharacterised activase paralogs pflC, ybiY and yjjW, with PflA
and NrdG as characterised references. Shared by the pflC, ybiY and yjjW reviews.

## Method

`activase_context.py` (run with `uv run python activase_context.py > activase_context.out`)
fetches live, with nothing hardcoded:

- the NCBI feature table of E. coli K-12 MG1655 (NC_000913.3), parsed for gene order,
  strand and coordinates (6 genes either side of each activase);
- UniProt sequences of the five activases (PflA P0A9N4, NrdG P0A9N8, PflC P32675,
  YbiY P75794, YjjW P39409) and six GREs (PflB P09373, TdcE P42632, NrdD P28903,
  PflD P32674, YbiW P75793, YjjI P37342), used for pairwise global identity
  (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5; identity over the
  shorter sequence) and for extracting the glycine-loop heptamer (RV.GY pattern in the
  last 80 residues);
- NCBIfam family descriptions from the InterPro API.

Raw output: `activase_context.out`. Gene order and strand are an operon proxy only;
transcription units were not retrieved.

## Results

### 1. Each activase gene is adjacent to, and co-directional with, one GRE gene

| Activase | Adjacent GRE | Strand | Gap |
|---|---|---|---|
| pflA (b0902) | pflB (b0903) | both - | 191 bp |
| nrdG (b4237) | nrdD (b4238) | both - | 157 bp |
| pflC (b3952) | pflD (b3951) | both + | -35 bp (overlap) |
| ybiY (b0824) | ybiW (b0823) | both - | 5 bp |
| yjjW (b4379) | yjjI (b4380) | both - | -29 bp (overlap) |

In each case the GRE gene is upstream of its activase in the direction of transcription.
pflC overlaps the 3' end of pflD by 35 bp and yjjW overlaps the 3' end of yjjI by 29 bp;
ybiY starts 5 bp after ybiW. Such overlapping or near-touching stop/start codons
are typical of translationally coupled genes in one operon.

The pflD-pflC pair lies inside the frw cluster (frwC, frwB, pflD, pflC, frwD). The
divergent genes just upstream are ptsA, fsaB (fructose-6-phosphate aldolase 2) and gldA
(L-1,2-propanediol dehydrogenase/glycerol dehydrogenase). ybiY is divergent from fsaA
(fructose-6-phosphate aldolase 1). FsaA, FsaB and GldA are the downstream enzymes of the
anhydroglycolysis pathway that starts with YbiW and PflD (PMID:39283600).
yjjW-yjjI is flanked by unrelated genes (yjjV hydrolase; the deo operon, divergent).

### 2. The PflC/YbiY and PflD/YbiW pairs are paralogous sets

Pairwise global identities (% of the shorter sequence):

- Activases: PflC-YbiY 37.3, the highest pair. Each of the three uncharacterised
  activases is only 24-33% identical to PflA or NrdG. YjjW is not closer to PflC/YbiY
  (24.4/26.1) than to PflA (32.5).
- GREs: PflB-TdcE 79.1 (the two known PflA substrates); PflD-YbiW 41.3; every other
  pair, including PflD or YbiW against PflB, is 21-29%.

So PflD/YbiW and their activases PflC/YbiY form a second, PFL-distinct pair of
paralogous operons. PflD and YbiW are no closer to PFL (26.7/26.8% identity) than
YjjI is (26.6%).

### 3. Glycine-loop heptamers

```
pflB   RVSGYAV  (Gly 735, UniProt numbering)
tdcE   RVSGYAV  (Gly 739)
nrdD   RVCGYLG  (Gly 681)
pflD   RVAGYSA  (Gly 741)
ybiW   RVAGYSA  (Gly 786)
yjjI   RVTGYMV  (Gly 465; 51 residues from the C-terminus of a 516-residue protein)
```

PflD and YbiW share one Gly-loop heptamer, RVAGYSA, which differs from the PFL/TdcE
loop (RVSGYAV) at three of seven positions. GRE activases recognise their substrate
largely through the Gly-loop sequence. PflA activates a PFL-loop peptide but not an
RNR-loop peptide, and cross-activation is reported only between GREs with the same or
nearly the same loop (PMID:42361324). On this basis PflC and YbiY would be expected to
serve PflD and YbiW, which share one loop and so could be served by either activase.
PflA, whose characterised substrates both carry RVSGYAV, would not be expected to
serve them. These are predictions; no activation of PflD or YbiW by a named activase
was verified here (see Limitations).

### 4. NCBIfam family text

- TIGR02494 (glycyl-radical enzyme activating protein; YbiY's NCBIfam family) says the
  E. coli PFLC and PFLE (YbiY) proteins "appear to lack characterization and may
  activate enzymes with distinctive functions".
- TIGR04041 (YjjW family glycine radical enzyme activase) says the family is "paired
  with and appear[s] to activate a glycyl radical enzyme of unknown function,
  designated YjjI" and that "Members of this family may be misannotated as pyruvate
  formate lyase activating enzyme."
- NF007483 (PflC's NCBIfam match) is named "[formate-C-acetyltransferase]-activating
  enzyme" and has no description. The name follows the historical "PFL2" label of
  PflD rather than any shown PFL activity.

## Conclusions

1. Each of pflC, ybiY and yjjW sits in an apparent two-gene GRE + activase unit with
   pflD, ybiW and yjjI respectively, in the same arrangement as pflB-pflA and nrdD-nrdG.
2. PflD and YbiW are not pyruvate formate-lyases: they are paralogous C-O lyases of
   1,5-anhydrohexitol 6-phosphates (PMID:39283600). Their Gly loop differs from PFL's.
   The PFL-specific activity term ([formate-C-acetyltransferase]-activating enzyme,
   EC 1.97.1.4) on PflC and YbiY therefore names the wrong substrate GRE. The general
   glycyl-radical enzyme activating activity remains well supported by family
   membership and genome context.
3. YjjW's partner YjjI is a truncated, GRE-like protein with an internal Gly loop and
   unknown function. Only the general activase term is warranted.

## Limitations

- The Ma et al. 2024 full text (PMID:39283600) could not be accessed: the cache is
  abstract-only and the publisher returned 403. Whether PflC or YbiY was the activase
  used to load radicals on PflD and YbiW in vitro, and whether ybiY/pflC deletions were
  tested for growth on 1,5-anhydroglucitol/1,5-anhydromannitol, is not known here.
- Operon structure is inferred from gene order and spacing only.
