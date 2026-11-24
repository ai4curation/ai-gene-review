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

import hashlib
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
SKIP_LABELS = {  # in reporting order; each test applies only to pairs the ones above passed
    "model_has_no_ec": "where the model has no EC number",
    "non_mf_term": "with a biological process or cellular component term",
    "mf_term_partial_ec_contains_model": "with a class term whose partial EC contains the model's EC",
    "mf_term_partial_ec_within_model": "with a class term whose partial EC lies inside the model's partial EC (narrower)",
    "mf_term_ancestor_of_model_term": "with a class term that is a GO ancestor of a term for the model's EC, though its partial EC does not contain it",
    "mf_term_partial_ec_outside_model": "with a class term unrelated to the model's EC by EC class or GO ancestry",
    "mf_term_has_no_ec": "with a molecular function term that reaches no EC, directly or through Rhea",
}
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}"


def ec_under(ec: str, family_ec: str) -> bool:
    """True when ``ec`` equals ``family_ec`` or falls under a partial family EC.

    >>> ec_under("2.1.2.2", "2.1.2.-"), ec_under("2.4.1.11", "2.4.1.21")
    (True, False)
    """
    fam = family_ec.split(".")
    return all(f == "-" or f == e for f, e in zip(fam, ec.split(".")))


def ec_class_relation(model_ec: str, term_ec: str) -> str | None:
    """How a GO term's partial EC class relates to a model's EC number.

    ``contains``: the term's class contains the model's EC (the term is broader).
    ``within``: the term's class lies inside a partial model EC (the term is narrower).

    >>> ec_class_relation("3.5.3.1", "3.5.-.-"), ec_class_relation("3.5.-.-", "3.5.3.-")
    ('contains', 'within')
    >>> ec_class_relation("2.6.1.121", "1.-.-.-") is None
    True
    """
    if ec_under(model_ec, term_ec):
        return "contains"
    if ec_under(term_ec, model_ec):
        return "within"
    return None


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


RHEA_URL = "https://ftp.expasy.org/databases/rhea/tsv/{name}"
RHEA_FILES = ("rhea2ec.tsv", "rhea-directions.tsv")


class RheaEC:
    """EC numbers of Rhea reactions, from Rhea's ``rhea2ec.tsv`` and ``rhea-directions.tsv``.

    GO cross-references many reaction terms only to Rhea, and may use any of a reaction's
    four ids (undirected master, left-to-right, right-to-left, bidirectional), while
    ``rhea2ec.tsv`` is keyed by the master id, so every id is mapped to its master first.

    >>> r = RheaEC.from_rows([("10000", "3.5.1.50")], [("10000", "10001", "10002", "10003")])
    >>> r.ecs("RHEA:10002"), r.ecs("RHEA:99")
    ({'3.5.1.50'}, set())
    """

    def __init__(
        self, ec_by_master: dict[str, set[str]], master: dict[str, str]
    ) -> None:
        self.ec_by_master, self.master = ec_by_master, master

    @classmethod
    def from_rows(cls, ec_rows, direction_rows) -> RheaEC:
        ec_by_master: dict[str, set[str]] = {}
        for master_id, ec in ec_rows:
            ec_by_master.setdefault(master_id, set()).add(ec)
        master = {i: row[0] for row in direction_rows for i in row}
        return cls(ec_by_master, master)

    @classmethod
    def load(cls, cache_dir: Path) -> RheaEC:
        """Read the Rhea tables from ``cache_dir``, downloading them when missing."""
        cache_dir.mkdir(parents=True, exist_ok=True)
        for name in RHEA_FILES:
            path = cache_dir / name
            if not path.exists():
                req = urllib.request.Request(RHEA_URL.format(name=name))
                path.write_bytes(_read_with_retry(req))

        def rows(name: str) -> list[list[str]]:
            lines = (cache_dir / name).read_text().splitlines()[1:]
            return [line.split("\t") for line in lines if line]

        ec_rows = [(r[2], r[3]) for r in rows("rhea2ec.tsv")]  # MASTER_ID, EC ID
        return cls.from_rows(ec_rows, rows("rhea-directions.tsv"))

    def ecs(self, xref: str) -> set[str]:
        """EC numbers of the reaction a ``RHEA:`` cross-reference names."""
        rid = xref.removeprefix("RHEA:")
        return set(self.ec_by_master.get(self.master.get(rid, rid), ()))


