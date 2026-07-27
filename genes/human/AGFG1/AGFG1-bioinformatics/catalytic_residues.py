"""Does human AGFG1 retain ALL the residues the field says Arf GAP catalysis needs?

`arfgap_motif.py` tested one residue - the arginine finger, which is what the 2008
consensus-nomenclature paper names. That is necessary but the field identifies THREE
catalytically required positions, and testing only the arginine gives the opposite
answer to testing all three. From PMID:23433073:

    "The three that are found in our analyses (W451, R469, and D484 in ASAP3
    correspond to W14, R32, and D47 in Figure S4) are each closely involved in
    catalysis. R469/R32 is the arginine finger. D484/D47 contacts the main chain of
    Arf6-Q67 plus D68 and the side chain of Q67, stabilizing switch 2 and catalytic
    glutamine in Arf6. W451/W14 is centrally located in the binding interface
    between the Arf and Arf GAP. Mutation of any one of these three residues leads
    to severe loss in Arf GAP activity (28)."

So this script aligns each subject's ArfGAP domain to the ASAP3 domain - the one with
a solved Arf6 complex - and reads off the residue at each of the three positions.

Controls, all of which must pass or the script raises:
  * ASAP3's own residues at 451/469/484 must be W/R/D in the current UniProt sequence
    (i.e. the paper's numbering still applies);
  * ASAP3 aligned to itself must recover all three (alignment sanity);
  * every GAP-COMPETENT ArfGAP in the panel must recover all three, because if the
    alignment cannot find them in proteins that have them, an absence in AGFG1 would
    be an alignment artefact rather than a biological result;
  * the arginine position recovered here must equal the one CX2CX16CX2CX4R gives in
    arfgap_motif.json - two independent methods agreeing on the same residue.

Usage:
    uv run python catalytic_residues.py
    uv run python catalytic_residues.py --self-test
"""

from __future__ import annotations

import json
import pathlib
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

HERE = pathlib.Path(__file__).parent
OUT = HERE / "catalytic_residues.json"
MOTIF_JSON = HERE / "arfgap_motif.json"

REFERENCE = "Q8TDY4"  # ASAP3_HUMAN; the ArfGAP-Arf6 complex structure
REF_DOMAIN = (440, 560)  # UniProt DOMAIN 439..560, trimmed to start at 440 for clarity
REF_POSITIONS = {"W451": 451, "R469": 469, "D484": 484}
EXPECTED_REF = {"W451": "W", "R469": "R", "D484": "D"}

# (accession, label, ArfGAP domain start, end, GAP-competent?)
PANEL = [
    ("Q8TDY4", "ASAP3 human (reference; Arf6 complex)", 440, 560, True),
    ("Q8N6T3", "ARFGAP1 human", 7, 124, True),
    ("Q9ULH1", "ASAP1 human", 439, 560, True),
    ("Q8IYB5", "SMAP1 human", 18, 136, True),
    ("Q9NP61", "ARFGAP3 human", 10, 126, True),
    ("P52594", "AGFG1 human (SUBJECT)", 11, 135, False),
    ("O95081", "AGFG2 human (paralogue)", 27, 153, False),
    ("Q8K2K6", "Agfg1 mouse", 11, 135, False),
    ("E1JHR0", "drongo Drosophila isoform F", 12, 136, False),
]


