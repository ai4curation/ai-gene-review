"""Reciprocal-best-hit mapping of module exemplars from Arabidopsis to field pennycress.

For every Arabidopsis UniProtKB representative member cited in the module(s) given on the
command line, search the pennycress reference proteome (UP000836841) with phmmer, then
search each top pennycress hit back against the Arabidopsis reference proteome
(UP000006548, plus the module's own query sequences, so that non-Col alleles such as the
Cvi-0 AOP2 can be matched by gene name). A pennycress protein is called a reciprocal best
hit (RBH) when its best Arabidopsis hit is the query itself or carries the same gene
name (GN=) as the query.

Outputs (written next to this script):
  results/orthologs.tsv   one row per query
  RESULTS.md              human-readable summary generated from the TSV

Usage:
  uv run python find_orthologs.py ../../../modules/aliphatic_glucosinolate_myrosinase_defense.yaml
"""

from __future__ import annotations

import csv
import hashlib
import gzip
import re
import sys
import time
from pathlib import Path

import pyhmmer
import requests
import yaml

HERE = Path(__file__).parent
DATA = HERE / "data"
RESULTS = HERE / "results"
UNIPROT = "https://rest.uniprot.org/uniprotkb"
PROTEOMES = {"THLAR": "UP000836841", "ARATH": "UP000006548"}
ALPHABET = pyhmmer.easel.Alphabet.amino()
TOP_N = 5


def fetch(url: str, dest: Path, params: dict | None = None, attempts: int = 4) -> Path:
    """Download url to dest (streamed, via a temp file, with retries); reuse dest if present."""
    if dest.exists():
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    for i in range(attempts):
        try:
            with requests.get(url, params=params, timeout=600, stream=True) as r:
                r.raise_for_status()
                with open(tmp, "wb") as fh:
                    for chunk in r.iter_content(1 << 20):
                        fh.write(chunk)
            tmp.rename(dest)
            return dest
        except requests.RequestException as e:
            print(f"download failed ({e}); retry {i + 1}/{attempts}", file=sys.stderr)
            time.sleep(2 ** (i + 1))
    raise RuntimeError(f"could not download {url}")


TAXA = {"THLAR": 13288, "ARATH": 3702}
FTP = "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota"


def proteome_fasta(code: str) -> Path:
    """Canonical (one protein per gene) reference proteome FASTA from the UniProt FTP site."""
    upid, taxid = PROTEOMES[code], TAXA[code]
    return fetch(f"{FTP}/{upid}/{upid}_{taxid}.fasta.gz", DATA / f"{code}_{upid}.fasta.gz")


def read_fasta(path: Path) -> list[pyhmmer.easel.TextSequence]:
    opener = gzip.open if path.suffix == ".gz" else open
    seqs, name, desc, buf = [], None, "", []
    with opener(path, "rt") as fh:
        for line in fh:
            line = line.rstrip()
            if line.startswith(">"):
                if name:
                    seqs.append(pyhmmer.easel.TextSequence(name=name, description=desc, sequence="".join(buf)))
                header = line[1:]
                name = header.split()[0]
                desc = header[len(name):].strip()
                buf = []
            elif line:
                buf.append(line)
    if name:
        seqs.append(pyhmmer.easel.TextSequence(name=name, description=desc, sequence="".join(buf)))
    return seqs


def _s(x) -> str:
    return x.decode() if isinstance(x, bytes) else x


def acc(name: str) -> str:
    name = _s(name)
    parts = name.split("|")
    return parts[1] if len(parts) > 2 else name


def gene_name(desc: str) -> str:
    desc = _s(desc)
    m = re.search(r"\bGN=(\S+)", desc)
    return m.group(1) if m else ""


def module_queries(module_paths: list[str]) -> list[tuple[str, str, str]]:
    """Return (module stem, annoton id, accession) for every UniProtKB representative member."""
    out = []

    def walk(o, mod, annoton=None):
        if isinstance(o, dict):
            if "participant" in o and "id" in o:
                annoton = o["id"]
            if o.get("id", "").startswith("UniProtKB:") if isinstance(o.get("id"), str) else False:
                out.append((mod, annoton, o["id"].split(":", 1)[1]))
            for v in o.values():
                walk(v, mod, annoton)
        elif isinstance(o, list):
            for v in o:
                walk(v, mod, annoton)

    for p in module_paths:
        walk(yaml.safe_load(open(p)), Path(p).stem)
    seen, uniq = set(), []
    for row in out:
        if row[2] not in seen:
            seen.add(row[2])
            uniq.append(row)
    return uniq


