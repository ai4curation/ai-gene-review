"""Inventory GO "X production" terms and their use in this repo.

Reads a GO edition in OBO format (``go.obo`` from a release, or
``src/ontology/go-edit.obo`` from a go-ontology checkout), every gene review
under ``genes/`` and the GO-CAM activity index (``gocams/index.tsv``), and
writes:

* ``production_terms.yaml`` -- every GO term whose label contains the word
  "production", live or obsolete: kind (production or regulation), the
  do-not-annotate flag, how many terms were merged into it (alt_ids), its
  asserted parents, whether it sits under GO:0001816 cytokine production, a
  heuristic mechanism class, and for obsolete terms the obsoletion comment,
  replacement pointers and tracker issues.
* ``gocam_models.yaml`` -- every cached GO-CAM (``gocams/<id>/<id>-src.yaml``)
  with an activity on such a term: title, contributing groups, which term
  families it uses, whether it names the regulated product (an input molecule
  or a causal edge to a cytokine activity), and all of its activities with
  their function, process, inputs and causal edges.
* ``summary.yaml`` -- counts: live and obsolete terms, do-not-annotate
  coverage, obsoletion reasons, heuristic classes, review actions on these
  terms, genes whose reviews ACCEPT one, and GO-CAM use (activities, models,
  model groups, transcription-factor inputs, and where the most-used genes'
  activities sit across all cached models).

The mechanism class is a **name-pattern heuristic** (see ``CLASS_RULES``),
not a curated judgement. It is there to size the groups discussed on the
project page; a curated classification is a separate step.

Nothing is hardcoded: re-run against a newer GO edition and the outputs move.

Usage::

    python projects/PRODUCTION_TERMS/scripts/inventory.py \\
        --go path/to/go-edit.obo --out projects/PRODUCTION_TERMS/data
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[3]
CYTOKINE_PRODUCTION = "GO:0001816"
DO_NOT_ANNOTATE = "gocheck_do_not_annotate"
PRODUCTION_WORD = re.compile(r"\bproduction\b")
REGULATION_PREFIX = re.compile(r"^(positive |negative )?regulation of ")

# Heuristic mechanism classes, tested in order against the label with any
# "(positive|negative) regulation of" prefix removed. First match wins.
CLASS_RULES: list[tuple[str, str]] = [
    ("il1_family_precursor_processing",
     r"interleukin-1 |interleukin-1$|interleukin-1 beta|interleukin-1 alpha"
     r"|interleukin-18|interleukin-33|interleukin-36|interleukin-37|interleukin-38"),
    ("tnf_superfamily",
     r"tumor necrosis factor|lymphotoxin|TRAIL|CD40 ligand|RANKL|TNFSF11"),
    ("tgf_beta_latency", r"transforming growth factor beta"),
    ("interferon_induction_irf3_irf7",
     r"type I interferon|type III interferon|interferon-alpha|interferon-beta"
     r"|interferon-lambda|interferon-kappa|interferon-omega|interferon-epsilon"
     r"|interferon-tau|interferon-delta"),
    ("cytotoxic_granule_mediator", r"granzyme|perforin|granulysin"),
    ("immunoglobulin", r"immunoglobulin"),
    ("small_molecule_mediator",
     r"histamine|serotonin|nitric oxide|prostaglandin|leukotriene|arachidonate"
     r"|aldosterone|platelet activating factor|reactive oxygen|hydrogen"),
    ("antimicrobial_peptide", r"antimicrobial|antibacterial|antifungal"),
    ("grouping_or_context",
     r"^cytokine production|^chemokine production$| cell cytokine production"
     r"|involved in|production of molecular mediator|in mucosal tissue"
     r"|by symbiont|by virus|symbiont-mediated|by organism|response to"
     r"|^macrophage cytokine|^myeloid leukocyte cytokine"),
    ("shared_programme_output",
     r"interleukin|chemokine|colony-stimulating|growth factor|oncostatin"
     r"|leukemia inhibitory|amphiregulin|XCL1|fractalkine|eotaxin|lymphotactin"
     r"|migration inhibitory|thymic stromal|interferon-gamma|type II interferon"
     r"|neurotrophin|nerve growth factor|cardiotrophin|neurotrophic factor"
     r"|monocyte chemotactic|macrophage inflammatory protein|IP-10|endothelin"),
]

# Obsoletion comment -> reason category. First match wins.
OBSOLETION_REASONS: list[tuple[str, str]] = [
    ("gene_product", r"(represents|refers to) a gene product"),
    ("precomposed_gocam", r"pre-composed"),
    ("readout", r"read ?out"),
    ("unnecessary_grouping", r"unnecessary grouping"),
    ("duplicate_of_signaling_term", r"same process as"),
    ("entity_does_not_exist", r"shown not to exist"),
    ("not_a_real_process",
     r"not represent a real|no evidence that this process exists"
     r"|process does not exist|does not represent a real process"),
    ("poorly_defined", r"not clearly defined"),
]


def parse_obo(path: Path) -> dict[str, dict[str, list[str]]]:
    """Return {id: {tag: [values]}} for every [Term] stanza."""
    terms: dict[str, dict[str, list[str]]] = {}
    cur: dict[str, list[str]] | None = None
    with path.open(encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.startswith("["):
                cur = defaultdict(list) if line == "[Term]" else None
                continue
            if cur is None or ":" not in line:
                continue
            tag, value = line.split(":", 1)
            value = value.strip()
            if tag == "id":
                terms[value] = cur
            cur[tag].append(value)
    return terms


def strip_comment(value: str) -> str:
    return value.split(" !", 1)[0].strip()


def parents(stanza: dict[str, list[str]]) -> list[str]:
    out = [strip_comment(v).split()[0] for v in stanza.get("is_a", [])]
    for rel in stanza.get("relationship", []):
        bits = strip_comment(rel).split()
        if len(bits) >= 2 and bits[0] == "part_of":
            out.append(bits[1])
    for inter in stanza.get("intersection_of", []):
        bits = strip_comment(inter).split()
        if len(bits) == 1 and bits[0].startswith("GO:"):
            out.append(bits[0])
    return out


def ancestors(term_id: str, terms: dict[str, dict[str, list[str]]],
              cache: dict[str, set[str]]) -> set[str]:
    if term_id in cache:
        return cache[term_id]
    seen: set[str] = set()
    stack = [term_id]
    while stack:
        node = stack.pop()
        for parent in parents(terms.get(node, {})):
            if parent not in seen:
                seen.add(parent)
                stack.append(parent)
    cache[term_id] = seen
    return seen


def regulated_target(stanza: dict[str, list[str]]) -> str | None:
    for inter in stanza.get("intersection_of", []):
        bits = strip_comment(inter).split()
        if len(bits) == 2 and bits[0] in {"regulates", "positively_regulates",
                                          "negatively_regulates"}:
            return bits[1]
    return None


def classify(label: str) -> str:
    target = REGULATION_PREFIX.sub("", label)
    for name, pattern in CLASS_RULES:
        if re.search(pattern, target):
            return name
    return "other"


def obsoletion_reason(comment: str) -> str:
    for name, pattern in OBSOLETION_REASONS:
        if re.search(pattern, comment):
            return name
    return "other"


def tracker_issues(stanza: dict[str, list[str]]) -> list[int]:
    out = []
    for value in stanza.get("property_value", []):
        match = re.search(r"term_tracker_item \"https://github.com/geneontology/"
                          r"go-ontology/issues/(\d+)\"", value)
        if match:
            out.append(int(match.group(1)))
    return out


def narrow_synonym_counts(stanza: dict[str, list[str]]) -> tuple[int, int]:
    bio = sec = 0
    for syn in stanza.get("synonym", []):
        match = re.match(r'"(.*)" (\w+)', syn)
        if not match or match.group(2) != "NARROW":
            continue
        if match.group(1).endswith("biosynthetic process"):
            bio += 1
        elif match.group(1).endswith("secretion"):
            sec += 1
    return bio, sec


def build_terms(terms: dict[str, dict[str, list[str]]]) -> list[dict[str, Any]]:
    cache: dict[str, set[str]] = {}
    rows = []
    for term_id, stanza in terms.items():
        name = stanza.get("name", [""])[0]
        if not PRODUCTION_WORD.search(name):
            continue
        obsolete = stanza.get("is_obsolete", ["false"])[0] == "true"
        kind = "regulation" if REGULATION_PREFIX.match(name) else "production"
        bio, sec = narrow_synonym_counts(stanza)
        row: dict[str, Any] = {
            "id": term_id,
            "label": name,
            "kind": kind,
            "obsolete": obsolete,
            "heuristic_class": classify(name.removeprefix("obsolete ")),
        }
        if not obsolete:
            row["do_not_annotate"] = DO_NOT_ANNOTATE in stanza.get("subset", [])
            row["merged_alt_ids"] = len(stanza.get("alt_id", []))
            row["narrow_biosynthesis_synonyms"] = bio
            row["narrow_secretion_synonyms"] = sec
            row["is_a"] = [strip_comment(v) for v in stanza.get("is_a", [])]
            if kind == "regulation":
                target = regulated_target(stanza)
                if target:
                    row["regulates"] = target
            row["under_cytokine_production"] = (
                term_id == CYTOKINE_PRODUCTION
                or CYTOKINE_PRODUCTION in ancestors(term_id, terms, cache))
        else:
            comment = stanza.get("comment", [""])[0]
            row["obsoletion_comment"] = comment
            row["obsoletion_reason"] = obsoletion_reason(comment)
            row["replaced_by"] = stanza.get("replaced_by", [])
            row["consider"] = stanza.get("consider", [])
        issues = tracker_issues(stanza)
        if issues:
            row["tracker_issues"] = issues
        rows.append(row)
    rows.sort(key=lambda r: r["id"])
    return rows


def review_rows(genes_dir: Path, production_ids: set[str]) -> list[dict[str, str]]:
    """Line-based scan of existing_annotations (a full YAML parse of every
    review takes minutes). Captures the first term id and the review action of
    each row."""
    out = []
    id_re = re.compile(r"^ {4}id: (GO:\d{7})")
    label_re = re.compile(r"^ {4}label: (.*)$")
    action_re = re.compile(r"^ {4}action: (\w+)")
    for path in sorted(genes_dir.glob("*/*/*-ai-review.yaml")):
        organism, gene = path.parts[-3], path.parts[-2]
        in_existing = False
        term_id = label = None
        with path.open(encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                if line.startswith("existing_annotations:"):
                    in_existing = True
                    continue
                if not in_existing:
                    continue
                if re.match(r"^[a-z_]+:", line):
                    break
                if line.startswith("- term:"):
                    term_id = label = None
                    continue
                match = id_re.match(line)
                if match and term_id is None:
                    term_id = match.group(1)
                    continue
                match = label_re.match(line)
                if match and label is None:
                    label = match.group(1).strip().strip("'\"")
                    continue
                match = action_re.match(line)
                if match and term_id in production_ids:
                    out.append({"organism": organism, "gene": gene,
                                "term_id": term_id, "label": label or "",
                                "action": match.group(1)})
                    term_id = None
    return out


def read_index(index: Path) -> list[dict[str, str]]:
    if not index.exists():
        return []
    with index.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


HAS_INPUT = "RO:0002233"


def term_family(label: str) -> str:
    """Group the production terms GO-CAMs use: the type I interferon terms, the
    precomposed "... involved in inflammatory response" terms, and the rest."""
    if re.search(r"type I interferon|interferon-alpha|interferon-beta", label):
        return "type_I_interferon"
    if "involved in inflammatory response" in label:
        return "inflammatory_response_precomposed"
    return "other"


def provided_by(node: Any, found: set[str]) -> set[str]:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "provided_by" and isinstance(value, list):
                found.update(str(v) for v in value)
            else:
                provided_by(value, found)
    elif isinstance(node, list):
        for item in node:
            provided_by(item, found)
    return found


def gocam_models(gocam_dir: Path, gocams: list[dict[str, str]],
                 index: list[dict[str, str]], production_ids: set[str],
                 labels: dict[str, str]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Read each cached model that uses a production term and record every
    activity: enabling gene product, function, the process it is part of,
    its has_input molecules and its causal edges. Two signals record whether
    the model names the regulated product: a transcription-factor activity on a
    production term with an input molecule (its target gene), and a causal edge
    from an activity on a production term to an activity whose function is a
    cytokine activity. Inputs of other activities (a kinase's substrate) are
    not counted."""
    models_out = []
    model_ids = sorted({r["model_id"] for r in gocams})
    tf_rows = Counter()
    for model_id in model_ids:
        path = gocam_dir / model_id / f"{model_id}-src.yaml"
        if not path.exists():
            models_out.append({"model_id": model_id, "cached": False})
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        objects = {o["id"]: o.get("label") for o in data.get("objects") or []}
        molecules = {m["id"]: m.get("term") for m in data.get("molecules") or []}
        activities = data.get("activities") or []
        act_label = {a["id"]: objects.get((a.get("enabled_by") or {}).get("term"),
                                          (a.get("enabled_by") or {}).get("term"))
                     for a in activities}
        act_mf = {a["id"]: objects.get((a.get("molecular_function") or {}).get("term"), "")
                  for a in activities}
        acts = []
        families: set[str] = set()
        tf_inputs: set[str] = set()
        cytokine_targets: set[str] = set()
        for act in activities:
            gene = act_label[act["id"]]
            mf_label = act_mf[act["id"]]
            bp = (act.get("part_of") or {}).get("term")
            inputs = [objects.get(molecules.get(m.get("molecule")), molecules.get(m.get("molecule")))
                      for m in act.get("molecular_associations") or []
                      if m.get("predicate") == HAS_INPUT]
            edges = [{"predicate": c.get("predicate"),
                      "to": act_label.get(c.get("downstream_activity"), c.get("downstream_activity")),
                      "to_function": act_mf.get(c.get("downstream_activity"), "")}
                     for c in act.get("causal_associations") or []]
            on_production = bp in production_ids
            if on_production:
                families.add(term_family(labels[bp]))
                cytokine_targets.update(str(e["to"]) for e in edges
                                        if "cytokine activity" in e["to_function"])
                if "transcription" in mf_label:
                    tf_inputs.update(str(i) for i in inputs)
                    key = "with_input" if inputs else "without_input"
                    tf_rows[(term_family(labels[bp]), key)] += 1
            entry: dict[str, Any] = {
                "enabled_by": gene,
                "function": mf_label,
                "part_of": objects.get(bp, bp) if bp else None,
                "part_of_is_production_term": on_production,
            }
            if inputs:
                entry["has_input"] = inputs
            if edges:
                entry["causal"] = [f'{e["predicate"]} -> {e["to"]}' for e in edges]
            acts.append(entry)
        models_out.append({
            "model_id": model_id,
            "title": (data.get("title") or "").strip(),
            "taxon": data.get("taxon"),
            "date_modified": data.get("date_modified"),
            "provided_by": sorted(provided_by(data, set())),
            "term_families": sorted(families),
            "transcription_factor_inputs": sorted(tf_inputs),
            "cytokine_activity_targets": sorted(cytokine_targets),
            "activities": acts,
        })

    cached = [m for m in models_out if m.get("cached", True)]
    by_family: dict[str, list[str]] = defaultdict(list)
    for m in cached:
        key = "+".join(m["term_families"])
        by_family[key].append(m["model_id"])
    group_count = Counter(tuple(m["provided_by"]) for m in cached)
    dates = sorted(str(m["date_modified"]) for m in cached if m.get("date_modified"))

    # Where else do the genes most often placed on a production term sit?
    gene_counts = Counter(r["gene_label"] for r in gocams)
    spread = {}
    for gene, n in gene_counts.most_common():
        if n < 5:
            break
        spread[gene] = dict(Counter(r["bp_label"] or "(none)" for r in index
                                    if r["gene_label"] == gene).most_common())

    stats = {
        "models_cached": len(cached),
        "models_by_term_family": {k: len(v) for k, v in sorted(by_family.items())},
        "models_with_transcription_factor_input": {
            k: sum(1 for m in cached if "+".join(m["term_families"]) == k
                   and m["transcription_factor_inputs"]) for k in sorted(by_family)},
        "models_with_edge_to_cytokine_activity": {
            k: sum(1 for m in cached if "+".join(m["term_families"]) == k
                   and m["cytokine_activity_targets"]) for k in sorted(by_family)},
        "transcription_factor_activities_on_production_terms": {
            f"{fam}/{key}": n for (fam, key), n in sorted(tf_rows.items())},
        "provided_by": {" + ".join(k) or "(none)": v for k, v in group_count.most_common()},
        "date_modified_range": [dates[0], dates[-1]] if dates else [],
        "direct_use_of_production_terms": sorted(
            {f'{r["model_id"]} {r["gene_label"]} -> {r["bp_label"]}' for r in gocams
             if not REGULATION_PREFIX.match(r["bp_label"])}),
        "process_spread_of_most_used_genes": spread,
    }
    return models_out, stats


