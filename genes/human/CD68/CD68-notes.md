# CD68 notes

Deep research providers unavailable in this environment (`just deep-research-falcon human CD68
--fallback perplexity-lite` failed). Research from cached publications and UniProt P34810.

## Structure / localization
- Type I single-pass membrane protein; signal 1-21, extracellular 22-319 (mucin-like region 23-140 with
  tandem repeats, then a LAMP-like membrane-proximal domain), TM 320-344, cytoplasmic 345-354.
  [PMID:7680921 "The cDNA sequence predicts a type I integral membrane protein of 354 residues with a heavily
  glycosylated extracellular domain of 298 residues"]; [PMID:7680921 "a membrane proximal domain that has
  significant sequence homology to a family of lysosomal/plasma membrane shuttling proteins known as the lamp 1 group"]
- UniProt: long isoform = endosome membrane + lysosome membrane; short isoform = cell membrane.
- Conclusion: predominantly intracellular (late endosome / lysosome membranes), with a minor
  plasma-membrane pool (isoform- and recirculation-dependent). This matters for surface-targeting:
  CD68 is a classic *permeabilized-section* macrophage marker.

## Function
- Not established. UniProt: "Could play a role in phagocytic activities of tissue macrophages ... Binds to
  tissue- and organ-specific lectins or selectins". Mouse macrosialin is described as an oxLDL-binding protein.
- Human GOA process terms are almost all ISS from mouse P31996 or IBA from the LAMP family; reviewed as
  non-core or UNDECIDED accordingly; no molecular function asserted in core_functions.

## Curation decisions
- Ten HuRI binary protein-binding rows (PMID:32296183) removed per the protein-binding policy.
- lysosome / endosome membrane / membrane / cytoplasmic vesicle membrane rows modified to lysosomal
  membrane and late endosome membrane.
