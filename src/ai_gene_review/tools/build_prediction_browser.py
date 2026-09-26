"""Build a static faceted catalog of prediction sets and their reviewed claims."""

from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import shutil
from typing import Any

from ai_gene_review.export.browser_payload import validate_browser_data_js_size
from ai_gene_review.export.prediction_export import collect_prediction_data
from ai_gene_review.tools.pages_dependencies import DependencyResolver


def encode_prediction_data_js(data: dict[str, Any]) -> str:
    """Share repeated column names and strings without changing field values.

    Rows with different fields use different layouts, so explicit null and
    absent fields stay distinct. Reconstruction is synchronous and requires
    neither a server nor decompression support. Review text is never shortened.

    Dictionary references use ``~<index>`` strings. Literal strings starting
    with ``~`` always enter the dictionary, whose contents are never decoded
    again, so even reference-like input remains unambiguous. Other strings are
    shared only when their repeated JSON representation costs more bytes.
    """
    columns: list[tuple[str, ...]] = []
    layouts: dict[tuple[str, ...], int] = {}
    counts: dict[str, int] = {}

    def count_strings(value: Any) -> None:
        """Count string values, including those in nested arrays and objects."""
        if isinstance(value, str):
            counts[value] = counts.get(value, 0) + 1
        elif isinstance(value, dict):
            for item in value.values():
                count_strings(item)
        elif isinstance(value, (list, tuple)):
            for item in value:
                count_strings(item)

    count_strings(data)
    strings: list[str] = []
    references: dict[str, str] = {}
    for value, count in counts.items():
        reference = f"~{len(strings)}"
        literal_size = len(json.dumps(value, ensure_ascii=True))
        reference_size = len(reference) + 2  # JSON quotes around the reference.
        if (
            value.startswith("~")
            or count * (literal_size - reference_size) > literal_size + 1
        ):
            references[value] = reference
            strings.append(value)

    def pack_strings(value: Any) -> Any:
        """Replace selected string values without reserving an object shape."""
        if isinstance(value, str):
            return references.get(value, value)
        if isinstance(value, dict):
            return {key: pack_strings(item) for key, item in value.items()}
        if isinstance(value, (list, tuple)):
            return [pack_strings(item) for item in value]
        return value

    def pack(rows: list[dict[str, Any]]) -> list[list[Any]]:
        """Replace repeated object keys with a shared layout identifier."""
        packed = []
        for row in rows:
            keys = tuple(row)
            if keys not in layouts:
                layouts[keys] = len(columns)
                columns.append(keys)
            packed.append(
                [layouts[keys], *(pack_strings(value) for value in row.values())]
            )
        return packed

    payload = {
        "sets": pack(data["sets"]),
        "claims": pack(data["claims"]),
        "metadata": pack_strings(data["metadata"]),
        "columns": columns,
        "strings": strings,
    }
    encoded = json.dumps(
        payload, ensure_ascii=True, separators=(",", ":"), allow_nan=False
    )
    return (
        "(()=>{const p=" + encoded + ";"
        'const value=v=>typeof v==="string"&&v.startsWith("~")?p.strings[+v.slice(1)]:'
        'Array.isArray(v)?v.map(value):v!==null&&typeof v==="object"?'
        "Object.fromEntries(Object.entries(v).map(([k,x])=>[k,value(x)])):v;"
        "const unpack=rows=>rows.map(row=>Object.fromEntries("
        "p.columns[row[0]].map((key,i)=>[key,value(row[i+1])])));"
        "window.predictionData={sets:unpack(p.sets),claims:unpack(p.claims),metadata:value(p.metadata)};})();\n"
    )


def build_prediction_browser(root: Path, output_dir: Path) -> dict[str, Any]:
    """Export canonical predictions without truncating judgments or inventing scores.

    Data is a classic script so both datasets work directly over ``file://``.
    A separate dependency manifest lets Pages staging copy files whose links
    are stored in rows and therefore invisible to static HTML link discovery.
    """
    root = root.resolve()
    output_dir = output_dir.resolve()
    relative_output = output_dir.relative_to(root)
    data = collect_prediction_data(root, output_dir)
    encoded = encode_prediction_data_js(data)
    size = len(encoded.encode("utf-8"))
    validate_browser_data_js_size(size)

    links = {
        value
        for row in [*data["sets"], *data["claims"]]
        for key, value in row.items()
        if key.endswith("_link")
        and isinstance(value, str)
        and value
        and not value.startswith(("?", "#"))
    }
    anchors = "".join(
        f'<a href="{escape(link, quote=True)}"></a>' for link in sorted(links)
    )
    sources = DependencyResolver(root).scan(relative_output / "index.html", anchors)
    if sources.missing:
        raise FileNotFoundError(
            "Prediction browser links to missing files: "
            + ", ".join(sorted(path.as_posix() for path in sources.missing))
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "data.js").write_text(encoded, encoding="utf-8")
    (output_dir / "source-files.json").write_text(
        json.dumps(sorted(path.as_posix() for path in sources.existing), indent=2)
        + "\n",
        encoding="utf-8",
    )
    templates = Path(__file__).resolve().parents[1] / "browser"
    shutil.copyfile(templates / "index.html", output_dir / "index.html")
    shutil.copyfile(templates / "predictions_schema.js", output_dir / "schema.js")
    return {
        "sets": len(data["sets"]),
        "claims": len(data["claims"]),
        "data_bytes": size,
    }


def main() -> None:
    """Build the browser from the command line and report its actual row counts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, default=Path("app/predictions"))
    args = parser.parse_args()
    root = args.root.resolve()
    output = (
        args.output_dir if args.output_dir.is_absolute() else root / args.output_dir
    )
    result = build_prediction_browser(root, output)
    print(json.dumps({"output": str(output), **result}, indent=2))


if __name__ == "__main__":
    main()
