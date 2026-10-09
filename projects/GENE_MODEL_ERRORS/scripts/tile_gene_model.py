#!/usr/bin/env python3
"""Test whether a UniProt entry is a fused gene model by tiling it with another assembly.

A fused gene model joins two (or more) neighbouring genes into one predicted
protein. If an independent assembly or annotation of the same species
predicts those genes separately, its proteins will *tile* the fused entry:
each aligns, at near-identity, to a different, non-overlapping segment.

For each target accession this script searches the target's sequence with
phmmer against a comparison proteome (any UniProt proteome id; sequences are
streamed from UniParc, so proteomes whose entries were deleted from
UniProtKB still work), collects near-identical segments, and fetches the
target's InterPro domain locations so each segment can be read as a domain
set. A target is called ``FUSION`` when at least two different comparison
proteins each cover >= --min-segment residues at >= --min-identity, overlap
each other by <= --max-overlap residues, and together cover >= --min-cover of
the target.

    uv run --with pyhmmer python projects/GENE_MODEL_ERRORS/scripts/tile_gene_model.py \\
        A0A0K3CAZ0 A0A0K3C7C1 --comparison-proteome UP000239560 \\
        --out projects/GENE_MODEL_ERRORS/data/tiling.tsv

Targets can also be selected from a ``resolve_deleted_accessions.py`` table
(``--from-resolution``): a current entry much longer than the archived
sequence it replaced is the typical signature of a fusion.

Output: one row per segment, with the call repeated on every row of a target.
Downloads are cached in ``--cache``.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import pyhmmer

REST = "https://rest.uniprot.org"
INTERPRO = "https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/{}"


def get(url: str) -> str:
    with urllib.request.urlopen(url, timeout=900) as r:
        return r.read().decode()


def comparison_fasta(upid: str, cache: Path) -> Path:
    path = cache / f"{upid}.uniparc.fasta"
    if not path.exists():
        print(f"downloading proteome {upid} from UniParc", file=sys.stderr)
        path.write_text(get(f"{REST}/uniparc/stream?query=proteome:{upid}&format=fasta"))
    return path


def member_accessions(upis: list[str]) -> dict[str, str]:
    """UPI -> UniProtKB accessions (versioned = archived, bare = active)."""
    out = {}
    for i in range(0, len(upis), 50):
        query = urllib.parse.quote(" OR ".join(f"upi:{u}" for u in upis[i : i + 50]))
        for line in get(f"{REST}/uniparc/search?query={query}&fields=upi,accession&format=tsv&size=500").splitlines()[1:]:
            upi, acc = (line.split("\t") + [""])[:2]
            out[upi] = acc
    return out


def domains(acc: str) -> list[tuple[str, str, int, int]]:
    try:
        body = get(INTERPRO.format(acc))
        data = json.loads(body) if body.strip() else {}
    except (OSError, ValueError):
        return []
    out = []
    for r in data.get("results", []):
        m = r["metadata"]
        if m["type"] not in ("domain", "family"):
            continue
        for p in r["proteins"]:
            for loc in p["entry_protein_locations"]:
                for frag in loc["fragments"]:
                    out.append((m["accession"], m["name"], frag["start"], frag["end"]))
    return sorted(out, key=lambda d: d[2])


def segments(seq: str, name: str, db: list, min_identity: float, min_segment: int) -> list[dict]:
    ab = pyhmmer.easel.Alphabet.amino()
    query = pyhmmer.easel.TextSequence(name=name.encode(), sequence=seq).digitize(ab)
    out = []
    for hits in pyhmmer.hmmer.phmmer([query], db):
        for hit in hits:
            if not hit.included:
                continue
            tname = hit.name.decode() if isinstance(hit.name, bytes) else hit.name
            for dom in hit.domains:
                if not dom.included:
                    continue
                aln = dom.alignment
                pairs = [
                    (a, b) for a, b in zip(aln.hmm_sequence, aln.target_sequence)
                    if a != "." and b != "-"
                ]
                ident = sum(a.upper() == b.upper() for a, b in pairs) / max(len(pairs), 1)
                if ident >= min_identity and aln.hmm_to - aln.hmm_from + 1 >= min_segment:
                    out.append({
                        "comparison_upi": tname,
                        "q_from": aln.hmm_from, "q_to": aln.hmm_to,
                        "t_from": aln.target_from, "t_to": aln.target_to,
                        "identity": ident,
                    })
    return out


def merge_by_protein(segs: list[dict]) -> list[dict]:
    """Collapse several domains of one comparison protein into one span."""
    by = {}
    for s in segs:
        b = by.setdefault(s["comparison_upi"], dict(s))
        b["q_from"], b["q_to"] = min(b["q_from"], s["q_from"]), max(b["q_to"], s["q_to"])
        b["t_from"], b["t_to"] = min(b["t_from"], s["t_from"]), max(b["t_to"], s["t_to"])
        b["identity"] = max(b["identity"], s["identity"])
    return sorted(by.values(), key=lambda s: s["q_from"])


def call(spans: list[dict], length: int, max_overlap: int, min_cover: float) -> str:
    """Greedy non-overlapping tiling by distinct proteins."""
    chosen = []
    for s in sorted(spans, key=lambda s: -(s["q_to"] - s["q_from"])):
        if all(min(s["q_to"], c["q_to"]) - max(s["q_from"], c["q_from"]) <= max_overlap for c in chosen):
            chosen.append(s)
    covered = sum(c["q_to"] - c["q_from"] + 1 for c in chosen)
    if len(chosen) >= 2 and covered / length >= min_cover:
        return "FUSION"
    if len(chosen) == 1 and (chosen[0]["q_to"] - chosen[0]["q_from"] + 1) / length >= min_cover:
        return "SINGLE_GENE"
    return "INCONCLUSIVE"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("targets", nargs="*", help="UniProtKB accessions to test")
    ap.add_argument(
        "--from-resolution", type=Path,
        help="output of resolve_deleted_accessions.py; test each replacement that is "
        "--length-ratio times longer than the archived sequence it replaced",
    )
    ap.add_argument("--length-ratio", type=float, default=1.3)
    ap.add_argument("--comparison-proteome", required=True, help="UniProt proteome id (UPxxxxxxxxx)")
    ap.add_argument("--min-identity", type=float, default=0.9)
    ap.add_argument("--min-segment", type=int, default=100)
    ap.add_argument("--max-overlap", type=int, default=30)
    ap.add_argument("--min-cover", type=float, default=0.7)
    ap.add_argument("--cache", type=Path, default=Path("tmp/gene_model_errors"))
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    targets = list(args.targets)
    if args.from_resolution:
        with args.from_resolution.open() as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                if (
                    r["call"] in ("same_gene", "same_gene_partial_model")
                    and r["target_length"] and r["length"]
                    and int(r["target_length"]) >= args.length_ratio * int(r["length"])
                ):
                    targets.append(r["replacement"])
    targets = list(dict.fromkeys(targets))
    if not targets:
        ap.error("no targets given")

    ab = pyhmmer.easel.Alphabet.amino()
    with pyhmmer.easel.SequenceFile(
        str(comparison_fasta(args.comparison_proteome, args.cache)), digital=True, alphabet=ab
    ) as f:
        db = list(f)

    rows = []
    for acc in targets:
        fasta = get(f"{REST}/uniprotkb/{acc}.fasta")
        seq = "".join(ln.strip() for ln in fasta.splitlines() if not ln.startswith(">"))
        spans = merge_by_protein(segments(seq, acc, db, args.min_identity, args.min_segment))
        verdict = call(spans, len(seq), args.max_overlap, args.min_cover)
        members = member_accessions([s["comparison_upi"] for s in spans])
        doms = domains(acc)
        for s in spans or [{}]:
            covered = [
                f"{d[0]} {d[1]}" for d in doms
                if s and d[2] >= s["q_from"] - 10 and d[3] <= s["q_to"] + 10
            ]
            rows.append({
                "target": acc, "target_length": len(seq), "call": verdict,
                "comparison_proteome": args.comparison_proteome,
                "comparison_upi": s.get("comparison_upi", ""),
                "comparison_accessions": members.get(s.get("comparison_upi", ""), ""),
                "target_from": s.get("q_from", ""), "target_to": s.get("q_to", ""),
                "comparison_from": s.get("t_from", ""), "comparison_to": s.get("t_to", ""),
                "identity": f"{s['identity']:.3f}" if s else "",
                "interpro_in_segment": "; ".join(dict.fromkeys(covered)),
            })
        print(f"{acc} ({len(seq)} aa): {verdict}, {len(spans)} near-identical spans", file=sys.stderr)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
