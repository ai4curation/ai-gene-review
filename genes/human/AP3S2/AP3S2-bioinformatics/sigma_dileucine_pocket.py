"""Does AP3S2 (sigma3B) retain the dileucine-signal pocket residues of sigma3A?

Background
----------
Acidic dileucine sorting signals, [DE]XXXL[LI], do not bind any single AP subunit.
They bind a composite site straddling the interface of the large subunit and the
small (sigma) subunit: gamma1-sigma1 in AP-1, alpha-sigma2 in AP-2, delta-sigma3
in AP-3 (PMID:14691137, PMID:21097499). Mattera et al. (PMID:21097499) located
that site by substitution: sigma2 V88D and L103S abolish signal binding, as do the
homologous sigma1A V88D / I103S and **sigma3A V94D / L109S**.

Every solved AP-3 structure to date is built on sigma3A (AP3S1) -- the 2024 cryo-EM
core (PMID:39705307) and the 2026 AP3:ARF1 coat (PMID:42139345, which states its
construct as "AP3S1(1-193) (H. sapiens)"). The functional question for AP3S2 is
therefore a paralogy question: does sigma3B carry the same pocket?

This script answers it from sequence, with no hardcoded result.

Method
------
1. Fetch the canonical sequences of the four human sigma subunits used in
   PMID:21097499's substitution series, plus the mouse AP3S2 ortholog that the
   human ISS/IEA rows name as donor, live from the UniProt REST API.
2. Assert the anchor residues actually are what PMID:21097499 says they are at
   those positions in their own records. If UniProt ever renumbers, this fails
   loudly rather than silently reporting the wrong residue.
3. Globally align AP3S2 to each comparator (Bio.Align.PairwiseAligner, BLOSUM62,
   affine gaps) and read out the AP3S2 position aligned to each anchor position.
4. Report the aligned residue, whether it is identical to the anchor, and the
   overall pairwise identity.

Output: sigma_dileucine_pocket.tsv
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
CACHE = HERE / "cache"
OUT = HERE / "sigma_dileucine_pocket.tsv"

TARGET = "P59780"  # human AP3S2, sigma3B

# Comparators. Anchor positions come from PMID:21097499 (Mattera et al. 2011),
# which reports loss of dileucine-signal binding for these substitutions.
COMPARATORS = [
    {
        "accession": "Q92572",
        "label": "AP3S1 / sigma3A (human)",
        "role": "direct paralog; the sigma subunit in every solved AP-3 structure",
        "anchors": [(94, "V", "sigma3A V94D abolishes dileucine-signal binding"),
                    (109, "L", "sigma3A L109S abolishes dileucine-signal binding")],
    },
    {
        "accession": "P53680",
        "label": "AP2S1 / sigma2 (human)",
        "role": "AP-2 small subunit; the site was first mapped here",
        "anchors": [(88, "V", "sigma2 V88D abolishes dileucine-signal binding"),
                    (103, "L", "sigma2 L103S abolishes dileucine-signal binding")],
    },
    {
        "accession": "P61966",
        "label": "AP1S1 / sigma1A (human)",
        "role": "AP-1 small subunit; homologous substitutions reported",
        "anchors": [(88, "V", "sigma1A V88D abolishes dileucine-signal binding"),
                    (103, "I", "sigma1A I103S abolishes dileucine-signal binding")],
    },
    {
        "accession": "Q8BSZ2",
        "label": "Ap3s2 / sigma3B (mouse)",
        "role": "the ISS/ISO donor named in the human AP3S2 GOA rows",
        "anchors": [(94, "V", "position homologous to sigma3A V94"),
                    (109, "L", "position homologous to sigma3A L109")],
    },
]


def fetch_entry(accession: str) -> dict:
    """Canonical sequence + sequence version, live from UniProt, cached on disk."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{accession}.json"
    if path.exists():
        return json.loads(path.read_text())
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    record = {
        "accession": data["primaryAccession"],
        "id": data["uniProtkbId"],
        "sequence": data["sequence"]["value"],
        "length": data["sequence"]["length"],
        "sequence_version": data["entryAudit"]["sequenceVersion"],
        "protein_name": data["proteinDescription"]["recommendedName"]["fullName"]["value"],
    }
    path.write_text(json.dumps(record, indent=1))
    return record


def aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "global"
    return al


