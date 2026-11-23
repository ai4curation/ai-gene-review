"""Check NCBIfam's release table for GO terms that disagree with the model's own EC numbers.

Each NCBIfam model in ``hmm_PGAP.tsv`` can carry EC numbers and GO terms. PGAP uses
both to annotate RefSeq proteins, and GO's InterPro2GO mappings inherit the GO terms
for the models InterPro integrates. A GO molecular-function term names a reaction
through its EC cross-references, so it can be compared with the model's EC numbers.

For every (model, GO term) pair where the term has complete EC cross-references and
the model has at least one EC number, the pair is classified:

* ``consistent``: an EC of the term equals, or falls under, one of the model's ECs.
* ``sister_reaction``: no match, but some pair shares the first three EC levels,
  so the term names a different reaction of the same subclass (the PurT, glycogen
  synthase and PS synthase cases from the cutoff-check sweep have this shape).
* ``other_reaction``: no match and no shared subclass.

Pairs that do not match are then placed in the GO hierarchy (semsql GO, the database
``just validate`` uses) against the GO terms that cross-reference the model's own ECs:
``broader`` (an ancestor: true, less specific), ``narrower`` (a descendant: a specific
substrate or cofactor) or ``unrelated`` (a different reaction, the strongest lead).

GO terms that QuickGO reports as obsolete are listed separately. Models whose EC list
is empty cannot be checked this way; a term that contradicts only the model's name
(TIGR02095.1, TIGR02491.1, TIGR01142.1) needs a curator's eye, as does a wrong term that
falls under a partial model EC (NF006766.0, ``2.1.2.-``). GO ids QuickGO does not
return are listed as unresolved.

    uv run python projects/ENZYME_SPECIFICITY/ncbifam-metadata/check_release_table.py

Writes ``release_table_check.yaml`` and ``CANDIDATES.md`` next to this script. Needs
network access to QuickGO on first run; term data are cached under ``.cache``.
"""

from __future__ import annotations

import json
import sqlite3
import sys
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

from ai_gene_review.validation.enzyme_family_cutoff import (
    NCBIfam,
    _read_with_retry,
    is_complete_ec,
)

HERE = Path(__file__).parent
GO_DB = (
    Path.home() / ".data" / "oaklib" / "go.db"
)  # semsql GO, as used by `just validate`
CACHE = Path(".cache")
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}"


def ec_under(ec: str, family_ec: str) -> bool:
    """True when ``ec`` equals ``family_ec`` or falls under a partial family EC.

    >>> ec_under("2.1.2.2", "2.1.2.-"), ec_under("2.4.1.11", "2.4.1.21")
    (True, False)
    """
    fam = family_ec.split(".")
    return all(f == "-" or f == e for f, e in zip(fam, ec.split(".")))


def same_subclass(a: str, b: str) -> bool:
    """True when two complete EC numbers share their first three levels.

    >>> same_subclass("2.4.1.11", "2.4.1.21"), same_subclass("2.7.8.5", "1.1.1.1")
    (True, False)
    """
    return a.split(".")[:3] == b.split(".")[:3]


def classify(family_ecs: list[str], term_ecs: list[str]) -> str:
    """Relation of a GO term's EC cross-references to a model's EC numbers.

    >>> classify(["2.4.1.21"], ["2.4.1.11"])
    'sister_reaction'
    >>> classify(["2.1.2.-"], ["2.1.2.2"])
    'consistent'
    >>> classify(["2.7.8.8"], ["1.1.1.1"])
    'other_reaction'
    """
    if any(ec_under(t, f) for t in term_ecs for f in family_ecs):
        return "consistent"
    complete = [f for f in family_ecs if is_complete_ec(f)]
    if any(same_subclass(t, f) for t in term_ecs for f in complete):
        return "sister_reaction"
    return "other_reaction"


