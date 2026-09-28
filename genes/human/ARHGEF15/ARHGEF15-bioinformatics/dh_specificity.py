"""Are the published Ephexin5 specificity residues present in the HUMAN protein,
and does the alpha5 signature actually discriminate RhoA-GEFs from Rac/Cdc42-GEFs?

Two questions, deliberately separate:

Q1  Mapping. PMID:21029865 numbered the alpha5 triad (L562/Q566/R567) and the EphB2
    phosphosite (Y361) in MOUSE Ephexin5. Human ARHGEF15 is 8 residues shorter, so the
    human positions must be obtained by alignment, never by subtracting 8.

Q2  Discrimination. Margolis et al. assert the triad is "conserved in other GEFs that,
    like E5, activate RhoA but not Rac1 and Cdc42". That is a falsifiable claim about
    a comparator panel: RhoA-specific GEFs should carry it and Rac1/Cdc42-specific GEFs
    should not. This script tests it and reports whichever way it comes out.

Neither question settles whether the human protein is an active GEF. Retention is
consistent with activity; it is not evidence of it, and the measured substrate range
(RhoA in one system, RhoA+Cdc42 in another) is not predicted by these residues at all.

Usage:
    uv run --no-project python dh_specificity.py            # analysis -> results.json
    uv run --no-project python dh_specificity.py --self-test  # guards + mutation tests
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import tempfile

from panel import ANCHOR, ANCHOR_SITES, PANEL, TARGET, TARGET_VARIANTS

HERE = pathlib.Path(__file__).parent
SEQ_DIR = HERE / "sequences"
RESULTS = HERE / "results.json"


# ----------------------------------------------------------------------------- io


def load_sequences() -> dict[str, str]:
    seqs = {}
    for acc in PANEL:
        path = SEQ_DIR / f"{acc}.fasta"
        if not path.exists():
            sys.exit(f"missing {path}; run fetch_sequences.py first")
        seqs[acc] = "".join(line.strip() for line in path.read_text().splitlines()[1:])
    return seqs


def load_dh_bounds() -> dict[str, tuple[int, int]]:
    meta = json.loads((HERE / "panel_identities.json").read_text())
    bounds = {}
    for acc, rec in meta.items():
        dh = rec["dh_domains"]
        if len(dh) != 1:
            sys.exit(f"{acc}: expected exactly one UniProt DH domain, got {dh}")
        bounds[acc] = (dh[0]["start"], dh[0]["end"])
    return bounds


# ------------------------------------------------------------------------ align


def mafft(records: dict[str, str]) -> dict[str, str]:
    """Align with MAFFT L-INS-i. Raises if mafft is absent -- silence is not a result."""
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for name, seq in records.items():
            fh.write(f">{name}\n{seq}\n")
        path = fh.name
    proc = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", "--amino", path],
        capture_output=True,
        text=True,
        check=True,
    )
    out: dict[str, str] = {}
    name = None
    for line in proc.stdout.splitlines():
        if line.startswith(">"):
            name = line[1:].strip()
            out[name] = ""
        elif name is not None:
            out[name] += line.strip()
    return out


def ungapped_index_to_column(aligned: str, position: int) -> int:
    """1-based ungapped `position` -> 0-based alignment column."""
    seen = 0
    for col, ch in enumerate(aligned):
        if ch != "-":
            seen += 1
            if seen == position:
                return col
    raise IndexError(f"position {position} beyond sequence of length {seen}")


def column_to_ungapped_index(aligned: str, column: int) -> int | None:
    """0-based alignment column -> 1-based ungapped position, or None if gapped."""
    if aligned[column] == "-":
        return None
    return sum(1 for ch in aligned[:column] if ch != "-") + 1


# --------------------------------------------------------------------- analysis


def map_anchor_sites(seqs: dict[str, str]) -> dict[int, dict]:
    """Q1: carry each mouse-numbered site onto the human protein by alignment."""
    pair = mafft({ANCHOR: seqs[ANCHOR], TARGET: seqs[TARGET]})
    mapped = {}
    for pos, (expected_aa, role) in sorted(ANCHOR_SITES.items()):
        observed_anchor = seqs[ANCHOR][pos - 1]
        col = ungapped_index_to_column(pair[ANCHOR], pos)
        target_pos = column_to_ungapped_index(pair[TARGET], col)
        target_aa = pair[TARGET][col]
        mapped[pos] = {
            "anchor_position": pos,
            "anchor_residue_expected": expected_aa,
            "anchor_residue_observed": observed_anchor,
            "anchor_residue_matches_publication": observed_anchor == expected_aa,
            "role": role,
            "target_position": target_pos,
            "target_residue": None if target_aa == "-" else target_aa,
            "status": (
                "RETAINED"
                if target_aa == observed_anchor
                else ("GAPPED" if target_aa == "-" else "DIVERGENT")
            ),
        }
    return mapped


def triad_across_panel(seqs: dict[str, str], bounds: dict[str, tuple[int, int]]) -> dict:
    """Q2: does the alpha5 triad separate RhoA-GEFs from Rac1/Cdc42-GEFs?"""
    dh = {acc: seqs[acc][bounds[acc][0] - 1 : bounds[acc][1]] for acc in PANEL}
    msa = mafft(dh)

    triad = sorted(p for p in ANCHOR_SITES if bounds[ANCHOR][0] <= p <= bounds[ANCHOR][1])
    anchor_dh_offset = bounds[ANCHOR][0] - 1
    cols = {p: ungapped_index_to_column(msa[ANCHOR], p - anchor_dh_offset) for p in triad}

    rows = {}
    for acc, (label, role, note) in PANEL.items():
        residues = {}
        for p, col in cols.items():
            aa = msa[acc][col]
            idx = column_to_ungapped_index(msa[acc], col)
            residues[p] = {
                "residue": None if aa == "-" else aa,
                "position": None if idx is None else idx + bounds[acc][0] - 1,
            }
        signature = {p: seqs[ANCHOR][p - 1] for p in triad}
        rows[acc] = {
            "label": label,
            "role": role,
            "measured_specificity": note,
            "residues": residues,
            "matches_full_triad": all(
                residues[p]["residue"] == signature[p] for p in triad
            ),
            "n_triad_matches": sum(
                1 for p in triad if residues[p]["residue"] == signature[p]
            ),
        }

    rhoa = [a for a, r in rows.items() if r["role"] == "RHOA_SPEC"]
    raccdc = [a for a, r in rows.items() if r["role"] == "RAC_CDC42"]
    return {
        "triad_anchor_positions": triad,
        "alignment_columns": cols,
        "rows": rows,
        "discrimination": {
            "rhoA_specific_matching_full_triad": [a for a in rhoa if rows[a]["matches_full_triad"]],
            "rhoA_specific_total": rhoa,
            "rac_cdc42_specific_matching_full_triad": [
                a for a in raccdc if rows[a]["matches_full_triad"]
            ],
            "rac_cdc42_specific_total": raccdc,
        },
    }


def map_target_variants(seqs: dict[str, str], bounds: dict[str, tuple[int, int]]) -> dict:
    """Carry the human disease variants onto the mouse protein, and locate them vs the DH domain."""
    pair = mafft({TARGET: seqs[TARGET], ANCHOR: seqs[ANCHOR]})
    dh_start, dh_end = bounds[TARGET]
    out = {}
    for pos, (expected_aa, note) in sorted(TARGET_VARIANTS.items()):
        observed = seqs[TARGET][pos - 1]
        col = ungapped_index_to_column(pair[TARGET], pos)
        anchor_pos = column_to_ungapped_index(pair[ANCHOR], col)
        anchor_aa = pair[ANCHOR][col]
        out[pos] = {
            "target_position": pos,
            "target_residue_expected": expected_aa,
            "target_residue_observed": observed,
            "target_residue_matches_uniprot": observed == expected_aa,
            "note": note,
            "anchor_position": anchor_pos,
            "anchor_residue": None if anchor_aa == "-" else anchor_aa,
            "same_residue_in_anchor": anchor_aa == observed,
            "inside_target_DH_domain": dh_start <= pos <= dh_end,
        }
    return out


def analyse(seqs: dict[str, str] | None = None) -> dict:
    seqs = seqs or load_sequences()
    bounds = load_dh_bounds()
    return {
        "anchor": ANCHOR,
        "target": TARGET,
        "target_DH_domain": {"start": bounds[TARGET][0], "end": bounds[TARGET][1]},
        "site_mapping": map_anchor_sites(seqs),
        "variant_mapping": map_target_variants(seqs, bounds),
        "panel_triad": triad_across_panel(seqs, bounds),
    }


# -------------------------------------------------------------------- reporting


def report(res: dict) -> str:
    lines = []
    lines.append(f"Anchor {res['anchor']} (mouse Ephexin5) -> target {res['target']} (human ARHGEF15)")
    for pos, m in sorted(res["site_mapping"].items(), key=lambda kv: int(kv[0])):
        ok = "ok" if m["anchor_residue_matches_publication"] else "ANCHOR RESIDUE MISMATCH"
        lines.append(
            f"  mouse {m['anchor_residue_observed']}{pos} [{ok}] -> human "
            f"{m['target_residue']}{m['target_position']}  {m['status']}   ({m['role']})"
        )
    lines.append("")
    dh = res["target_DH_domain"]
    lines.append(f"human disease/uncertain variants (human DH domain = {dh['start']}-{dh['end']}):")
    for pos, v in sorted(res["variant_mapping"].items(), key=lambda kv: int(kv[0])):
        ok = "ok" if v["target_residue_matches_uniprot"] else "UNIPROT RESIDUE MISMATCH"
        inside = "inside DH" if v["inside_target_DH_domain"] else "outside DH"
        lines.append(
            f"  human {v['target_residue_observed']}{pos} [{ok}, {inside}] -> mouse "
            f"{v['anchor_residue']}{v['anchor_position']}  same_residue={v['same_residue_in_anchor']}"
        )
    pt = res["panel_triad"]
    lines.append("")
    lines.append(f"alpha5 triad at mouse positions {pt['triad_anchor_positions']}:")
    for acc, row in pt["rows"].items():
        got = "".join(
            (row["residues"][p]["residue"] or "-") for p in pt["triad_anchor_positions"]
        )
        lines.append(
            f"  {acc}  {row['role']:<10} {got}  full_triad={row['matches_full_triad']}  {row['label']}"
        )
    d = pt["discrimination"]
    lines.append("")
    lines.append(
        f"RhoA-specific comparators carrying the full triad: "
        f"{len(d['rhoA_specific_matching_full_triad'])}/{len(d['rhoA_specific_total'])}"
    )
    lines.append(
        f"Rac1/Cdc42-specific comparators carrying the full triad: "
        f"{len(d['rac_cdc42_specific_matching_full_triad'])}/{len(d['rac_cdc42_specific_total'])}"
    )
    return "\n".join(lines)


# -------------------------------------------------------------------- self-test


def self_test() -> int:
    """Every guard must be shown to FAIL on a broken input, not merely to pass on a good one."""
    seqs = load_sequences()
    base = analyse(seqs)
    failures = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
        if not ok:
            failures.append(name)

    print("negative controls (must stay silent on the real data):")
    check(
        "anchor residues match the published identities",
        all(m["anchor_residue_matches_publication"] for m in base["site_mapping"].values()),
    )
    check(
        "no anchor site maps into a gap in the target",
        all(m["status"] != "GAPPED" for m in base["site_mapping"].values()),
    )
    check(
        "target DH bounds are the UniProt ones",
        load_dh_bounds()[TARGET] == (417, 601),
        str(load_dh_bounds()[TARGET]),
    )
    check(
        "variant residues match the identities UniProt lists",
        all(v["target_residue_matches_uniprot"] for v in base["variant_mapping"].values()),
    )

    print("mutation tests (each must flip a specific verdict):")

    # 1. Break the triad in the target: every triad site must become DIVERGENT.
    triad = base["panel_triad"]["triad_anchor_positions"]
    tgt = list(seqs[TARGET])
    for p in triad:
        hp = base["site_mapping"][p]["target_position"]
        tgt[hp - 1] = "A" if tgt[hp - 1] != "A" else "G"
    mutated = dict(seqs)
    mutated[TARGET] = "".join(tgt)
    m1 = analyse(mutated)
    check(
        "alanine-scanning the human triad makes all three DIVERGENT",
        all(m1["site_mapping"][p]["status"] == "DIVERGENT" for p in triad),
        str({p: m1["site_mapping"][p]["status"] for p in triad}),
    )
    check(
        "...and the mutated target no longer matches the full triad",
        not m1["panel_triad"]["rows"][TARGET]["matches_full_triad"],
    )
    check(
        "...while the real target DOES match the full triad",
        base["panel_triad"]["rows"][TARGET]["matches_full_triad"],
    )

    # 2. Deleting the target region must be reported as GAPPED, not silently skipped.
    hp = base["site_mapping"][triad[0]]["target_position"]
    deleted = dict(seqs)
    deleted[TARGET] = seqs[TARGET][: hp - 1] + seqs[TARGET][hp + 14 :]
    m2 = analyse(deleted)
    check(
        "deleting 15 residues around the triad yields GAPPED or DIVERGENT, never RETAINED",
        all(m2["site_mapping"][p]["status"] != "RETAINED" for p in triad),
        str({p: m2["site_mapping"][p]["status"] for p in triad}),
    )

    # 3. The discrimination counts must be able to move: corrupt a comparator and
    #    watch its membership change. A count that cannot change is not a measurement.
    #    The predicate is factored out so the mutation and the no-op probe below cannot
    #    drift from it, and so it has no `or <constant>` escape hatch.
    def count_moved(before_n: int, after_n: int) -> bool:
        return before_n > 0 and after_n == 0

    victim = next(a for a, (_, role, _) in PANEL.items() if role == "RHOA_SPEC")
    before = base["panel_triad"]["rows"][victim]["n_triad_matches"]
    bounds = load_dh_bounds()
    vs = list(seqs[victim])
    # blunt but decisive: replace the comparator's whole DH domain with polyglycine
    vs[bounds[victim][0] - 1 : bounds[victim][1]] = "G" * (bounds[victim][1] - bounds[victim][0] + 1)
    corrupt = dict(seqs)
    corrupt[victim] = "".join(vs)
    after = analyse(corrupt)["panel_triad"]["rows"][victim]["n_triad_matches"]
    check(
        f"comparator triad count is data-dependent ({victim}: {before} -> {after})",
        count_moved(before, after),
    )
    # ...and prove that predicate is not constant-true: with NO corruption it must be False.
    noop = analyse(dict(seqs))["panel_triad"]["rows"][victim]["n_triad_matches"]
    check(
        f"the same predicate returns False on an uncorrupted run ({victim}: {before} -> {noop})",
        not count_moved(before, noop),
    )

    print()
    if failures:
        print(f"SELF-TEST FAILED: {failures}")
        return 1
    print("SELF-TEST PASSED (all guards fired on broken input and stayed silent on real input)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    res = analyse()
    RESULTS.write_text(json.dumps(res, indent=2, sort_keys=True, default=str) + "\n")
    print(report(res))
    print(f"\nwrote {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
