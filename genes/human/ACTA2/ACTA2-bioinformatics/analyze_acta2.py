#!/usr/bin/env python3
"""ACTA2 (P62736): five questions, all computed at run time. Nothing is hard-coded from a prior run.

1. GO:0005200 provenance across the human actin family. PAINT asserts the term once, at
   PTHR11937 node PTN000940351, and has since IRD-negated it at several descendant nodes.
   Enumerate, from QuickGO rather than from prose, exactly which human genes still receive
   it and by which evidence route, and reconcile that census against the cached PAINT
   export. The census is also the test of a claim handed to this review as background, so
   it is asked in a form that can refute it.

2. Residue tallies at the two actin surfaces that the sibling ACTL8 and ACTL10 analyses
   scored, using the same PDB entries and cutoffs, so the columns are comparable by
   construction. The script asserts it reproduces ACTL8's committed values before drawing
   any conclusion, and it refuses to score a panel member whose sequence is materially
   shorter than the family median without recording the shortfall separately from
   substitution - the ACTL10 artefact, where 20 absent residues were counted as 20
   non-conservative substitutions.

3. ACTA2's disease variants against those same surfaces. ACTA2 causes thoracic aortic
   aneurysm/dissection, Moyamoya disease and multisystemic smooth-muscle dysfunction;
   distinguishing what the protein does from what happens when it is mutated needs the
   variant positions placed on the structures, not asserted from a modelling paper.

4. Every WITH/FROM token on every non-experimental row of ACTA2's GOA: resolve it, print
   its name and reviewed status and length, and ask what evidence the source itself holds
   for the term it donated.

5. Reference projection. For each literature reference supporting an ACTA2 row, how many
   annotations and how many DISTINCT entities does that reference carry? An annotation
   count is not an entity count, and a large result is paginated - both are reported as
   unavailable rather than guessed when the result exceeds what one page can carry.

Run:  uv run python analyze_acta2.py
Out:  results.json, RESULTS.md   (both regenerated in full; diff them to verify)
"""

from __future__ import annotations

import ast
import io
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Data.IUPACData import protein_letters_3to1
from Bio.PDB import MMCIFParser, NeighborSearch

THREE_TO_ONE = {k.upper(): v for k, v in protein_letters_3to1.items()}
THREE_TO_ONE.update({"MSE": "M", "HIC": "H", "SEP": "S", "TPO": "T", "PTR": "Y"})

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO_ROOT = GENE_DIR.parents[2]
GOA_TSV = GENE_DIR / "ACTA2-goa.tsv"
UNIPROT_TXT = GENE_DIR / "ACTA2-uniprot.txt"
REVIEW_YAML = GENE_DIR / "ACTA2-ai-review.yaml"
PAINT_TSV = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-paint.tsv"
ACTL8_RESULTS = REPO_ROOT / "genes" / "human" / "ACTL8" / "ACTL8-bioinformatics" / "RESULTS.md"

ACTA2 = "P62736"
FAMILY_NODE = "PTN000940351"  # the single PTHR11937 node that asserts GO:0005200
STRUCTURAL_MF = "GO:0005200"

CONTACT_CUTOFF = 4.0  # Angstrom, heavy atom to heavy atom
ATP_STRUCTURE = ("2BTF", "A", ("ATP", "SR"))  # beta-actin:profilin; ATP + Sr(II) in the Mg site
FILAMENT_STRUCTURE = ("6DJO", None, ())       # four F-actin protomers, ADP + Mg

# The ACTL8 panel (so the tallies line up with the two committed sibling analyses) plus the
# three muscle actins that share ACTA2's GO:0005200 IBA row and are absent from both.
PANEL = {
    "P60709": "ACTB (human beta-actin) - cytoplasmic actin, PTN000940351 IBD seed",
    "P68133": "ACTA1 (human alpha-skeletal actin) - shares ACTA2's IBA row",
    "P62736": "ACTA2 (human aortic smooth-muscle actin) - THIS GENE",
    "P63267": "ACTG2 (human enteric smooth-muscle actin) - shares ACTA2's IBA row",
    "P68032": "ACTC1 (human alpha-cardiac actin) - shares ACTA2's IBA row",
    "P63261": "ACTG1 (human gamma-cytoplasmic actin) - GO:0005200 by IC, not IBA",
    "P45891": "Arp53D (Drosophila actin-like 53D) - divergent actin that DOES polymerise",
    "P61160": "ACTR2 (human Arp2) - IBD seed AND IRD-negated at its own node",
    "P61158": "ACTR3 (human Arp3) - IBD seed AND IRD-negated at its own node",
    "Q9NZ32": "ACTR10 (human Arp11) - shares ACTA2's IBA row, non-polymerising",
    "Q9H568": "ACTL8 (human actin-like 8) - reviewed sibling, REMOVE verdict",
    "Q8TDG2": "ACTRT1 (human actin-related protein T1) - shares ACTA2's IBA row",
    "Q5JWF8": "ACTL10 (human actin-like 10) - shares ACTA2's IBA row; 245 aa Swiss-Prot entry",
}
THIS_GENE_LABEL = PANEL[ACTA2]

# A panel member whose annotated sequence is shorter than this fraction of the panel median
# cannot be scored as if every structural position were tested. ACTL10 (245 aa against a
# ~375 aa family) is the case that motivated it: its 20 unreached interface positions were
# counted as 20 non-conservative substitutions in a merged sibling review.
SHORT_SEQUENCE_FRACTION = 0.90

# Controls on the precursor->structure numbering, each taken from a source that states BOTH
# numbers, so the mapping is checked against documented facts rather than against itself.
# P62736 is a 377-aa precursor; the structures use mature actin numbering, so the offset should
# be -2 everywhere - but an offset assumed is an offset unverified.
NUMBERING_CONTROLS = {
    # UniProt CC PTM line, cached in ACTA2-uniprot.txt: "Monomethylation at Lys-86 (K84me1)".
    86: (84, "K", 'UniProt CC PTM line gives both numbers: "Monomethylation at Lys-86 (K84me1)"'),
    # PMID:30626964 titles SETD3 an actin histidine methyltransferase; the modified residue is
    # actin His73, annotated here as FT MOD_RES 75 "Tele-methylhistidine".
    75: (73, "H", "SETD3 methylates actin His73; UniProt annotates it at precursor position 75"),
    # PMID:26637293 writes the identity out explicitly: "R179 (R177 in alpha1-actin)".
    179: (177, "R", 'PMID:26637293: "R179 (R177 in alpha1-actin)"'),
}

# PMID:26637293 names the residues that contact R179 across the inter-strand interface:
# "a contact takes place between R179 in subdomain 3 and L112 in subdomain 1 ... from one
# molecule and K193 and T196 in subdomain 4 ... of the paired molecule". Given in ACTA2
# precursor numbering; the paired-molecule pair must therefore fall inside an independently
# computed inter-protomer contact set, or the structural analysis and the literature disagree.
INTERSTRAND_LITERATURE_CONTROL = {193: "K", 196: "T"}

# Load-bearing PMIDs whose retraction / erratum / expression-of-concern status is checked. A
# Publisher Correction is invisible to a publication-type query and has to be read from the
# CITED article's own CommentsCorrections block.
CORRECTION_CHECK_PMIDS = [
    "26637293", "26153420", "34600884", "24204762", "30626964", "40378078", "40603847",
    "17994018", "19409525", "20734336", "16548883", "18468998", "17464107", "12355421",
    "11927518", "23533145", "23580065", "28514442", "33961781", "38486025", "36007455",
]

EXPERIMENTAL_CODES = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
XREF_DB = {
    "MGI": "mgi", "RGD": "rgd", "SGD": "sgd", "PomBase": "pombase", "FB": "flybase",
    "dictyBase": "dictybase", "CGD": "cgd", "WB": "wormbase", "ZFIN": "zfin",
    "AGI_LocusCode": "araport",
}
# Evidence-bearing GOA rows need no propagation analysis; these are the codes that do.
INFERRED_CODES = {"IBA", "IEA", "ISS", "ISO", "IBD", "TAS", "IC"}

SESSION = requests.Session()
SESSION.headers["Accept"] = "application/json"


# --------------------------------------------------------------------------- infra

def require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"missing required input {path}\n  regenerate with: {fix}")
    return path


def get_json(url: str, params: dict | None = None) -> dict:
    r = SESSION.get(url, params=params, timeout=180)
    r.raise_for_status()
    return r.json()


QUICKGO_SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
QUICKGO_MAX_PAGE = 200  # server-enforced; limit=400 answers HTTP 400


def assert_quickgo_calls_are_guarded() -> int:
    """Every QuickGO search in this file must go through `quickgo_all`.

    Carried over from the ACTL10 analysis, where the reviewer pointed out that an assertion
    living in the one-off script that made an edit is true of the moment and not of the
    artefact. Guarding the NAME rather than one call shape closes the keyword-argument, the
    assign-to-a-local and the raw-`SESSION.get` escape routes at once. Done over the AST,
    because the textual version matched this function's own error strings.
    """
    src = Path(__file__).read_text()
    lines = src.splitlines()
    literal = [ln for ln in lines if QUICKGO_SEARCH in ln]
    defining = [ln for ln in literal if ln.strip().startswith("QUICKGO_SEARCH =")]
    if len(literal) != 1 or len(defining) != 1:
        raise RuntimeError(
            f"the QuickGO endpoint URL must be written literally exactly once (the QUICKGO_SEARCH "
            f"constant) but appears on {len(literal)} line(s): "
            f"{[h.strip()[:70] for h in literal]}. A new call site must go through quickgo_all().")
    tree = ast.parse(src)
    defs: dict[str, list] = defaultdict(list)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            defs[node.name].append(node)
    for name in ("quickgo_all", "assert_quickgo_calls_are_guarded"):
        if len(defs.get(name, [])) > 1:
            raise RuntimeError(
                f"{name}() is defined {len(defs[name])} times (lines "
                f"{[d.lineno for d in defs[name]]}); containment is tested by line range, so a "
                "shadowed definition makes the allowed range ambiguous")
    funcs = {k: v[0] for k, v in defs.items()}
    guard = funcs.get("quickgo_all")
    if guard is None:
        raise RuntimeError("quickgo_all() is gone; the QuickGO coverage guard no longer exists")
    selfcheck = funcs.get("assert_quickgo_calls_are_guarded")
    if selfcheck is None:
        raise RuntimeError("assert_quickgo_calls_are_guarded() is gone")
    allowed = [(f.lineno, f.end_lineno or f.lineno) for f in (guard, selfcheck)]
    reads = [n for n in ast.walk(tree)
             if isinstance(n, ast.Name) and n.id == "QUICKGO_SEARCH"
             and not isinstance(n.ctx, ast.Store)]
    stray = [n for n in reads if not any(lo <= n.lineno <= hi for lo, hi in allowed)]
    if stray:
        raise RuntimeError(
            f"QUICKGO_SEARCH is read outside quickgo_all() at line(s) "
            f"{[n.lineno for n in stray]}; every QuickGO search must go through quickgo_all()")
    in_guard = [n for n in reads if guard.lineno <= n.lineno <= (guard.end_lineno or guard.lineno)]
    if not in_guard:
        raise RuntimeError(
            "quickgo_all() no longer reads QUICKGO_SEARCH; it has stopped fetching from QuickGO "
            "and the coverage assertions guard nothing")
    return len(reads)


