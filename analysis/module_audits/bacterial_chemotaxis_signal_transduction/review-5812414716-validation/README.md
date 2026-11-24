# Additive focused validation and renders

All ten commands completed sequentially with exit 0. `results.json` records exact argument vectors, working directory, start/end times, exit codes and SHA256 of each complete log.

- ECOLI CheW and BACSU CheY: normal `just validate` including schema, terms, references, best practices and markdown PMID checks.
- Chemotaxis module: LinkML schema plus production module validator, including conformance.
- Three generated histories: normal history validation.
- Both genes and the module: normal HTML renders.

Module validation passed with four warnings: the Pfam prefix lacks ontology label configuration; the CheA activity, sink CheA transfer activity and FliY phosphatase activity encounter the existing UNRESOLVED broader-family scopes. Those warnings do not negate the supported member activities or justify widening family grants. Five descriptors intentionally omit an unestablished PANTHER ID; the validator reports this separately as information. The dependency emits a `pkg_resources` deprecation warning, unrelated to curation. The two gene checks and three history checks report no curation/schema warnings.

The prior 16-file handoff and its own hash are unchanged. All 89 captured raw/provider/publication and historical audit inputs remain byte-identical. All 18 pre-existing ontology cache files are unchanged, with none added. The only derived updates outside this new directory are the two gene HTML files and module HTML; before/after hashes are recorded in `preservation.json`.

No science source, annotation payload, historical receipt or old checker was edited. No full-corpus or capacity run was performed, and no commit or push was made. The historical 65-case capacity result remains scoped to its original run. This additive receipt closes the focused-validation/render items deferred by the earlier handoff.
