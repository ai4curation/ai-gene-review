#!/usr/bin/env python3
"""Generate EC-bridge-confirmed NCBIFAM -> GO mapping *candidates* at collection scale.

The hand-curated seed [`ncbifam2go.sssom.yaml`](ncbifam2go.sssom.yaml) is 28 reviewed
rows. This script scales the same idea to the whole NCBIFAM collection using the one
piece of verification that needs no human judgement: the **EC bridge**. For every
NCBIFAM model that carries an EC number, if the public `ec2go` mapping sends that EC
to one of the model's own NCBI-assigned `go_terms`, then NCBIFAM(EC) and ec2go(EC)
*agree* on the GO term -- an automatically confirmed exactMatch candidate.

    NCBIFAM model --(hmm_PGAP EC)--> EC --(ec2go)--> GO   == model's own go_terms

This is the NCBIFAM analog of the RHEA project's EC-bridge-supported rhea2go rows.
The bridge guarantees the GO term matches the enzyme activity; these candidates still
warrant altitude review (an EC can map to a generic GO parent), but they do NOT need
per-row correctness review -- the agreement of two independent curated resources is
the evidence. Rows already in the reviewed seed are flagged.

Output (TSV, written next to this script): one row per (model, EC-confirmed GO):
  subject_id  predicate_id  object_id  ec  family_type  in_seed  product

Mapping justification for every row is ``semapv:CompositeMatching`` (composed via the
EC bridge), distinguishing these generated candidates from the hand-curated
``semapv:ManualMappingCuration`` seed.

Data (live, no auth):
  * NCBIFAM HMM metadata : https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv
  * ec2go                : https://current.geneontology.org/ontology/external2go/ec2go

Usage::

    uv run python ncbifam2go_candidates.py                 # write candidates TSV + stats
    uv run python ncbifam2go_candidates.py --stats-only     # just the funnel numbers
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

HMM_PGAP_URL = "https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv"
EC2GO_URL = "https://current.geneontology.org/ontology/external2go/ec2go"
UA = "ai-gene-review-ncbifam/1.0"

COL_ACCESSION, COL_FAMILY_TYPE, COL_PRODUCT, COL_EC, COL_GO = 0, 6, 10, 13, 14
EC_RE = re.compile(r"^\d+\.\d+\.\d+\.\w+$")


def _fetch(url: str, cache: Path, timeout: int = 120) -> str:
    if not cache.exists():
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
            cache.write_bytes(resp.read())
    return cache.read_text("utf-8", "replace")


def load_ec2go(text: str) -> dict[str, set[str]]:
    """EC number -> set of GO ids, from the ec2go external2go file."""
    out: dict[str, set[str]] = {}
    for line in text.splitlines():
        if not line.startswith("EC:"):
            continue
        m = re.match(r"EC:(\S+)\s+>.*;\s+(GO:\d+)", line)
        if m:
            out.setdefault(m.group(1), set()).add(m.group(2))
    return out


def seed_subjects(seed_path: Path) -> set[str]:
    """Versionless NCBIFAM accessions already in the reviewed SSSOM seed."""
    if not seed_path.exists():
        return set()
    import yaml

    doc = yaml.safe_load(seed_path.read_text())
    return {
        m["subject_id"].split(":")[1].split(".")[0]
        for m in doc.get("mappings", [])
        if str(m.get("subject_id", "")).startswith("NCBIFAM:")
    }


def main(argv=None) -> int:
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hmm-cache", type=Path, default=Path("/tmp/hmm_PGAP.tsv"))
    ap.add_argument("--ec2go-cache", type=Path, default=Path("/tmp/ec2go.txt"))
    ap.add_argument("--out", type=Path, default=here / "ncbifam2go.candidates.tsv")
    ap.add_argument("--stats-only", action="store_true")
    args = ap.parse_args(argv)

    ec2go = load_ec2go(_fetch(EC2GO_URL, args.ec2go_cache, 60))
    in_seed = seed_subjects(here / "ncbifam2go.sssom.yaml")
    hmm = _fetch(HMM_PGAP_URL, args.hmm_cache).splitlines()

    n_go = n_ec_and_go = n_refine = 0
    rows: list[tuple[str, str, str, str, str, str]] = []
    bridged_models: set[str] = set()
    for line in hmm[1:]:
        c = line.split("\t")
        if len(c) <= COL_GO:
            continue
        acc, ftype, prod = c[COL_ACCESSION], c[COL_FAMILY_TYPE], c[COL_PRODUCT]
        gos = [t for t in c[COL_GO].replace(",", " ").split() if t.startswith("GO:")]
        ecs = [
            e.strip()
            for e in c[COL_EC].replace(",", " ").split()
            if EC_RE.match(e.strip())
        ]
        if gos:
            n_go += 1
        if gos and ecs:
            n_ec_and_go += 1
        if not (gos and ecs):
            continue
        targets: set[str] = set()
        for e in ecs:
            targets |= ec2go.get(e, set())
        confirmed = [(g, e) for g in gos for e in ecs if g in ec2go.get(e, set())]
        if not confirmed:
            # ec2go HAS a GO target for the EC but NCBI's go_terms does not include it:
            # ec2go would refine/replace NCBI's term (the spermidine-synthase pattern).
            if targets:
                n_refine += 1
            continue
        bridged_models.add(acc)
        base = acc.split(".")[0]
        seen: set[str] = set()
        for go, ec in confirmed:
            if go in seen:
                continue
            seen.add(go)
            rows.append(
                (
                    f"NCBIFAM:{base}",
                    go,
                    ec,
                    ftype,
                    "yes" if base in in_seed else "",
                    prod[:70],
                )
            )

    rows.sort()
    print("# NCBIFAM -> GO EC-bridge candidate funnel (live)")
    print(f"#   GO-bearing NCBIFAM models                : {n_go}")
    print(f"#   ...with BOTH an EC and a GO term         : {n_ec_and_go}")
    print(
        f"#   ...where ec2go(EC) CONFIRMS a model GO   : {len(bridged_models)}  (exactMatch candidates)"
    )
    print(
        f"#   ...where ec2go(EC) would REFINE NCBI's GO: {n_refine}  (propose-our-own-term class)"
    )
    print(f"#   candidate (model, EC-confirmed GO) rows  : {len(rows)}")
    print(
        f"#   ...already in the reviewed seed          : {sum(1 for r in rows if r[4] == 'yes')}"
    )

    if args.stats_only:
        return 0

    header = "subject_id\tpredicate_id\tobject_id\tec\tfamily_type\tin_seed\tproduct\n"
    body = "".join(
        f"{s}\tskos:exactMatch\t{go}\t{ec}\t{ft}\t{seed}\t{prod}\n"
        for (s, go, ec, ft, seed, prod) in rows
    )
    banner = (
        "# GENERATED -- EC-bridge-confirmed NCBIFAM->GO exactMatch candidates.\n"
        "# Source of truth: ncbifam2go_candidates.py (NOT hand-reviewed; mapping_justification\n"
        "# would be semapv:CompositeMatching). The 28-row ncbifam2go.sssom.yaml is the reviewed core.\n"
        "# Regenerate: uv run python projects/NCBIFam/ncbifam2go_candidates.py\n"
    )
    args.out.write_text(banner + header + body)
    print(f"# wrote {len(rows)} candidate rows -> {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
