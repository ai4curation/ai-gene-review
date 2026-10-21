#!/usr/bin/env python3
"""Test simple rules that might flag bad TreeGrafter propagations in advance.

Every reviewed TreeGrafter (GO_REF:0000118) annotation in
``treegrafter_review.tsv`` already carries a reviewer action. This script
asks: are there cheap, mechanical signals, computable without reading
the literature, that pick out the annotations reviewers went on to
down-grade? Each rule is scored as a classifier against the review
actions: how many rows it flags, the down-grade rate among them, and
the lift over the base rate.

"Down-graded" means REMOVE, MODIFY, MARK_AS_OVER_ANNOTATED or TOO_GENERAL (as elsewhere on
the project page). UNDECIDED rows are excluded from the rates.

Rules (all computed from files already in the repo, plus GO itself):

  generic_cc          CC term is one of the five broad compartments
                      (cytoplasm, cytosol, membrane, plasma membrane, nucleus).
  ancestor_of_other   the TreeGrafter term is a strict is_a/part_of ancestor of
                      another GO term annotated to the same protein in GOA, so
                      a more specific statement already exists.
  inactive_subfamily  MF term on a protein whose PANTHER family or subfamily
                      name says INACTIVE / PSEUDO / NON-CATALYTIC.
  no_name_overlap     catalytic MF term ("... activity", not binding) that
                      shares no content word with the PANTHER family or
                      subfamily name -- a crude sign the node term describes a
                      different enzyme than the subfamily the protein sits in.
  metazoan_term_off_metazoa
                      BP/CC term whose label names an animal tissue, organ or
                      cell type, on a protein from outside Metazoa.
  eukaryotic_cc_on_prokaryote
                      CC term for a eukaryote-only structure on a bacterial or
                      archaeal protein.
  ec_contradiction    MF term whose GO EC cross-reference contradicts every EC
                      number on the protein's UniProt record (DE EC=): the two
                      differ at an EC level both of them specify. A coarser GO
                      term (oxidoreductase, 1.-.-.-) is compatible, not a
                      contradiction. ec_match (the full EC agrees) is the
                      negative control.
  uncorroborated      no other GOA row (any source but TreeGrafter) asserts the
                      same term or a descendant of it.
  sibling_of_other    catalytic MF term (not binding) that shares a direct parent with another MF term
                      on the protein from a non-TreeGrafter source, without
                      either subsuming the other (e.g. phosphotransferase to a
                      phosphate group vs to another group).
  same_species_paralogs
                      the protein's species has two or more reviewed proteins in
                      the same PANTHER family (paralogs, where the subfamily
                      split carries the specificity).

Outputs (next to this script, or under --out-dir):
  propagation_rules.tsv          one row per rule: n flagged, rates, lift
  propagation_rule_hits.tsv      one row per (rule, annotation) hit, for spot
                                 checks

Run:
  python3 projects/TREEGRAFTER/propagation_rules.py --go-obo go-basic.obo

``--go-obo`` is required for ``ancestor_of_other`` (download
http://purl.obolibrary.org/obo/go/go-basic.obo); without it that rule is
skipped.
"""
from __future__ import annotations

import argparse
import csv
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TREEGRAFTER_REF = "GO_REF:0000118"
# TOO_GENERAL (true but entailed by a more specific term in the same review)
# counts as down-graded, like MODIFY: the review did not keep the term as is.
DOWNGRADE = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY", "TOO_GENERAL"}

GENERIC_CC = {
    "GO:0005737": "cytoplasm",
    "GO:0005829": "cytosol",
    "GO:0016020": "membrane",
    "GO:0005886": "plasma membrane",
    "GO:0005634": "nucleus",
}
# Eukaryote-only structures, matched on the CC label.
EUK_CC = re.compile(
    r"\b(nucle(us|olus|ar)|mitochondri|endoplasmic reticulum|golgi|lysosom|"
    r"vacuol|peroxisom|endosom|centrosom|cilium|ciliary|chromatin|"
    r"spliceosom|kinetochore|microtubule organizing|actin cortex)",
    re.I,
)
# Animal tissue / organ / cell-type vocabulary, matched on BP/CC labels.
METAZOAN = re.compile(
    r"\b(organs?\b|organ growth|tissue|embryo|neur|synap|axon|dendrit|muscle|heart|cardiac|"
    r"limb|kidney|brain|gland|epiderm|angiogenesis|vascul|blood|leukocyte|"
    r"lymphocyte|T cell|B cell|macrophage|osteo|cartilage|hair|eye|retina|"
    r"spermat|oocyte|gastrulation|somite|neural crest|wing)",
    re.I,
)
ASPECT = {"molecular_function": "MF", "biological_process": "BP",
          "cellular_component": "CC"}
