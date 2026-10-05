"""Build the static homology-propagation browser (``app/propagation/``).

Each row is one GOA annotation carried to a target from other gene products
(ISO/ISS/ISA, IBA, Ensembl Compara, TreeGrafter), shown as
donor(s) → intermediate (PANTHER node, where there is one) → target, with the
donor's current support for the term, what else the target carries, and the
gene review's verdict. Donor facts come from the cache written by
``refresh_propagation_sources``; nothing is fetched at build time.

Strings are interned into one table and donor records are deduplicated, so the
payload stays a fraction of the raw JSON while keeping every value intact.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
from typing import Any

from ai_gene_review.export.browser_payload import (
    GITHUB_FILE_SIZE_LIMIT_BYTES,
    browser_data_size_limit,
    validate_browser_data_js_size,
)
from ai_gene_review.export.propagation_export import DEFAULT_DATA_DIR, collect_propagation_data

#: Row fields, in encoded order. Lists are encoded element-wise.
FIELDS = [
    "target", "target_id", "target_species", "species_dir", "gene_dir",
    "term_id", "term_label", "aspect", "qualifier", "evidence", "reference",
    "method", "method_class", "assigned_by", "date", "nodes", "donors",
    "donor_count", "donor_species", "donor_support", "symbol_match",
    "iba_on_target", "experimental_on_target", "review_link", "action",
    "summary", "reason", "root_cause", "failure_modes",
]
DONOR_FIELDS = ["id", "symbol", "organism", "accession", "support", "codes"]


class Interner:
    """Map strings (and donor records) to dense integer ids.

    >>> table = Interner()
    >>> table.s("a"), table.s("b"), table.s("a")
    (0, 1, 0)
    >>> table.donor({"id": "X:1"}), table.donor({"id": "X:1"})
    (0, 0)
    """

    def __init__(self) -> None:
        self.strings: list[str] = []
        self._ids: dict[str, int] = {}
        self.donors: list[list[Any]] = []
        self._donor_ids: dict[tuple, int] = {}

    def s(self, value: str) -> int:
        if value not in self._ids:
            self._ids[value] = len(self.strings)
            self.strings.append(value)
        return self._ids[value]

    def donor(self, donor: dict[str, str]) -> int:
        key = tuple(donor.get(f, "") for f in DONOR_FIELDS)
        if key not in self._donor_ids:
            self._donor_ids[key] = len(self.donors)
            self.donors.append([self.s(v) if v else None for v in key])
        return self._donor_ids[key]

    def value(self, key: str, value: Any) -> Any:
        if value is None:
            return None
        if key == "donors":
            return [self.donor(d) for d in value]
        if isinstance(value, list):
            return [self.s(str(v)) for v in value]
        if isinstance(value, int):
            return value
        return self.s(str(value))


def encode_propagation_data(rows: list[dict[str, Any]], metadata: dict[str, Any]) -> str:
    """Encode rows as a classic script defining ``window.propagationData``."""
    table = Interner()
    packed = [[table.value(k, row.get(k)) for k in FIELDS] for row in rows]
    payload = {"fields": FIELDS, "donor_fields": DONOR_FIELDS,
               "strings": table.strings, "donors": table.donors,
               "rows": packed, "metadata": metadata}
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    return "window.propagationPayload=" + encoded + ";\n"


def build_propagation_browser(root: Path, output_dir: Path,
                              data_dir: Path = DEFAULT_DATA_DIR, *,
                              max_bytes: int | None = GITHUB_FILE_SIZE_LIMIT_BYTES) -> dict[str, Any]:
    """Write ``index.html`` and ``data.js`` for the propagation browser."""
    root = root.resolve()
    rows = collect_propagation_data(root, data_dir)["rows"]
    meta_path = root / data_dir / "refresh-metadata.json"
    donor_meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    metadata = {
        "donor_cache": donor_meta,
        "row_count": len(rows),
    }
    encoded = encode_propagation_data(rows, metadata)
    size = len(encoded.encode("utf-8"))
    validate_browser_data_js_size(size, max_bytes=max_bytes)
    # Rows link to gene review pages; list the ones that exist so Pages
    # staging copies them (dynamic links are invisible to static discovery).
    links = sorted({r["review_link"] for r in rows if r.get("review_link")
                    and (root / r["review_link"]).is_file()})
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "data.js").write_text(encoded, encoding="utf-8")
    (output_dir / "source-files.json").write_text(json.dumps(links, indent=2) + "\n",
                                                  encoding="utf-8")
    template = Path(__file__).resolve().parents[1] / "browser" / "propagation_index.html"
    shutil.copyfile(template, output_dir / "index.html")
    return {"rows": len(rows), "data_bytes": size}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, default=Path("app/propagation"))
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--target", choices=("git", "pages"), default="git")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output_dir if args.output_dir.is_absolute() else root / args.output_dir
    result = build_propagation_browser(root, output, args.data_dir,
                                       max_bytes=browser_data_size_limit(args.target))
    print(json.dumps({"output": str(output), **result}, indent=2))


if __name__ == "__main__":
    main()
