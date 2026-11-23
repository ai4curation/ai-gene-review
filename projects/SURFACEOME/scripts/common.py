"""Shared helpers for SURFACEOME scoring scripts. Run from the repository root."""
import csv
import collections
import os
import sqlite3
from pathlib import Path

PROJECT = Path("projects/SURFACEOME")
DATA = PROJECT / "data"
RESULTS = PROJECT / "results"
GO_DB = Path(os.path.expanduser("~/.data/oaklib/go.db"))  # oaklib sqlite GO build

_db = None


def go_db():
    global _db
    if _db is None:
        _db = sqlite3.connect(GO_DB)
    return _db


def desc(*roots):
    """is_a/part_of reflexive descendants of the given GO roots."""
    out = set(roots)
    for root in roots:
        out |= {r[0] for r in go_db().execute(
            "select subject from entailed_edge where object=? "
            "and predicate in ('rdfs:subClassOf','BFO:0000050')", (root,))}
    return out


def label(curie):
    row = go_db().execute(
        "select value from statements where subject=? and predicate='rdfs:label'", (curie,)).fetchone()
    return row[0] if row else curie


def benchmark():
    """SurfaceBench truth, one row per gene (keyed by UniProt accession)."""
    truth = {}
    for r in csv.DictReader(open(DATA / "triage-benchmark-with-reasoning.tsv"), delimiter="\t"):
        truth.setdefault(r["uniprot_acc"], r)
    return truth


def reviewed_human():
    """UniProt accession -> gene folder for every genes/human/*/*-ai-review.yaml."""
    out = {}
    for f in Path("genes/human").glob("*/*-ai-review.yaml"):
        for line in open(f):
            if line.startswith("id:"):
                out[line.split()[1].strip()] = f.parent.name
                break
    return out


# GO term sets used by the rules
def term_sets():
    return {
        "OUT_CC": desc("GO:0009986", "GO:0009897"),  # cell surface, external side of PM
        "PM": desc("GO:0005886"),
        "TM_MF": desc("GO:0004888", "GO:0022857", "GO:0015267"),  # TM signaling receptor, TM transporter, channel
        "INNER": desc("GO:0009898", "GO:0031234"),  # cytoplasmic side of PM (+ extrinsic)
        "SIDE": desc("GO:0098552"),  # side of membrane (includes cytoplasmic side)
        "PM_COMPLEX": desc("GO:0098797"),  # plasma membrane protein complex
    }


def counter():
    return collections.Counter()
