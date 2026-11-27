"""Shared helpers for the KRT9 bioinformatics analysis (no results live here)."""
from __future__ import annotations

import csv
import json
import re
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
RESULTS = HERE / "results"
CACHE = HERE / "cache"

HEPTAD = "abcdefg"

THREE2ONE = {
    "Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E",
    "Gly": "G", "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F",
    "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V", "Ter": "*",
    "Sec": "U",
}
THREE2ONE_UPPER = {k.upper(): v for k, v in THREE2ONE.items()}


def load_json(path: Path):
    with open(path) as fh:
        return json.load(fh)


def dump_json(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True)
        fh.write("\n")


def write_tsv(rows: list[dict], path: Path, columns: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if columns is None:
        columns = []
        for r in rows:
            for k in r:
                if k not in columns:
                    columns.append(k)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns, delimiter="\t", extrasaction="ignore",
                           lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: fmt(r.get(k, "")) for k in columns})


def read_tsv(path: Path) -> list[dict]:
    with open(path) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def fmt(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:.4g}"
    if isinstance(v, (list, tuple, set)):
        return ";".join(str(x) for x in v)
    return v


def http_json(session, url, *, params=None, json_body=None, tries=6, pause=1.0, ok404=False):
    """GET/POST returning (json, response); retries on 429/5xx and on eutils rate-limit bodies."""
    last = None
    for attempt in range(tries):
        if json_body is not None:
            r = session.post(url, json=json_body, timeout=120)
        else:
            r = session.get(url, params=params, timeout=120)
        if ok404 and r.status_code == 404:
            return None, r
        if r.status_code == 200:
            try:
                data = r.json()
            except ValueError:
                data = None
            if data is not None and not (isinstance(data, dict) and "API rate limit" in str(data.get("error", ""))):
                return data, r
        last = r
        time.sleep(pause * (attempt + 2))
    raise RuntimeError(f"request failed after {tries} tries: {url} status={last.status_code} body={last.text[:200]}")


# ---------------------------------------------------------------- UniProt helpers
def regions(entry: dict) -> list[dict]:
    """UniProt 'Region' features as dicts with start/end/name."""
    out = []
    for f in entry.get("features", []):
        if f["type"] == "Region":
            out.append({"name": f["description"], "start": f["location"]["start"]["value"],
                        "end": f["location"]["end"]["value"]})
    return out


ARCH_NAMES = ["Head", "Coil 1A", "Linker 1", "Coil 1B", "Linker 12", "Coil 2", "Tail",
              "Rod-like helical tail"]


def architecture(entry: dict) -> list[dict]:
    """The head/rod/tail segmentation UniProt gives for intermediate filament proteins."""
    segs = [r for r in regions(entry) if r["name"] in ARCH_NAMES]
    return sorted(segs, key=lambda r: r["start"])


def domain_of(pos: int, arch: list[dict]) -> str:
    for seg in arch:
        if seg["start"] <= pos <= seg["end"]:
            return seg["name"]
    return "unassigned"


def seg(arch: list[dict], name: str) -> dict | None:
    for s in arch:
        if s["name"] == name:
            return s
    return None


def natural_variants(entry: dict) -> list[dict]:
    out = []
    for f in entry.get("features", []):
        if f["type"] != "Natural variant":
            continue
        alt = f.get("alternativeSequence", {})
        desc = f.get("description", "")
        # "in EPPK1; ..." names a disease; "in dbSNP:rs..." or "in a ... sample" does not
        m = re.match(r"in (?!dbSNP)(?!an? )([^;]+)", desc)
        out.append({
            "start": f["location"]["start"]["value"], "end": f["location"]["end"]["value"],
            "ref": alt.get("originalSequence", ""),
            "alts": alt.get("alternativeSequences", []),
            "description": desc,
            "disease": m.group(1).strip() if m else "",
            "feature_id": f.get("featureId", ""),
            "dbsnp": [x["id"] for x in f.get("featureCrossReferences", []) if x["database"] == "dbSNP"],
            "pubmed": sorted({e["id"] for e in f.get("evidences", []) if e.get("source") == "PubMed"}),
        })
    return out


def gene_name(entry: dict) -> str:
    return entry["genes"][0]["geneName"]["value"] if entry.get("genes") else entry["primaryAccession"]


def protein_name(entry: dict) -> str:
    d = entry["proteinDescription"]
    if "recommendedName" in d:
        return d["recommendedName"]["fullName"]["value"]
    return d["submissionNames"][0]["fullName"]["value"]


# ---------------------------------------------------------------- alignment helpers
def aln_maps(aligned: str) -> tuple[dict[int, int], dict[int, int]]:
    """(residue number 1-based -> column, column -> residue number) for one aligned row."""
    r2c, c2r, n = {}, {}, 0
    for c, ch in enumerate(aligned):
        if ch != "-":
            n += 1
            r2c[n] = c
            c2r[c] = n
    return r2c, c2r
