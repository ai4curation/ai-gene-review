#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.85", "pyfamsa>=0.5", "requests", "pyyaml", "numpy", "piqtree>=0.8", "cogent3"]
# ///
"""Evolutionary analysis of the succinyl-CoA synthetase subunit families.

Beta subunit: PANTHER PTHR11815 (S. cerevisiae LSC2, P53312)
Alpha subunit: PANTHER PTHR11117 (S. cerevisiae LSC1, P53598)

Nothing is hard-coded except identifiers: the query proteins, the PANTHER node ids
being interrogated, the organism panel and a list of extra UniProt accessions. Every
organism name, residue, count, clade and support value is computed at run time.

1. PANTHER trees (PANTHER API). Per organism, how many beta-subunit genes fall in each
   daughter clade of the eukaryotic beta duplication node, and how many alpha-subunit
   genes it has. Organisms are grouped by their UniProt lineage, not by the PANTHER
   node they sit under, so a bacterial leaf placed inside an animal clade stays a bacterium.
2. Position 20. The residue homologous to Pro20 of E. coli SucC (Gln20 of the mature pig
   GTP-specific beta subunit; PMID:16481318, PMID:22751660) is read by pairwise local
   alignment to three references (E. coli SucC, human SUCLA2, human SUCLG2) and taken
   from the best-scoring one. A protein without the N-terminal ATP-grasp domain (Pfam
   PF08442) has no homologous residue and is reported as such. The scan covers
   (a) every leaf of the PANTHER PTHR11815 tree, reported per PANTHER node,
   (b) every fungal UniProt entry of the family (taxonomy 4751), reported per phylum, and
   (c) every other eukaryotic UniProt entry outside animals and land plants/green algae.
3. Panel trees. A panel of beta subunits (PANTHER leaves of the panel organisms plus the
   extra accessions) is aligned with FAMSA. Neighbor-joining trees (BLOSUM62
   dissimilarities) with column bootstrap, and maximum-likelihood trees (IQ-TREE via
   piqtree, LG+G4, ultrafast bootstrap, three runs with fixed seeds), are read in the same way: the tree
   is rooted on E. coli SucC, and
   - for each eukaryotic tip X, the rooted triplet (X, human SUCLA2, human SUCLG2) says
     whether X is closer to SUCLA2, closer to SUCLG2, or outside both;
   - for named sets of tips, the smallest clade holding them is listed with its true clade
     support (how often exactly that clade is recovered in the bootstrap trees).
   The triplet is the outgroup-anchored quartet (X, SUCLA2, SUCLG2, E. coli SucC).
   A sensitivity run repeats the ML tree without proteins that lack the ATP-grasp domain.

Run: uv run --script scs_family_evolution.py --bootstraps 200
(needs network access to pantherdb.org and rest.uniprot.org)

Outputs: results.yaml, beta_panel_nj.nwk (internal labels = NJ clade bootstrap, percent)
and beta_panel_ml.nwk (internal labels = lowest ultrafast bootstrap over the ML runs).
The NJ analysis is exactly reproducible. IQ-TREE as called through piqtree is not, even
with a fixed seed, so ML supports are reported as a range over runs. Results may be
inconclusive; the script reports whatever it computes.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import requests
import yaml
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from pyfamsa import Aligner, Sequence

PANTHER_TREE = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family={fam}"
UNIPROT = "https://rest.uniprot.org"
META_FIELDS = "accession,organism_name,organism_id,lineage,xref_pfam,protein_name,gene_names,length,xref_panther"

BETA_FAMILY = "PTHR11815"
ALPHA_FAMILY = "PTHR11117"
# Node at which PANTHER infers a duplication of the eukaryotic beta subunit, and the node
# at which PAINT records the gain of GDP-forming / loss of ADP-forming activity.
BETA_EUK_DUPLICATION = "PTN000212530"
PAINT_GDP_NODE = "PTN000929335"
ATP_GRASP_PFAM = "PF08442"   # N-terminal ATP-grasp domain of the beta subunit; position 20 lies in it
CITRATE_LYASE_PFAM = {"PF16114", "PF00285", "PF24948"}  # ATP-citrate lyase domains (not SCS beta)

# Organisms sampled for the panel trees (names as PANTHER writes them).
PANEL_ORGANISMS = [
    "Homo sapiens", "Mus musculus", "Drosophila melanogaster", "Caenorhabditis elegans",
    "Nematostella vectensis", "Monosiga brevicollis",
    "Saccharomyces cerevisiae", "Schizosaccharomyces pombe", "Candida albicans",
    "Neurospora crassa", "Cryptococcus neoformans", "Ustilago maydis",
    "Batrachochytrium dendrobatidis", "Dictyostelium discoideum",
    "Arabidopsis thaliana", "Oryza sativa", "Chlamydomonas reinhardtii",
    "Trypanosoma brucei", "Leishmania major", "Trichomonas vaginalis",
    "Plasmodium falciparum", "Paramecium tetraurelia", "Phytophthora ramorum", "Thalassiosira pseudonana",
    "Escherichia coli", "Pseudomonas aeruginosa", "Bacillus subtilis",
    "Mycobacterium tuberculosis", "Bradyrhizobium diazoefficiens",
    "Sulfolobus solfataricus", "Methanocaldococcus jannaschii", "Halobacterium salinarum",
]
# Extra accessions added to the panel, with the reason each is there. Organism names and
# everything else about them are fetched from UniProt; an accession that cannot be fetched
# is dropped and listed under panel.missing. Some are not leaves of the PANTHER tree.
EXTRA_ACCESSIONS = {
    "P53590": "pig GTP-specific beta subunit, crystal structure (PMID:16481318)",
    "B3FHP0": "Blastocystis beta subunit, ATP-specific by assay (PMID:18452512)",
    "P25126": "Thermus thermophilus beta subunit (Thermus SCS prefers GTP, PMID:22751660)",
    "A0A1Y2H5W1": "early-diverging fungus, second beta gene (Lobosporangium)",
    "A0A1Y2GFP6": "same species as A0A1Y2H5W1, first beta gene",
    "A0A197JV50": "early-diverging fungus, second beta gene (Linnemannia)",
    "A0A197JVG0": "same species as A0A197JV50, first beta gene",
    "A0A075B0S1": "early-diverging fungus (Rozella)",
    "A0A1Y1YRN0": "early-diverging fungus, second beta gene (Basidiobolus)",
    "A0A1Y1Y1F7": "same species as A0A1Y1YRN0, first beta gene",
    "A0A0E9NQG5": "ascomycete Saitoella, second beta gene",
    "A0A0E9N8G8": "same species as A0A0E9NQG5, first beta gene",
    "I7MLW4": "ciliate (Tetrahymena)",
    "A0A0L0DTA8": "apusomonad (Thecamonas)",
    "A0A0D2X2I5": "filasterean (Capsaspora)",
    "D2VP45": "heterolobosean (Naegleria)",
}

Q = {  # reference proteins the tests are phrased in terms of
    "LSC2": "P53312", "SUCLA2": "Q9P2R7", "SUCLG2": "Q96I99", "EcSucC": "P0A836",
    "SpBeta": "O94415", "pigG": "P53590",
}
EC_POSITION = 20  # residue of E. coli SucC (no transit peptide) that anchors "position 20"

CACHE_DIR: Path | None = None  # set by --cache-dir (development aid; off by default)


# ----------------------------------------------------------------------------- network
def http_get(url, tries=5):
    if CACHE_DIR is not None:
        f = CACHE_DIR / hashlib.sha1(url.encode()).hexdigest()
        if f.exists():
            return f.read_text()
    last = None
    for i in range(tries):
        try:
            r = requests.get(url, timeout=300)
            if r.status_code == 200:
                if CACHE_DIR is not None:
                    f.write_text(r.text)
                return r.text
            last = f"HTTP {r.status_code}"
            if r.status_code in (400, 404):
                break
        except requests.RequestException as e:  # retried
            last = repr(e)
        time.sleep(3 * (i + 1))
    raise RuntimeError(f"could not fetch {url}: {last}")


def get_tree(fam):
    s = json.loads(http_get(PANTHER_TREE.format(fam=fam)))["search"]
    return s["product"]["version"], s["tree_topology"]["annotation_node"]


def parse_tsv(text):
    lines = text.rstrip("\n").split("\n")
    head = lines[0].split("\t")
    return [dict(zip(head, ln.split("\t"))) for ln in lines[1:] if ln]


def meta_record(row):
    lin = [x.strip() for x in row.get("Taxonomic lineage", "").split(",") if x.strip()]
    return {
        "organism": row.get("Organism", ""),
        "organism_id": row.get("Organism (ID)", ""),
        "lineage": [re.sub(r" \([^()]*\)$", "", x) for x in lin],
        "phylum": next((re.sub(r" \(phylum\)$", "", x) for x in lin if x.endswith("(phylum)")), None),
        "pfam": [p for p in row.get("Pfam", "").split(";") if p],
        "protein_name": row.get("Protein names", ""),
        "gene_names": row.get("Gene Names", ""),
        "length": int(row["Length"]) if row.get("Length", "").isdigit() else None,
        "panther": [p for p in row.get("PANTHER", "").split(";") if p],
        "sequence": row.get("Sequence"),
    }


def fetch_entries(accs):
    """UniProtKB sequence and metadata for accessions. Returns (seqs, meta, unisave_only, missing)."""
    accs = list(dict.fromkeys(accs))
    seqs, meta = {}, {}
    for i in range(0, len(accs), 50):
        chunk = ",".join(accs[i:i + 50])
        for rec in SeqIO.parse(io.StringIO(http_get(f"{UNIPROT}/uniprotkb/accessions?accessions={chunk}&format=fasta")), "fasta"):
            seqs[rec.id.split("|")[1]] = str(rec.seq)
        for row in parse_tsv(http_get(f"{UNIPROT}/uniprotkb/accessions?accessions={chunk}&format=tsv&fields={META_FIELDS}")):
            meta[row["Entry"]] = meta_record(row)
    unisave, missing = [], []
    for a in accs:
        if a in seqs:
            continue
        try:  # entry deleted from UniProtKB: take its last sequence version from UniSave
            rec = next(SeqIO.parse(io.StringIO(http_get(f"{UNIPROT}/unisave/{a}?format=fasta", tries=3)), "fasta"))
            seqs[a] = str(rec.seq)
            unisave.append(a)
        except (RuntimeError, StopIteration):
            missing.append(a)
    return seqs, meta, sorted(unisave), sorted(missing)


def fetch_query(query):
    """All UniProtKB entries matching a query, with metadata and sequence."""
    url = f"{UNIPROT}/uniprotkb/stream?query={requests.utils.quote(query)}&format=tsv&fields={META_FIELDS},sequence"
    return {row["Entry"]: meta_record(row) for row in parse_tsv(http_get(url))}


# ----------------------------------------------------------------------- PANTHER tree helpers
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


def smallest_node(root, leaf_ids):
    """Smallest internal node containing every leaf in `leaf_ids` (None if the set is empty)."""
    target = set(leaf_ids)
    if not target:
        return None
    best = None

    def walk(n):
        nonlocal best
        if target <= {x["persistent_id"] for x in leaves(n)}:
            best = n
            for c in kids(n):
                walk(c)
    walk(root)
    return best


def organism_leaf_ids(node, organism):
    return [x["persistent_id"] for x in leaves(node) if x.get("organism") == organism]


def tree_nodes(alpha, beta):
    """PANTHER node ids that the family reviews cite, read from the trees rather than typed in."""
    out = {}
    for fam, root, acc, label in ((ALPHA_FAMILY, alpha, "P53598", "LSC1"), (BETA_FAMILY, beta, Q["LSC2"], "LSC2")):
        pth = path_to(root, acc)
        out[f"{fam}_tree_root"] = node_record(root)
        out[f"{fam}_path_root_to_{label}"] = [node_record(n) for n in pth[:-1]] if pth else "leaf not found"
        tv = smallest_node(root, organism_leaf_ids(root, "Trichomonas vaginalis"))
        out[f"{fam}_Trichomonas_vaginalis_clade"] = node_record(tv) if tv is not None else None
    out[f"{BETA_FAMILY}_Xanthomonas_campestris_leaves"] = []
    for x in leaves(beta):
        if x.get("organism") == "Xanthomonas campestris":
            pth = path_to(beta, acc_of(x)) if acc_of(x) else None
            out[f"{BETA_FAMILY}_Xanthomonas_campestris_leaves"].append(
                {"leaf": x["persistent_id"], "accession": acc_of(x),
                 "parent_path": [node_record(n) for n in pth[-4:-1]] if pth else None})
    # the PAINT node, its parent and the parent's other children; the Paramecium genes in that parent
    pth = path_to(beta, Q["SUCLG2"])
    idx = next((i for i, n in enumerate(pth or []) if n.get("persistent_id") == PAINT_GDP_NODE), None)
    if idx:
        parent = pth[idx - 1]
        out[f"{BETA_FAMILY}_PAINT_GDP_node"] = node_record(pth[idx])
        out[f"{BETA_FAMILY}_PAINT_GDP_node_parent"] = node_record(parent)
        out[f"{BETA_FAMILY}_PAINT_GDP_node_sisters"] = [node_record(c) for c in kids(parent) if c is not pth[idx]]
        pt = smallest_node(parent, organism_leaf_ids(parent, "Paramecium tetraurelia"))
        if pt is not None:
            ptp = path_to(beta, acc_of(leaves(pt)[0]))
            j = next(i for i, n in enumerate(ptp) if n is pt)
            out[f"{BETA_FAMILY}_Paramecium_tetraurelia_clade_in_G_daughter"] = {
                "clade": node_record(pt), "leaves": [acc_of(x) for x in leaves(pt)],
                "path_from_G_daughter": [node_record(n) for n in ptp[ptp.index(parent):j]]}
    return out


# ------------------------------------------------------------------------------ position 20
class Pos20:
    """Residue homologous to E. coli SucC residue 20, read by pairwise local alignment."""

    def __init__(self, refs):
        self.al = PairwiseAligner(mode="local", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                                  open_gap_score=-11, extend_gap_score=-1)
        self.clean = lambda s: re.sub(r"[^ACDEFGHIKLMNPQRSTVWY]", "X", s.upper())
        ec = refs["EcSucC"]
        self.refs = {"EcSucC": (self.clean(ec), EC_POSITION - 1)}
        for name, seq in refs.items():
            if name != "EcSucC":
                _, j = self._map(self.clean(ec), EC_POSITION - 1, self.clean(seq))
                if j is None:
                    raise RuntimeError(f"reference {name} does not align over E. coli SucC position {EC_POSITION}")
                self.refs[name] = (self.clean(seq), j)

    def _map(self, ref, pos, seq):
        a = self.al.align(ref, seq)[0]
        for (rs, re_), (qs, _) in zip(*a.aligned):
            if rs <= pos < re_:
                return a.score, qs + (pos - rs)
        return a.score, None

    def reference_positions(self):
        return {k: f"{s[p]}{p + 1}" for k, (s, p) in self.refs.items()}

    def call(self, seq, pfam=None):
        """pfam: list of Pfam ids if known. Returns dict(residue, context, closest_reference, note)."""
        seq = self.clean(seq)
        best = max(((name,) + self._map(ref, pos, seq) for name, (ref, pos) in self.refs.items()), key=lambda t: t[1])
        name, _, j = best
        out = {"residue": None, "context": None, "closest_reference": name}
        if pfam is not None and ATP_GRASP_PFAM not in pfam:
            out["note"] = "no_ATP_grasp_domain"   # nothing homologous to position 20
        elif j is None:
            out["note"] = "position_not_covered"  # N-terminally truncated or too divergent
        else:
            out["residue"] = seq[j]
            out["context"] = seq[max(0, j - 4):j] + "[" + seq[j] + "]" + seq[j + 1:j + 4]
        return out


def tally(calls):
    c = Counter(x["residue"] or x.get("note", "none") for x in calls)
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))


# ------------------------------------------------------------------------------------ trees
class Distances:
    """BLOSUM62 dissimilarity 1 - score/max(self scores) over ungapped column pairs
    (the definition used by Biopython's DistanceCalculator('blosum62')), vectorised so
    that bootstrap replicates are column-weight vectors."""

    def __init__(self, rows):
        m = substitution_matrices.load("BLOSUM62")
        alpha = m.alphabet
        idx = {ch: i for i, ch in enumerate(alpha)}
        S = np.array([[m[a, b] for b in alpha] for a in alpha], dtype=np.float64)
        code = np.array([[idx.get(ch, idx["X"]) for ch in r] for r in rows])
        gap = np.array([[ch in "-*" for ch in r] for r in rows])
        n = len(rows)
        self.n = n
        self.iu = np.triu_indices(n, 1)
        a, b = self.iu
        valid = ~(gap[a] | gap[b])
        self.sab = np.where(valid, S[code[a], code[b]], 0.0)
        self.saa = np.where(valid, S[code[a], code[a]], 0.0)
        self.sbb = np.where(valid, S[code[b], code[b]], 0.0)

    def matrix(self, weights=None):
        w = np.ones(self.sab.shape[1]) if weights is None else weights
        score, mx = self.sab @ w, np.maximum(self.saa @ w, self.sbb @ w)
        d = np.where(mx > 0, 1 - score / np.where(mx > 0, mx, 1), 1.0)
        D = np.zeros((self.n, self.n))
        D[self.iu] = d
        return D + D.T


def neighbor_joining(names, D):
    """Standard neighbor joining. Returns an unrooted tree as nested nodes
    {'tips': frozenset, 'children': [(node, branch_length), ...]} (tips have 'name')."""
    D = D.copy()
    nodes = [{"tips": frozenset([nm]), "name": nm, "children": []} for nm in names]
    while len(nodes) > 3:
        n = len(nodes)
        r = D.sum(1)
        qm = (n - 2) * D - r[:, None] - r[None, :]
        np.fill_diagonal(qm, np.inf)
        i, j = sorted(np.unravel_index(np.argmin(qm), qm.shape))
        li = 0.5 * D[i, j] + (r[i] - r[j]) / (2 * (n - 2))
        new = {"tips": nodes[i]["tips"] | nodes[j]["tips"], "children": [(nodes[i], li), (nodes[j], D[i, j] - li)]}
        dn = 0.5 * (D[i] + D[j] - D[i, j])
        D[i, :] = dn
        D[:, i] = dn
        D[i, i] = 0.0
        D = np.delete(np.delete(D, j, 0), j, 1)
        nodes[i] = new
        del nodes[j]
    l0 = 0.5 * (D[0, 1] + D[0, 2] - D[1, 2])
    return {"tips": frozenset(names), "children": [(nodes[0], l0), (nodes[1], D[0, 1] - l0), (nodes[2], D[0, 2] - l0)]}


def rooted_clades(tipsets, alltips, outgroup):
    """Clades of the tree rooted on `outgroup`: for every internal branch, the side without the outgroup."""
    out = set()
    for st in tipsets:
        st = alltips - st if outgroup in st else st
        if 1 < len(st) < len(alltips) - 1:
            out.add(st)
    return out


def node_tipsets(node, root=True):
    out = [] if root else [node["tips"]]
    for c, _ in node["children"]:
        out.extend(node_tipsets(c, False))
    return out


def newick(node, label, digits=6):
    """Newick with an internal-node label from `label(tips)` (None for no label)."""
    def w(nd):
        if not nd["children"]:
            return nd["name"]
        lab = label(nd["tips"])
        return "(" + ",".join(f"{w(c)}:{ln:.{digits}f}" for c, ln in nd["children"]) + ")" + ("" if lab is None else str(lab))
    return "(" + ",".join(f"{w(c)}:{ln:.{digits}f}" for c, ln in node["children"]) + ");"


def smallest_clade(clades, names, alltips, outgroup):
    names = frozenset(names)
    hits = [c for c in clades if names <= c]
    return min(hits, key=len) if hits else alltips - {outgroup}


def triplet(clades, x, a, g):
    """Rooted triplet for tips x, a, g: which two are closer to each other than to the third."""
    xa = any(x in c and a in c and g not in c for c in clades)
    xg = any(x in c and g in c and a not in c for c in clades)
    ag = any(a in c and g in c and x not in c for c in clades)
    return "with_SUCLA2" if xa else "with_SUCLG2" if xg else "outside_both" if ag else "unresolved"


def run_ml(rows, model, seed, replicates):
    """IQ-TREE via piqtree, single thread and fixed seed. Returns (nested tree, {tipset: ufboot}, lnL)."""
    import cogent3
    import piqtree

    caln = cogent3.make_aligned_seqs(rows, moltype="protein")
    ml = piqtree.build_tree(caln, model, rand_seed=seed, bootstrap_replicates=replicates, num_threads=1)

    def support(nd):
        s = getattr(nd, "support", None)
        if s is None:
            s = getattr(nd, "params", {}).get("support")
        return None if s is None else float(s)

    def conv(nd):
        if nd.is_tip():
            return {"tips": frozenset([nd.name]), "name": nd.name, "children": [], "support": None}
        ch = [(conv(c), float(c.length or 0.0)) for c in nd.children]
        return {"tips": frozenset().union(*(c["tips"] for c, _ in ch)), "children": ch, "support": support(nd)}

    tree = conv(ml)
    sup = {}

    def collect(nd, root=True):
        if nd["children"] and not root:
            sup[nd["tips"]] = nd["support"]
        for c, _ in nd["children"]:
            collect(c, False)
    collect(tree)
    lnl = getattr(ml, "params", {}).get("lnL")
    return tree, sup, (None if lnl is None else float(lnl))


# ------------------------------------------------------------------------------------- main
def main():
    global CACHE_DIR
    ap = argparse.ArgumentParser()
    ap.add_argument("--bootstraps", type=int, default=100, help="neighbor-joining bootstrap replicates")
    ap.add_argument("--seed", type=int, default=1, help="seed for the NJ bootstrap and the first ML run")
    ap.add_argument("--ml-bootstraps", type=int, default=1000, help="ultrafast bootstraps for the ML trees; 0 skips them")
    ap.add_argument("--ml-model", default="LG+G4")
    ap.add_argument("--ml-runs", type=int, default=3, help="independent ML runs (seeds seed, seed+1, ...)")
    ap.add_argument("--ml-workers", type=int, default=4, help="ML runs executed in parallel (one thread each)")
    ap.add_argument("--out", default=str(Path(__file__).parent / "results.yaml"))
    ap.add_argument("--nodes-only", action="store_true",
                    help="only refresh the panther_tree_nodes section of an existing results file")
    ap.add_argument("--dump-alignment", default=None, help="also write the trimmed panel alignment (FASTA) to this path")
    ap.add_argument("--cache-dir", default=None, help="development aid: reuse downloaded responses from this directory")
    args = ap.parse_args()
    if args.cache_dir:
        CACHE_DIR = Path(args.cache_dir)
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    res: dict = {}

    # ---- 1. PANTHER trees ---------------------------------------------------------
    bver, beta = get_tree(BETA_FAMILY)
    aver, alpha = get_tree(ALPHA_FAMILY)
    res["panther_version"] = {"beta": bver, "alpha": aver}
    res["panther_tree_nodes"] = tree_nodes(alpha, beta)
    if args.nodes_only:
        merged = yaml.safe_load(Path(args.out).read_text())
        merged["panther_version"] = res["panther_version"]
        merged["panther_tree_nodes"] = res["panther_tree_nodes"]
        Path(args.out).write_text(yaml.safe_dump(merged, sort_keys=False, width=110))
        yaml.safe_dump(res["panther_tree_nodes"], sys.stdout, sort_keys=False, width=110)
        return

    dup = find(beta, BETA_EUK_DUPLICATION)
    gdp_leaves = {x["persistent_id"] for x in leaves(find(beta, PAINT_GDP_NODE))}
    # Name the daughter clades by content rather than by assumption.
    pclass, daughters = {}, []
    for dnode in kids(dup):
        accs = {acc_of(x) for x in leaves(dnode)}
        has_a, has_g = Q["SUCLA2"] in accs, Q["SUCLG2"] in accs
        name = "both" if has_a and has_g else "A_daughter" if has_a else "G_daughter" if has_g else "other_" + dnode["persistent_id"]
        daughters.append({"node": dnode["persistent_id"], "name": name, "contains": "human SUCLA2" if name == "A_daughter"
                          else "human SUCLG2" if name == "G_daughter" else None,
                          "n_leaves": len(leaves(dnode)), "subfamily": dnode.get("sf_id")})
        for x in leaves(dnode):
            pclass[x["persistent_id"]] = ("G_daughter_under_PAINT_GDP_node" if x["persistent_id"] in gdp_leaves
                                          else "G_daughter_outside_PAINT_GDP_node") if name == "G_daughter" else name
    for x in leaves(beta):
        pclass.setdefault(x["persistent_id"], "outside_eukaryotic_duplication")
    res["beta_eukaryotic_duplication"] = {"node": BETA_EUK_DUPLICATION, "event_type": dup.get("event_type"),
                                          "taxon": dup.get("species"), "daughters": daughters,
                                          "PAINT_GDP_node": {"node": PAINT_GDP_NODE, "n_leaves": len(gdp_leaves)}}
    beta_leaves = [x for x in leaves(beta) if acc_of(x)]
    leaf_of = {acc_of(x): x for x in beta_leaves}

    # ---- sequences and metadata for every PANTHER beta leaf, plus the extra accessions ----
    seqs, meta, unisave, missing = fetch_entries(list(leaf_of) + list(EXTRA_ACCESSIONS) + list(Q.values()))
    for k, acc in Q.items():
        if acc not in seqs:
            raise RuntimeError(f"reference {k} {acc} could not be fetched")
    p20 = Pos20({k: seqs[Q[k]] for k in ("EcSucC", "SUCLA2", "SUCLG2")})

    def call(acc):
        return p20.call(seqs[acc], meta[acc]["pfam"] if acc in meta else None)

    # organism -> major group, from the UniProt lineage of its leaves
    GROUPS = [("Fungi", {"Fungi"}), ("Metazoa-Choanoflagellata", {"Metazoa", "Choanoflagellata"}),
              ("Amoebozoa", {"Amoebozoa"}), ("Viridiplantae", {"Viridiplantae"}),
              ("Discoba-Metamonada", {"Discoba", "Metamonada"}), ("Alveolata", {"Alveolata"}),
              ("Stramenopiles", {"Stramenopiles"}), ("Archaea", {"Archaea"}), ("Bacteria", {"Bacteria"})]

    PANTHER_LABEL_GROUP = {"Fungi": "Fungi", "Metazoa-Choanoflagellida": "Metazoa-Choanoflagellata",
                           "Dictyostelium": "Amoebozoa", "Viridiplantae": "Viridiplantae",
                           "Excavates": "Discoba-Metamonada", "Alveolata": "Alveolata",
                           "Stramenopiles": "Stramenopiles", "Archaea": "Archaea", "Eubacteria": "Bacteria"}

    def group_of_lineage(lin):
        """Major group; a lineage outside the listed groups is named by its first rank below the domain."""
        return next((g for g, keys in GROUPS if keys & set(lin)), lin[2] if len(lin) > 2 else "unclassified")
    org_group, fallback = {}, []
    for x in beta_leaves:
        a = acc_of(x)
        if a in meta:
            org_group.setdefault(x["organism"], group_of_lineage(meta[a]["lineage"]))
    for x in beta_leaves:  # organisms whose leaves are all deleted UniProt entries: use the PANTHER node labels
        if x["organism"] not in org_group:
            labels = [n.get("species") for n in reversed(path_to(beta, acc_of(x)))]
            org_group[x["organism"]] = next((PANTHER_LABEL_GROUP[lb] for lb in labels if lb in PANTHER_LABEL_GROUP), "unclassified")
            fallback.append(x["organism"])
    census = defaultdict(Counter)
    for x in leaves(beta):
        census[x["organism"]][pclass[x["persistent_id"]]] += 1
    for x in leaves(alpha):
        census[x["organism"]]["alpha"] += 1
    summary, per_org = defaultdict(Counter), {}
    for org, c in sorted(census.items()):
        if not any(k != "alpha" for k in c):
            continue  # organism only in the alpha tree
        a = c.get("A_daughter", 0)
        gu, go = c.get("G_daughter_under_PAINT_GDP_node", 0), c.get("G_daughter_outside_PAINT_GDP_node", 0)
        m = org_group.get(org, "unclassified")
        state = "A_and_G" if a and gu + go else "A_only" if a else "G_only" if gu + go else "neither"
        summary[m][state] += 1
        per_org[org] = {"group": m, "state": state, "beta_A_daughter": a, "beta_G_daughter_under_PAINT_GDP_node": gu,
                        "beta_G_daughter_outside_PAINT_GDP_node": go,
                        "beta_outside_duplication": c.get("outside_eukaryotic_duplication", 0), "alpha": c.get("alpha", 0)}
    res["beta_paralog_census_note"] = ("A/G are the two daughter clades of the PANTHER duplication node, i.e. PANTHER's "
                                       "placement, not a statement about nucleotide specificity. Groups are UniProt lineages.")
    res["beta_paralog_census_organisms_grouped_by_PANTHER_label"] = sorted(fallback)
    res["beta_paralog_census_by_group"] = {k: dict(v) for k, v in sorted(summary.items())}
    res["beta_paralog_census_fungi"] = {o: v for o, v in per_org.items() if v["group"] == "Fungi"}
    res["beta_paralog_census_A_and_G_outside_animals"] = {
        o: v for o, v in per_org.items() if v["state"] == "A_and_G" and v["group"] != "Metazoa-Choanoflagellata"}
    res["beta_paralog_census_exceptions"] = {
        o: v for o, v in per_org.items()
        if (v["group"] == "Fungi" and v["state"] != "A_only")
        or (v["group"] == "Metazoa-Choanoflagellata" and v["state"] != "A_and_G")
        or (v["group"] in ("Bacteria", "Archaea") and v["state"] != "neither")}
    res["beta_paralog_census_selected"] = {o: per_org[o] for o in PANEL_ORGANISMS if o in per_org}
    res["clade_membership"] = {
        k: {"accession": acc, "panther_class": pclass[leaf_of[acc]["persistent_id"]] if acc in leaf_of else "not_in_panther_tree",
            "panther_subfamily": (leaf_of[acc].get("prop_sf_id") or leaf_of[acc].get("sf_id")) if acc in leaf_of else None}
        for k, acc in Q.items()}
    # leaves whose PANTHER definition does not name succinate-CoA ligase, per family
    res["non_scs_named_leaves"] = {
        fam: sorted(f'{x["organism"]} {acc_of(x)}: {x.get("definition")}' for x in leaves(root)
                    if x.get("definition") and not re.search(r"[Ss]uccin", x["definition"]))
        for fam, root in ((BETA_FAMILY, beta), (ALPHA_FAMILY, alpha))}

    # ---- 2a. position 20 across every PANTHER beta leaf -----------------------------------
    by_class, by_class_domain, leaf_calls = defaultdict(list), defaultdict(list), {}
    for acc, x in leaf_of.items():
        if acc not in seqs:
            continue
        c = call(acc)
        leaf_calls[acc] = c
        cls = pclass[x["persistent_id"]]
        by_class[cls].append(c)
        dom = meta[acc]["lineage"][1] if acc in meta and len(meta[acc]["lineage"]) > 1 else "unknown"
        by_class_domain[f"{cls} / {dom}"].append(c)

    def leaf_row(acc):
        x, c = leaf_of[acc], leaf_calls[acc]
        return {"accession": acc, "organism": x["organism"], "leaf": x["persistent_id"],
                "residue": c["residue"] or c.get("note"), "context": c["context"],
                "protein_name": meta.get(acc, {}).get("protein_name") or x.get("definition"),
                "pfam": meta.get(acc, {}).get("pfam")}
    res["position20_panther_leaves"] = {
        "method": "residue aligned to E. coli SucC residue %d in a pairwise local alignment (BLOSUM62, gap open 11, "
                  "extend 1) with the best-scoring of three references; 'no_ATP_grasp_domain' = protein lacks Pfam %s; "
                  "'position_not_covered' = alignment does not reach the position" % (EC_POSITION, ATP_GRASP_PFAM),
        "reference_residues": p20.reference_positions(),
        "n_leaves": len(leaf_of), "n_sequences": len(leaf_calls),
        "from_unisave_last_version": [a for a in unisave if a in leaf_of],
        "not_retrievable": [a for a in missing if a in leaf_of],
        "by_panther_class": {k: {"n": len(v), "residues": tally(v)} for k, v in sorted(by_class.items())},
        "by_panther_class_and_domain": {k: {"n": len(v), "residues": tally(v)} for k, v in sorted(by_class_domain.items())},
        "Gln_leaves_outside_PAINT_GDP_node": [leaf_row(a) for a in leaf_calls if leaf_calls[a]["residue"] == "Q"
                                              and pclass[leaf_of[a]["persistent_id"]] != "G_daughter_under_PAINT_GDP_node"],
        "non_Gln_leaves_under_PAINT_GDP_node": [leaf_row(a) for a in leaf_calls if leaf_calls[a]["residue"] != "Q"
                                                and pclass[leaf_of[a]["persistent_id"]] == "G_daughter_under_PAINT_GDP_node"],
        "eukaryotic_duplication_leaves_with_neither_Pro_nor_Gln": [
            f'{a} {leaf_of[a]["organism"]} [{pclass[leaf_of[a]["persistent_id"]]}]: {leaf_calls[a]["residue"] or leaf_calls[a].get("note")}'
            for a in leaf_calls if leaf_calls[a]["residue"] not in ("P", "Q")
            and pclass[leaf_of[a]["persistent_id"]] != "outside_eukaryotic_duplication"],
    }

    # ---- 2b. UniProt-wide census of the family in fungi and in other eukaryotes ------------
    def uniprot_census(query, group_fn):
        ent = fetch_query(query)
        kept, dropped = {}, Counter()
        for acc, m in ent.items():
            if CITRATE_LYASE_PFAM & set(m["pfam"]):
                dropped["ATP-citrate lyase domains"] += 1
            elif ATP_GRASP_PFAM not in m["pfam"]:
                dropped["no ATP-grasp domain (fragment or beta-like protein)"] += 1
            else:
                kept[acc] = dict(m, call=p20.call(m["sequence"], m["pfam"]), group=group_fn(m))
        groups = defaultdict(list)
        for acc, m in kept.items():
            groups[m["group"]].append(acc)
        by_group = {}
        for g, accs in sorted(groups.items()):
            sp = defaultdict(set)
            for a in accs:
                sp[kept[a]["organism_id"]].add(kept[a]["call"]["residue"])
            sf = Counter(";".join(p.split(":")[1] for p in kept[a]["panther"] if ":" in p) or "none"
                         for a in accs if kept[a]["call"]["residue"] == "Q")
            by_group[g] = {"entries": len(accs), "residues": tally([kept[a]["call"] for a in accs]),
                           "Gln20_entries_by_PANTHER_subfamily": dict(sorted(sf.items())),
                           "organisms": len(sp), "organisms_with_Gln20_gene": sum("Q" in v for v in sp.values()),
                           "organisms_with_Gln20_and_Pro20_genes": sum({"Q", "P"} <= v for v in sp.values())}
        gln = [{"accession": a, "organism": m["organism"], "group": m["group"], "context": m["call"]["context"],
                "closest_reference": m["call"]["closest_reference"],
                "panther": [p for p in m["panther"] if ":" in p], "protein_name": m["protein_name"]}
               for a, m in sorted(kept.items(), key=lambda kv: (kv[1]["group"], kv[1]["organism"])) if m["call"]["residue"] == "Q"]
        return ent, kept, {"query": query, "n_entries": len(ent), "n_beta_subunits_with_ATP_grasp_domain": len(kept),
                           "excluded": dict(dropped), "residues_overall": tally([m["call"] for m in kept.values()]),
                           "by_group": by_group, "Gln20_entries": gln}

    fung_all, fung, fc = uniprot_census(f"(xref:panther-{BETA_FAMILY}) AND (taxonomy_id:4751)",
                                        lambda m: m["phylum"] or "Fungi, no phylum rank")
    fc["note"] = ("group = phylum; an organism is one UniProt taxon id, so strains count separately; "
                  "'Gln20' is the residue only, no enzyme in this census has been assayed")
    fc["reference_yeast_entries"] = {
        name: [f'{a}: {m["protein_name"]} | Pfam {";".join(m["pfam"])} | position 20 '
               f'{(p20.call(m["sequence"], m["pfam"])["residue"] or "none") if not CITRATE_LYASE_PFAM & set(m["pfam"]) else "n/a (ATP-citrate lyase)"}'
               for a, m in sorted(fung_all.items()) if m["organism_id"] == tid]
        for name, tid in (("Saccharomyces cerevisiae S288c (taxon 559292)", "559292"),
                          ("Schizosaccharomyces pombe 972h- (taxon 284812)", "284812"))}
    res["fungal_uniprot_census"] = fc
    _, _, pc = uniprot_census(
        f"(xref:panther-{BETA_FAMILY}) AND (taxonomy_id:2759) NOT (taxonomy_id:4751) NOT (taxonomy_id:33208) NOT (taxonomy_id:33090)",
        lambda m: " > ".join(m["lineage"][2:4]) or "unplaced")
    pc["note"] = "eukaryotes other than Fungi, Metazoa and Viridiplantae; group = first two lineage names below Eukaryota"
    res["other_eukaryote_uniprot_census"] = pc

    # ---- 3. panel ------------------------------------------------------------------------
    panel = {}
    for acc, x in leaf_of.items():
        if x["organism"] in PANEL_ORGANISMS:
            panel[acc] = "PANTHER leaf of a panel organism"
    for acc, why in EXTRA_ACCESSIONS.items():
        panel[acc] = why
    panel_missing = sorted(a for a in panel if a not in seqs)
    ids = [a for a in panel if a in seqs]

    def info(acc):
        m, c = meta.get(acc, {}), call(acc)
        org = m.get("organism") or leaf_of[acc]["organism"]
        return {"organism": re.sub(r" \(.*", "", org), "group": group_of_lineage(m.get("lineage", [])),
                "panther_class": pclass[leaf_of[acc]["persistent_id"]] if acc in leaf_of else "not_in_panther_tree",
                "position20": c["residue"] or c.get("note"), "context": c["context"],
                "has_ATP_grasp_domain": ATP_GRASP_PFAM in m["pfam"] if m else None,
                "protein_name": m.get("protein_name"), "gene_names": m.get("gene_names"), "length": len(seqs[acc]),
                "in_panel_because": panel[acc]}
    pinfo = {a: info(a) for a in ids}
    res["panel"] = {"n_requested": len(panel), "n_fetched": len(ids), "missing": panel_missing,
                    "extra_accessions_in_panther_tree": sorted(a for a in EXTRA_ACCESSIONS if a in leaf_of),
                    "members": {a: pinfo[a] for a in sorted(ids, key=lambda a: (pinfo[a]["panther_class"], pinfo[a]["group"], pinfo[a]["organism"]))}}

    msa = Aligner().align([Sequence(a.encode(), seqs[a].encode()) for a in ids])
    aln = {m.id.decode(): m.sequence.decode() for m in msa}
    ids = [a for a in ids if a in aln]
    ncol = len(aln[ids[0]])

    def trimmed(members):
        """Rows for `members`, keeping columns with <50% gaps among them (drops transit peptides and extensions)."""
        cols = [i for i in range(ncol) if sum(aln[a][i] == "-" for a in members) < 0.5 * len(members)]
        return {a: "".join(aln[a][i] for i in cols) for a in members}, len(cols)

    rows, nkeep = trimmed(ids)
    if args.dump_alignment:
        Path(args.dump_alignment).write_text("".join(f">{a}\n{rows[a]}\n" for a in ids))
    res["alignment"] = {"program": "FAMSA (pyfamsa)", "n_sequences": len(ids), "n_columns": ncol, "n_columns_used": nkeep}

    # position 20 read from the alignment column, as a check on the pairwise call
    def col_of(acc, pos):
        n = 0
        for i, ch in enumerate(aln[acc]):
            if ch != "-":
                n += 1
                if n == pos:
                    return i
        raise ValueError(pos)
    c20 = col_of(Q["EcSucC"], EC_POSITION)
    disagree = {a: {"pairwise": pinfo[a]["position20"], "alignment_column": aln[a][c20]} for a in ids
                if pinfo[a]["has_ATP_grasp_domain"] is not False and aln[a][c20] != pinfo[a]["position20"]}
    res["position20_panel"] = {
        "by_panther_class_and_group": {},
        "pairwise_call_differs_from_alignment_column": disagree,
        "proteins_without_ATP_grasp_domain": {a: {"organism": pinfo[a]["organism"], "protein_name": pinfo[a]["protein_name"],
                                                  "gene_names": pinfo[a]["gene_names"], "length": pinfo[a]["length"],
                                                  "panther_class": pinfo[a]["panther_class"]}
                                              for a in ids if pinfo[a]["has_ATP_grasp_domain"] is False}}
    for a, rec in res["position20_panel"]["proteins_without_ATP_grasp_domain"].items():
        # alpha-subunit tree leaves of the same organism, with their gene names (is the beta-like gene next to an alpha-like one?)
        al = [x for x in leaves(alpha) if a in leaf_of and x.get("organism") == leaf_of[a]["organism"] and acc_of(x)]
        _, ameta, _, _ = fetch_entries([acc_of(x) for x in al]) if al else ({}, {}, [], [])
        rec["alpha_tree_leaves_of_same_organism"] = [
            {"accession": acc_of(x), "leaf": x["persistent_id"], "panther_definition": x.get("definition"),
             "gene_names": ameta.get(acc_of(x), {}).get("gene_names")} for x in al]
    grp = defaultdict(list)
    for a in ids:
        grp[f'{pinfo[a]["panther_class"]} / {pinfo[a]["group"]}'].append(a)
    for k, accs in sorted(grp.items()):
        res["position20_panel"]["by_panther_class_and_group"][k] = {
            "n": len(accs), "residues": dict(Counter(str(pinfo[a]["position20"]) for a in accs).most_common()),
            "members": [f'{a} {pinfo[a]["organism"]} {pinfo[a]["position20"]}' for a in accs]}

    # ---- 3a. tip sets the tree tests are phrased in --------------------------------------
    ec = Q["EcSucC"]
    alltips = frozenset(ids)

    def members_of(pred):
        return sorted(a for a in ids if pred(pinfo[a]))
    euk = members_of(lambda p: p["group"] not in ("Bacteria", "Archaea"))
    gln_euk = [a for a in euk if pinfo[a]["position20"] == "Q"]
    fungal_gln = [a for a in gln_euk if pinfo[a]["group"] == "Fungi"]
    fungal_pro = members_of(lambda p: p["group"] == "Fungi" and p["position20"] == "P")
    gln_species = {pinfo[a]["organism"] for a in fungal_gln}
    partners = [a for a in fungal_pro if pinfo[a]["organism"] in gln_species]
    no_grasp = members_of(lambda p: p["has_ATP_grasp_domain"] is False)

    def pick(pred):
        return next(iter(members_of(pred)), None)
    arab = pick(lambda p: p["organism"].startswith("Arabidopsis"))
    dictyA = pick(lambda p: p["organism"].startswith("Dictyostelium") and p["panther_class"] == "A_daughter")
    dictyG = pick(lambda p: p["organism"].startswith("Dictyostelium") and p["panther_class"].startswith("G_"))
    paraG = members_of(lambda p: p["organism"].startswith("Paramecium") and p["panther_class"].startswith("G_"))
    blasto = pick(lambda p: p["organism"].startswith("Blastocystis"))
    sets = {
        "LSC2 + human SUCLA2": [Q["LSC2"], Q["SUCLA2"]],
        "LSC2 + S. pombe beta": [Q["LSC2"], Q["SpBeta"]],
        "human SUCLG2 + pig SUCLG2": [Q["SUCLG2"], Q["pigG"]],
        "LSC2 + human SUCLG2": [Q["LSC2"], Q["SUCLG2"]],
        "all eukaryotic Gln20 subunits": gln_euk,
    }
    if dictyG:
        sets["human SUCLG2 + Dictyostelium Gln20 beta"] = [Q["SUCLG2"], dictyG]
    if dictyA:
        sets["human SUCLA2 + Dictyostelium Pro20 beta"] = [Q["SUCLA2"], dictyA]
    if fungal_gln:
        sets["fungal Gln20 genes"] = fungal_gln
        sets["human SUCLG2 + fungal Gln20 genes"] = [Q["SUCLG2"]] + fungal_gln
    if partners:
        sets["LSC2 + human SUCLA2 + Pro20 genes of the fungi that also have a Gln20 gene"] = [Q["LSC2"], Q["SUCLA2"]] + partners
    if paraG:
        sets["Paramecium Gln20 genes"] = paraG
        sets["human SUCLG2 + Paramecium Gln20 genes"] = [Q["SUCLG2"]] + paraG
    if blasto:
        sets["human SUCLG2 + Blastocystis beta"] = [Q["SUCLG2"], blasto]
    if arab:
        sets["Arabidopsis beta + human SUCLA2"] = [arab, Q["SUCLA2"]]
        sets["Arabidopsis beta + human SUCLG2"] = [arab, Q["SUCLG2"]]
    for a in no_grasp:
        sets[f"{a} (no ATP-grasp domain) + LSC2"] = [a, Q["LSC2"]]
        sets[f"{a} (no ATP-grasp domain) + human SUCLG2"] = [a, Q["SUCLG2"]]
    res["tree_test_tip_sets"] = {k: v for k, v in sets.items()}

    def describe(clades, names, tips, support):
        present = [n for n in names if n in tips]
        if len(present) < len(names) or len(present) < 2:
            return "not evaluated (tip absent from this tree)"
        c = smallest_clade(clades, present, tips, ec)
        comp = Counter(str(pinfo[m]["position20"]) for m in c)
        out = {"n_tips": len(c), "is_exactly_the_named_tips": c == frozenset(present),
               "position20_of_members": dict(comp.most_common()),
               "contains_human_SUCLA2": Q["SUCLA2"] in c, "contains_human_SUCLG2": Q["SUCLG2"] in c,
               "members_by_group": dict(sorted(Counter(pinfo[m]["group"] for m in c).items()))}
        out.update(support(c))
        out["members"] = sorted(f'{m} {pinfo[m]["organism"]} [{pinfo[m]["position20"]}]' for m in c)
        return out

    def placements(clades, tips):
        return {x: triplet(clades, x, Q["SUCLA2"], Q["SUCLG2"]) for x in euk
                if x in tips and x not in (Q["SUCLA2"], Q["SUCLG2"])}

    def by_group(per_tip):
        """Summarise per-tip placements by organism group and position-20 residue."""
        g = defaultdict(Counter)
        for x, r in per_tip.items():
            g[f'{pinfo[x]["group"]} / position 20 {pinfo[x]["position20"]}'][r] += 1
        return {k: dict(v) for k, v in sorted(g.items())}

    # ---- 3b. neighbor joining with clade bootstrap -----------------------------------------
    dist = Distances([rows[a] for a in ids])
    ref = neighbor_joining(ids, dist.matrix())
    # self-check of the vectorised distance and NJ code against Biopython on the full alignment
    from Bio.Align import MultipleSeqAlignment
    from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
    bdm = DistanceCalculator("blosum62").get_distance(MultipleSeqAlignment([SeqRecord(Seq(rows[a]), id=a) for a in ids]))
    bmat = np.array([[bdm[a, b] for b in ids] for a in ids])
    btree = DistanceTreeConstructor().nj(bdm)
    bsplits = rooted_clades([frozenset(t.name for t in c.get_terminals()) for c in btree.get_nonterminals()], frozenset(ids), Q["EcSucC"])
    ref_clades = rooted_clades(node_tipsets(ref), alltips, ec)
    clade_count, trip_count = Counter(), {x: Counter() for x in placements(ref_clades, alltips)}
    for _ in range(args.bootstraps):
        w = np.bincount(rng.integers(0, nkeep, nkeep), minlength=nkeep).astype(float)
        bc = rooted_clades(node_tipsets(neighbor_joining(ids, dist.matrix(w))), alltips, ec)
        clade_count.update(bc)
        for x, r in placements(bc, alltips).items():
            trip_count[x][r] += 1

    def canon(st):
        return alltips - st if ec in st else st

    def nj_support(c):
        return {"nj_clade_bootstrap": f"{clade_count[c]}/{args.bootstraps}"}
    nj_place = placements(ref_clades, alltips)
    res["neighbor_joining"] = {
        "method": "neighbor joining on BLOSUM62 dissimilarities (uncorrected), %d column-bootstrap replicates, seed %d; "
                  "clades read with the tree rooted on E. coli SucC; nj_clade_bootstrap = number of replicates that "
                  "contain exactly that clade" % (args.bootstraps, args.seed),
        "distances_match_biopython": bool(np.allclose(bmat, dist.matrix(), atol=1e-9)),
        "reference_topology_matches_biopython_nj": bsplits == ref_clades,
        "n_internal_branches_shorter_than_0.01": sum(1 for n in _internal(ref) for c, ln in n["children"] if c["children"] and ln < 0.01),
        "smallest_clade_containing": {k: describe(ref_clades, v, alltips, nj_support) for k, v in sets.items()},
        "placement_relative_to_SUCLA2_and_SUCLG2": {
            "note": "rooted triplet (X, human SUCLA2, human SUCLG2) in the tree rooted on E. coli SucC, i.e. the "
                    "outgroup-anchored quartet; bootstrap = number of replicates with each resolution",
            "by_group_reference_tree": by_group(nj_place),
            "per_tip": {x: {"organism": pinfo[x]["organism"], "position20": pinfo[x]["position20"],
                            "panther_class": pinfo[x]["panther_class"], "reference_tree": nj_place[x],
                            "bootstrap": dict(trip_count[x].most_common())} for x in nj_place}},
    }
    Path(args.out).with_name("beta_panel_nj.nwk").write_text(
        newick(ref, lambda t: None if len(canon(t)) < 2 else round(100 * clade_count[canon(t)] / max(args.bootstraps, 1))) + "\n")

    # ---- 3c. maximum likelihood --------------------------------------------------------------
    if args.ml_bootstraps:
        from concurrent.futures import ProcessPoolExecutor
        from importlib.metadata import version
        import multiprocessing as mp

        seeds = [args.seed + i for i in range(args.ml_runs)]
        jobs = [(rows, args.ml_model, s, args.ml_bootstraps) for s in seeds]
        sub = [a for a in ids if a not in no_grasp]
        if no_grasp:  # sensitivity: without proteins that lack the ATP-grasp domain (half-length, long branches)
            srows, scols = trimmed(sub)
            jobs.append((srows, args.ml_model, seeds[0], args.ml_bootstraps))
        with ProcessPoolExecutor(max_workers=min(len(jobs), args.ml_workers), mp_context=mp.get_context("spawn")) as ex:
            out = list(ex.map(run_ml, *zip(*jobs)))
        runs = [(t, sup, rooted_clades(sup, alltips, ec), lnl) for t, sup, lnl in out[:len(seeds)]]
        best = max(range(len(runs)), key=lambda i: (runs[i][3] is not None, runs[i][3] or 0.0, -i))
        tree0, sup0, clades0, _ = runs[best]

        def run_support(run, c):
            _, sup, cl, _ = run
            return sup.get(c if c in sup else alltips - c) if c in cl else None

        def ml_support(c):
            vals = [run_support(r, c) for r in runs]
            return {"ufboot_by_run": {f"seed{s}": ("clade absent" if v is None else v) for s, v in zip(seeds, vals)},
                    "ufboot_min": min((v or 0.0) for v in vals), "ufboot_max": max((v or 0.0) for v in vals),
                    "nj_clade_bootstrap": f"{clade_count[c]}/{args.bootstraps}"}
        ml_place = placements(clades0, alltips)
        per_run_place = [placements(cl, alltips) for _, _, cl, _ in runs]
        res["maximum_likelihood"] = {
            "method": f"IQ-TREE (piqtree {version('piqtree')}, cogent3 {version('cogent3')}), model {args.ml_model} (fixed, no "
                      f"model selection), {args.ml_bootstraps} ultrafast bootstraps, one thread per run, {len(seeds)} independent "
                      f"runs with rand_seed {seeds}; same trimmed alignment as the NJ analysis; clades read with the tree rooted "
                      "on E. coli SucC. Clades are those of the run with the highest log-likelihood; ufboot_min/ufboot_max = "
                      "lowest and highest ultrafast bootstrap of that clade over the runs (0 where a run lacks the clade)",
            "reproducibility_note": "piqtree passes rand_seed to IQ-TREE, but in this version two runs with the same seed do "
                                    "not give identical trees or supports, so supports are reported as a range over runs and "
                                    "will differ by a few points on rerun; the NJ clade bootstrap is exactly reproducible",
            "log_likelihood_by_run": {f"seed{s}": r[3] for s, r in zip(seeds, runs)},
            "tree_written_from_run": f"seed{seeds[best]}",
            "same_topology_in_all_runs": all(r[2] == clades0 for r in runs),
            "n_clades_differing_from_written_tree": {f"seed{s}": len(r[2] ^ clades0) for s, r in zip(seeds, runs)},
            "smallest_clade_containing": {k: describe(clades0, v, alltips, ml_support) for k, v in sets.items()},
            "placement_relative_to_SUCLA2_and_SUCLG2": {
                "note": "same rooted-triplet reading as for NJ, in the ML tree of each run",
                "by_group_written_tree": by_group(ml_place),
                "tips_placed_differently_between_runs": sorted(x for x in ml_place if len({pp[x] for pp in per_run_place}) > 1),
                "per_tip": {x: {"organism": pinfo[x]["organism"], "position20": pinfo[x]["position20"],
                                "panther_class": pinfo[x]["panther_class"],
                                **{f"seed{s}": pp[x] for s, pp in zip(seeds, per_run_place)}}
                            for x in ml_place}},
        }
        Path(args.out).with_name("beta_panel_ml.nwk").write_text(
            newick(tree0, lambda t: None if len(canon(t)) < 2 else f"{min((run_support(r, canon(t)) or 0.0) for r in runs):g}",
                   digits=4) + "\n")

        if no_grasp:
            stips = frozenset(sub)
            _, ssup, slnl = out[-1]
            sclades = rooted_clades(ssup, stips, ec)

            def s_support(c):
                return {"ufboot": ssup.get(c if c in ssup else stips - c)}
            splace = placements(sclades, stips)
            res["maximum_likelihood_without_proteins_lacking_ATP_grasp_domain"] = {
                "removed": no_grasp, "n_sequences": len(sub), "n_columns_used": scols, "seed": seeds[0],
                "log_likelihood": slnl, "runs": 1,
                "smallest_clade_containing": {k: describe(sclades, v, stips, s_support) for k, v in sets.items()
                                              if not set(v) & set(no_grasp)},
                "placement_by_group": by_group(splace),
                "per_tip_placement_changed": {x: {"with": ml_place[x], "without": r} for x, r in splace.items() if ml_place[x] != r},
            }

    # ---- 4. pairwise identities -------------------------------------------------------------
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


def _internal(node):
    if node["children"]:
        yield node
        for c, _ in node["children"]:
            yield from _internal(c)


if __name__ == "__main__":
    main()