class GoHierarchy:
    """EC-to-GO cross-references and is_a ancestry from the semsql GO database."""

    def __init__(self, path: Path) -> None:
        if not path.exists():
            raise SystemExit(
                f"{path} not found: run `just validate` once so oaklib fetches sqlite:obo:go"
            )
        self.db = sqlite3.connect(path)

    def terms_for_ec(self, ec: str) -> set[str]:
        """GO terms that cross-reference this EC number, or any EC under a partial one
        (``7.1.1.-`` matches every ``7.1.1.n``)."""
        if is_complete_ec(ec):
            query, arg = "value=?", f"EC:{ec}"
        else:
            prefix = ".".join(p for p in ec.split(".") if p != "-")
            query, arg = "value LIKE ?", f"EC:{prefix}.%"
        rows = self.db.execute(
            f"SELECT subject FROM statements WHERE predicate='oio:hasDbXref' AND {query}",
            (arg,),
        )
        return {r[0] for r in rows if r[0].startswith("GO:")}

    def ancestors(self, term: str) -> set[str]:
        """Proper GO ancestors of a term over rdfs:subClassOf."""
        rows = self.db.execute(
            "SELECT object FROM entailed_edge WHERE subject=? AND predicate='rdfs:subClassOf'",
            (term,),
        )
        return {r[0] for r in rows if r[0].startswith("GO:") and r[0] != term}


def broad_class_term(family_ecs: list[str], term_ecs: list[str]) -> bool:
    """True for a class-level GO term: three or more EC cross-references, all in a
    subclass the model's EC belongs to (e.g. serine-type endopeptidase, 3.4.21.*).

    >>> broad_class_term(["3.4.21.89"], ["3.4.21.1", "3.4.21.4", "3.4.21.5"])
    True
    >>> broad_class_term(["2.3.1.180"], ["2.3.1.179", "2.3.1.41"])
    False
    """
    complete = [f for f in family_ecs if is_complete_ec(f)]
    return len(term_ecs) >= 3 and any(
        all(same_subclass(t, f) for t in term_ecs) for f in complete
    )


def placement(
    go: str, family_ecs: list[str], term_ecs: list[str], hierarchy: GoHierarchy
) -> tuple[str, list[str]]:
    """Where a metadata GO term sits relative to the GO terms for the model's own ECs.

    ``broader``: an ancestor of a term for the model's EC (true, only less specific).
    ``narrower``: a descendant of such a term (a more specific substrate or cofactor).
    ``unrelated``: neither, so the term names a different reaction.
    ``no_go_for_model_ec``: no GO term cross-references the model's EC numbers.
    ``broad_class``: a class-level term covering the model's EC subclass (see
    ``broad_class_term``), which GO's hierarchy does not always link to the EC's term.
    This heuristic is tested first, before the hierarchy is consulted.

    Also returns the GO terms for the model's own ECs (a partial EC matches every EC
    under it), the machine-derived candidates to replace an ``unrelated`` term.
    """
    if broad_class_term(family_ecs, term_ecs):
        return "broad_class", []
    model_terms = {t for ec in family_ecs for t in hierarchy.terms_for_ec(ec)}
    if not model_terms:
        return "no_go_for_model_ec", []
    if any(go in hierarchy.ancestors(t) for t in model_terms):
        return "broader", sorted(model_terms)
    if model_terms & hierarchy.ancestors(go):
        return "narrower", sorted(model_terms)
    return "unrelated", sorted(model_terms)


