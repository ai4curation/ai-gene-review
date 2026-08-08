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

# ACTA1 is processed at its N-terminus: UniProt has INIT_MET 1 "Removed", CHAIN 2..377
# (intermediate form, N-acetylcysteine at residue 2) and CHAIN 3..377 for the mature
# protein, the acetylated cysteine being cleaved by ACTMAP. So the ORF sequence's
# N-terminal tryptic peptide does not exist in vivo, and a targeted-proteomics experiment
# built on it would name a species that cannot be detected. The mature chain is therefore
# the primary analysis; the ORF is computed alongside it only to show the counts agree.
# ACTA1's mature chain start is PARSED from the local UniProt record rather than typed in.
# A number transcribed from a feature table by hand is a latent bug: it cannot be checked
# against anything, and the guard below can only tell a corrupting offset from a plausible
# one, not a correct one from an off-by-one within the processing window (MATURE_START = 4
# yields region 4-30 and passes every check). Reading it from the source removes the class.
UNIPROT_TXT = HERE.parent / "ACTA1-uniprot.txt"

# N-terminal offsets applied to the COMPARATORS, in residues removed. ACTA1's own mature
# start is 3, but that number is specific to ACTA1 and must not be reused for the others:
# ACTB (P60709) is annotated CHAIN 1..375 *and* CHAIN 2..375 "N-terminally processed", so
# its observable forms begin at residue 1 or 2, and slicing it at 3 would both mis-state its
# processing and miss a form. Rather than look up six CHAIN features and depend on their
# completeness, every comparator contributes its digest at all three offsets. This can only
# ENLARGE the comparator peptide pool and therefore only shrink the distinguishing set, so
# the error direction is conservative by construction.
COMPARATOR_OFFSETS = (0, 1, 2)

# How far into the sequence a peptide may start and still count as "N-terminal" for the
# ORF-versus-mature agreement check below. This MUST be a fixed constant grounded in the
# biology - N-terminal processing of an actin removes at most a couple of residues - and must
# NOT be derived from MATURE_START. An earlier version used MATURE_START + 1, which made the
# tolerance scale with the parameter under test: setting MATURE_START to 50 widened the
# window to 51, so the check accepted its own corruption and reported a confident, wrong
# region (50-64) with no complaint. A guard whose tolerance is set by the thing it guards is
# worse than no guard, because it still reports success.
N_TERMINAL_TOLERANCE = 4

MATURE_START = 0  # replaced at run time by mature_chain_start()

# Peptide length window in which tryptic peptides are routinely observed by LC-MS/MS.
MIN_LEN, MAX_LEN = 7, 30

# How far below the panel median a sequence may fall before it is treated as truncated
# rather than merely divergent. The conventional actins span 375-377 aa, so 5 admits the
# genuine N-terminal-processing differences and nothing else.
MAX_LENGTH_DEFICIT = 5


