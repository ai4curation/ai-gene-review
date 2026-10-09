#!/usr/bin/env python3
"""Find current UniProtKB replacements for deleted (proteome-removed) accessions.

UniProt's proteome-redundancy cleanup removed TrEMBL entries of non-reference
proteomes from UniProtKB; their sequences survive only in UniParc. A gene
review, mapping table or supplement keyed on such an accession then points at
nothing. For each input accession this script reports, in order of
preference:

1. ``active`` -- the accession is still in UniProtKB.
2. ``identical_active`` -- UniParc shows an active UniProtKB entry with the
   identical sequence (reviewed entries preferred, then the same taxon).
3. ``same_gene`` / ``same_gene_partial_model`` / ``weak`` -- best phmmer hit
   of the archived sequence against the reference proteome(s) of its species:
   ``same_gene`` is >= 90% identity over >= 80% of the query; ``partial_model``
   is >= 95% identity over a shorter span (gene models differ in length);
   ``weak`` is anything lower and should not be used without inspection.
4. ``no_hit`` / ``no_reference_proteome`` / ``no_sequence`` / ``not_found``.

A ``same_gene`` hit to a much longer target can mean the target is a fused
gene model; see ``projects/GENE_MODEL_ERRORS.md``.

    uv run --with pyhmmer python projects/PROTEOME_REMOVAL/scripts/resolve_deleted_accessions.py \\
        A0A1V0M5B3 Q1IFG0 --out resolved.tsv
    uv run --with pyhmmer python projects/PROTEOME_REMOVAL/scripts/resolve_deleted_accessions.py \\
        --from-tsv table.tsv --column uniprot --proteome UP000199069 --out resolved.tsv

``--proteome`` (repeatable) skips the automatic reference-proteome lookup.
Downloads are cached in ``--cache``.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pyhmmer

REST = "https://rest.uniprot.org"
FIELDS = [
    "accession", "uniprotkb_status", "upi", "length", "taxon",
    "replacement", "replacement_reviewed", "replacement_taxon", "target_proteome",
    "target_length", "identity", "query_coverage", "evalue", "call",
]


def get(url: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=600) as r:
                return r.read().decode()
        except OSError:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    return ""


def q(s: str) -> str:
    return urllib.parse.quote(s)


def kb_records(accs: list[str]) -> dict[str, dict]:
    """UniProtKB status for accessions: deleted entries come back as 'deleted'."""
    out = {}
    for i in range(0, len(accs), 100):
        batch = accs[i : i + 100]
        tsv = get(
            f"{REST}/uniprotkb/search?query={q(' OR '.join(f'accession:{a}' for a in batch))}"
            "&fields=accession,protein_name,reviewed,organism_id&format=tsv&size=500"
        )
        for line in tsv.splitlines()[1:]:
            f = (line.split("\t") + [""] * 4)[:4]
            out[f[0]] = {
                "status": "deleted" if f[1] == "deleted" else "active",
                "reviewed": f[2] == "reviewed",
                "taxon": f[3],
            }
        time.sleep(0.2)
    return out


def uniparc_entry(acc: str) -> dict | None:
    """UPI, sequence, taxa and the accessions sharing the sequence."""
    tsv = get(f"{REST}/uniparc/search?query={q(acc)}&fields=upi,accession,organism_id&format=tsv&size=10")
    for line in tsv.splitlines()[1:]:
        upi, kbs, taxa = (line.split("\t") + ["", ""])[:3]
        members = [k.strip() for k in kbs.split(";") if k.strip()]
        if not any(m.split(".")[0] == acc for m in members):
            continue
        fasta = get(f"{REST}/uniparc/{upi}.fasta")
        seq = "".join(ln.strip() for ln in fasta.splitlines() if not ln.startswith(">"))
        # UniParc lists archived members with a version suffix and active
        # UniProtKB members without one.
        active = [m for m in members if "." not in m and m != acc]
        return {
            "upi": upi,
            "sequence": seq,
            "taxa": [t.strip() for t in taxa.split(";") if t.strip()],
            "active_members": active,
        }
    return None


def species_of(taxon: str, cache: dict) -> str:
    if taxon in cache:
        return cache[taxon]
    d = json.loads(get(f"{REST}/taxonomy/{taxon}?format=json"))
    sp = taxon if d.get("rank") == "species" else ""
    for anc in d.get("lineage", []):
        if not sp and anc.get("rank") == "species":
            sp = str(anc["taxonId"])
    cache[taxon] = sp or taxon
    return cache[taxon]


def reference_proteomes(species: str, limit: int = 5) -> list[str]:
    tsv = get(
        f"{REST}/proteomes/search?query={q(f'taxonomy_id:{species} AND reference:true')}"
        f"&fields=upid,protein_count&format=tsv&size={limit}"
    )
    return [line.split("\t")[0] for line in tsv.splitlines()[1:] if line.strip()]


def proteome_fasta(upid: str, cache: Path) -> Path:
    path = cache / f"{upid}.fasta"
    if not path.exists():
        print(f"downloading proteome {upid}", file=sys.stderr)
        path.write_text(get(f"{REST}/uniprotkb/stream?query=proteome:{upid}&format=fasta"))
    return path


def best_hit(seq: str, name: str, targets: list[Path]) -> dict | None:
    ab = pyhmmer.easel.Alphabet.amino()
    query = pyhmmer.easel.TextSequence(name=name.encode(), sequence=seq).digitize(ab)
    best = None
    for path in targets:
        with pyhmmer.easel.SequenceFile(str(path), digital=True, alphabet=ab) as f:
            db = list(f)
        for hits in pyhmmer.hmmer.phmmer([query], db):
            for hit in hits:
                if not hit.included:
                    continue
                aln = hit.best_domain.alignment
                pairs = [
                    (a, b) for a, b in zip(aln.hmm_sequence, aln.target_sequence)
                    if a != "." and b != "-"
                ]
                ident = sum(a.upper() == b.upper() for a, b in pairs) / max(len(pairs), 1)
                tname = hit.name.decode() if isinstance(hit.name, bytes) else hit.name
                tlen = next(len(s) for s in db if (s.name.decode() if isinstance(s.name, bytes) else s.name) == tname)
                cand = {
                    "target": tname.split("|")[1] if "|" in tname else tname,
                    "target_proteome": path.stem,
                    "target_length": tlen,
                    "identity": ident,
                    "coverage": (aln.hmm_to - aln.hmm_from + 1) / len(seq),
                    "evalue": hit.evalue,
                }
                if best is None or cand["evalue"] < best["evalue"]:
                    best = cand
                break
    return best


def read_accessions(args) -> list[str]:
    accs = list(args.accessions)
    if args.from_tsv:
        with args.from_tsv.open() as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row.get(args.column):
                    accs.append(row[args.column].strip())
    seen, out = set(), []
    for a in accs:
        a = a.split(".")[0]
        if a and a not in seen and a != "#N/A":
            seen.add(a)
            out.append(a)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("accessions", nargs="*")
    ap.add_argument("--from-tsv", type=Path)
    ap.add_argument("--column", default="uniprot")
    ap.add_argument("--proteome", action="append", default=[], help="target proteome UPID")
    ap.add_argument("--cache", type=Path, default=Path("tmp/proteome_removal"))
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)

    accs = read_accessions(args)
    kb = kb_records(accs)
    taxon_cache: dict[str, str] = {}
    rows = []
    for n, acc in enumerate(accs, 1):
        row = dict.fromkeys(FIELDS, "")
        row["accession"] = acc
        rec = kb.get(acc)
        row["uniprotkb_status"] = rec["status"] if rec else "not_found"
        if rec and rec["status"] == "active":
            row.update(replacement=acc, replacement_reviewed=rec["reviewed"],
                       replacement_taxon=rec["taxon"], call="active")
            rows.append(row)
            continue
        entry = uniparc_entry(acc)
        if not entry:
            row["call"] = "no_sequence" if rec else "not_found"
            rows.append(row)
            continue
        taxon = entry["taxa"][0] if entry["taxa"] else ""
        row.update(upi=entry["upi"], length=len(entry["sequence"]), taxon=taxon)
        if entry["active_members"]:
            members = kb_records(entry["active_members"][:100])
            live = [(m, members[m]) for m in entry["active_members"][:100] if m in members]
            live.sort(key=lambda x: (not x[1]["reviewed"], x[1]["taxon"] != taxon))
            if live:
                m, info = live[0]
                row.update(replacement=m, replacement_reviewed=info["reviewed"],
                           replacement_taxon=info["taxon"], call="identical_active")
                rows.append(row)
                continue
        proteomes = args.proteome or reference_proteomes(species_of(taxon, taxon_cache))
        if not proteomes:
            row["call"] = "no_reference_proteome"
            rows.append(row)
            continue
        hit = best_hit(entry["sequence"], acc, [proteome_fasta(p, args.cache) for p in proteomes])
        if not hit:
            row.update(target_proteome=";".join(proteomes), call="no_hit")
        else:
            ident, cov = hit["identity"], hit["coverage"]
            if ident >= 0.9 and cov >= 0.8:
                call = "same_gene"
            elif ident >= 0.95:
                call = "same_gene_partial_model"
            else:
                call = "weak"
            row.update(
                replacement=hit["target"], target_proteome=hit["target_proteome"],
                target_length=hit["target_length"], identity=f"{ident:.3f}",
                query_coverage=f"{cov:.2f}", evalue=f"{hit['evalue']:.1e}", call=call,
            )
        rows.append(row)
        if n % 25 == 0:
            print(f"  {n}/{len(accs)}", file=sys.stderr)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["call"]] = counts.get(r["call"], 0) + 1
    print(f"{len(rows)} accessions: {counts}; wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
