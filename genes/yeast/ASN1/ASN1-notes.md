# ASN1 notes

- Glutamine-dependent asparagine synthetase, EC 6.3.5.4 [UniProt "Reaction=L-aspartate + L-glutamine + ATP + H2O = L-asparagine + L-"].
- Two biochemically similar, probably cytosolic AS enzymes [PMID:6105958 "the occurrence of two L-asparagine synthetases"; "Neither one is located in mitochondria and both are probably cytosolic."].
- Redundant: only asn1 asn2 double mutant is auxotrophic [PMID:8951815 "Simultaneous disruption of both genes leads to a total asparagine auxotrophy"]; both Gcn4-dependent; HAP complex specifically regulates ASN1 [PMID:8951815 "was shown to specifically affect ASN1 expression"].
- Asn1-Asn2 co-purify in HTP AP-MS (PMID:16429126, PMID:37968396): protein binding REMOVED as uninformative (interaction not disputed).
- Asn1 forms starvation-induced cytoophidia docking with Ura7/Prs5 filaments [PMID:39836171 "Prs5, Ura7, and Asn1 exhibited a starvation-induced cytoophidium forming pattern"]; kept non-core.


## 2026-10-26 comparative annotation audit

Reviewed all 14 existing rows and the core-function synthesis for yeast/ASN1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 10, 'REMOVE': 2, 'MODIFY': 1, 'KEEP_AS_NON_CORE': 1}.

PMID:6105958 identifies two biochemically similar enzymes: “Neither one is located in mitochondria and both are probably cytosolic.” PMID:8951815 reports asparagine auxotrophy after double disruption, while either single disruption grows in the tested conditions; the compensation claim is limited accordingly. The N-terminal glutaminase and ATP-dependent synthetase architecture support the glutamine-dependent amidation already annotated. No ammonia-only donor preference is invented.

PMID:39836171 full text contains Asn1-tagged cytoophidium complexes with Ura7 and Prs5; this conditional assembly remains non-core. Cytoplasm is refined to the independently supported cytosol. The two bare protein-binding rows follow the current project policy: REMOVE as uninformative, without denying the reported paralog association or inferring an obligatory functional heterocomplex from proteomics alone. No new interaction-derived MF is asserted.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP403 authentication failure; Perplexity returned HTTP401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-ASN1-research.log` and `aspartate-yeast-ASN1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-ASN1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.
