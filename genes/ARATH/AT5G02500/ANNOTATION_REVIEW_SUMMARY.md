# HSP70-1/HSC70-1 (AT5G02500) Annotation Review Summary

## Current Review Position

The YAML review treats HSP70-1 as a cytosolic/nuclear Hsp70 chaperone with a core
ATP-dependent protein-folding role and a supported regulatory role in basal
thermotolerance through HsfA/HSP101 control.

## Key Decisions

- Retain ATP hydrolysis, ATP binding, protein folding chaperone, protein folding,
  protein refolding, and unfolded-protein binding annotations where supported.
- Retain cytoplasm, cytosol, and nucleus annotations supported by positive evidence.
- Remove the negated RCA cytosol annotation because it asserts `NOT located_in
  cytosol` and conflicts with positive localization evidence.
- Modify HsfA1d/HsfA1e physical-interaction annotations to
  `GO:0140297 DNA-binding transcription factor binding`.
- Keep immune, stomatal, seed-germination, mRNA-binding, and protease-binding
  annotations as non-core or context-specific when supported.
- Keep plasma membrane HDA localization as non-core proteomics evidence without
  asserting an AT5G02500-specific clathrin-uncoating mechanism.

## Non-Retained Draft Recommendations

Earlier draft summaries proposed `GO:0051082 unfolded protein binding` for HsfA
interactions and framed clathrin uncoating as a current curation conclusion. Those
recommendations are not retained.
