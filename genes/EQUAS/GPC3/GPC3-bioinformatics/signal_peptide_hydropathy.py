# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Hydropathy and von Heijne-style signal-peptide check of the donkey GPC3 A0A9L0J2B1 N-terminus.

Question: does the alternative N-terminus of A0A9L0J2B1 contain a secretory signal
peptide (a different one from the human leader), which would let the product enter
the ER, be GPI-anchored, carry heparan sulfate and reach the cell surface?

Method (no external predictor is installed; this is a transparent rule-based check):

1. Kyte-Doolittle hydropathy (Kyte & Doolittle 1982) in sliding windows of 7, 9 and 11
   residues over residues 1..50; report the maximum window mean and its position.
2. von Heijne-style tripartite scan (von Heijne 1985, 1986): for every candidate
   h-region (a contiguous run of 7-15 residues starting at position 2..12, from the
   apolar set AVLIFMCWG plus at most one S or T, with at most one G, hence no charged
   residue and no P), require
   - an n-region (residues before the h-region) of 1-11 residues with net charge >= 0
     (K, R counted +1; D, E counted -1; the free N-terminal amine is not counted);
   - a c-region of 3-10 residues after the h-region whose last residue (-1) and the
     residue two before it (-3) are small/neutral (A, G, S, C, T, Q for -3; A, G, S, C,
     T for -1), with no P at -3..-1;
   - total signal length 15-35.
   The c-region upper bound (10) and the single S/T allowance were set so that both
   positive controls below pass; they are the only calibration applied.
   Report the best h-region (longest; ties broken by mean KD) and whether a full
   n/h/c assignment with a valid -3/-1 cleavage motif exists.
3. Controls: the human GPC3 leader (P51654, FT SIGNAL 1..24) read from the FASTA file,
   and the canonical donkey GPC3 product A0A9L0JGR2 N-terminus (sequence as recorded in
   RESULTS-rereview.md from the UniProt REST API, 2026-10-21) must both pass.

Rule-based scoring is weaker than a trained predictor (SignalP); a failed call is
evidence against a classical Sec signal peptide, not proof of absence.

Usage (from this folder):
    uv run --script signal_peptide_hydropathy.py ../GPC3-uniprot.txt human-GPC3-P51654.fasta
"""

import sys

KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}
APOLAR = set("AVLIFMCWG")
CHARGE = {"K": 1, "R": 1, "D": -1, "E": -1}
SMALL_M1 = set("AGSCT")
SMALL_M3 = set("AGSCTQ")

# Canonical donkey GPC3 product A0A9L0JGR2, N-terminal 67 residues, as recorded in
# RESULTS-rereview.md (UniProt REST API, 2026-10-21). Used only as a positive control.
DONKEY_CANONICAL_NTERM = "MAGTVHTACLVVAMLLSLDCPGQAQPPPPPPDATCHQVRSFFQRLQPGLKWVPETPVPGSDLQVCLPK"


def read_uniprot_flat(path: str) -> str:
    seq, in_sq = [], False
    for line in open(path):
        if line.startswith("SQ "):
            in_sq = True
            continue
        if in_sq:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", "").strip())
    return "".join(seq)


def read_fasta(path: str) -> str:
    return "".join(line.strip() for line in open(path) if not line.startswith(">"))


def kd_windows(seq: str, width: int, limit: int = 50) -> tuple[float, int]:
    region = seq[:limit]
    best, best_pos = -99.0, 0
    for i in range(len(region) - width + 1):
        mean = sum(KD[a] for a in region[i : i + width]) / width
        if mean > best:
            best, best_pos = mean, i + 1
    return best, best_pos


def h_regions(seq: str) -> list[tuple[int, int]]:
    """Candidate h-regions as (start, end), 1-based inclusive."""
    out = []
    for start in range(2, 13):
        for length in range(7, 16):
            end = start + length - 1
            seg = seq[start - 1 : end]
            if len(seg) < length:
                continue
            polar = sum(a in "ST" for a in seg)
            if all(a in APOLAR or a in "ST" for a in seg) and polar <= 1 and seg.count("G") <= 1:
                out.append((start, end))
    return out


def full_signal(seq: str, h: tuple[int, int]) -> int | None:
    """Return a cleavage position (last residue of the signal) or None."""
    start, end = h
    nreg = seq[: start - 1]
    if not 1 <= len(nreg) <= 11 or sum(CHARGE.get(a, 0) for a in nreg) < 0:
        return None
    for clen in range(3, 11):
        cut = end + clen
        if not 15 <= cut <= 35 or cut > len(seq):
            continue
        m1, m3 = seq[cut - 1], seq[cut - 3]
        if m1 in SMALL_M1 and m3 in SMALL_M3 and "P" not in seq[cut - 3 : cut]:
            return cut
    return None


def report(name: str, seq: str) -> None:
    print(f"== {name}")
    print(f"N-terminal 50: {seq[:50]}")
    for w in (7, 9, 11):
        best, pos = kd_windows(seq, w)
        print(f"Max Kyte-Doolittle mean, window {w}: {best:.2f} at residues {pos}..{pos + w - 1}")
    cands = h_regions(seq)
    if not cands:
        print("Apolar h-region (7-15 residues, start 2..12, <=1 S/T): none")
        print("Signal peptide (n/h/c rule): NOT FOUND")
        return
    best = max(cands, key=lambda h: (h[1] - h[0], sum(KD[a] for a in seq[h[0] - 1 : h[1]])))
    seg = seq[best[0] - 1 : best[1]]
    print(f"Longest apolar h-region: {best[0]}..{best[1]} {seg} (mean KD {sum(KD[a] for a in seg) / len(seg):.2f})")
    hits = [(h, full_signal(seq, h)) for h in cands]
    hits = [(h, c) for h, c in hits if c is not None]
    if hits:
        h, cut = hits[0]
        print(f"Signal peptide (n/h/c rule): FOUND, h {h[0]}..{h[1]}, predicted cleavage after {cut} ({seq[:cut]})")
    else:
        print("Signal peptide (n/h/c rule): NOT FOUND")


def main() -> None:
    donkey = read_uniprot_flat(sys.argv[1])
    human = read_fasta(sys.argv[2])
    report("Positive control: human GPC3 P51654 (FT SIGNAL 1..24)", human)
    report("Positive control: donkey canonical GPC3 A0A9L0JGR2", DONKEY_CANONICAL_NTERM)
    report("Query: donkey GPC3 A0A9L0J2B1", donkey)
    print("== Query: longest apolar run anywhere in A0A9L0J2B1 residues 1..50")
    run, best_run, best_start = 0, 0, 0
    for i, a in enumerate(donkey[:50]):
        run = run + 1 if a in APOLAR else 0
        if run > best_run:
            best_run, best_start = run, i - run + 2
    print(f"Longest apolar run: {best_run} residues at {best_start}..{best_start + best_run - 1} "
          f"({donkey[best_start - 1 : best_start - 1 + best_run]})")
    charged = [(i + 1, a) for i, a in enumerate(donkey[:43]) if a in CHARGE or a == "H"]
    print(f"Charged/His residues in 1..43: {' '.join(f'{a}{p}' for p, a in charged)}")


if __name__ == "__main__":
    main()