def term_data(go_ids: set[str]) -> dict[str, dict]:
    """Name, obsolescence and complete EC cross-references of each GO term, cached."""
    path = CACHE / "quickgo_term_ec.json"
    cache = json.loads(path.read_text()) if path.exists() else {}
    # ids QuickGO did not return last time are retried rather than trusted
    missing = sorted(go for go in go_ids if not cache.get(go, {}).get("name"))
    for start in range(0, len(missing), 50):
        batch = missing[start : start + 50]
        ids = ",".join(batch)
        req = urllib.request.Request(
            QUICKGO.format(ids=ids), headers={"Accept": "application/json"}
        )
        terms = {r["id"]: r for r in json.loads(_read_with_retry(req))["results"]}
        req = urllib.request.Request(
            QUICKGO.format(ids=ids) + "/xrefs", headers={"Accept": "application/json"}
        )
        xrefs = {r["id"]: r for r in json.loads(_read_with_retry(req))["results"]}
        for go in batch:
            t = terms.get(go, {})
            cache[go] = {
                "name": t.get("name"),
                "aspect": t.get("aspect"),
                "obsolete": bool(t.get("isObsolete")),
                "ec": [
                    x["dbId"]
                    for x in xrefs.get(go, {}).get("xRefs", [])
                    if x["dbCode"] == "EC" and is_complete_ec(x["dbId"])
                ],
            }
        print(f"{min(start + 50, len(missing))}/{len(missing)} terms", file=sys.stderr)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, indent=0, sort_keys=True))
    return cache


def refseq_hits(cache_dir: Path) -> dict[str, int]:
    """RefSeq protein hit count per model, from the release table."""
    with (cache_dir / "hmm_PGAP.tsv").open() as fh:
        header = fh.readline().lstrip("#").rstrip("\n").split("\t")
        idx_acc, idx_hits = (
            header.index("ncbi_accession"),
            header.index("n_refseq_protein_hits"),
        )
        out = {}
        for line in fh:
            cols = line.rstrip("\n").split("\t")
            out[cols[idx_acc]] = int(cols[idx_hits] or 0)
    return out


def main() -> None:
    """Classify every (model, GO term) pair and write the results and candidate list."""
    db = NCBIfam(CACHE / "ncbifam")
    hierarchy = GoHierarchy(GO_DB)
    hits = refseq_hits(db.cache_dir)
    terms = term_data({go for f in db.families for go in f.go_terms})
    rows, obsolete = [], []
    # GO ids in the release table that QuickGO does not return (merged or invalid ids)
    unresolved = sorted(
        {
            f"{f.accession} {go}"
            for f in db.families
            for go in f.go_terms
            if not terms[go]["name"]
        }
    )
    for f in db.families:
        for go in f.go_terms:
            t = terms[go]
            if t["obsolete"]:
                obsolete.append(
                    {
                        "model": f.accession,
                        "product_name": f.product_name,
                        "go": go,
                        "go_name": t["name"],
                        "refseq_hits": hits.get(f.accession, 0),
                    }
                )
            if not t["ec"] or not f.ec_numbers:
                continue
            rows.append(
                {
                    "model": f.accession,
                    "product_name": f.product_name,
                    "family_type": f.family_type,
                    "ec_numbers": f.ec_numbers,
                    "go": go,
                    "go_name": t["name"],
                    "go_ec": t["ec"],
                    "relation": (rel := classify(f.ec_numbers, t["ec"])),
                    "refseq_hits": hits.get(f.accession, 0),
                }
            )
            if rel == "consistent":
                rows[-1]["placement"] = None
            else:
                where, model_terms = placement(go, f.ec_numbers, t["ec"], hierarchy)
                rows[-1]["placement"] = where
                if where != "broad_class":  # the heuristic does not look terms up
                    rows[-1]["model_ec_terms_first10"] = model_terms[:10]
                    rows[-1]["model_ec_term_count"] = len(model_terms)
    meta = {
        "ncbifam_release": db.release(),
        "models": len(db.families),
        "models_with_go": sum(1 for f in db.families if f.go_terms),
        "pairs_checked": len(rows),
        "relations": dict(Counter(r["relation"] for r in rows)),
        "placements": dict(Counter(r["placement"] for r in rows if r["placement"])),
        "obsolete_go_pairs": len(obsolete),
        "unresolved_go": unresolved,
    }
    (HERE / "release_table_check.yaml").write_text(
        yaml.safe_dump(
            {
                "meta": meta,
                # consistent pairs are only counted in meta, to keep the file small
                "pairs": [r for r in rows if r["relation"] != "consistent"],
                "obsolete_go": obsolete,
            },
            sort_keys=False,
            width=120,
        )
    )
    (HERE / "CANDIDATES.md").write_text(render(meta, rows, obsolete))