def rhea_digest(cache_dir: Path) -> dict[str, str]:
    """SHA-256 of each Rhea table used, so a run records which Rhea data it read."""
    return {
        name: hashlib.sha256((cache_dir / name).read_bytes()).hexdigest()
        for name in RHEA_FILES
    }


class GoHierarchy:
    """EC-to-GO cross-references and is_a ancestry from the semsql GO database.

    With ``rhea``, a GO term cross-referenced to a Rhea reaction also counts as
    cross-referencing that reaction's EC number, but only when its Rhea cross-references
    reach exactly one EC and the term carries no partial EC of its own. A generic term
    fails that test: ATP hydrolysis activity's Rhea reaction maps to nine ECs (helicases,
    translocases), so the route would give it a reaction it does not name.
    """

    def __init__(self, path: Path, rhea: RheaEC | None = None) -> None:
        if not path.exists():
            raise SystemExit(
                f"{path} not found: run `just validate` once so oaklib fetches sqlite:obo:go"
            )
        self.db = sqlite3.connect(path)
        self.rhea_ecs_by_term: dict[str, set[str]] = {}
        self.rhea_ambiguous: set[str] = set()  # terms whose Rhea reaches several ECs
        if rhea is not None:
            reached: dict[str, set[str]] = {}
            for term, xref in self.db.execute(
                "SELECT subject, value FROM statements WHERE predicate='oio:hasDbXref' "
                "AND value LIKE 'RHEA:%' AND subject LIKE 'GO:%'"
            ):
                if ecs := rhea.ecs(xref):
                    reached.setdefault(term, set()).update(ecs)
            class_terms = {
                t
                for (t,) in self.db.execute(
                    "SELECT subject FROM statements WHERE predicate='oio:hasDbXref' "
                    "AND value LIKE 'EC:%-%' AND subject LIKE 'GO:%'"
                )
            }
            for term, ecs in reached.items():
                if term in class_terms:
                    continue
                if len(ecs) == 1 and is_complete_ec(next(iter(ecs))):
                    self.rhea_ecs_by_term[term] = ecs
                else:
                    self.rhea_ambiguous.add(term)
        self.rhea_terms_by_ec: dict[str, set[str]] = {}
        for term, ecs in self.rhea_ecs_by_term.items():
            for ec in ecs:
                self.rhea_terms_by_ec.setdefault(ec, set()).add(term)

    def rhea_ecs(self, term: str) -> list[str]:
        """Complete EC numbers a GO term reaches through its Rhea cross-references."""
        return sorted(self.rhea_ecs_by_term.get(term, ()))

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
        terms = {r[0] for r in rows if r[0].startswith("GO:")}
        if is_complete_ec(ec):
            terms |= self.rhea_terms_by_ec.get(ec, set())
        else:
            terms |= {
                t
                for rhea_ec, ts in self.rhea_terms_by_ec.items()
                if rhea_ec.startswith(f"{prefix}.")
                for t in ts
            }
        return terms

    def partial_ecs(self, term: str) -> list[str]:
        """The partial EC cross-references (``1.8.-.-``) on a GO term, which a class
        term often has instead of a complete one."""
        rows = self.db.execute(
            "SELECT value FROM statements WHERE subject=? AND predicate='oio:hasDbXref' "
            "AND value LIKE 'EC:%'",
            (term,),
        )
        return sorted(r[0][3:] for r in rows if not is_complete_ec(r[0][3:]))

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
    rhea = RheaEC.load(CACHE / "rhea")
    hierarchy = GoHierarchy(GO_DB, rhea)
    hits = refseq_hits(db.cache_dir)
    terms = term_data({go for f in db.families for go in f.go_terms})
    # a term's reaction: its own complete EC cross-references, else those its Rhea
    # cross-references reach (many GO terms now cross-reference only Rhea)
    for go, t in terms.items():
        t["ec_rhea"] = [] if t["ec"] else hierarchy.rhea_ecs(go)
        t["ec_all"] = t["ec"] or t["ec_rhea"]
    rows, obsolete, class_mismatch, class_within, class_ancestor = [], [], [], [], []
    # GO ids in the release table that QuickGO does not return (merged or invalid ids)
    unresolved = sorted(
        {
            f"{f.accession} {go}"
            for f in db.families
            for go in f.go_terms
            if not terms[go]["name"]
        }
    )
    skipped: Counter = Counter()
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
            if not f.ec_numbers:
                skipped["model_has_no_ec"] += 1
                continue
            if not t["ec_all"]:
                # the term has no complete EC: BP and CC terms, class terms with only a
                # partial EC, and MF terms with none are counted, not compared
                if t["aspect"] != "molecular_function":
                    skipped["non_mf_term"] += 1
                elif partial := hierarchy.partial_ecs(go):
                    relations = {
                        ec_class_relation(m, pe) for m in f.ec_numbers for pe in partial
                    }
                    # EC-class relations are tested before GO ancestry, so each
                    # counter means what it says whatever the later tests find
                    if "contains" in relations:
                        skipped["mf_term_partial_ec_contains_model"] += 1
                        continue
                    model_terms = {
                        mt for m in f.ec_numbers for mt in hierarchy.terms_for_ec(m)
                    }
                    go_ancestor = any(
                        go == mt or go in hierarchy.ancestors(mt) for mt in model_terms
                    )
                    record = {
                        "model": f.accession,
                        "product_name": f.product_name,
                        "family_type": f.family_type,
                        "ec_numbers": f.ec_numbers,
                        "go": go,
                        "go_name": t["name"],
                        "go_partial_ec": partial,
                        "refseq_hits": hits.get(f.accession, 0),
                    }
                    if "within" in relations:
                        skipped["mf_term_partial_ec_within_model"] += 1
                        # a GO ancestor too, the narrowing may be only the term's
                        # cross-reference (endopeptidase activity: EC:3.4.99.- only)
                        class_within.append(record | {"also_go_ancestor": go_ancestor})
                    elif go_ancestor:
                        # the term's own EC xref is narrower than its scope
                        skipped["mf_term_ancestor_of_model_term"] += 1
                        class_ancestor.append(
                            record
                            # the term is itself a term for the model's EC in the GO
                            # database, though QuickGO gave it no complete EC
                            | {"term_is_model_ec_term": go in model_terms}
                        )
                    else:
                        skipped["mf_term_partial_ec_outside_model"] += 1
                        # without a GO term for the model's EC, ancestry is untested
                        class_mismatch.append(
                            record | {"ancestry_tested": bool(model_terms)}
                        )
                else:
                    skipped["mf_term_has_no_ec"] += 1
                continue
            rows.append(
                {
                    "model": f.accession,
                    "product_name": f.product_name,
                    "family_type": f.family_type,
                    "ec_numbers": f.ec_numbers,
                    "go": go,
                    "go_name": t["name"],
                    "go_ec": t["ec_all"],
                    "go_ec_source": "rhea" if t["ec_rhea"] else "ec_xref",
                    "relation": (rel := classify(f.ec_numbers, t["ec_all"])),
                    "refseq_hits": hits.get(f.accession, 0),
                }
            )
            if rel == "consistent":
                rows[-1]["placement"] = None
            else:
                where, model_terms = placement(go, f.ec_numbers, t["ec_all"], hierarchy)
                rows[-1]["placement"] = where
                if where != "broad_class":  # the heuristic does not look terms up
                    rows[-1]["model_ec_terms_first10"] = model_terms[:10]
                    rows[-1]["model_ec_term_count"] = len(model_terms)
    meta = {
        "ncbifam_release": db.release(),
        "models": len(db.families),
        "models_with_go": sum(1 for f in db.families if f.go_terms),
        "model_go_pairs": sum(len(f.go_terms) for f in db.families),
        "pairs_skipped": {k: skipped[k] for k in SKIP_LABELS},
        "pairs_checked": len(rows),
        "pairs_checked_via_rhea": sum(1 for r in rows if r["go_ec_source"] == "rhea"),
        "rhea_tables_sha256": rhea_digest(CACHE / "rhea"),
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
                "class_term_outside_model_ec": class_mismatch,
                "class_term_within_model_ec": class_within,
                "class_term_ancestor_of_model_ec_term": class_ancestor,
            },
            sort_keys=False,
            width=120,
        )
    )
    (HERE / "CANDIDATES.md").write_text(
        render(meta, rows, obsolete, class_mismatch, class_within)
    )


