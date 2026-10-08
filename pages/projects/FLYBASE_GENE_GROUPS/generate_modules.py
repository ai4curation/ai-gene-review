#!/usr/bin/env python3
"""Generate D. melanogaster ModuleReview YAML files from compact module specs.

Each spec in ``module_specs/<module>.yaml`` holds the curated content of one
module (description, GO grounding, parts, variants and connections) and names
its participants by FlyBase gene symbol or FlyBase group symbol. This script
expands a spec into ``modules/<module>.yaml``:

* gene symbols are resolved to UniProtKB accessions (Swiss-Prot preferred) and
  protein names from ``group_index.yaml``, falling back to the D. melanogaster
  UniProt table; genes without a protein product (snRNAs, lncRNAs) are
  grounded to their FlyBase gene id;
* FlyBase group symbols are expanded to all members of the group's subtree;
* the FlyBase groups that the triage assigns to the module become top-level
  evidence, and regulator-set groups of a pathway are listed in the notes.

Nothing about the participants is typed by hand, so accessions and labels
always come from the FlyBase and UniProt files.

Usage (from the repository root)::

    uv run python projects/FLYBASE_GENE_GROUPS/generate_modules.py            # all specs
    uv run python projects/FLYBASE_GENE_GROUPS/generate_modules.py dmel_augmin_complex
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
TAXON = {"preferred_term": "Drosophila melanogaster",
         "term": {"id": "NCBITaxon:7227", "label": "Drosophila melanogaster"}}


class Folded(str):
    """String emitted as a YAML folded block scalar."""



def recommended_name(full: str) -> str:
    """UniProt 'Recommended (Alt 1) (Alt 2)' -> 'Recommended'.

    Only trailing balanced parenthesised groups are removed, so names that
    contain parentheses themselves (``tRNA (guanine-N(7)-)-methyltransferase``)
    are kept whole.
    """
    name = full.strip()
    while name.endswith(")"):
        depth = 0
        for i in range(len(name) - 1, -1, -1):
            depth += {")": 1, "(": -1}.get(name[i], 0)
            if depth == 0:
                break
        if i <= 0 or name[i - 1] != " ":
            break
        name = name[: i - 1].rstrip()
    return name or full

def _folded(dumper: yaml.Dumper, data: Folded):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style=">")


yaml.add_representer(Folded, _folded)


def fold(text: str | None) -> Folded | None:
    if not text:
        return None
    return Folded(" ".join(str(text).split()))


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def term(t: dict | None) -> dict | None:
    if not t:
        return None
    return {"id": t["id"], "label": t["label"]}


def descriptor(t: dict, preferred: str | None = None, description: str | None = None) -> dict:
    d = {"preferred_term": preferred or t.get("preferred_term") or t["label"], "term": term(t)}
    if description or t.get("description"):
        d["description"] = fold(description or t.get("description"))
    return d


class Resolver:
    def __init__(self, index: dict, uniprot_tsv: Path):
        self.genes_by_symbol: dict[str, tuple[str, dict]] = {}
        for fbgn, g in index["genes"].items():
            self.genes_by_symbol.setdefault(g["symbol"], (fbgn, g))
        self.group_ids = {g["symbol"]: g["id"] for g in index["groups"]}
        self.groups = {g["id"]: g for g in index["groups"]}
        self.uniprot: dict[str, dict] = {}
        with open(uniprot_tsv) as fh:
            next(fh)
            for line in fh:
                acc, reviewed, gene, name, fb, length = line.rstrip("\n").split("\t")
                cur = self.uniprot.get(gene)
                key = (reviewed == "reviewed", int(length or 0))
                if gene and (cur is None or key > cur["key"]):
                    self.uniprot[gene] = {
                        "key": key, "accession": acc,
                        "protein_name": recommended_name(name),
                        "fbgn": fb.split(";")[0] or None,
                    }

    def subtree(self, gid: str) -> set[str]:
        g = self.groups[gid]
        out = set(g["direct_members"])
        for c in g["children"]:
            out |= self.subtree(c)
        return out

    def group_genes(self, symbol: str) -> list[str]:
        if symbol not in self.group_ids:
            raise KeyError(f"unknown FlyBase group symbol {symbol!r}")
        members = self.subtree(self.group_ids[symbol])
        index_genes = {fbgn: sym for sym, (fbgn, _) in self.genes_by_symbol.items()}
        return sorted(index_genes[f] for f in members)

    def gene(self, symbol: str) -> dict:
        if symbol in self.genes_by_symbol:
            fbgn, g = self.genes_by_symbol[symbol]
            if g["uniprot"]:
                return {"symbol": symbol, "fbgn": fbgn, "accession": g["uniprot"],
                        "protein_name": g["protein_name"]}
            return {"symbol": symbol, "fbgn": fbgn, "accession": None, "protein_name": None}
        if symbol in self.uniprot:
            u = self.uniprot[symbol]
            return {"symbol": symbol, "fbgn": u["fbgn"], "accession": u["accession"],
                    "protein_name": u["protein_name"]}
        raise KeyError(f"unknown D. melanogaster gene symbol {symbol!r}")


def participant(g: dict) -> dict:
    if g["accession"]:
        return {"selector_type": "GENE_PRODUCT", "gene_product": {
            "preferred_term": g["symbol"],
            "term": {"id": f"UniProtKB:{g['accession']}", "label": g["protein_name"]}}}
    return {"selector_type": "GENE", "gene": {
        "preferred_term": g["symbol"],
        "term": {"id": f"FB:{g['fbgn']}", "label": g["symbol"]}}}


def member_symbols(spec: dict, res: Resolver) -> list[str]:
    syms: list[str] = []
    for grp in spec.get("groups", []) or ([spec["group"]] if spec.get("group") else []):
        syms += res.group_genes(grp)
    syms += spec.get("genes", [])
    exclude = set(spec.get("exclude", []))
    seen, out = set(), []
    for s in syms:
        if s not in seen and s not in exclude:
            seen.add(s)
            out.append(s)
    if not out:
        raise ValueError(f"{spec.get('id')}: no members")
    return out


def build_annotons(spec: dict, res: Resolver, as_complex: bool) -> list[dict]:
    genes = [res.gene(s) for s in member_symbols(spec, res)]
    roles = spec.get("roles", {})
    unit_functions = spec.get("unit_functions", {})
    fn = spec.get("function")
    procs = [descriptor(p) for p in spec.get("processes", [])]
    locs = [descriptor(p) for p in spec.get("locations", [])]
    if as_complex and len(genes) > 1:
        units = []
        for g in genes:
            u = {"id": slug(g["symbol"]), "label": g["symbol"], "participant": participant(g)}
            if g["symbol"] in roles:
                u["role"] = roles[g["symbol"]]
            if g["symbol"] in unit_functions:
                u["function"] = descriptor(unit_functions[g["symbol"]])
            units.append(u)
        pc = {"preferred_term": spec.get("complex_label", spec["label"])}
        if spec.get("complex_term"):
            pc["term"] = term(spec["complex_term"])
        pc["active_units"] = units
        ann = {"id": f"{spec['id']}_complex", "label": spec.get("complex_label", spec["label"]),
               "participant": {"selector_type": "PROTEIN_COMPLEX", "protein_complex": pc}}
        if fn:
            ann["function"] = descriptor(fn)
        if procs:
            ann["processes"] = procs
        if locs:
            ann["locations"] = locs
        if spec.get("role_description"):
            ann["role_description"] = fold(spec["role_description"])
        return [ann]
    anns = []
    for g in genes:
        ann = {"id": f"{spec['id']}_{slug(g['symbol'])}",
               "label": f"{g['symbol']} {spec.get('annoton_label', spec['label'])}".strip(),
               "participant": participant(g)}
        f = unit_functions.get(g["symbol"], fn)
        if f:
            ann["function"] = descriptor(f)
        if procs:
            ann["processes"] = procs
        if locs:
            ann["locations"] = locs
        rd = roles.get(g["symbol"], spec.get("role_description"))
        if rd:
            ann["role_description"] = fold(rd)
        anns.append(ann)
    return anns


def build_node(spec: dict, res: Resolver, default_type: str, as_complex: bool) -> dict:
    node = {"id": spec["id"], "label": spec["label"]}
    node["module_type"] = spec.get("module_type", default_type)
    if spec.get("description"):
        node["description"] = fold(spec["description"])
    if spec.get("concepts"):
        node["concepts"] = [descriptor(c) for c in spec["concepts"]]
    elif spec.get("complex_term") and (spec.get("parts") or spec.get("variant_sets")):
        # A decomposed complex has no single annoton to carry its complex term.
        node["concepts"] = [descriptor(spec["complex_term"])]
    decomposed = bool(spec.get("parts") or spec.get("variant_sets")
                      or (spec.get("_root") and spec.get("subunit_parts", True)))
    if decomposed and spec.get("processes"):
        # Processes of a decomposed node have no annoton to sit on; keep them as
        # node concepts so they are not lost.
        have = {c["term"]["id"] for c in node.get("concepts", []) if c.get("term")}
        node.setdefault("concepts", []).extend(
            descriptor(p) for p in spec["processes"] if p["id"] not in have)
    complex_here = spec.get("complex", as_complex)
    if spec.get("parts"):
        node["parts"] = [build_part(p, i + 1, res, default_type, complex_here)
                         for i, p in enumerate(spec["parts"])]
    if spec.get("variant_sets"):
        node["variant_sets"] = [build_variant_set(v, res, default_type, complex_here)
                                for v in spec["variant_sets"]]
    if not spec.get("parts") and not spec.get("variant_sets"):
        if spec.get("_root") and spec.get("subunit_parts", True):
            # A complex with no curated decomposition: one part per subunit, so
            # the module exposes each subunit as a role-bearing part.
            node["parts"] = []
            for i, sym in enumerate(member_symbols(spec, res)):
                sub = {"id": f"{spec['id']}_{slug(sym)}", "label": sym, "genes": [sym],
                       "function": spec.get("unit_functions", {}).get(sym),
                       "role_description": spec.get("roles", {}).get(sym),
                       "locations": spec.get("locations", []), "annoton_label": "subunit"}
                node["parts"].append({"order": i + 1, "role": spec.get("roles", {}).get(sym, f"{sym} subunit")[:80],
                                      "node": build_node(dict(sub, module_type="MODULE"), res, default_type, False)})
        else:
            node["annotons"] = build_annotons(spec, res, complex_here)
    if spec.get("connections"):
        node["connections"] = [
            {k: (fold(v) if k == "description" else v) for k, v in c.items()}
            for c in spec["connections"]]
    if spec.get("notes"):
        node["notes"] = fold(spec["notes"])
    return node


def build_part(p: dict, order: int, res: Resolver, default_type: str, as_complex: bool) -> dict:
    part = {"order": order, "role": p.get("role", p["label"])}
    if p.get("optional") is not None:
        part["optional"] = p["optional"]
    part["node"] = build_node(p, res, default_type, as_complex)
    return part


def build_variant_set(v: dict, res: Resolver, default_type: str, as_complex: bool) -> dict:
    out = {"id": v["id"], "label": v["label"]}
    if v.get("axis"):
        out["axis"] = fold(v["axis"])
    # The schema has no description slot on a variant set; keep the text as notes.
    if v.get("description") or v.get("notes"):
        out["notes"] = fold(" ".join(x for x in (v.get("description"), v.get("notes")) if x))
    out["selection"] = v.get("selection", "ONE_OR_MORE")
    out["variants"] = []
    for var in v["variants"]:
        node = build_node(var, res, default_type, as_complex)
        out["variants"].append(node)
    return out


def load_triage() -> dict[str, dict]:
    doc = yaml.safe_load((HERE / "group_triage.yaml").read_text())
    by_module: dict[str, dict] = {}
    for r in doc["groups"]:
        if r.get("module"):
            by_module.setdefault(r["module"], {"realized": [], "subsumed": []})
            key = "realized" if r["decision"] == "NEW_MODULE" else "subsumed"
            by_module[r["module"]][key].append(r)
    return by_module


def regulator_sets(doc_groups: list[dict], realized: list[dict], res: Resolver) -> list[dict]:
    ids = {r["id"] for r in realized}
    out = []
    for r in doc_groups:
        if r["decision"] != "REGULATOR_SET":
            continue
        if any(p in ids for p in res.groups[r["id"]]["parents"]):
            out.append(r)
    return out


def generate(spec_path: Path, res: Resolver, triage: dict, triage_groups: list[dict],
             out_dir: Path) -> Path:
    spec = yaml.safe_load(spec_path.read_text())
    mod = spec["module"]
    if mod not in triage:
        raise ValueError(f"{mod}: not a module in group_triage.yaml")
    realized = triage[mod]["realized"]
    mtype = spec.get("module_type", "PROTEIN_COMPLEX")
    as_complex = spec.get("complex", mtype == "PROTEIN_COMPLEX")

    evidence = []
    for r in realized:
        evidence.append({
            "source_id": f"FB:{r['id']}",
            "title": f"FlyBase gene group {r['symbol']}: {r['name'].capitalize()}",
            "statement": fold(
                f"FlyBase release {spec.get('release', 'FB2026_03')} groups "
                f"{r['n_members']} D. melanogaster genes as {r['name'].lower()} "
                f"({r['symbol']}); this module models that group."),
        })
    for c in spec.get("concepts", []):
        evidence.append({"source_id": c["id"], "title": c["label"],
                         "statement": fold(c.get("evidence_statement")
                                           or f"GO term grounding the module as {c['label']}.")})
    for e in spec.get("evidence", []):
        evidence.append({k: (fold(v) if k in ("statement", "supporting_text") else v)
                         for k, v in e.items()})

    note_parts = [spec.get("notes", "")]
    covered = ", ".join(f"{r['symbol']} ({r['id']})" for r in realized)
    sub = ", ".join(f"{r['symbol']}" for r in triage[mod]["subsumed"])
    note_parts.append(f"FlyBase groups realized by this module: {covered}."
                      + (f" Subgroups folded into it: {sub}." if sub else ""))
    regs = regulator_sets(triage_groups, realized, res)
    if regs:
        note_parts.append(
            "FlyBase also curates regulator sets for this pathway, which are context and "
            "not modelled as parts: "
            + "; ".join(f"{r['symbol']} ({r['name'].lower()}, {r['n_members']} genes)" for r in regs)
            + ".")
    note_parts.append(
        "Participants were generated from the FlyBase gene-group membership and mapped to "
        "UniProtKB by projects/FLYBASE_GENE_GROUPS/generate_modules.py "
        f"from module_specs/{mod}.yaml. Genes without a UniProtKB entry (mostly non-coding "
        "RNAs) are grounded to their FlyBase gene ids. None of the member genes has a gene "
        "review yet unless noted.")

    root_spec = {k: v for k, v in spec.items()
                 if k in ("parts", "variant_sets", "connections", "concepts", "group", "groups",
                          "genes", "exclude", "function", "processes", "locations", "roles",
                          "unit_functions", "complex_term", "complex_label", "role_description",
                          "subunit_parts")}
    root_spec.update({"id": mod, "label": spec["label"], "module_type": mtype,
                      "description": spec.get("summary"), "_root": True})
    node = build_node(root_spec, res, "PROTEIN_COMPLEX" if as_complex else mtype, as_complex)
    node["module_type"] = mtype
    ctx = {"taxa": [TAXON]}
    if spec.get("cellular_components"):
        ctx["cellular_components"] = [descriptor(c) for c in spec["cellular_components"]]
    if spec.get("developmental_stages"):
        ctx["developmental_stages"] = [descriptor(c) for c in spec["developmental_stages"]]
    if spec.get("anatomical_locations"):
        ctx["anatomical_locations"] = [descriptor(c) for c in spec["anatomical_locations"]]
    ordered = {"id": node.pop("id"), "label": node.pop("label"), "module_type": node.pop("module_type")}
    if "description" in node:
        ordered["description"] = node.pop("description")
    if "concepts" in node:
        ordered["concepts"] = node.pop("concepts")
    ordered["context"] = ctx
    ordered.update(node)
    if spec.get("knowledge_gaps"):
        ordered["knowledge_gaps"] = [
            {k: (fold(v) if isinstance(v, str) and k != "gap_kind" else v) for k, v in g.items()}
            for g in spec["knowledge_gaps"]]

    doc = {
        "id": f"MODULE:{mod}",
        "title": spec["title"],
        "description": fold(spec["description"]),
        "status": "DRAFT",
        "scope": "CONCRETE",
        "evidence": evidence,
        "notes": fold(" ".join(p for p in note_parts if p)),
        "module": ordered,
    }
    out = out_dir / f"{mod}.yaml"
    out.write_text(yaml.dump(doc, sort_keys=False, width=88, allow_unicode=True))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("modules", nargs="*", help="module ids (default: every spec)")
    ap.add_argument("--specs", type=Path, default=HERE / "module_specs")
    ap.add_argument("--out", type=Path, default=Path("modules"))
    ap.add_argument("--uniprot", type=Path, default=Path(".cache/flybase/uniprot_dmel.tsv"))
    args = ap.parse_args()
    index = yaml.safe_load((HERE / "group_index.yaml").read_text())
    res = Resolver(index, args.uniprot)
    triage_doc = yaml.safe_load((HERE / "group_triage.yaml").read_text())
    triage = load_triage()
    paths = ([args.specs / f"{m}.yaml" for m in args.modules] if args.modules
             else sorted(args.specs.glob("*.yaml")))
    failed = 0
    for p in paths:
        try:
            out = generate(p, res, triage, triage_doc["groups"], args.out)
            print(f"wrote {out}")
        except Exception as exc:  # report every bad spec, then fail
            failed += 1
            print(f"ERROR {p.name}: {exc}", file=sys.stderr)
    if failed:
        raise SystemExit(f"{failed} spec(s) failed")


if __name__ == "__main__":
    main()
