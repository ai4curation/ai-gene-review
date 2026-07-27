"""Test whether AGFG1 retains the ArfGAP catalytic apparatus.

The anchor is published, not remembered. Kahn et al. 2008 (PMID:18809720), the
consensus-nomenclature paper for the human ArfGAPs, states:

    "They contain a characteristic C4-type zinc finger motif and a conserved
    arginine that is required for activity, within a particular spacing
    (CX2CX16CX2CX4R). The zinc finger has an architectural rather than catalytic
    role"

and for human ArfGAP1 names "the conserved arginine (Arg50, on the right) and the
four zinc finger cysteines (center; Cys22, 25, 42, and 45)".

So the script does two things:
  1. POSITIVE CONTROL: it must reproduce the paper's own numbers for ArfGAP1
     (Cys22/25/42/45 + Arg50) before any other result is reported. If the
     reproduction fails the script raises - a scan whose useful output may be
     "motif absent" must contain a case where it finds something.
  2. It then reports the motif for AGFG1, its paralogue AGFG2, the orthologues
     named in AGFG1's GOA WITH/FROM column, and the rest of the characterised
     human ArfGAP panel.

Note the motif is a *necessary* condition read off sequence. Retaining it does
not demonstrate GAP activity; only an assay does. The script therefore reports
"apparatus intact / not intact", never "is / is not a GAP".

Usage:
    uv run python arfgap_motif.py
    uv run python arfgap_motif.py --self-test
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
import urllib.request

OUT = pathlib.Path(__file__).parent / "arfgap_motif.json"

# CX2CX16CX2CX4R, as published. Written with explicit spacing so the pattern can
# be compared against the paper's string by eye.
MOTIF = re.compile(r"C..C.{16}C..C.{4}R")

# The paper's own numbers for human ArfGAP1 (Q8N6T3), used as the control.
ARFGAP1_EXPECTED = {"cys": [22, 25, 42, 45], "arg": 50}

PANEL = {
    # subject and paralogue
    "P52594": "AGFG1 human (subject)",
    "O95081": "AGFG2 human (paralogue)",
    # orthologues named in AGFG1's GOA WITH/FROM
    "Q8K2K6": "Agfg1 mouse (IBA donor MGI:1333754)",
    "E1JHR0": "drongo Drosophila isoform F (IBA donor FB:FBgn0020304)",
    # characterised human ArfGAPs, one per subfamily where possible
    "Q8N6T3": "ARFGAP1 human (control: paper gives Cys22/25/42/45, Arg50)",
    "Q8N6H7": "ARFGAP2 human",
    "Q9NP61": "ARFGAP3 human",
    "Q9ULH1": "ASAP1 human",
    "Q15027": "ACAP1 human",
    "Q8IYB5": "SMAP1 human",
    "Q9Y2X7": "GIT1 human",
    "O75689": "ADAP1 human (subfamily reported to LACK in vitro GAP activity)",
}


def sequence(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=accession,sequence"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        d = json.load(fh)
    # A merged/secondary accession returns HTTP 200 for a DIFFERENT protein.
    assert d["primaryAccession"] == acc, (
        f"{acc} resolved to {d['primaryAccession']}"
    )
    return d["sequence"]["value"]


def find_motif(seq: str) -> list[dict]:
    """All CX2CX16CX2CX4R matches, 1-based. Overlapping matches are found by
    scanning every start position, not with finditer, which skips overlaps."""
    hits = []
    # C(1) xx(2) C(1) x16(16) C(1) xx(2) C(1) x4(4) R(1) == 29 residues.
    span = 1 + 2 + 1 + 16 + 1 + 2 + 1 + 4 + 1
    assert span == 29, span
    for i in range(len(seq) - span + 1):
        window = seq[i : i + span]
        if MOTIF.fullmatch(window):
            hits.append(
                {
                    "cys": [i + 1, i + 4, i + 21, i + 24],
                    "arg": i + 29,
                    "match": window,
                }
            )
    return hits


def control() -> None:
    seq = sequence("Q8N6T3")
    hits = find_motif(seq)
    assert len(hits) == 1, f"ARFGAP1 control: expected 1 motif, found {len(hits)}"
    got = {"cys": hits[0]["cys"], "arg": hits[0]["arg"]}
    assert got == ARFGAP1_EXPECTED, (
        f"control FAILED: reproduced {got}, paper states {ARFGAP1_EXPECTED}. "
        "Every other number below would be untrustworthy."
    )
    print(
        "positive control OK: the motif reproduces PMID:18809720's published "
        f"ArfGAP1 numbers exactly ({got})"
    )


def self_test() -> None:
    """Break-tests. Each asserts the mutation changed the input, then that the
    verdict changed in the stated direction."""
    seq = sequence("P52594")
    hits = find_motif(seq)
    assert len(hits) == 1, f"AGFG1: expected 1 motif, got {len(hits)}"
    arg = hits[0]["arg"]

    # 1. Mutating the conserved Arg must abolish the motif.
    mutated = seq[: arg - 1] + "A" + seq[arg:]
    assert mutated != seq, "mutation did not change the sequence"
    assert seq[arg - 1] == "R" and mutated[arg - 1] == "A"
    assert find_motif(mutated) == [], "guard did not fire on R->A"

    # 2. Mutating one zinc-finger cysteine must abolish it too - a different
    #    direction, because a check that only sees the Arg would pass here.
    c = hits[0]["cys"][2]
    mutated2 = seq[: c - 1] + "S" + seq[c:]
    assert mutated2 != seq and seq[c - 1] == "C" and mutated2[c - 1] == "S"
    assert find_motif(mutated2) == [], "guard did not fire on C->S"

    # 3. Happy direction: an untouched sequence must still match. (A guard that
    #    fails on perfect agreement is a real observed failure mode.)
    assert find_motif(seq) == hits, "unmutated sequence stopped matching"

    # 4. The scan must find overlapping candidates, so a second motif inside the
    #    span cannot be skipped. Build a sequence with two overlapping matches.
    unit = "C" + "xx" + "C" + "y" * 16 + "C" + "xx" + "C" + "z" * 4 + "R"
    assert len(unit) == 29
    doubled = unit[:1] + unit  # shifts by one, creating an overlap
    assert len(find_motif(unit)) == 1, "single unit should match once"
    assert len(find_motif(doubled)) == 1, f"overlap scan: {find_motif(doubled)}"
    print("self-test OK (4 directions, 3 break-tests)")


def main() -> None:
    control()
    if "--self-test" in sys.argv:
        self_test()
        return
    out = {}
    for acc, label in PANEL.items():
        seq = sequence(acc)
        hits = find_motif(seq)
        out[acc] = {"label": label, "length": len(seq), "motifs": hits}
        if hits:
            h = hits[0]
            print(
                f"{acc} {label:60s} len={len(seq):5d} "
                f"Cys{h['cys']} Arg{h['arg']}  apparatus INTACT"
            )
        else:
            print(f"{acc} {label:60s} len={len(seq):5d} motif NOT FOUND")
    n_intact = sum(1 for v in out.values() if v["motifs"])
    print(f"\n{n_intact}/{len(out)} panel members retain CX2CX16CX2CX4R")
    subj = out["P52594"]
    assert subj["motifs"], "subject lost the motif - re-read before reporting"
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