def render(
    meta: dict,
    rows: list[dict],
    obsolete: list[dict],
    class_mismatch: list[dict],
    class_within: list[dict],
) -> str:
    """CANDIDATES.md, built only from the computed results."""
    lines = [
        "# NCBIfam release-table check: candidate GO metadata errors",
        "",
        "Generated by `check_release_table.py`; do not edit by hand. Raw output: "
        "`release_table_check.yaml`.",
        f"NCBIfam release {meta['ncbifam_release']}: {meta['models']} models, "
        f"{meta['models_with_go']} with GO terms; {meta['pairs_checked']} (model, GO term) "
        "pairs where both sides carry EC numbers, out of "
        f"{meta['model_go_pairs']}. Skipped: "
        + ", ".join(f"{n} {SKIP_LABELS[k]}" for k, n in meta["pairs_skipped"].items())
        + ".",
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
        [
            "",
            f"## Class term inside the model's partial EC ({len(class_within)})",
            "",
            "The model's EC is partial and the GO term's partial EC lies inside it. "
            "Either the term really is more specific than the model's EC "
            "(oxidoreductase acting on CH-OH donors on the mycofactocin dehydrogenase "
            "MftG, EC 1.-.-.-), or only the term's cross-reference is: endopeptidase "
            "activity is cross-referenced only to EC 3.4.99.- but covers all of EC 3.4. "
            "`GO ancestor` says whether the term is also a GO ancestor of a term for "
            "the model's EC; for a partial model EC that test matches nearly any class "
            "term, so it cannot tell the two readings apart. Each row is triaged in "
            "`triage.yaml` (`class_term_triage`).",
            "",
            "| model | product name | family type | model EC | GO term | term EC | "
            "GO ancestor | RefSeq hits |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    lines.extend(
        f"| {r['model']} | {r['product_name']} | {r['family_type']} | "
        f"{', '.join(r['ec_numbers'])} | {r['go']} {r['go_name']} | "
        f"{', '.join(r['go_partial_ec'])} | {'yes' if r['also_go_ancestor'] else 'no'} | "
        f"{r['refseq_hits']} |"
        for r in sorted(class_within, key=lambda r: (-r["refseq_hits"], r["model"]))
    )
    lines.extend(
        [
            "",
            f"## Class term outside the model's EC class ({len(class_mismatch)})",
            "",
            "Not compared above: the GO term carries only a partial EC, neither EC class "
            "contains the other, and the term is not a GO ancestor of any term for the "
            "model's EC, or the ancestry test could not run because no GO term reaches "
            "that EC (`ancestry tested` is `no`). A glycoside hydrolase term on the "
            "branching enzyme GlgB is an example. Candidate causes: a wrong-class term "
            "that follows the family's fold, a wrong EC on the model, an EC "
            "reclassification, or a term whose partial EC is narrower than its scope. "
            "Each row is triaged in `triage.yaml` (`class_term_triage`); FEEDBACK.md "
            "lists the ones that are not acceptable.",
            "",
            "`ancestry tested` is `no` where GO has no term cross-referencing the "
            "model's EC, so the GO-ancestor test could not run; endopeptidase activity "
            "(cross-referenced only to EC 3.4.99.-) on proteasome subunits (EC 3.4.25.1) "
            "is such a row, and is correct.",
            "",
            "| model | product name | family type | model EC | GO term | term EC | "
            "ancestry tested | RefSeq hits |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    lines.extend(
        f"| {r['model']} | {r['product_name']} | {r['family_type']} | "
        f"{', '.join(r['ec_numbers'])} | {r['go']} {r['go_name']} | "
        f"{', '.join(r['go_partial_ec'])} | {'yes' if r['ancestry_tested'] else 'no'} | "
        f"{r['refseq_hits']} |"
        for r in sorted(class_mismatch, key=lambda r: (-r["refseq_hits"], r["model"]))
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
