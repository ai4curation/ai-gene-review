#!/usr/bin/env python3
"""Is human ADCK5 (Q3MIX3) built like a canonical protein kinase, or like a UbiB
atypical kinase?

Stefely et al. 2015 (PMID:25498144) defined the sequence features that distinguish the
UbiB family from the rest of the protein-kinase-like (PKL) superfamily, and showed that
two of them are positioned to *inhibit* protein kinase activity:

  * the invariant **KxGQ** motif, whose N-terminal domain "occupies the typical substrate
    binding pocket";
  * an **AAAS** motif in an alanine-rich (**A-rich**) loop that "replaces the canonical
    glycine-rich (G-rich) nucleotide-binding loop" and confers selectivity for ADP over ATP.

Stefely et al. 2016 (PMID:27499294) then showed COQ8A/Coq8p "lacks canonical protein
kinase activity in trans" and instead has ATPase activity.

This script asks, per column of a real multiple sequence alignment, whether ADCK5 sits on
the UbiB side or the canonical-protein-kinase side of each diagnostic position.

Design notes (deliberate, please do not "simplify" these away):

* Motif columns are located from a **reference sequence whose residue numbering is
  published**, and every reference residue is ASSERTED against the literature value before
  anything is read off the alignment. A drifted anchor must be a hard error, not a silent
  mis-read (the alignment would happily report a residue from the wrong column).
* Both a **positive control** (COQ8B, a UbiB protein with the same demonstrated
  non-protein-kinase behaviour) and a **negative control** (PKA Calpha, an archetypal
  active protein kinase) are carried through, so the discriminating power of each column is
  visible rather than assumed. A column on which PKA and the UbiB proteins agree tells us
  nothing and is reported as non-discriminating.
* Percent identity is computed and printed next to every call, because a motif "match" at
  low identity can be alignment noise.
"""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
FASTA = HERE / "ubib_family.fasta"
ALN = HERE / "ubib_family.aln.fasta"
RESULTS_JSON = HERE / "results.json"

SUBJECT = "ADCK5"

# accession -> (label, role)
SEQUENCES: dict[str, tuple[str, str]] = {
    "Q3MIX3": ("ADCK5", "subject"),
    "Q86TW2": ("ADCK1", "human_ubib_paralog"),
    "Q7Z695": ("ADCK2", "human_ubib_paralog"),
    "Q8NI60": ("COQ8A", "ubib_reference_characterised"),
    "Q96D53": ("COQ8B", "ubib_positive_control"),
    "P27697": ("Coq8p_yeast", "ubib_positive_control"),
    "P0A6A0": ("UbiB_ecoli", "ubib_founding_member"),
    "P17612": ("PKA_Calpha", "canonical_pk_negative_control"),
}

# Residues whose numbering is stated in the primary literature. Asserted before use.
# COQ8A numbering from PMID:27499294 (K276 KxGQ; D507 Mg-nucleotide; D488 catalytic base)
# and PMID:25498144 (A339 A-rich loop).
COQ8A_ANCHORS = {276: "K", 339: "A", 488: "D", 507: "D"}
# Yeast Coq8p numbering from PMID:27499294 (K134 KxGQ, A197 A-rich, D365 active site).
COQ8Y_ANCHORS = {134: "K", 197: "A", 365: "D"}
# PKA Calpha canonical protein-kinase catalytic machinery.
# NOTE: the classical Knighton numbering (G52/K72/E91/D166/N171/D184) counts from the
# MATURE protein; UniProt P17612 counts the initiator Met, so every number is +1. This
# script uses UniProt numbering throughout. The mismatch was caught by
# assert_literature_anchors() rather than by reading, which is the whole point of it.
PKA_ANCHORS = {53: "G", 73: "K", 92: "E", 167: "D", 172: "N", 185: "D"}


@dataclass(frozen=True)
class Column:
    """One diagnostic alignment column."""

    name: str
    # (reference label, 1-based residue number in that reference)
    ref_label: str
    ref_pos: int
    # what the UbiB family is expected to carry here, and what a canonical PK carries
    ubib_expect: str
    canonical_pk_expect: str
    note: str


