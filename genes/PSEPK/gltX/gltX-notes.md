# gltX curation notes

- Q88LF6 is a reviewed class I glutamate--tRNA ligase that directly charges
  tRNA(Glu) [file:PSEPK/gltX/gltX-uniprot.txt, "Catalyzes the attachment of
  glutamate to tRNA(Glu)"].
- The exact record does not establish tRNA(Gln) misacylation. That route remains
  a PSEPK-specific knowledge gap because KT2440 also encodes GlnS.
- The InterPro-derived zinc-binding annotation was removed after a reproducible
  alignment to zinc-binding *E. coli* GluRS P04805 showed that Q88LF6 lacks the
  complete four-cysteine cluster [file:PSEPK/gltX/gltX-bioinformatics/RESULTS.md,
  "Q88LF6 therefore does not preserve the four-cysteine zinc-binding cluster present in P04805."].

## 2026-10-26 complete annotation reassessment

GltX is a cytosolic class-I glutamyl-tRNA synthetase that activates glutamate with ATP and attaches it to tRNA(Glu) for translation. Its conserved catalytic architecture includes the HIGH and KMSKS regions. Its putative zinc-binding region differs at two positions from the characterized E. coli and P. aeruginosa canonical coordination sites.

Exact accession Q88LF6 and KT2440 symbol/locus were checked against the immutable UniProt record and current fetched identity snapshot. All original machine-seeded row fields and order are preserved. Actual Falcon/fallback attempts failed; no provider report was fabricated. Normal publication caching completed; FEBA retrieval was attempted but no data source was reachable.

The target biochemical assignment rests on curated HAMAP/family and site evidence, augmented by the source-specific comparative papers below. No generic family label is treated as a native kinetic assay. Ordinary relationship metadata does not negate a real complex contribution; contributes_to cores explicitly represent shared catalytic work. Integral substrate/cofactor binding and the supported intracellular location are not classified as peripheral solely because they are binding or location. Current QuickGO retires the amino-acid-specific BP terms; original ids/labels remain unchanged and reviews use current supported process replacements.

- PMID:7797500: The E. coli GluRS canonical site contains three cysteines and one histidine, correcting the legacy four-cysteine interpretation.
- PMID:25686371: Domain-swapped E. coli constructs separate metal binding from catalytic requirement; native structural absence and a hypothetical target binding capacity are not equivalent.
- PMID:14729703: Native PAO1 uses direct GlnRS and indirect Asn formation; its GatABC also transamidates supplied heterologous Glu-tRNA(Gln) in vitro. Do not infer native KT2440 Gln-transamidation flux from that capacity.

The prior four-cysteine rationale is corrected by the regenerated bioinformatics analysis. Canonical ligand divergence is real, but the broader native zinc-binding claim is UNDECIDED without a metal-content/affinity experiment. Native absence of structural occupancy, binding capacity and catalytic metal requirement are different questions.
