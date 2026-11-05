# GS–GOGAT native-route checks

The module has four alternative native-organism implementations: PSEPK, ECOLI, BACSU and AZOBR. Each requires one exact GlnA product and an assembled GOGAT catalytic unit containing both exact large and small chains. The original six PSEPK/ECOLI exemplars are retained. Bacillus uses gltA for the large chain and gltB for the small chain. The three AZOBR sequences have Sp7 genomic provenance, while the cited physiological and biochemical preparations have separately recorded strain limits.

`members.json` records the 12 reviewed products, immutable raw-source paths, taxon, subunit role and official family classification. `family-verification.json` records independent PANTHER release 19 and current UniProt assignments: six panel proteins occur in the retrieved release-pinned organism classifications; all 12 independently agree with UniProt and their immutable records. The official labels agree with `interpro/panther/panther.obo`. The NADH wording of PTHR11938:SF133 does not establish donor specificity of an individual protein. This bounded verification is not installed or represented as a release-wide PANTHER member cache.

Run:

```sh
uv run python modules/bacterial_ammonia_assimilation-source-analysis/check_module.py
uv run python modules/bacterial_ammonia_assimilation-source-analysis/check_routes.py
```

The first check invokes the production module validator with the independently verified member index and exact reviewed-gene index. It also checks every family, exact-product selector, taxon, reaction, active unit and connection for identity and evidence placement. It does not replace ontology/source validation with a custom mock resolver.

The second check uses the production Boolean compiler with an explicit assembly-aware predicate. Its independent expected result is whether any one native triple is complete. All 4,096 subsets are tested, including incomplete assemblies and cross-organism combinations. Exactly 1,695 subsets contain at least one complete native triple; 2,401 do not. The compiler itself treats each complex as an activity atom and does not infer its active-unit requirements or shared cellular context. Separate counterexamples document why either bare atom accession matching or “any one chain present” is an insufficient oracle. Presence means catalytic capacity; these tests do not establish expression, flux, physical assembly in an arbitrary sample or growth sufficiency.

Detailed outputs, source retrieval failures, source hashes and publication candidates are under `.cache/module-audit-logs/ammonia-module-review/`. Those logs are not cited as biochemical evidence. Every step and reciprocal metabolite link instead cites primary reaction evidence, with review synthesis and exact-target domain/rule evidence distinguished explicitly.
