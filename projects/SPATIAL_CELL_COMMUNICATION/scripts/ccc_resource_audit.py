"""Audit cell-cell communication (CCC) ligand-receptor resources against GO and curation.

Track A of projects/SPATIAL_CELL_COMMUNICATION.md. For every human protein
ligand-receptor interaction in CellPhoneDB (directionality ``Ligand-Receptor``,
``is_ppi`` True; small-molecule interactions are counted but not audited), ask:

Q1  ligand_activity: does some ligand subunit enable GO:0048018 receptor ligand
    activity or an is_a descendant in GOA? Ligand subunits that instead carry only
    an MF under GO:0005102 signaling receptor binding are listed as
    ``binding_only``.
Q2  shared_pathway: is some ligand subunit and some receptor subunit involved_in
    the same specific signaling pathway, allowing one term to be an is_a/part_of
    ancestor of the other? "Specific" means a strict descendant of GO:0007165
    signal transduction other than the generic GO:0007166 / GO:0007186 roots.
Q3  gocam: do a ligand subunit and a receptor subunit appear in the same
    production GO-CAM model (gocams/index.tsv)? If so, does the model have a
    direct causal edge from an activity enabled by a ligand subunit to one
    enabled by a receptor subunit (gocams/<id>/<id>-src.yaml), and is the
    ligand's MF in that edge receptor ligand activity or a descendant?
    module: does a curated module (modules/*.yaml) list a ligand subunit on a
    ligand-activity annoton and a receptor subunit on another annoton of the
    same module? Matching uses the UniProt accessions written in the module
    (gene or representative_members); family members not written out are not
    matched, so this undercounts pan-species modules.
Q4  reviews: is each side reviewed in genes/human, does the ligand's review have
    a ligand-activity core function, and did it REMOVE any ligand-activity row?

Categories (first match wins):
  review_flag         the ligand's review REMOVEs its ligand-activity rows and keeps
                      none (no ACCEPT/KEEP_AS_NON_CORE/NEW row, no core function)
  concordant          in a module, Q1 and Q2 true
  go_gap              in a module, Q1 or Q2 false
  go_supported        not in a module, Q1 and Q2 true (module candidate)
  partial_go          not in a module, exactly one of Q1/Q2 true
  resource_only       not in a module, neither Q1 nor Q2

Also writes module ligand-receptor pairs absent from CellPhoneDB (module_only:
every ligand x signaling-receptor accession pair within one module, so modules
with several ligand-receptor steps yield some non-cognate pairs; the
q2_shared_pathways column helps separate them),
and compares CellPhoneDB with OmniPath at the protein-pair level.

GOA counts positive rows of any evidence code (BP involved_in, MF enables), as in
projects/LIGANDS_IN_SIGNALING/scripts/ligand_gap_check.py, whose GO reader is reused.

Usage:
  projects/SPATIAL_CELL_COMMUNICATION/scripts/fetch_data.sh
  uv run python projects/SPATIAL_CELL_COMMUNICATION/scripts/ccc_resource_audit.py \
      --data .cache/spatial_ccc --out projects/SPATIAL_CELL_COMMUNICATION/results
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "projects/LIGANDS_IN_SIGNALING/scripts"))
from go_ontology import GO  # noqa: E402

LIGAND_ACTIVITY = "GO:0048018"
RECEPTOR_BINDING = "GO:0005102"
SIGNAL_TRANSDUCTION = "GO:0007165"
TRANSDUCER_ACTIVITY = "GO:0060089"
SIGNALING_RECEPTOR = "GO:0038023"
KEPT_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW"}
GENERIC_ROOTS = {"GO:0007165", "GO:0007166", "GO:0007186"}


# ---------------------------------------------------------------- GOA
def load_goa(path: Path, go: GO):
    """Return per-UniProt MF set, signaling-BP set, and symbol map."""
    mf: dict[str, set[str]] = collections.defaultdict(set)
    bp: dict[str, set[str]] = collections.defaultdict(set)
    symbol: dict[str, str] = {}
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            c = line.rstrip("\n").split("\t")
            if len(c) < 15 or c[0] != "UniProtKB" or "NOT" in c[3]:
                continue
            acc, term, aspect, qual = c[1], c[4], c[8], c[3]
            symbol.setdefault(acc, c[2])
            if aspect == "F" and "enables" in qual:
                mf[acc].add(term)
            elif aspect == "P" and "involved_in" in qual:
                if SIGNAL_TRANSDUCTION in go.ancestors(term, with_part_of=True):
                    bp[acc].add(term)
    return mf, bp, symbol


def has_ligand_mf(go: GO, terms: set[str]) -> bool:
    return any(LIGAND_ACTIVITY in go.ancestors(t) for t in terms)


def binding_only_terms(go: GO, terms: set[str]) -> list[str]:
    return sorted(t for t in terms
                  if RECEPTOR_BINDING in go.ancestors(t) and LIGAND_ACTIVITY not in go.ancestors(t))


def shared_pathways(go: GO, bp_l: set[str], bp_r: set[str]) -> list[str]:
    """Specific signaling terms shared by the two sides (one may subsume the other).

    Returns the more general term of each related pair, so the result names a
    pathway both sides are (transitively) involved in.
    """
    out = set()
    for a in bp_l:
        anc_a = go.ancestors(a, with_part_of=True)
        for b in bp_r:
            if a == b:
                shared = a
            elif b in anc_a:
                shared = b
            elif a in go.ancestors(b, with_part_of=True):
                shared = a
            else:
                continue
            if shared not in GENERIC_ROOTS:
                out.add(shared)
    return sorted(out)


# ---------------------------------------------------------------- CellPhoneDB
def load_cpdb(d: Path):
    complexes = {}
    for row in csv.DictReader(open(d / "complex_input.csv")):
        complexes[row["complex_name"]] = [row[f"uniprot_{i}"] for i in range(1, 6) if row[f"uniprot_{i}"]]
    rows = list(csv.DictReader(open(d / "interaction_input.csv")))

    def subunits(partner: str) -> list[str]:
        return complexes.get(partner, [partner])

    return rows, subunits


# ---------------------------------------------------------------- GO-CAMs
def load_gocams(path: Path):
    """UniProt accession -> production models, from gocams/index.tsv.

    The index lists a complex by its complex term, not its members, so models with
    a non-UniProt enabler are read from their -src.yaml to add complex parts.
    """
    models: dict[str, set[str]] = collections.defaultdict(set)
    titles: dict[str, str] = {}
    with_complexes = set()
    for row in csv.DictReader(open(path), delimiter="\t"):
        gp = row["gene_product"]
        titles[row["model_id"]] = row["model_title"]
        if gp.startswith("UniProtKB:"):
            models[gp.split(":", 1)[1].split("-")[0]].add(row["model_id"])
        elif gp.startswith(("GO:", "ComplexPortal:")):
            with_complexes.add(row["model_id"])
    for m in with_complexes:
        for _aid, enablers, _mf, _causal in model_activities(m):
            for acc in enablers:
                models[acc].add(m)
    return models, titles


def _enablers(enabled_by: dict) -> set[str]:
    """UniProt accessions enabling an activity: the gene product, or complex parts (has_part)."""
    out = set()
    for tid in [enabled_by.get("term", "")] + [(p or {}).get("term", "") for p in enabled_by.get("has_part") or []]:
        if isinstance(tid, str) and tid.startswith("UniProtKB:"):
            out.add(tid.split(":", 1)[1].split("-")[0])
    return out


_MODEL_CACHE: dict[str, list[tuple[str, set[str], str, list[tuple[str, str]]]]] = {}


def model_activities(model_id: str):
    """[(activity id, enabling accessions, MF id, [(predicate, downstream id)])] for a cached model."""
    if model_id not in _MODEL_CACHE:
        path = REPO / "gocams" / model_id / f"{model_id}-src.yaml"
        acts = []
        if path.exists():
            doc = yaml.safe_load(open(path)) or {}
            for a in doc.get("activities") or []:
                acts.append((
                    a.get("id", ""),
                    _enablers(a.get("enabled_by") or {}),
                    ((a.get("molecular_function") or {}).get("term") or ""),
                    [(c.get("predicate", ""), c.get("downstream_activity", ""))
                     for c in a.get("causal_associations") or []],
                ))
        _MODEL_CACHE[model_id] = acts
    return _MODEL_CACHE[model_id]


def gocam_links(models: list[str], lig: list[str], rec: list[str]) -> list[dict]:
    """Direct causal edges from a ligand-subunit activity to a receptor-subunit activity."""
    out = []
    for m in models:
        acts = model_activities(m)
        by_id = {a[0]: a for a in acts}
        for aid, enablers, mf_id, causal in acts:
            if not enablers & set(lig):
                continue
            for pred, down in causal:
                d = by_id.get(down)
                if d and d[1] & set(rec):
                    out.append({"model": m, "ligand_mf": mf_id, "predicate": pred, "receptor_mf": d[2]})
    return out


# ---------------------------------------------------------------- modules
def _uniprots_in(obj) -> set[str]:
    """Every UniProtKB accession written anywhere inside obj (complex members included)."""
    out = set()
    if isinstance(obj, dict):
        tid = (obj.get("term") or {}).get("id", "") if isinstance(obj.get("term"), dict) else ""
        if tid.startswith("UniProtKB:"):
            out.add(tid.split(":", 1)[1].split("-")[0])
        for v in obj.values():
            out |= _uniprots_in(v)
    elif isinstance(obj, list):
        for v in obj:
            out |= _uniprots_in(v)
    return out


def _annotons(obj):
    """Yield every annoton dict (members of an ``annotons`` list) in a module tree."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "annotons" and isinstance(v, list):
                for a in v:
                    if isinstance(a, dict):
                        yield a
            yield from _annotons(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _annotons(v)


def load_modules(go: GO, modules_dir: Path):
    """Per module: (ligand, receptor-side, signaling-receptor accessions).

    Reads each annoton directly, so subunits of PROTEIN_COMPLEX participants and
    family representative_members are all included. Ligand annotons enable
    GO:0048018 or a descendant. Receptor-side annotons enable GO:0060089 molecular
    transducer activity or a descendant (signaling receptor activity sits there),
    or state no function; downstream effectors such as kinases are excluded. The
    third set keeps only annotons that enable GO:0038023 signaling receptor
    activity or a descendant, for the module_only report.
    """
    out = {}
    failed = []
    for path in sorted(modules_dir.glob("*.yaml")):
        try:
            doc = yaml.safe_load(open(path)) or {}
        except Exception as exc:  # noqa: BLE001 - report and continue
            failed.append(f"{path.name}: {type(exc).__name__}")
            continue
        lig, other, strict = set(), set(), set()
        for annoton in _annotons(doc.get("module") or {}):
            accs = _uniprots_in(annoton.get("participant") or {})
            fids = [tid for d in (annoton.get("function"),
                                  (annoton.get("participant") or {}).get("required_function"))
                    if (tid := (((d or {}).get("term")) or {}).get("id", "")).startswith("GO:")]
            if any(LIGAND_ACTIVITY in go.ancestors(f) for f in fids):
                lig |= accs
            elif not fids or any(TRANSDUCER_ACTIVITY in go.ancestors(f) for f in fids):
                other |= accs
                if any(SIGNALING_RECEPTOR in go.ancestors(f) for f in fids):
                    strict |= accs
        if lig:
            out[path.stem] = (lig, other, strict)
    return out, failed


# ---------------------------------------------------------------- gene reviews
ID_RE = re.compile(r"^id:\s*(\S+)", re.M)


def index_reviews(genes_dir: Path):
    idx = {}
    for path in genes_dir.glob("*/*-ai-review.yaml"):
        head = path.read_text(errors="replace")[:400]
        m = ID_RE.search(head)
        if m:
            idx[m.group(1).removeprefix("UniProtKB:")] = path
    return idx


def review_facts(go: GO, path: Path) -> dict:
    d = yaml.safe_load(open(path)) or {}
    core_lig = any(
        (cf.get("molecular_function") or {}).get("id", "").startswith("GO:")
        and LIGAND_ACTIVITY in go.ancestors(cf["molecular_function"]["id"])
        for cf in d.get("core_functions") or []
    )
    lig_rows = [a for a in d.get("existing_annotations") or []
                if a.get("term", {}).get("id", "").startswith("GO:")
                and LIGAND_ACTIVITY in go.ancestors(a["term"]["id"])]
    kept = any((a.get("review") or {}).get("action") in KEPT_ACTIONS for a in lig_rows)
    removed = sorted({
        a["term"]["id"] for a in d.get("existing_annotations") or []
        if (a.get("review") or {}).get("action") == "REMOVE"
        and a.get("term", {}).get("id", "").startswith("GO:")
        and LIGAND_ACTIVITY in go.ancestors(a["term"]["id"])
    })
    return {"core_ligand_mf": core_lig, "removed_ligand_rows": removed,
            "rejects_ligand_activity": bool(removed) and not kept and not core_lig}


# ---------------------------------------------------------------- OmniPath
def load_omnipath(ic_path: Path, int_path: Path) -> set[tuple[str, str]]:
    ligands, receptors = set(), set()
    for row in csv.DictReader(open(ic_path), delimiter="\t"):
        if row["entity_type"] != "protein":
            continue
        if row["category"] == "ligand" and row["transmitter"] == "True":
            ligands.add(row["uniprot"])
        if row["category"] == "receptor" and row["receiver"] == "True":
            receptors.add(row["uniprot"])
    pairs = set()
    for row in csv.DictReader(open(int_path), delimiter="\t"):
        if row["is_directed"] != "True":
            continue
        if not (row["omnipath"] == "True" or row["ligrecextra"] == "True"):
            continue
        s, t = row["source"], row["target"]
        if s in ligands and t in receptors:
            pairs.add((s, t))
    return pairs


def render_results(summary: dict, records: list[dict], module_only: list[dict], go: GO) -> str:
    """Generated RESULTS.md: counts and short lists, every number read from the run."""
    cats = summary["categories"]
    order = ["concordant", "go_gap", "go_supported", "partial_go", "resource_only", "review_flag"]
    linked = collections.Counter(x["category"] for x in records if x["q3_gocam_linked"])
    lines = [
        "# CCC resource audit: results (generated)",
        "",
        "Generated by `scripts/ccc_resource_audit.py`; do not edit by hand.",
        "",
        "## Inputs",
        "",
        f"- CellPhoneDB data {summary['inputs']['cellphonedb']}",
        f"- OmniPath web service, retrieved {summary['inputs']['omnipath_retrieved']}",
        f"- goa_human.gaf generated {summary['inputs']['goa_human_date_generated']}; GO {summary['inputs']['go_data_version']}",
        f"- {summary['inputs']['modules_with_ligand_step']} curated modules with a ligand-activity step; "
        f"{summary['inputs']['human_gene_reviews']} human gene reviews; production GO-CAMs in `gocams/`",
        "",
        "## CellPhoneDB interactions",
        "",
        "| Directionality | Interactions |",
        "|---|---:|",
    ]
    for k, v in sorted(summary["cpdb_interactions_by_directionality"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {k} | {v} |")
    lines += [
        "",
        f"Audited: the {summary['audited_interactions']} protein `Ligand-Receptor` interactions. "
        "Non-PPI interactions (small molecules, represented in CellPhoneDB by their biosynthetic "
        "enzymes) are counted only.",
        "",
        "## Categories",
        "",
        "| Category | Interactions | with a direct GO-CAM link |",
        "|---|---:|---:|",
    ]
    for c in order:
        lines.append(f"| {c} | {cats.get(c, 0)} | {linked.get(c, 0)} |")
    lines += [
        "",
        f"- Q1, ligand subunit enables receptor ligand activity (GO:0048018 or descendant): "
        f"{summary['q1_ligand_activity_true']}; ligand carries only a receptor-binding MF: {summary['q1_binding_only']}.",
        f"- Q2, ligand and receptor share a specific signaling pathway term: {summary['q2_shared_pathway_true']}.",
        f"- Q3, ligand and receptor in the same production GO-CAM: {summary['q3_in_same_gocam']}; "
        f"with a direct causal edge from the ligand's activity to the receptor's: {summary['q3_gocam_direct_link']}; "
        f"edges whose ligand MF is not receptor ligand activity: {summary['q3_gocam_link_ligand_mf_not_ligand_activity']}.",
        f"- Q3, in a curated module (ligand step and receptor-side step): {summary['q3_in_module']}.",
        "",
        "### Receptor-binding MFs carried by ligands that lack a ligand-activity MF",
        "",
        "| GO term | Interactions |",
        "|---|---:|",
    ]
    for t, n in collections.Counter(t for x in records for t in x["binding_only_mf"].split(";") if t).most_common(10):
        lines.append(f"| {t} {go.name.get(t, '')} | {n} |")
    lines += ["", "### Ligand MFs on direct GO-CAM ligand-to-receptor edges", "", "| GO term | Interactions |", "|---|---:|"]
    for t, n in summary["q3_gocam_link_ligand_mf_counts"]:
        lines.append(f"| {t} {go.name.get(t, '')} | {n} |")
    lines += ["", "### go_gap: in a module, but GOA lacks the ligand MF or a shared pathway", "",
              "| Interaction | Module | Q1 | Shared pathway |", "|---|---|---|---|"]
    for x in records:
        if x["category"] == "go_gap":
            lines.append(f"| {x['interaction']} | {x['q3_modules']} | {x['q1_ligand_activity']} | "
                         f"{x['q2_shared_pathways'] or '-'} |")
    lines += ["", "### review_flag: the ligand's review removes its ligand-activity rows and keeps none", "",
              "| Interaction | Removed ligand-activity terms |", "|---|---|"]
    for x in records:
        if x["category"] == "review_flag":
            lines.append(f"| {x['interaction']} | {x['ligand_removed_ligand_rows']} |")
    lines += ["", "### resource_only, by CellPhoneDB classification (top 12)", "", "| Classification | Interactions |", "|---|---:|"]
    for c, n in collections.Counter(x["classification"] or "(none)" for x in records
                                    if x["category"] == "resource_only").most_common(12):
        lines.append(f"| {c} | {n} |")
    lines += ["", "## Module pairs absent from CellPhoneDB", "",
              f"{summary['module_only_pairs']} ligand x signaling-receptor accession pairs from curated modules are "
              "not in CellPhoneDB. Modules with several ligand-receptor steps contribute some non-cognate "
              "pairs; see `module_only_pairs.tsv`. Ligands absent from CellPhoneDB altogether:", ""]
    absent = sorted({(x["module"], x["ligand_symbol"]) for x in module_only if x["ligand_in_cpdb"] is False})
    lines += [f"- {sym} ({mod})" for mod, sym in absent]
    lines += ["", "## OmniPath comparison (protein pairs)", "",
              f"- OmniPath ligand-receptor pairs: {summary['omnipath_pairs']}; CellPhoneDB protein pairs "
              f"(complexes expanded): {summary['cpdb_protein_pairs']}; in both: {summary['omnipath_and_cpdb']}.",
              f"- OmniPath-only pairs: {summary['omnipath_only']}, of which "
              f"{summary['omnipath_only_with_q1_and_q2']} have GO support (Q1 and Q2); see `omnipath_only_pairs.tsv`.",
              ""]
    return "\n".join(lines)


# ---------------------------------------------------------------- main
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=REPO / ".cache/spatial_ccc")
    ap.add_argument("--out", type=Path, default=REPO / "projects/SPATIAL_CELL_COMMUNICATION/results")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    go = GO(args.data / "go-basic.obo")
    mf, bp, symbol = load_goa(args.data / "goa_human.gaf.gz", go)
    gaf_date = next((l.split(":", 1)[1].strip() for l in gzip.open(args.data / "goa_human.gaf.gz", "rt")
                     if l.startswith("!date-generated")), "unknown")
    rows, subunits = load_cpdb(args.data / "cellphonedb")
    gocam_models, gocam_titles = load_gocams(REPO / "gocams/index.tsv")
    modules, module_failures = load_modules(go, REPO / "modules")
    reviews = index_reviews(REPO / "genes/human")
    review_cache: dict[str, dict] = {}

    def rf(acc: str) -> dict | None:
        if acc not in reviews:
            return None
        if acc not in review_cache:
            review_cache[acc] = review_facts(go, reviews[acc])
        return review_cache[acc]

    def sym(accs) -> str:
        return "+".join(symbol.get(a, a) for a in accs)

    counts = collections.Counter(r["directionality"] + ("" if r["is_ppi"] == "True" else " (non-PPI)") for r in rows)
    audited = [r for r in rows if r["directionality"] == "Ligand-Receptor" and r["is_ppi"] == "True"]

    records = []
    cpdb_protein_pairs = set()
    cpdb_ligands = set()
    seen_module_pairs = set()
    for r in audited:
        lig, rec = subunits(r["partner_a"]), subunits(r["partner_b"])
        cpdb_protein_pairs |= {(a, b) for a in lig for b in rec}
        cpdb_ligands |= set(lig)
        lig_mf = set().union(*(mf.get(a, set()) for a in lig))
        q1 = has_ligand_mf(go, lig_mf)
        b_only = [] if q1 else binding_only_terms(go, lig_mf)
        shared = shared_pathways(go, set().union(*(bp.get(a, set()) for a in lig)),
                                 set().union(*(bp.get(b, set()) for b in rec)))
        q2 = bool(shared)
        models = sorted(set().union(*(gocam_models.get(a, set()) for a in lig))
                        & set().union(*(gocam_models.get(b, set()) for b in rec)))
        links = gocam_links(models, lig, rec)
        mods = sorted(m for m, (ml, mo, _s) in modules.items() if set(lig) & ml and set(rec) & mo)
        for m in mods:
            ml, mo, _s = modules[m]
            seen_module_pairs |= {(m, a, b) for a in lig if a in ml for b in rec if b in mo}
        lig_reviews = {a: rf(a) for a in lig if rf(a) is not None}
        rec_reviewed = [b for b in rec if b in reviews]
        removed = sorted({t for f in lig_reviews.values() for t in f["removed_ligand_rows"]})
        if lig_reviews and all(f["rejects_ligand_activity"] for f in lig_reviews.values()):
            cat = "review_flag"
        elif mods:
            cat = "concordant" if (q1 and q2) else "go_gap"
        elif q1 and q2:
            cat = "go_supported"
        elif q1 or q2:
            cat = "partial_go"
        else:
            cat = "resource_only"
        records.append({
            "interaction": r["interactors"] or f"{r['partner_a']}-{r['partner_b']}",
            "ligand": r["partner_a"], "ligand_symbols": sym(lig),
            "receptor": r["partner_b"], "receptor_symbols": sym(rec),
            "classification": r["classification"], "cpdb_source": r["source"],
            "category": cat,
            "q1_ligand_activity": q1, "binding_only_mf": ";".join(b_only),
            "q2_shared_pathways": ";".join(shared),
            "q3_gocam_models": ";".join(models),
            "q3_gocam_linked": ";".join(sorted({l["model"] for l in links})),
            "q3_gocam_ligand_mf": ";".join(sorted({l["ligand_mf"] for l in links})),
            "q3_gocam_ligand_mf_is_ligand_activity": (any(LIGAND_ACTIVITY in go.ancestors(l["ligand_mf"])
                                                          for l in links) if links else ""),
            "q3_modules": ";".join(mods),
            "ligand_reviewed": ";".join(symbol.get(a, a) for a in lig_reviews),
            "ligand_core_ligand_mf": any(f["core_ligand_mf"] for f in lig_reviews.values()) if lig_reviews else "",
            "ligand_removed_ligand_rows": ";".join(removed),
            "receptor_reviewed": ";".join(symbol.get(b, b) for b in rec_reviewed),
        })

    # module-only: human accession pairs in modules that CellPhoneDB lacks
    module_only = []
    for m, (ml, _mo, strict) in sorted(modules.items()):
        human_l = sorted(a for a in ml if a in symbol)
        human_r = sorted(b for b in strict if b in symbol)
        for a in human_l:
            for b in human_r:
                if (a, b) not in cpdb_protein_pairs:
                    shared = shared_pathways(go, bp.get(a, set()), bp.get(b, set()))
                    module_only.append({"module": m, "ligand": a, "ligand_symbol": symbol[a],
                                        "receptor": b, "receptor_symbol": symbol[b],
                                        "ligand_in_cpdb": a in cpdb_ligands,
                                        "q2_shared_pathways": ";".join(shared)})

    op_pairs = load_omnipath(args.data / "omnipath_intercell.tsv", args.data / "omnipath_interactions.tsv")
    op_only = sorted(op_pairs - cpdb_protein_pairs)
    op_only_rows = []
    for a, b in op_only:
        q1 = has_ligand_mf(go, mf.get(a, set()))
        shared = shared_pathways(go, bp.get(a, set()), bp.get(b, set()))
        op_only_rows.append({"ligand": a, "ligand_symbol": symbol.get(a, a), "receptor": b,
                             "receptor_symbol": symbol.get(b, b), "q1_ligand_activity": q1,
                             "q2_shared_pathways": ";".join(shared)})

    def write_tsv(name, recs):
        if not recs:
            return
        with open(args.out / name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(recs[0]), delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerows(recs)

    records.sort(key=lambda x: (x["category"], x["interaction"]))
    write_tsv("cpdb_pair_audit.tsv", records)
    write_tsv("module_only_pairs.tsv", module_only)
    write_tsv("omnipath_only_pairs.tsv", op_only_rows)

    cat_counts = collections.Counter(x["category"] for x in records)
    cls_by_cat = collections.defaultdict(collections.Counter)
    for x in records:
        cls_by_cat[x["category"]][x["classification"]] += 1
    summary = {
        "inputs": {
            "cellphonedb": (args.data / "cellphonedb/VERSION").read_text().strip(),
            "omnipath_retrieved": (args.data / "OMNIPATH_RETRIEVED").read_text().strip(),
            "goa_human_date_generated": gaf_date,
            "go_data_version": go.data_version,
            "modules_with_ligand_step": len(modules),
            "modules_failed_to_compile": module_failures,
            "human_gene_reviews": len(reviews),
        },
        "cpdb_interactions_by_directionality": dict(counts),
        "audited_interactions": len(audited),
        "categories": dict(cat_counts),
        "q1_ligand_activity_true": sum(x["q1_ligand_activity"] for x in records),
        "q1_binding_only": sum(bool(x["binding_only_mf"]) for x in records),
        "q2_shared_pathway_true": sum(bool(x["q2_shared_pathways"]) for x in records),
        "q3_in_same_gocam": sum(bool(x["q3_gocam_models"]) for x in records),
        "q3_gocam_direct_link": sum(bool(x["q3_gocam_linked"]) for x in records),
        "q3_gocam_link_ligand_mf_counts": collections.Counter(
            t for x in records for t in x["q3_gocam_ligand_mf"].split(";") if t).most_common(),
        "q3_gocam_link_ligand_mf_not_ligand_activity": sum(x["q3_gocam_ligand_mf_is_ligand_activity"] is False
                                                           for x in records),
        "q3_in_module": sum(bool(x["q3_modules"]) for x in records),
        "module_pairs_matched_in_cpdb": len(seen_module_pairs),
        "module_only_pairs": len(module_only),
        "omnipath_pairs": len(op_pairs),
        "cpdb_protein_pairs": len(cpdb_protein_pairs),
        "omnipath_and_cpdb": len(op_pairs & cpdb_protein_pairs),
        "omnipath_only": len(op_only),
        "omnipath_only_with_q1_and_q2": sum(r["q1_ligand_activity"] and bool(r["q2_shared_pathways"])
                                            for r in op_only_rows),
        "top_classifications_by_category": {k: v.most_common(8) for k, v in sorted(cls_by_cat.items())},
        "gocam_models_used": {m: gocam_titles[m] for m in sorted({m for x in records
                                                                  for m in x["q3_gocam_models"].split(";") if m})},
    }
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (args.out / "RESULTS.md").write_text(render_results(summary, records, module_only, go))
    print(json.dumps({k: summary[k] for k in ("audited_interactions", "categories", "q3_in_same_gocam", "q3_gocam_direct_link",
                                              "q3_gocam_link_ligand_mf_not_ligand_activity",
                                              "q3_in_module", "module_only_pairs", "omnipath_only")}, indent=2))


if __name__ == "__main__":
    main()
