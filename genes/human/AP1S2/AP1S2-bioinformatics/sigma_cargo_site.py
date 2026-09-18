"""Map the experimentally defined AP-complex dileucine-signal binding residues onto AP1S2 (sigma1B).

Mattera et al. 2011 (PMID:21097499) located the (D/E)XXXL(L/I) sorting-signal binding site on
the AP-1 gamma/sigma1, AP-2 alpha/sigma2 and AP-3 delta/sigma3 hemicomplexes by mutating
sigma-side residues and assaying signal binding. The positions it names in its text are:

    sigma2 (AP2S1): R15, A63, V88, N92, E100, L101, L103
    sigma1A (AP1S1): R15, A63, V88, L101, I103
    sigma3A (AP3S1): R15, V94, D98, L107, L109

These are the positions tested, not a set of positions all required for binding: the effect of
a substitution is frequently signal-dependent, and several of these are exceptions for one
signal while still reducing binding of another. The three sigma1A substitutions the paper
reports as abolishing the gamma1-sigma1A interaction outright are V88D and I103S (for the Nef
signal) "and also by A63D (for tyrosinase)"; the remaining sigma1A positions tested are weaker
or signal-dependent.

The paper assayed gamma1-sigma1B hemicomplexes functionally but did not report the sigma1B
residue numbers. This script fetches the sequences live, aligns sigma1B (AP1S2) to each
comparator, and reports which residue AP1S2 carries at the position corresponding to each
tested site, in AP1S2's own numbering.

No result is hardcoded. Every sequence, length and sequence version is read from the live
UniProt record and asserted against the record's own metadata.
"""

from __future__ import annotations

import csv
import json
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT_JSON = "https://rest.uniprot.org/uniprotkb/{acc}.json"

# accession -> short label used in the report
PROTEINS = {
    "P56377": "sigma1B / AP1S2 (human, target)",
    "P61966": "sigma1A / AP1S1 (human)",
    "Q96PC3": "sigma1C / AP1S3 (human)",
    "P53680": "sigma2 / AP2S1 (human)",
    "Q92572": "sigma3A / AP3S1 (human)",
    "Q9DB50": "sigma1B / Ap1s2 (mouse)",
}

# Sites tested in PMID:21097499, keyed by the comparator accession.
# (position in the comparator's own numbering, expected residue, role)
TESTED_SITES = {
    "P61966": [
        (15, "R", "sigma-side basic residue contacting the (D/E) of (D/E)XXXL(L/I); for AP-1 "
                  "this contact depends mainly on gamma1 Arg15, so sigma1A R15 is weak"),
        (63, "A", "pocket residue; A63D abolishes binding of the tyrosinase signal by "
                  "gamma1-sigma1A, one of only three sigma1A substitutions that abolish it"),
        (88, "V", "hydrophobic pocket residue; V88D abolishes dileucine-signal binding"),
        (101, "L", "hydrophobic pocket residue; L101A has signal-dependent effects"),
        (103, "I", "hydrophobic pocket residue; I103S abolishes dileucine-signal binding"),
    ],
    "P53680": [
        (15, "R", "sigma2 R15; R15E inhibits dileucine-signal binding"),
        (63, "A", "sigma2 A63; A63D largely abolishes binding of both Nef and tyrosinase"),
        (88, "V", "sigma2 V88; V88D abolishes dileucine-signal binding"),
        (92, "N", "sigma2 N92; N92A had no effect on Nef binding but decreased tyrosinase "
                  "binding - a tolerant, signal-dependent position"),
        (100, "E", "sigma2 E100; E100A largely abolishes binding of both signals"),
        (101, "L", "sigma2 L101; L101A has signal-dependent effects"),
        (103, "L", "sigma2 L103; L103S abolishes dileucine-signal binding"),
    ],
    "Q92572": [
        (15, "R", "sigma3A R15"),
        (94, "V", "sigma3A V94; V94D decreases dileucine-signal binding"),
        (98, "D", "sigma3A D98; D98A was the one sigma3A substitution that did not reduce "
                  "binding of the TYROSINASE signal specifically - it is not a blanket "
                  "no-effect result, and the paper's other exception, L107A, is for Nef"),
        (107, "L", "sigma3A L107"),
        (109, "L", "sigma3A L109; L109S decreases dileucine-signal binding"),
    ],
}

TARGET = "P56377"


@dataclass
class Record:
    accession: str
    entry_name: str
    sequence: str
    length: int
    sequence_version: int


def fetch(accession: str) -> Record:
    url = UNIPROT_JSON.format(acc=accession)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        assert resp.status == 200, f"UniProt returned HTTP {resp.status} for {accession}"
        data = json.load(resp)
    assert data["primaryAccession"] == accession, (
        f"requested {accession} but UniProt returned {data['primaryAccession']} "
        "(merged/demerged accession)"
    )
    seq = data["sequence"]["value"]
    declared = data["sequence"]["length"]
    assert len(seq) == declared, f"{accession}: sequence length {len(seq)} != declared {declared}"
    version = data["entryAudit"]["sequenceVersion"]
    return Record(accession, data["uniProtkbId"], seq, declared, version)


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    return a