INACTIVE = re.compile(r"INACTIVE|PSEUDO|NON-?CATALYTIC|CATALYTICALLY", re.I)
STOP = {
    "activity", "process", "protein", "proteins", "the", "and", "with", "from",
    "into", "via", "type", "family", "subfamily", "related", "member", "domain",
    "containing", "like", "putative", "probable", "uncharacterized", "acting",
    "group", "groups", "donors", "acceptor", "acceptors", "other", "than",
    "using", "dependent", "subunit", "chain", "mitochondrial", "chloroplastic",
}

PANTHER_FAM = re.compile(r"PANTHER;\s*(PTHR\d+);\s*([^;]+?)\s*;?\s*\d*\.?$")
PANTHER_SF = re.compile(r"PANTHER;\s*(PTHR\d+:SF\d+);\s*([^;]+?)\s*;?\s*\d*\.?$")


def _first(gene_dir: str, suffix: str) -> str:
    try:
        for name in sorted(os.listdir(gene_dir)):
            if name.endswith(suffix):
                return os.path.join(gene_dir, name)
    except FileNotFoundError:
        pass
    return ""


def uniprot_info(gene_dir: str) -> dict:
    """Lineage (OC) and PANTHER family/subfamily from the UniProt record."""
    info = {"lineage": "", "fam": "", "fam_name": "", "sf": "", "sf_name": "",
            "ec": set()}
    up = _first(gene_dir, "-uniprot.txt")
    if not up:
        return info
    oc = []
    with open(up) as fh:
        for line in fh:
            if line.startswith("OC   "):
                oc.append(line[5:].strip())
            elif line.startswith("DE   "):
                info["ec"].update(re.findall(r"EC=([0-9]+\.[0-9n.\-]+)", line))
            elif "PANTHER;" in line:
                m = PANTHER_SF.search(line)
                if m:
                    info["sf"], info["sf_name"] = m.group(1), m.group(2).strip()
                    continue
                m = PANTHER_FAM.search(line)
                if m and not info["fam"]:
                    info["fam"], info["fam_name"] = m.group(1), m.group(2).strip()
    info["lineage"] = " ".join(oc)
    return info


def goa_terms(gene_dir: str) -> tuple[set, dict, dict]:
    """GOA (non-NOT) GO ids, TreeGrafter graft nodes, and per-term aspect of
    the rows from any other source."""
    goa = _first(gene_dir, "-goa.tsv")
    terms, nodes, other = set(), {}, {}
    if not goa:
        return terms, nodes, other
    with open(goa) as fh:
        for line in fh:
            c = line.rstrip("\n").split("\t")
            if len(c) < 11 or not c[4].startswith("GO:"):
                continue
            if "NOT" in c[3]:
                continue
            terms.add(c[4])
            if c[9] != TREEGRAFTER_REF:
                other[c[4]] = c[6]
            if c[9] == TREEGRAFTER_REF:
                m = re.search(r"(PTN\d+)", c[10])
                if m:
                    nodes[c[4]] = m.group(1)
    return terms, nodes, other


def load_go(path: str) -> tuple[dict, dict]:
    """child -> set(parents) over is_a and part_of; term -> EC xrefs."""
    parents = defaultdict(set)
    ec = defaultdict(set)
    cur = None
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line == "[Term]":
                cur = None
            elif line.startswith("id: GO:"):
                cur = line[4:]
            elif cur and line.startswith("is_a: "):
                parents[cur].add(line[6:16])
            elif cur and line.startswith("xref: EC:"):
                ec[cur].add(line[9:].split()[0])
            elif cur and line.startswith("relationship: part_of "):
                parents[cur].add(line[22:32])
            elif line.startswith("[Typedef]"):
                cur = None
    return parents, ec


