# PSEPK carnitine consultation

`evidence.md` records the scientific judgments, shared PR6108 provenance and primary access limits. `results.yaml` contains the complete action ledger, sequence alignments, exact Q88R31-to-BKACE511 mapping and the raw target screen columns. The two XLSX files and RCSB JSON are unmodified, independently retrieved source artifacts. `ontology.yaml` and the ancestry/search responses record current GO checks.

From the repository root, reproduce the preservation, sequence and dataset checks with:

```sh
uv run python analysis/module_audits/bacterial_l_carnitine_catabolism/psepk-consultation/check_evidence.py
uv run ruff check analysis/module_audits/bacterial_l_carnitine_catabolism/psepk-consultation/check_evidence.py
```

The project environment supplies Biopython, PyYAML and openpyxl. The checker reads the frozen baseline, protected sources and archived input artifacts; it requires no network. It deliberately corrupts an annotation ID, row order and inherited NEW action in memory to confirm detection. It does not infer a biological positive call from the unprocessed enzyme-screen values.

All six scoped gene validations, renders, PAINT-loss commands and generated-history validations completed. Exact commands and log hashes are in `checks.yaml`. PAINT lineages were unassessable because source/tree membership was missing; that is a coverage limit, not a negative loss result. PP_0303's core acyltransferase term is independently source-supported but absent from the annotation block after GO:0043720 became UNDECIDED. The validator's suggested NEW was not adopted merely to eliminate that warning.

`handoff.yaml` freezes every released file by SHA256 and names all gene histories. No module, family, shared project or another worktree was edited by this consultation. No commit, push or full-corpus validation was performed.
