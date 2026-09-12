#!/usr/bin/env python3
"""Corroborate UniProt-annotated TM helices against a hydropathy profile.

For each UniProt-annotated TRANSMEM segment, report the peak (max windowed
Kyte-Doolittle hydropathy) within that segment. A positive peak within an
annotated helix supports it being a genuine hydrophobic membrane-spanning
segment. This does NOT attempt to count helices de novo (see RESULTS.md for why
the sliding-window count is unreliable for closely packed MFS helices); it only
checks whether the annotated helices are hydrophobic.

Usage:
    python hydropathy_corroboration.py --fasta data/panel.fasta --acc P36032 \
        --topology results/uniprot_topology.tsv --out results/tm_hydropathy_corroboration.tsv
"""
import argparse
from pathlib import Path

from predict_tm import KD, hydropathy_profile, read_fasta


def load_transmem(topology_tsv: Path) -> list[tuple[int, int]]:
    segs = []
    for line in topology_tsv.read_text().splitlines()[1:]:
        parts = line.split("\t")
        if parts and parts[0] == "TRANSMEM":
            segs.append((int(parts[1]), int(parts[2])))
    return segs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fasta", required=True, type=Path)
    ap.add_argument("--acc", required=True)
    ap.add_argument("--topology", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--window", type=int, default=19)
    args = ap.parse_args()

    records = read_fasta(args.fasta)
    seq = None
    for name, s in records:
        if name.split("|")[0] == args.acc:
            seq = s
            break
    if seq is None:
        raise SystemExit(f"Accession {args.acc} not found in {args.fasta}")

    prof = hydropathy_profile(seq, args.window)
    segs = load_transmem(args.topology)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    n_hydrophobic = 0
    with args.out.open("w") as fh:
        fh.write("tm_index\tstart\tend\tpeak_hydropathy\tmean_hydropathy\thydrophobic_peak\n")
        for i, (s, e) in enumerate(segs, 1):
            window_vals = prof[s - 1 : e]
            peak = max(window_vals)
            mean = sum(window_vals) / len(window_vals)
            is_hydrophobic = peak > 0.0
            n_hydrophobic += int(is_hydrophobic)
            fh.write(f"{i}\t{s}\t{e}\t{peak:.2f}\t{mean:.2f}\t{is_hydrophobic}\n")

    print(f"Annotated TM helices: {len(segs)}")
    print(f"TM helices with a positive hydropathy peak: {n_hydrophobic}/{len(segs)}")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
