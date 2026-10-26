# AZOVI algE: alginate polymerization/export review

## Identity and scope

Q44497, 484 aa; full-length X86533/CAA60245.1 from strain E (PMID8936313). X98863/CAA67371.1 supplies only residues 1–128 from ATCC 9046 (PMID9368366); the complete record is not a fragment. Secondary accession P94201. Specific IPR025388 and IPR053728 AlgE export/channel domains; no PANTHER cross-reference. All records retain species-level NCBITaxon:354; none is silently relabeled as strain DJ.

## Source-specific findings

- [PMID:8936313](https://pubmed.ncbi.nlm.nih.gov/8936313/): Strain E export AlgJ, now called AlgE, is localized to the outer membrane by recombinant expression and native immunodetection. The abstract supports channel homology/topology, not direct native alginate translocation measurements.
- [PMID:9368366](https://pubmed.ncbi.nlm.nih.gov/9368366/): Provides the ATCC 9046 N-terminal 1–128 sequence portion and operon context; functional disruption is of AlgK, not AlgE.

## Annotation decisions

- GO:0009279 (IEA): ACCEPT. The primary study identifies recombinant protein in the E. coli outer membrane and a corresponding native Azotobacter outer-membrane protein by immunodetection. This is stronger than the location-vocabulary mapping alone. The historical 18-strand model is not treated as an experimentally determined structure.
- GO:0042121 (IEA): ACCEPT. Specific AlgE-family identity, the native alginate locus and outer-membrane localization support direct export-system participation. It is not an epimerase or polymerase. Native polymer translocation through purified Q44497 was not demonstrated in the accessible original study; that detailed mechanism remains a homolog-based inference.

No cached GO-CAM index match for this accession. Original source/evidence/term fields were preserved. No NEW process annotations were proposed. Live QuickGO definitions were checked for reaction specificity; AlgL GO:0045135 is a descendant of both seeded generic lyase terms. Alg8 substrate corrections are lateral, not ontology-ancestry claims. For AlgG, exact polymer epimerase chemistry is represented by a supported proposed term rather than a guessed GO identifier.

## Research provenance

Applied review, annotation-reviewer and core-function-synthesizer guidance. Default Falcon deep research and fetch-gene-pmids ran concurrently. Falcon failed authentication (403); Perplexity-lite fallback failed with insufficient_quota (401). No provider report was fabricated. Fitness retrieval was attempted but no reachable FEBA source or local AZOVI mapping yielded data; no fitness artifact was written. These failures are missing evidence, not negative phenotypes. Logs are /tmp/azovi-poly-algE-deep.log and /tmp/azovi-poly-algE-fitness.log. Manual primary research and curated-record assessments supply the review.

## Verified family selector labels

IPR053728 — Alginate Permeability Channel-forming (homologous superfamily); IPR025388 — Alginate export domain (domain). Actual membership is present in the target UniProt cross-references; official InterPro labels/types were checked against the live InterPro API. No PTN evolutionary placement is inferred.

## Inferred transport MF

Added one conservative ISS NEW GO:0015159 row. Specific target AlgE export/channel family, native outer-membrane localization and the curated probable alginate-pore assignment support the inferred molecular function. [PMID:21778407](https://pubmed.ncbi.nlm.nih.gov/21778407/) supplies Pseudomonas homolog structure/halide-flux/loop-complementation evidence. It is neither a native Azotobacter assay nor direct purified-polymer translocation. No BP was added; the two seeded rows and all source fields remain unchanged.


## PR #5552 follow-up, 2026-10-26

Unified the existing-term representation on GO:0015159, whose live definition explicitly covers transfer of polysaccharides across a membrane. Removed the KT2440 alginate-channel NTR because the evidence does not require an additional channel-specific ontology proposal. Pa structure/halide flux/pore-mutant secretion phenotypes (PMID:21778407; PMID:23335756) support an IC molecular-function recommendation, not direct visualization of polymer passage. KT2440 and Azotobacter assignments remain ISS-level homolog inferences. The missing Pa and KT2440 MF rows are nonredundant with their BP/CC rows; no NEW process was added. Normal refetch of PMID:23335756 still returned abstract only, so no full-text-only assay detail was inferred.