def render(meta: dict, rows: list[dict], obsolete: list[dict]) -> str:
    """CANDIDATES.md, built only from the computed results."""
    lines = [
        "# NCBIfam release-table check: candidate GO metadata errors",
        "",
        "Generated by `check_release_table.py`; do not edit by hand. Raw output: "
        "`release_table_check.yaml`.",
        f"NCBIfam release {meta['ncbifam_release']}: {meta['models']} models, "
        f"{meta['models_with_go']} with GO terms; {meta['pairs_checked']} (model, GO term) "
        "pairs where both sides carry EC numbers.",
        "",
        "| relation | pairs |",
        "|---|---|",
    ]
    lines += [f"| {k} | {v} |" for k, v in sorted(meta["relations"].items())]
    lines += [f"| obsolete GO term | {meta['obsolete_go_pairs']} |"]

    lines += [
        "",
        "Pairs whose EC numbers do not match are placed in the GO hierarchy relative to "
        "the GO terms that cross-reference the model's own EC numbers:",
        "",
        "| placement | pairs |",
        "|---|---|",
    ]
    lines += [f"| {k} | {v} |" for k, v in sorted(meta["placements"].items())]

    def table(kind: str, title: str, explain: str) -> None:
        sel = sorted(
            (r for r in rows if r["placement"] == kind),
            key=lambda r: (-r["refseq_hits"], r["model"]),
        )
        lines.extend(["", f"## {title} ({len(sel)})", "", explain, ""])
        if not sel:
            return
        lines.append(
            "| model | product name | model EC | GO term | term EC | EC relation | RefSeq hits |"
        )
        lines.append("|---|---|---|---|---|---|---|")
        lines.extend(
            f"| {r['model']} | {r['product_name']} | {', '.join(r['ec_numbers'])} | "
            f"{r['go']} {r['go_name']} | {', '.join(r['go_ec'][:4])}"
            f"{' …' if len(r['go_ec']) > 4 else ''} | {r['relation']} | {r['refseq_hits']} |"
            for r in sel
        )

    table(
        "unrelated",
        "GO term names a different reaction from the model's EC",
        "The strongest leads. The term is neither an ancestor nor a descendant of any GO "
        "term for the model's EC numbers. Bifunctional models (two activities in the "
        "product name) can legitimately carry such a term; the rest name the wrong "
        "reaction. Ranked by the number of RefSeq proteins the model hits.",
    )
    table(
        "narrower",
        "GO term is more specific than the model's EC",
        "The term is a descendant of a GO term for the model's EC: a specific substrate "
        "or cofactor. Right only if every member of the family has that specificity.",
    )
    table(
        "no_go_for_model_ec",
        "No GO term cross-references the model's EC",
        "These cannot be placed: no GO term carries the model's EC as a "
        "cross-reference (a recent EC number, or a GO term cross-referenced only to "
        "Rhea). Check by name.",
    )
    broader = meta["placements"].get("broader", 0)
    broad = meta["placements"].get("broad_class", 0)
    lines.extend(
        [
            "",
            f"The {broader} `broader` pairs (ancestors of the model's own GO term) and the "
            f"{broad} `broad_class` pairs (class terms such as serine-type endopeptidase "
            "activity) are true but less specific. They are listed in "
            "`release_table_check.yaml` only.",
        ]
    )
    lines.extend(
        ["", f"## Obsolete GO terms in the release table ({len(obsolete)})", ""]
    )
    if obsolete:
        lines.append("| model | product name | GO term | RefSeq hits |")
        lines.append("|---|---|---|---|")
        lines.extend(
            f"| {o['model']} | {o['product_name']} | {o['go']} {o['go_name']} | "
            f"{o['refseq_hits']} |"
            for o in sorted(obsolete, key=lambda o: (-o["refseq_hits"], o["model"]))
        )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