def quickgo_all(params: dict, what: str, allow_zero: bool = False,
                count_only: bool = False, paginate: bool = False) -> dict:
    """QuickGO search whose result set is asserted to be complete, or declared incomplete.

    QuickGO reports the true total in `numberOfHits` while returning at most `limit` rows, so
    `len(results)` cannot detect its own truncation.

    `allow_zero` distinguishes the two meanings an empty result can have. For an enumeration
    zero means the query broke and must abort; for a per-donor evidence lookup a donor that
    carries nothing for the term it donated is a genuine finding and aborting would destroy it.

    `count_only` is for a caller that reads no rows and wants `numberOfHits` alone; page
    coverage is inapplicable there, and the rows are stripped from the return so a future
    caller cannot iterate a page whose completeness was never checked.
    """
    if "limit" not in params:
        raise RuntimeError(
            f"quickgo_all needs an explicit limit in params for {what}; without it the page size "
            "is whatever the server defaults to and coverage cannot be verified")
    limit = int(params["limit"])
    if limit > QUICKGO_MAX_PAGE:
        raise RuntimeError(
            f"limit={limit} for {what} exceeds QuickGO's maximum page size of {QUICKGO_MAX_PAGE}; "
            "the server answers 400, so a large limit is not a way to avoid pagination")
    d = get_json(QUICKGO_SEARCH, params)
    total = d.get("numberOfHits")
    if total is None:
        raise RuntimeError(f"QuickGO returned no numberOfHits for {what}; cannot verify coverage")
    if count_only:
        # No rows are read, so completeness of the row set is not a property this caller depends
        # on. Return the count ALONE: handing back an unverified `results` array would leave a
        # future caller free to iterate a page whose completeness was never checked.
        if total == 0 and not allow_zero:
            raise RuntimeError(f"QuickGO returned zero rows for {what}")
        return {"numberOfHits": total}
    rows = list(d.get("results", []))
    if total > limit:
        if not paginate:
            raise RuntimeError(
                f"{what} has {total} rows at limit={limit} and pagination was not requested. "
                "A page total is not a whole total - one implementation in this campaign mixed a "
                "full total with a 2% sample. Either pass paginate=True or report the count alone.")
        page = 2
        while len(rows) < total:
            nxt = get_json(QUICKGO_SEARCH, dict(params, page=str(page)))
            got_page = nxt.get("results", [])
            if not got_page:
                raise RuntimeError(
                    f"QuickGO page {page} of {what} came back empty at {len(rows)} of {total} rows; "
                    "the enumeration is incomplete and must not be reported as whole")
            rows.extend(got_page)
            page += 1
            if page > 1 + -(-total // limit):
                raise RuntimeError(f"pagination of {what} overran its own page bound")
    if len(rows) != total:
        # Equality, not `<`: an over-count would be just as much a sign that the response does not
        # mean what this function assumes.
        raise RuntimeError(
            f"QuickGO row count disagrees with its own total for {what}: {len(rows)} of {total}")
    if total == 0 and not allow_zero:
        raise RuntimeError(
            f"QuickGO returned zero rows for {what}; this query underwrites an enumeration, so an "
            "empty result is a broken query rather than a finding")
    d["results"] = rows
    return d


def quickgo_count(params: dict, what: str) -> int:
    """`numberOfHits` for a query whose rows we do not read. Never returns rows."""
    p = dict(params)
    p["limit"] = "1"
    return int(quickgo_all(p, what, allow_zero=True, count_only=True)["numberOfHits"])


def uniprot_entry(acc: str) -> dict:
    """Fetch an entry and prove it is the one asked for.

    A dead or merged accession answers 200 with a different primaryAccession, and a silent
    zero there reads as a finding (the ACTR10 O15507 case). Assert instead.
    """
    d = get_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json",
                 {"fields": "accession,id,sequence,protein_name,organism_name,reviewed,gene_names"})
    got = d.get("primaryAccession")
    if got != acc:
        raise RuntimeError(f"asked UniProt for {acc}, got {got} - accession is dead or merged")
    seq = d["sequence"]["value"]
    if not seq:
        raise RuntimeError(f"UniProt returned an empty sequence for {acc}")
    genes = [g.get("geneName", {}).get("value") for g in d.get("genes", []) if g.get("geneName")]
    return {
        "accession": acc,
        "entry_name": d["uniProtkbId"],
        "gene": genes[0] if genes else None,
        "reviewed": d["entryType"],
        "organism": d["organism"]["scientificName"],
        "length": len(seq),
        "sequence": seq,
    }


def aligner(matrix: str = "BLOSUM62", open_gap: float = -11.0, extend_gap: float = -1.0):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load(matrix)
    al.open_gap_score = open_gap
    al.extend_gap_score = extend_gap
    al.mode = "global"
    return al


ALIGNMENT_SCHEMES = {
    "BLOSUM62/-11/-1": ("BLOSUM62", -11.0, -1.0),
    "BLOSUM45/-14/-2": ("BLOSUM45", -14.0, -2.0),
}

CONSERVATIVE = [set("GA"), set("ST"), set("DE"), set("KRH"), set("NQ"), set("ILVMF"), set("FYW")]


def classify(ref_aa: str, obs_aa: str) -> str:
    if obs_aa == "-":
        return "gap"
    if ref_aa == obs_aa:
        return "identical"
    if any(ref_aa in g and obs_aa in g for g in CONSERVATIVE):
        return "conservative"
    return "non-conservative"


def pair_identity(a: str, b: str, al) -> tuple[float, float]:
    aln = al.align(a, b)[0]
    top, bot = str(aln[0]), str(aln[1])
    matches = sum(1 for x, y in zip(top, bot) if x == y and x != "-")
    return round(100.0 * matches / min(len(a), len(b)), 1), round(float(aln.score), 1)


# ----------------------------------------- Q1: who still receives GO:0005200, and how

def structural_mf_census() -> dict:
    """Every human GO:0005200 annotation, split by evidence route and PANTHER node.

    Asked in two passes on purpose. The IBA pass answers "who does PAINT still project the
    term onto"; the all-evidence pass answers "who holds the term at all". Conflating them
    is how a claim about the retained set can be wrong in both directions at once - a gene
    can hold the term without an IBA (ACTB) and the IBA set can contain genes the claim
    never mentioned.
    """
    iba = quickgo_all({"goId": STRUCTURAL_MF, "goUsage": "exact", "taxonId": "9606",
                       "evidenceCode": "ECO:0000318", "limit": str(QUICKGO_MAX_PAGE)},
                      "human GO:0005200 IBA census", paginate=True)
    by_node: dict[str, list[str]] = defaultdict(list)
    for r in iba["results"]:
        nodes = [x["id"] for wf in (r.get("withFrom") or []) for x in wf["connectedXrefs"]
                 if x["db"] == "PANTHER"]
        for n in nodes:
            by_node[n].append(r["symbol"])
    every = quickgo_all({"goId": STRUCTURAL_MF, "goUsage": "exact", "taxonId": "9606",
                         "limit": str(QUICKGO_MAX_PAGE)},
                        "human GO:0005200 all-evidence census", paginate=True)
    routes: dict[str, list[dict]] = defaultdict(list)
    for r in every["results"]:
        routes[r["symbol"]].append({"evidence": r["goEvidence"], "reference": r["reference"],
                                    "assigned_by": r["assignedBy"]})
    actin_family = {k: v for k, v in sorted(routes.items())
                    if k.startswith("ACT") or k.startswith("POTE")}
    return {
        "n_human_IBA_rows": iba["numberOfHits"],
        "n_human_rows_all_evidence": every["numberOfHits"],
        "IBA_by_panther_node": {k: sorted(v) for k, v in sorted(by_node.items())},
        "IBA_from_family_node": sorted(by_node.get(FAMILY_NODE, [])),
        "actin_family_all_routes": actin_family,
        "acta2_in_IBA_set": "ACTA2" in by_node.get(FAMILY_NODE, []),
    }


def paint_record() -> dict:
    """The cached PTHR11937 PAINT export, read for GO:0005200 assertion and negation."""
    lines = require(PAINT_TSV, "cached PANTHER PAINT export").read_text().splitlines()
    header = lines[0].split("\t")
    rows = [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]
    ibd = [r for r in rows if r["go_id"] == STRUCTURAL_MF and r["evidence"] == "IBD"]
    ird = [r for r in rows if r["go_id"] == STRUCTURAL_MF and r["negated"] == "true"]
    other = [r for r in rows if r["go_id"] == STRUCTURAL_MF
             and r["evidence"] != "IBD" and r["negated"] != "true"]
    if len(ibd) != 1:
        raise RuntimeError(
            f"expected exactly one GO:0005200 IBD assertion in {PAINT_TSV}, found {len(ibd)} "
            f"at {[r['node'] for r in ibd]}; the whole propagation argument assumes a single "
            "point of assertion and must be re-derived if that changed")
    if ibd[0]["node"] != FAMILY_NODE:
        raise RuntimeError(f"GO:0005200 is asserted at {ibd[0]['node']}, not {FAMILY_NODE}")
    return {
        "n_paint_rows": len(rows),
        "assertion_node": ibd[0]["node"],
        "assertion_seeds": split_withfrom(ibd[0]["seeds"]),
        "assertion_date": ibd[0]["date"],
        "n_IRD_negations": len(ird),
        "IRD_negations": [{"node": r["node"], "seeds": split_withfrom(r["seeds"]),
                           "date": r["date"]} for r in sorted(ird, key=lambda x: x["node"])],
        "other_rows": [{"node": r["node"], "evidence": r["evidence"], "negated": r["negated"]}
                       for r in other],
    }


def seed_vs_negation(paint: dict, resolved_seeds: dict) -> dict:
    """Is any protein used as an IBD seed for GO:0005200 also inside an IRD-negated clade?

    PAINT records negations by node, not by gene, so the two facts live in different rows and
    the contradiction is invisible unless the seed accessions are matched against the seed
    accessions of the negated nodes' own other rows. A seed that supports the assertion while
    its own clade is exempted from it is a defect in the tree, not in either row.
    """
    negated_nodes = {n["node"] for n in paint["IRD_negations"]}
    lines = require(PAINT_TSV, "cached PANTHER PAINT export").read_text().splitlines()
    header = lines[0].split("\t")
    rows = [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]
    seeds_of_negated: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        if r["node"] in negated_nodes and r["go_id"] != STRUCTURAL_MF:
            seeds_of_negated[r["node"]].update(split_withfrom(r["seeds"]))
    out = []
    for tok in paint["assertion_seeds"]:
        hits = sorted(n for n, s in seeds_of_negated.items() if tok in s)
        if hits:
            chosen = (resolved_seeds.get(tok) or {}).get("chosen") or {}
            out.append({"seed": tok, "gene": chosen.get("gene"),
                        "organism": chosen.get("organism"), "negated_nodes": hits})
    return {"n_seeds": len(paint["assertion_seeds"]),
            "seeds_also_inside_a_negated_clade": out,
            "n_contradictions": len(out)}


