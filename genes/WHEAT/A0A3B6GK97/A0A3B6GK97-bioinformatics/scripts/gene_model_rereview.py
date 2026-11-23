"""Re-review analysis: is the A0A3B6GK97 N-terminal truncation a gene-model artifact?

Steps (all inputs fetched live; nothing hardcoded except accessions/ids given on the CLI):
1. Fetch the query and comparator protein sequences (UniProt REST).
2. Scan each for the patatin catalytic-Ser elbow (G-x-S-x-G) and oxyanion (DGGG) motifs.
3. Locally align the query to each comparator; report where the query starts on the comparator.
4. Fetch the genomic region upstream of the query gene (Ensembl REST), translate the three
   forward-strand frames, and (a) scan for the motifs and (b) locally align the comparator's
   N-terminal segment that the query lacks against each frame, to test whether the missing
   catalytic region is encoded upstream of the annotated start.

Usage:
  uv run python scripts/gene_model_rereview.py --query A0A3B6GK97 \
      --comparators A0A3B6E9X0,A0A9R1KF31,A0A1D5WV83,Q6ZG46 \
      --gene TraesCS3D02G033600 --upstream 8000 --outdir results_rereview
"""

import argparse
import json
import re
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Seq import Seq

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"
ENSEMBL = "https://rest.ensembl.org"
SER_ELBOW = re.compile(r"G.S.G")
OXYANION = re.compile(r"DGGG")


def fetch_protein(acc: str) -> str:
    r = requests.get(UNIPROT.format(acc=acc), timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def ensembl_get(path: str, **params) -> dict | str:
    r = requests.get(
        ENSEMBL + path, params=params, headers={"Content-Type": "application/json"}, timeout=120
    )
    r.raise_for_status()
    return r.json()


def motifs(seq: str) -> dict:
    return {
        "ser_elbow_GxSxG": [(m.start() + 1, m.group()) for m in SER_ELBOW.finditer(seq)],
        "oxyanion_DGGG": [(m.start() + 1, m.group()) for m in OXYANION.finditer(seq)],
    }


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "local"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    return a


def local_align(q: str, s: str) -> dict:
    aln = aligner().align(q, s)[0]
    qb, sb = aln.aligned
    ident = sum(
        sum(1 for i, j in zip(range(qs, qe), range(ss, se)) if q[i] == s[j])
        for (qs, qe), (ss, se) in zip(qb, sb)
    )
    alen = sum(qe - qs for qs, qe in qb)
    return {
        "score": aln.score,
        "query_start": int(qb[0][0]) + 1,
        "query_end": int(qb[-1][1]),
        "subject_start": int(sb[0][0]) + 1,
        "subject_end": int(sb[-1][1]),
        "aligned_query_residues": int(alen),
        "identity_pct": round(100 * ident / alen, 1) if alen else 0.0,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--query", required=True)
    p.add_argument("--comparators", required=True)
    p.add_argument("--gene", required=True)
    p.add_argument("--species", default="triticum_aestivum")
    p.add_argument("--upstream", type=int, default=8000)
    p.add_argument("--outdir", required=True)
    args = p.parse_args()
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    accs = [args.query] + args.comparators.split(",")
    seqs = {a: fetch_protein(a) for a in accs}
    q = seqs[args.query]

    report: dict = {"proteins": {}, "upstream": {}}
    for a, s in seqs.items():
        entry = {"length": len(s), **motifs(s)}
        if a != args.query:
            entry["alignment_vs_query"] = local_align(q, s)
        report["proteins"][a] = entry

    gene = ensembl_get(f"/lookup/id/{args.gene}", species=args.species)
    assert gene["strand"] == 1, "script assumes a forward-strand gene"
    chrom, gstart = gene["seq_region_name"], gene["start"]
    rstart = max(1, gstart - args.upstream)
    region = ensembl_get(
        f"/sequence/region/{args.species}/{chrom}:{rstart}..{gstart - 1}:1"
    )["seq"].upper()
    report["upstream"]["region"] = f"{chrom}:{rstart}-{gstart - 1}:+"
    report["upstream"]["length_nt"] = len(region)

    frames = {}
    for f in range(3):
        sub = region[f:]
        sub = sub[: len(sub) - len(sub) % 3]
        frames[f] = str(Seq(sub).translate())
    report["upstream"]["frames"] = {}
    for a in args.comparators.split(","):
        aln = report["proteins"][a]["alignment_vs_query"]
        missing = seqs[a][: max(0, aln["subject_start"] - 1 - aln["query_start"] + 1)]
        report["proteins"][a]["segment_missing_from_query_len"] = len(missing)
    for f, prot in frames.items():
        fr = {"motifs": motifs(prot), "best_hits_to_missing_segments": {}}
        for a in args.comparators.split(","):
            aln = report["proteins"][a]["alignment_vs_query"]
            seg = seqs[a][: aln["subject_start"] - 1]
            if len(seg) >= 20:
                hit = local_align(seg, prot.replace("*", "X"))
                fr["best_hits_to_missing_segments"][a] = hit
        report["upstream"]["frames"][str(f)] = fr
    (out / "upstream_frames.fasta").write_text(
        "".join(f">frame{f}\n{p}\n" for f, p in frames.items())
    )
    (out / "summary_rereview.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
