# HSP70-1/HSC70-1 (AT5G02500) Curation Notes

## Current Review Position

HSP70-1/HSC70-1 is a cytosolic and nuclear Hsp70-family molecular chaperone. The
review keeps the core functions focused on ATP-dependent protein folding/refolding
and HSF/HSP101-linked regulation of basal thermotolerance.

## Supported Conclusions

- HSP70-1 performs canonical ATP-dependent Hsp70 chaperone activity in cytosolic
  proteostasis.
- PMID:32573848 supports physical interaction with HsfA1d and HsfA1e in the cytosol
  and a negative-regulatory role upstream of HSP101 and basal thermotolerance.
- The generic HsfA interaction annotations should be represented as
  `GO:0140297 DNA-binding transcription factor binding`, not unfolded protein binding.
- Positive cytosol/cytoplasm/nucleus localization annotations are retained.
- The negated RCA cytosol annotation is removed because `NOT located_in cytosol`
  conflicts with the positive cytosol evidence and should not be interpreted as
  "not exclusively cytosolic."

## Context-Specific Non-Core Roles

SGT1/immune, stomatal closure, ABA/seed germination, mRNA-binding, protease-binding,
and high-throughput localization annotations are retained only where existing GOA
evidence supports them and are treated as non-core or context-specific.

## Non-Retained Draft Claims

Earlier notes proposed clathrin uncoating as a current HSP70-1 curation conclusion.
That Perplexity-only mechanism is not retained in the YAML review; the plasma membrane
HDA annotation is kept only as a low-specificity, non-core proteomics localization.