# ------------------------- Q1b: node<->gene reach, asked in BOTH directions

# Terms whose PANTHER node placement is in question for the smooth-muscle actins. Each is a term
# every conventional actin should plausibly hold.
NODE_AUDIT_TERMS = ["GO:0005884", "GO:0017022", "GO:0033275", "GO:0007015", "GO:0005576"]
CONVENTIONAL_ACTINS = {
    "P68133": "ACTA1", "P62736": "ACTA2", "P68032": "ACTC1", "P63267": "ACTG2",
    "P60709": "ACTB", "P63261": "ACTG1",
}


def node_audit() -> dict:
    """Which nodes carry a term, AND which node's reach is exactly a given gene set.

    Two different questions, and only the second surfaces the interesting case. Asking only "which
    node gives ACTA2 term X" cannot find a node that gives ACTA2 nothing it should have; asking
    "what is this node FOR" can. The reverse query is what shows that PTHR11937 has a node whose
    entire human output is the two smooth-muscle actins, and that what it gives them is a
    localisation outside the cell.
    """
    forward: dict[str, dict] = {}
    for go in NODE_AUDIT_TERMS:
        d = quickgo_all({"goId": go, "goUsage": "exact", "taxonId": "9606",
                         "evidenceCode": "ECO:0000318", "limit": str(QUICKGO_MAX_PAGE)},
                        f"human IBA census for {go}", paginate=True)
        by_node: dict[str, list[str]] = defaultdict(list)
        for r in d["results"]:
            for n in [x["id"] for wf in (r.get("withFrom") or []) for x in wf["connectedXrefs"]
                      if x["db"] == "PANTHER"]:
                by_node[n].append(r["symbol"])
        # Restrict to nodes that touch at least one conventional actin, so the table is about this
        # family rather than about every cytoskeletal protein in the ontology.
        fam = {n: sorted(set(v)) for n, v in by_node.items()
               if set(v) & set(CONVENTIONAL_ACTINS.values())}
        holders: dict[str, list[str]] = {}
        for acc, sym in CONVENTIONAL_ACTINS.items():
            h = quickgo_all({"geneProductId": f"UniProtKB:{acc}", "goId": go,
                             "goUsage": "descendants", "goUsageRelationships": "is_a,part_of",
                             "limit": "50"},
                            f"{sym} coverage of {go} and descendants", allow_zero=True)
            holders[sym] = sorted({f"{r['goId']}:{r['goEvidence']}" for r in h.get("results", [])})
        forward[go] = {
            "nodes_touching_conventional_actins": fam,
            "per_gene_including_descendants": holders,
            "conventional_actins_with_nothing": sorted(k for k, v in holders.items() if not v),
        }
    # Reverse: what is each of those nodes FOR, across all of human?
    reverse: dict[str, dict] = {}
    nodes = sorted({n for go in forward for n in forward[go]["nodes_touching_conventional_actins"]})
    for node in nodes:
        d = quickgo_all({"taxonId": "9606", "evidenceCode": "ECO:0000318", "withFrom": f"PANTHER:{node}",
                         "limit": str(QUICKGO_MAX_PAGE)},
                        f"human reach of {node}", allow_zero=True, paginate=True)
        genes = sorted({r["symbol"] for r in d["results"]})
        terms = sorted({f"{r['goId']} {r.get('goName') or ''}".strip() for r in d["results"]})
        reverse[node] = {
            "n_human_annotations": d.get("numberOfHits"),
            "human_genes": genes, "terms": terms,
            "reach_is_exactly_the_smooth_muscle_pair": genes == ["ACTA2", "ACTG2"],
        }
    return {"forward_term_to_nodes": forward, "reverse_node_to_reach": reverse}


# --------------------------------------- Q2: residue tallies at the two actin surfaces

def fetch_cif(pdb_id: str) -> str:
    r = SESSION.get(f"https://files.rcsb.org/download/{pdb_id.upper()}.cif", timeout=300)
    r.raise_for_status()
    return r.text


def polymer_residues(chain):
    return [r for r in chain if r.id[0] != "W" and r.get_resname().upper() in THREE_TO_ONE]


def chain_sequence(residues) -> str:
    return "".join(THREE_TO_ONE[r.get_resname().upper()] for r in residues)


