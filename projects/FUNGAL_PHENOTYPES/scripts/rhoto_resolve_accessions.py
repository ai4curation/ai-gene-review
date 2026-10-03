#!/usr/bin/env python3
"""Map R. toruloides IFO0880 (RTO4) genes onto current UniProtKB entries.

The RTO4 -> UniProt mapping of Coradetti et al. 2023 points at the IFO0880
proteome (UP000239560), most of whose TrEMBL entries have since been deleted
and survive only as UniParc sequences. This script takes the genes in
``data/rhoto_specific_defects.tsv``, fetches each 2023 accession's sequence
from UniParc, and searches it with phmmer (pyhmmer) against the R. toruloides
reference proteome (UP000199069). The best hit is reported with its percent
identity and query coverage; a hit is called ``same_gene`` when identity
>= 90% and coverage >= 80% (a strain-level ortholog), ``same_gene_partial_model``
when identity >= 95% over a shorter span (the two assemblies' gene models
differ in length), otherwise ``weak``.

    uv run --with pyhmmer python \\
        projects/FUNGAL_PHENOTYPES/scripts/rhoto_resolve_accessions.py

Nothing is hardcoded; downloads are cached in ``--cache``.
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pyhmmer

REST = "https://rest.uniprot.org"
REFERENCE_PROTEOME = "UP000199069"


def get(url: str) -> str:
    with urllib.request.urlopen(url, timeout=300) as r:
        return r.read().decode()


def reference_fasta(cache: Path) -> Path:
    path = cache / f"{REFERENCE_PROTEOME}.fasta"
    if not path.exists():
        print(f"downloading proteome {REFERENCE_PROTEOME}", file=sys.stderr)
        path.write_text(
            get(f"{REST}/uniprotkb/stream?query=proteome:{REFERENCE_PROTEOME}&format=fasta")
        )
    return path


def query_fasta(accs: list[str], cache: Path) -> Path:
    """Sequences for 2023 accessions, active or deleted, keyed by accession."""
    path = cache / "rhoto_query_seqs.fasta"
    have = set()
    if path.exists():
        have = {l[1:].split()[0] for l in path.read_text().splitlines() if l.startswith(">")}
    todo = [a for a in accs if a not in have]
    with path.open("a") as out:
        for i in range(0, len(todo), 50):
            batch = todo[i : i + 50]
            # Free-text search finds deleted accessions; field search does not.
            q = urllib.parse.quote(" OR ".join(batch))
            tsv = get(f"{REST}/uniparc/search?query={q}&fields=upi,accession&format=tsv&size=500")
            upi_of = {}
            for line in tsv.splitlines()[1:]:
                upi, kb = (line.split("\t") + [""])[:2]
                for acc in kb.split(";"):
                    acc = acc.strip().split(".")[0]
                    if acc in batch:
                        upi_of[acc] = upi
            if not upi_of:
                continue
            q = urllib.parse.quote(" OR ".join(f"upi:{u}" for u in set(upi_of.values())))
            seqs, cur = {}, None
            for line in get(f"{REST}/uniparc/stream?query={q}&format=fasta").splitlines():
                if line.startswith(">"):
                    cur = line[1:].split()[0]
                    seqs[cur] = []
                elif cur:
                    seqs[cur].append(line.strip())
            for acc, upi in upi_of.items():
                if upi in seqs:
                    out.write(f">{acc} {upi}\n{''.join(seqs[upi])}\n")
            time.sleep(0.2)
    return path


def read_fasta(path: Path, alphabet) -> list:
    with pyhmmer.easel.SequenceFile(str(path), digital=True, alphabet=alphabet) as f:
        return list(f)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--cache", type=Path, default=Path("tmp/fungal_phenotypes"))
    ap.add_argument(
        "--defects",
        type=Path,
        default=Path("projects/FUNGAL_PHENOTYPES/data/rhoto_specific_defects.tsv"),
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("projects/FUNGAL_PHENOTYPES/data/rhoto_accession_resolution.tsv"),
    )
    args = ap.parse_args()

    rows = list(csv.DictReader(args.defects.open(), delimiter="\t"))
    accs = sorted({r["uniprot_2023"] for r in rows if r["uniprot_2023"]})
    alphabet = pyhmmer.easel.Alphabet.amino()
    queries = read_fasta(query_fasta(accs, args.cache), alphabet)
    targets = read_fasta(reference_fasta(args.cache), alphabet)

    best = {}
    for hits in pyhmmer.hmmer.phmmer(queries, targets, cpus=0):
        qname = hits.query.name
        qname = qname.decode() if isinstance(qname, bytes) else qname
        qlen = len(hits.query)
        for hit in hits:
            if not hit.included:
                continue
            dom = hit.best_domain.alignment
            pairs = [
                (a, b)
                for a, b in zip(dom.hmm_sequence, dom.target_sequence)
                if a != "." and b != "-"
            ]
            ident = sum(a.upper() == b.upper() for a, b in pairs) / max(len(pairs), 1)
            cov = (dom.hmm_to - dom.hmm_from + 1) / qlen
            name = hit.name.decode() if isinstance(hit.name, bytes) else hit.name
            best[qname] = (name.split("|")[1] if "|" in name else name, ident, cov, hit.evalue)
            break

    with args.out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(
            ["rto4_id", "uniprot_2023", "uniprot_status", "reference_accession",
             "identity", "query_coverage", "evalue", "call"]
        )
        counts = {}
        for r in rows:
            acc = r["uniprot_2023"]
            if r["uniprot_status"] not in ("deleted", "not_found", ""):
                ref, ident, cov, ev, call = acc, "", "", "", "active"
            elif acc in best:
                ref, ident, cov, ev = best[acc]
                if ident >= 0.9 and cov >= 0.8:
                    call = "same_gene"
                elif ident >= 0.95:
                    call = "same_gene_partial_model"
                else:
                    call = "weak"
                ident, cov, ev = f"{ident:.3f}", f"{cov:.2f}", f"{ev:.1e}"
            else:
                ref, ident, cov, ev, call = "", "", "", "", "no_hit"
            counts[call] = counts.get(call, 0) + 1
            w.writerow([r["rto4_id"], acc, r["uniprot_status"], ref, ident, cov, ev, call])
    print(f"{len(rows)} genes: {counts}; wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
