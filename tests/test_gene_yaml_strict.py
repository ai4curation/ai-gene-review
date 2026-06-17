"""Enforce that every gene-review YAML parses under the strict YAML loader.

linkml-reference-validator parses data with ruamel's (libyaml C) parser, which is
stricter than PyYAML. Constructs PyYAML silently accepts are rejected there, e.g.:

- unquoted CURIE scalars in flow sequences (``additional_reference_ids: [PMID:123]``);
  the ``:`` makes it an ambiguous plain scalar in flow context (quote the items), and
- duplicate mapping keys (PyYAML keeps the last; ruamel errors).

Keeping the corpus valid under the strict parser lets the reference validator read the
files directly, and catches real bugs (like duplicate keys) that the lenient parser hides.
"""

from pathlib import Path

from ruamel.yaml import YAML

REPO_ROOT = Path(__file__).resolve().parents[1]
GENES_DIR = REPO_ROOT / "genes"


def test_all_gene_reviews_parse_under_strict_yaml() -> None:
    yaml = YAML(typ="safe")
    failures = []
    for fp in sorted(GENES_DIR.glob("*/*/*-ai-review.yaml")):
        try:
            yaml.load(fp.read_text())
        except Exception as exc:  # noqa: BLE001 - any parse failure is a failure
            failures.append(f"{fp.relative_to(REPO_ROOT)}: {type(exc).__name__}: {exc}")
    assert not failures, (
        f"{len(failures)} gene-review file(s) are not valid under the strict YAML parser "
        "used by linkml-reference-validator (quote flow-list CURIEs, remove duplicate keys):\n"
        + "\n".join(failures[:25])
    )
