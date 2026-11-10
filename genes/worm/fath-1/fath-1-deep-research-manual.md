# fath-1 (C25A1.5; UniProt Q9XVS0) - manual literature research

No deep-research provider was run for this gene (no API keys available in this
environment). This file records a manual literature survey done with PubMed
searches and the cached publications in `publications/`.

## Search strategy

- PubMed: `fath-1 elegans` (0 hits), `2-hydroxy fatty acid Caenorhabditis elegans hydroxylase`
  (1 hit, PMID:30184537), `FATH-1 OR C25A1.5 OR "fatty acid 2-hydroxylase" elegans` (1 hit, PMID:30184537).
- Papers cited by PMID:30184537 for earlier fath-1 phenotypes were traced by title
  (PMID:21926990 tubular polarity screen; PMID:19023415 immunity, which on full-text
  inspection does not name fath-1/C25A1.5 in the cached text and is not used).
- PMID:23705068 (key experimental paper named by the task) and PMID:14992718 (GOA IPI source).

## Identity and family

- UniProt Q9XVS0 is an unreviewed TrEMBL entry, 316 aa, named by PIRNR rule
  "Fatty acid 2-hydroxylase"; it belongs to the sterol desaturase family, SCS7 subfamily
  (PIRSF005149; InterPro IPR014430 Scs7; PANTHER PTHR12863:SF1 FATTY ACID 2-HYDROXYLASE)
  [file:worm/fath-1/fath-1-uniprot.txt "Belongs to the sterol desaturase family. SCS7 subfamily."].
- Domain architecture: N-terminal cytochrome b5 heme-binding domain (residues 1-78, axial
  heme ligands at 29 and 61) and a C-terminal fatty acid hydroxylase domain (PF04116) with
  four predicted (Phobius) transmembrane helices (128-149, 161-182, 219-237, 243-267) and
  the histidine-rich di-metal centre ligands (183, 188, 206, 209, 210, 264, 268, 285, 288, 289;
  PIRSR005149-1) [file:worm/fath-1/fath-1-uniprot.txt].
- "Fatty acid two-hydroxylase 1 (FATH-1) is the sole C. elegans homolog for mammalian FA2H,
  whose corresponding gene number is C25A1.5" [PMID:30184537].

## Experimental literature in C. elegans

### Li et al. 2018 (PMID:30184537), full text
- GFP::FATH-1 translational reporter is expressed in embryos, larvae and adults, in neurons,
  intestine and epidermis; "most FATH-1 proteins were uniformly distributed in the cytoplasm,
  with moderate enrichment in the nuclei" [PMID:30184537]. This is a whole-cell resolution
  observation; no ER co-marker was used.
- fath-1 RNAi from L1 causes growth retardation and shortened lifespan; intestine-specific RNAi
  phenocopies systemic RNAi, epidermis-specific RNAi does not [PMID:30184537 "When fath-1 was
  inactivated only in the intestine, it affected the worm growth in a similar degree as when
  systemic knockdown was applied."].
- Product rescue: "(R)-2-OH FA supplement nicely rescued the growth defect caused by fath-1 RNAi,
  while (S)-2-OH FA did not" [PMID:30184537]. This is genetic/chemical-complementation
  evidence that the in vivo product is an (R)-2-hydroxy fatty acid; no enzyme assay with
  FATH-1 protein was done.
- fath-1 RNAi reduces lipid droplets, causes aggregation of peroxisomes and of RAB-7 / RAB-11
  apical endosomes in the intestine; ER, Golgi, mitochondria and lysosome markers unaffected
  [PMID:30184537].
- Fatty acid profiling: "loss of FATH-1 function significantly decreased the relative percentage
  of C17:1 (m/z 494) in total FAs" and Delta10-C17:1 supplementation rescues growth [PMID:30184537].
  The mechanistic link between 2-hydroxylation and C17:1 (possibly alpha-oxidation of 2-OH C18
  species) is not established.

### Zhu et al. 2013 (PMID:23705068), full text
- "fath-1(C25A1.5) encodes a homolog of mammalian fatty acid 2-hydrolase (FA2H) responsible for the
  synthesis of the FA side chain of ceramides" [PMID:23705068] ("hydrolase" is a typo for hydroxylase).
- fath-1 RNAi causes L1 arrest that is not rescued by d17iso-sphinganine, like cgt-1;cgt-3, and
  is suppressed by nprl-3(ku540) [PMID:23705068 "As shown above, RNAi of fath-1, or mutating both
  cgt-1 and cgt-3, caused larval arrest that could not be rescued by feeding with either mmBCFAs or
  d17iso-SPA"]. The authors place FATH-1 upstream of d17iso-glucosylceramide in a
  sphingolipid-TORC1 pathway controlling postembryonic development. Evidence is epistatic,
  not biochemical.

### Zhang et al. 2011 (PMID:21926990), full text
- Single knockdown of "a predicted sphingolipid-fatty-acid hydroxylase, C25A1.5" causes the
  intestinal apicobasal polarity conversion phenotype, as does cgt-1;cgt-3 double knockdown
  [PMID:21926990].
- Worm GlcCer is "invariably hydroxylated, consistent with the identified sphingolipid fatty-acid
  hydroxylase, C25A1.5" [PMID:21926990]. This supports that 2-hydroxy acyl chains are the normal
  constituent of C. elegans glucosylceramide, though the paper did not measure loss of
  hydroxylation in fath-1(RNAi).

### Tewari et al. 2004 (PMID:14992718), abstract only
- Large-scale Y2H mapping of the DAF-7/TGF-beta network; source of the FATH-1-DAF-3 IPI
  (IntAct EBI-360227/EBI-326363). The interaction is from a Y2H screen; its physiological
  relevance for an ER-membrane enzyme is unclear.

## Gaps
- No in vitro enzyme assay of FATH-1; substrate preference (free fatty acid vs ceramide-bound acyl
  chain) is not established in worm.
- Subcellular localisation of FATH-1 has not been resolved to ER by co-localisation.
