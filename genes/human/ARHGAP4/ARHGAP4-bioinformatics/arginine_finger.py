#!/usr/bin/env python3
"""Does ARHGAP4 retain the RHOGAP catalytic arginine finger, and does that settle
anything about its activity?

Two questions, deliberately kept apart because the answer to the first does not
imply an answer to the second.

**Q1 -- residue.** Is the position that corresponds to the structurally resolved
arginine finger of p50RhoGAP/ARHGAP1 an arginine in ARHGAP4?  Answered by an
alignment we compute here, *not* by reading UniProt's ``SITE`` feature.  UniProt's
site is a PROSITE-ProRule projection (``ECO:0000255``), so quoting it back would be
circular; instead it is used as an **independent second opinion** that the
alignment must reproduce.

The anchor is ARHGAP1 Arg-282 (UniProt ``Q07960`` numbering).  PDB **1TX4** is the
RHOA-GDP-AlF4(-)-p50RhoGAP transition-state complex; SIFTS maps its chain A
residues 1-198 onto ``Q07960`` 234-431, so Arg-282 is residue 49 of the deposited
model.  The script downloads 1TX4 and verifies that (a) residue 49 of chain A is
ARG and (b) its guanidinium nitrogens reach the AlF4(-) moiety -- i.e. the anchor
really is the catalytic arginine inserted into the active site, not merely a
conserved arginine.

**Q2 -- does the residue predict activity?**  Tested empirically rather than
assumed, by asking GOA whether ``GO:0005096 GTPase activator activity`` is
annotated to the RHOGAP-domain proteins that Amin et al. 2016 (PMID:27481945)
identified as *lacking* the arginine finger, and to ARHGAP11B, which retains it.
If curated activity appears on both sides of the residue split, then residue
identity is not a proxy for activity in this family and a "retains the arginine
finger" statement carries no weight on its own.

Controls are mandatory, not decorative:

* positive, structurally resolved -- ARHGAP1 (`Q07960`, PDB 1TX4);
* further positives -- ARHGAP35/p190A, STARD13/DLC2, ARHGAP21, ARHGAP11A;
* known-dead -- ARHGAP36, DEPDC1B, OCRL1, INPP5B, the four members of Amin's
  arginine-finger-less list whose Rho-GAP domain UniProt delimits;
* retains-the-residue-but-curated-inactive -- ARHGAP11B (`Q3KRB8`), which GOA
  carries as ``NOT|enables GO:0005096``.

The run aborts if a positive control does not come out as R or a known-dead
control does, because either means the alignment anchor moved and every other row
is then meaningless.

Run:    uv run --with biopython --with requests python arginine_finger.py
        uv run --with biopython --with requests python arginine_finger.py --self-test
Writes: arginine_finger.json
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
RCSB_CIF = "https://files.rcsb.org/download/{pdb}.cif"

# The anchor.  ARHGAP1 == p50RhoGAP; Arg-282 in UniProt numbering is the arginine
# finger resolved in the 1TX4 transition-state complex.
ANCHOR_ACC = "Q07960"
ANCHOR_POS = 282
ANCHOR_PDB = "1TX4"
ANCHOR_PDB_CHAIN = "A"
# SIFTS: 1TX4 chain A residues 1-198 == Q07960 234-431.  Asserted, not assumed.
ANCHOR_PDB_UNP_START = 234
ANCHOR_PDB_LABEL_START = 1

# expectation: "R" (arginine finger present) | "X" (absent) | None (the question)
PANEL: dict[str, dict[str, object]] = {
    "Q07960": {
        "symbol": "ARHGAP1/p50",
        "role": "positive control, structure 1TX4",
        "expect": "R",
    },
    "P98171": {"symbol": "ARHGAP4", "role": "TARGET", "expect": None},
    "Q9NRY4": {"symbol": "ARHGAP35/p190A", "role": "positive control", "expect": "R"},
    "Q9Y3M8": {"symbol": "STARD13/DLC2", "role": "positive control", "expect": "R"},
    "Q5T5U3": {"symbol": "ARHGAP21", "role": "positive control", "expect": "R"},
    "Q6P4F7": {"symbol": "ARHGAP11A", "role": "positive control", "expect": "R"},
    "Q3KRB8": {
        "symbol": "ARHGAP11B",
        "role": "retains residue, curated NOT|enables GO:0005096",
        "expect": "R",
    },
    "Q6ZRI8": {
        "symbol": "ARHGAP36",
        "role": "known-dead (Amin 2016: lacks arginine finger)",
        "expect": "X",
    },
    "Q8WUY9": {
        "symbol": "DEPDC1B",
        "role": "known-dead (Amin 2016: lacks arginine finger)",
        "expect": "X",
    },
    "Q01968": {
        "symbol": "OCRL1",
        "role": "known-dead (Amin 2016: lacks arginine finger)",
        "expect": "X",
    },
    "P32019": {
        "symbol": "INPP5B",
        "role": "known-dead (Amin 2016: lacks arginine finger)",
        "expect": "X",
    },
}

# Amin et al. 2016 (PMID:27481945) Table 1 / "Not all RHOGAP Domain-containing
# Proteins Are GAPs": these seven were reported to carry serine, threonine or
# glutamine where the arginine finger belongs.  Queried against GOA in Q2.
AMIN_NO_ARGININE_FINGER = {
    "Q6ZRI8": "ARHGAP36",
    "Q8WZ64": "ARAP2 (CNT-D1)",
    "Q5TB30": "DEPDC1 (DEP1)",
    "Q8WUY9": "DEPDC1B (DEP2)",
    "Q9NYF5": "FAM13B",
    "P32019": "INPP5B",
    "Q01968": "OCRL1",
}
# Retains the arginine finger; included in Q2 as the mirror-image case.
RETAINS_BUT_QUESTIONED = {"Q3KRB8": "ARHGAP11B", "P98171": "ARHGAP4 (target)"}


def fetch_uniprot(acc: str) -> dict:
    r = requests.get(UNIPROT.format(acc=acc), timeout=90)
    r.raise_for_status()
    return r.json()


def rho_gap_domain(entry: dict) -> tuple[int, int]:
    """UniProt's own Rho-GAP domain boundaries. Aligning whole chains of very
    different length (946 vs 439 aa) invites a spurious local optimum; aligning
    the delimited domains does not."""
    doms = [
        (f["location"]["start"]["value"], f["location"]["end"]["value"])
        for f in entry.get("features", [])
        if f["type"] == "Domain" and "Rho-GAP" in f.get("description", "")
    ]
    if len(doms) != 1:
        raise RuntimeError(
            f"expected exactly one Rho-GAP domain, found {len(doms)}: {doms}"
        )
    return doms[0]


def prorule_site(entry: dict) -> tuple[int | None, str | None]:
    """UniProt's ProRule-projected 'Arginine finger' SITE, used only as a second
    opinion to compare against our alignment."""
    for f in entry.get("features", []):
        if f["type"] == "Site" and "rginine finger" in f.get("description", ""):
            pos = f["location"]["start"]["value"]
            return pos, entry["sequence"]["value"][pos - 1]
    return None, None


def make_aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    return a


def project(
    aligner: Align.PairwiseAligner,
    ref_seq: str,
    ref_offset: int,
    ref_target_pos: int,
    qry_seq: str,
    qry_offset: int,
) -> tuple[int | None, str]:
    """Align qry domain to ref domain; return the query's full-length position and
    residue aligned to ``ref_target_pos`` (full-length ref numbering).

    Returns ``(None, '-')`` when the anchor column is a gap in the query, which is
    a real answer (the residue is absent), not a failure."""
    aln = aligner.align(ref_seq, qry_seq)[0]
    ref_idx = ref_target_pos - ref_offset  # 0-based index into ref_seq
    if not 0 <= ref_idx < len(ref_seq):
        raise RuntimeError("anchor lies outside the reference domain slice")
    # aln.indices is a 2 x alignment-length array of 0-based sequence indices,
    # -1 for gaps.  Find the column holding ref_idx, then read the query there.
    indices = aln.indices
    cols = [c for c in range(indices.shape[1]) if indices[0][c] == ref_idx]
    if len(cols) != 1:
        raise RuntimeError(f"anchor maps to {len(cols)} alignment columns")
    q_idx = indices[1][cols[0]]
    if q_idx < 0:
        return None, "-"
    return qry_offset + int(q_idx), qry_seq[q_idx]


def verify_anchor_structure() -> dict[str, object]:
    """Confirm the anchor is the catalytic arginine in 1TX4: right residue, and
    close enough to AlF4(-) to be the transition-state-stabilising one."""
    r = requests.get(RCSB_CIF.format(pdb=ANCHOR_PDB), timeout=120)
    r.raise_for_status()
    label_seq = ANCHOR_PDB_LABEL_START + (ANCHOR_POS - ANCHOR_PDB_UNP_START)

    arg_atoms: list[tuple[str, float, float, float]] = []
    alf_atoms: list[tuple[str, float, float, float]] = []
    resname = None
    for line in r.text.splitlines():
        if not line.startswith("ATOM") and not line.startswith("HETATM"):
            continue
        f = line.split()
        # mmCIF atom_site column order is fixed in RCSB-distributed files.
        atom, comp, chain, seq_id = f[3], f[5], f[6], f[8]
        x, y, z = float(f[10]), float(f[11]), float(f[12])
        if chain == ANCHOR_PDB_CHAIN and seq_id == str(label_seq):
            resname = comp
            arg_atoms.append((atom, x, y, z))
        if comp in ("ALF", "AF3"):
            alf_atoms.append((atom, x, y, z))

    if not arg_atoms:
        raise RuntimeError(
            f"{ANCHOR_PDB} chain {ANCHOR_PDB_CHAIN} has no residue {label_seq}; "
            "the SIFTS offset assumed here is wrong"
        )
    if not alf_atoms:
        raise RuntimeError(f"{ANCHOR_PDB} contains no AlF4(-)/AlF3 moiety")

    guanidinium = [a for a in arg_atoms if a[0] in ("NH1", "NH2", "NE")]
    dmin = min(
        math.dist((a[1], a[2], a[3]), (b[1], b[2], b[3]))
        for a in guanidinium
        for b in alf_atoms
    )
    return {
        "pdb": ANCHOR_PDB,
        "chain": ANCHOR_PDB_CHAIN,
        "label_seq_id": label_seq,
        "residue_name": resname,
        "min_guanidinium_to_AlF_distance_angstrom": round(dmin, 2),
        "contacts_transition_state": bool(resname == "ARG" and dmin < 5.0),
    }


def query_go_activator(acc: str) -> dict[str, object]:
    r = requests.get(
        QUICKGO,
        params={
            "geneProductId": f"UniProtKB:{acc}",
            "goId": "GO:0005096",
            "limit": 100,
        },
        headers={"Accept": "application/json"},
        timeout=90,
    )
    r.raise_for_status()
    d = r.json()
    rows = d.get("results") or []
    if d.get("numberOfHits") is not None and d["numberOfHits"] > len(rows):
        raise RuntimeError(f"paginated GO:0005096 result for {acc}; widen the page")
    return {
        "n": d.get("numberOfHits"),
        "rows": [
            {
                "qualifier": x.get("qualifier"),
                "evidence": x.get("goEvidence"),
                "reference": x.get("reference"),
            }
            for x in rows
        ],
        "has_positive": any(
            not (x.get("qualifier") or "").startswith("NOT") for x in rows
        ),
        "has_negated": any((x.get("qualifier") or "").startswith("NOT") for x in rows),
    }


def run() -> dict[str, object]:
    aligner = make_aligner()
    entries = {acc: fetch_uniprot(acc) for acc in PANEL}

    ref = entries[ANCHOR_ACC]
    ref_start, ref_end = rho_gap_domain(ref)
    ref_full = ref["sequence"]["value"]
    if not ref_start <= ANCHOR_POS <= ref_end:
        raise RuntimeError("anchor is outside ARHGAP1's own Rho-GAP domain")
    if ref_full[ANCHOR_POS - 1] != "R":
        raise RuntimeError(
            f"{ANCHOR_ACC} position {ANCHOR_POS} is "
            f"{ref_full[ANCHOR_POS - 1]}, not R -- the sequence changed"
        )
    ref_seq = ref_full[ref_start - 1 : ref_end]

    rows: dict[str, dict[str, object]] = {}
    for acc, meta in PANEL.items():
        e = entries[acc]
        q_start, q_end = rho_gap_domain(e)
        q_full = e["sequence"]["value"]
        pos, res = project(
            aligner, ref_seq, ref_start, ANCHOR_POS, q_full[q_start - 1 : q_end], q_start
        )
        site_pos, site_res = prorule_site(e)
        rows[acc] = {
            **meta,
            "length": len(q_full),
            "rho_gap_domain": [q_start, q_end],
            "aligned_position": pos,
            "aligned_residue": res,
            "is_arginine": res == "R",
            "uniprot_prorule_site_position": site_pos,
            "uniprot_prorule_site_residue": site_res,
            "agrees_with_prorule": (pos == site_pos) if site_pos else None,
        }

    # Controls.  A control that fails is not a finding about the protein; it means
    # the anchor moved and nothing in this table can be believed.
    failures = [
        f"{r['symbol']} ({acc}): expected {r['expect']}, aligned residue {r['aligned_residue']}"
        for acc, r in rows.items()
        if r["expect"] == "R"
        and not r["is_arginine"]
        or r["expect"] == "X"
        and r["is_arginine"]
    ]
    if failures:
        raise RuntimeError("control failure; alignment anchor is wrong:\n  " + "\n  ".join(failures))

    disagreements = [
        acc for acc, r in rows.items() if r["agrees_with_prorule"] is False
    ]

    go_rows = {
        acc: {"symbol": sym, "arginine_finger": "absent", **query_go_activator(acc)}
        for acc, sym in AMIN_NO_ARGININE_FINGER.items()
    }
    go_rows.update(
        {
            acc: {"symbol": sym, "arginine_finger": "present", **query_go_activator(acc)}
            for acc, sym in RETAINS_BUT_QUESTIONED.items()
        }
    )

    activity_without_residue = sorted(
        go_rows[a]["symbol"] for a in AMIN_NO_ARGININE_FINGER if go_rows[a]["has_positive"]
    )
    residue_without_activity = sorted(
        go_rows[a]["symbol"] for a in RETAINS_BUT_QUESTIONED if go_rows[a]["has_negated"]
    )

    return {
        "anchor": {
            "accession": ANCHOR_ACC,
            "symbol": "ARHGAP1/p50RhoGAP",
            "uniprot_position": ANCHOR_POS,
            "structure": verify_anchor_structure(),
        },
        "panel": rows,
        "prorule_disagreements": disagreements,
        "target": {
            "accession": "P98171",
            "aligned_position": rows["P98171"]["aligned_position"],
            "aligned_residue": rows["P98171"]["aligned_residue"],
            "arginine_finger_present": rows["P98171"]["is_arginine"],
        },
        "go_activator_annotations": go_rows,
        "decoupling": {
            "curated_GAP_activity_without_arginine_finger": activity_without_residue,
            "arginine_finger_without_curated_GAP_activity": residue_without_activity,
            "decoupled_in_both_directions": bool(
                activity_without_residue and residue_without_activity
            ),
        },
    }


def self_test() -> int:
    """Break the anchor on purpose and require each guard to fire; then require the
    negative control to stay silent."""
    global ANCHOR_POS, ANCHOR_PDB_UNP_START
    checks: list[tuple[str, str]] = []

    aligner = make_aligner()
    ref = fetch_uniprot(ANCHOR_ACC)
    ref_start, ref_end = rho_gap_domain(ref)
    ref_seq = ref["sequence"]["value"][ref_start - 1 : ref_end]
    tgt = fetch_uniprot("P98171")
    t_start, t_end = rho_gap_domain(tgt)
    t_seq = tgt["sequence"]["value"][t_start - 1 : t_end]

    # 1. A displaced anchor must stop being an arginine in the target. If shifting
    #    the anchor left the answer unchanged, the alignment would be reading
    #    something other than the column we think it is.
    _, res_true = project(aligner, ref_seq, ref_start, ANCHOR_POS, t_seq, t_start)
    shifted = [
        project(aligner, ref_seq, ref_start, ANCHOR_POS + d, t_seq, t_start)[1]
        for d in (-3, -2, -1, 1, 2, 3)
    ]
    checks.append(
        (
            "anchor is position-specific",
            "PASS" if res_true == "R" and shifted.count("R") <= 1 else f"FAIL {shifted}",
        )
    )

    # 2. An out-of-domain anchor must raise rather than silently return something.
    try:
        project(aligner, ref_seq, ref_start, ref_end + 50, t_seq, t_start)
        checks.append(("out-of-range anchor raises", "FAIL (no exception)"))
    except RuntimeError:
        checks.append(("out-of-range anchor raises", "PASS"))

    # 3. A wrong SIFTS offset must be caught by the structural check, not absorbed.
    saved = ANCHOR_PDB_UNP_START
    ANCHOR_PDB_UNP_START = saved + 400
    try:
        verify_anchor_structure()
        checks.append(("bad SIFTS offset raises", "FAIL (no exception)"))
    except RuntimeError:
        checks.append(("bad SIFTS offset raises", "PASS"))
    finally:
        ANCHOR_PDB_UNP_START = saved

    # 4. NEGATIVE CONTROL: the real offset must stay silent and confirm ARG.
    s = verify_anchor_structure()
    checks.append(
        (
            "true offset resolves to ARG contacting AlF4-",
            "PASS" if s["residue_name"] == "ARG" and s["contacts_transition_state"] else f"FAIL {s}",
        )
    )

    # 5. Mandatory-control machinery: flipping an expectation must abort the run.
    saved_expect = PANEL["Q01968"]["expect"]
    PANEL["Q01968"]["expect"] = "R"  # claim a known-dead protein has the arginine
    try:
        run()
        checks.append(("control failure aborts run", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(
            (
                "control failure aborts run",
                "PASS" if "control failure" in str(e) else f"FAIL wrong error: {e}",
            )
        )
    finally:
        PANEL["Q01968"]["expect"] = saved_expect

    for name, verdict in checks:
        print(f"  [{verdict.split()[0]}] {name}" + ("" if verdict.startswith("PASS") else f" -- {verdict}"))
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("arginine_finger.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    a = out["anchor"]["structure"]
    print(
        f"anchor: ARHGAP1 Arg-{ANCHOR_POS} == {ANCHOR_PDB} chain {a['chain']} "
        f"residue {a['label_seq_id']} ({a['residue_name']}), "
        f"{a['min_guanidinium_to_AlF_distance_angstrom']} A from AlF4(-)\n"
    )
    print(f"{'symbol':<18} {'role':<48} {'pos':>6} {'res':>4} {'ProRule':>8}")
    for acc, r in out["panel"].items():
        agree = {True: "agree", False: "DIFFER", None: "-"}[r["agrees_with_prorule"]]
        print(
            f"{r['symbol']:<18} {r['role']:<48} {str(r['aligned_position']):>6} "
            f"{r['aligned_residue']:>4} {agree:>8}"
        )
    print()
    print("GO:0005096 vs arginine finger")
    for acc, g in out["go_activator_annotations"].items():
        q = ",".join(
            f"{x['qualifier']}/{x['evidence']}" for x in g["rows"]
        ) or "-"
        print(f"  {g['symbol']:<20} finger={g['arginine_finger']:<8} n={g['n']:<3} {q}")
    d = out["decoupling"]
    print()
    print("  curated GAP activity WITHOUT arginine finger:", d["curated_GAP_activity_without_arginine_finger"] or "none")
    print("  arginine finger WITHOUT curated GAP activity:", d["arginine_finger_without_curated_GAP_activity"] or "none")
    print("  decoupled in both directions:", d["decoupled_in_both_directions"])
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
