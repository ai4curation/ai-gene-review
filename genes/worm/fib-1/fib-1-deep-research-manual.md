# fib-1 (Q22053, T01C3.7, WBGene00001423) - manual literature research

No deep-research API was available in this session. This file was compiled by hand from
the cached publications in `publications/` and PubMed searches (query
`fib-1 fibrillarin elegans`, 11 hits, run 2026-10-28). Every claim carries its source.

## Identity and family

- C. elegans FIB-1 is the single fibrillarin ortholog (352 aa). UniProt: "Belongs to the
  methyltransferase superfamily. Fibrillarin family." [file:worm/fib-1/fib-1-uniprot.txt].
  Domain architecture: an N-terminal glycine/arginine-rich (GAR, RG/RGG) domain of ~115
  residues (MobiDB-lite disordered region 1..115, Gly-rich compositional bias) followed by
  the conserved fibrillarin Rossmann-fold SAM-dependent methyltransferase domain
  (Pfam PF01269, PROSITE PS00566, HAMAP MF_00351 RNA_methyltransf_FlpA, PANTHER
  PTHR10335:SF17) [file:worm/fib-1/fib-1-uniprot.txt].
- The RG/RGG repeats of FIB-1 carry the phenylalanine-rich nucleolar motif shared with
  human FBL, NCL and GAR1: "A phenylalanine-rich motif, “FRGGDRGGFR,” was found 2–6 times
  in each of the RG/RGG sequences from nucleolar proteins FIB-1, LPD-6, and Y66H1A.4"
  [PMID:36329008].

## Molecular function (inferred from orthologs; no direct worm biochemistry)

- No enzymatic assay of worm FIB-1 has been published. The catalytic function is
  transferred from yeast Nop1 / human FBL: UniProt FUNCTION (ECO:0000250 from P15646)
  describes "site-specific 2'-hydroxyl methylation of ribose moieties in pre-ribosomal RNA",
  with site specificity from a guide RNA, and methylation of histone H2A Gln-105 (H2AQ105me)
  at rDNA [file:worm/fib-1/fib-1-uniprot.txt].
- Worm papers describe FIB-1 in these terms: "In wild-type animals, FIB-1 is highly
  expressed and localized in the nucleolus, where it methylates pre-rRNAs during ribosome
  maturation" [PMID:23705068]; "nol-5, K07C5.4 and fib-1 encode proteins predicted to be
  members of the Box C/D snoRNP" [PMID:18804378]; "C. elegans fib-1 encodes the highly
  conserved nucleolar methyltransferase fibrillarin, which is a vital factor in the C/D
  small nucleolar ribonucleoprotein (snoRNP) complex" [PMID:30190478].
- Fibrillarin co-distributes with U3 snoRNA in the early embryo (Sasano et al. 2008,
  abstract only): fibrillarin "is an essential component of U3 small nucleolar
  ribonucleoprotein complex" [PMID:18312858].

## Localization (direct worm evidence)

- Nucleolus: anti-FIB-1 immunostaining - "We observed robust FIB-1 in 100% of the nucleoli
  of wild-type animals, and this signal was lost after fib-1(RNAi), indicating the stain was
  specific" [PMID:18804378]. Starvation moves it out: "FIB-1 levels were reduced and
  restricted to the nucleoplasm" [PMID:18804378]. Intestinal nucleolar FIB-1 depends on
  TORC1 activity downstream of mmBCFA/d17iso-GlcCer: "the nucleolar localized FIB-1 was
  dramatically reduced in intestinal cells of mmBCFA-deficient [elo-5(RNAi)] animals"
  [PMID:23705068].
- Embryo: before zygotic genome activation FIB-1 labels nucleoplasmic foci; "At the 2-cell
  stage, the DAO-5 and FIB-1 antibodies label numerous dots of varying size and intensity
  throughout the nucleoplasm"; nucleoli form at the 6-8-cell stage [PMID:22768349].
- Sub-nucleolar: C. elegans nucleoli have two phase-separated compartments; "C. elegans
  nucleoli contain 2 phase-separated compartments, with NUCL-1 and LPD-6 in the GC and FIB-1
  and GARR-1 in the FC" [PMID:36329008]. (In amniotes FBL marks the DFC; the worm "FC" as
  defined by these authors is the fibrillarin-containing inner compartment.) FIB-1 FC
  organisation depends on the NUCL-1 RG/RGG domain [PMID:36329008].

## Genetic / phenotypic evidence

- fib-1 is essential: "fib-1 mutation led to lethality" (fib-1(ok2527)); mutant L1 nucleoli
  are small [PMID:26492166]. "full FIB-1 RG/RGG deletion does not provide viable worms"
  [PMID:36329008].
- rRNA pool: "knockdown of FIB-1 led to an overall reduction in the rRNA levels"
  [PMID:26492166]; "fib-1 RNAi reduces the levels of 26S and 18S rRNA in worms"
  [PMID:30190478].
- Translation: fib-1 RNAi reduces 35S-methionine incorporation by ~20% [PMID:18804378] and
  puromycin incorporation [PMID:30190478], interpreted as a consequence of reduced ribosome
  biogenesis.
- Regulation of fib-1 itself: NCL-1 (TRIM-NHL) with PUF/NOS represses fib-1 translation via
  its 3'UTR; let-7 represses ncl-1 - the let-7-ncl-1-fib-1 cascade sets nucleolar size and
  rRNA abundance [PMID:26492166]. Longevity pathways reduce FIB-1 and nucleolar size; "fib-1
  RNAi knockdown reduced nucleolar size and extended lifespan of wild-type worms"
  [PMID:28853436]. fib-1 knockdown enhances resistance to S. aureus and E. faecalis
  [PMID:30190478]. These are downstream organismal consequences, not activities of FIB-1.
- Neuron size laterality (ASEL/ASER) depends on asymmetric FIB-1-containing nucleoli
  (Goldsmith et al. 2010, PMID:21122110, not cached; from PubMed abstract).

## Assessment

The core, well-supported biology is the conserved catalytic role of FIB-1 as the
methyltransferase of box C/D snoRNPs (rRNA 2'-O-ribose methylation) and its role in early
pre-rRNA processing (U3 snoRNP/SSU processome), located in the nucleolar fibrillar
compartment. Histone H2A Gln methylation is plausible by homology but untested in worms.
Translation, lifespan, immunity and nucleolar-size phenotypes are indirect consequences
of ribosome biogenesis capacity.