def map_positions(query: Record, subject: Record) -> tuple[dict[int, int], float]:
    """Align subject (comparator) to query (target) and return subject_pos -> query_pos.

    Positions are 1-based in each protein's own numbering. Identity is over aligned
    columns where both sides have a residue.
    """
    aln = aligner().align(subject.sequence, query.sequence)[0]
    mapping: dict[int, int] = {}
    ident = 0
    aligned_cols = 0
    for (s_start, s_end), (q_start, q_end) in zip(*aln.aligned):
        for offset in range(s_end - s_start):
            s_pos = s_start + offset  # 0-based in subject
            q_pos = q_start + offset  # 0-based in query
            mapping[s_pos + 1] = q_pos + 1
            aligned_cols += 1
            if subject.sequence[s_pos] == query.sequence[q_pos]:
                ident += 1
    pct = 100.0 * ident / aligned_cols if aligned_cols else 0.0
    return mapping, pct


def main() -> int:
    records = {acc: fetch(acc) for acc in PROTEINS}
    target = records[TARGET]

    print("# Sequences fetched live from UniProt")
    for acc, label in PROTEINS.items():
        r = records[acc]
        print(f"  {acc}  {r.entry_name:<14} len={r.length:<4} seqver={r.sequence_version}  {label}")
    print()

    rows = []
    print("# Pairwise identity to AP1S2 (sigma1B, P56377), global BLOSUM62 alignment")
    for acc in PROTEINS:
        if acc == TARGET:
            continue
        _, pct = map_positions(target, records[acc])
        print(f"  {acc} {records[acc].entry_name:<14} identity_to_P56377 = {pct:.1f}%")
    print()

    print("# Dileucine-signal binding residues (PMID:21097499) mapped onto AP1S2 numbering")
    for comparator, sites in TESTED_SITES.items():
        comp = records[comparator]
        mapping, pct = map_positions(target, comp)
        print(f"\n  comparator {comparator} ({comp.entry_name}, len {comp.length}, "
              f"{pct:.1f}% identical to AP1S2)")
        for pos, expected, role in sites:
            observed = comp.sequence[pos - 1]
            assert observed == expected, (
                f"{comparator} position {pos} is {observed}, not the {expected} reported in "
                "PMID:21097499 -- the sequence has changed; re-check before using this site"
            )
            tgt_pos = mapping.get(pos)
            tgt_res = target.sequence[tgt_pos - 1] if tgt_pos else None
            if tgt_pos is None:
                verdict = "NO_ALIGNED_POSITION"
            elif tgt_res == expected:
                verdict = "RETAINED"
            else:
                verdict = "SUBSTITUTED"
            print(f"    {comparator} {expected}{pos:<4} -> AP1S2 "
                  f"{tgt_res or '-'}{tgt_pos or '-':<4}  {verdict:<18} {role}")
            rows.append({
                "anchor_accession": comparator,
                "anchor_entry": comp.entry_name,
                "anchor_position": pos,
                "anchor_residue": expected,
                "anchor_sequence_version": comp.sequence_version,
                "target_accession": TARGET,
                "target_position": tgt_pos or "",
                "target_residue": tgt_res or "",
                "target_sequence_version": target.sequence_version,
                "verdict": verdict,
                "role": role,
            })

    print("\n# sigma1A residue at each sigma2-tested position "
          "(the AP-1 counterpart, computed not assumed)")
    s2, s1a = records["P53680"], records["P61966"]
    s2_to_s1a, _ = map_positions(s1a, s2)
    for pos, expected, _role in TESTED_SITES["P53680"]:
        tgt = s2_to_s1a.get(pos)
        res = s1a.sequence[tgt - 1] if tgt else None
        print(f"    sigma2 {expected}{pos:<4} -> sigma1A {res or '-'}{tgt or '-'}")

    print("\n# Alignment gap structure relative to AP1S2 (P56377, 157 aa)")
    for comparator in ("P53680", "Q9DB50"):
        comp = records[comparator]
        mapping, pct = map_positions(target, comp)
        aligned_target = set(mapping.values())
        gap_in_comp = [i for i in range(1, target.length + 1) if i not in aligned_target]
        gap_in_target = [i for i in range(1, comp.length + 1) if i not in mapping]
        print(f"  {comparator} ({comp.entry_name}, {comp.length} aa, {pct:.1f}% identical "
              f"over {len(mapping)} aligned columns)")
        print(f"    AP1S2 positions with no {comparator} residue aligned "
              f"({len(gap_in_comp)}): {gap_in_comp}")
        print(f"    {comparator} positions with no AP1S2 residue aligned "
              f"({len(gap_in_target)}): {gap_in_target}")
        mismatches = [(i, comp.sequence[i - 1], mapping[i], target.sequence[mapping[i] - 1])
                      for i in sorted(mapping)
                      if comp.sequence[i - 1] != target.sequence[mapping[i] - 1]]
        print(f"    mismatched aligned columns: {len(mismatches)}"
              + (f" {mismatches}" if len(mismatches) <= 12 else ""))

    out_path = Path(__file__).with_name("sigma_cargo_site.tsv")
    with out_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {out_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
