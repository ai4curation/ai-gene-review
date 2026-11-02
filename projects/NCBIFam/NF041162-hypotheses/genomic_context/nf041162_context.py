#!/usr/bin/env python3
"""Genomic-context check for NCBIFAM NF041162 (family 2A encapsulin shell) members.

Question: do any UniProtKB entries carrying NF041162 sit in a phage/prophage
context rather than an encapsulin operon? Aguilar et al. 2026 (Nat Commun,
PMID:42875451) report HK97-fold viral major capsid proteins
that carry the SrpI-like (family 2) encapsulin Pfam domain, so a blanket
NF041162 -> GO:0140737 (encapsulin nanocompartment) propagation could reach
viral capsids if the equivalog model does not separate them.

Steps (all live queries, raw downloads cached under --cache):
  1. UniProtKB: entries with xref ncbifam-NF041162 (taxonomy, EMBL protein ids).
  2. NCBI protein GenBank: the CDS location (``coded_by``).
  3. NCBI nuccore GenBank for +/- --flank bp around the CDS: neighbouring
     CDS products.
  4. Classify each neighbourhood by regex over product names:
       phage_structural  portal / terminase / tail / baseplate / head-tail ...
       integrase         integrase / excisionase (weak: also genomic islands)
       cargo             cysteine desulfurase / terpene cyclase / encapsulin cargo
Each entry is tried with at most its first two EMBL protein ids (the first
with a resolvable CDS location and nucleotide features is used).
Outputs a per-entry TSV and a summary YAML. Nothing is hardcoded; entries
whose context could not be retrieved are reported as such.

Usage:
    python nf041162_context.py --cache .cache --out .
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

UNIPROT = "https://rest.uniprot.org/uniprotkb/stream"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
UA = "ai-gene-review-ncbifam/1.0"

# "holin-like" is excluded on purpose: in bacterial genomes it names the
# LrgA/CidA murein-hydrolase regulators (paired with LrgB/CidB), not phage
# holins. A bare word-boundary "holin" also avoids matching "choline".
PHAGE_STRUCT = re.compile(
    r"\bportal\b|terminase|\btail\b|baseplate|head[- ]tail|prohead|head morphogenesis|"
    r"phage (?:major )?capsid|virion|\bholin\b(?!-like)|tape measure",
    re.I,
)
INTEGRASE = re.compile(r"integrase|excisionase|recombinase", re.I)
CARGO = re.compile(
    r"cysteine desulfurase|terpene|polyprenyl|encapsulin.*cargo|cargo", re.I
)
PHAGE_WORD = re.compile(r"\bphage\b|prophage", re.I)


def get(url: str, cache: Path, retries: int = 4) -> str:
    if cache.exists():
        return cache.read_text()
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as r:  # noqa: S310
                txt = r.read().decode("utf-8", "replace")
            cache.write_text(txt)
            time.sleep(0.35)  # NCBI: <=3 requests/s without an API key
            return txt
        except Exception:  # noqa: BLE001
            time.sleep(2 ** (i + 1))
    return ""


def uniprot_members(cache: Path) -> list[dict]:
    q = urllib.parse.urlencode(
        {"query": "xref:ncbifam-NF041162", "format": "json",
         "fields": "accession,organism_name,lineage,protein_name,xref_embl"}
    )
    data = json.loads(get(f"{UNIPROT}?{q}", cache / "uniprot_nf041162.json"))
    out = []
    for e in data["results"]:
        pids = [
            p["value"]
            for x in e.get("uniProtKBCrossReferences", [])
            if x["database"] == "EMBL"
            for p in x.get("properties", [])
            if p["key"] == "ProteinId" and p["value"] != "-"
        ]
        lineage = [t if isinstance(t, str) else t["scientificName"] for t in e["organism"].get("lineage", [])]
        out.append({
            "accession": e["primaryAccession"],
            "organism": e["organism"]["scientificName"],
            "superkingdom": lineage[0] if lineage else "",
            "protein_ids": pids,
        })
    return out


def coded_by(pid: str, cache: Path) -> tuple[str, int, int] | None:
    q = urllib.parse.urlencode({"db": "protein", "id": pid, "rettype": "gb"})
    txt = get(f"{EUTILS}?{q}", cache / f"prot_{pid}.gb")
    m = re.search(r'/coded_by="(?:complement\()?(?:join\()?([^:"]+):<?(\d+)\.\.>?(\d+)', txt)
    if not m:
        return None
    return m.group(1), int(m.group(2)), int(m.group(3))


def neighbour_products(nuc: str, start: int, stop: int, flank: int, cache: Path) -> list[str] | None:
    lo, hi = max(1, start - flank), stop + flank
    q = urllib.parse.urlencode(
        {"db": "nuccore", "id": nuc, "rettype": "gb", "seq_start": lo, "seq_stop": hi}
    )
    txt = get(f"{EUTILS}?{q}", cache / f"nuc_{nuc}_{lo}_{hi}.gb")
    if "FEATURES" not in txt:
        return None
    feats = txt.split("FEATURES", 1)[1].split("\nORIGIN", 1)[0]
    prods = []
    for block in re.split(r"\n     (?=\S)", feats):
        if block.startswith("CDS"):
            m = re.search(r'/product="([^"]+)"', block, re.S)
            prods.append(re.sub(r"\s+", " ", m.group(1)) if m else "")
    return prods


def classify(prods: list[str]) -> dict:
    # the encapsulin shell itself is excluded from phage matching
    others = [p for p in prods if "encapsulin" not in p.lower() or "cargo" in p.lower()]
    return {
        "phage_structural": sorted({p for p in others if PHAGE_STRUCT.search(p)}),
        "phage_word": sorted({p for p in others if PHAGE_WORD.search(p)}),
        "integrase": sorted({p for p in others if INTEGRASE.search(p)}),
        "cargo": sorted({p for p in prods if CARGO.search(p)}),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", type=Path, default=Path(".cache"))
    ap.add_argument("--out", type=Path, default=Path("."))
    ap.add_argument("--flank", type=int, default=8000)
    a = ap.parse_args()
    a.cache.mkdir(parents=True, exist_ok=True)

    members = uniprot_members(a.cache)
    rows, counts = [], collections.Counter()
    counts["entries"] = len(members)
    counts["viral_taxonomy"] = sum(m["superkingdom"] == "Viruses" for m in members)
    for m in members:
        row = {**m, "status": "no_embl_protein_id", "n_neighbours": 0}
        for pid in m["protein_ids"][:2]:
            loc = coded_by(pid, a.cache)
            if not loc:
                continue
            prods = neighbour_products(*loc, a.flank, a.cache)
            if prods is None:
                row["status"] = "no_nucleotide_features"
                continue
            row.update(classify(prods), status="ok", n_neighbours=len(prods), contig=loc[0])
            break
        else:
            if m["protein_ids"]:
                row["status"] = row["status"] if row["status"] != "no_embl_protein_id" else "no_cds_location"
        counts[f"status_{row['status']}"] += 1
        if row["status"] == "ok":
            for k in ("phage_structural", "phage_word", "integrase", "cargo"):
                counts[f"with_{k}"] += bool(row[k])
            counts["phage_structural_and_no_cargo"] += bool(row["phage_structural"]) and not row["cargo"]
        rows.append(row)

    cols = ["accession", "organism", "status", "contig", "n_neighbours",
            "cargo", "phage_structural", "integrase", "phage_word"]
    with open(a.out / "nf041162_context.tsv", "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(
                "; ".join(r.get(c, [])) if isinstance(r.get(c), list) else str(r.get(c, ""))
                for c in cols) + "\n")
    with open(a.out / "nf041162_context_summary.yaml", "w") as fh:
        fh.write(f"flank_bp: {a.flank}\n")
        for k, v in sorted(counts.items()):
            fh.write(f"{k}: {v}\n")
        for key in ("phage_structural", "integrase", "phage_word"):
            fh.write(f"{key}_neighbour_entries:\n")
            for r in rows:
                if r.get(key):
                    fh.write(f"  - {r['accession']}\n")
        fh.write("mobile_element_neighbour_without_cargo:\n")
        for r in rows:
            if (r.get("phage_structural") or r.get("integrase")) and not r.get("cargo"):
                fh.write(f"  - {r['accession']}\n")
    print(dict(counts))


if __name__ == "__main__":
    main()
