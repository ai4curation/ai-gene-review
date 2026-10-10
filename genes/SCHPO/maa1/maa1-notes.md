# maa1 (SPBC725.01, UniProt O94320) notes

Mitochondrial aspartate aminotransferase; = classical glu1 (glutamate-requiring) locus.

- Reaction (by similarity to S. cerevisiae Aat1 Q01802): [UniProt:O94320 "Reaction=L-aspartate + 2-oxoglutarate = oxaloacetate + L-glutamate;"]
- Location: [UniProt:O94320 "SUBCELLULAR LOCATION: Mitochondrion matrix"] (ECO:0000269, PMID:16823372); predicted N-terminal transit peptide.
- Kitamura 2024 (full text cached): [PMID:39502420 "maa1 , encoding a mitochondrial aspartate aminotransferase, is the causative"] gene of glu1; glu1-NS176 is an R176 opal nonsense allele, rescued by integrated maa1+ and by sup3-5 suppressor; multicopy yhm2 (mitochondrial 2-oxoglutarate carrier) weakly suppresses; caa1+ does not.
  - Direction: [PMID:39502420 "However, mitochondrial Maa1 has a pivotal role in glutamate synthesis by promoting the reaction in an opposite direction"]; [PMID:39502420 "Since this reaction can proceed in both directions, the same enzyme also supplies glutamate by catalyzing the reverse reaction."]
  - [PMID:39502420 "growth defects in this mutant may be related to glutamate, but not aspartate, shortage."]

## S. pombe-specific difference from S. cerevisiae AAT1 review
- AAT1 review core BP = L-aspartate biosynthetic process (matrix). For maa1 the S. pombe genetics point to the glutamate-forming direction, so core BP chosen = GO:0097054 L-glutamate biosynthetic process (MODIFY of the ISS "glutamate metabolic process" row). IBA L-aspartate catabolic process (same direction) ACCEPTED.
- PomBase GO-CAM 67c10cc400005826 has maa1 part_of GO:0006532 (aspartate biosynthesis) and GO:0043490 (shuttle); the IC GO:0006532 row is kept as non-core.

## Other
- Shuttle (IC/ARBA) non-core: plausible by analogy (S. cerevisiae aat1 respiratory deficiency, PMID:22010850) but untested in S. pombe.
