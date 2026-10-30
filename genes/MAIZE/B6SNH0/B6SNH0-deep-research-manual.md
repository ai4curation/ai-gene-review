# B6SNH0 (ZmbZIP60) - manual literature research

No deep-research API was available in this session, so this summary was compiled by hand
from PubMed searches (query `ZmbZIP60 OR (bZIP60 AND maize)`, 14 hits) and the cached
publications in `publications/`.

## Identity

- UniProt B6SNH0 (TrEMBL, 300 aa, "BZIP transcription factor protein"), NCBI GeneID
  100280864. NCBI Gene lists the aliases ZEAMMB73_Zm00001d046718 and GRMZM2G025812 and the
  designation "bZIP transcription factor 60".
- Zm00001d046718 is the locus used for ZmbZIP60 by the Howell laboratory
  [PMID:30008724 "ZmbZIP60 (Zm00001d046718)"].
- The 300-aa length equals the protein predicted from unspliced ZmbZIP60 mRNA
  [PMID:22417282 "The unspliced mRNA is predicted to encode a type II membrane protein of
  300 AA with a single transmembrane domain (TMD)"]. B6SNH0 is therefore the unspliced,
  membrane-anchored precursor form.

## Domain architecture (UniProt B6SNH0 record)

- bZIP domain 139-202 (PROSITE PS50217), coiled coil 157-184, InterPro IPR004827/IPR046347,
  Pfam PF00170, CDD cd14704 (bZIP_HY5-like). PANTHER PTHR47416:SF8.
- A hydrophobic stretch around residues 221-240 (LPLVSLLWLVSIVCLFLMPV) corresponds to the
  predicted TMD of the unspliced form; the record carries no FT TRANSMEM line, and its ER
  membrane/transmembrane keywords rest on ARBA only.

## Mechanism: IRE1-type unconventional splicing

- ZmbZIP60 mRNA contains a twin-loop structure resembling the IRE1 recognition site and is
  spliced in response to ER stress, excising a 20-nt intron [PMID:22417282 "A segment of the
  mRNA encoding ZmbZIP60 in maize can be folded into a twin loop structure, and in response to
  ER stress this mRNA is spliced, excising a 20b intron."].
- Splicing causes a frameshift: the spliced form encodes a 258-aa protein lacking the TMD
  and carrying a putative NLS [PMID:22417282 "the spliced form is predicted to encode a
  protein of 258 AA lacking a TMD, but having acquired a putative nuclear targeting signal
  (NLS)"]. This spliced protein is not represented by any UniProt entry.
- Splicing is elicited by DTT and tunicamycin and by heat (42 C), but not by CPA, hypoxia,
  cold, NaCl, dehydration or ABA under the conditions tested [PMID:22417282].
- The maize IRE1 responsible was not identified experimentally; maize has two IRE1
  orthologs [PMID:22417282].

## Transcription factor activity

- GFP fused to a truncated ZmbZIP60 lacking the TMD (ZmbZIP60deltaC) is nuclear; both full
  length and truncated forms show transcriptional activity in yeast one-hybrid assays
  [PMID:22307781, abstract only].
- ZmbZIP60 expressed in an Arabidopsis bzip60 mutant partially restores tunicamycin
  induction of BiP3 [PMID:22307781 "The expression of ZmbZIP60 in Arabidopsis bzip60 mutant
  partially restored the induction of BiP3 transcription under TM treatment"].
- ZmBIPb is upregulated by ER stress with kinetics lagging bZIP60 splicing, but direct
  regulation was not shown [PMID:22417282 "It is still unclear whether ZmbZIP60 is directly
  involved in the upregulation of ZmBIPb by ER stress."].
- In maize, a bzip60-2 knock-down mutant blunts the heat shock response; the HSFTF13
  (HSFA6B family) promoter and promoters of chlorophyll catabolism/chloroplast protein
  turnover genes are targets of bZIP60 in maize protoplasts [PMID:32843434, abstract only].

## Expression and natural variation

- ZmbZIP60 transcription is induced by dehydration, salinity, ABA and tunicamycin
  [PMID:22307781].
- A cis-acting QTL in the ZmbZIP60 promoter makes tropical lines (CML52-type promoters)
  upregulate ZmbZIP60 more robustly under heat than B73 [PMID:30008724].
- Splicing is increased by paclobutrazol plus elevated temperature [PMID:31316112] and by
  expression of 16-kDa gamma-zein in Arabidopsis (for AtbZIP60) [PMID:34618077].
- Autophagy loss (atg10) does not change heat-induced bZIP60 splicing in maize
  [PMID:41318379].

## Comparators

- Arabidopsis bZIP60 (Q9C7S0) carries experimental GO annotations for DNA-binding
  transcription factor activity (IDA), nucleus (IDA), ER membrane (IDA) and ER unfolded
  protein response (IMP/IEP) in QuickGO (queried 2026-10-28).
- Metazoan functional analog: XBP1, the IRE1 splicing target.