DIAGNOSTIC_COLUMNS = [
    Column(
        "KxGQ_lysine",
        "COQ8A",
        276,
        "K",
        "-",
        "invariant UbiB KxGQ motif; its domain occludes the peptide-substrate pocket "
        "(PMID:25498144). Absent from canonical PKs entirely.",
    ),
    Column(
        "A_rich_loop_A339",
        "COQ8A",
        339,
        "A",
        "G",
        "AAAS A-rich loop replacing the canonical GxGxxG G-rich nucleotide loop; "
        "confers ADP-over-ATP selectivity. A->G flips selectivity and enables "
        "autophosphorylation (PMID:25498144).",
    ),
    Column(
        "catalytic_loop_Asp",
        "COQ8A",
        488,
        "D",
        "D",
        "catalytic-loop aspartate (putative catalytic base D488 in COQ8A; D166 in PKA).",
    ),
    Column(
        "DFG_Asp",
        "COQ8A",
        507,
        "D",
        "D",
        "Mg2+-binding aspartate of the DFG motif (D507 in COQ8A; D184 in PKA).",
    ),
    Column(
        "beta3_lysine",
        "PKA_Calpha",
        73,
        "K",
        "K",
        "beta3 VAIK lysine that positions the ATP alpha/beta phosphates.",
    ),
    Column(
        "alphaC_glutamate",
        "PKA_Calpha",
        92,
        "E",
        "E",
        "alphaC helix glutamate that salt-bridges the beta3 lysine in the active "
        "conformation.",
    ),
    Column(
        "G_rich_loop_G53",
        "PKA_Calpha",
        53,
        "A",
        "G",
        "second glycine of the canonical GxGxxG loop, critical for ATP binding and "
        "protein-kinase catalysis in PKA (PMID:25498144 discussion).",
    ),
    Column(
        "catalytic_loop_Asn",
        "PKA_Calpha",
        172,
        "N",
        "N",
        "catalytic-loop asparagine that chelates the second Mg2+.",
    ),
]


def fetch_sequences() -> dict[str, str]:
    """Download sequences, caching to FASTA. Fails loudly on an empty/dead accession."""
    if FASTA.exists():
        return read_fasta(FASTA)

    seqs: dict[str, str] = {}
    for acc, (label, _role) in SEQUENCES.items():
        url = (
            f"https://rest.uniprot.org/uniprotkb/{acc}.json"
            "?fields=accession,id,sequence,protein_name"
        )
        rec = json.load(urllib.request.urlopen(url))
        entry_name = rec.get("uniProtkbId")
        seq = rec.get("sequence", {}).get("value", "")
        # A dead/deleted UniProt accession returns an entry with no sequence and no name;
        # querying it is otherwise indistinguishable from a real but featureless protein.
        if not seq or not entry_name:
            raise SystemExit(
                f"FATAL: accession {acc} ({label}) returned no sequence/entry name "
                f"(entry_name={entry_name!r}, len={len(seq)}). This is what a deleted "
                f"UniProt entry looks like. Check the accession before re-running."
            )
        print(f"  fetched {acc} {entry_name} {label} {len(seq)} aa", file=sys.stderr)
        seqs[label] = seq

    with FASTA.open("w") as fh:
        for label, seq in seqs.items():
            fh.write(f">{label}\n")
            for i in range(0, len(seq), 60):
                fh.write(seq[i : i + 60] + "\n")
    return seqs


def read_fasta(path: Path) -> dict[str, str]:
    seqs: dict[str, str] = {}
    label = None
    buf: list[str] = []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if label is not None:
                seqs[label] = "".join(buf)
            label = line[1:].strip().split()[0]
            buf = []
        else:
            buf.append(line.strip())
    if label is not None:
        seqs[label] = "".join(buf)
    return seqs


def assert_literature_anchors(seqs: dict[str, str]) -> None:
    """Every published residue number must match the sequence we actually downloaded.

    Without this the script would happily read a residue out of a shifted column and
    report it as a finding.
    """
    checks = [
        ("COQ8A", COQ8A_ANCHORS, "PMID:25498144 / PMID:27499294"),
        ("Coq8p_yeast", COQ8Y_ANCHORS, "PMID:27499294"),
        ("PKA_Calpha", PKA_ANCHORS, "UniProt P17612 feature table"),
    ]
    for label, anchors, source in checks:
        seq = seqs[label]
        for pos, expected in anchors.items():
            got = seq[pos - 1]
            if got != expected:
                raise SystemExit(
                    f"FATAL: anchor drift. {label} residue {pos} is {got!r}, "
                    f"literature ({source}) says {expected!r}. The sequence version has "
                    f"changed; re-derive the residue numbers before trusting any column."
                )
        print(f"  anchors OK: {label} ({len(anchors)} residues, {source})", file=sys.stderr)


