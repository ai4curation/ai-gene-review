# ASN2 notes

- Glutamine-dependent asparagine synthetase, EC 6.3.5.4 [UniProt "Reaction=L-aspartate + L-glutamine + ATP + H2O = L-asparagine + L-"].
- Two biochemically similar, probably cytosolic AS enzymes [PMID:6105958 "the occurrence of two L-asparagine synthetases"; "Neither one is located in mitochondria and both are probably cytosolic."].
- Redundant: only asn1 asn2 double mutant is auxotrophic [PMID:8951815 "Simultaneous disruption of both genes leads to a total asparagine auxotrophy"]; both Gcn4-dependent; HAP complex specifically regulates ASN1 [PMID:8951815 "was shown to specifically affect ASN1 expression"].
- Asn1-Asn2 co-purify in HTP AP-MS (PMID:16429126, PMID:37968396): protein binding REMOVED as uninformative (interaction not disputed).


## 2026-10-26 comparative annotation audit

Reviewed all 13 existing rows and the core-function synthesis for yeast/ASN2; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 10, 'REMOVE': 2, 'MODIFY': 1}.

PMID:6105958 and PMID:8951815 support the second glutamine-dependent asparagine synthetase and compensation with Asn1 in the tested growth conditions. The latter differentiates ASN1 HAP-complex regulation from ASN2 regulation; compensation does not mean every regulatory or physiological role is identical. The soluble-enzyme cytoplasmic term is refined to the independently supported cytosol.

The two generic protein-binding rows are removed under the standing bare-binding policy, not because the recorded Asn1 association is false. Neither a specific regulatory activity nor obligatory heterocomplex is inferred from the interaction records. No new cytoophidium annotation is transferred from Asn1 to Asn2.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP403 authentication failure; Perplexity returned HTTP401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-ASN2-research.log` and `aspartate-yeast-ASN2-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-ASN2-*`. Final results and machine-payload proof are in the panel validation/payload manifests.
