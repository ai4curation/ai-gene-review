# Moss PINA evidence notes

## Identity
Q5TK28 is PpPINA, current locus Pp3c23_10200/LOC112276099, RefSeq XP_024362879.1. PMID:36696950 publisher text gives the current PINA/PINB/PINC locus crosswalk, consistent with the normally fetched UniProt genomic cross-reference. That paper's PINC-specific reproductive findings are not transferred to PINA. Physcomitrium patens is the current name of the organism commonly called Physcomitrella patens in the papers.

## Distinct assays
PMID:25448003 full text uses native targeted disruptants; residual transcripts mean these lines should not automatically be called molecular nulls. Double-mutant growth, reporter, shoot-tropism and sporophyte phenotypes support partly redundant PINA/PINB action. PINA has the stronger auxin-sensitive gametophore contribution; PINB has a stronger contribution to the measured sporophyte abnormalities. These are not interchangeable paralogs. The anti-Arabidopsis-PIN antibody localization is not uniquely PINA-specific.

PMID:25448004 author PDF includes heterologous tobacco-protoplast radioactive IAA export by moss PINs, native media export in overexpressors and a slight reduction in pinA pinB, and native-promoter PINA-GFP polarized at moss filament tips. PMID:37528584 full text directly measures increased H3-IAA release after inducible PINA-GFP expression in moss; it also shows native-promoter tip polarity, basal/apical young-leaf polarity and less polarized basal-leaf localization. These experiments support exporter MF and native context-dependent transport, not a universally canalized shoot axis.

## ER claim
PAINT PTN001589272 ER IBD from Arabidopsis PIN5/6/8 is an ancestral claim, not a pairwise transfer. PMID:25448003 discusses the historical tobacco-protoplast PINA ER observation but finds native PIN staining separate from BIP2. Both the heterologous context and antibody specificity matter. Native functional ER residence remains unresolved; PM positivity does not prove ER absence. No IBA loss or erroneous node is claimed. All five seeded rows are preserved; broad transporter and BP are refined to auxin export, with no NEW.

## Review method and access (2026-10-26)

All original rows were reviewed individually from the seeded YAML. Only review judgments were changed; original terms, labels, evidence, source references, supporting entities, qualifiers and flags are retained. Provider/publication jobs were run by the coordinating agent in parallel: all normal publication jobs completed; genuine Falcon and perplexity-lite attempts failed authentication (shared log `.cache/module-audit-logs/auxin-polar-fetch/provider-publication-results.json`). No provider report was fabricated or used as primary evidence. Additional primary retrievals used normal `just fetch-pmid` or `ReferenceFetcher` URL acquisition. No raw source cache was hand-edited. No GOA file was used as functional support.

References below are source-specific: full-text availability is recorded in each normal publication cache. `PMID:37528584` was recovered after a real initial HTTP 429 and a later successful retry. The full author PDF of `PMID:25448004` was normally acquired from https://folia.unifr.ch/documents/304040/files/gei_dat.pdf; its PMID cache remains abstract-only. Wiley publisher pages for `PMID:36696950` and `PMID:36880411` were inspected through the web reader; normal direct URL acquisition attempts returned 403, so their PMID caches remain abstract-only. This difference is not concealed by modifying the cached PMID record.

The comparison distinguishes cellular export into culture medium from native directional tissue flow. It does not infer a complete AUX1/ABCB/AGC-kinase circuit in rice, moss or liverwort from transporter conservation or phosphorylation motifs. Core descriptions remain gene biology, with these workflow limits kept here.

Normal fetch of the historical PMID:19506555 succeeded with abstract only (no PMC record). It establishes that an early moss PIN ER observation existed, but does not independently resolve construct-specific native PINA residence; the later full study provides the named-PINA discussion. This limitation is retained in the ER review.

## 2026-10-26 — independent follow-up on native phyllid development

Normally fetched full PMID:41984944 (Lin et al., 2026) resolves a developmental-stage distinction: PINA/PINB lack clear basal polarization during early phyllid growth; the previously reported polar/bipolar pattern occurs in differentiated nongrowing tip cells from 3.5 days after initiation. Both proteins have a membrane fraction facing extracellular space. R2D2 sensing in independent CRISPR double mutants and growth measurements support limiting intracellular auxin, with outward export inferred from localization and physiology. The growth model explicitly did not model auxin transport. These results refine scope without disproving native protonemal tip polarity or transporter activity. No new GO assertion or changed action is needed.

For PINB, the 2014 family-level tobacco-protoplast assays are not treated as an independently verified PINB-specific flux measurement without its construct-level supplement; native double-mutant export and paralog-specific genetic/localization evidence remain available.