def map_positions(anchor_seq: str, target_seq: str) -> tuple[dict[int, int | None], float]:
    """Map every 1-based anchor position to the aligned 1-based target position.

    Returns (mapping, percent identity over aligned columns).
    """
    alignment = aligner().align(anchor_seq, target_seq)[0]
    a_idx, t_idx = alignment.indices  # two rows of column -> sequence index (-1 = gap)
    mapping: dict[int, int | None] = {}
    identical = 0
    aligned_cols = 0
    for col in range(len(a_idx)):
        ai, ti = int(a_idx[col]), int(t_idx[col])
        if ai >= 0:
            mapping[ai + 1] = (ti + 1) if ti >= 0 else None
        if ai >= 0 and ti >= 0:
            aligned_cols += 1
            if anchor_seq[ai] == target_seq[ti]:
                identical += 1
    pct = 100.0 * identical / aligned_cols if aligned_cols else 0.0
    return mapping, pct


def main() -> int:
    target = fetch_entry(TARGET)
    print(f"target: {target['accession']} {target['id']} "
          f"({target['protein_name']}), {target['length']} aa, SV{target['sequence_version']}")

    rows: list[list[str]] = []
    failures: list[str] = []

    for comp in COMPARATORS:
        entry = fetch_entry(comp["accession"])
        mapping, pct = map_positions(entry["sequence"], target["sequence"])
        exact = entry["sequence"] == target["sequence"]
        print(f"\n{comp['label']} {entry['accession']} {entry['length']} aa "
              f"SV{entry['sequence_version']} -- identity to AP3S2 over aligned "
              f"columns: {pct:.1f}%"
              + ("  [sequences are byte-for-byte identical]" if exact else ""))

        for pos, expected, role in comp["anchors"]:
            if pos > entry["length"]:
                failures.append(
                    f"{entry['accession']} has only {entry['length']} residues; "
                    f"position {pos} does not exist")
                continue
            actual = entry["sequence"][pos - 1]
            if actual != expected:
                failures.append(
                    f"{entry['accession']} position {pos} is {actual}, not the "
                    f"{expected} reported in PMID:21097499 -- numbering has drifted")
                continue
            tpos = mapping.get(pos)
            tres = target["sequence"][tpos - 1] if tpos else None
            verdict = "RETAINED" if tres == expected else (
                "NO_ALIGNED_POSITION" if tres is None else "SUBSTITUTED")
            print(f"  {entry['accession']} {expected}{pos} -> AP3S2 "
                  f"{tres or '-'}{tpos or '-'}  [{verdict}]  ({role})")
            rows.append([
                comp["label"], entry["accession"], str(entry["sequence_version"]),
                f"{expected}{pos}", role,
                f"{tres or '-'}{tpos or '-'}", str(target["sequence_version"]),
                verdict, f"{pct:.1f}",
            ])

    # How far does the paralog difference reach around the pocket? Counted, not
    # eyeballed: every mismatching column between AP3S1 and AP3S2 in the window
    # spanned by the two anchors, padded by 15 residues either side.
    ap3s1 = fetch_entry("Q92572")
    mapping, _ = map_positions(ap3s1["sequence"], target["sequence"])
    lo, hi = 94 - 15, 109 + 15
    diffs = []
    for pos in range(lo, hi + 1):
        tpos = mapping.get(pos)
        a = ap3s1["sequence"][pos - 1]
        t = target["sequence"][tpos - 1] if tpos else "-"
        if a != t:
            diffs.append(f"{a}{pos}->{t}{tpos or '-'}")
    print(f"\nAP3S1 vs AP3S2 over the pocket window {lo}-{hi} "
          f"({hi - lo + 1} positions): {len(diffs)} difference(s)"
          + (f": {', '.join(diffs)}" if diffs else ""))
    whole = sum(1 for i, a in enumerate(ap3s1["sequence"])
                if i < len(target["sequence"]) and a != target["sequence"][i])
    print(f"AP3S1 vs AP3S2 over the full 1-{min(len(ap3s1['sequence']), len(target['sequence']))} "
          f"ungapped comparison: {whole} difference(s)")

    with OUT.open("w") as fh:
        fh.write("\t".join([
            "comparator", "comparator_accession", "comparator_sequence_version",
            "anchor", "anchor_role", "ap3s2_position", "ap3s2_sequence_version",
            "verdict", "pct_identity_to_ap3s2",
        ]) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print(f"\nwrote {OUT.name} ({len(rows)} rows)")

    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
