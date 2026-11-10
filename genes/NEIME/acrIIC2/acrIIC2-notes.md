# acrIIC2 evidence audit

## 2026-10-25

Identity: A0A425B3G2, tax487 Neisseria meningitidis; RefSeq WP_042743678.1; PDB 6N05/6J9K/6J9L/6J9M. The bacterial source taxon records an inhibitor discovered in a mobile-element context and does not imply a viral UniProt assignment. PMID:31243272 shows no inhibition when sgRNA is prebound; prebinding inhibitor to apo-Cas9 gives complete inhibition at a 2:1 ratio, while simultaneous addition requires substantially more inhibitor. These assay-dependent results must not become a universal molar-excess requirement. PMID:30850331 supports activity across tested Cas9 orthologues with variable potency, not all Cas9. The assembly target is apo-Cas9, so a requirement for binding assembled RNP would invert the mechanism.

Normal accession-specific fetch-gene produced the source caches and seeded review. Falcon deep research with perplexity-lite fallback failed; see `.cache/module-audit-logs/anti-crispr-deep-NEIME-acrIIC2.log`. This is manual primary-literature research, not a provider-generated research file. Publications were fetched through the normal fetch-pmids workflow and full texts inspected where available. No source cache was hand-edited.

The inhibitor itself performs the interference-blocking step, so the process assignment is based on biochemical participation, not solely deletion/rescue necessity. GO:0098672 is already used for experimentally characterized inhibitors in the same role (AcrIIC1, AcrIIA4, AcrIF2); no redundant parent process is proposed. Conservatively proposed only the essential inhibitor molecular function and, where absent, this specific process. Generic binding and inferred cellular locations are not added as separate NEW rows.
