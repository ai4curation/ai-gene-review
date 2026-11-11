#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.85", "pyfamsa>=0.5", "requests", "pyyaml", "piqtree>=0.8", "cogent3"]
# ///
"""Evolutionary analysis of the succinyl-CoA synthetase subunit families.

Beta subunit: PANTHER PTHR11815 (S. cerevisiae LSC2, P53312)
Alpha subunit: PANTHER PTHR11117 (S. cerevisiae LSC1, P53598)

What it does (nothing is hard-coded except identifiers of the query proteins,
the PANTHER node ids being interrogated, and the organism panel):

1. Downloads the current PANTHER tree of each family from the PANTHER API and
   reports, for every organism in the tree, how many beta-subunit genes fall in
   each daughter clade of the eukaryotic beta duplication node, and how many
   alpha-subunit genes it has (paralog census).
2. Fetches the sequences of a panel of beta subunits from UniProt, aligns them
   (FAMSA), builds bootstrapped neighbor-joining trees (BLOSUM62 distances) and
   scores quartets that test where yeast LSC2 sits relative to the animal
   ATP-specific (SUCLA2) and GTP-specific (SUCLG2) beta subunits. This is an
   independent check of the PANTHER topology, not a copy of it. The same alignment is
   then analysed by maximum likelihood (IQ-TREE via piqtree, LG+G4, ultrafast bootstrap)
   and the membership and support of the clades around LSC2, SUCLA2 and SUCLG2 are
   reported, because distance trees can be misled by long branches.
3. Reports the residue aligned to position 20 of the mature E. coli / pig beta
   subunit (Pro in E. coli and T. aquaticus, Gln in pig GTP-specific SCS;
   PMID:16481318, PMID:22751660) for every panel member, and pairwise identity
   of LSC2 to human SUCLA2 and SUCLG2.

Run: uv run --script scs_family_evolution.py --bootstraps 200   (needs network access to pantherdb.org and uniprot.org)

Outputs: results.yaml (machine-readable) and a printed summary. Results may be
inconclusive; the script reports whatever it computes.
"""
from __future__ import annotations

import argparse
import io
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import requests
import yaml
from Bio import Phylo, SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from pyfamsa import Aligner, Sequence

PANTHER_TREE = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family={fam}"
UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/accessions?accessions={accs}&format=fasta"

BETA_FAMILY = "PTHR11815"
ALPHA_FAMILY = "PTHR11117"
# Node at which PANTHER infers a duplication of the eukaryotic beta subunit, and the node
# at which PAINT records the gain of GDP-forming / loss of ADP-forming activity.
BETA_EUK_DUPLICATION = "PTN000212530"
PAINT_GDP_NODE = "PTN000929335"

# Organisms sampled for the independent tree (names as PANTHER writes them).
PANEL_ORGANISMS = [
    "Homo sapiens", "Mus musculus", "Drosophila melanogaster", "Caenorhabditis elegans",
    "Nematostella vectensis", "Monosiga brevicollis",
    "Saccharomyces cerevisiae", "Schizosaccharomyces pombe", "Candida albicans",
    "Neurospora crassa", "Cryptococcus neoformans", "Ustilago maydis",
    "Batrachochytrium dendrobatidis", "Dictyostelium discoideum",
    "Arabidopsis thaliana", "Oryza sativa", "Chlamydomonas reinhardtii",
    "Trypanosoma brucei", "Leishmania major", "Trichomonas vaginalis",
    "Plasmodium falciparum", "Phytophthora ramorum", "Thalassiosira pseudonana",
    "Escherichia coli", "Pseudomonas aeruginosa", "Bacillus subtilis",
    "Mycobacterium tuberculosis", "Bradyrhizobium diazoefficiens",
    "Sulfolobus solfataricus", "Methanocaldococcus jannaschii", "Halobacterium salinarum",
]
# Extra experimentally characterised reference not in the PANTHER tree: pig GTP-specific beta.
EXTRA_ACCESSIONS = {"P53590": "Sus scrofa"}

Q = {  # proteins the quartets are phrased in terms of
    "LSC2": "P53312", "SUCLA2": "Q9P2R7", "SUCLG2": "Q96I99", "EcSucC": "P0A836",
    "SpBeta": "O94415", "pigG": "P53590",
}


