# Csal_1000 review notes

## 2026-11-06 native-locus comparative audit

Persistent marker DMG-CHRI1-Csal_1000-20261106. Normal accession-aware fetch was frozen before edits in non-psepk/CHRI1-Csal_1000-baseline.json. Default Falcon failed403; these are manual notes. All seed payloads/raw files remain untouched.

The exact UniProt target/domain and native0998–1001 gene arrangement support an inferred alpha subunit. Full PMID32631860 reports locus involvement, citing2017PMID28660361. Public publisher figures were inspected: they label ΔsarC and Δcsal1415, but accessible captions/methods do not map sarC to each0998–1001gene. No four-independent-deletions claim is made. No purified target-subunit assay is invented.

The existing sarcosine oxidase term is retained for the conditional folate-free complex reaction. Core GO0016647 is a contribution, and the specific THF-forming NTR remains a collective proposal. No NEW rows were added solely for module coverage.


## PR #6122 round-1 gene follow-up (2026-11-06)

- Retain the supported alpha subunit role and existing cofactor core, if any; use the same subunit-specific versus complex-contribution convention without filling unsupported cofactor slots.
- Record provenance-specific WRONG_QUALIFIER correction queries (enables to contributes_to) on original sarcosine-oxidase rows; keep all original qualifiers and actions unchanged.

Schema compatibility does not establish an isolated-subunit reaction. The common convention preserves supported catalytic, structural, and cofactor distinctions and marks ortholog transfers explicitly. All historical non-review payloads, inherited NEW actions, and raw/provider bytes remain unchanged; no annotation rows were added or deleted and no publication cache was refreshed.
