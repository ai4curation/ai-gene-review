# fng (Fringe, Q24342) — curation notes

Drosophila melanogaster, FBgn0011591, CG10580. 412 aa, type II Golgi membrane protein,
GT31 family. PANTHER PTHR10811 (FRINGE-RELATED); the UniProt record lists no PANTHER
subfamily line.

## Notch role: Fringe O-fucose beta1,3-GlcNAc-transferase (signal-receiving cell)

- Activity [PMID:10935626 "Drosophila and mammalian Fringe proteins possess a fucose-specific
  beta1,3 N-acetylglucosaminyltransferase activity that initiates elongation of O-linked
  fucose residues attached to epidermal growth factor-like sequence repeats of Notch."];
  [PMID:10935637 "Fringe catalyses the addition of N-acetylglucosamine to fucose"].
- Acts in Golgi, DxD motif required; secreted form inactive [PMID:10899003].
- Sufficiency of GlcNAc addition: [PMID:17923477 "the addition of N-acetylglucosamine onto
  O-fucose in vitro is sufficient both to enhance Notch binding to the Delta ligand and to
  inhibit Notch binding to the Serrate ligand."]
- Site selectivity on Notch EGF repeats [PMID:27268051]; also modifies Dl/Ser in vitro
  [PMID:12036964]; in vivo Fng product extended with GlcA [PMID:18725413].
- Genetic: cell-autonomously inhibits Ser response and potentiates Dl response
  [PMID:9202123]; boundary of fng expression positions Notch activation at wing D/V boundary
  [PMID:7954826, PMID:7671307], eye equator [PMID:9834035], leg joints [PMID:9806911,
  PMID:10357895], ovarian polar cells [PMID:11493544]. Modulates cis interactions too
  [PMID:25255098]. Can also positively affect Ser signalling [PMID:23152840].

## Pathway variant notes
- Drosophila has a single Fringe; mammals have LFNG, MFNG, RFNG with differing effects
  (e.g. RFNG/LFNG enhance DLL1 and inhibit/enhance JAG1 differently). C. elegans lacks
  Fringe. Requires prior O-fucosylation by O-fut1 (Pofut1).

## Annotation decisions
- MARK_AS_OVER_ANNOTATED: GO:0048100 wing disc anterior/posterior pattern formation (based on
  ectopic ptcGal4>fng at the A/P boundary, not an endogenous role).
- All other annotations accepted or kept as non-core developmental processes.

## Deep research
- falcon run rate-limited initially; relaunched with longer timeout.
