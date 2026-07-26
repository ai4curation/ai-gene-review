"""Can a shotgun-proteomics experiment attribute an actin peptide to ACTA1?

Five of ACTA1's GOA rows are HDA (high-throughput mass spectrometry) placements in
extracellular compartments -- prostatic-secretion exosomes, parotid exosomes,
trabecular-meshwork exosomes, plasma microparticles and tears -- none of which is
skeletal muscle. Whether those rows can be about ACTA1 *specifically* depends on a
measurable quantity: how much of ACTA1's tryptic peptide space is distinguishable
from the other five human actins.

This script computes that. It does an in-silico trypsin digest of all six human
actin isoforms and asks, for each ACTA1 peptide in a plausible MS-detectable
length range, whether that exact peptide also occurs in any other human actin.

Nothing is hardcoded: sequences are fetched from UniProt, and the script reports
whatever the numbers turn out to be.
"""
import itertools
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "peptide_specificity.json"

# The six conventional human actins. ACTA1 is the subject; the rest are the
# isoforms a mass spectrometer would have to be distinguished from.
ACTINS = {
    "ACTA1": "P68133",  # alpha skeletal muscle  (subject)
    "ACTA2": "P62736",  # alpha aortic smooth muscle
    "ACTC1": "P68032",  # alpha cardiac muscle
    "ACTG2": "P63267",  # gamma enteric smooth muscle
    "ACTB": "P60709",   # beta cytoplasmic
    "ACTG1": "P63261",  # gamma cytoplasmic
}

SUBJECT = "ACTA1"

# Peptide length window in which tryptic peptides are routinely observed by LC-MS/MS.
MIN_LEN, MAX_LEN = 7, 30

# How far below the panel median a sequence may fall before it is treated as truncated
# rather than merely divergent. The conventional actins span 375-377 aa, so 5 admits the
# genuine N-terminal-processing differences and nothing else.
MAX_LENGTH_DEFICIT = 5


