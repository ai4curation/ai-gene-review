"""Inventory of what ai-gene-review holds for each causal gene in scope.

Usage, from the ai-gene-review root with a dismech checkout beside it:

    DISMECH_DIR=../dismech uv run python projects/DISMECH_VISION_ALIGNMENT/gene_state.py

Reads scope_decisions.yaml (which entries each gene is causal for), gene_identities.yaml
(HGNC id, UniProt accession and PANTHER family, from UniProt) and orthologs.yaml (PANTHER
orthologues), then looks at this repository only: the gene review, the PANTHER family
review, module membership, GO-CAM activities and reviewed orthologues. Writes
gene_state.yaml next to this script.

Module membership is read from the module structure (any UniProtKB identifier under the
`module:` key), so an accession mentioned only in a module's notes or evidence does not
count.
"""
import collections
import csv
import glob
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
ID_RE = re.compile(r"^id:\s*['\"]?([A-Za-z0-9_:\-.]+)", re.M)
STATUS_RE = re.compile(r"^status:\s*(\S+)", re.M)
FAMILY_STATUS_RE = re.compile(r"^review_status:\s*(\S+)", re.M)


def load(name):
    return yaml.load(open(os.path.join(HERE, name)), Loader=Loader)


def accessions(obj, out):
    """Every UniProtKB accession named as an identifier anywhere under a module body."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "id" and isinstance(v, str) and v.startswith("UniProtKB:"):
                out.add(v.split(":", 1)[1])
            else:
                accessions(v, out)
    elif isinstance(obj, list):
        for v in obj:
            accessions(v, out)
    return out


def main():
    decisions = load("scope_decisions.yaml")["decisions"]
    ident = load("gene_identities.yaml")["genes"]
    orth = load("orthologs.yaml")["orthologs"]
    entries = collections.defaultdict(list)
    for r in decisions:
        if r["decision"] != "EXCLUDED":
            for g in r["causal_genes"]:
                entries[g].append(r["entry"])
    # dismech labels can lag HGNC; match on the HGNC id carried in gene_identities.yaml
    by_hgnc_label = {}
    dm = os.environ.get("DISMECH_DIR", "../dismech")
    with open(os.path.join(dm, "cache/hgnc/terms.csv"), newline="") as fh:
        for row in csv.reader(fh):
            if len(row) >= 2:
                by_hgnc_label[row[1]] = row[0].lower()
    hgnc_to_symbol = {v["hgnc"]: k for k, v in ident.items()}

    other = {}
    for f in glob.glob("genes/*/*/*-ai-review.yaml"):
        org, gene = f.split("/")[1], f.split("/")[2]
        if org == "human":
            continue
        text = open(f).read()
        m = ID_RE.search(text[:3000])
        if m:
            s = STATUS_RE.search(text)
            other[m.group(1)] = (org, gene, s.group(1) if s else None)

    module_members = {}
    for f in sorted(glob.glob("modules/*.yaml")):
        d = yaml.load(open(f), Loader=Loader)
        if isinstance(d, dict) and isinstance(d.get("module"), dict):
            module_members[os.path.basename(f)[:-5]] = (accessions(d["module"], set()), d.get("status"))

    gocam, gocam_title = collections.defaultdict(set), {}
    with open("gocams/index.tsv") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            gocam[r["gene_product"]].add(r["model_id"])
            gocam_title[r["model_id"]] = r["model_title"]

    state = {}
    for dismech_label, slugs in sorted(entries.items()):
        symbol = hgnc_to_symbol.get(by_hgnc_label.get(dismech_label), dismech_label)
        info = ident.get(symbol) or {}
        acc, fam = info.get("uniprot"), info.get("panther_family")
        rec = dict(hgnc=info.get("hgnc"), uniprot=acc, entries=sorted(slugs))
        if symbol != dismech_label:
            rec["dismech_label"] = dismech_label
        review = f"genes/human/{symbol}/{symbol}-ai-review.yaml"
        if os.path.exists(review):
            d = yaml.load(open(review), Loader=Loader)
            ann = d.get("existing_annotations") or []
            actions = collections.Counter((a.get("review") or {}).get("action", "NONE") for a in ann)
            core = []
            for cf in d.get("core_functions") or []:
                for key in ("molecular_function", "contributes_to_molecular_function"):
                    t = cf.get(key)
                    if isinstance(t, dict) and t.get("id"):
                        core.append(dict(relation=key, id=t["id"], label=t.get("label")))
                if cf.get("proposed_molecular_function"):
                    core.append(dict(relation="proposed_molecular_function", label=cf["proposed_molecular_function"]))
            rec["review"] = dict(status=d.get("status"), annotations=len(ann), actions=dict(sorted(actions.items())),
                                 core_molecular_functions=core,
                                 deep_research=sorted(re.sub(r".*-deep-research-(.*)\.md", r"\1", x)
                                                      for x in glob.glob(f"genes/human/{symbol}/*-deep-research-*.md")))
        else:
            rec["review"] = None
        if fam:
            fdir = f"interpro/panther/{fam}"
            frev = f"{fdir}/{fam}-review.yaml"
            fstat = None
            if os.path.exists(frev):
                m = FAMILY_STATUS_RE.search(open(frev).read())
                fstat = m.group(1) if m else "PRESENT"
            rec["family"] = dict(id=fam, subfamily=info.get("panther_subfamily"), cached=os.path.isdir(fdir),
                                 paint_slice=os.path.exists(f"{fdir}/{fam}-paint.tsv"), review=fstat)
        else:
            rec["family"] = None
        rec["modules"] = [dict(module=m, status=st) for m, (accs, st) in module_members.items() if acc and acc in accs]
        rec["gocams"] = [dict(model=m, title=gocam_title[m], reviewed=os.path.exists(f"gocams/{m}/{m}-review.yaml"))
                         for m in sorted(gocam.get(f"UniProtKB:{acc}", ()))] if acc else []
        rec["reviewed_orthologs"] = [dict(organism=other[o["uniprot"]][0], gene=other[o["uniprot"]][1],
                                          status=other[o["uniprot"]][2], type=o["type"])
                                     for o in orth.get(symbol, []) if o["uniprot"] in other]
        state[symbol] = rec

    def n(pred):
        return sum(1 for r in state.values() if pred(r))
    summary = dict(
        genes=len(state),
        review_status=dict(collections.Counter((r["review"] or {}).get("status") or "NONE" for r in state.values()).most_common()),
        distinct_families=len({r["family"]["id"] for r in state.values() if r["family"]}),
        genes_with_family_review=n(lambda r: r["family"] and r["family"]["review"]),
        genes_in_a_module=n(lambda r: r["modules"]),
        genes_in_a_gocam=n(lambda r: r["gocams"]),
        gocam_models=len({g["model"] for r in state.values() for g in r["gocams"]}),
        gocam_models_reviewed=len({g["model"] for r in state.values() for g in r["gocams"] if g["reviewed"]}),
        genes_with_a_reviewed_ortholog=n(lambda r: r["reviewed_orthologs"]),
    )
    with open(os.path.join(HERE, "gene_state.yaml"), "w") as fh:
        yaml.safe_dump(dict(summary=summary, genes=state), fh, sort_keys=False, width=120)
    print(summary)


if __name__ == "__main__":
    main()
