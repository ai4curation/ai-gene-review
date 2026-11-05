# crc (cryptocephal, Drosophila ATF4) - manual literature review

No deep-research API was available; this summary was compiled by hand from cached
publications in `publications/` and PubMed searches ("cryptocephal" OR "Drosophila ATF4").

## Identity
- UniProt M9PBF8 (TrEMBL, unreviewed, 372 aa), FlyBase FBgn0000370, GeneID 47767, CG8669.
- bZIP family (Pfam PF00170; CDD cd14692 bZIP_ATF4; PANTHER PTHR13044 ATF4/5). bZIP domain aa 303-366.
- crc "encodes a Drosophila homolog of vertebrate ATF4, a member of the CREB/ATF family of
  basic-leucine zipper (bZIP) transcription factors" [PMID:10924469].

## Genetics: molting and metamorphosis
- [PMID:10924469, abstract only] crc mutants "display defects associated with larval molting and
  pupariation. In addition, they fail to evert the head and fail to elongate the imaginal discs
  during pupation". Two lethal complementation groups; CRC-A, CRC-B (bZIP) and CRC-D (truncated).
  "In third instar larvae, crc expression is high in targets of ecdysone signaling, such as the leg
  and wing imaginal discs, and in the ring gland".

## Transcriptional activation of ETH in Inka cells
- [PMID:16651547, abstract only] "Expression of Ecdysis triggering hormone (ETH) in the endocrine Inka
  cells requires crc"; "crc activates ETH expression though a 382 bp enhancer"; enhancer regions are
  "imperfect matches to recognition elements for activating transcription factor-4 (ATF-4)". No direct
  DNA-binding assay is described in the abstract.

## Coactivator of the ecdysone receptor isoform B2
- [PMID:22912598, full text] Yeast two-hybrid screen with the EcR-B2 AF1 recovered CRC-A; in vitro
  "Radiolabeled CRC-A bound to the EcR-B2 amino-terminus and to full-length EcR-B2, but not to EcR-B1";
  charge-swap suppression ("CRC-R361E bound EcR-B2-E9K") "strongly implies direct interaction".
  Inka-cell crc RNAi: "larvae with crc RNAi showed a 15-fold or greater reduction in ETH transcript levels".
  Conclusion: "these findings implicate CRC as an isoform-specific transcriptional activator for EcR-B2."
  The interaction surface is the CRC leucine zipper. Binding was "not dependent upon USP or ecdysone".

## Integrated stress response effector
- [PMID:27979906, full text] "GCN2 and its downstream transcription factor, ATF4, mediate 4E-BP
  induction"; "The 4E-BP intron contains ATF4-binding sites"; mutating the putative sites reduced
  stress induction of the reporter; "ATF4 is a major mediator of 4E-BP induction in response to amino
  acid deprivation in Drosophila larvae."
- [PMID:25978358] ATF4 5'UTR uORF translational reporter is induced by starvation and ER stress.
- [PMID:34919148] Crc-GFP protein-trap: "We observed Crc-GFP signal localized to the nucleus in the larval
  fat bodies"; induced by PERK and by phosphomimetic eIF2alpha; hypomorph sensitive to amino acid
  deprivation, with retinal degeneration, wing vein and oocyte defects.
- [PMID:38179767, abstract] crc mutant larvae show altered energy metabolism and ATF4-dependent lipase
  gene expression under nutrient restriction.
- [PMID:42048457, abstract] crc overexpression shortens and knockdown extends adult lifespan.

## Synthesis
CRC is a nuclear bZIP transcription activator of RNA polymerase II genes. It acts downstream of
eIF2alpha kinases (GCN2, PERK) in the integrated stress response, where it activates targets such as
4E-BP/Thor through ATF4 sites. In ecdysone signalling it binds the EcR-B2 AF1 and acts as an
isoform-specific coactivator, driving ETH expression in Inka cells; this explains the ecdysis,
pupariation and head-eversion defects of crc mutants.