def mature_chain_start() -> int:
    """First residue of ACTA1's mature chain, from the UniProt FT table.

    Picks the CHAIN feature whose /note matches the entry's RecName, i.e. the mature
    protein rather than the "intermediate form" that still carries N-acetyl-Cys2. Fails
    loudly if the record does not yield exactly one such feature, because silently
    defaulting would reintroduce the hand-typed constant this replaces.
    """
    if not UNIPROT_TXT.exists():
        raise SystemExit(f"missing {UNIPROT_TXT}; run: just fetch-gene human ACTA1")
    text = UNIPROT_TXT.read_text()
    rec = re.search(r"^DE   RecName: Full=([^;]+);", text, flags=re.M)
    if not rec:
        raise RuntimeError(f"no RecName in {UNIPROT_TXT.name}")
    want = rec.group(1).strip()
    starts = [
        int(m.group(1))
        for m in re.finditer(
            r'^FT   CHAIN\s+(\d+)\.\.\d+\n(?:FT\s+/note="([^"]+)")',
            text, flags=re.M)
        if m.group(2) == want
    ]
    if len(starts) != 1:
        raise RuntimeError(
            f"expected exactly one CHAIN feature noted {want!r} in {UNIPROT_TXT.name}, "
            f"found {len(starts)}: {starts}"
        )
    return starts[0]


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
    global MATURE_START
    MATURE_START = mature_chain_start()
    print(f"mature chain start parsed from {UNIPROT_TXT.name}: residue {MATURE_START}")
    if MATURE_START > N_TERMINAL_TOLERANCE:
        raise SystemExit(
            f"MATURE_START={MATURE_START} exceeds N_TERMINAL_TOLERANCE="
            f"{N_TERMINAL_TOLERANCE}; a chain start that far in is not N-terminal "
            "processing, and the ORF-versus-mature agreement check would be vacuous"
        )
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

    # Comparators contribute both their ORF and their own mature-chain digests, so a
    # peptide is only called distinguishing if no other actin can produce it in either
    # form. Not doing this would call an ACTA1 peptide unique merely because a comparator
    # happens to present it after its own N-terminal processing.
    others: set[str] = set()
    for name, seq in seqs.items():
        if name != SUBJECT:
            for off in COMPARATOR_OFFSETS:
                others |= digest(seq[off:])

    mature = seqs[SUBJECT][MATURE_START - 1:]
    subject = {p for p in digest(mature) if MIN_LEN <= len(p) <= MAX_LEN}

    # Cross-check against the ORF form. The reviewer's point was that the ORF's
    # N-terminal peptide is not observable; the counts are expected to be identical,
    # and if they ever diverge that is a finding rather than a detail to smooth over.
    orf_subject = {p for p in digest(seqs[SUBJECT]) if MIN_LEN <= len(p) <= MAX_LEN}
    orf_unique = {p for p in orf_subject if p not in others}

    unique = sorted(p for p in subject if p not in others)
    shared = sorted(p for p in subject if p in others)

    # Which isoforms does each shared peptide also occur in? A peptide shared only
    # with the other sarcomeric actins is a different problem from one shared with
    # the ubiquitous cytoplasmic actins, because ACTB/ACTG1 are expressed in every
    # tissue the five HDA studies sampled.
    # All comparator offsets again, for the same reason as the `others` set above.
    cytoplasmic = set()
    for name in ("ACTB", "ACTG1"):
        for off in COMPARATOR_OFFSETS:
            cytoplasmic |= digest(seqs[name][off:])
    shared_with_cytoplasmic = [p for p in shared if p in cytoplasmic]

    # Collapse missed-cleavage variants. Nine distinguishing peptides sounds like
    # nine independent handles, but most are nested extensions of the same span, so
    # the raw count overstates the evidence exactly as a whole-triad count would.
    # Group by overlap on the subject sequence and report BOTH numbers.
    # Coordinates are reported in full-length (ORF) numbering so they line up with
    # UniProt's feature table, but they are computed on the mature chain, hence the offset.
    off = MATURE_START - 1
    spans = sorted((mature.index(p) + off, mature.index(p) + len(p) + off)
                   for p in unique)
    regions: list[list[int]] = []
    for start, end in spans:
        if regions and start < regions[-1][1]:
            regions[-1][1] = max(regions[-1][1], end)
        else:
            regions.append([start, end])

    # Comparing SETS rather than cardinalities matters, and not only in principle: both
    # forms yield exactly 9 distinguishing peptides, so an equal-count test passes, yet the
    # sets differ in 4 members. An equal-cardinality check would have certified an agreement
    # that does not hold.
    #
    # But the sets are not SUPPOSED to be identical - modelling the N-terminal processing is
    # the whole point of the change, so the two N-terminal peptides necessarily differ. The
    # invariant worth asserting is therefore narrower and stronger: the counts must agree,
    # and every peptide the two forms disagree about must lie at the N-terminus. A divergence
    # anywhere else would mean the offset had corrupted the digest, and that is what this
    # catches.
    diff = orf_unique ^ set(unique)
    n_term_limit = N_TERMINAL_TOLERANCE
    positions = {}
    for pep in diff:
        for form, seq_ in (("orf", seqs[SUBJECT]), ("mature", mature)):
            i = seq_.find(pep)
            if i != -1:
                positions[pep] = i + 1 + (0 if form == "orf" else MATURE_START - 1)
                break
    # NOT `bool(diff) and all(...)`: with that, a run in which the two forms agree
    # completely - an empty symmetric difference, the best possible outcome - evaluates
    # False and is reported as corruption. `all()` over an empty set is already True,
    # which is the correct reading: nothing disagrees, so nothing disagrees off the
    # N-terminus.
    # Every differing peptide must have been located. A peptide present in neither form's
    # sequence would drop out of `positions` and be skipped by all(), passing vacuously -
    # impossible today because `mature` is a suffix of the ORF, but the guard should not
    # depend on that staying true.
    unlocated = sorted(diff - set(positions))
    if unlocated:
        raise SystemExit(
            f"could not locate {len(unlocated)} differing peptide(s) in either form: "
            f"{unlocated}; the agreement check cannot be evaluated"
        )
    confined = all(v <= n_term_limit for v in positions.values())
    counts_agree = len(orf_unique) == len(unique)

    print(f"  (ORF form gives {len(orf_unique)} distinguishing peptides; counts "
          f"{'agree' if counts_agree else 'DISAGREE'})")
    print(f"  ORF/mature sets differ in {len(diff)} peptide(s), all at the N-terminus: "
          f"{confined}")
    if not counts_agree or not confined:
        raise SystemExit(
            "ORF and mature analyses disagree beyond the N-terminal peptides "
            f"(counts_agree={counts_agree}, confined_to_n_terminus={confined}, "
            f"positions={positions}); the offset has corrupted the digest rather than "
            "merely modelled the processing"
        )

    result = {
        "accessions": ACTINS,
        "analysed_form": f"mature chain {MATURE_START}..{len(seqs[SUBJECT])} "
                         "(UniProt CHAIN; INIT_MET removed and N-acetyl-Cys2 cleaved by ACTMAP)",
        "n_unique_orf_form": len(orf_unique),
        "orf_and_mature_counts_agree": len(orf_unique) == len(unique),
        "orf_and_mature_sets_agree": sorted(orf_unique) == sorted(unique),
        "orf_vs_mature_symmetric_difference": sorted(orf_unique ^ set(unique)),
        "orf_vs_mature_difference_confined_to_n_terminus": confined,
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

    print(f"\ntryptic peptides of the {SUBJECT} MATURE chain "
          f"({MATURE_START}..{len(seqs[SUBJECT])}) in the {MIN_LEN}-{MAX_LEN} aa window: "
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
