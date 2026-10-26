"""Inventory precomposed "X involved in Y" GO terms and their use in this repo.

Reads a GO release (``go.obo``, the full edition with ``intersection_of``
logical definitions), every gene review under ``genes/``, the GO-CAM activity
index (``gocams/index.tsv``) and the module YAMLs under ``modules/``, and writes:

* ``go_terms.yaml``   -- every GO term whose label contains " involved in ",
  live or obsolete, with its logical definition (genus + differentia) when GO
  provides one, and the obsoletion comment / replacement pointers.
* ``annotations.yaml`` -- every ``existing_annotations`` row in a gene review
  that uses such a term, with the current review action, the decomposition
  implied by the logical definition, and which GO-CAM activities and modules
  already mention the gene (same gene product, or the same symbol in another
  species as a crude ortholog proxy).
* ``module_candidates.yaml`` -- the "Y" contexts grouped across genes, with
  the modules that already mention Y; contexts with several genes and no module
  are candidates for new modules.
* ``summary.yaml``    -- counts.

Nothing is hardcoded: re-run against a newer GO release and the outputs move.

Usage::

    uv run python projects/INVOLVED_IN_PRECOMPOSITION/scripts/inventory.py \\
        --go path/to/go.obo --out projects/INVOLVED_IN_PRECOMPOSITION/data
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[3]
INVOLVED_IN = " involved in "

# UniProt species code / repo folder -> suffix used in gocams/index.tsv gene_label
INDEX_SPECIES = {
    "human": "Hsap",
    "mouse": "Mmus",
    "rat": "Rnor",
    "yeast": "Scer",
    "SCHPO": "Spom",
    "DROME": "Dmel",
    "DANRE": "Drer",
    "worm": "Cele",
    "CAEEL": "Cele",
    "XENLA": "Xlae",
    "XENTR": "Xtro",
    "ARATH": "Atha",
}


@dataclass
class GoTerm:
    """A GO stanza, reduced to what the inventory needs."""

    id: str
    name: str = ""
    namespace: str = ""
    is_obsolete: bool = False
    comment: str = ""
    replaced_by: list[str] = field(default_factory=list)
    consider: list[str] = field(default_factory=list)
    is_a: list[str] = field(default_factory=list)
    part_of: list[str] = field(default_factory=list)
    intersection_of: list[tuple[str | None, str]] = field(default_factory=list)


def parse_obo(path: Path) -> dict[str, GoTerm]:
    """Parse the [Term] stanzas of an OBO file.

    >>> import tempfile
    >>> p = Path(tempfile.mkstemp(suffix=".obo")[1])
    >>> _ = p.write_text('[Term]\\nid: GO:1\\nname: a involved in b\\n'
    ...     'intersection_of: GO:2\\nintersection_of: part_of GO:3\\n')
    >>> parse_obo(p)["GO:1"].intersection_of
    [(None, 'GO:2'), ('part_of', 'GO:3')]
    """
    terms: dict[str, GoTerm] = {}
    cur: GoTerm | None = None
    in_term = False
    for line in path.read_text().splitlines():
        if line.startswith("["):
            in_term = line == "[Term]"
            cur = None
            continue
        if not in_term or ": " not in line:
            continue
        tag, val = line.split(": ", 1)
        val = re.sub(r"\s*\{.*\}\s*$", "", val.split(" ! ")[0]).strip()
        if tag == "id":
            cur = GoTerm(id=val)
            terms[val] = cur
        elif cur is None:
            continue
        elif tag == "name":
            cur.name = val
        elif tag == "namespace":
            cur.namespace = val
        elif tag == "is_obsolete":
            cur.is_obsolete = val == "true"
        elif tag == "comment":
            cur.comment = val
        elif tag == "replaced_by":
            cur.replaced_by.append(val)
        elif tag == "consider":
            cur.consider.append(val)
        elif tag == "is_a":
            cur.is_a.append(val)
        elif tag == "relationship" and val.startswith("part_of "):
            cur.part_of.append(val.split()[1])
        elif tag == "intersection_of":
            parts = val.split()
            cur.intersection_of.append(
                (None, parts[0]) if len(parts) == 1 else (parts[0], parts[1])
            )
    return terms


def ancestors(terms: dict[str, GoTerm], tid: str) -> set[str]:
    """Reflexive is_a/part_of ancestors of a term."""
    seen: set[str] = set()
    stack = [tid]
    while stack:
        t = stack.pop()
        if t in seen or t not in terms:
            continue
        seen.add(t)
        stack.extend(terms[t].is_a + terms[t].part_of)
    return seen


def label(terms: dict[str, GoTerm], tid: str) -> str:
    """Label of a term id, or the id itself if unknown."""
    return terms[tid].name if tid in terms else tid


def by_label(terms: dict[str, GoTerm]) -> dict[str, str]:
    """Live term label -> id, for the label-split fallback."""
    return {t.name: tid for tid, t in terms.items() if not t.is_obsolete}


def decomposition(
    terms: dict[str, GoTerm], t: GoTerm, labels: dict[str, str] | None = None
) -> dict | None:
    """Genus + differentia of a term.

    Uses GO's logical definition (``intersection_of``) when present. Otherwise,
    if ``labels`` is given and both halves of "X involved in Y" are exact labels
    of live GO terms, returns that split, marked ``source: label_split`` (a
    heuristic: GO asserts no ``part_of`` here). A differentia filler that is
    itself an "involved in" term is flagged ``nested``.
    """
    if t.intersection_of:
        genus = [g for rel, g in t.intersection_of if rel is None]
        diffs = [(rel, f) for rel, f in t.intersection_of if rel is not None]
        out: dict = {"source": "logical_definition"}
        if genus:
            out["genus"] = {"id": genus[0], "label": label(terms, genus[0])}
            if genus[0] in terms:
                out["genus_aspect"] = terms[genus[0]].namespace
        out["differentia"] = [
            {"relation": rel, "id": f, "label": label(terms, f)} for rel, f in diffs
        ]
    elif labels is not None and INVOLVED_IN in t.name:
        x, y = t.name.removeprefix("obsolete ").split(INVOLVED_IN, 1)
        if x not in labels or y not in labels:
            return None
        out = {
            "source": "label_split",
            "genus": {"id": labels[x], "label": x},
            "genus_aspect": terms[labels[x]].namespace,
            "differentia": [{"relation": "part_of", "id": labels[y], "label": y}],
        }
    else:
        return None
    out["nested"] = any(INVOLVED_IN in d["label"] for d in out["differentia"])
    return out


def pattern_of(
    terms: dict[str, GoTerm], t: GoTerm, labels: dict[str, str] | None = None
) -> str:
    """Short pattern code, e.g. ``MF part_of BP``, ``BP part_of BP``, ``unparsed``.

    The aspect is taken from the genus; the differentia aspect from the filler.
    """
    dec = decomposition(terms, t, labels)
    if not dec or "genus" not in dec or not dec["differentia"]:
        return "no logical definition"
    asp = {
        "molecular_function": "MF",
        "biological_process": "BP",
        "cellular_component": "CC",
    }
    g = asp.get(dec.get("genus_aspect", ""), "?")
    d = dec["differentia"][0]
    f = asp.get(terms[d["id"]].namespace, "other") if d["id"] in terms else "other"
    tag = " (label split)" if dec["source"] == "label_split" else ""
    return f"{g} {d['relation']} {f}{tag}"


def load_index() -> list[dict]:
    """Rows of the GO-CAM activity index."""
    with (REPO / "gocams/index.tsv").open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def index_lookup(rows: list[dict]) -> tuple[dict, dict]:
    """Index rows by UniProt accession and by (lowercased) symbol."""
    by_acc: dict[str, list[dict]] = defaultdict(list)
    by_sym: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        gp = r["gene_product"]
        if gp.startswith("UniProtKB:"):
            by_acc[gp.split(":", 1)[1].split("-")[0]].append(r)
        sym = r["gene_label"].rsplit(" ", 1)[0] if " " in r["gene_label"] else ""
        if sym:
            by_sym[sym.lower()].append(r)
    return by_acc, by_sym


def gocam_hits(
    terms: dict[str, GoTerm],
    rows: list[dict],
    dec: dict | None,
) -> list[dict]:
    """Summarize GO-CAM activities, flagging those that realize the decomposition.

    ``covers_genus``: the activity's MF (or, for BP genera, its BP) is the genus
    or a descendant of it.  ``covers_differentia``: the activity's BP is the
    differentia filler or one of its descendants (is_a/part_of).
    """
    out = []
    seen = set()
    for r in rows:
        key = (r["model_id"], r["activity_id"])
        if key in seen:
            continue
        seen.add(key)
        hit = {
            "model": r["model_id"],
            "title": r["model_title"],
            "gene_label": r["gene_label"],
            "mf": f"{r['molecular_function']} {r['mf_label']}".strip(),
            "bp": f"{r['biological_process']} {r['bp_label']}".strip(),
        }
        if dec and "genus" in dec:
            g = dec["genus"]["id"]
            node = (
                r["molecular_function"]
                if dec.get("genus_aspect") == "molecular_function"
                else r["biological_process"]
            )
            hit["covers_genus"] = bool(node) and g in ancestors(terms, node)
            fill = {d["id"] for d in dec["differentia"]}
            bp = r["biological_process"]
            hit["covers_differentia"] = bool(bp) and bool(fill & ancestors(terms, bp))
        out.append(hit)
    return out


def module_hits(accession: str, symbol: str, modules: dict[str, str]) -> list[str]:
    """Module files whose text mentions the accession (or ``UniProtKB:`` symbol)."""
    return sorted(
        name
        for name, text in modules.items()
        if accession in text or f"symbol: {symbol}\n" in text
    )


def authored_uses(doc: dict, gene: str, inv: dict[str, GoTerm]) -> list[dict]:
    """Precomposed terms a reviewer authored, rather than inherited from GOA.

    Covers MODIFY replacement terms, core-function terms and isoform-specific
    terms. These are the places a review can introduce a precomposed term, as
    opposed to the GOA rows it reviews.

    >>> t = {"GO:1": GoTerm(id="GO:1", name="x involved in y")}
    >>> doc = {"existing_annotations": [{"term": {"id": "GO:2"},
    ...   "review": {"action": "MODIFY",
    ...              "proposed_replacement_terms": [{"id": "GO:1", "label": "x involved in y"}]}}],
    ...   "core_functions": [{"molecular_function": {"id": "GO:1", "label": "x involved in y"}}],
    ...   "functional_isoforms": [{"id": "X-1", "isoform_specific_terms": [{"id": "GO:1"}]}]}
    >>> [u["slot"] for u in authored_uses(doc, "human/X", t)]
    ['proposed_replacement_terms', 'core_functions.molecular_function', 'functional_isoforms.isoform_specific_terms']
    """

    def precomposed(term: dict) -> bool:
        return term.get("id") in inv or INVOLVED_IN in str(term.get("label", ""))

    out = []
    for ea in doc.get("existing_annotations") or []:
        review = ea.get("review") or {}
        for t in review.get("proposed_replacement_terms") or []:
            if precomposed(t):
                out.append(
                    {
                        "gene": gene,
                        "slot": "proposed_replacement_terms",
                        "term": f"{t.get('id')} {t.get('label', '')}".strip(),
                        "from": (ea.get("term") or {}).get("id"),
                    }
                )
    for cf in doc.get("core_functions") or []:
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            t = cf.get(slot) or {}
            if precomposed(t):
                out.append(
                    {
                        "gene": gene,
                        "slot": f"core_functions.{slot}",
                        "term": f"{t.get('id')} {t.get('label', '')}".strip(),
                    }
                )
        for t in cf.get("directly_involved_in") or []:
            if precomposed(t):
                out.append(
                    {
                        "gene": gene,
                        "slot": "core_functions.directly_involved_in",
                        "term": f"{t.get('id')} {t.get('label', '')}".strip(),
                    }
                )
    for iso in doc.get("functional_isoforms") or []:
        for t in iso.get("isoform_specific_terms") or []:
            if isinstance(t, dict) and precomposed(t):
                out.append(
                    {
                        "gene": gene,
                        "slot": "functional_isoforms.isoform_specific_terms",
                        "term": f"{t.get('id')} {t.get('label', '')}".strip(),
                        "isoform": iso.get("id"),
                    }
                )
    return out


def _term_dicts(node: Any) -> list[dict]:
    """Every ``term`` mapping in a nested YAML structure."""
    if isinstance(node, dict):
        found = [node["term"]] if isinstance(node.get("term"), dict) else []
        return found + [t for v in node.values() for t in _term_dicts(v)]
    if isinstance(node, list):
        return [t for item in node for t in _term_dicts(item)]
    return []


def module_annoton_uses(node: Any, module: str, inv: dict[str, GoTerm]) -> list[dict]:
    """Precomposed terms used anywhere in a module annoton.

    An annoton is a mapping with a ``function``. Every term inside it is
    checked (function, processes, targets, inputs, locations), and the slot is
    the annoton key it sits under.

    >>> t = {"GO:1": GoTerm(id="GO:1", name="x involved in y")}
    >>> doc = {"parts": [{"node": {"annotons": [
    ...     {"id": "a1", "function": {"term": {"id": "GO:1"}}},
    ...     {"id": "a2", "function": {"term": {"id": "GO:3"}},
    ...      "processes": [{"term": {"id": "GO:1"}}]}]}}]}
    >>> [(u["annoton"], u["slot"]) for u in module_annoton_uses(doc, "m", t)]
    [('a1', 'module.annoton.function'), ('a2', 'module.annoton.processes')]
    """
    if isinstance(node, list):
        return [u for item in node for u in module_annoton_uses(item, module, inv)]
    if not isinstance(node, dict):
        return []
    if "function" not in node:
        return [u for v in node.values() for u in module_annoton_uses(v, module, inv)]
    out = []
    for key, value in node.items():
        for term in _term_dicts(value):
            if term.get("id") in inv or INVOLVED_IN in str(term.get("label", "")):
                out.append(
                    {
                        "module": module,
                        "slot": f"module.annoton.{key}",
                        "term": f"{term.get('id')} {term.get('label', '')}".strip(),
                        "annoton": node.get("id"),
                    }
                )
    return out


def main() -> None:
    """Build the inventory."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--go", type=Path, required=True, help="GO go.obo (full)")
    ap.add_argument("--out", type=Path, required=True, help="output directory")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    terms = parse_obo(args.go)
    data_version = next(
        (
            line.split(": ", 1)[1].strip()
            for line in args.go.open()
            if line.startswith("data-version:")
        ),
        "unknown",
    )
    labels = by_label(terms)
    inv = {tid: t for tid, t in terms.items() if INVOLVED_IN in t.name}

    go_rows = []
    for tid, t in sorted(inv.items()):
        row = {
            "id": tid,
            "label": t.name,
            "aspect": t.namespace,
            "obsolete": t.is_obsolete,
            "pattern": pattern_of(terms, t, labels),
        }
        dec = decomposition(terms, t, labels)
        if dec:
            row["decomposition"] = dec
        if t.is_obsolete:
            row["obsoletion_comment"] = t.comment
            row["replaced_by"] = [
                {"id": r, "label": label(terms, r)} for r in t.replaced_by
            ]
            row["consider"] = [{"id": c, "label": label(terms, c)} for c in t.consider]
        go_rows.append(row)

    index_rows = load_index()
    by_acc, by_sym = index_lookup(index_rows)
    modules = {p.name: p.read_text() for p in sorted((REPO / "modules").glob("*.yaml"))}

    ann_rows = []
    authored = []
    for name, text in modules.items():
        authored.extend(
            module_annoton_uses(
                yaml.load(text, Loader=yaml.CSafeLoader),
                name.removesuffix(".yaml"),
                inv,
            )
        )
    for path in sorted((REPO / "genes").glob("*/*/*-ai-review.yaml")):
        doc = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if not isinstance(doc, dict):
            continue
        org = path.parts[-3]
        acc = str(doc.get("id", ""))
        sym = str(doc.get("gene_symbol", ""))
        authored.extend(authored_uses(doc, f"{org}/{path.parts[-2]}", inv))
        for ea in doc.get("existing_annotations") or []:
            term = ea.get("term") or {}
            tid, tlabel = term.get("id", ""), term.get("label", "")
            if tid not in inv and INVOLVED_IN not in str(tlabel):
                continue
            t = inv.get(tid) or terms.get(tid)
            dec = decomposition(terms, t, labels) if t else None
            review = ea.get("review") or {}
            same = list(by_acc.get(acc, []))
            suffix = INDEX_SPECIES.get(org)
            if suffix:
                same += [
                    r
                    for r in by_sym.get(sym.lower(), [])
                    if r["gene_label"].endswith(suffix)
                ]
            ortho = [r for r in by_sym.get(sym.lower(), []) if r not in same]
            same_hits = gocam_hits(terms, same, dec)
            ortho_hits = gocam_hits(terms, ortho, dec)
            row = {
                "gene": f"{org}/{path.parts[-2]}",
                "id": acc,
                "term": {"id": tid, "label": tlabel},
                "obsolete_in_go": bool(t and t.is_obsolete),
                "pattern": pattern_of(terms, t, labels)
                if t
                else "term not in GO release",
                "evidence_type": ea.get("evidence_type"),
                "reference": ea.get("original_reference_id"),
                "qualifier": ea.get("qualifier"),
                "has_extensions": bool(ea.get("extensions")),
                "action": review.get("action"),
                "decomposition_recorded": bool(review.get("decomposed_into")),
                "proposed_replacement_terms": [
                    f"{r.get('id')} {r.get('label', '')}".strip()
                    for r in review.get("proposed_replacement_terms") or []
                ],
            }
            if dec:
                row["decomposition"] = dec
            row["gocam_same_gene"] = {
                "activities": len(same_hits),
                "covers_genus": sum(h.get("covers_genus", False) for h in same_hits),
                "covers_differentia": sum(
                    h.get("covers_differentia", False) for h in same_hits
                ),
                "realizing": [h for h in same_hits if h.get("covers_differentia")][:5],
            }
            row["gocam_same_symbol_other_species"] = {
                "activities": len(ortho_hits),
                "covers_differentia": sum(
                    h.get("covers_differentia", False) for h in ortho_hits
                ),
                "realizing": [h for h in ortho_hits if h.get("covers_differentia")][:5],
            }
            row["modules"] = module_hits(acc, sym, modules)
            ann_rows.append(row)

    def count(rows: list[dict], key: str) -> dict:
        return dict(Counter(str(r[key]) for r in rows).most_common())

    live = [r for r in go_rows if not r["obsolete"]]
    obs = [r for r in go_rows if r["obsolete"]]
    gocam_comment = [r for r in obs if "GO-CAM" in r.get("obsoletion_comment", "")]
    genes = {r["gene"] for r in ann_rows}
    summary = {
        "go_release": data_version,
        "go_terms": {
            "live": len(live),
            "obsolete": len(obs),
            "obsolete_with_gocam_comment": len(gocam_comment),
            "live_by_aspect": count(live, "aspect"),
            "live_by_pattern": count(live, "pattern"),
        },
        "review_annotations": {
            "rows": len(ann_rows),
            "genes": len(genes),
            "distinct_terms": len({r["term"]["id"] for r in ann_rows}),
            "rows_on_obsolete_terms": sum(r["obsolete_in_go"] for r in ann_rows),
            "by_pattern": count(ann_rows, "pattern"),
            "by_action": count(ann_rows, "action"),
            "by_evidence": count(ann_rows, "evidence_type"),
            "rows_nested": sum(
                bool((r.get("decomposition") or {}).get("nested")) for r in ann_rows
            ),
            "rows_decomposition_recorded": sum(
                r["decomposition_recorded"] for r in ann_rows
            ),
            "rows_with_extensions": sum(r["has_extensions"] for r in ann_rows),
            "rows_gene_in_any_gocam": sum(
                r["gocam_same_gene"]["activities"] > 0 for r in ann_rows
            ),
            "rows_gocam_realizes_differentia_same_gene": sum(
                r["gocam_same_gene"]["covers_differentia"] > 0 for r in ann_rows
            ),
            "rows_gocam_realizes_differentia_other_species": sum(
                r["gocam_same_symbol_other_species"]["covers_differentia"] > 0
                for r in ann_rows
            ),
            "rows_gene_in_module": sum(bool(r["modules"]) for r in ann_rows),
            "top_terms": dict(
                Counter(
                    f"{r['term']['id']} {r['term']['label']}" for r in ann_rows
                ).most_common(40)
            ),
        },
    }

    # Module candidates: group rows by the differentia filler (the "Y" context),
    # and record which modules already mention Y's GO id.
    by_ctx: dict[str, set[str]] = defaultdict(set)
    ctx_label: dict[str, str] = {}
    for r in ann_rows:
        for d in (r.get("decomposition") or {}).get("differentia", []):
            by_ctx[d["id"]].add(r["gene"])
            ctx_label[d["id"]] = d["label"]
    candidates = [
        {
            "context": {"id": cid, "label": ctx_label[cid]},
            "n_genes": len(genes_),
            "genes": sorted(genes_),
            "modules_mentioning_context": sorted(
                n for n, text in modules.items() if cid in text
            ),
        }
        for cid, genes_ in sorted(by_ctx.items(), key=lambda kv: -len(kv[1]))
    ]
    summary["module_candidates"] = {
        "contexts": len(candidates),
        "contexts_with_3plus_genes": sum(c["n_genes"] >= 3 for c in candidates),
        "contexts_3plus_genes_no_module": sum(
            c["n_genes"] >= 3 and not c["modules_mentioning_context"]
            for c in candidates
        ),
    }

    summary["authored_precomposed"] = {
        "uses": len(authored),
        "genes": len({a["gene"] for a in authored if "gene" in a}),
        "modules": len({a["module"] for a in authored if "module" in a}),
        "by_slot": dict(Counter(a["slot"] for a in authored).most_common()),
    }

    dump = dict(sort_keys=False, allow_unicode=True, width=100)
    (args.out / "go_terms.yaml").write_text(yaml.safe_dump(go_rows, **dump))
    (args.out / "annotations.yaml").write_text(yaml.safe_dump(ann_rows, **dump))
    (args.out / "module_candidates.yaml").write_text(yaml.safe_dump(candidates, **dump))
    (args.out / "authored_precomposed.yaml").write_text(
        yaml.safe_dump(authored, **dump)
    )
    (args.out / "summary.yaml").write_text(yaml.safe_dump(summary, **dump))
    print(yaml.safe_dump(summary, **dump))


if __name__ == "__main__":
    main()