def ec_agree(a: str, b: str, levels: int) -> bool:
    pa, pb = a.split("."), b.split(".")
    for i in range(levels):
        if i >= len(pa) or i >= len(pb):
            return False
        if "-" in (pa[i], pb[i]) or pa[i] != pb[i]:
            return False
    return True


def ec_conflict(a: str, b: str) -> bool:
    """True when two EC numbers differ at a level both of them specify.

    A partial number (``1.1.1.-``) or a preliminary one (``n2``) is compatible
    with anything below it, so it can only conflict at a level above.
    """
    for x, y in zip(a.split("."), b.split(".")):
        if x == "-" or y == "-" or x.startswith("n") or y.startswith("n"):
            return False
        if x != y:
            return True
    return False


def ancestors(term: str, parents: dict, cache: dict) -> set:
    if term in cache:
        return cache[term]
    out, stack = set(), list(parents.get(term, ()))
    while stack:
        t = stack.pop()
        if t in out:
            continue
        out.add(t)
        stack.extend(parents.get(t, ()))
    cache[term] = out
    return out


def words(text: str) -> set:
    toks = re.split(r"[^a-z0-9]+", text.lower())
    # crude stem: first 5 letters of each content word
    return {t[:5] for t in toks if len(t) >= 4 and t not in STOP}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--review-tsv", default=os.path.join(HERE, "treegrafter_review.tsv"))
    ap.add_argument("--go-obo", default="")
    ap.add_argument("--out-dir", default=HERE)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.review_tsv), delimiter="\t"))
    rows = [r for r in rows if r.get("negated", "").lower() not in ("true", "1")]

    parents, go_ec = load_go(args.go_obo) if args.go_obo else (None, {})
    anc_cache: dict = {}

    gene_cache: dict = {}
    for r in rows:
        f = r["file"]
        if f not in gene_cache:
            gdir = os.path.dirname(os.path.join(ROOT, f))
            info = uniprot_info(gdir)
            info["terms"], info["nodes"], info["other"] = goa_terms(gdir)
            info["species"] = f.split("/")[1]
            gene_cache[f] = info

    # same-species paralogs: >=2 review files per (species, PANTHER family)
    fam_files = defaultdict(set)
    for f, info in gene_cache.items():
        if info["fam"]:
            fam_files[(info["species"], info["fam"])].add(f)

    def rule_hits(r: dict) -> list[tuple[str, str]]:
        info = gene_cache[r["file"]]
        tid, label = r["term_id"], r["term_label"]
        aspect = ASPECT.get(r["aspect"], r["aspect"])
        lineage = info["lineage"]
        hits = []
        if aspect == "CC" and tid in GENERIC_CC:
            hits.append(("generic_cc", label))
        if parents is not None:
            more = [
                t for t in info["terms"]
                if t != tid and tid in ancestors(t, parents, anc_cache)
            ]
            if more:
                hits.append(("ancestor_of_other", ";".join(sorted(more))[:200]))
        names = f"{info['fam_name']} {info['sf_name']}"
        if aspect == "MF" and INACTIVE.search(names):
            hits.append(("inactive_subfamily", names.strip()))
        if (aspect == "MF" and label.endswith("activity")
                and "binding" not in label and names.strip()
                and not (words(label) & words(names))):
            hits.append(("no_name_overlap", names.strip()))
        if aspect in ("BP", "CC") and lineage and "Metazoa" not in lineage \
                and METAZOAN.search(label):
            hits.append(("metazoan_term_off_metazoa", lineage.split(";")[0]))
        if aspect == "CC" and lineage.startswith(("Bacteria", "Archaea")) \
                and EUK_CC.search(label):
            hits.append(("eukaryotic_cc_on_prokaryote", lineage.split(";")[0]))
        if aspect == "MF" and go_ec.get(tid) and info["ec"]:
            t_ec, p_ec = go_ec[tid], info["ec"]
            detail = f"GO {','.join(sorted(t_ec))} vs UniProt {','.join(sorted(p_ec))}"
            # GO's is_a can cross EC branches (GO:0008834, EC 2.5.1.31, is_a
            # GO:0045547, EC 2.5.1.87): a term that subsumes another GOA term
            # whose EC does match the protein is compatible, not contradicted.
            subsumes_match = parents is not None and any(
                tid in ancestors(t, parents, anc_cache)
                and any(ec_agree(x, y, 4) for x in go_ec.get(t, ()) for y in p_ec)
                for t in info["other"]
            )
            if not subsumes_match and all(
                    ec_conflict(a, b) for a in t_ec for b in p_ec):
                hits.append(("ec_contradiction", detail))
            elif any(ec_agree(a, b, 4) for a in t_ec for b in p_ec):
                hits.append(("ec_match", detail))
        if parents is not None:
            support = [
                t for t in info["other"]
                if t == tid or tid in ancestors(t, parents, anc_cache)
            ]
            if not support:
                hits.append(("uncorroborated", ""))
            if aspect == "MF" and "binding" not in label:
                tp = parents.get(tid, set())
                sibs = [
                    t for t, a in info["other"].items()
                    if a == "molecular_function" and t != tid
                    and parents.get(t, set()) & tp
                    and tid not in ancestors(t, parents, anc_cache)
                    and t not in ancestors(tid, parents, anc_cache)
                ]
                if sibs:
                    hits.append(("sibling_of_other", ";".join(sorted(sibs))))
        if info["fam"] and len(fam_files[(info["species"], info["fam"])]) >= 2:
            n = len(fam_files[(info["species"], info["fam"])])
            hits.append(("same_species_paralogs", f"{info['fam']} x{n}"))
        return hits

    scored = [r for r in rows if r["action"] != "UNDECIDED"]
    base_n = len(scored)
    base_dg = sum(r["action"] in DOWNGRADE for r in scored)
    base_rate = base_dg / base_n if base_n else 0.0

    per_rule = defaultdict(list)
    hit_rows = []
    for r in rows:
        for rule, detail in rule_hits(r):
            info = gene_cache[r["file"]]
            hit_rows.append({
                "rule": rule, "gene": r["gene"], "species": info["species"],
                "term_id": r["term_id"], "term_label": r["term_label"],
                "aspect": r["aspect"], "action": r["action"],
                "graft_node": info["nodes"].get(r["term_id"], ""),
                "panther_family": info["fam"], "panther_subfamily": info["sf"],
                "subfamily_name": info["sf_name"], "detail": detail,
                "file": r["file"],
            })
            if r["action"] != "UNDECIDED":
                per_rule[rule].append(r)

    os.makedirs(args.out_dir, exist_ok=True)
    out = os.path.join(args.out_dir, "propagation_rules.tsv")
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["rule", "flagged", "downgraded", "downgrade_rate",
                     "base_rate", "lift", "recall_of_downgrades",
                     "removed", "accepted"])
        w.writerow(["(all reviewed TreeGrafter rows)", base_n, base_dg,
                    f"{base_rate:.3f}", f"{base_rate:.3f}", "1.00", "1.000",
                    sum(r["action"] == "REMOVE" for r in scored),
                    sum(r["action"] == "ACCEPT" for r in scored)])
        for rule in sorted(per_rule, key=lambda k: -len(per_rule[k])):
            rs = per_rule[rule]
            dg = sum(r["action"] in DOWNGRADE for r in rs)
            rate = dg / len(rs)
            w.writerow([rule, len(rs), dg, f"{rate:.3f}", f"{base_rate:.3f}",
                        f"{rate / base_rate:.2f}" if base_rate else "",
                        f"{dg / base_dg:.3f}" if base_dg else "",
                        sum(r["action"] == "REMOVE" for r in rs),
                        sum(r["action"] == "ACCEPT" for r in rs)])
    out_hits = os.path.join(args.out_dir, "propagation_rule_hits.tsv")
    with open(out_hits, "w", newline="") as fh:
        cols = list(hit_rows[0]) if hit_rows else ["rule"]
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for h in sorted(hit_rows, key=lambda h: (h["rule"], h["species"], h["gene"], h["term_id"])):
            w.writerow(h)
    print(f"wrote {out} and {out_hits}")
    print(open(out).read())


if __name__ == "__main__":
    main()