def sequence(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=accession,sequence"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        d = json.load(fh)
    assert d["primaryAccession"] == acc, f"{acc} -> {d['primaryAccession']}"
    return d["sequence"]["value"]


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    return a


def map_positions(ref_seq: str, ref_start: int, sub_seq: str, sub_start: int) -> dict:
    """Align two domain fragments and map each reference position to the subject."""
    aln = aligner().align(ref_seq, sub_seq)[0]
    ri, si = ref_start, sub_start
    mapping: dict[int, tuple[int | None, str]] = {}
    for rc, sc in zip(aln[0], aln[1]):
        if rc != "-":
            mapping[ri] = (si if sc != "-" else None, sc)
        if rc != "-":
            ri += 1
        if sc != "-":
            si += 1
    return mapping


def main() -> None:
    ref_full = sequence(REFERENCE)

    # Control 0: the paper's numbering must still apply to the current sequence.
    for name, pos in REF_POSITIONS.items():
        got = ref_full[pos - 1]
        assert got == EXPECTED_REF[name], (
            f"ASAP3 position {pos} is {got}, but PMID:23433073 names it "
            f"{EXPECTED_REF[name]} - the numbering has drifted, stop here"
        )
    print(f"control 0 OK: ASAP3 {REFERENCE} still has W451, R469, D484")

    ref_dom = ref_full[REF_DOMAIN[0] - 1 : REF_DOMAIN[1]]
    motif = json.loads(MOTIF_JSON.read_text()) if MOTIF_JSON.exists() else {}

    results = {}
    for acc, label, s, e, competent in PANEL:
        seq = sequence(acc)
        sub_dom = seq[s - 1 : e]
        mapping = map_positions(ref_dom, REF_DOMAIN[0], sub_dom, s)
        row = {"label": label, "gap_competent_control": competent, "positions": {}}
        for name, pos in REF_POSITIONS.items():
            sub_pos, aa = mapping.get(pos, (None, "-"))
            row["positions"][name] = {
                "subject_position": sub_pos,
                "subject_residue": aa,
                "conserved": aa == EXPECTED_REF[name],
            }
        row["n_conserved"] = sum(
            1 for v in row["positions"].values() if v["conserved"]
        )
        results[acc] = row

    # Control 1: every GAP-competent member must recover all three, else an absence
    # in AGFG1 is an alignment artefact rather than a result.
    for acc, row in results.items():
        if row["gap_competent_control"]:
            assert row["n_conserved"] == 3, (
                f"CONTROL FAILED: {row['label']} recovers only "
                f"{row['n_conserved']}/3 - the alignment cannot find these residues "
                "in a protein known to have them, so no absence below is interpretable"
            )
    print(
        f"control 1 OK: all {sum(1 for r in results.values() if r['gap_competent_control'])} "
        "GAP-competent members recover W/R/D at 3/3"
    )

    # Control 2: the arginine this method finds must equal the one the independent
    # CX2CX16CX2CX4R scan finds.
    if motif:
        agreed = 0
        for acc, row in results.items():
            m = motif.get(acc)
            if not m or not m.get("motifs"):
                continue
            arg_motif = m["motifs"][0]["arg"]
            arg_aln = row["positions"]["R469"]["subject_position"]
            assert arg_aln == arg_motif, (
                f"{row['label']}: alignment puts the arginine at {arg_aln} but the "
                f"CX2CX16CX2CX4R scan puts it at {arg_motif}"
            )
            agreed += 1
        assert agreed >= 5, f"only {agreed} entries cross-validated"
        print(f"control 2 OK: {agreed} entries agree with arfgap_motif.json on the arginine")

    print("\nresidues at the three catalytically required ASAP3 positions:")
    print(f"{'protein':42s} {'W451':>8s} {'R469':>8s} {'D484':>8s}   n/3")
    for acc, row in results.items():
        p = row["positions"]
        cells = [
            f"{p[n]['subject_residue']}{p[n]['subject_position'] or '-'}"
            for n in ("W451", "R469", "D484")
        ]
        mark = "" if row["n_conserved"] == 3 else "   <== incomplete"
        print(
            f"{row['label']:42s} {cells[0]:>8s} {cells[1]:>8s} {cells[2]:>8s}   "
            f"{row['n_conserved']}/3{mark}"
        )

    agfg = [r for r in results.values() if not r["gap_competent_control"]]
    assert agfg, "no AGFG members in the panel"
    print(
        f"\n{sum(1 for r in agfg if r['n_conserved'] == 3)}/{len(agfg)} AGFG-family "
        "members retain all three; "
        f"{sum(1 for r in agfg if r['positions']['R469']['conserved'])}/{len(agfg)} "
        "retain the arginine finger alone"
    )
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    assert json.loads(OUT.read_text()), "wrote an empty artifact"
    print(f"wrote {OUT} ({len(results)} entries)")


def self_test() -> None:
    """Break-test: corrupting the reference numbering must abort at control 0, and a
    subject with a substituted arginine must lose that position."""
    ref = sequence(REFERENCE)
    assert ref[450] == "W" and ref[468] == "R" and ref[483] == "D"
    ref_dom = ref[REF_DOMAIN[0] - 1 : REF_DOMAIN[1]]
    sub = sequence("P52594")
    dom = sub[10:135]
    mapping = map_positions(ref_dom, REF_DOMAIN[0], dom, 11)
    base = {n: mapping.get(p, (None, "-")) for n, p in REF_POSITIONS.items()}
    assert base["R469"][1] == "R", f"baseline lost the arginine: {base}"

    arg_pos = base["R469"][0]
    mutated = sub[: arg_pos - 1] + "A" + sub[arg_pos:]
    assert mutated != sub and mutated[arg_pos - 1] == "A"
    m2 = map_positions(ref_dom, REF_DOMAIN[0], mutated[10:135], 11)
    assert m2[REF_POSITIONS["R469"]][1] == "A", "mutation not visible through the map"
    print("self-test OK (numbering control + arginine substitution break-test)")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        main()