def summarise(rows: list[dict[str, Any]], reviews: list[dict[str, str]],
              gocams: list[dict[str, str]], labels: dict[str, str]) -> dict[str, Any]:
    live = [r for r in rows if not r["obsolete"]]
    obsolete = [r for r in rows if r["obsolete"]]
    live_prod = [r for r in live if r["kind"] == "production"]
    live_reg = [r for r in live if r["kind"] == "regulation"]
    cyto = [r for r in live_prod if r["under_cytokine_production"]]

    kinds = {r["id"]: r["kind"] for r in rows}
    actions: dict[str, Counter] = defaultdict(Counter)
    for rev in reviews:
        actions[kinds[rev["term_id"]]][rev["action"]] += 1

    accepted: dict[str, set[str]] = defaultdict(set)
    for rev in reviews:
        if rev["action"] == "ACCEPT" and rev["organism"] in {"human", "mouse"}:
            target = REGULATION_PREFIX.sub("", labels.get(rev["term_id"], rev["label"]))
            accepted[f'{rev["organism"]}/{rev["gene"]}'].add(target)

    gocam_terms = Counter(labels.get(r["biological_process"], r["biological_process"])
                          for r in gocams)

    return {
        "terms": {
            "production_named_terms": len(rows),
            "live": len(live),
            "live_production_terms": len(live_prod),
            "live_regulation_terms": len(live_reg),
            "obsolete": len(obsolete),
            "live_production_terms_do_not_annotate": sum(r["do_not_annotate"] for r in live_prod),
            "live_regulation_terms_do_not_annotate": sum(r["do_not_annotate"] for r in live_reg),
            "live_under_cytokine_production": len(cyto),
            "live_under_cytokine_production_do_not_annotate": sum(r["do_not_annotate"] for r in cyto),
            "cytokine_branch_terms_missing_do_not_annotate": sorted(
                f'{r["id"]} {r["label"]}' for r in cyto if not r["do_not_annotate"]),
            "production_terms_outside_cytokine_branch_without_do_not_annotate": sorted(
                f'{r["id"]} {r["label"]}' for r in live_prod
                if not r["under_cytokine_production"] and not r["do_not_annotate"]),
            "alt_ids_on_live_terms": sum(r["merged_alt_ids"] for r in live),
            "narrow_biosynthesis_synonyms_on_live_terms": sum(r["narrow_biosynthesis_synonyms"] for r in live),
            "narrow_secretion_synonyms_on_live_terms": sum(r["narrow_secretion_synonyms"] for r in live),
        },
        "obsoletion_reasons": dict(Counter(r["obsoletion_reason"] for r in obsolete).most_common()),
        "heuristic_classes_live_production_terms": dict(
            Counter(r["heuristic_class"] for r in live_prod).most_common()),
        "heuristic_classes_live_regulation_terms": dict(
            Counter(r["heuristic_class"] for r in live_reg).most_common()),
        "reviews": {
            "rows": len(reviews),
            "genes": len({(r["organism"], r["gene"]) for r in reviews}),
            "actions_by_kind": {k: dict(v.most_common()) for k, v in sorted(actions.items())},
            "human_mouse_genes_with_an_accepted_row": len(accepted),
            "accepted_terms_by_gene": {g: sorted(t) for g, t in sorted(accepted.items())},
        },
        "gocams": {
            "activities": len(gocams),
            "models": len({r["model_id"] for r in gocams}),
            "activities_by_term": dict(gocam_terms.most_common()),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--go", type=Path, required=True, help="go.obo or go-edit.obo")
    parser.add_argument("--genes", type=Path, default=REPO / "genes")
    parser.add_argument("--gocam-index", type=Path, default=REPO / "gocams" / "index.tsv")
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent.parent / "data")
    args = parser.parse_args()

    terms = parse_obo(args.go)
    rows = build_terms(terms)
    production_ids = {r["id"] for r in rows}
    labels = {r["id"]: r["label"] for r in rows}
    reviews = review_rows(args.genes, production_ids)
    index = read_index(args.gocam_index)
    gocams = [r for r in index if r.get("biological_process") in production_ids]
    summary = summarise(rows, reviews, gocams, labels)
    models, model_stats = gocam_models(args.gocam_index.parent, gocams, index,
                                       production_ids, labels)
    summary["gocams"].update(model_stats)
    summary = {"source": {"go_file": args.go.name}, **summary}

    args.out.mkdir(parents=True, exist_ok=True)
    with (args.out / "production_terms.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(rows, fh, sort_keys=False, allow_unicode=True, width=100)
    with (args.out / "gocam_models.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(models, fh, sort_keys=False, allow_unicode=True, width=100)
    with (args.out / "summary.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(summary, fh, sort_keys=False, allow_unicode=True, width=100)
    print(yaml.safe_dump(summary["terms"], sort_keys=False, width=100))


if __name__ == "__main__":
    main()
