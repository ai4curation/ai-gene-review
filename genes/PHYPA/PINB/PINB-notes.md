# Moss PINB evidence notes

## Identity
A9RN82 is PpPINB, locus Pp3c24_2970/LOC112276308, RefSeq XP_024363256.1. PMID:36696950 publisher text maps this locus separately from PINA Pp3c23_10200 and PINC Pp3c10_24880; the normally fetched UniProt cross-reference agrees. PINC-specific spermatogenesis evidence is not assigned here.

## Export, redundancy and polarity
PMID:25448003 full text establishes native PINA/PINB redundancy with targeted disruptants (which retain residual transcripts) and a stronger PINB contribution to measured sporophyte defects. Reporter redistribution is not a direct molecular-flux assay. PMID:25448004 author PDF adds heterologous moss-PIN IAA transport assays and native pinA pinB media-export reduction, together supporting PINB's exporter role. The direct H3-IAA assay in PMID:37528584 tests PINA and MpPINZ, NOT PINB; it is not cited as a PINB-specific transport assay.

PMID:37528584 examines native-promoter PINB-GFP: more even PM distribution and an intracellular pool without visible tip polarity. Older rice-actin-promoter overexpression in PMID:25448004 gave stronger tip polarity; this expression/context difference is preserved. No universally polarized PINB or complete Arabidopsis-like polarity machinery is inferred.

## ER and reviewed scope
The intracellular signal is not identified as ER. The old heterologous PINA ER observation does not identify PINB. PAINT PTN001589272's ER ancestral judgment remains unresolved for PINB, without claiming that positive PM localization contradicts it. All five seeded rows are retained; generic membrane and transport terms are refined with substrate-specific support. No NEW.

## Review method and access (2026-10-26)

All original rows were reviewed individually from the seeded YAML. Only review judgments were changed; original terms, labels, evidence, source references, supporting entities, qualifiers and flags are retained. Provider/publication jobs were run by the coordinating agent in parallel: all normal publication jobs completed; genuine Falcon and perplexity-lite attempts failed authentication (shared log `.cache/module-audit-logs/auxin-polar-fetch/provider-publication-results.json`). No provider report was fabricated or used as primary evidence. Additional primary retrievals used normal `just fetch-pmid` or `ReferenceFetcher` URL acquisition. No raw source cache was hand-edited. No GOA file was used as functional support.

References below are source-specific: full-text availability is recorded in each normal publication cache. `PMID:37528584` was recovered after a real initial HTTP 429 and a later successful retry. The full author PDF of `PMID:25448004` was normally acquired from https://folia.unifr.ch/documents/304040/files/gei_dat.pdf; its PMID cache remains abstract-only. Wiley publisher pages for `PMID:36696950` and `PMID:36880411` were inspected through the web reader; normal direct URL acquisition attempts returned 403, so their PMID caches remain abstract-only. This difference is not concealed by modifying the cached PMID record.

The comparison distinguishes cellular export into culture medium from native directional tissue flow. It does not infer a complete AUX1/ABCB/AGC-kinase circuit in rice, moss or liverwort from transporter conservation or phosphorylation motifs. Core descriptions remain gene biology, with these workflow limits kept here.

## 2026-10-26 — independent follow-up on native phyllid development

Normally fetched full PMID:41984944 (Lin et al., 2026) resolves a developmental-stage distinction: PINA/PINB lack clear basal polarization during early phyllid growth; the previously reported polar/bipolar pattern occurs in differentiated nongrowing tip cells from 3.5 days after initiation. Both proteins have a membrane fraction facing extracellular space. R2D2 sensing in independent CRISPR double mutants and growth measurements support limiting intracellular auxin, with outward export inferred from localization and physiology. The growth model explicitly did not model auxin transport. These results refine scope without disproving native protonemal tip polarity or transporter activity. No new GO assertion or changed action is needed.

For PINB, the 2014 family-level tobacco-protoplast assays are not treated as an independently verified PINB-specific flux measurement without its construct-level supplement; native double-mutant export and paralog-specific genetic/localization evidence remain available.
