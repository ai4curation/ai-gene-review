"""Fill the generated tables of projects/DISMECH_VISION_ALIGNMENT.md.

Usage, from the ai-gene-review root:

    uv run python projects/DISMECH_VISION_ALIGNMENT/make_page.py

Reads scope_decisions.yaml, gene_state.yaml and report.yaml (the audit report written by
projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py over scope.yaml) and rewrites the text
between the `<!-- BEGIN GENERATED: name -->` and `<!-- END GENERATED: name -->` markers of
the page. Everything outside the markers is written by hand and left alone. A marker that
is missing from the page is an error, so a table cannot silently stop being updated.
"""
import collections
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(os.path.dirname(HERE), "DISMECH_VISION_ALIGNMENT.md")
Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
DISMECH_FLAGS = ("UNTYPED", "NO_ORIGIN", "GENE_ON_NO_NODE", "NO_GO_ON_GENE_NODES")
PRINCIPAL = ("CAUSATIVE", None)


def load(name):
    return yaml.load(open(os.path.join(HERE, name)), Loader=Loader)


def scope_block(dec):
    d = dec["decisions"]
    inc = [r for r in d if r["decision"] != "EXCLUDED"]
    c = collections.Counter(r["decision"] for r in d)
    genes = {g for r in inc for g in r["causal_genes"]}
    out = [f"{len(inc)} entries are in scope ({c['NONSYNDROMIC']} non-syndromic, {c['MIXED']} mixed), "
           f"with {len(genes)} distinct causal genes; {c['EXCLUDED']} candidates under the MONDO visual-system "
           f"branch were excluded. MONDO {dec['inputs']['mondo_version']}, HPO {dec['inputs']['hp_version']}.", ""]
    out += ["Entries kept or dropped by a hand decision rather than by the phenotype-share rule:", "",
            "| Entry | Decision | Eye / all phenotypes | Reason |", "|---|---|---|---|"]
    for r in d:
        mechanical = (r["reason"].startswith("eye-restricted by phenotype share") and ";" not in r["reason"]) or \
            r["reason"].startswith(("extra-ocular features", "MONDO classes", "no germline", "no HPO-bound"))
        if not mechanical:
            out.append(f"| {r['entry']} | {r['decision']} | {r['eye_phenotypes']}/{r['phenotypes']} | {r['reason']} |")
    return "\n".join(out)


def gene_block(state):
    s = state["summary"]
    rs = s["review_status"]
    out = [f"{s['genes']} genes. Gene reviews: "
           + ", ".join(f"{v} {k}" for k, v in rs.items()) + ". "
           f"{s['distinct_families']} PANTHER families, of which the families of {s['genes_with_family_review']} genes have a "
           f"family review. {s['genes_in_a_module']} genes are a part of at least one module. {s['genes_in_a_gocam']} genes "
           f"appear in {s['gocam_models']} GO-CAM models, {s['gocam_models_reviewed']} of them reviewed here. "
           f"{s['genes_with_a_reviewed_ortholog']} genes have at least one reviewed orthologue.", "",
           "| Gene | Entries | Review | Core molecular function | Family (review) | Modules | GO-CAMs reviewed / all | Reviewed orthologues |",
           "|---|---|---|---|---|---|---|---|"]
    for sym, r in state["genes"].items():
        rev = r["review"]
        status = rev["status"] if rev else "-"
        core = "; ".join(dict.fromkeys(
            (f"{c['id']} {c['label']}" if c.get("id") else f"proposed: {c['label']}")
            + (" (contributes)" if c["relation"].startswith("contributes") else "")
            for c in (rev or {}).get("core_molecular_functions", []))) or "-"
        fam = r["family"]
        famtxt = f"{fam['id']} ({fam['review'] or 'none'})" if fam else "-"
        mods = ", ".join(m["module"] for m in r["modules"]) or "-"
        gc = f"{sum(1 for g in r['gocams'] if g['reviewed'])} / {len(r['gocams'])}" if r["gocams"] else "-"
        orth = ", ".join(f"{o['organism']} {o['gene']} ({o['status']})" for o in r["reviewed_orthologs"]) or "-"
        out.append(f"| {sym} | {len(r['entries'])} | {status} | {core} | {famtxt} | {mods} | {gc} | {orth} |")
    return "\n".join(out)


def audit_block(rep):
    p = rep["provenance"]
    rows = [(e["entry"], g) for e in rep["entries"] for g in e.get("genes", [])]
    principal = [(e, g) for e, g in rows if g.get("relationship") in PRINCIPAL]
    flags = collections.Counter(f for _, g in principal for f in g["flags"])
    out = [f"Audit run {p['run_date']} over dismech `{str(p['dismech_revision'])[:9]}` and ai-gene-review "
           f"`{str(p['aigr_revision'])[:9]}` (GO adapter `{p['go_adapter']}`"
           + (", ai-gene-review tree had uncommitted changes" if p.get("aigr_dirty") else "") + "). "
           f"{len(rep['entries'])} entries, {len(rows)} gene rows, {len(principal)} of them causal or untyped.", "",
           "Flag counts on causal and untyped rows: "
           + ", ".join(f"`{k}` {v}" for k, v in sorted(flags.items(), key=lambda kv: -kv[1])) + ".", "",
           "| Entry | Gene | Relationship | Nodes | Review | Aligned node terms (node->core) | Unaligned node terms | Flags |",
           "|---|---|---|---|---|---|---|---|"]
    for entry, g in rows:
        pairs = g.get("aligned_pairs") or {}
        al = " ".join(t if (v == t or v == [t]) else f"{t}->{'/'.join(v) if isinstance(v, list) else v}"
                      for t, v in pairs.items()) or "-"
        un = " ".join(g.get("dismech_only") or []) or "-"
        out.append(f"| {entry} | {g['gene']} | {g.get('relationship') or 'untyped'} | {g.get('nodes', 0)} | "
                   f"{g.get('aigr_status') or '-'} | {al} | {un} | {', '.join(g['flags']) or 'ok'} |")
    return "\n".join(out)


def main():
    blocks = {"scope": scope_block(load("scope_decisions.yaml")), "genes": gene_block(load("gene_state.yaml"))}
    if os.path.exists(os.path.join(HERE, "report.yaml")):
        blocks["audit"] = audit_block(load("report.yaml"))
    text = open(PAGE).read()
    # frontmatter gene list: the in-scope genes that have a review folder here
    reviewed = sorted(g for g, r in load("gene_state.yaml")["genes"].items() if r["review"])
    text, n = re.subn(r"(?m)^genes: \[.*\]$", "genes: [" + ", ".join(reviewed) + "]", text, count=1)
    if n != 1:
        sys.exit("frontmatter 'genes: [...]' line not found")
    for name, body in blocks.items():
        pat = re.compile(rf"(<!-- BEGIN GENERATED: {name} -->\n)(?:.*?\n)?(<!-- END GENERATED: {name} -->)", re.S)
        if not pat.search(text):
            sys.exit(f"marker for generated block '{name}' is missing from {PAGE}")
        text = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)
    open(PAGE, "w").write(text)
    print("filled:", ", ".join(blocks))


if __name__ == "__main__":
    main()
