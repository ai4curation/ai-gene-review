# B-cell receptor evidence findings

`evidence-findings.yaml` holds manually assessed review and primary findings for the ongoing module audit. Each record preserves the cached title, a checked source excerpt, the proposed role and explicit assay/taxon/access limits. Records marked `FULL_TEXT` describe cache availability; their assessment says which evidence was actually inspected. This intermediate file does not replace the final module's reference reviews or step/edge evidence.

The corresponding module notes explain boundary choices and unresolved integration. The source files under `publications/` are normal cache outputs and were not manually rewritten. All 18 excerpts were checked as whitespace-normalized substrings when this file was created. Findings must be reconciled against completed member reviews before the module can be finalized.


## Integrated draft checks

`members.yaml` records the 22 accession/taxon/classification tuples from normal UniProt fetching, with official PANTHER labels. `check_module.py` independently rereads those source records and invokes the production validator with a bounded member index. `check_routes.py` checks structural requirements with the production compiler and a complex-unit-aware predicate. Run both with `uv run python` from the repository root.

The 20 route cases test human core completeness, accessory-modifier optionality, class IA subunit requirements, isoform specificity and species matching. They do not prove physiological sufficiency, temporal order, universal native requirements or activity in a cell that merely expresses the proteins. Those assertions remain literature judgments.

The preliminary `evidence-findings.yaml` records the first 18 research findings. The integrated module now contains 32 reference assessments and 36 mined findings, including human class IA biochemistry, BTK/PLCG2 substrate specificity and human BCAP domain evidence. The module is the current integrated authority; the earlier research matrix remains provenance. No PANTHER ancestral node is inferred from these membership checks.


All 22 individual reviews are complete: 2,645 original annotation payloads and 44 raw-source hashes were independently rechecked at integration. Final activity evidence includes native mouse BLNK, chicken BLNK phosphosite rescue, SYK kinase assays, PLCG2 chemistry and human class IB PI3K characterization. Assay host, construct identity, perturbation evidence and ortholog inference are stated separately. Four production-validator advisories remain for the two CD79B contribution descriptors at gene and family levels; no unsupported molecular-function identifier was added to silence them.
