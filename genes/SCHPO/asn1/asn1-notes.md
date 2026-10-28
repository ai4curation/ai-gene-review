# asn1 (SPBC119.10, UniProt P78753) notes

Glutamine-dependent asparagine synthetase (EC 6.3.5.4).

- Reaction: [UniProt:P78753 "Reaction=L-aspartate + L-glutamine + ATP + H2O = L-asparagine + L-"]
- [UniProt:P78753 "DISRUPTION PHENOTYPE: Causes asparagine auxotrophy."] (PMID:17622533)
- Ma et al. 2007 forward screen for auxotrophs (abstract only cached): [PMID:17622533 "cys2 (+) and pha2 (+) were required for biosynthesis of asparagine, cysteine and"] (asn1+ listed as one of three new genes).
- Location: cytoplasm + nucleus by ORFeome GFP [UniProt:P78753 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16823372}. Nucleus"]; HDA cytosol.
- PANTHER PTHR11772:SF2.

## Difference from S. cerevisiae
- S. cerevisiae has redundant ASN1/ASN2: [PMID:8951815 "Simultaneous disruption of both genes leads to a total asparagine auxotrophy, while disruption of asn1 or asn2 alone has no effect on growth under tested conditions."]. S. pombe has a single gene whose loss alone gives auxotrophy. Core function otherwise identical to the ASN1 review (GO:0004066 / GO:0070981 / cytosol).
- GO-CAM 67c10cc400005826: asn1 GO:0004066 in cytosol part_of GO:0070981 — agrees.
- Nucleus (IEA SubCell) kept non-core.


## 2026-10-26 comparative annotation audit

Reviewed all 9 existing rows and the core-function synthesis for SCHPO/asn1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 7, 'KEEP_AS_NON_CORE': 1, 'MODIFY': 1}.

PMID:17622533 identifies native asparagine-auxotrophic asn1 mutants and establishes its biosynthetic requirement in the tested conditions. The abstract explicitly states that asn1 is required for asparagine biosynthesis. The previous universal “sole route” formulation is narrowed rather than inferring exhaustive testing of every nitrogen condition. Conserved glutamine-amidotransferase architecture and curated catalytic chemistry support the existing MF.

Cytoplasm refines to cytosol with the existing imaging/phylogenetic support. The curated additional nuclear location remains a precise non-core localization; no nuclear mechanism is invented. The source's shared amino-acid-marker study is not rejected because it also studies other genes.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP 403 authentication failure; Perplexity returned HTTP 401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-SCHPO-asn1-research.log` and `aspartate-SCHPO-asn1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-SCHPO-asn1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.


## PR #5568 follow-up, 2026-10-26

Repaired authored citation spacing and fused numeric prose while preserving original annotation payloads, every action, raw UniProt/GOA records and all existing supporting quotations. Source-cited passages in notes were protected from rewriting.
