# nuc-1 (C. elegans, Q17778) curation notes

No deep-research provider keys were available; these notes were assembled manually
from Europe PMC searches (query `"nuc-1" AND elegans`, ~197 hits) and the cached
publications. All PMIDs below were verified against Europe PMC and cached with
`ai-gene-review fetch-pmid`.

## Identity

- NUC-1 = C07B5.5, WBGene00003828; 375 aa, N-terminal signal peptide 1-21
  (UniProt FT SIGNAL, predicted), one predicted N-glycosylation site; DNase II family
  (Pfam PF03265, InterPro IPR004947, PANTHER PTHR10858:SF31). One of three DNase II
  paralogs in C. elegans (NUC-1, CRN-6, CRN-7).

## Enzyme activity

- Classical biochemistry: nuc-1 mutants have <1% of the major worm DNase activity
  [PMID:3228446 "Three independent mutations in the nuc-1 gene were shown to reduce
  nuclease activity to less than 1% of that seen in wild-type organisms."]. The
  enzyme makes nicks and double-strand breaks, prefers dsDNA, and is
  cation-independent and EDTA-insensitive (DNase II-like) [PMID:3228446].
- Cloning: [PMID:10903446 "wild-type animals contained a potent endonuclease activity
  with a cleavage preference similar to DNase II, while nuc-1 mutant worms
  demonstrated a marked reduction in this nuclease activity"]; e1392 is a nonsense
  allele, and the C07B5.5 transgene complements it.
- Acidic pH optimum: NUC-1 in excretory/secretory products degrades extracellular
  DNA, with maximal activity at pH 6 [PMID:37523858; PMID:40349596 "environmental pH
  specifically modulates NUC-1 activity rather than expression"].

## Apoptotic DNA degradation

- [PMID:10716942 "Mutations in nuc-1 allowed the generation of TUNEL-reactive DNA but
  blocked the conversion of TUNEL-reactive DNA to a subsequent TUNEL-unreactive
  state."] Completion of degradation needed engulfment in that study.
- [PMID:19809494 "nuc-1 plays a major role, crn-6 plays an auxiliary role, and crn-7
  plays a negligible role in resolving 3' OH DNA breaks generated in apoptotic
  cells"]. NUC-1 is secreted and acts across its expression border; the signal
  peptide is needed. Lai et al. found engulfment-defective mutants did not block
  nuc-1-mediated TUNEL resolution and argued NUC-1 can act inside apoptotic cells,
  while also allowing action in phagocytes.
- [PMID:26182365] ToLFP probe: DNase II-generated ends are reduced most in nuc-1
  embryos. Estimates a ~3:7 autonomous:non-autonomous ratio; anteriorly expressed
  NUC-1 acts in posterior blastomeres "in a non-autonomous and secretion-dependent
  manner".
- [PMID:26251453] Germline apoptosis: NUC-1 (pachytene) and CRN-7 (loop) act
  sequentially; loss raises antimicrobial gene expression (abf-2, spp-1, nlp-29,
  cnc-2, lys-7), plausibly through ERK activation by undigested DNA, an indirect
  effect.
- 2026 preprint (Europe PMC PPR1304135, not cached, not peer reviewed; noted only):
  NUC-1 acts exclusively in engulfing cells in the phagosomal lumen. NUC-1 is not
  in nuclei of apoptotic or live cells, apoptotic nuclei are not acidic, and
  blocking lysosome-phagosome fusion blocks degradation of apoptotic chromatin.
  This resolves the Lai 2009 versus Wu 2000 disagreement in favour of a
  phagolysosomal site.

## Localization

- Lysosome: WormBase IDA from Guo et al. 2010 [PMID:20921409] (abstract only).
  NUC-1::mCHERRY is a standard lysosome/phagolysosome marker [PMID:22822152 "Using
  NUC-1::mCHERRY, which labels lysosomes (8, 9)"].
- Secreted: signal peptide needed for transport out of the pharynx and for
  non-autonomous rescue [PMID:19809494]. NUC-1 is present in excretory/secretory
  products [PMID:37523858].
- Nucleus (TAS, PMID:10716942): nothing supports the enzyme being in the nucleus. The
  substrate is nuclear chromatin, but the enzyme is a signal-peptide-bearing acid
  hydrolase. Marked as over-annotation.

## Other roles

- Degrades DNA of ingested bacteria in the intestinal lumen (classic Nuc phenotype:
  Syto-11-stainable gut), and only NUC-1 among the three DNase IIs does this
  [PMID:19809494].

## Decisions summary

- DNase II activity (GO:0004531): ACCEPT on all rows.
- DNA endonuclease activity (IEA ARBA): MODIFY to GO:0004531.
- DNA metabolic process (IEA): MODIFY to DNA catabolic process / apoptotic DNA
  fragmentation.
- Apoptotic DNA fragmentation (GO:0006309): ACCEPT. NUC-1 directly cleaves apoptotic
  DNA (late step, after CAD-like nicking).
- Negative regulation of AMP production: KEEP_AS_NON_CORE (indirect).
- Lysosome: ACCEPT. NEW lysosomal lumen (IC: signal peptide, no TM segment, acidic
  optimum, lysosomal IDA). NEW extracellular region (IDA, secretion).