def align(seqs: dict[str, str]) -> dict[str, str]:
    if not ALN.exists():
        print("  running mafft --auto ...", file=sys.stderr)
        with ALN.open("w") as out:
            subprocess.run(
                ["mafft", "--auto", "--quiet", str(FASTA)],
                stdout=out,
                check=True,
            )
    aln = read_fasta(ALN)
    width = {len(s) for s in aln.values()}
    if len(width) != 1:
        raise SystemExit(f"FATAL: ragged alignment, widths={width}")
    if set(aln) != set(seqs):
        raise SystemExit(
            f"FATAL: alignment labels {sorted(aln)} != input labels {sorted(seqs)}"
        )
    return aln


def ungapped_to_column(aln_seq: str) -> dict[int, int]:
    """1-based residue number -> 0-based alignment column."""
    mapping: dict[int, int] = {}
    n = 0
    for col, ch in enumerate(aln_seq):
        if ch != "-":
            n += 1
            mapping[n] = col
    return mapping


def pct_identity(a: str, b: str) -> float:
    """Identity over columns where BOTH sequences have a residue."""
    both = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    if not both:
        return 0.0
    return 100.0 * sum(x == y for x, y in both) / len(both)


# Two of the diagnostic columns are anchored on DIFFERENT reference sequences but are
# claimed by the literature to be the same structural position: COQ8A's A-rich loop A339
# is "the analogous" position to the second glycine of PKA's GxGxxG loop (PMID:25498144
# discussion). If the alignment agrees, both anchors must resolve to ONE column. This is a
# real invariant, not a restatement of the input: nothing in the code forces it, and if
# mafft placed the loops differently the two would diverge and the A-rich claim would be
# unsupported by this alignment.
CROSS_ANCHOR_EQUIVALENCES = [("A_rich_loop_A339", "G_rich_loop_G53")]


def assert_cross_anchor_agreement(rows: list[dict]) -> None:
    by_name = {r["column"]: r for r in rows}
    for a, b in CROSS_ANCHOR_EQUIVALENCES:
        if a not in by_name or b not in by_name:
            raise SystemExit(
                f"FATAL: cross-anchor check names a column that does not exist "
                f"({a!r}/{b!r}). Present: {sorted(by_name)}. A guard that silently skips "
                f"a missing target is worse than no guard."
            )
        ca, cb = by_name[a]["alignment_column"], by_name[b]["alignment_column"]
        if ca != cb:
            raise SystemExit(
                f"FATAL: {a} (col {ca}) and {b} (col {cb}) were expected to be the same "
                f"structural position but the alignment separated them. The A-rich-loop "
                f"correspondence is NOT supported by this alignment - do not report it."
            )
        print(
            f"  cross-anchor OK: {a} and {b} both resolve to alignment column {ca}",
            file=sys.stderr,
        )


