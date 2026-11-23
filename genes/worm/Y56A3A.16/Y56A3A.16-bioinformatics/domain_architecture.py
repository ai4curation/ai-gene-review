"""Compare domain architecture and sequence similarity of C. elegans Y56A3A.16
(RUB-1; UniProt G2HK09/G2HK08) with human RUBCN (Q92622), human RUBCNL/Pacer
(Q9H714) and Drosophila Rubicon (Q9W3C9).

All data are fetched live from UniProt REST and the InterPro API; nothing is
hardcoded except the accession list. Outputs results/*.tsv and prints a summary.

Analyses:
 1. InterPro/Pfam/SMART/CDD domain coordinates for each protein.
 2. Global and local (Smith-Waterman, BLOSUM62) alignment identity of the
    Rubicon-homology (RH, Pfam PF13901) domain of each protein vs the worm RH.
 3. Local alignment of the worm N-terminal region (residues before the RH
    domain) against the RUN domain (Pfam/SMART/CDD-defined) of human RUBCN and
    fly Rubicon, with a shuffled-sequence null distribution (empirical z-score),
    to ask whether a divergent RUN domain could be present but missed by HMMs.
 4. Cysteine/histidine pattern of the RH domain (zinc-binding residues).
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q92622": "human RUBCN (Rubicon)",
    "Q9H714": "human RUBCNL (Pacer)",
    "Q9W3C9": "fly Rubicon (CG12772)",
    "G2HK09": "worm Y56A3A.16b (RUB-1)",
    "G2HK08": "worm Y56A3A.16 alt isoform",
}
WORM = "G2HK09"
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)
SESSION = requests.Session()


def fetch_seq(acc: str) -> str:
    r = SESSION.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def fetch_domains(acc: str) -> list[tuple[str, str, str, int, int]]:
    url = f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/?page_size=100"
    rows = []
    while url:
        r = SESSION.get(url, timeout=60)
        if r.status_code == 204:
            break
        r.raise_for_status()
        d = r.json()
        for res in d["results"]:
            md = res["metadata"]
            for p in res["proteins"]:
                for loc in p.get("entry_protein_locations") or []:
                    for f in loc["fragments"]:
                        rows.append((md["source_database"], md["accession"], md["name"] or "", int(f["start"]), int(f["end"])))
        url = d.get("next")
    return sorted(rows, key=lambda x: (x[3], x[0]))


def aligner(mode: str) -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = mode
    return a


def identity(aln) -> tuple[float, int]:
    """Percent identity over aligned (non-gap) columns, and aligned length."""
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    if not cols:
        return 0.0, 0
    ident = sum(1 for x, y in cols if x == y)
    return 100.0 * ident / len(cols), len(cols)


def domain_span(doms, pred) -> tuple[int, int] | None:
    hits = [(s, e) for db, acc, name, s, e in doms if pred(db, acc, name)]
    if not hits:
        return None
    return min(s for s, _ in hits), max(e for _, e in hits)


def is_rh(db, acc, name):
    return acc in ("PF13901", "SM01175", "IPR025258")


def is_run(db, acc, name):
    n = name.lower()
    return acc in ("PF02759", "SM00593", "PS50826", "IPR004012", "cd17686") or (n.startswith("run") and "rubc" not in n and acc != "IPR037213") or acc == "IPR037213"


def main() -> int:
    seqs, doms = {}, {}
    with open(OUT / "domains.tsv", "w") as fh:
        fh.write("accession\tprotein\tlength\tsource_db\tentry\tname\tstart\tend\n")
        for acc, label in ACCS.items():
            seqs[acc] = fetch_seq(acc)
            doms[acc] = fetch_domains(acc)
            for db, eacc, name, s, e in doms[acc]:
                fh.write(f"{acc}\t{label}\t{len(seqs[acc])}\t{db}\t{eacc}\t{name}\t{s}\t{e}\n")

    print("== Domain architecture (InterPro API, live) ==")
    for acc, label in ACCS.items():
        d = doms[acc]
        rh = domain_span(d, is_rh)
        run = domain_span(d, is_run)
        pikbd = [(s, e) for db, a, n, s, e in d if a in ("PF21054", "IPR048569")]
        print(f"{acc} {label} len={len(seqs[acc])} RH={rh} RUN={run} PIKBD(PF21054/IPR048569)={sorted(set(pikbd))}")

    # 2. RH-domain comparisons vs worm
    print("\n== RH domain (PF13901/SM01175 span) identity vs worm G2HK09 ==")
    wrh = domain_span(doms[WORM], is_rh)
    wrh_seq = seqs[WORM][wrh[0] - 1 : wrh[1]]
    with open(OUT / "rh_identity.tsv", "w") as fh:
        fh.write("query\ttarget\ttarget_label\tmode\tpercent_identity\taligned_columns\tscore\n")
        for acc, label in ACCS.items():
            if acc == WORM:
                continue
            span = domain_span(doms[acc], is_rh)
            if span is None:
                continue
            tseq = seqs[acc][span[0] - 1 : span[1]]
            for mode in ("global", "local"):
                aln = aligner(mode).align(wrh_seq, tseq)[0]
                pid, n = identity(aln)
                fh.write(f"{WORM}\t{acc}\t{label}\t{mode}\t{pid:.1f}\t{n}\t{aln.score:.0f}\n")
                print(f"  {acc} {label:28s} {mode:6s} identity={pid:5.1f}% over {n} cols score={aln.score:.0f}")

    # full-length local alignment
    print("\n== Full-length local alignment vs worm G2HK09 ==")
    with open(OUT / "fulllength_identity.tsv", "w") as fh:
        fh.write("query\ttarget\ttarget_label\tpercent_identity\taligned_columns\tscore\n")
        for acc, label in ACCS.items():
            if acc == WORM:
                continue
            aln = aligner("local").align(seqs[WORM], seqs[acc])[0]
            pid, n = identity(aln)
            fh.write(f"{WORM}\t{acc}\t{label}\t{pid:.1f}\t{n}\t{aln.score:.0f}\n")
            print(f"  {acc} {label:28s} identity={pid:5.1f}% over {n} cols score={aln.score:.0f}")

    # 3. RUN-domain search in worm N-terminal region with shuffle null
    print("\n== Worm N-terminal region vs RUN domains (local SW, 200 shuffles) ==")
    nterm = seqs[WORM][: wrh[0] - 1]
    rng = random.Random(1)
    with open(OUT / "run_search.tsv", "w") as fh:
        fh.write("run_source\trun_span\tworm_region\tscore\tnull_mean\tnull_sd\tz\n")
        for acc in ("Q92622", "Q9W3C9"):
            span = domain_span(doms[acc], is_run)
            if span is None:
                print(f"  {acc}: no RUN domain annotated; skipped")
                continue
            run_seq = seqs[acc][span[0] - 1 : span[1]]
            al = aligner("local")
            score = al.score(nterm, run_seq)
            null = []
            for _ in range(200):
                l = list(nterm)
                rng.shuffle(l)
                null.append(al.score("".join(l), run_seq))
            mu = sum(null) / len(null)
            sd = (sum((x - mu) ** 2 for x in null) / (len(null) - 1)) ** 0.5
            z = (score - mu) / sd if sd else float("nan")
            fh.write(f"{acc}\t{span[0]}-{span[1]}\t1-{wrh[0]-1}\t{score:.0f}\t{mu:.1f}\t{sd:.1f}\t{z:.2f}\n")
            print(f"  RUN of {acc} ({span[0]}-{span[1]}): score={score:.0f} null={mu:.1f}+/-{sd:.1f} z={z:.2f}")

    # 3b. all-vs-all RH and full-length local identity (to place fly/worm relative to RUBCN vs Pacer)
    print("\n== All-vs-all local identity (RH span / full length) ==")
    core = ["Q92622", "Q9H714", "Q9W3C9", WORM]
    with open(OUT / "pairwise_matrix.tsv", "w") as fh:
        fh.write("a\tb\tregion\tpercent_identity\taligned_columns\tscore\n")
        for i, a in enumerate(core):
            for b in core[i + 1 :]:
                for region in ("RH", "full"):
                    if region == "RH":
                        sa, sb = domain_span(doms[a], is_rh), domain_span(doms[b], is_rh)
                        qa, qb = seqs[a][sa[0] - 1 : sa[1]], seqs[b][sb[0] - 1 : sb[1]]
                    else:
                        qa, qb = seqs[a], seqs[b]
                    aln = aligner("local").align(qa, qb)[0]
                    pid, n = identity(aln)
                    fh.write(f"{a}\t{b}\t{region}\t{pid:.1f}\t{n}\t{aln.score:.0f}\n")
                    print(f"  {a} vs {b} {region:4s} identity={pid:5.1f}% over {n} cols score={aln.score:.0f}")
        ra, rb = domain_span(doms["Q92622"], is_run), domain_span(doms["Q9W3C9"], is_run)
        if ra and rb:
            aln = aligner("local").align(seqs["Q92622"][ra[0]-1:ra[1]], seqs["Q9W3C9"][rb[0]-1:rb[1]])[0]
            pid, n = identity(aln)
            fh.write(f"Q92622\tQ9W3C9\tRUN\t{pid:.1f}\t{n}\t{aln.score:.0f}\n")
            print(f"  Q92622 vs Q9W3C9 RUN  identity={pid:5.1f}% over {n} cols score={aln.score:.0f}")

    # 4. Cys/His pattern in RH domains
    print("\n== Cys/His counts in RH domain spans ==")
    for acc, label in ACCS.items():
        span = domain_span(doms[acc], is_rh)
        if span is None:
            continue
        s = seqs[acc][span[0] - 1 : span[1]]
        print(f"  {acc} {label:28s} RH {span[0]}-{span[1]} len={len(s)} C={s.count('C')} H={s.count('H')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
