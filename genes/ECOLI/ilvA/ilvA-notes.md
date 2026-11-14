# ilvA (P04968, E. coli K-12) review notes

No provider deep research was run for this gene. These notes are my own,
built from the cached publications in `publications/`, the UniProt record
(`ilvA-uniprot.txt`) and the existing reviews of the same pathway step
(`genes/PSEPK/ilvA-I`, `genes/PSEPK/ilvA-II`, `genes/yeast/ILV1`,
`genes/SCHPO/tda1`).

## Identity and function

- Biosynthetic L-threonine dehydratase (threonine deaminase), EC 4.3.1.19,
  514 aa, last gene of the ilvGMEDA operon. UniProt: "Catalyzes the anaerobic
  formation of alpha-ketobutyrate and ammonia from threonine in a two-step
  reaction" [file:ECOLI/ilvA/ilvA-uniprot.txt, CC:FUNCTION, ECO:0000269 PMID:13405870].
- Committed step of isoleucine biosynthesis: "2-oxobutanoate from
  L-threonine: step 1/1" [UniProt CC:PATHWAY].
- PLP enzyme: "The catalytic activity of threonine deaminase is absolutely
  dependent on the presence of pyridoxal phosphate, and the tetrameric molecule
  is isolated containing 1 mol of cofactor/56,000-Da chain" [PMID:2005118].
  Lys62 Schiff base (UniProt MOD_RES, ECO:0000269 PMID:9562556 structure).
- Allostery: "The negative allosteric effector L-isoleucine strongly inhibits
  the enzyme ... whereas enzyme activity is greatly increased by L-valine"
  [PMID:2005118]. Two C-terminal ACT-like domains (UniProt FT DOMAIN);
  "an amino-terminal domain that is involved in catalysis and a carboxy-terminal
  domain that is important for regulation" [PMID:8407838].
- Genetics: inactive ilvA alleles fail "to complement an ilvA deletion strain
  to isoleucine prototrophy" [PMID:8407838]; intragenic complementation
  restores "threonine deaminase activity in vivo" [PMID:4604254].
- Two threonine deaminases in E. coli: PMID:13405870 (title; abstract not
  cached) separated biosynthetic IlvA from the biodegradative, AMP-activated
  TdcB (P0AGF6, verified via UniProt REST).

## Serine side reaction (KT2440 standard)

- E. coli GOA has no L-serine catabolic process or L-serine ammonia-lyase row
  for IlvA, so the KT2440 MARK_AS_OVER_ANNOTATED decision has no row to apply
  to here. E. coli has dedicated L-serine dehydratases, all verified by UniProt
  REST on this date: SdaA (P16095, b1814), SdaB (P30744, b2797), TdcG (P42630,
  b4471). PMID:30327426 names biosynthetic IlvA as "a significant generator of
  2AA in the bacteria Salmonella enterica, Escherichia coli, and Pseudomonas
  aeruginosa". I did not propose a NEW serine row for the same reasons as the
  KT2440 review.

## Questionable reference attribution

- PMID:5321308 (Phillips & Wood 1965), cited for the PLP-binding IDA row and
  the UniProt COFACTOR line, is titled "The mechanism of action of
  5'-adenylic acid-activated threonine dehydrase". AMP activation is the
  hallmark of the biodegradative TdcB, not IlvA (IlvA is regulated by
  isoleucine/valine). UniProt cites the same paper on TdcB (P0AGF6), which
  carries AMP-binding features. The PLP claim is true for IlvA on other
  evidence, so the row is accepted and the reference recorded as a suspected
  source defect (UniProt, CHECK).

## Other rows

- PMID:348689 (IMP, BCAA biosynthesis) studies aminoacyl-tRNA synthetase
  regulation in ilvDAC deletion and ilvA point mutants; the process supported
  by an ilvA mutant is isoleucine biosynthesis, so the broad BCAA term was
  modified to L-isoleucine biosynthetic process (as for the IEA row).
- Abstract-only/no-abstract papers (PMID:4573981, PMID:5321308,
  PMID:13405870): Europe PMC full text was not available (HTTP 500 for the
  PMC ids tried). Experimental rows whose function is clearly correct were
  accepted, deferring to the curators.

## Threonine catabolic process

- I did not propose L-threonine catabolic process (GO:0006567) for IlvA,
  although the KT2440 IlvA reviews accept it. The PTHR48078 family review limits
  it to the catabolic dehydratases and flags the KT2440 reading as broader than
  PAINT's and yeast ILV1's. E. coli has dedicated catabolic routes (TdcB,
  among others), so the IDA L-threonine metabolic process row is kept as
  non-core and the GO:0006520 row is modified to L-isoleucine biosynthetic
  process only.
