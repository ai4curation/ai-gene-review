# Bacterial cellulose comparative audit

The module distinguishes common polymerization from five support/envelope architectures. The reviewed panel covers21 genes across Pseudomonas, Rhodobacter, Agrobacterium, E. coli, Komagataeibacter, cyanobacteria and Streptomyces. Seventeen curated references include three comparative reviews.

Run `uv run python modules/bacterial_cellulose_biosynthesis-source-analysis/check_audit.py` from the repository root to verify original annotation payloads and raw hashes and replay23 scenarios through the production module compiler. These are checks of the reviewed panel, not exhaustive genome capacity predictions. Family names alone do not establish chemistry. The synthetic GT2 negative case tests the functional restriction; it is not a claim about an actual inactive CslA.

`seed-baseline.yaml` retains88 original payloads, including one inherited NEW row. Eleven newly proposed annotations are separate. `provider-source-preservation.yaml` records12 unchanged existing research artifacts. `selector-scope-findings.yaml` records corrections to family constraints and database prose.

TypeIII and cyanobacterial envelope roles are deliberately unresolved required obligations, reported as abduction targets. They must not become empty compiler branches that silently evaluate true. Native cellulose production in these organisms is not contradicted by incomplete machinery coverage. The Streptomyces route establishes binary-complex cellulose synthesis in vitro; native glycan composition remains unresolved. E. coli intact/repaired BcsQ and the native K12 pseudogene fragment are distinct scenarios.

`validation-results.yaml` records focused checks and the separately tracked repository-wide run. No pending run is represented as a pass. Existing PR2143 is adopted rather than replaced by a new cellulose PR.