def self_test() -> int:
    """Break-test the guards: each must FAIL when its premise is violated, and PASS when
    it is not. A guard is only trustworthy if both directions have been exercised."""
    failures: list[str] = []

    def expect_exit(desc: str, fn) -> None:
        try:
            fn()
        except SystemExit:
            print(f"  PASS (correctly rejected): {desc}")
            return
        failures.append(f"guard did NOT fire: {desc}")
        print(f"  FAIL (accepted bad input): {desc}")

    def expect_ok(desc: str, fn) -> None:
        try:
            fn()
        except SystemExit as e:
            failures.append(f"guard fired on GOOD input: {desc} -> {e}")
            print(f"  FAIL (rejected good input): {desc}")
            return
        print(f"  PASS (correctly accepted): {desc}")

    seqs = fetch_sequences()

    # --- anchor guard: catch direction ---
    for label, pos in [("COQ8A", 276), ("PKA_Calpha", 73)]:
        bad = dict(seqs)
        s = bad[label]
        assert s[pos - 1] != "W", "mutation target already W; pick another residue"
        bad[label] = s[: pos - 1] + "W" + s[pos:]
        expect_exit(
            f"anchor guard on a mutated {label}:{pos}",
            lambda b=bad: assert_literature_anchors(b),
        )
    # --- anchor guard: happy direction (a guard can be wrong about success too) ---
    expect_ok("anchor guard on the unmodified sequences", lambda: assert_literature_anchors(seqs))

    # --- cross-anchor guard: catch, missing-target, and happy directions ---
    good = [
        {"column": "A_rich_loop_A339", "alignment_column": 391},
        {"column": "G_rich_loop_G53", "alignment_column": 391},
    ]
    expect_ok("cross-anchor guard on agreeing columns", lambda: assert_cross_anchor_agreement(good))
    disagree = [dict(good[0]), {"column": "G_rich_loop_G53", "alignment_column": 999}]
    expect_exit("cross-anchor guard on disagreeing columns", lambda: assert_cross_anchor_agreement(disagree))
    expect_exit(
        "cross-anchor guard when a named column is absent (deleting the guarded thing "
        "must not silently pass)",
        lambda: assert_cross_anchor_agreement([good[0]]),
    )

    print()
    if failures:
        for f in failures:
            print("SELF-TEST FAILURE:", f)
        return 1
    print("self-test: all guards behaved correctly in both directions")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    print("Fetching sequences...", file=sys.stderr)
    seqs = fetch_sequences()

    print("Verifying published residue numbers against downloaded sequences...", file=sys.stderr)
    assert_literature_anchors(seqs)

    print("Aligning...", file=sys.stderr)
    aln = align(seqs)
    maps = {label: ungapped_to_column(s) for label, s in aln.items()}

    subject_aln = aln[SUBJECT]
    identities = {
        label: round(pct_identity(subject_aln, s), 1)
        for label, s in aln.items()
        if label != SUBJECT
    }

    rows = []
    for col in DIAGNOSTIC_COLUMNS:
        ref_map = maps[col.ref_label]
        if col.ref_pos not in ref_map:
            raise SystemExit(
                f"FATAL: {col.ref_label} residue {col.ref_pos} missing from its own "
                f"alignment row - impossible unless the mapping is wrong."
            )
        c = ref_map[col.ref_pos]
        residues = {label: aln[label][c] for label in aln}

        subject_res = residues[SUBJECT]
        ubib_members = [
            label
            for _acc, (label, role) in SEQUENCES.items()
            if role != "canonical_pk_negative_control" and label != SUBJECT
        ]
        pk_control = residues["PKA_Calpha"]

        ubib_agree = sum(residues[m] == col.ubib_expect for m in ubib_members)
        # A column only discriminates if the canonical PK differs from the UbiB
        # expectation. Otherwise the subject matching "UbiB" is uninformative.
        discriminating = pk_control != col.ubib_expect

        rows.append(
            {
                "column": col.name,
                "reference": f"{col.ref_label}:{col.ref_pos}",
                "alignment_column": c + 1,
                "ubib_expected": col.ubib_expect,
                "canonical_pk_expected": col.canonical_pk_expect,
                "subject_residue": subject_res,
                "subject_position": next(
                    (p for p, cc in maps[SUBJECT].items() if cc == c), None
                ),
                "pka_residue": pk_control,
                "ubib_members_matching_expectation": f"{ubib_agree}/{len(ubib_members)}",
                "per_sequence": residues,
                "subject_matches_ubib": subject_res == col.ubib_expect,
                "column_discriminates_ubib_from_pk": discriminating,
                "note": col.note,
            }
        )

    assert_cross_anchor_agreement(rows)

    out = {
        "subject": SUBJECT,
        "subject_accession": "Q3MIX3",
        "n_sequences": len(aln),
        "alignment_width": len(subject_aln),
        "percent_identity_to_subject": identities,
        "columns": rows,
    }
    RESULTS_JSON.write_text(json.dumps(out, indent=2) + "\n")

    # ---- human-readable ----
    print()
    print(f"Percent identity to {SUBJECT} (over co-aligned columns):")
    for label, v in sorted(identities.items(), key=lambda kv: -kv[1]):
        print(f"  {label:<22} {v:5.1f}%")
    print()
    hdr = f"{'column':<22}{'ref':<14}{'UbiB':<6}{'PKA':<6}{SUBJECT:<8}{'disc?':<7}{'UbiB n/n':<10}"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        pos = r["subject_position"]
        sub = f"{r['subject_residue']}{pos if pos else ''}"
        print(
            f"{r['column']:<22}{r['reference']:<14}{r['ubib_expected']:<6}"
            f"{r['pka_residue']:<6}{sub:<8}"
            f"{'yes' if r['column_discriminates_ubib_from_pk'] else 'NO':<7}"
            f"{r['ubib_members_matching_expectation']:<10}"
        )
    print()
    print(f"Wrote {RESULTS_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
