# Ofut1 (O-fut1, neurotic; UniProt Q9V6X7) notes

Directory named `O-fut1` (FlyBase synonym used by the Notch module brief); the
current FlyBase/UniProt symbol is `Ofut1` (FBgn0033901), recorded as `gene_symbol`.
Fetched with `just fetch-gene DROME Q9V6X7 --alias O-fut1`.

## Deep research
`just deep-research-falcon DROME Q9V6X7 --alias O-fut1 --fallback perplexity-lite`
was launched (2026-09-30). The wrapper hit its 600 s timeout and the
perplexity-lite fallback is not configured ("Provider 'perplexity' not
available"). See end of file for final status. Review is based on cached
publications and UniProt.

## Key findings
- Enzyme: O-fucosylates Ser/Thr in EGF repeats of Notch and ligands
  [PMID:12526814 "Notch and its ligands are modified by a protein O-fucosyltransferase (OFUT1) that attaches fucose to a Serine or Threonine within EGF domains."]
- Required cell-autonomously in the signal-receiving cell, upstream of Notch activation; overexpression inhibits
  [PMID:12526814 "The requirement for Ofut1 is cell autonomous, in the signal-receiving cell, and upstream of Notch activation."]
- Needed for Delta-Notch and Serrate-Notch binding; generates the Fringe substrate
  [PMID:12909620 "Down-regulation of OFUT1 by RNA interference in Notch-secreting cells inhibits both Delta-Notch and Serrate-Notch binding"]
- Maternal neurogenic gene neurotic
  [PMID:12917292 "Neurotic is required for the activity of the full-length but not an activated form of Notch"]
- Notch chaperone, independent of catalysis; ER protein
  [PMID:15692013 "OFUT1 ... also has a distinct Notch chaperone activity."; "This ability of OFUT1 to facilitate folding of Notch did not require its fucosyltransferase activity."]
- Catalytically dead R245A rescues embryonic neurogenesis; O-fucose dispensable for Fringe-independent signalling
  [PMID:18194540 "the chaperone activity of OFUT1 is sufficient for the generation of functional Notch."]
- But O-fucose monosaccharide has a temperature-sensitive essential function, redundant with Rumi O-glucose
  [PMID:25378397 "the monosaccharide O-fucose modification of N has a temperature-sensitive function that is essential for N signaling."]
- Endocytic trafficking of Notch; stable complex with Notch ECD; can act extracellularly
  [PMID:17329366 "O-fut1 formed a stable complex with the extracellular domain of Notch."]

## Review decisions
- Core MF: GO:0046922 peptide-O-fucosyltransferase activity (ER lumen).
- NEW MF: GO:0044183 protein folding chaperone (Notch-selective chaperone; PMID:15692013, PMID:18194540).
- Notch binding (IDA x2) accepted.
- positive regulation of endocytosis / protein localization to cell surface kept non-core (cargo-specific).
- cell fate commitment (intestinal stem cells; PMID:21965616) kept non-core.
- No IBA rows in GOA for this gene. PANTHER PTHR21420 / PTHR21420:SF10.

## Pathway-variant notes
- Fly-specific(?) chaperone role making catalysis dispensable for many Notch events; in mouse Pofut1 the enzyme is required (catalytic role more prominent).

## Deep research final status
Falcon output arrived after the wrapper timeout (`O-fut1-deep-research-falcon.md`); reviewed and cited in the review YAML.
