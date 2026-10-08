#!/usr/bin/env python3
"""Does the Pcbd2-specific N-terminal extension look like a mitochondrial targeting sequence?

Context
-------
Mouse Pcbd2 (Q9CZL5) is 136 aa; mouse Pcbd1 (P61458) is 104 aa. The extra ~32
residues sit at the N-terminus of Pcbd2 and are absent from Pcbd1. The two
crystal structures of Pcbd2 (PDB 1RU0, 4WIL) both start at residue 33/34, so the
extension is disordered or absent in the crystallised protein. GOA carries a
single HDA `located_in mitochondrion` annotation for Pcbd2 (PMID:18614015,
MitoCarta), which UniProt has not adopted (its SUBCELLULAR LOCATION lists only
Cytoplasm and Nucleus). This script asks whether the extension carries the
sequence features of a cleavable mitochondrial presequence.

Method
------
Classical N-terminal mitochondrial targeting sequences (MTS) are short,
Arg-rich, essentially free of acidic residues, and form an amphipathic helix
(Roise & Schatz; von Heijne). Rather than assert a threshold, we benchmark each
feature on two UniProt-derived mouse reference sets and report where Pcbd2's
extension falls in each distribution:

  positives  reviewed mouse proteins with an experimentally/annotation-backed
             TRANSIT "Mitochondrion" feature; we score the annotated transit
             peptide itself.
  negatives  reviewed mouse proteins annotated to the cytosol (SL-0091) with no
             transit peptide, no signal peptide and no transmembrane region; we
             score their first N residues.

Features (computed over a sequence window):
  net_charge    (K + R) - (D + E)
  n_arg         Arg count
  n_acidic      Asp + Glu count
  frac_ser_thr  Ser+Thr fraction (enriched in presequences)
  frac_ala      Ala fraction. Reported as a confounder control, not as an MTS
                feature: the Pcbd2 extension is Ala-rich, and any low-complexity
                Ala tract will lack acidic residues for reasons that have
                nothing to do with targeting.
  mu_h_max      maximum mean hydrophobic moment over any 18-residue
                sub-window, using the Eisenberg consensus scale and 100
                degrees per residue -- the standard amphipathicity measure.

Nothing is hardcoded: every number in RESULTS.md comes from a run of this file.
If the UniProt REST API is unreachable the script exits non-zero rather than
emitting made-up values.

Usage
-----
    uv run python nterm_mts_analysis.py            # writes results.json
    uv run python nterm_mts_analysis.py --refresh  # ignore the local cache

Python 3.12 standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
CACHE = HERE / "data"

# Eisenberg et al. (1984) normalised consensus hydrophobicity scale.
EISENBERG = {
    "A": 0.62, "R": -2.53, "N": -0.78, "D": -0.90, "C": 0.29,
    "Q": -0.85, "E": -0.74, "G": 0.48, "H": -0.40, "I": 1.38,
    "L": 1.06, "K": -1.50, "M": 0.64, "F": 1.19, "P": 0.12,
    "S": -0.18, "T": -0.05, "W": 0.81, "Y": 0.26, "V": 1.08,
}

# The Pcbd2 extension is residues 1..32 (Pcbd1 residue 1 aligns to Pcbd2 ~33).
# Window length used for every sequence so the comparison is like-for-like.
WINDOW = 32
MOMENT_WINDOW = 18
DEG_PER_RESIDUE = 100.0
REFSET_SIZE = 300

FOCUS = {
    "Q9CZL5": "mouse Pcbd2 (DCoH2)",
    "P61458": "mouse Pcbd1 (DCoH)",
    "Q9H0N5": "human PCBD2",
    "P61457": "human PCBD1",
}


def http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/Pcbd2-bioinformatics"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8")


def cached_get(url: str, name: str, refresh: bool) -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / name
    if path.exists() and not refresh:
        return path.read_text()
    try:
        body = http_get(url)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        sys.exit(f"ERROR: UniProt REST request failed for {name}: {exc}\n"
                 f"  URL: {url}\n"
                 f"  No cached copy available; refusing to emit results.")
    path.write_text(body)
    return body


def uniprot_search(query: str, fields: str, size: int, name: str, refresh: bool) -> list[dict]:
    """Page through the UniProt REST search endpoint (cached as one JSON file)."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / name
    if path.exists() and not refresh:
        return json.loads(path.read_text())

    collected: list[dict] = []
    params = urllib.parse.urlencode(
        {"query": query, "fields": fields, "format": "json", "size": min(size, 500)}
    )
    url = f"https://rest.uniprot.org/uniprotkb/search?{params}"
    while url and len(collected) < size:
        req = urllib.request.Request(
            url, headers={"User-Agent": "ai-gene-review/Pcbd2-bioinformatics"}
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
                link = resp.headers.get("Link", "")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            sys.exit(f"ERROR: UniProt REST search failed for {name}: {exc}")
        collected.extend(payload.get("results", []))
        url = ""
        if 'rel="next"' in link:
            url = link.split("<", 1)[1].split(">", 1)[0]
    collected = collected[:size]
    path.write_text(json.dumps(collected))
    return collected


def entry_sequence(entry: dict) -> str:
    return entry.get("sequence", {}).get("value", "")


def transit_peptide(entry: dict) -> tuple[int, int] | None:
    """Return (start, end) 1-based of a mitochondrial TRANSIT feature, if any."""
    for feat in entry.get("features", []):
        if feat.get("type") != "Transit peptide":
            continue
        desc = (feat.get("description") or "").lower()
        if "mitochond" not in desc:
            continue
        loc = feat.get("location", {})
        start = loc.get("start", {}).get("value")
        end = loc.get("end", {}).get("value")
        if isinstance(start, int) and isinstance(end, int) and end > start:
            return start, end
    return None


def hydrophobic_moment(seq: str) -> float:
    """Mean hydrophobic moment <mu_H> of a helical segment (Eisenberg 1982)."""
    if not seq:
        return float("nan")
    radians = math.radians(DEG_PER_RESIDUE)
    sin_sum = sum(EISENBERG.get(aa, 0.0) * math.sin(i * radians) for i, aa in enumerate(seq))
    cos_sum = sum(EISENBERG.get(aa, 0.0) * math.cos(i * radians) for i, aa in enumerate(seq))
    return math.hypot(sin_sum, cos_sum) / len(seq)


def max_moment(seq: str) -> float:
    if len(seq) < MOMENT_WINDOW:
        return hydrophobic_moment(seq)
    return max(
        hydrophobic_moment(seq[i : i + MOMENT_WINDOW])
        for i in range(len(seq) - MOMENT_WINDOW + 1)
    )


def features(seq: str) -> dict[str, float]:
    n = len(seq)
    if n == 0:
        return {}
    basic = seq.count("K") + seq.count("R")
    acidic = seq.count("D") + seq.count("E")
    return {
        "length": n,
        "net_charge": basic - acidic,
        "n_arg": seq.count("R"),
        "n_acidic": acidic,
        "frac_ser_thr": round((seq.count("S") + seq.count("T")) / n, 4),
        "frac_ala": round(seq.count("A") / n, 4),
        "mu_h_max": round(max_moment(seq), 4),
    }


def percentile_of(value: float, population: list[float]) -> float | None:
    """Fraction of the population strictly below `value` (0-100)."""
    pop = [v for v in population if v == v]  # drop NaN
    if not pop:
        return None
    below = sum(1 for v in pop if v < value)
    ties = sum(1 for v in pop if v == value)
    return round(100.0 * (below + 0.5 * ties) / len(pop), 1)


def summarise(population: list[float]) -> dict[str, float]:
    pop = sorted(v for v in population if v == v)
    if not pop:
        return {}

    def q(p: float) -> float:
        idx = (len(pop) - 1) * p
        lo, hi = math.floor(idx), math.ceil(idx)
        return round(pop[lo] + (pop[hi] - pop[lo]) * (idx - lo), 4)

    return {"n": len(pop), "p10": q(0.10), "median": q(0.50), "p90": q(0.90)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refresh", action="store_true", help="bypass the local cache")
    args = ap.parse_args()

    out: dict = {
        "method": {
            "window": WINDOW,
            "moment_window": MOMENT_WINDOW,
            "degrees_per_residue": DEG_PER_RESIDUE,
            "hydrophobicity_scale": "Eisenberg normalised consensus (1984)",
            "refset_target_size": REFSET_SIZE,
        },
        "focus": {},
        "reference_sets": {},
        "percentiles": {},
        "orthologs": {},
    }

    # ---- focus proteins -------------------------------------------------
    fields = "accession,id,protein_name,sequence,ft_transit,organism_name"
    for acc, label in FOCUS.items():
        entry = json.loads(
            cached_get(
                f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields={fields}",
                f"{acc}.json",
                args.refresh,
            )
        )
        seq = entry_sequence(entry)
        out["focus"][acc] = {
            "label": label,
            "uniprot_id": entry.get("uniProtkbId"),
            "length": len(seq),
            "sha256": hashlib.sha256(seq.encode()).hexdigest()[:16],
            "nterm_window": seq[:WINDOW],
            "features": features(seq[:WINDOW]),
            "uniprot_mito_transit_annotated": transit_peptide(entry) is not None,
        }

    # ---- reference sets -------------------------------------------------
    positives = uniprot_search(
        "(organism_id:10090) AND (reviewed:true) AND (ft_transit:mitochondrion)",
        "accession,sequence,ft_transit",
        REFSET_SIZE,
        "positives.json",
        args.refresh,
    )
    negatives = uniprot_search(
        "(organism_id:10090) AND (reviewed:true) AND (cc_scl_term:SL-0091) "
        "AND NOT (ft_transit:*) AND NOT (ft_signal:*) AND NOT (ft_transmem:*)",
        "accession,sequence",
        REFSET_SIZE,
        "negatives.json",
        args.refresh,
    )

    pos_feats, neg_feats = [], []
    for entry in positives:
        seq = entry_sequence(entry)
        span = transit_peptide(entry)
        if not seq or not span:
            continue
        # Score the annotated presequence, capped at WINDOW for comparability.
        tp = seq[span[0] - 1 : span[1]][:WINDOW]
        if len(tp) >= MOMENT_WINDOW:
            pos_feats.append(features(tp))
    for entry in negatives:
        seq = entry_sequence(entry)
        if len(seq) >= WINDOW:
            neg_feats.append(features(seq[:WINDOW]))

    keys = ["net_charge", "n_arg", "n_acidic", "frac_ser_thr", "frac_ala", "mu_h_max"]
    out["reference_sets"] = {
        "positives": {
            "description": "reviewed mouse proteins with a UniProt TRANSIT "
                           "'Mitochondrion' feature; the presequence itself is scored",
            "n_scored": len(pos_feats),
            "stats": {k: summarise([f[k] for f in pos_feats]) for k in keys},
        },
        "negatives": {
            "description": "reviewed mouse cytosolic (SL-0091) proteins without "
                           "transit/signal/transmembrane features; first "
                           f"{WINDOW} residues scored",
            "n_scored": len(neg_feats),
            "stats": {k: summarise([f[k] for f in neg_feats]) for k in keys},
        },
    }

    for acc, rec in out["focus"].items():
        f = rec["features"]
        out["percentiles"][acc] = {
            k: {
                "value": f[k],
                "pct_within_positives": percentile_of(f[k], [p[k] for p in pos_feats]),
                "pct_within_negatives": percentile_of(f[k], [p[k] for p in neg_feats]),
            }
            for k in keys
        }

    # ---- conservation of the extension across PCBD2 orthologs ----------
    orthologs = uniprot_search(
        "(gene:PCBD2) AND (reviewed:true)",
        "accession,id,organism_name,sequence",
        50,
        "pcbd2_orthologs.json",
        args.refresh,
    )
    for entry in orthologs:
        seq = entry_sequence(entry)
        out["orthologs"][entry.get("primaryAccession", "?")] = {
            "uniprot_id": entry.get("uniProtkbId"),
            "organism": entry.get("organism", {}).get("scientificName"),
            "length": len(seq),
            "nterm_window": seq[:WINDOW],
            "features": features(seq[:WINDOW]) if len(seq) >= WINDOW else {},
        }

    (HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
