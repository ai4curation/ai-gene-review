# DOT5 (YIL010W, P40553) notes

Module context: `glutathione_thioredoxin_redox_systems`, thiol_peroxidase_step, variant bcp_prx (DOT5, S. pombe bcp1), MF GO:0140824, BP GO:0042744, nucleus. Not in the YeastPathways summary; no RCA rows; no S. cerevisiae GO-CAM.

## Evidence
- BCP/PrxQ subfamily, 215 aa, monomer, atypical 2-Cys (intramolecular disulfide) [UniProt:P40553].
- Activity: [PMID:12730197 "Replacement of Cys-106 or Cys-111 with serine resulted in a complete loss of thioredoxin-linked peroxidase activity."]; [PMID:12730197 "nTPx preferentially reduced alkyl-hydroperoxides rather than H2O2."].
- Localisation and naming: [PMID:10681558 "Three novel isoforms showed a distinct thiol peroxidase activity supported by thioredoxin, and appeared to be distinctively localized in cytoplasm, mitochondria, and nucleus."].
- Physiology: [PMID:12730197 "these data demonstrate that nTPx is a thiol peroxidase family acting as alkyl-hydroperoxide reductase in the nucleus during post-diauxic growth"].
- Chromatin: [PMID:42423308 "Here, we show that Dot5 directly interacts with nucleosomes in vitro, and its HMGN-like motif and the nucleosome acidic patch are critical for this engagement."]; overexpression phenotypes [PMID:42423308 "Further, the increased expression of Dot5 in yeast compromises heterochromatin function, genome stability, and cell growth in an HMGN-dependent manner."].

## Issues
- PMID:2408019 (IDA nucleus) is an E. coli aroP sequence paper: wrong identifier. Annotation content is right; accepted with WRONG_IDENTIFIER flag.
- IBA cytoplasm: over-propagated from bacterial BCPs; DOT5 is nuclear.
- IEA telomeric region from UniProt ECO:0000305 inference; chromatin-wide nucleosome binding is better supported -> over-annotated.
- Module uses GO:0042744 hydrogen peroxide catabolic process for DOT5; DOT5 prefers alkyl hydroperoxides, so H2O2 catabolism is a weak fit. Core BP here set to cell redox homeostasis only.

## Decisions
- Obsolete GO:0008379 -> MODIFY GO:0140824. Nucleosome binding / chromatin -> KEEP_AS_NON_CORE. NOT protein stabilization accepted.