def identity_and_coverage(hit, qlen: int) -> tuple[float, float]:
    """Identity over aligned columns of all included domains; query coverage = union of their spans."""
    covered, same, cols = set(), 0, 0
    for dom in hit.domains.included:
        aln = dom.alignment
        covered.update(range(aln.hmm_from, aln.hmm_to + 1))
        for a, b in zip(aln.hmm_sequence, aln.target_sequence):
            if a not in ".-" and b not in ".-":
                cols += 1
                same += a.upper() == b.upper()
    return round(100 * same / max(cols, 1), 1), round(100 * len(covered) / qlen, 1)


def search(queries, targets_digital):
    return {
        q.name: hits
        for q, hits in zip(queries, pyhmmer.hmmer.phmmer(queries, targets_digital, cpus=0))
    }


def main(module_paths: list[str]) -> None:
    rows = module_queries(module_paths)
    query_ids = [r[2] for r in rows]
    qfasta = fetch(
        f"{UNIPROT}/stream",
        DATA / f"queries_{hashlib.sha1(' '.join(sorted(query_ids)).encode()).hexdigest()[:10]}.fasta",
        {"query": " OR ".join(f"accession:{a}" for a in query_ids), "format": "fasta"},
    )
    all_q = {acc(s.name): s for s in read_fasta(qfasta)}
    arath_q = {a: s for a, s in all_q.items() if "OX=3702" in s.description}

    thlar = read_fasta(proteome_fasta("THLAR"))
    arath = read_fasta(proteome_fasta("ARATH"))
    arath_names = {acc(s.name) for s in arath}
    arath_db = arath + [s for a, s in arath_q.items() if a not in arath_names]

    thlar_d = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [s.digitize(ALPHABET) for s in thlar])
    arath_d = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [s.digitize(ALPHABET) for s in arath_db])
    thlar_desc = {s.name: s.description for s in thlar}
    arath_desc = {s.name: s.description for s in arath_db}

    queries = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [s.digitize(ALPHABET) for s in arath_q.values()])
    fwd = search(queries, thlar_d)

    # reverse-search the top forward hits of every query
    top = {}
    for qname, hits in fwd.items():
        top[qname] = [h for h in hits if h.included][:TOP_N]
    rev_names = sorted({h.name for hs in top.values() for h in hs})
    thlar_by_name = {s.name: s for s in thlar}
    rev_q = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [thlar_by_name[n].digitize(ALPHABET) for n in rev_names])
    rev = search(rev_q, arath_d) if rev_names else {}

    RESULTS.mkdir(exist_ok=True)
    out_rows = []
    for mod, annoton, qacc in rows:
        if qacc not in arath_q:
            continue  # non-Arabidopsis exemplar (e.g. pennycress TFP, human ELOVL)
        qseq = arath_q[qacc]
        qname = qseq.name
        qgene = gene_name(qseq.description)
        hits = top.get(qname, [])
        best = hits[0] if hits else None
        row = dict(module=mod, annoton=annoton, query=qacc, query_gene=qgene, n_included_hits=len(hits))
        if best is None:
            row.update(thlar_acc="", thlar_locus="", bitscore="", evalue="", identity_pct="", query_cov_pct="",
                       second_bitscore="", reverse_best="", reverse_best_gene="", rbh="no hit")
        else:
            bname = best.name
            ident, cov = identity_and_coverage(best, len(qseq.sequence))
            rbest = next((h for h in rev.get(bname, []) if h.included), None)
            rname = rbest.name if rbest else ""
            rgene = gene_name(arath_desc.get(rname, ""))
            is_rbh = bool(rbest) and (acc(rname) == qacc or (rgene and rgene.upper() == qgene.upper()))
            row.update(
                thlar_acc=acc(bname),
                thlar_locus=gene_name(thlar_desc[bname]),
                bitscore=round(best.score, 1),
                evalue=f"{best.evalue:.1e}",
                identity_pct=ident,
                query_cov_pct=cov,
                second_bitscore=round(hits[1].score, 1) if len(hits) > 1 else "",
                reverse_best=acc(rname),
                reverse_best_gene=rgene,
                rbh="yes" if is_rbh else "no",
            )
        out_rows.append(row)

    cand_rows = []
    for mod, annoton, qacc in rows:
        if qacc not in arath_q:
            continue
        qseq = arath_q[qacc]
        for rank, h in enumerate(top.get(qseq.name, []), 1):
            hn = h.name
            ident, cov = identity_and_coverage(h, len(qseq.sequence))
            rb = next((x for x in rev.get(hn, []) if x.included), None)
            rn = rb.name if rb else ""
            cand_rows.append(dict(query=qacc, query_gene=gene_name(qseq.description), rank=rank,
                                  thlar_acc=acc(hn), thlar_locus=gene_name(thlar_desc[hn]),
                                  bitscore=round(h.score, 1), identity_pct=ident, query_cov_pct=cov,
                                  target_len=len(thlar_by_name[hn].sequence),
                                  reverse_best=acc(rn), reverse_best_gene=gene_name(arath_desc.get(rn, ""))))
    with open(RESULTS / "candidates.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(cand_rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(cand_rows)

    # pennycress-native exemplars (e.g. TFP, FAE1): which proteome entry is the same protein?
    native = {a: q for a, q in all_q.items() if "OX=13288" in q.description}
    native_rows = []
    if native:
        nq = pyhmmer.easel.DigitalSequenceBlock(ALPHABET, [q.digitize(ALPHABET) for q in native.values()])
        for (a, q), hits in zip(native.items(), pyhmmer.hmmer.phmmer(nq, thlar_d, cpus=0)):
            for rank, h in enumerate([h for h in hits if h.included][:3], 1):
                ident, cov = identity_and_coverage(h, len(q.sequence))
                native_rows.append(dict(exemplar=a, exemplar_gene=gene_name(q.description), rank=rank,
                                        thlar_acc=acc(h.name), thlar_locus=gene_name(thlar_desc[h.name]),
                                        identity_pct=ident, query_cov_pct=cov,
                                        target_len=len(thlar_by_name[h.name].sequence)))
        with open(RESULTS / "native_exemplars.tsv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(native_rows[0].keys()), delimiter="\t")
            w.writeheader()
            w.writerows(native_rows)

    tsv = RESULTS / "orthologs.tsv"
    with open(tsv, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(out_rows)
    write_results_md(out_rows, module_paths)
    print(f"wrote {tsv} ({len(out_rows)} queries)")


def write_results_md(rows, module_paths):
    n_rbh = sum(r["rbh"] == "yes" for r in rows)
    lines = [
        "# Pennycress orthologs of module exemplars (reciprocal best hits)",
        "",
        "Generated by `find_orthologs.py`; do not edit by hand. Re-run with",
        "`uv run python find_orthologs.py " + " ".join(module_paths) + "`.",
        "",
        "Method: phmmer (pyhmmer) search of each Arabidopsis exemplar against the field pennycress",
        "reference proteome UP000836841 (canonical FASTA from the UniProt FTP site), then of each top pennycress hit back against the Arabidopsis",
        "reference proteome UP000006548. RBH = the reverse best hit is the query or has the same gene name.",
        "`second_bitscore` is the next-best pennycress hit; a small gap to the best hit flags close paralogs",
        "where the 1:1 call needs care.",
        "",
        f"{n_rbh} of {len(rows)} Arabidopsis exemplars have a reciprocal best hit in pennycress.",
        "",
        "| Annoton | Query | Gene | Pennycress | Locus | Bits | 2nd bits | %id | %cov | Reverse best | RBH |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['annoton']} | {r['query']} | {r['query_gene']} | {r['thlar_acc']} | {r['thlar_locus']} | "
            f"{r['bitscore']} | {r['second_bitscore']} | {r['identity_pct']} | {r['query_cov_pct']} | "
            f"{r['reverse_best']} ({r['reverse_best_gene']}) | {r['rbh']} |"
        )
    (HERE / "RESULTS.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