def kids(n):
    c = n.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def leaves(n):
    k = kids(n)
    return [n] if not k else [x for c in k for x in leaves(c)]


def find(n, pid):
    if n.get("persistent_id") == pid:
        return n
    for c in kids(n):
        r = find(c, pid)
        if r is not None:
            return r
    return None


def acc_of(leaf):
    m = re.search(r"UniProtKB=([A-Z0-9]+)", leaf.get("node_name", ""))
    return m.group(1) if m else None


def get_tree(fam):
    r = requests.get(PANTHER_TREE.format(fam=fam), timeout=180)
    r.raise_for_status()
    s = r.json()["search"]
    return s["product"]["version"], s["tree_topology"]["annotation_node"]


def lineage_label(root, leaf_pid):
    """Deepest named taxon labels on the path root -> leaf (for grouping organisms)."""
    path = []

    def walk(n, acc):
        acc = acc + ([n["species"]] if n.get("species") else [])
        if n.get("persistent_id") == leaf_pid:
            path.extend(acc)
            return True
        return any(walk(c, acc) for c in kids(n))

    walk(root, [])
    return path


def path_to(root, acc):
    """Nodes on the path from the tree root to the leaf with UniProt accession `acc`."""
    def walk(n, trail):
        trail = trail + [n]
        if not kids(n):
            return trail if acc_of(n) == acc else None
        for c in kids(n):
            r = walk(c, trail)
            if r:
                return r
        return None
    return walk(root, [])


def node_record(n):
    return {"node": n.get("persistent_id"), "event_type": n.get("event_type"), "taxon": n.get("species"),
            "n_leaves": len(leaves(n))}


def organism_clade(root, organism):
    """Smallest internal node containing every leaf of `organism` (None if the organism is absent)."""
    target = {x["persistent_id"] for x in leaves(root) if x.get("organism") == organism}
    if not target:
        return None
    best = None

    def walk(n):
        nonlocal best
        ids = {x["persistent_id"] for x in leaves(n)}
        if target <= ids:
            best = n
            for c in kids(n):
                walk(c)
    walk(root)
    return best


def tree_nodes(alpha, beta):
    """PANTHER node ids that the family reviews cite, read from the trees rather than typed in."""
    out = {}
    for fam, root, acc, label in ((ALPHA_FAMILY, alpha, "P53598", "LSC1"), (BETA_FAMILY, beta, Q["LSC2"], "LSC2")):
        pth = path_to(root, acc)
        out[f"{fam}_path_root_to_{label}"] = [node_record(n) for n in pth[:-1]] if pth else "leaf not found"
        tv = organism_clade(root, "Trichomonas vaginalis")
        out[f"{fam}_Trichomonas_vaginalis_clade"] = node_record(tv) if tv is not None else None
    xc = [x for x in leaves(beta) if x.get("organism") == "Xanthomonas campestris"]
    out[f"{BETA_FAMILY}_Xanthomonas_campestris_leaves"] = []
    for x in xc:
        pth = path_to(beta, acc_of(x)) if acc_of(x) else None
        out[f"{BETA_FAMILY}_Xanthomonas_campestris_leaves"].append(
            {"leaf": x["persistent_id"], "parent_path": [node_record(n) for n in pth[-4:-1]] if pth else None})
    return out


def fetch_fasta(accs):
    out = {}
    accs = list(accs)
    for i in range(0, len(accs), 50):
        r = requests.get(UNIPROT_FASTA.format(accs=",".join(accs[i:i + 50])), timeout=120)
        r.raise_for_status()
        for rec in SeqIO.parse(io.StringIO(r.text), "fasta"):
            out[rec.id.split("|")[1]] = str(rec.seq)
    return out


