# Native bacterial aspartate-to-threonine audit

The module represents three complete, separately scoped native routes: Pseudomonas putida KT2440, Escherichia coli K-12 and Corynebacterium glutamicum ATCC 13032. A P. aeruginosa PAO1 ThrH reaction is an optional comparison. The 20-gene panel includes three PSEPK paralogs whose physiological contribution remains unresolved; they cannot satisfy required canonical steps in this conservative model.

Run from the repository root:

```sh
uv run python modules/bacterial_aspartate_to_threonine_biosynthesis-source-analysis/check_module.py
uv run python modules/bacterial_aspartate_to_threonine_biosynthesis-source-analysis/check_routes.py
```

Both commands write deterministic YAML results under `analysis/module_audits/bacterial_aspartate_to_threonine_biosynthesis/`. `members.yaml` records the manually selected scope. The module is curated from literature and reviewed target evidence; these scripts validate it rather than infer enzyme function from family labels.

`check_module.py` uses the production module validator with a bounded index from unchanged target UniProt records. It checks exact accessions/taxa, actual PANTHER membership and official labels, source quotations, gene-function conformance, covered members, and evidence on every activity and connection. The beta LysC product is not assigned the full-length catalytic family. Free-text chain roles and the unreviewed family-level ThrH function can produce documented advisories; the actual activities have GO identifiers and target gene evidence.

`check_routes.py` combines the production Boolean compiler with an explicit native-product, chain and supplied-resource predicate. The compiler does not itself infer taxonomy, expand protein complexes or simulate metabolite propagation. The predicate excludes foreign proteins and requires both LysC alternative-initiation products. ATP, NADPH, water and PLP are boundary resources; homoserine is an internal intermediate for complete routes and an external input for isolated ThrH. Twelve edges independently check that each principal reaction product is the next reaction's substrate. These are capacity checks under stated assumptions, not knockout growth predictions or a quantitative flux model.

The 49 cases cover complete and incomplete native routes, unresolved paralogs, E. coli isozyme redundancy and the indispensable Asd reaction between fused domains, LysC chains, cofactors, and phosphoserine-dependent ThrH. Removing a canonical PSEPK member makes this model incomplete; it does not assert that a candidate paralog can never compensate biologically.

Source identity and access limits are in the module notes and individual gene notes. In particular, native construct identities from PMID:40236303 are checked by the committed primer analysis under `genes/PSEPK/PP_4473/PP_4473-bioinformatics/primer-identity/`; terminal matches are not full-CDS verification. Historical coryneform and Pseudomonas assays are not relabeled as experiments on the exact sampled strains. A disputed source claim that ThrA replaces Asd is retained only as an assessed finding.

The broader `aspartate_family_threonine_biosynthesis` module remains a distinct comparative mechanism model. This audit supplies concrete bacterial implementations and a bounded member review; it does not replace that broader model or claim universal presence in Bacteria.
