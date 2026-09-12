"""How much of the AHNAK2 / AHNAK / periaxin similarity is the PDZ domain, and
how much is the low-complexity central repeat?

The AHNAK2 GO record is dominated by inferences donated by AHNAK (Q09666) and by
periaxin (PRX/Prx). PANTHER puts all three in PTHR23348, but in three *different*
subfamilies. Before treating any of those donations as ortholog-strength, measure
what the three proteins actually share.

Method, all computed, nothing hardcoded except the UniProt accessions:

* PDZ boundaries come from each entry's own UniProt FT DOMAIN record (PROSITE
  PS50106), not from an assumed offset.
* The repeat is located by its own anchor motif, discovered from AHNAK2 rather
  than asserted: take the most frequent 10-mer in AHNAK2 and require it to occur
  more than twice. Its occurrences define the repeat span.
* Pairwise identity is computed with Bio.Align.PairwiseAligner (BLOSUM62,
  local), separately for (a) the PDZ domains and (b) the full-length proteins,
  so a high full-length score driven by a shared low-complexity repeat cannot be
  mistaken for domain-wide homology.

Run: uv run python paralogue_architecture.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

from uniprot import _cached_get

HERE = Path(__file__).parent
ACCS = {
    "AHNAK2": "Q8IVF2",   # human, the subject
    "AHNAK2_MOUSE": "A0A7N9VR94",  # MGI:2144831, the ortholog donor (TrEMBL)
    "AHNAK": "Q09666",    # human paralogue, donor on the cytoplasm IBA
    "AHNAK_MOUSE": "E9Q616",  # MGI:1316648, donor on all three IBAs (TrEMBL)
    "PRX": "Q9BXM0",      # human periaxin, donor on the nucleus + cytoplasm IBAs
    "PRX_MOUSE": "O55103",  # MGI:108176, donor on all three IBAs
    "PRX_RAT": "Q63425",  # RGD:619960, donor on the nucleus + cytoplasm IBAs
}
# Pairs to score. The first block is the question; the second block is the
# ortholog-strength control that calibrates what a "high" number looks like.
PAIRS = [
    ("AHNAK2", "AHNAK"),
    ("AHNAK2", "PRX"),
    ("AHNAK2", "PRX_MOUSE"),
    ("AHNAK2", "PRX_RAT"),
    ("AHNAK2", "AHNAK2_MOUSE"),   # control: subject vs its own ortholog
    ("AHNAK", "AHNAK_MOUSE"),     # control: paralogue vs its own ortholog
    ("PRX", "PRX_MOUSE"),         # control: periaxin vs its own ortholog
]
ANCHOR_K = 10
MIN_ANCHOR_OCCURRENCES = 3


def entry(acc: str) -> dict:
    body = _cached_get(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json", f"arch_{acc}"
    )
    return json.loads(body)


def pdz_span(e: dict) -> tuple[int, int] | None:
    """(start, end) 1-based of the entry's own PDZ DOMAIN feature, or None.

    Returning None rather than raising is deliberate: unreviewed (TrEMBL)
    entries often carry no DOMAIN feature at all, and that is *data* about the
    donor's annotation depth, not a missing input. Callers print 'n/a' and the
    absence stays visible.
    """
    spans = [
        (f["location"]["start"]["value"], f["location"]["end"]["value"])
        for f in e.get("features", [])
        if f["type"] == "Domain" and "PDZ" in f.get("description", "")
    ]
    if not spans:
        return None
    if len(spans) > 1:
        raise SystemExit(f"{e['primaryAccession']} has {len(spans)} PDZ domains: {spans}")
    return spans[0]


def discover_anchor(seq: str) -> tuple[str, int]:
    """Most frequent k-mer in `seq`, with its count. Discovered, not asserted."""
    counts = Counter(seq[i:i + ANCHOR_K] for i in range(len(seq) - ANCHOR_K + 1))
    motif, n = counts.most_common(1)[0]
    if n < MIN_ANCHOR_OCCURRENCES:
        raise SystemExit(
            f"most frequent {ANCHOR_K}-mer occurs only {n}x -- no repeat to anchor on"
        )
    return motif, n


def occurrences(seq: str, motif: str) -> list[int]:
    out, i = [], seq.find(motif)
    while i != -1:
        out.append(i + 1)
        i = seq.find(motif, i + 1)
    return out


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "local"
    return a


def pct_identity(a: str, b: str) -> tuple[float, int]:
    """Local-alignment percent identity and aligned length."""
    aln = aligner().align(a, b)[0]
    sa, sb = aln[0], aln[1]
    ident = sum(1 for x, y in zip(sa, sb) if x == y and x != "-")
    n = sum(1 for x, y in zip(sa, sb) if x != "-" and y != "-")
    return 100.0 * ident / n, n


def split_by_repeat(a: str, b: str, span: tuple[int, int]) -> dict[str, tuple[float, int]]:
    """Percent identity of the a-vs-b local alignment, partitioned by whether the
    position in `a` falls inside `span` (the low-complexity repeat) or outside.

    This is the measurement the paralogue question actually needs: a big
    full-length alignment between two giant repeat proteins tells you nothing if
    every aligned column is repeat-on-repeat.
    """
    aln = aligner().align(a, b)[0]
    pos_a = aln.aligned[0][0][0]  # 0-based start in a
    ident = {"inside": 0, "outside": 0}
    total = {"inside": 0, "outside": 0}
    sa, sb = aln[0], aln[1]
    for x, y in zip(sa, sb):
        if x != "-":
            pos_a += 1
        if x == "-" or y == "-":
            continue
        key = "inside" if span[0] <= pos_a <= span[1] else "outside"
        total[key] += 1
        if x == y:
            ident[key] += 1
    return {
        k: ((100.0 * ident[k] / total[k]) if total[k] else float("nan"), total[k])
        for k in ("inside", "outside")
    }


def main() -> None:
    entries = {name: entry(acc) for name, acc in ACCS.items()}
    seqs = {n: e["sequence"]["value"] for n, e in entries.items()}
    pdz = {n: pdz_span(e) for n, e in entries.items()}

    lines: list[str] = []

    def say(s: str = "") -> None:
        print(s)
        lines.append(s)

    say("## Architecture of the three donors vs AHNAK2")
    say()
    say("| protein | accession | status | length | PDZ (UniProt FT) | PDZ as % of chain |")
    say("|---|---|---|---|---|---|")
    for n, acc in ACCS.items():
        L = len(seqs[n])
        status = ("Swiss-Prot" if entries[n]["entryType"].startswith("UniProtKB reviewed")
                  else "TrEMBL")
        if pdz[n] is None:
            say(f"| {n} | {acc} | {status} | {L} | none annotated | n/a |")
        else:
            s, e = pdz[n]
            say(f"| {n} | {acc} | {status} | {L} | {s}-{e} | "
                f"{100.0 * (e - s + 1) / L:.1f}% |")
    say()

    say("Each giant AHNAK has a large central repeat. Discover each one's own anchor")
    say("rather than assuming they share a unit, then cross-test.")
    say()
    say("| protein | own most frequent 10-mer | occurrences |")
    say("|---|---|---|")
    own_anchor: dict[str, str] = {}
    for n in ACCS:
        counts = Counter(seqs[n][i:i + ANCHOR_K] for i in range(len(seqs[n]) - ANCHOR_K + 1))
        m, c = counts.most_common(1)[0]
        own_anchor[n] = m
        say(f"| {n} | `{m}` | {c} |")
    say()

    motif, n_hits = discover_anchor(seqs["AHNAK2"])
    say(f"Cross-test of the AHNAK2 anchor `{motif}` ({n_hits} occurrences in AHNAK2) "
        "against every other protein:")
    say()
    say("| protein | AHNAK2-anchor occurrences | first | last | span | span as % of chain |")
    say("|---|---|---|---|---|---|")
    spans: dict[str, tuple[int, int] | None] = {}
    for n in ACCS:
        occ = occurrences(seqs[n], motif)
        L = len(seqs[n])
        if occ:
            spans[n] = (occ[0], occ[-1] + ANCHOR_K - 1)
            say(f"| {n} | {len(occ)} | {occ[0]} | {occ[-1]} | "
                f"{spans[n][0]}-{spans[n][1]} | "
                f"{100.0 * (spans[n][1] - spans[n][0] + 1) / L:.1f}% |")
        else:
            spans[n] = None
            say(f"| {n} | 0 | - | - | - | 0.0% |")
    say()

    say("The only structured domain either AHNAK has is the PDZ. Score it separately")
    say("from the full-length alignment, and calibrate against ortholog controls.")
    say()
    say("| pair | PDZ-vs-PDZ identity | aligned aa | full-length local identity | aligned aa |")
    say("|---|---|---|---|---|")
    for left, right in PAIRS:
        fid, fn = pct_identity(seqs[left], seqs[right])
        if pdz[left] is None or pdz[right] is None:
            missing = [x for x in (left, right) if pdz[x] is None]
            say(f"| {left} vs {right} | n/a (no PDZ feature on {', '.join(missing)}) | - "
                f"| {fid:.1f}% | {fn} |")
            continue
        s1, e1 = pdz[left]
        s2, e2 = pdz[right]
        pid, pn = pct_identity(seqs[left][s1 - 1:e1], seqs[right][s2 - 1:e2])
        say(f"| {left} vs {right} | {pid:.1f}% | {pn} | {fid:.1f}% | {fn} |")
    say()

    # How much of each full-length alignment is repeat-on-repeat?
    rep = spans["AHNAK2"]
    say(f"Partition of the AHNAK2 full-length local alignment by the AHNAK2 repeat "
        f"span {rep[0]}-{rep[1]}:")
    say()
    say("| pair | aligned aa inside repeat | identity inside | aligned aa outside | "
        "identity outside | % of aligned length inside |")
    say("|---|---|---|---|---|---|")
    for other in ("AHNAK", "PRX", "AHNAK2_MOUSE"):
        d = split_by_repeat(seqs["AHNAK2"], seqs[other], rep)
        tot = d["inside"][1] + d["outside"][1]
        say(f"| AHNAK2 vs {other} | {d['inside'][1]} | {d['inside'][0]:.1f}% | "
            f"{d['outside'][1]} | {d['outside'][0]:.1f}% | "
            f"{100.0 * d['inside'][1] / tot:.1f}% |")
    say()

    (HERE / "paralogue_architecture.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