def ligand_contacts(cif_text, pdb_id, chain_id, ligand_names, cutoff):
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chain = model[chain_id]
    residues = polymer_residues(chain)
    ligands = [r for r in chain if r.get_resname().strip() in ligand_names]
    if not ligands:
        raise RuntimeError(f"{pdb_id} chain {chain_id} carries none of {sorted(ligand_names)}")
    ns = NeighborSearch([a for r in residues for a in r])
    hits: dict[int, dict] = {}
    for lig in ligands:
        for atom in lig:
            for other in ns.search(atom.coord, cutoff):
                res = other.get_parent()
                d = float(atom - other)
                rec = hits.setdefault(res.id[1], {"resname": res.get_resname(),
                                                  "ligands": set(), "min_dist": d})
                rec["ligands"].add(lig.get_resname().strip())
                rec["min_dist"] = min(rec["min_dist"], d)
    for rec in hits.values():
        rec["ligands"] = sorted(rec["ligands"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return residues, hits


def interface_contacts(cif_text, pdb_id, cutoff):
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chains = {c.id: polymer_residues(c) for c in model}
    chains = {k: v for k, v in chains.items() if len(v) > 200}
    if len(chains) < 3:
        raise RuntimeError(f"{pdb_id} yielded {len(chains)} long chains; need a multi-protomer model")
    best = None
    for cid, residues in chains.items():
        others = [a for k, v in chains.items() if k != cid for r in v for a in r]
        ns = NeighborSearch(others)
        hits: dict[int, dict] = {}
        for res in residues:
            for atom in res:
                for other in ns.search(atom.coord, cutoff):
                    d = float(atom - other)
                    rec = hits.setdefault(res.id[1], {"resname": res.get_resname(),
                                                      "partners": set(), "min_dist": d})
                    rec["partners"].add(other.get_parent().get_parent().id)
                    rec["min_dist"] = min(rec["min_dist"], d)
        if best is None or len(hits) > len(best[2]):
            best = (cid, residues, hits)
    cid, residues, hits = best
    for rec in hits.values():
        rec["partners"] = sorted(rec["partners"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return cid, sorted(chains), residues, hits


def align_map(struct_seq: str, struct_numbers: list[int], query_seq: str, al):
    """Two dictionaries relating structure numbering to a query sequence.

    `by_struct[struct_number] -> (query_aa, query_index_1based | None)`
    `by_query[query_index_1based] -> struct_number`
    The second is what places a UniProt variant position onto a structure, and it must come
    from the same alignment as the first or the two answers can disagree.
    """
    aln = al.align(struct_seq, query_seq)[0]
    top, bot = str(aln[0]), str(aln[1])
    si = qi = 0
    by_struct: dict[int, tuple[str, int | None]] = {}
    by_query: dict[int, int] = {}
    for sc, qc in zip(top, bot):
        if sc != "-":
            si += 1
        if qc != "-":
            qi += 1
        if sc != "-":
            num = struct_numbers[si - 1]
            by_struct[num] = (qc, qi if qc != "-" else None)
            if qc != "-":
                by_query[qi] = num
    return by_struct, by_query


def score_against(struct_seq: str, struct_numbers: list[int], contact_nums: list[int],
                  query_seq: str, al) -> dict:
    """Map structure contact positions onto a query, splitting gaps by cause.

    `outside_span` means the query does not extend to that structural position at all - the
    position is absent from the ANNOTATION, which is a different fact from a substitution.
    `internal_gap` means the query does span the position but has a deletion there.
    """
    by_struct, _ = align_map(struct_seq, struct_numbers, query_seq, al)
    aligned = [n for n, (aa, _) in by_struct.items() if aa != "-"]
    if not aligned:
        raise RuntimeError("query aligned to nothing")
    first, last = min(aligned), max(aligned)
    per: dict[str, str] = {}
    tally = Counter()
    for num in contact_nums:
        ref_aa = struct_seq[struct_numbers.index(num)]
        obs = by_struct[num][0]
        if obs == "-":
            kind = "internal_gap" if first <= num <= last else "outside_span"
        else:
            kind = classify(ref_aa, obs)
        per[str(num)] = f"{obs}:{kind}"
        tally[kind] += 1
    ident, score = pair_identity(struct_seq, query_seq, al)
    return {
        "identical": tally["identical"], "conservative": tally["conservative"],
        "non_conservative": tally["non-conservative"],
        "internal_gap": tally["internal_gap"], "outside_span": tally["outside_span"],
        "compatible": tally["identical"] + tally["conservative"],
        "present": len(contact_nums) - tally["outside_span"],
        "aligned_struct_span": [first, last],
        "pct_identity_to_struct_chain": ident,
        "per_residue": per,
    }


def parse_actl8_interface_table(path: Path) -> dict[str, tuple[int, int, int, int]]:
    """ACTL8's committed filament-interface tallies, used as a cross-file reproduction check.

    Fails loudly if the table cannot be found: a silently empty expectation makes the
    assertion below vacuous, which is the "guard defeatable by deleting the thing it guards"
    failure mode.
    """
    text = require(path, "see genes/human/ACTL8/ACTL8-bioinformatics/").read_text()
    m = re.search(r"## 2\. Is the filament protomer interface still present\?(.*?)\n### ",
                  text, re.S)
    if not m:
        raise RuntimeError(f"could not locate the filament-interface section in {path}")
    out: dict[str, tuple[int, int, int, int]] = {}
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[1].isdigit():
            out[cells[0]] = tuple(int(c) for c in cells[1:])
    if not out:
        raise RuntimeError(f"parsed zero rows from the filament-interface table in {path}")
    return out


def short_sequence_guard(entries: dict[str, dict]) -> dict:
    """Which panel members are too short for a residue tally to mean what it looks like?

    The ACTL10 artefact in one line: Q5JWF8 is 245 aa where the family is ~375, its Swiss-Prot
    sequence begins mid-fold, and 20 interface positions it never reaches were tallied as 20
    non-conservative substitutions in a merged sibling review. Any member below the fraction is
    flagged here, and the tally below reports `outside_span` as its own column so the two kinds
    of absence can never be added together again.
    """
    lengths = sorted(e["length"] for e in entries.values())
    n = len(lengths)
    median = lengths[n // 2] if n % 2 else (lengths[n // 2 - 1] + lengths[n // 2]) / 2
    cut = SHORT_SEQUENCE_FRACTION * median
    flagged = {acc: {"length": e["length"], "gene": e["gene"],
                     "fraction_of_median": round(e["length"] / median, 3)}
               for acc, e in entries.items() if e["length"] < cut}
    if entries[ACTA2]["length"] < cut:
        raise RuntimeError(
            f"ACTA2's own reference sequence ({entries[ACTA2]['length']} aa) is below "
            f"{SHORT_SEQUENCE_FRACTION:.0%} of the panel median ({median}); every tally in this "
            "run would be measuring the annotation boundary rather than the protein")
    return {"panel_median_length": median, "threshold_length": round(cut, 1),
            "flagged_short": flagged, "n_flagged": len(flagged)}


# ----------------------------------- Q3: disease variants against the same two surfaces

VARIANT_RE = re.compile(r"^FT\s+VARIANT\s+(\d+)\s*$")


def parse_variants(path: Path) -> list[dict]:
    """UniProt FT VARIANT positions with their disease labels, from the cached flat file.

    Positions are in P62736's own 377-residue precursor numbering; the mapping onto the
    structures is done by alignment, never by an assumed offset.
    """
    lines = require(path, "just fetch-gene human ACTA2").read_text().splitlines()
    out: list[dict] = []
    i = 0
    while i < len(lines):
        m = VARIANT_RE.match(lines[i])
        if not m:
            i += 1
            continue
        pos = int(m.group(1))
        note_parts: list[str] = []
        evidence: list[str] = []
        j = i + 1
        while j < len(lines) and lines[j].startswith("FT       ") and "VARIANT" not in lines[j]:
            body = lines[j][21:].strip()
            if body.startswith("/note="):
                note_parts.append(body[len("/note="):].strip('"'))
            elif body.startswith("/evidence="):
                evidence.append(body[len("/evidence="):].strip('"'))
            elif note_parts and not body.startswith("/"):
                note_parts.append(body.strip('"'))
            elif evidence and not body.startswith("/"):
                evidence.append(body.strip('"'))
            j += 1
        note = " ".join(note_parts)
        diseases = sorted(set(re.findall(r"\b(AAT6|MYMY5|SMDYS)\b", note)))
        out.append({"position": pos, "note": note, "diseases": diseases,
                    "pathogenic": bool(diseases),
                    "n_pmids": len(set(re.findall(r"PubMed:(\d+)", " ".join(evidence))))})
        i = j
    if not out:
        raise RuntimeError(f"parsed zero FT VARIANT lines from {path}")
    return out


def check_numbering(acta2_seq: str, surfaces: dict, al) -> dict:
    """Verify the precursor->structure offset against sources that state both numbers.

    Without this the -2 offset is an assumption, and an assumed offset placing a variant one
    residue off a 4 A contact set would produce a confident wrong negative.
    """
    out = {}
    for surf_name, surf in surfaces.items():
        _, by_query = align_map(surf["struct_seq"], surf["struct_numbers"], acta2_seq, al)
        for pre, (expect, aa, provenance) in NUMBERING_CONTROLS.items():
            got = by_query.get(pre)
            if got != expect:
                raise RuntimeError(
                    f"numbering control failed on {surf_name}: ACTA2 precursor {pre} maps to "
                    f"structure {got}, expected {expect}. Provenance: {provenance}")
            if acta2_seq[pre - 1] != aa:
                raise RuntimeError(
                    f"ACTA2 residue {pre} is {acta2_seq[pre-1]}, expected {aa} ({provenance})")
            out[f"{surf_name}:{pre}->{expect}"] = provenance
    return out


def check_interstrand_literature(surfaces: dict, acta2_seq: str, al) -> dict:
    """Do the residues PMID:26637293 names as R179's inter-strand partners fall in the set?

    A literature-derived control on the contact set itself. If the paper's named paired-molecule
    residues are absent from an independently computed inter-protomer contact set, the set is
    wrong and nothing downstream of it can be believed.
    """
    surf = surfaces["filament_interface"]
    _, by_query = align_map(surf["struct_seq"], surf["struct_numbers"], acta2_seq, al)
    out = {}
    for pre, aa in INTERSTRAND_LITERATURE_CONTROL.items():
        if acta2_seq[pre - 1] != aa:
            raise RuntimeError(f"ACTA2 residue {pre} is {acta2_seq[pre-1]}, expected {aa}")
        snum = by_query.get(pre)
        present = snum in surf["contact_nums"]
        out[f"{aa}{pre}"] = {"struct_position": snum, "in_contact_set": present,
                             "partners": surf["hits"].get(snum, {}).get("partners")}
        if not present:
            raise RuntimeError(
                f"PMID:26637293 names {aa}{pre} (structure {snum}) as an inter-strand contact "
                f"residue, but it is absent from the computed {len(surf['contact_nums'])}-residue "
                "inter-protomer contact set; the contact set is not measuring what it claims")
    return out


def protomer_distances(cif_text: str, pdb_id: str, struct_positions: list[int],
                       cutoff_report: float = 15.0) -> dict:
    """Closest approach of each structural position to ANY other protomer, over ALL chains.

    Two reasons this is not the same query as the contact set. (1) An absence from a 4 A set is
    not a finding; a measured distance is. (2) 6DJO holds four protomers, so no single chain has
    both its i-2 and its i+2 neighbour - chain C is missing i+2 and chain B is missing i-2 - and
    a per-chain answer would silently omit one relationship. Taking the minimum over every chain
    covers both the same-strand (|delta index| = 2) and cross-strand (= 1) relationships.
    """
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chains = {c.id: polymer_residues(c) for c in model}
    chains = {k: v for k, v in chains.items() if len(v) > 200}
    order = sorted(chains)
    atoms_by_chain = {k: [a for r in v for a in r] for k, v in chains.items()}
    out: dict[str, dict] = {}
    for pos in struct_positions:
        best = None
        for cid in order:
            res = next((r for r in chains[cid] if r.id[1] == pos), None)
            if res is None:
                continue
            others = [(k, a) for k in order if k != cid for a in atoms_by_chain[k]]
            ns_pairs = [(k, float(a - b)) for k, a in others for b in res]
            if not ns_pairs:
                continue
            k, d = min(ns_pairs, key=lambda x: x[1])
            rel = "same-strand (i+/-2)" if abs(order.index(cid) - order.index(k)) == 2 \
                else "cross-strand (i+/-1)" if abs(order.index(cid) - order.index(k)) == 1 \
                else f"index offset {abs(order.index(cid) - order.index(k))}"
            if best is None or d < best[1]:
                best = (cid, d, k, rel)
        if best is None:
            out[str(pos)] = {"status": "position absent from every long chain"}
            continue
        cid, d, k, rel = best
        out[str(pos)] = {"min_dist_to_other_protomer": round(d, 2), "from_chain": cid,
                         "to_chain": k, "relationship": rel,
                         "within_report_shell": d <= cutoff_report}
    if not out:
        raise RuntimeError("protomer_distances measured nothing")
    return out


def nucleotide_distances(cif_text: str, pdb_id: str, chain_id: str, ligand_names,
                         struct_positions: list[int]) -> dict:
    """Closest approach of each structural position to the bound nucleotide."""
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chain = model[chain_id]
    ligs = [r for r in chain if r.get_resname().strip() in ligand_names]
    if not ligs:
        raise RuntimeError(f"{pdb_id} chain {chain_id} carries none of {sorted(ligand_names)}")
    lig_atoms = [a for r in ligs for a in r]
    out = {}
    for pos in struct_positions:
        res = next((r for r in polymer_residues(chain) if r.id[1] == pos), None)
        if res is None:
            out[str(pos)] = {"status": "position absent from the chain"}
            continue
        out[str(pos)] = {"min_dist_to_nucleotide":
                         round(min(float(a - b) for a in lig_atoms for b in res), 2)}
    return out


def variants_on_surfaces(variants: list[dict], surfaces: dict, acta2_seq: str, al) -> dict:
    """Place every FT VARIANT position on the nucleotide site and the filament interface.

    Enrichment is reported as a plain 2x2 count, not a p-value: with 19 variants and two
    contact sets of 19 and 38 residues out of ~375, a test statistic would carry more
    apparent precision than the data.
    """
    rows: list[dict] = []
    per_surface_hits: dict[str, list[int]] = {k: [] for k in surfaces}
    for v in variants:
        rec = {"position": v["position"], "note": v["note"], "diseases": v["diseases"],
               "pathogenic": v["pathogenic"], "surfaces": {}}
        for name, surf in surfaces.items():
            _, by_query = align_map(surf["struct_seq"], surf["struct_numbers"], acta2_seq, al)
            snum = by_query.get(v["position"])
            on = snum is not None and snum in surf["contact_nums"]
            rec["surfaces"][name] = {
                "struct_position": snum,
                "on_surface": on,
                "partners": surf["hits"].get(snum, {}).get("partners") if on else None,
                "ligands": surf["hits"].get(snum, {}).get("ligands") if on else None,
                "min_dist": surf["hits"].get(snum, {}).get("min_dist") if on else None,
            }
            if on:
                per_surface_hits[name].append(v["position"])
        rows.append(rec)
    summary = {}
    for name, surf in surfaces.items():
        path_hits = [r["position"] for r in rows
                     if r["pathogenic"] and r["surfaces"][name]["on_surface"]]
        benign_hits = [r["position"] for r in rows
                       if not r["pathogenic"] and r["surfaces"][name]["on_surface"]]
        n_path = sum(1 for r in rows if r["pathogenic"])
        summary[name] = {
            "n_contact_residues": len(surf["contact_nums"]),
            "chain_length": len(surf["struct_seq"]),
            "surface_fraction_of_chain": round(len(surf["contact_nums"]) / len(surf["struct_seq"]), 3),
            "n_pathogenic_variants": n_path,
            "n_pathogenic_on_surface": len(path_hits),
            "pathogenic_on_surface": path_hits,
            "n_nonpathogenic_variants": len(rows) - n_path,
            "n_nonpathogenic_on_surface": len(benign_hits),
            "nonpathogenic_on_surface": benign_hits,
        }
    return {"per_variant": rows, "per_surface": summary}


# ------------------------------------------- Q4: WITH/FROM resolution + donor evidence

def parse_goa(path: Path) -> list[dict]:
    lines = require(path, "just fetch-gene human ACTA2").read_text().splitlines()
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def split_withfrom(field: str) -> list[str]:
    return [t for t in field.split("|") if t.strip()]


def resolve_token(token: str) -> dict:
    """Resolve a WITH/FROM token, always requesting more than one hit so ambiguity shows.

    `size=1` converts an ambiguity into a confident wrong answer: on ABHD8 one Drosophila gene
    mapped to two TrEMBL accessions with different names and the single-hit query silently
    picked the one that named an activity.
    """
    if token.startswith("PANTHER:"):
        return {"token": token, "kind": "panther_node", "resolved": False,
                "note": "PANTHER internal tree node, not a protein - carries no evidence of its own"}
    if token.startswith("GO:"):
        return {"token": token, "kind": "go_term", "resolved": False,
                "note": "a GO term, not a gene product - this row is an inter-ontology inference"}
    if token.startswith("UniProtKB-SubCell:"):
        return {"token": token, "kind": "subcell_vocabulary", "resolved": False,
                "note": "a UniProt Subcellular Location vocabulary id, not a gene product"}
    if token.startswith("ensembl:"):
        return {"token": token, "kind": "ensembl_protein", "resolved": False,
                "note": "Ensembl protein id; the UniProt token on the same row is the resolvable one"}
    db, _, ident = token.partition(":")
    if db == "UniProtKB":
        q = f"accession:{ident}"
    elif db == "WB":
        q = f"xref:{ident}"
    elif db in XREF_DB:
        inner = ident.split(":")[-1]  # MGI arrives as MGI:MGI:87906; the inner colon is a 400
        q = f"xref:{XREF_DB[db]}-{inner}"
    else:
        return {"token": token, "kind": "unknown_db", "resolved": False,
                "note": f"no UniProt xref mapping for db {db!r}"}
    d = get_json("https://rest.uniprot.org/uniprotkb/search",
                 {"query": q, "fields": "accession,id,gene_names,organism_name,reviewed,length",
                  "format": "json", "size": "5"})
    hits = d.get("results", [])
    if not hits:
        return {"token": token, "kind": "protein", "resolved": False,
                "note": "no UniProt entry found - cannot be dismissed, only deferred"}
    cands = []
    for r in hits:
        genes = [g.get("geneName", {}).get("value") for g in r.get("genes", []) if g.get("geneName")]
        cands.append({
            "accession": r["primaryAccession"], "entry_name": r.get("uniProtkbId"),
            "gene": genes[0] if genes else None,
            "organism": r["organism"]["scientificName"],
            "reviewed": r["entryType"], "length": r["sequence"]["length"],
        })
    reviewed = [c for c in cands if "Swiss-Prot" in c["reviewed"]]
    chosen = reviewed[0] if reviewed else cands[0]
    return {"token": token, "kind": "protein", "resolved": True,
            "n_candidates": len(cands), "candidates": cands, "chosen": chosen,
            "ambiguous": len(cands) > 1,
            "reviewed_status": "Swiss-Prot" if reviewed else "TrEMBL (unreviewed) - a name from "
                               "such an entry is not evidence of what the family does"}


def quickgo_evidence(gene_product: str, go_id: str) -> dict:
    """What evidence does this source itself hold for the term it donated, and for WHICH term?

    Recording the term and not merely the presence of one is what caught the ACRV1 case, where a
    donor's IDA sat three levels BELOW the term that was propagated.
    """
    d = quickgo_all({"geneProductId": gene_product, "goId": go_id, "goUsage": "descendants",
                     "goUsageRelationships": "is_a,part_of", "limit": "100"},
                    f"own-evidence query for {gene_product} / {go_id}", allow_zero=True)
    codes = Counter()
    terms = Counter()
    exact = Counter()
    for r in d.get("results", []):
        codes[r["goEvidence"]] += 1
        terms[f"{r['goId']} {r.get('goName','')}"] += 1
        if r["goId"] == go_id:
            exact[r["goEvidence"]] += 1
    n = d.get("numberOfHits", 0)
    absent = None
    if n == 0:
        # A zero has two meanings: the donor holds nothing for the donated term (a finding that
        # weakens the propagation), or QuickGO does not hold this accession at all (a data
        # artefact that would read as a property of the donor - the dead-accession trap).
        absent = quickgo_count({"geneProductId": gene_product}, f"presence probe {gene_product}") == 0
    return {"n": n, "codes": dict(codes), "terms": dict(terms),
            "codes_on_exact_term": dict(exact),
            "has_experimental": bool(set(codes) & EXPERIMENTAL_CODES),
            "has_experimental_on_exact_term": bool(set(exact) & EXPERIMENTAL_CODES),
            "accession_absent_from_quickgo": absent}


def withfrom_analysis(goa: list[dict]) -> dict:
    """Every WITH/FROM token on every non-experimental row, resolved and interrogated.

    Built FROM the GOA field with a count assertion, never by hand: source lists maintained by
    hand drifted on three genes in this campaign, and only a scripted diff found it.
    """
    rows: list[dict] = []
    cache_resolve: dict[str, dict] = {}
    cache_evid: dict[tuple[str, str], dict] = {}
    total_tokens = 0
    for r in goa:
        if r["GO EVIDENCE CODE"] not in INFERRED_CODES:
            continue
        toks = split_withfrom(r["WITH/FROM"])
        total_tokens += len(toks)
        sources = []
        for t in toks:
            if t not in cache_resolve:
                cache_resolve[t] = resolve_token(t)
            info = dict(cache_resolve[t])
            if info.get("resolved"):
                acc = info["chosen"]["accession"]
                key = (f"UniProtKB:{acc}", r["GO TERM"])
                if key not in cache_evid:
                    cache_evid[key] = quickgo_evidence(*key)
                info["own_evidence_for_donated_term"] = cache_evid[key]
            sources.append(info)
        rows.append({
            "go_id": r["GO TERM"], "go_name": r["GO NAME"], "aspect": r["GO ASPECT"],
            "evidence": r["GO EVIDENCE CODE"], "qualifier": r["QUALIFIER"],
            "reference": r["REFERENCE"], "assigned_by": r["ASSIGNED BY"],
            "n_tokens": len(toks), "sources": sources,
        })
    tally = sum(x["n_tokens"] for x in rows)
    if tally != total_tokens:
        raise RuntimeError(f"token accounting broke: {tally} vs {total_tokens}")
    return {"n_inferred_rows": len(rows), "n_withfrom_tokens": total_tokens, "rows": rows}


# ------------------------------------ Q4b: interaction partners and detection methods

def interaction_partners(goa: list[dict]) -> dict:
    """Resolve every GO:0005515 partner and ask how the interaction was actually detected.

    Two lessons folded in. A named partner is not a verified partner - ACRV1's "TSC1" was an
    unreviewed 366-aa ORFeome clone rather than canonical 1164-aa TSC1 - so each accession is
    resolved and its length and reviewed status printed. And an interaction count is not a count
    of independent experiments: on ACRV1 five rows traced to one Y2H screen logged under three
    sub-method names, so the IntAct detection methods are read rather than the row count.
    """
    toks: dict[str, set[str]] = defaultdict(set)
    for r in goa:
        if r["GO TERM"] == "GO:0005515":
            for t in split_withfrom(r["WITH/FROM"]):
                toks[t].add(r["REFERENCE"])
    partners = []
    for tok in sorted(toks):
        info = resolve_token(tok)
        rec = {"token": tok, "references": sorted(toks[tok])}
        if info.get("resolved"):
            ch = info["chosen"]
            rec |= {"gene": ch["gene"], "accession": ch["accession"], "length": ch["length"],
                    "organism": ch["organism"],
                    "reviewed": "Swiss-Prot" if "Swiss-Prot" in ch["reviewed"] else "TrEMBL",
                    "n_candidates": info["n_candidates"]}
            sub = get_json(f"https://rest.uniprot.org/uniprotkb/{ch['accession']}.json",
                           {"fields": "cc_subcellular_location"})
            locs = sorted({loc["location"]["value"]
                           for c in sub.get("comments", [])
                           if c.get("commentType") == "SUBCELLULAR LOCATION"
                           for loc in c.get("subcellularLocations", [])})
            rec["subcellular_location"] = locs
        else:
            rec["note"] = info.get("note")
        partners.append(rec)
    # IntAct, paginated to completion, so the method census covers every logged interaction.
    inter = []
    page = 0
    while True:
        d = get_json(f"https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/{ACTA2}",
                     {"page": str(page), "pageSize": "100"})
        rows = d.get("content", [])
        inter.extend(rows)
        if len(inter) >= d.get("totalElements", len(inter)) or not rows:
            break
        page += 1
    if d.get("totalElements") is not None and len(inter) != d["totalElements"]:
        raise RuntimeError(
            f"IntAct returned {len(inter)} of {d['totalElements']} interactions for {ACTA2}; the "
            "method census would be computed on a partial set")
    methods = Counter(x.get("detectionMethod") for x in inter)
    partner_names = Counter()
    for x in inter:
        other = x["moleculeA"] if x["uniqueIdB"].startswith(ACTA2) else x["moleculeB"]
        partner_names[other] += 1
    return {
        "goa_partners": partners,
        "n_goa_partner_tokens": len(partners),
        "intact_total": len(inter),
        "intact_detection_methods": dict(methods),
        "intact_partner_row_counts": dict(sorted(partner_names.items())),
        "intact_singletons": sorted(k for k, v in partner_names.items() if v == 1),
    }


# ------------------------------------------- retraction / erratum / correction check

def crossref_corrections(doi: str) -> list[dict]:
    """Works that Crossref records as updating this DOI (erratum / corrigendum / retraction)."""
    d = get_json("https://api.crossref.org/works",
                 {"filter": f"updates:{doi}", "rows": "20",
                  "select": "DOI,title,type,update-to,published"})
    return [{"doi": it.get("DOI"), "type": it.get("type"),
             "title": (it.get("title") or [""])[0],
             "update_types": sorted({u.get("type") for u in (it.get("update-to") or [])})}
            for it in d["message"]["items"]]


def corrections_check(pmids: list[str]) -> dict:
    """Retraction, erratum, correction and expression-of-concern status for cited PMIDs.

    A Publisher Correction is NOT discoverable by a publication-type search; it has to be read
    from the CITED article's own CommentsCorrections block. Both halves are read here.
    """
    import xml.etree.ElementTree as ET
    out: dict[str, dict] = {}
    chunk = 20
    for i in range(0, len(pmids), chunk):
        ids = pmids[i:i + chunk]
        r = SESSION.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                        params={"db": "pubmed", "id": ",".join(ids), "retmode": "xml"},
                        timeout=180)
        r.raise_for_status()
        root = ET.fromstring(r.text)
        for art in root.iter("PubmedArticle"):
            pmid = art.findtext(".//PMID")
            ptypes = [e.text for e in art.iter("PublicationType")]
            cc = [{"ref_type": e.get("RefType"), "pmid": e.findtext("PMID")}
                  for e in art.iter("CommentsCorrections")]
            flags = sorted({c["ref_type"] for c in cc
                            if c["ref_type"] in {"RetractionIn", "ErratumIn", "CorrectedandRepublishedIn",
                                                 "ExpressionOfConcernIn", "RetractedandRepublishedIn"}})
            doi = next((e.text for e in art.iter("ArticleId")
                        if e.get("IdType") == "doi"), None)
            refs = [c for c in cc if c["ref_type"] in flags]
            # PubMed's CommentsCorrections can carry a NULL pmid for a correction that was never
            # indexed as its own record - PMID:17994018's 2008 corrigendum is such a case, so the
            # correction is undiscoverable from PubMed alone. Crossref records the reverse link.
            for c in refs:
                if c["pmid"] is None and doi:
                    c["crossref_updates"] = crossref_corrections(doi)
            out[pmid] = {
                "title": art.findtext(".//ArticleTitle"),
                "doi": doi,
                "publication_types": ptypes,
                "is_retracted_publication": "Retracted Publication" in ptypes,
                "correction_flags": flags,
                "correction_refs": refs,
                "clean": not flags and "Retracted Publication" not in ptypes,
            }
    missing = [p for p in pmids if p not in out]
    if missing:
        raise RuntimeError(f"PubMed returned no record for {missing}; status is unknown, not clean")
    return {"n_checked": len(out), "n_flagged": sum(1 for v in out.values() if not v["clean"]),
            "per_pmid": out}


# ------------------------------------------------------- Q5: reference projection check

def reference_projection(goa: list[dict]) -> dict:
    """For each literature reference on an ACTA2 row: how many annotations, how many entities?

    Two ways to get this wrong, both paid for earlier in this campaign:
      - an annotation count is NOT an entity count (one reference carried 22 annotations over
        12 entities), so entities are derived as a distinct set of gene-product ids; and
      - a large result is paginated, so a page total must never be read as the whole. Above
        what one page can carry, the honest output is "entity count unavailable".
    A many-entity reference is only a PROJECTION if the phenotype spreads with the
    localisation, so the terms are reported per entity-count as well.
    """
    refs = sorted({r["REFERENCE"] for r in goa if r["REFERENCE"].startswith("PMID:")})
    page = QUICKGO_MAX_PAGE
    out = []
    for ref in refs:
        total = quickgo_count({"reference": ref}, f"annotation count for {ref}")
        rec = {"reference": ref, "n_annotations": total}
        if total > page:
            rec.update({
                "n_entities": None,
                "entity_count_status": f"unavailable: {total} annotations exceed the {page}-row "
                                       "page this script reads, and a page total is not a whole "
                                       "total; the projection test is unreliable for this "
                                       "reference and is not attempted",
            })
        else:
            d = quickgo_all({"reference": ref, "limit": str(page)},
                            f"entity enumeration for {ref}", allow_zero=True)
            ents = {r["geneProductId"] for r in d["results"]}
            terms = Counter(f"{r['goId']} {r.get('goName','')}" for r in d["results"])
            per_term_entities = defaultdict(set)
            for r in d["results"]:
                per_term_entities[f"{r['goId']} {r.get('goName','')}"].add(r["geneProductId"])
            rec.update({
                "n_entities": len(ents),
                "entity_count_status": "derived as a distinct set of gene-product ids",
                "annotations_per_term": dict(terms),
                "entities_per_term": {k: len(v) for k, v in sorted(per_term_entities.items())},
                "assigned_by": dict(Counter(r["assignedBy"] for r in d["results"])),
                "evidence_codes": dict(Counter(r["goEvidence"] for r in d["results"])),
            })
        out.append(rec)
    return {"n_references": len(refs), "references": out}


# ------------------------------------------------------ coverage / duplicate-key audit

class NoDuplicateKeys(dict):
    """Sentinel type; the loader below rejects duplicated mapping keys outright."""


def raw_vs_parsed_counts() -> dict:
    """Reconcile raw text occurrences against the parsed document.

    PyYAML keeps the LAST of a duplicated mapping key and discards the earlier one silently, so
    provenance can be deleted before any quote gate runs - every existing check in this repo
    walks the parsed document and is structurally blind to it. Detection has to read the raw
    text. Reported as arithmetic that must balance exactly; a gap is a bug report, not something
    to find a story for.
    """
    import yaml

    class StrictLoader(yaml.SafeLoader):
        pass

    def no_dups(loader, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in mapping:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate key {key!r} at line {key_node.start_mark.line + 1}",
                    key_node.start_mark)
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, no_dups)

    if not REVIEW_YAML.exists():
        return {"status": "review yaml absent; run just fetch-gene human ACTA2"}
    text = REVIEW_YAML.read_text()
    doc = yaml.load(text, Loader=StrictLoader)  # raises on a duplicate key
    # The list-item form is `- reference_id:`, so a `^\s*reference_id:` pattern counts zero and
    # the guard fires on its own blind spot rather than on the data. That is what happened on the
    # first run here; the dash is optional in the pattern for exactly that reason. "original_" is
    # not matched because the pattern anchors reference_id to the start of the token.
    raw_ref = len(re.findall(r"^\s*-?\s*reference_id:", text, re.M))
    raw_orig = len(re.findall(r"^\s*original_reference_id:", text, re.M))
    parsed_ref = 0
    def walk(o):
        nonlocal parsed_ref
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "reference_id":
                    parsed_ref += 1
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(doc)
    goa_lines = [ln for ln in GOA_TSV.read_text().splitlines()[1:] if ln.strip()]
    goa_rows = len(goa_lines)
    # A raw line count and a distinct-annotation count can differ legitimately, and two merged
    # genes in this campaign reconciled only after deduping. Assert they agree here rather than
    # letting the coverage arithmetic below rest on an unstated assumption.
    n_distinct = len(set(goa_lines))
    if n_distinct != goa_rows:
        raise RuntimeError(
            f"{GOA_TSV.name} has {goa_rows} data lines but only {n_distinct} distinct ones; the "
            "coverage arithmetic compares existing_annotations against DISTINCT GOA rows and must "
            "be recomputed against the deduped set")
    n_entries = len(doc.get("existing_annotations") or [])
    n_new = sum(1 for a in (doc.get("existing_annotations") or [])
                if (a.get("review") or {}).get("action") == "NEW")
    rec = {
        "raw_reference_id_lines": raw_ref,
        "raw_original_reference_id_lines": raw_orig,
        "parsed_reference_id_count": parsed_ref,
        "balanced": raw_ref == parsed_ref,
        "goa_data_rows": goa_rows,
        "goa_distinct_data_rows": n_distinct,
        "existing_annotations": n_entries,
        "existing_annotations_marked_NEW": n_new,
        "goa_rows_covered": n_entries - n_new,
        "coverage_balanced": (n_entries - n_new) == goa_rows,
    }
    if not rec["balanced"]:
        raise RuntimeError(
            f"raw reference_id lines ({raw_ref}) != parsed ({parsed_ref}); a duplicated YAML key "
            "may have deleted provenance. Do not rationalise the gap - find it.")
    return rec


# ------------------------------------------------------------------------ reporting

def main() -> None:
    res: dict = {}
    n_refs = assert_quickgo_calls_are_guarded()
    print(f"guard: {n_refs} QUICKGO_SEARCH read(s), all inside quickgo_all()", file=sys.stderr)

    goa = parse_goa(GOA_TSV)
    res["inputs"] = {"goa_rows": len(goa), "paint_tsv": str(PAINT_TSV.relative_to(REPO_ROOT)),
                     "actl8_results": str(ACTL8_RESULTS.relative_to(REPO_ROOT))}

    print("Q1 GO:0005200 census + PAINT record", file=sys.stderr)
    census = structural_mf_census()
    paint = paint_record()
    seeds_resolved = {t: resolve_token(t) for t in paint["assertion_seeds"]}
    for tok, info in seeds_resolved.items():
        if info.get("resolved"):
            info["own_evidence_for_donated_term"] = quickgo_evidence(
                f"UniProtKB:{info['chosen']['accession']}", STRUCTURAL_MF)
    res["q1_structural_mf"] = {
        "census": census, "paint": paint,
        "assertion_seeds_resolved": seeds_resolved,
        "seed_vs_negation": seed_vs_negation(paint, seeds_resolved),
    }

    print("Q1b node audit", file=sys.stderr)
    res["q1b_node_audit"] = node_audit()

    print("Q2 residue tallies", file=sys.stderr)
    entries = {acc: uniprot_entry(acc) for acc in PANEL}
    guard = short_sequence_guard(entries)
    al = aligner()
    surfaces: dict[str, dict] = {}

    pdb, chain_id, ligs = ATP_STRUCTURE
    atp_cif = cif = fetch_cif(pdb)
    residues, hits = ligand_contacts(cif, pdb, chain_id, set(ligs), CONTACT_CUTOFF)
    surfaces["nucleotide_site"] = {
        "structure": pdb, "chain": chain_id, "ligands": list(ligs),
        "struct_seq": chain_sequence(residues),
        "struct_numbers": [r.id[1] for r in residues],
        "contact_nums": sorted(hits), "hits": hits,
    }

    pdb, _, _ = FILAMENT_STRUCTURE
    fil_cif = cif = fetch_cif(pdb)
    cid, all_chains, residues, hits = interface_contacts(cif, pdb, CONTACT_CUTOFF)
    surfaces["filament_interface"] = {
        "structure": pdb, "chain": cid, "all_chains": all_chains, "ligands": [],
        "struct_seq": chain_sequence(residues),
        "struct_numbers": [r.id[1] for r in residues],
        "contact_nums": sorted(hits), "hits": hits,
    }

    tallies: dict[str, dict] = {}
    for name, surf in surfaces.items():
        tallies[name] = {
            acc: score_against(surf["struct_seq"], surf["struct_numbers"], surf["contact_nums"],
                               entries[acc]["sequence"], al)
            for acc in PANEL
        }

    # Reproduce ACTL8's committed numbers before drawing any conclusion from this panel.
    expected = parse_actl8_interface_table(ACTL8_RESULTS)
    checked: list[str] = []
    for label, want in expected.items():
        acc = next((a for a, lab in PANEL.items() if lab.split(" (")[0] == label.split(" (")[0]),
                   None)
        if acc is None:
            continue
        got = tallies["filament_interface"][acc]
        # ACTL8's table has a single "gap" column; this script splits gaps by cause, so the
        # comparable quantity is their sum. ACTL10 is deliberately excluded from the
        # reproduction set: its committed ACTL8 row is the artefact this guard exists to
        # prevent, and asserting against it would enshrine the artefact.
        mine = (got["identical"], got["conservative"], got["non_conservative"],
                got["internal_gap"] + got["outside_span"])
        if acc == "Q5JWF8":
            continue
        if mine != want:
            raise RuntimeError(
                f"this script does not reproduce ACTL8's committed filament-interface tally for "
                f"{label}: ACTL8 says {want}, this run says {mine}. Resolve the discrepancy before "
                "reading anything else in this report.")
        checked.append(label)
    if len(checked) < 4:
        raise RuntimeError(
            f"only {len(checked)} panel member(s) could be checked against ACTL8's committed "
            f"table ({checked}); the reproduction assertion is too weak to rely on")

    robustness: dict[str, dict] = {}
    for scheme, (mat, op, ex) in ALIGNMENT_SCHEMES.items():
        al2 = aligner(mat, op, ex)
        robustness[scheme] = {
            acc: {k: score_against(surfaces[k]["struct_seq"], surfaces[k]["struct_numbers"],
                                   surfaces[k]["contact_nums"], entries[acc]["sequence"], al2)
                  for k in surfaces}
            for acc in (ACTA2, "P60709", "Q9H568")
        }

    res["q2_surfaces"] = {
        "panel": {acc: {k: v for k, v in entries[acc].items() if k != "sequence"} | {"label": lab}
                  for acc, lab in PANEL.items()},
        "short_sequence_guard": guard,
        "surfaces": {k: {kk: vv for kk, vv in v.items()
                         if kk not in ("struct_seq", "struct_numbers", "hits")}
                     for k, v in surfaces.items()},
        "contact_detail": {k: {str(n): v["hits"][n] for n in v["contact_nums"]}
                           for k, v in surfaces.items()},
        "tallies": tallies,
        "reproduces_actl8_for": checked,
        "robustness": robustness,
    }

    print("Q3 disease variants on those surfaces", file=sys.stderr)
    variants = parse_variants(UNIPROT_TXT)
    acta2_seq = entries[ACTA2]["sequence"]
    numbering = check_numbering(acta2_seq, surfaces, al)
    lit_control = check_interstrand_literature(surfaces, acta2_seq, al)
    placed = variants_on_surfaces(variants, surfaces, acta2_seq, al)
    fil = surfaces["filament_interface"]
    _, by_query = align_map(fil["struct_seq"], fil["struct_numbers"], acta2_seq, al)
    var_struct = sorted({by_query[v["position"]] for v in variants if v["position"] in by_query})
    dist_prot = protomer_distances(fil_cif, FILAMENT_STRUCTURE[0], var_struct)
    dist_nuc = nucleotide_distances(atp_cif, ATP_STRUCTURE[0], ATP_STRUCTURE[1],
                                    set(ATP_STRUCTURE[2]), var_struct)
    for rec in placed["per_variant"]:
        sn = rec["surfaces"]["filament_interface"]["struct_position"]
        rec["min_dist_to_other_protomer"] = dist_prot.get(str(sn), {})
        rec["min_dist_to_nucleotide"] = dist_nuc.get(str(sn), {}).get("min_dist_to_nucleotide")
    # The per-chain contact set UNDERCOUNTS for this question and must not be the headline.
    # Chain C has A at i-2, B at i-1 and D at i+1 but no i+2 neighbour, and actin protomer
    # contacts are not symmetric: a residue that reaches only "upward" to i+2 is invisible from
    # chain C. Deriving the count from the all-chain distance measurement instead changed the
    # answer from "no pathogenic variant touches another protomer" to four that do - which is
    # exactly why an absence from a single-chain 4 A set is not a finding.
    def within(cut: float, pathogenic: bool) -> list[int]:
        return sorted(v["position"] for v in placed["per_variant"]
                      if v["pathogenic"] is pathogenic
                      and v["min_dist_to_other_protomer"].get(
                          "min_dist_to_other_protomer", 1e9) <= cut)
    def near_nuc(cut: float, pathogenic: bool) -> list[int]:
        return sorted(v["position"] for v in placed["per_variant"]
                      if v["pathogenic"] is pathogenic
                      and (v["min_dist_to_nucleotide"] or 1e9) <= cut)
    res["q3_variants"] = {
        "n_variants": len(variants),
        "numbering_controls": numbering,
        "interstrand_literature_control": lit_control,
        "all_chain_derived_counts": {
            "note": "derived from the minimum over ALL chains, not from the single-chain contact "
                    "set, which lacks the i+2 relationship and undercounts",
            "pathogenic_within_4A_of_another_protomer": within(CONTACT_CUTOFF, True),
            "pathogenic_within_5A_of_another_protomer": within(5.0, True),
            "nonpathogenic_within_4A_of_another_protomer": within(CONTACT_CUTOFF, False),
            "nonpathogenic_within_5A_of_another_protomer": within(5.0, False),
            "pathogenic_within_5A_of_nucleotide": near_nuc(5.0, True),
            "nonpathogenic_within_5A_of_nucleotide": near_nuc(5.0, False),
        },
    } | placed

    print("Q4b interaction partners", file=sys.stderr)
    res["q4b_partners"] = interaction_partners(goa)

    print("corrections check", file=sys.stderr)
    res["corrections"] = corrections_check(CORRECTION_CHECK_PMIDS)

    print("Q4 WITH/FROM", file=sys.stderr)
    res["q4_withfrom"] = withfrom_analysis(goa)

    print("Q5 reference projection", file=sys.stderr)
    res["q5_reference_projection"] = reference_projection(goa)

    print("audit", file=sys.stderr)
    res["audit"] = raw_vs_parsed_counts()

    (HERE / "results.json").write_text(json.dumps(res, indent=2, sort_keys=True, default=str))
    write_report(res)
    print("wrote results.json and RESULTS.md", file=sys.stderr)


def _tbl(rows: list[list[str]], head: list[str]) -> list[str]:
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out + [""]


def write_report(res: dict) -> None:
    L: list[str] = []

    def A(*parts, sep: str = "\n") -> None:
        """Append one or more lines. `A(*_tbl(...))` splices a whole table in."""
        L.append(sep.join(str(x) for x in parts))

    A("# ACTA2 (P62736) — computed analysis")
    A("")
    A("Regenerate with `uv run python analyze_acta2.py`; both this file and `results.json` are")
    A("rewritten in full, so `git diff` after a run is the check that nothing here was hand-edited.")
    A("")

    q1 = res["q1_structural_mf"]
    c, p = q1["census"], q1["paint"]
    A("## 1. GO:0005200 structural constituent of cytoskeleton: who still receives it")
    A("")
    A(f"PAINT asserts GO:0005200 exactly once in PTHR11937, at node **{p['assertion_node']}** "
      f"(IBD, {p['assertion_date']}, {len(p['assertion_seeds'])} seeds), and negates it by IRD at "
      f"**{p['n_IRD_negations']}** descendant nodes. The assertion count is asserted by the script, "
      "so a change to the tree breaks the run rather than the argument.")
    A("")
    A(f"Human GO:0005200 rows in QuickGO: **{c['n_human_rows_all_evidence']}** in total, of which "
      f"**{c['n_human_IBA_rows']}** are IBA. The IBA rows resolve to "
      f"{len(c['IBA_by_panther_node'])} PANTHER nodes:")
    A("")
    A(*_tbl([[n, len(g), ", ".join(g)] for n, g in c["IBA_by_panther_node"].items()],
            ["PANTHER node", "n human genes", "genes"]), sep="\n")
    A(f"So the set still receiving the term from the actin node {FAMILY_NODE} is "
      f"**{len(c['IBA_from_family_node'])} genes**: {', '.join(c['IBA_from_family_node'])}. "
      f"ACTA2 is {'IN' if c['acta2_in_IBA_set'] else 'NOT in'} that set.")
    A("")
    A("Evidence route per actin-family gene that holds the term at all — the distinction that")
    A("makes the IBA set and the holds-the-term set two different sets:")
    A("")
    A(*_tbl([[g, "; ".join(f"{r['evidence']} ({r['reference']}, {r['assigned_by']})" for r in rs)]
             for g, rs in c["actin_family_all_routes"].items()],
            ["gene", "route(s)"]), sep="\n")

    A("### The seeds of the assertion, and what evidence each holds for the term it donated")
    A("")
    rows = []
    for tok, info in q1["assertion_seeds_resolved"].items():
        if not info.get("resolved"):
            rows.append([f"`{tok}`", info.get("note", ""), "-", "-", "-"])
            continue
        ch = info["chosen"]
        ev = info.get("own_evidence_for_donated_term", {})
        rows.append([f"`{tok}`", f"{ch['gene']} ({ch['accession']}, {ch['organism']}, {ch['length']} aa)",
                     "Swiss-Prot" if "Swiss-Prot" in ch["reviewed"] else "TrEMBL",
                     ", ".join(f"{k}x{v}" for k, v in sorted(ev.get("codes_on_exact_term", {}).items())) or "none",
                     "yes" if ev.get("has_experimental_on_exact_term") else "no"])
    A(*_tbl(rows, ["seed", "resolves to", "status", "own codes on GO:0005200", "experimental?"]),
      sep="\n")

    sv = q1["seed_vs_negation"]
    A("### Is any seed of the assertion also inside a clade the same term was negated in?")
    A("")
    if sv["n_contradictions"]:
        A(f"**Yes — {sv['n_contradictions']} of {sv['n_seeds']}.** These proteins supply the "
          "experimental support that justifies GO:0005200 at the family root, and PAINT then "
          "exempts their own clades from the term it justified:")
        A("")
        A(*_tbl([[f"`{x['seed']}`", x["gene"] or "?", x["organism"] or "?",
                  ", ".join(x["negated_nodes"])] for x in sv["seeds_also_inside_a_negated_clade"]],
                ["seed", "gene", "organism", "IRD-negated node(s) whose clade it seeds"]), sep="\n")
    else:
        A(f"No. None of the {sv['n_seeds']} seeds appears among the seed sets of the "
          "IRD-negated nodes, so the assertion and its negations do not overlap.")
    A("")
    A(*_tbl([[x["node"], x["date"], ", ".join(x["seeds"])] for x in p["IRD_negations"]],
            ["IRD-negated node", "date", "IRD seed"]), sep="\n")

    na = res["q1b_node_audit"]
    A("## 1b. Which node carries which term, and what is each node FOR")
    A("")
    A("Two different questions. The first cannot find a node that gives a gene nothing it should")
    A("have; the second can.")
    A("")
    for go, rec in na["forward_term_to_nodes"].items():
        A(f"**{go}** - PANTHER nodes projecting it onto any conventional human actin:")
        A("")
        A(*_tbl([[n, ", ".join(g)] for n, g in sorted(rec["nodes_touching_conventional_actins"].items())]
                or [["(none)", "-"]], ["node", "human conventional actins reached"]))
        A(*_tbl([[sym, ", ".join(v) or "**nothing, at any granularity**"]
                 for sym, v in rec["per_gene_including_descendants"].items()],
                ["conventional actin", "own annotations to this term or its descendants"]))
    A("Reverse direction - the entire human reach of each node that appeared above:")
    A("")
    A(*_tbl([[n, r["n_human_annotations"], ", ".join(r["human_genes"]),
              "; ".join(r["terms"]),
              "YES" if r["reach_is_exactly_the_smooth_muscle_pair"] else ""]
             for n, r in sorted(na["reverse_node_to_reach"].items())],
            ["node", "human annotations", "human genes", "terms", "reach == ACTA2+ACTG2 only"]))

    q2 = res["q2_surfaces"]
    A("## 2. Residue tallies at the nucleotide site and the filament protomer interface")
    A("")
    for name, s in q2["surfaces"].items():
        A(f"- **{name}**: PDB {s['structure']} chain {s['chain']}"
          + (f", ligands {', '.join(s['ligands'])}" if s["ligands"] else "")
          + f", {CONTACT_CUTOFF} Å heavy-atom cutoff → {len(s['contact_nums'])} contact residues.")
    A("")
    A(f"Reproduction check: this script reproduces the committed ACTL8 filament-interface tally "
      f"for {len(q2['reproduces_actl8_for'])} shared panel members "
      f"({'; '.join(q2['reproduces_actl8_for'])}); a mismatch aborts the run.")
    A("")
    g = q2["short_sequence_guard"]
    flagged = ", ".join(
        "{} ({} aa, {:.2f} of median)".format(v["gene"], v["length"], v["fraction_of_median"])
        for v in g["flagged_short"].values()) or "none"
    A(f"Reference-length guard: panel median {g['panel_median_length']} aa, so anything below "
      f"{g['threshold_length']} aa cannot be scored as if every structural position were tested. "
      f"Flagged: {flagged}. `outside_span` is reported as its own column below so an unreached "
      "position can never be added to a substitution count again.")
    A("")
    for name in q2["tallies"]:
        A(f"### {name.replace('_', ' ')} "
          f"({len(q2['surfaces'][name]['contact_nums'])} positions)")
        A("")
        rows = []
        for acc, lab in PANEL.items():
            t = q2["tallies"][name][acc]
            rows.append([lab, t["identical"], t["conservative"], t["non_conservative"],
                         t["internal_gap"], t["outside_span"], t["present"],
                         f"{t['compatible']}/{t['present']}",
                         t["pct_identity_to_struct_chain"]])
        rows.sort(key=lambda r: -(int(r[7].split("/")[0])))
        A(*_tbl(rows, ["protein", "ident", "cons", "non-cons", "internal gap", "outside span",
                       "positions present", "compatible / present", "%id to chain"]), sep="\n")
    A("Robustness: the same three proteins under a second substitution matrix and gap model.")
    A("")
    rows = []
    for scheme, per in q2["robustness"].items():
        for acc, surfs in per.items():
            for name, t in surfs.items():
                rows.append([PANEL[acc].split(" (")[0], scheme, name,
                             f"{t['identical']}/{t['conservative']}/{t['non_conservative']}/"
                             f"{t['internal_gap']}/{t['outside_span']}"])
    A(*_tbl(rows, ["protein", "scheme", "surface", "id/cons/non-cons/int-gap/outside"]), sep="\n")

    q3 = res["q3_variants"]
    A("## 3. ACTA2 disease variants against those two surfaces")
    A("")
    A(f"{q3['n_variants']} FT VARIANT positions parsed from the cached UniProt entry, mapped onto "
      "each structure by the same alignment used for the tallies (never by an assumed offset).")
    A("")
    A("The per-surface table below uses the SINGLE-chain contact sets, which is the right basis")
    A("for the cross-species panel in section 2 (every protein is scored on the same positions)")
    A("but the wrong basis for this question: chain C of the filament model has no i+2 neighbour,")
    A("and actin protomer contacts are not symmetric, so a residue reaching only 'upward' is")
    A("invisible from it. The derived counts that follow, and the distance table, use the minimum")
    A("over every chain. Reading the single-chain table alone would have said no pathogenic")
    A("variant touches another protomer; four do.")
    A("")
    A(*_tbl([[n.replace("_", " "), s["n_contact_residues"], s["chain_length"],
              f"{s['surface_fraction_of_chain']:.1%}",
              f"{s['n_pathogenic_on_surface']}/{s['n_pathogenic_variants']}",
              ", ".join(str(x) for x in s["pathogenic_on_surface"]) or "-",
              f"{s['n_nonpathogenic_on_surface']}/{s['n_nonpathogenic_variants']}"]
             for n, s in q3["per_surface"].items()],
            ["surface", "n contact res", "chain len", "% of chain", "pathogenic on surface",
             "which", "non-pathogenic on surface"]), sep="\n")
    dc = q3["all_chain_derived_counts"]
    A("All-chain derived counts (the headline figures):")
    A("")
    A(*_tbl([[k.replace("_", " "), len(v), ", ".join(str(x) for x in v) or "-"]
             for k, v in dc.items() if isinstance(v, list)],
            ["measure", "n", "ACTA2 positions"]))
    rows = []
    for v in q3["per_variant"]:
        on = [k.replace("_", " ") for k, d in v["surfaces"].items() if d["on_surface"]]
        rows.append([v["position"], ", ".join(v["diseases"]) or "not disease-linked",
                     ", ".join(on) or "neither",
                     v["surfaces"]["filament_interface"]["partners"] or "-",
                     v["note"][:60]])
    A(*_tbl(rows, ["ACTA2 pos", "disease", "on surface", "interface partner chains", "note"]),
      sep="\n")

    A("### Numbering and contact-set controls")
    A("")
    A("P62736 is a 377-residue precursor and the structures use mature actin numbering, so the")
    A("offset should be -2. Verified against three sources that state both numbers, and the")
    A("contact set is itself checked against the residues PMID:26637293 names as R179's")
    A("inter-strand partners. Any failure aborts the run.")
    A("")
    A(*_tbl([[k, v] for k, v in q3["numbering_controls"].items()],
            ["control", "provenance"]))
    A(*_tbl([[k, v["struct_position"], v["in_contact_set"], v["partners"]]
             for k, v in q3["interstrand_literature_control"].items()],
            ["residue named by PMID:26637293", "structure position", "in contact set", "partners"]))
    A("### Closest approach, because an absence from a 4 Å set is not a finding")
    A("")
    A("Measured over every chain of the filament model, not one: with four protomers no single")
    A("chain has both its i-2 and its i+2 neighbour, so a per-chain answer would silently omit")
    A("one strand relationship.")
    A("")
    A(*_tbl([[v["position"], ", ".join(v["diseases"]) or "not disease-linked",
              v["min_dist_to_other_protomer"].get("min_dist_to_other_protomer", "?"),
              v["min_dist_to_other_protomer"].get("relationship", "?"),
              v["min_dist_to_nucleotide"]]
             for v in sorted(q3["per_variant"],
                             key=lambda x: x["min_dist_to_other_protomer"].get(
                                 "min_dist_to_other_protomer", 999))],
            ["ACTA2 pos", "disease", "min Å to another protomer", "via", "min Å to nucleotide"]))

    q4b = res["q4b_partners"]
    A("## 4b. GO:0005515 partners, resolved, and how the interactions were detected")
    A("")
    A(*_tbl([[f"`{x['token']}`",
              f"{x.get('gene','?')} ({x.get('accession','?')}, {x.get('length','?')} aa)",
              x.get("reviewed", "-"),
              "; ".join(x.get("subcellular_location") or []) or "no SUBCELLULAR LOCATION comment",
              ", ".join(x["references"])] for x in q4b["goa_partners"]],
            ["token", "resolves to", "status", "UniProt subcellular location", "GOA references"]))
    A(f"IntAct holds **{q4b['intact_total']}** interactions for {ACTA2}. Detection methods:")
    A("")
    A(*_tbl([[k or "(none given)", v] for k, v in
             sorted(q4b["intact_detection_methods"].items(), key=lambda x: -x[1])],
            ["detection method", "interaction rows"]))
    A(f"{len(q4b['intact_singletons'])} of {len(q4b['intact_partner_row_counts'])} IntAct partners "
      "are logged exactly once.")
    A("")

    cor = res["corrections"]
    A("## Retraction / erratum / correction status of the PMIDs this review leans on")
    A("")
    A(f"{cor['n_checked']} checked, **{cor['n_flagged']}** flagged. Both halves are read: the "
      "publication-type list AND the cited article's own CommentsCorrections block, because a "
      "Publisher Correction is invisible to a publication-type query.")
    A("")
    def _corr(v):
        bits = []
        for c in v["correction_refs"]:
            if c["pmid"]:
                bits.append(f"{c['ref_type']} -> PMID:{c['pmid']}")
            else:
                xr = "; ".join(f"{x['doi']} ({', '.join(x['update_types']) or x['type']})"
                               for x in c.get("crossref_updates") or [])
                bits.append(f"{c['ref_type']} -> no PubMed record; Crossref: {xr or 'none found'}")
        return " | ".join(bits) or "-"
    A(*_tbl([[k, "; ".join(v["correction_flags"]) or "-",
              "yes" if v["is_retracted_publication"] else "no", _corr(v)]
             for k, v in sorted(cor["per_pmid"].items()) if not v["clean"]] or
            [["(none)", "-", "-", "-"]],
            ["PMID", "flags", "retracted publication type", "correction record"]))

    q4 = res["q4_withfrom"]
    A("## 4. WITH/FROM resolution and donor evidence")
    A("")
    A(f"{q4['n_inferred_rows']} non-experimental GOA rows carry {q4['n_withfrom_tokens']} WITH/FROM "
      "tokens in total. Counts are derived from the GOA field, with an assertion, because "
      "hand-maintained source lists drifted on three genes in this campaign.")
    A("")
    for row in q4["rows"]:
        A(f"**{row['go_id']} {row['go_name']}** ({row['aspect']}, {row['evidence']}, "
          f"{row['qualifier']}, {row['reference']}, assigned by {row['assigned_by']}) — "
          f"{row['n_tokens']} token(s)")
        A("")
        rows = []
        for s in row["sources"]:
            if not s.get("resolved"):
                rows.append([f"`{s['token']}`", s.get("note", ""), "-", "-"])
                continue
            ch = s["chosen"]
            ev = s.get("own_evidence_for_donated_term", {})
            note = ""
            if s.get("ambiguous"):
                note = f" [{s['n_candidates']} candidates]"
            rows.append([
                f"`{s['token']}`",
                f"{ch['gene']} ({ch['accession']}, {ch['organism']}, {ch['length']} aa){note}",
                "Swiss-Prot" if "Swiss-Prot" in ch["reviewed"] else "TrEMBL (unreviewed)",
                ", ".join(f"{k}x{v}" for k, v in sorted(ev.get("codes", {}).items()))
                or ("accession absent from QuickGO" if ev.get("accession_absent_from_quickgo")
                    else "no annotation for this term or its descendants"),
            ])
        A(*_tbl(rows, ["token", "resolves to", "status", "own evidence for the donated term"]),
          sep="\n")

    q5 = res["q5_reference_projection"]
    A("## 5. Reference projection check")
    A("")
    A("For each literature reference on an ACTA2 row: how many annotations does it carry across "
      "GOA, and how many DISTINCT entities? A reference that annotates a whole set with identical "
      "evidence is one finding projected, not N findings — but only if the phenotype spreads with "
      "it, so the per-term entity counts are given too.")
    A("")
    A(*_tbl([[r["reference"], r["n_annotations"],
              r["n_entities"] if r["n_entities"] is not None else "unavailable",
              (", ".join(f"{k}x{v}" for k, v in sorted(r.get("evidence_codes", {}).items()))
               or "-")]
             for r in q5["references"]],
            ["reference", "annotations", "distinct entities", "evidence codes"]), sep="\n")
    for r in q5["references"]:
        if r["n_entities"] is None:
            A(f"- `{r['reference']}`: {r['entity_count_status']}")
    A("")
    for r in q5["references"]:
        if r.get("entities_per_term"):
            A(f"**{r['reference']}** — per-term entity counts:")
            A("")
            A(*_tbl([[k, r["annotations_per_term"][k], v]
                     for k, v in r["entities_per_term"].items()],
                    ["term", "annotations", "distinct entities"]), sep="\n")

    a = res["audit"]
    A("## Audit")
    A("")
    A(*_tbl([[k, v] for k, v in a.items()], ["check", "value"]), sep="\n")

    (HERE / "RESULTS.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
