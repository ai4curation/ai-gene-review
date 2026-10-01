#!/usr/bin/env python3
"""Assemble a per-organism metabolic network from reviewed MF annotations and
test how well its topology agrees with reviewed BP annotations.

Pipeline
  1. For every gene review in genes/<ORG>/, collect the *reviewed* MF and BP terms:
       - core_functions[].molecular_function / directly_involved_in
       - existing_annotations[] whose review.action is ACCEPT or KEEP_AS_NON_CORE
       - proposed_replacement_terms of MODIFY actions, and NEW annotations
  2. Map each MF to Rhea reactions with the GO column of the Rhea TSV (= rhea2go,
     exact mapping only; a general MF such as "oxidoreductase activity" is NOT
     expanded to its descendants' reactions).
  3. Reaction -> ChEBI participants; currency metabolites (H2O, ATP, NAD(P)H ...)
     are removed so that edges reflect pathway intermediates rather than cofactors.
  4. Gene-gene edge  <=>  the two genes' reactions share a non-currency metabolite.
  5. Compare with BP (propagated over is_a/part_of, restricted to metabolic process):
       a. edge-level: do metabolically linked genes share a specific BP more than
          random gene pairs?
       b. term-level: is the gene set of each BP term connected in the network,
          compared with random gene sets of the same size?
       c. community-level: Louvain communities vs best-matching BP term.

Inputs are downloaded into data/ (see README.md); nothing is hard-coded.
Outputs go to results/<ORG>/.
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx
import yaml

try:
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
DATA = HERE / "data"

KEEP_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}
METABOLIC_PROCESS = "GO:0008152"

# Currency / cofactor metabolites, matched against Rhea participant *names*
# (resolved to ChEBI ids from the Rhea equations, so no ChEBI id is hand-typed).
CURRENCY_NAMES = {
    "H2O", "H(+)", "O2", "CO2", "hydrogencarbonate", "NH4(+)", "phosphate", "diphosphate",
    "ATP", "ADP", "AMP", "GTP", "GDP", "GMP", "CTP", "CDP", "CMP", "UTP", "UDP", "UMP",
    "ITP", "IDP", "dATP", "dADP",
    "NAD(+)", "NADH", "NADP(+)", "NADPH", "FAD", "FADH2", "FMN", "FMNH2",
    "CoA", "H2O2", "S-adenosyl-L-methionine", "S-adenosyl-L-homocysteine",
    "an oxidized [electron-transfer flavoprotein]", "a reduced [electron-transfer flavoprotein]",
    "AH2", "A", "a ubiquinone", "a ubiquinol", "a quinone", "a quinol", "a menaquinone",
    "a menaquinol", "Fe(III)-[cytochrome c]", "Fe(II)-[cytochrome c]",
    "oxidized [thioredoxin]", "reduced [thioredoxin]",
    "L-glutathione", "glutathione disulfide",
    "Na(+)", "K(+)", "Mg(2+)", "Ca(2+)", "Zn(2+)", "Fe(2+)", "Fe(3+)", "Cu(+)", "Cu(2+)",
    "Mn(2+)", "chloride", "hydrogen sulfide", "sulfite", "sulfate", "superoxide",
    "[thioredoxin]-dithiol", "[thioredoxin]-disulfide",
    "reduced 2[4Fe-4S]-[ferredoxin]", "oxidized 2[4Fe-4S]-[ferredoxin]",
    "2 reduced [2Fe-2S]-[ferredoxin]", "2 oxidized [2Fe-2S]-[ferredoxin]",
    "reduced [2Fe-2S]-[ferredoxin]", "oxidized [2Fe-2S]-[ferredoxin]",
    "an [apo-acyl-carrier-protein]",
    "L-glutamate", "2-oxoglutarate",  # amino-group shuttle; huge hubs in transaminations
    "L-glutamine",
}


# Electron-carrier pools (quinones of any prenyl length, cytochromes, flavodoxins,
# NADPH--hemoprotein reductase) are also treated as currency.
CURRENCY_PATTERNS = re.compile(
    r"(ubiquinon|ubiquinol|menaquinon|menaquinol|plastoquinon|plastoquinol|cytochrome|"
    r"flavodoxin|ferredoxin|hemoprotein reductase|electron-transfer flavoprotein)", re.I)
# Macromolecular residues ("L-seryl-[protein]", "a 5'-end ... in mRNA", "tRNA(Leu)") link
# kinases, methyltransferases, aaRSs etc. through polymers, not through small-molecule
# metabolism; they are excluded from the metabolite layer. Acyl-carrier-protein
# intermediates ("-[ACP]") are kept: they are genuine pathway intermediates.
MACROMOLECULE_PATTERNS = re.compile(
    r"(\[(protein|histone|collagen|[^\]]*protein\]|DNA|RNA|mRNA|tRNA|rRNA)|"
    r"\bin (DNA|RNA|mRNA|tRNA|rRNA|.*RNA)\b|^tRNA|^a tRNA|^an? \w*-?tRNA|-tRNA|tRNA\(|"
    r"\bDNA\b|\bRNA\b|^\[protein\]|-\[protein|ribonucleic|\(deoxyribonucleotide\))")
# One GO MF can map to dozens of Rhea reactions (a class reaction plus substrate
# examples). Above this many, only the class reactions (with "a"/"an" generic
# participants) are kept, so a broad hydrolase does not connect to every acyl-CoA.
MAX_SPECIFIC_RHEA_PER_GO = 5


# ---------------------------------------------------------------- GO ontology
def load_go(path: Path):
    names, ns, parents, obsolete = {}, {}, defaultdict(set), set()
    cur = None
    for line in path.open():
        line = line.rstrip("\n")
        if line == "[Term]":
            cur = {}
        elif line.startswith("[") and line.endswith("]"):
            cur = None
        elif cur is not None and line.startswith("id: "):
            cur["id"] = line[4:]
        elif cur is not None and "id" in cur:
            tid = cur["id"]
            if line.startswith("name: "):
                names[tid] = line[6:]
            elif line.startswith("namespace: "):
                ns[tid] = line[11:]
            elif line.startswith("is_a: "):
                parents[tid].add(line[6:].split(" ")[0])
            elif line.startswith("relationship: part_of "):
                parents[tid].add(line.split(" ")[2])
            elif line.startswith("is_obsolete: true"):
                obsolete.add(tid)
            elif line.startswith("alt_id: "):
                names.setdefault("ALT:" + line[8:], tid)
    alt = {k[4:]: v for k, v in names.items() if k.startswith("ALT:")}
    return names, ns, parents, obsolete, alt


def ancestors_fn(parents):
    cache = {}

    def anc(t):
        if t in cache:
            return cache[t]
        out = {t}
        for p in parents.get(t, ()):
            out |= anc(p)
        cache[t] = out
        return out

    return anc


# ---------------------------------------------------------------- Rhea
def split_participants(side: str):
    return [re.sub(r"^\d+ ", "", t.strip()) for t in side.split(" + ")]


def load_rhea(path: Path):
    """Return go2rhea, rhea2chebi, chebi2name, rhea2eq, rhea2sides."""
    go2rhea = defaultdict(set)
    rhea2chebi, rhea2eq, rhea2sides, chebi_names = {}, {}, {}, defaultdict(Counter)
    for r in csv.DictReader(path.open(), delimiter="\t"):
        rid = r["Reaction identifier"]
        eq = r["Equation"]
        chebis = [c for c in r["ChEBI identifier"].split(";") if c]
        rhea2chebi[rid] = set(chebis)
        rhea2eq[rid] = eq
        sides = [split_participants(s) for s in eq.split(" = ")]
        names = [n for s in sides for n in s]
        if len(names) == len(chebis):
            for n, c in zip(names, chebis):
                chebi_names[c][n] += 1
            k = len(sides[0])
            rhea2sides[rid] = (set(chebis[:k]), set(chebis[k:]))
        for m in re.finditer(r"(GO:\d{7})", r["Gene Ontology"] or ""):
            go2rhea[m.group(1)].add(rid)
    chebi2name = {c: cnt.most_common(1)[0][0] for c, cnt in chebi_names.items()}
    n_trimmed = 0
    for go, rxns in go2rhea.items():
        if len(rxns) > MAX_SPECIFIC_RHEA_PER_GO:
            generic = {r for r in rxns if re.search(r"(^|= |\+ )an? ", rhea2eq[r])}
            if generic:
                go2rhea[go] = generic
                n_trimmed += 1
    print(f"GO terms trimmed to generic Rhea reactions: {n_trimmed}")
    return go2rhea, rhea2chebi, chebi2name, rhea2eq, rhea2sides


# ---------------------------------------------------------------- reviews
def term_ids(obj):
    if isinstance(obj, dict) and obj.get("id"):
        return [obj["id"]]
    if isinstance(obj, list):
        return [t for o in obj for t in term_ids(o)]
    return []


def load_reviews(org: str):
    genes = {}
    for f in sorted((ROOT / "genes" / org).glob("*/*-ai-review.yaml")):
        try:
            doc = yaml.load(f.open(), Loader=Loader)
        except Exception as e:  # noqa: BLE001
            print(f"WARN cannot parse {f}: {e}")
            continue
        if not isinstance(doc, dict):
            continue
        sym = doc.get("gene_symbol") or f.parent.name
        acc = doc.get("id") or sym
        mf_core, terms = set(), set()
        for cf in doc.get("core_functions") or []:
            mf_core |= set(term_ids(cf.get("molecular_function")))
            mf_core |= set(term_ids(cf.get("contributes_to_molecular_function")))
            terms |= set(term_ids(cf.get("directly_involved_in")))
        for ea in doc.get("existing_annotations") or []:
            rv = ea.get("review") or {}
            act = rv.get("action")
            if ea.get("negated"):
                continue
            if act in KEEP_ACTIONS or act == "NEW":
                terms |= set(term_ids(ea.get("term")))
            elif act == "MODIFY":
                terms |= {t for t in term_ids(rv.get("proposed_replacement_terms")) if t.startswith("GO:")}
        genes[acc] = {"symbol": sym, "terms": terms | mf_core}
    return genes


# ---------------------------------------------------------------- bulk sources
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def load_uniprot(org: str, rhea_master: dict):
    """data/<ORG>/uniprot.tsv from fetch_bulk.py -> acc -> symbol, Rhea master ids."""
    genes = {}
    for r in csv.DictReader((DATA / org / "uniprot.tsv").open(), delimiter="\t"):
        acc = r["Entry"]
        sym = r["Gene Names (primary)"] or (r["Gene Names (ordered locus)"].split() or [acc])[0]
        rx = {rhea_master.get(x, x) for x in r["Rhea ID"].split()}
        genes[acc] = {"symbol": sym, "rhea": rx, "terms": set()}
    return genes


def load_gaf(org: str, evidence: str):
    """GOA GAF -> acc -> GO ids. evidence: all | noiea | exp. NOT rows are skipped."""
    import gzip
    out = defaultdict(set)
    with gzip.open(DATA / org / "goa.gaf.gz", "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            c = line.rstrip("\n").split("\t")
            if c[0] != "UniProtKB" or "NOT" in c[3].split("|"):
                continue
            ev = c[6]
            if evidence == "noiea" and ev == "IEA":
                continue
            if evidence == "exp" and ev not in EXPERIMENTAL:
                continue
            out[c[1]].add(c[4])
    return out


def load_rhea_master(path: Path):
    m = {}
    for r in csv.DictReader(path.open(), delimiter="\t"):
        for k in ("RHEA_ID_LR", "RHEA_ID_RL", "RHEA_ID_BI", "RHEA_ID_MASTER"):
            m["RHEA:" + r[k]] = "RHEA:" + r["RHEA_ID_MASTER"]
    return m


SOURCES = ("reviews", "uniprot-rhea", "goa-all", "goa-noiea", "goa-exp")


def load_source(org: str, source: str, rhea_master: dict):
    """Return acc -> {symbol, terms, [rhea]} for the chosen annotation source."""
    if source == "reviews":
        return load_reviews(org)
    up = load_uniprot(org, rhea_master)
    ev = {"uniprot-rhea": "all", "goa-all": "all", "goa-noiea": "noiea", "goa-exp": "exp"}[source]
    gaf = load_gaf(org, ev)
    for acc, d in up.items():
        d["terms"] = gaf.get(acc, set())
        if source != "uniprot-rhea":
            d.pop("rhea")
    return up


# ---------------------------------------------------------------- analysis
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("organism")
    ap.add_argument("--n-random", type=int, default=200)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--source", choices=SOURCES, default="reviews",
                    help="reviews = curated gene reviews; uniprot-rhea = UniProt CATALYTIC ACTIVITY "
                         "Rhea ids (BP from GOA, all evidence); goa-* = GOA MF->rhea2go and GOA BP, "
                         "filtered by evidence")
    ap.add_argument("--reviewed-genes-only", action="store_true",
                    help="restrict a bulk source to the accessions that have a gene review")
    args = ap.parse_args()
    random.seed(args.seed)
    tag = args.source + ("-reviewedset" if args.reviewed_genes_only else "")
    out = HERE / "results" / args.organism / tag
    out.mkdir(parents=True, exist_ok=True)

    names, ns, parents, obsolete, alt = load_go(DATA / "go-basic.obo")
    anc = ancestors_fn(parents)
    go2rhea, rhea2chebi, chebi2name, rhea2eq, rhea2sides = load_rhea(DATA / "rhea.tsv")
    currency = {c for c, n in chebi2name.items() if n in CURRENCY_NAMES or CURRENCY_PATTERNS.search(n)
                or MACROMOLECULE_PATTERNS.search(n)}

    rhea_master = load_rhea_master(DATA / "rhea-directions.tsv")
    genes = load_source(args.organism, args.source, rhea_master)
    if args.reviewed_genes_only:
        keep = set(load_reviews(args.organism))
        genes = {a: d for a, d in genes.items() if a in keep}
    label = {a: d["symbol"] for a, d in genes.items()}
    norm = lambda t: alt.get(t, t)  # noqa: E731

    gene_rxn, gene_bp, gene_chem = {}, {}, {}
    n_mf_genes = 0
    for g, d in genes.items():
        terms = {norm(t) for t in d["terms"]}
        mfs = {t for t in terms if ns.get(t) == "molecular_function"}
        bps = {t for t in terms if ns.get(t) == "biological_process"}
        n_mf_genes += bool(mfs)
        if "rhea" in d:
            rx = {r for r in d["rhea"] if r in rhea2chebi}
            n_mf_genes += bool(rx) and not mfs
        else:
            rx = set().union(*[go2rhea.get(t, set()) for t in mfs]) if mfs else set()
        if rx:
            gene_rxn[g] = rx
            gene_chem[g] = set().union(*[rhea2chebi[r] for r in rx]) - currency
        gene_bp[g] = set().union(*[anc(t) for t in bps]) if bps else set()

    # bipartite gene<->metabolite and the gene projection
    chem_genes = defaultdict(set)
    for g, cs in gene_chem.items():
        for c in cs:
            chem_genes[c].add(g)
    G = nx.Graph()
    G.add_nodes_from(gene_rxn)
    edge_chems = defaultdict(set)
    for c, gs in chem_genes.items():
        gs = sorted(gs)
        for i in range(len(gs)):
            for j in range(i + 1, len(gs)):
                edge_chems[(gs[i], gs[j])].add(c)
    for (a, b), cs in edge_chems.items():
        G.add_edge(a, b, chems=sorted(cs), weight=len(cs))

    enz = sorted(gene_rxn)
    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    giant = comps[0] if comps else set()

    # ---------- BP: metabolic-process descendants, frequency within enzyme set
    met_bp = {g: {t for t in gene_bp[g] if METABOLIC_PROCESS in anc(t) and t != METABOLIC_PROCESS} for g in enz}
    freq = Counter(t for g in enz for t in met_bp[g])
    n_enz_bp = sum(1 for g in enz if met_bp[g])
    specific_cut = max(2, int(0.05 * len(enz)))  # term on <=5% of enzymes = "specific"
    spec = {g: {t for t in met_bp[g] if freq[t] <= specific_cut} for g in enz}

    def share_specific(a, b):
        return bool(spec[a] & spec[b])

    def jacc(a, b):
        u = met_bp[a] | met_bp[b]
        return len(met_bp[a] & met_bp[b]) / len(u) if u else 0.0

    with_bp = [g for g in enz if met_bp[g]]
    edges_bp = [(a, b) for a, b in G.edges() if met_bp[a] and met_bp[b]]
    obs_share = sum(share_specific(a, b) for a, b in edges_bp) / max(1, len(edges_bp))
    obs_jacc = sum(jacc(a, b) for a, b in edges_bp) / max(1, len(edges_bp))
    rnd_pairs = [tuple(random.sample(with_bp, 2)) for _ in range(20000)] if len(with_bp) > 1 else []
    rnd_share = sum(share_specific(a, b) for a, b in rnd_pairs) / max(1, len(rnd_pairs))
    rnd_jacc = sum(jacc(a, b) for a, b in rnd_pairs) / max(1, len(rnd_pairs))
    # metabolite-weighted: strong edges (>=2 shared intermediates)
    strong = [(a, b) for a, b in edges_bp if G[a][b]["weight"] >= 2]
    strong_share = sum(share_specific(a, b) for a, b in strong) / max(1, len(strong))

    # ---------- term-level coherence
    term_rows = []
    for t, n in freq.items():
        if n < 3 or n > specific_cut * 4:
            continue
        gs = [g for g in enz if t in met_bp[g]]
        sub = G.subgraph(gs)
        lcc = max((len(c) for c in nx.connected_components(sub)), default=0) / len(gs)
        rnd = []
        for _ in range(args.n_random):
            rs = random.sample(enz, len(gs))
            rnd.append(max((len(c) for c in nx.connected_components(G.subgraph(rs))), default=0) / len(gs))
        p = (1 + sum(r >= lcc for r in rnd)) / (1 + len(rnd))
        isolated = [g for g in gs if sub.degree(g) == 0]
        term_rows.append({
            "term": t, "label": names.get(t, ""), "n_genes": len(gs),
            "lcc_frac": round(lcc, 3), "random_lcc_mean": round(sum(rnd) / len(rnd), 3),
            "p_value": round(p, 4), "edges": sub.number_of_edges(),
            "isolated_genes": ";".join(label[g] for g in isolated), "genes": ";".join(label[g] for g in gs),
        })
    term_rows.sort(key=lambda r: (r["p_value"], -r["lcc_frac"]))

    # ---------- communities vs BP
    comm_rows = []
    if G.number_of_edges():
        comms = nx.community.louvain_communities(G.subgraph(giant), weight="weight", seed=args.seed)
        for i, cm in enumerate(sorted(comms, key=len, reverse=True)):
            best = None
            for t in set().union(*[met_bp[g] for g in cm]):
                tg = {g for g in enz if t in met_bp[g]}
                tp = len(tg & cm)
                prec, rec = tp / len(cm), tp / len(tg)
                f1 = 2 * prec * rec / (prec + rec) if tp else 0
                if best is None or f1 > best[0]:
                    best = (f1, t, prec, rec)
            hub = Counter(c for g in cm for c in gene_chem[g]).most_common(5)
            comm_rows.append({
                "community": i, "size": len(cm),
                "best_bp": best[1] if best else "", "best_bp_label": names.get(best[1], "") if best else "",
                "f1": round(best[0], 3) if best else 0, "precision": round(best[2], 3) if best else 0,
                "recall": round(best[3], 3) if best else 0,
                "top_metabolites": "; ".join(f"{chebi2name.get(c, c)}({n})" for c, n in hub),
                "genes": ";".join(sorted(label[g] for g in cm)), "_acc": sorted(cm),
            })

    # ---------- discordant edges: strong metabolic link, no shared metabolic BP at all
    disc = []
    for a, b in G.edges():
        if met_bp[a] and met_bp[b] and not (met_bp[a] & met_bp[b] - {METABOLIC_PROCESS}):
            disc.append({"gene_a": label[a], "gene_b": label[b], "n_shared": G[a][b]["weight"],
                         "shared_metabolites": "; ".join(chebi2name.get(c, c) for c in G[a][b]["chems"])})
    disc.sort(key=lambda r: -r["n_shared"])

    # enzymes with no metabolic BP at all
    no_bp = [g for g in enz if not met_bp[g]]

    summary = {
        "organism": args.organism,
        "reviews": len(genes),
        "genes_with_reviewed_mf": n_mf_genes,
        "genes_with_rhea_reactions": len(enz),
        "distinct_reactions": len(set().union(*gene_rxn.values())) if gene_rxn else 0,
        "distinct_noncurrency_metabolites": len(chem_genes),
        "network_edges": G.number_of_edges(),
        "connected_components": len(comps),
        "giant_component_size": len(giant),
        "isolated_enzymes": sum(1 for g in enz if G.degree(g) == 0),
        "enzymes_with_metabolic_bp": n_enz_bp,
        "enzymes_without_metabolic_bp": len(no_bp),
        "specific_bp_cutoff_genes": specific_cut,
        "edge_share_specific_bp": round(obs_share, 3),
        "random_pair_share_specific_bp": round(rnd_share, 3),
        "strong_edge_share_specific_bp": round(strong_share, 3),
        "n_strong_edges": len(strong),
        "edge_mean_bp_jaccard": round(obs_jacc, 3),
        "random_pair_mean_bp_jaccard": round(rnd_jacc, 3),
        "bp_terms_tested": len(term_rows),
        "bp_terms_more_connected_than_random_p<0.05": sum(r["p_value"] < 0.05 for r in term_rows),
        "bp_terms_fully_connected": sum(r["lcc_frac"] == 1 for r in term_rows),
        "discordant_edges": len(disc),
        "louvain_communities": len(comm_rows),
        "communities_best_bp_f1>=0.5": sum(r["f1"] >= 0.5 for r in comm_rows),
        "top_hub_metabolites": [(chebi2name.get(c, c), len(gs)) for c, gs in
                                sorted(chem_genes.items(), key=lambda x: -len(x[1]))[:15]],
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2))

    def wtsv(name, rows):
        if not rows:
            return
        with (out / name).open("w") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
            w.writeheader()
            w.writerows(rows)

    wtsv("bp_term_coherence.tsv", term_rows)
    wtsv("communities.tsv", [{k: v for k, v in r.items() if k != "_acc"} for r in comm_rows])
    wtsv("discordant_edges.tsv", disc)
    wtsv("gene_reactions.tsv", [{"gene": label[g], "uniprot": g, "reactions": ";".join(sorted(gene_rxn[g])),
                                  "metabolites": "; ".join(sorted(chebi2name.get(c, c) for c in gene_chem[g])),
                                  "metabolic_bp": "; ".join(sorted(names.get(t, t) for t in spec[g])),
                                  "degree": G.degree(g)} for g in enz])
    wtsv("edges.tsv", [{"gene_a": label[a], "gene_b": label[b], "shared_metabolites": "; ".join(chebi2name.get(c, c) for c in d["chems"]),
                        "share_specific_bp": share_specific(a, b) if met_bp[a] and met_bp[b] else ""}
                       for a, b, d in G.edges(data=True)])
    # graph for visualisation
    comm_of = {g: r["community"] for r in comm_rows for g in r["_acc"]}
    json.dump({
        "nodes": [{"id": g, "label": label[g], "deg": G.degree(g), "comm": comm_of.get(g, -1),
                   "bp": sorted(names.get(t, t) for t in spec[g])[:6],
                   "rxn": [rhea2eq[r] for r in sorted(gene_rxn[g])][:4]} for g in enz if G.degree(g)],
        "links": [{"source": a, "target": b, "w": d["weight"],
                   "m": [chebi2name.get(c, c) for c in d["chems"]][:5],
                   "bp": share_specific(a, b) if met_bp[a] and met_bp[b] else None}
                  for a, b, d in G.edges(data=True)],
        "communities": [{k: r[k] for k in ("community", "size", "best_bp_label", "f1", "top_metabolites")} for r in comm_rows],
        "summary": summary,
    }, (out / "graph.json").open("w"))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
