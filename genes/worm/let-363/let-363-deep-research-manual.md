# let-363 (CeTOR; UniProt Q95Q95) - manual literature synthesis

No deep-research provider was available for this review; this summary was compiled
by hand from cached publications (`publications/PMID_*.md`) and the UniProt record
(`let-363-uniprot.txt`). Each claim carries its provenance.

## Identity and domain architecture

- let-363 (B0261.2) encodes the single C. elegans Target of Rapamycin homolog, a
  2697-aa PI3K-related kinase (PIKK) with N-terminal HEAT repeats, a FAT domain,
  an FRB (FKBP12-rapamycin binding) domain, the PI3K/PI4K catalytic domain and a
  C-terminal FATC domain [file:worm/let-363/let-363-uniprot.txt, "DOMAIN 2332..2647 /note=\"PI3K/PI4K catalytic\""; "Belongs to the PI3/PI4-kinase family"].
- PANTHER places it in PTHR11139:SF9 (SERINE/THREONINE-PROTEIN KINASE MTOR); InterPro
  IPR026683 (TOR catalytic domain) [uniprot file].

## Molecular function: protein serine/threonine kinase

- Native C. elegans TORC1 (immunoprecipitated via endogenous DAF-15::mCherry, in
  which LET-363 was the most abundant interactor and no other kinase was detected)
  phosphorylated peptides from ALY-2, RSP-6, VAV-1 and EPG-3 in vitro
  [PMID:35479415 "Among the eighteen candidates tested, four peptides were identified as direct TORC1 targets by this strategy"; "Importantly, no other kinases were identified in the IP preparations"].
- Long et al. 2002 suggested that CeTOR acts as a protein kinase regulating
  translation [PMID:12225660 abstract; UniProt CC FUNCTION].

## Complexes: TORC1 and TORC2

- Epitope-tagged LET-363 co-immunoprecipitated both DAF-15/Raptor and RICT-1/Rictor,
  while DAF-15 and RICT-1 did not co-precipitate each other, defining two complexes
  [PMID:21952218 "the LET-363 IP contained both DAF-15 and RICT-1 (Fig. 2b). On the other hand, the DAF-15 IP contained LET-363 but not RICT-1, whereas the RICT-1 IP contained LET-363 but not DAF-15"].
- Semaphorin/plexin signalling shifts LET-363 partner choice from RICT-1 to DAF-15
  [PMID:21952218 "the SMP signal through PLX-1 serves to promote a shift of the LET-363-associated adaptor from RICT-1 towards DAF-15"].
- Endogenous DAF-15 IP-MS recovered LET-363 as main partner [PMID:35479415 "The most abundant of these interactors was LET-363/Tor"].

## Biological roles (mostly loss-of-function genetics)

- Translation / growth: loss of let-363 causes mid-to-late L3 arrest with intestinal
  atrophy attributed to inhibition of global mRNA translation [PMID:12225660
  "TOR is a major upstream regulator of overall mRNA translation in C. elegans, as in yeast"].
  let-363 RNAi halves 35S incorporation [PMID:18804378 "Reduction of let-363 led to a 50% decrease in 35S incorporation"].
- Nucleolus / ribosome biogenesis: let-363 inactivation reduces FIB-1 levels and
  mislocalizes box C/D snoRNPs out of the nucleolus [PMID:18804378 "Inactivation of let-363/TOR produced similar defects, with low levels of FIB-1, which were localized to the nucleoplasm and nucleolar periphery"]. This is a readout downstream of TOR signalling; LET-363 has not been shown to bind or assemble snoRNPs.
- Lifespan: reduced let-363 extends adult lifespan [PMID:14668850 (abstract not available in cache); PMID:18804378 "Reduction of let-363 and daf-15 together led to a statistically-significant increase in lifespan"; PMID:17277769 "Knockdown of target of rapamycin (TOR) ... further increases the longevity of ife-2 mutants"].
- Autophagy: let-363 RNAi increases autophagic (LGG-1::GFP) puncta [PMID:18282106 "we observed a significant increase in the number of autophagic vesicles in their L3 progeny"]. EPG-3/VMP1 is a direct in vitro TORC1 substrate [PMID:35479415].
- Postembryonic development / nutrient sensing: an mmBCFA-derived glucosylceramide
  promotes L1 growth through intestinal TORC1 [PMID:23705068 "this lipid function is mediated by TORC1 and antagonized by the NPRL-2/3 complex in the intestine"]; LET-363 is described as "a key component of both TORC1 and TORC2" [PMID:23705068].
- Germline progenitors: let-363 or daf-15 reduction depletes the larval germline
  progenitor pool, similar to rsks-1; ife-1 double loss [PMID:22278922].
- TORC2 context: inactivation of TORC2 components partly suppresses skn-1 embryonic
  lethality; let-363 RNAi had only a mild effect (1.1% viable vs 0%) [PMID:23973804 "genetic inhibition of the TOR kinase let-363 only had a mild effect on skn-1 associated lethality"].
- Male ray morphogenesis: ray-specific let-363 RNAi phenocopies plexin mutants [PMID:21952218].

## Localization

- WormBase IDA cytoplasm and UniProt nucleus both cite Long et al. 2002 (abstract only
  in cache; the localization data could not be checked). Ubiquitous expression
  [UniProt CC TISSUE SPECIFICITY].
