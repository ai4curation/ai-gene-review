# TFR2 review notes

## 2026-07-19

- Seeded 40 grouped review entries from 43 QuickGO rows with
  `just fetch-gene human TFR2`; all source rows are represented by the grouped YAML.
- Cached all nine GOA-cited PMIDs. PMID:29388418 contains full text; the other GOA-cited
  papers are abstract-only in the local cache. Experimental annotations were therefore
  not overruled on absent assay detail; decisions use the accessible abstract plus the
  holistic evidence base.
- OpenScientist attempt 1 timed out after 600 seconds without producing a provider file.
  A second requested attempt was launched. Manual synthesis is recorded in
  `TFR2-deep-research-manual.md`; no provider-named report was authored manually.
- Added cached primary studies PMID:20576915 (human hepatocyte iron sensing) and
  PMID:20177050 (hepatocyte-targeted Hfe/Tfr2 rescue in mice) to cross-check the systemic
  hepcidin-regulatory role.
- Curatorial gestalt: membrane TFR2-alpha binds transferrin and can mediate endocytic iron
  uptake, but its defining physiological function is to sense transferrin saturation in
  an HFE/HJV-associated hepatocyte membrane complex and promote the hepcidin response.
  Cytoplasmic localization belongs to transmembrane-domain-lacking isoform beta and is
  non-core.
- Planned non-ACCEPT decisions: modify transferrin-backed `protein binding` to
  transferrin receptor activity; modify HFE-backed generic binding to the specific
  HFE-transferrin receptor complex; mark HuRI and CD81 generic binding as over-annotated;
  keep HFE maturation and beta-isoform cytoplasm as non-core.