def fetch_sequence(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as fh:
                text = fh.read().decode()
            break
        except urllib.error.URLError as exc:
            if attempt == 3:
                raise RuntimeError(f"could not fetch {acc}: {exc}") from exc
            time.sleep(2 * (attempt + 1))
    lines = [ln.strip() for ln in text.splitlines() if ln and not ln.startswith(">")]
    seq = "".join(lines)
    if not seq:
        raise RuntimeError(f"empty sequence for {acc}")
    return seq


def digest(seq: str, missed_cleavages: int = 2) -> set[str]:
    """Trypsin digest: cleave C-terminal to K or R, but not before P.

    Missed cleavages are included because real digests are incomplete, and a
    peptide spanning a missed site is more likely to carry an isoform-specific
    residue -- so ignoring them would bias the answer towards "distinguishable".
    """
    sites = [0]
    for m in re.finditer(r"[KR]", seq):
        i = m.end()
        if i < len(seq) and seq[i] == "P":
            continue
        sites.append(i)
    if sites[-1] != len(seq):
        sites.append(len(seq))
    peptides: set[str] = set()
    for a in range(len(sites) - 1):
        for b in range(a + 1, min(a + 2 + missed_cleavages, len(sites))):
            peptides.add(seq[sites[a]:sites[b]])
    return peptides


def identity(a: str, b: str) -> float:
    """Ungapped percent identity. Valid here only because all six actins are the
    same length; asserted rather than assumed."""
    assert len(a) == len(b), (len(a), len(b))
    same = sum(1 for x, y in zip(a, b) if x == y)
    return 100.0 * same / len(a)


def main() -> None:
    seqs = {name: fetch_sequence(acc) for name, acc in ACTINS.items()}
    for name, seq in seqs.items():
        print(f"{name:6} {ACTINS[name]}  {len(seq)} aa")

    # Length guard on the comparator panel. A Swiss-Prot entry that is truncated
    # relative to its orthologues manufactures apparent divergence out of residues the
    # sequence never reaches - the ACTL10 case, where a 245 aa entry against 346-368 aa
    # orthologues turned 20 absent positions into 20 "non-conservative substitutions".
    # Here it would inflate the distinguishing-peptide count, because a peptide absent
    # from a short comparator looks unique to ACTA1. So require every sequence to be
    # within a few residues of the panel median, and fail loudly naming the offender
    # rather than scoring a truncation.
    lengths = {n: len(q) for n, q in seqs.items()}
    median = sorted(lengths.values())[len(lengths) // 2]
    short = {n: L for n, L in lengths.items() if median - L > MAX_LENGTH_DEFICIT}
    if short:
        raise SystemExit(
            f"comparator panel has truncated entry/entries {short} against a panel median "
            f"of {median} aa; conservation and uniqueness counts computed on these would be "
            "artefacts of absent residues, not of sequence divergence"
        )
    print(f"length guard OK: all {len(lengths)} sequences within "
          f"{MAX_LENGTH_DEFICIT} aa of the panel median ({median} aa)")

    # The six isoforms are 375-377 aa (they differ in N-terminal processing), so an
    # ungapped identity is only meaningful for equal-length pairs. Report those and
    # name the pairs that were skipped, rather than silently omitting them or
    # forcing a comparison that would be off by a frame.
    ident, skipped = {}, []
    for a, b in itertools.combinations(sorted(seqs), 2):
        if len(seqs[a]) == len(seqs[b]):
            ident[f"{a}|{b}"] = round(identity(seqs[a], seqs[b]), 1)
        else:
            skipped.append(f"{a}|{b}")
    print("\npairwise identity (ungapped; equal-length pairs only):")
    for k, v in sorted(ident.items()):
        print(f"  {k:14} {v:5.1f}%")
    print(f"  skipped (unequal length, needs alignment): {', '.join(skipped)}")

    digests = {name: digest(seq) for name, seq in seqs.items()}
    subject = {p for p in digests[SUBJECT] if MIN_LEN <= len(p) <= MAX_LEN}
    others: set[str] = set()
    for name, peps in digests.items():
        if name != SUBJECT:
            others |= peps

    unique = sorted(p for p in subject if p not in others)
    shared = sorted(p for p in subject if p in others)

    # Which isoforms does each shared peptide also occur in? A peptide shared only
    # with the other sarcomeric actins is a different problem from one shared with
    # the ubiquitous cytoplasmic actins, because ACTB/ACTG1 are expressed in every
    # tissue the five HDA studies sampled.
    cytoplasmic = digests["ACTB"] | digests["ACTG1"]
    shared_with_cytoplasmic = [p for p in shared if p in cytoplasmic]

    # Collapse missed-cleavage variants. Nine distinguishing peptides sounds like
    # nine independent handles, but most are nested extensions of the same span, so
    # the raw count overstates the evidence exactly as a whole-triad count would.
    # Group by overlap on the subject sequence and report BOTH numbers.
    spans = sorted((seqs[SUBJECT].index(p), seqs[SUBJECT].index(p) + len(p))
                   for p in unique)
    regions: list[list[int]] = []
    for start, end in spans:
        if regions and start < regions[-1][1]:
            regions[-1][1] = max(regions[-1][1], end)
        else:
            regions.append([start, end])

    result = {
        "accessions": ACTINS,
        "lengths": {k: len(v) for k, v in seqs.items()},
        "pairwise_identity_pct": ident,
        "identity_pairs_skipped_unequal_length": skipped,
        "peptide_window": [MIN_LEN, MAX_LEN],
        "n_subject_peptides_in_window": len(subject),
        "n_unique_to_subject": len(unique),
        "n_shared": len(shared),
        "pct_unique": round(100.0 * len(unique) / len(subject), 1) if subject else None,
        "n_shared_with_cytoplasmic_actins": len(shared_with_cytoplasmic),
        "n_independent_distinguishing_regions": len(regions),
        "distinguishing_regions": [
            {"start_1based": s + 1, "end_1based": e, "sequence": seqs[SUBJECT][s:e]}
            for s, e in regions
        ],
        "unique_peptides": unique,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")

    print(f"\ntryptic peptides of {SUBJECT} in the {MIN_LEN}-{MAX_LEN} aa window: "
          f"{len(subject)}")
    print(f"  distinguishing (found in no other human actin): {len(unique)} "
          f"({result['pct_unique']}%)")
    print(f"  shared with >=1 other human actin:              {len(shared)}")
    print(f"  of those, shared with ACTB and/or ACTG1:        "
          f"{len(shared_with_cytoplasmic)}")
    print(f"\nthose {len(unique)} peptides collapse to "
          f"{len(regions)} independent distinguishing region(s):")
    for s, e in regions:
        print(f"  {s + 1}-{e}: {seqs[SUBJECT][s:e]}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