def quartet(tree, a, b, c, d):
    """Return which pairing the unrooted tree supports for four tips: 'ab|cd', 'ac|bd' or 'ad|bc'."""
    def dist(x, y):
        if hasattr(tree, "trace"):  # Bio.Phylo tree
            return len(tree.trace(x, y))
        nx, ny = tree.get_node_matching_name(x), tree.get_node_matching_name(y)  # cogent3 tree
        ax = [id(n) for n in nx.ancestors()]
        ay = [id(n) for n in ny.ancestors()]
        shared = len(set(ax) & set(ay))
        return (len(ax) - shared) + (len(ay) - shared)
    s = {"ab|cd": dist(a, b) + dist(c, d), "ac|bd": dist(a, c) + dist(b, d), "ad|bc": dist(a, d) + dist(b, c)}
    best = sorted(s.items(), key=lambda kv: kv[1])
    return best[0][0] if best[0][1] < best[1][1] else "unresolved"


def nj(aln):
    dm = DistanceCalculator("blosum62").get_distance(aln)
    return DistanceTreeConstructor().nj(dm)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bootstraps", type=int, default=100)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--ml-bootstraps", type=int, default=1000, help="ultrafast bootstraps for the ML tree; 0 skips it")
    ap.add_argument("--out", default=str(Path(__file__).parent / "results.yaml"))
    ap.add_argument("--nodes-only", action="store_true",
                    help="only refresh the panther_tree_nodes section of an existing results file")
    args = ap.parse_args()
    random.seed(args.seed)
    res: dict = {}

    # ---- 1. paralog census from the PANTHER trees --------------------------------
    bver, beta = get_tree(BETA_FAMILY)
    aver, alpha = get_tree(ALPHA_FAMILY)
    res["panther_version"] = {"beta": bver, "alpha": aver}
    res["panther_tree_nodes"] = tree_nodes(alpha, beta)
    if args.nodes_only:
        old = yaml.safe_load(Path(args.out).read_text())
        merged = {}
        for k, v in old.items():
            merged[k] = v
            if k == "panther_version":
                merged["panther_tree_nodes"] = res["panther_tree_nodes"]
        merged["panther_tree_nodes"] = res["panther_tree_nodes"]
        Path(args.out).write_text(yaml.safe_dump(merged, sort_keys=False, width=110))
        yaml.safe_dump(res["panther_tree_nodes"], sys.stdout, sort_keys=False, width=110)
        return
    dup = find(beta, BETA_EUK_DUPLICATION)
    daughters = kids(dup)
    gdp_node = find(beta, PAINT_GDP_NODE)
    # Name the daughter clades by content rather than by assumption.
    clade_of = {}
    clade_names = {}
    for dnode in daughters:
        accs = {acc_of(x) for x in leaves(dnode)}
        if Q["SUCLA2"] in accs and Q["SUCLG2"] in accs:
            name = "contains_both_SUCLA2_and_SUCLG2"
        elif Q["SUCLA2"] in accs:
            name = "A_clade(contains human SUCLA2)"
        elif Q["SUCLG2"] in accs:
            name = "G_clade(contains human SUCLG2)"
        else:
            name = "other_" + dnode["persistent_id"]
        clade_names[dnode["persistent_id"]] = name
        for x in leaves(dnode):
            clade_of[x["persistent_id"]] = name
    res["beta_eukaryotic_duplication"] = {
        "node": BETA_EUK_DUPLICATION, "event_type": dup.get("event_type"), "taxon": dup.get("species"),
        "daughters": [{"node": d["persistent_id"], "name": clade_names[d["persistent_id"]],
                       "n_leaves": len(leaves(d)), "subfamily": d.get("sf_id")} for d in daughters],
    }
    gdp_leaves = {x["persistent_id"] for x in leaves(gdp_node)}
    census = defaultdict(lambda: Counter())
    group = {}
    for x in leaves(beta):
        org = x["organism"]
        c = clade_of.get(x["persistent_id"], "outside_eukaryotic_duplication")
        census[org]["beta:" + c] += 1
        if x["persistent_id"] in gdp_leaves:
            census[org]["beta:under_PAINT_GDP_node"] += 1
        group.setdefault(org, set()).update(lineage_label(beta, x["persistent_id"]))
    for x in leaves(alpha):
        census[x["organism"]]["alpha"] += 1
    a_name = next((n for n in clade_names.values() if n.startswith("A_clade")), None)
    g_name = next((n for n in clade_names.values() if n.startswith("G_clade")), None)
    res["clade_membership"] = {}
    for k, acc in Q.items():
        hit = [x for x in leaves(beta) if acc_of(x) == acc]
        res["clade_membership"][k] = {
            "accession": acc,
            "clade": clade_of.get(hit[0]["persistent_id"], "outside_eukaryotic_duplication") if hit else "not_in_panther_tree",
            "under_PAINT_GDP_node": bool(hit and hit[0]["persistent_id"] in gdp_leaves),
            "panther_subfamily": (hit[0].get("prop_sf_id") or hit[0].get("sf_id")) if hit else None,
        }
    # summarise eukaryotes by major group
    def major(org):
        lab = group.get(org, set())
        for key in ["Fungi", "Metazoa-Choanoflagellida", "Dictyostelium", "Viridiplantae", "Excavates",
                    "Alveolata", "Stramenopiles", "Archaea", "Eubacteria"]:
            if key in lab:
                return key
        return "other"
    summary = defaultdict(lambda: Counter())
    per_org = {}
    for org, c in sorted(census.items()):
        a = c.get("beta:" + a_name, 0) if a_name else 0
        g = c.get("beta:" + g_name, 0) if g_name else 0
        m = major(org)
        if m in ("Archaea", "Eubacteria", "other"):
            state = "prokaryote_or_unplaced"
        else:
            state = "A_and_G" if a and g else "A_only" if a else "G_only" if g else "neither"
        summary[m][state] += 1
        per_org[org] = {"group": m, "beta_A_clade": a, "beta_G_clade": g,
                        "beta_under_PAINT_GDP_node": c.get("beta:under_PAINT_GDP_node", 0),
                        "beta_outside_duplication": c.get("beta:outside_eukaryotic_duplication", 0),
                        "alpha": c.get("alpha", 0)}
    res["eukaryotes_not_matching_group_majority"] = {
        o: v for o, v in per_org.items()
        if (v["group"] == "Fungi" and v["beta_G_clade"]) or (v["group"] == "Metazoa-Choanoflagellida" and not (v["beta_A_clade"] and v["beta_G_clade"]))}
    res["beta_paralog_census_by_group"] = {k: dict(v) for k, v in sorted(summary.items())}
    res["beta_paralog_census_fungi"] = {o: v for o, v in per_org.items() if v["group"] == "Fungi"}
    res["beta_paralog_census_selected"] = {o: per_org[o] for o in PANEL_ORGANISMS if o in per_org}
    # non-canonical leaves in the trees (by PANTHER definition line)
    res["non_scs_named_leaves"] = sorted({f'{x["organism"]}: {x.get("definition")}' for x in leaves(beta) + leaves(alpha)
                                          if x.get("definition") and not re.search(r"[Ss]uccin", x["definition"])})

    # ---- 2. independent tree on a panel -------------------------------------------
    panel = {}
    for x in leaves(beta):
        if x["organism"] in PANEL_ORGANISMS and acc_of(x):
            panel[acc_of(x)] = (x["organism"], clade_of.get(x["persistent_id"], "outside"))
    for acc, org in EXTRA_ACCESSIONS.items():
        panel[acc] = (org, "not_in_panther_tree")
    seqs = fetch_fasta(panel)
    missing = sorted(set(panel) - set(seqs))
    res["panel"] = {"n_requested": len(panel), "n_fetched": len(seqs), "missing": missing}
    msa = Aligner().align([Sequence(a.encode(), s.encode()) for a, s in seqs.items()])
    aln = {m.id.decode(): m.sequence.decode() for m in msa}
    ids = list(aln)
    ncol = len(next(iter(aln.values())))
    # keep columns with <50% gaps (removes transit peptides / lineage-specific extensions)
    keep = [i for i in range(ncol) if sum(aln[a][i] == "-" for a in ids) < 0.5 * len(ids)]
    res["alignment"] = {"n_sequences": len(ids), "n_columns": ncol, "n_columns_used": len(keep)}

    def make(cols):
        return MultipleSeqAlignment([SeqRecord(Seq("".join(aln[a][i] for i in cols)), id=a) for a in ids])

    quartets = {
        "LSC2+SUCLA2 | SUCLG2+EcSucC": ("LSC2", "SUCLA2", "SUCLG2", "EcSucC"),
        "SpBeta+SUCLA2 | SUCLG2+EcSucC": ("SpBeta", "SUCLA2", "SUCLG2", "EcSucC"),
        "LSC2+SpBeta | SUCLA2+SUCLG2": ("LSC2", "SpBeta", "SUCLA2", "SUCLG2"),
        "pigG+SUCLG2 | SUCLA2+LSC2": ("pigG", "SUCLG2", "SUCLA2", "LSC2"),
    }
    # add a plant and a Dictyostelium member of each clade if present, to test the deep duplication
    def pick(org, clade_prefix):
        for acc, (o, c) in sorted(panel.items()):
            if o == org and c.startswith(clade_prefix) and acc in aln:
                return acc
        return None
    plantG = pick("Arabidopsis thaliana", "G_clade")
    dictyA, dictyG = pick("Dictyostelium discoideum", "A_clade"), pick("Dictyostelium discoideum", "G_clade")
    usG = pick("Ustilago maydis", "G_clade")
    extra = {"plant": plantG, "dictyA": dictyA, "dictyG": dictyG, "UstilagoG": usG}
    res["extra_tips"] = extra
    tips = dict(Q, **{k: v for k, v in extra.items() if v})
    if plantG:
        quartets["plant+SUCLG2 | SUCLA2+LSC2"] = ("plant", "SUCLG2", "SUCLA2", "LSC2")
    if dictyA and dictyG:
        quartets["dictyA+SUCLA2 | dictyG+SUCLG2"] = ("dictyA", "SUCLA2", "dictyG", "SUCLG2")
        quartets["dictyA+LSC2 | dictyG+SUCLG2"] = ("dictyA", "LSC2", "dictyG", "SUCLG2")
    if usG:
        quartets["UstilagoG+SUCLG2 | SUCLA2+LSC2"] = ("UstilagoG", "SUCLG2", "SUCLA2", "LSC2")
    absent = [k for k, v in tips.items() if v not in aln]
    res["quartet_tips_missing"] = absent
    ref_tree = nj(make(keep))
    qres = {}
    for name, (a, b, c, d) in quartets.items():
        if any(t in absent for t in (a, b, c, d)):
            qres[name] = "not evaluated (tip missing)"
            continue
        qres[name] = {"full_alignment_topology": quartet(ref_tree, tips[a], tips[b], tips[c], tips[d]), "bootstrap_support": Counter()}
    for _ in range(args.bootstraps):
        cols = [random.choice(keep) for _ in keep]
        t = nj(make(cols))
        for name, (a, b, c, d) in quartets.items():
            if isinstance(qres[name], dict):
                qres[name]["bootstrap_support"][quartet(t, tips[a], tips[b], tips[c], tips[d])] += 1
    for name in qres:
        if isinstance(qres[name], dict):
            qres[name]["bootstrap_support"] = dict(qres[name]["bootstrap_support"])
    res["quartets"] = {"note": "'ab|cd' = the pairing written in the quartet name; bootstraps=%d" % args.bootstraps, "results": qres}
    Phylo.write(ref_tree, str(Path(args.out).with_name("beta_panel_nj.nwk")), "newick")

    # ---- 2b. maximum-likelihood tree on the same alignment -----------------------------
    if args.ml_bootstraps:
        import cogent3
        import piqtree

        caln = cogent3.make_aligned_seqs({a: "".join(aln[a][i] for i in keep) for a in ids}, moltype="protein")
        ml = piqtree.build_tree(caln, "LG+G4", rand_seed=args.seed, bootstrap_replicates=args.ml_bootstraps)
        alltips = frozenset(ml.get_tip_names())
        split_support = {}
        for nd in ml.preorder():
            if nd.is_tip() or nd.is_root():
                continue
            st = frozenset(nd.get_tip_names())
            sup = getattr(nd, "support", None)
            split_support[st] = sup
            split_support[alltips - st] = sup
        rooted = ml.rooted_with_tip(Q["EcSucC"])

        def describe(names):
            """Smallest clade (tree rooted on E. coli SucC) holding the named tips: members and support."""
            node = rooted.lowest_common_ancestor(names)
            members = frozenset(node.get_tip_names())
            comp = Counter()
            for m in members:
                org, cl = panel[m]
                tag = "A" if cl.startswith("A_") else "G" if cl.startswith("G_") else "prokaryote" if cl == "outside" else "pig_SUCLG2"
                comp[f"{org} [{tag}]"] += 1
            return {"n_tips": len(members), "ufboot_support": split_support.get(members),
                    "members": dict(sorted(comp.items()))}

        tests = {
            "LSC2 + human SUCLA2": [Q["LSC2"], Q["SUCLA2"]],
            "LSC2 + S. pombe beta": [Q["LSC2"], Q["SpBeta"]],
            "human SUCLG2 + pig SUCLG2": [Q["SUCLG2"], Q["pigG"]],
            "LSC2 + human SUCLG2": [Q["LSC2"], Q["SUCLG2"]],
        }
        if dictyG:
            tests["human SUCLG2 + Dictyostelium G-clade beta"] = [Q["SUCLG2"], dictyG]
        if dictyA:
            tests["human SUCLA2 + Dictyostelium A-clade beta"] = [Q["SUCLA2"], dictyA]
        if plantG:
            tests["Arabidopsis beta + human SUCLG2"] = [plantG, Q["SUCLG2"]]
            tests["Arabidopsis beta + human SUCLA2"] = [plantG, Q["SUCLA2"]]
        if usG:
            tests["Ustilago second protein + LSC2"] = [usG, Q["LSC2"]]
            tests["Ustilago second protein + human SUCLG2"] = [usG, Q["SUCLG2"]]
        res["maximum_likelihood"] = {
            "method": f"IQ-TREE (piqtree {piqtree.__version__}), model LG+G4, {args.ml_bootstraps} ultrafast bootstraps, "
                      "same trimmed alignment as the NJ analysis; clades read with the tree rooted on E. coli SucC",
            "tags": "A/G = daughter clade of the eukaryotic duplication in the PANTHER tree",
            "smallest_clade_containing": {k: describe(v) for k, v in tests.items()},
        }
        mlq = {}
        for name, (a, b, c, d) in quartets.items():
            if isinstance(qres[name], dict):
                mlq[name] = quartet(ml, tips[a], tips[b], tips[c], tips[d])
        res["maximum_likelihood"]["quartet_topology_in_ml_tree"] = mlq
        Path(args.out).with_name("beta_panel_ml.nwk").write_text(ml.get_newick(with_distances=True) + "\n")

    # ---- 3. residue at mature position 20 and pairwise identities ------------------
    def col_of(acc, pos):  # alignment column of 1-based residue `pos` of protein `acc`
        n = 0
        for i, ch in enumerate(aln[acc]):
            if ch != "-":
                n += 1
                if n == pos:
                    return i
        raise ValueError(pos)
    ec = Q["EcSucC"]
    c20 = col_of(ec, 20)
    res["position20"] = {"anchor": f"E. coli SucC {ec} residue 20 = {aln[ec][c20]}", "by_protein": {}}
    for acc in sorted(ids, key=lambda a: (panel[a][1], panel[a][0])):
        res["position20"]["by_protein"][acc] = {"organism": panel[acc][0], "clade": panel[acc][1], "residue": aln[acc][c20]}

    def ident(a, b):
        pairs = [(x, y) for x, y in zip(aln[a], aln[b]) if x != "-" and y != "-"]
        return round(100 * sum(x == y for x, y in pairs) / len(pairs), 1), len(pairs)
    res["pairwise_identity_percent"] = {}
    for a, b in [("LSC2", "SUCLA2"), ("LSC2", "SUCLG2"), ("LSC2", "EcSucC"), ("LSC2", "SpBeta"), ("SUCLA2", "SUCLG2")]:
        if Q[a] in aln and Q[b] in aln:
            i, n = ident(Q[a], Q[b])
            res["pairwise_identity_percent"][f"{a}_vs_{b}"] = {"identity": i, "aligned_positions": n}

    class NoAlias(yaml.SafeDumper):
        def ignore_aliases(self, data):
            return True
    text = yaml.dump(res, Dumper=NoAlias, sort_keys=False, width=110)
    Path(args.out).write_text(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
