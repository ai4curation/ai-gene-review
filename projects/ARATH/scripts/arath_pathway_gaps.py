"""Find Arabidopsis pathways that the repository has not curated.

Reads the hand-curated pathway map projects/ARATH/ARATH-pathway-map.yaml and
checks it against modules/ and genes/ARATH/. For each pathway it reports which
mapped modules exist, whether they mention Arabidopsis, which reviewed ARATH
genes they contain, and which named ARATH genes belong to no module. It also
lists KEGG ath maps that the map file neither assigns to a pathway nor marks as
out of scope.

Run from the repository root:

    uv run python projects/ARATH/scripts/arath_pathway_gaps.py [--kegg-list FILE]

--kegg-list takes a saved copy of https://rest.kegg.jp/list/pathway/ath;
without it the list is fetched. Writes projects/ARATH/ARATH-pathway-gaps.yaml.
Every coverage call is computed; the only judgments are in the map file.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
GENES = ROOT / "genes" / "ARATH"
MODULES = ROOT / "modules"
MAP = ROOT / "projects" / "ARATH" / "ARATH-pathway-map.yaml"
OUT = ROOT / "projects" / "ARATH" / "ARATH-pathway-gaps.yaml"

# Ordered from least to most curated.
STATUSES = [
    "NO_MODULE",
    "MODULE_WITHOUT_ARABIDOPSIS",
    "MODULE_WITHOUT_ARATH_GENES",
    "MODULE_WITH_ARATH_GENES",
]


def load(path: Path):
    with path.open() as fh:
        return yaml.safe_load(fh)


def review_ids() -> dict[str, str]:
    """UniProt accession -> gene folder, for every ARATH review."""
    out = {}
    for d in sorted(p for p in GENES.iterdir() if p.is_dir()):
        f = d / f"{d.name}-ai-review.yaml"
        if f.exists():
            acc = (load(f) or {}).get("id")
            if acc:
                out[acc] = d.name
    return out


def module_facts(module_id: str, acc2folder: dict[str, str]) -> dict:
    """Same membership rule as arath_corpus_stats.py: UniProt accessions of
    reviewed ARATH genes, plus explicit genes/ARATH/<folder>/ paths."""
    f = MODULES / f"{module_id}.yaml"
    if not f.exists():
        sys.exit(f"ERROR: module '{module_id}' named in {MAP.name} does not exist")
    text = f.read_text()
    accs = set(re.findall(r"UniProtKB:([A-Z0-9]+)", text))
    hits = {acc2folder[a] for a in accs if a in acc2folder}
    refs = set(re.findall(r"genes/ARATH/([A-Za-z0-9_.-]+)/", text))
    doc = load(f) or {}
    return {
        "module": module_id,
        "title": doc.get("title"),
        "status": doc.get("status"),
        "mentions_arabidopsis": "Arabidopsis" in text,
        "arath_reviewed_members": sorted(hits | refs),
    }


def all_module_members(acc2folder: dict[str, str]) -> set[str]:
    members = set()
    for f in MODULES.glob("*.yaml"):
        members |= set(module_facts(f.stem, acc2folder)["arath_reviewed_members"])
    return members


def kegg_list(path: str | None) -> dict[str, str]:
    if path:
        text = Path(path).read_text()
    else:
        with urllib.request.urlopen(MAP_DOC["reference"]["kegg_list_url"], timeout=60) as r:
            text = r.read().decode()
    out = {}
    for line in text.splitlines():
        if "\t" in line:
            k, name = line.split("\t", 1)
            out[k.strip()] = name.replace(" - Arabidopsis thaliana (thale cress)", "").strip()
    return out


def coverage(facts: list[dict]) -> str:
    if not facts:
        return "NO_MODULE"
    if any(m["arath_reviewed_members"] for m in facts):
        return "MODULE_WITH_ARATH_GENES"
    if any(m["mentions_arabidopsis"] for m in facts):
        return "MODULE_WITHOUT_ARATH_GENES"
    return "MODULE_WITHOUT_ARABIDOPSIS"


MAP_DOC = load(MAP)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--kegg-list", help="saved copy of rest.kegg.jp/list/pathway/ath")
    args = ap.parse_args()

    acc2folder = review_ids()
    in_any_module = all_module_members(acc2folder)
    kegg = kegg_list(args.kegg_list)

    rows = []
    mapped_kegg = set()
    for p in MAP_DOC["pathways"]:
        for g in p.get("arath_genes", []):
            if not (GENES / g).is_dir():
                sys.exit(f"ERROR: gene folder genes/ARATH/{g} named for '{p['name']}' does not exist")
        for k in p.get("kegg", []):
            if k not in kegg:
                sys.exit(f"ERROR: KEGG map {k} for '{p['name']}' is not in the KEGG ath list")
        mapped_kegg.update(p.get("kegg", []))
        facts = [module_facts(m, acc2folder) for m in p.get("modules", [])]
        for m in p.get("related_modules", []):
            module_facts(m, acc2folder)  # existence check only
        genes = p.get("arath_genes", [])
        rows.append(
            {
                "name": p["name"],
                "group": p["group"],
                "coverage": coverage(facts),
                "kegg": [f"{k} {kegg[k]}" for k in p.get("kegg", [])],
                "modules": facts,
                "related_modules": p.get("related_modules", []),
                "arath_genes_named": genes,
                "arath_genes_outside_any_module": sorted(g for g in genes if g not in in_any_module),
                "notes": p.get("notes"),
            }
        )

    out_of_scope = {k for v in MAP_DOC["kegg_out_of_scope"].values() for k in v}
    unknown = sorted(out_of_scope - set(kegg))
    if unknown:
        sys.exit(f"ERROR: out-of-scope KEGG maps not in the KEGG ath list: {unknown}")
    not_assessed = sorted(set(kegg) - mapped_kegg - out_of_scope)

    counts = Counter(r["coverage"] for r in rows)
    doc = {
        "summary": {
            "generated": date.today().isoformat(),
            "n_pathways": len(rows),
            "coverage": {s: counts.get(s, 0) for s in STATUSES},
            "n_kegg_ath_maps": len(kegg),
            "n_kegg_maps_mapped": len(mapped_kegg),
            "n_kegg_maps_out_of_scope": len(out_of_scope),
            "n_kegg_maps_not_assessed": len(not_assessed),
        },
        "kegg_maps_not_assessed": [f"{k} {kegg[k]}" for k in not_assessed],
        "pathways": sorted(rows, key=lambda r: (STATUSES.index(r["coverage"]), r["group"], r["name"])),
    }
    OUT.write_text(yaml.safe_dump(doc, sort_keys=False, width=100, allow_unicode=True))
    print(yaml.safe_dump(doc["summary"], sort_keys=False))


if __name__ == "__main__":
    main()
