"""Where does AP4M1 (mu4) bind cargo, and is that site shared with the clathrin-adaptor mu subunits?

Motivation
----------
The GO_Central IBA for GO:0035615 "clathrin-cargo adaptor activity" reaches AP4M1 from
the pan-mu ancestral node PTN000055849, whose IBD seeds are all AP-1 / AP-2 mu subunits.
UniProt records two mutagenesis positions for human mu4 that abolish or strongly reduce
binding of the APP YKFFE signal (F255A, R283D; ECO:0000269|PubMed:20230749).

This script asks two mechanically checkable questions:

1. Does the human AP4M1 sequence actually carry F at 255 and R at 283, inside the
   annotated MHD domain (184-452)?
2. Are those two positions conserved in mu4 orthologs, and what residues do the
   clathrin-adaptor paralogs (mu1A, mu1B, mu2, mu3A, mu3B) carry at the aligned
   positions?

Everything is fetched live from the UniProt REST API. Nothing is hardcoded except the
accessions and the two UniProt-annotated positions being tested.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass

import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb"

TARGET = "O00189"  # human AP4M1 / mu4

# UniProt FT MUTAGEN positions on O00189 (evidence ECO:0000269|PubMed:20230749):
#   255 F->A: Abolishes interaction with APP.
#   283 R->D: Strongly reduced interaction with APP.
SITES = {255: "F", 283: "R"}

ORTHOLOGS = {
    "Q9JKC7": "Ap4m1 (Mus musculus)",
    "Q2PWT8": "Ap4m1 (Rattus norvegicus)",
    "E2RED8": "AP4M1 (Canis lupus familiaris)",
    "Q9SB50": "AP4M (Arabidopsis thaliana)",
}

PARALOGS = {
    "Q9BXS5": "AP1M1 / mu1A (Homo sapiens)",
    "Q9Y6Q5": "AP1M2 / mu1B (Homo sapiens)",
    "Q96CW1": "AP2M1 / mu2 (Homo sapiens)",
    "Q9Y2T2": "AP3M1 / mu3A (Homo sapiens)",
    "P53677": "AP3M2 / mu3B (Homo sapiens)",
}


@dataclass
class Entry:
    accession: str
    uniprot_id: str
    name: str
    organism: str
    sequence: str
    sequence_version: int

    @property
    def length(self) -> int:
        return len(self.sequence)


def fetch(accession: str) -> Entry:
    r = requests.get(f"{UNIPROT}/{accession}.json", timeout=60)
    r.raise_for_status()
    d = r.json()
    seq = d["sequence"]["value"]
    return Entry(
        accession=d["primaryAccession"],
        uniprot_id=d.get("uniProtkbId", "?"),
        name=d.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value", "?"),
        organism=d.get("organism", {}).get("scientificName", "?"),
        sequence=seq,
        sequence_version=d.get("entryAudit", {}).get("sequenceVersion", 0),
    )


def mhd_domain(accession: str) -> tuple[int, int] | None:
    """Return the (start, end) of the MHD domain from the UniProt feature table."""
    r = requests.get(f"{UNIPROT}/{accession}.json", timeout=60)
    r.raise_for_status()
    for f in r.json().get("features", []):
        if f.get("type") == "Domain" and "MHD" in (f.get("description") or ""):
            loc = f["location"]
            return loc["start"]["value"], loc["end"]["value"]
    return None


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    return a


def map_positions(
    target: Entry, other: Entry, positions: list[int]
) -> tuple[dict[int, tuple[int | None, str]], float]:
    """Align `other` to `target` and report, for each 1-based target position,
    the aligned position and residue in `other`. Returns (mapping, percent identity)."""
    aln = aligner().align(target.sequence, other.sequence)[0]
    t_idx, o_idx = aln.indices  # 0-based, -1 for gaps
    mapping: dict[int, tuple[int | None, str]] = {}
    ident = 0
    aligned_cols = 0
    for ti, oi in zip(t_idx, o_idx):
        if ti >= 0 and oi >= 0:
            aligned_cols += 1
            if target.sequence[ti] == other.sequence[oi]:
                ident += 1
    for p in positions:
        hit: tuple[int | None, str] = (None, "-")
        for ti, oi in zip(t_idx, o_idx):
            if ti == p - 1:
                hit = (
                    (oi + 1, other.sequence[oi]) if oi >= 0 else (None, "-")
                )
                break
        mapping[p] = hit
    pid = 100.0 * ident / aligned_cols if aligned_cols else 0.0
    return mapping, pid


def main() -> int:
    target = fetch(TARGET)
    print(f"# target: {target.accession} {target.uniprot_id} ({target.organism}), "
          f"length {target.length}, sequence version {target.sequence_version}")

    # (1) The two UniProt mutagenesis positions must really carry those residues.
    for pos, expected in sorted(SITES.items()):
        observed = target.sequence[pos - 1]
        status = "OK" if observed == expected else "MISMATCH"
        print(f"#   position {pos}: expected {expected}, observed {observed}  [{status}]")
        assert observed == expected, (
            f"{TARGET} position {pos} is {observed}, not the UniProt-annotated {expected}; "
            "the UniProt record or this script's positions are out of date"
        )

    dom = mhd_domain(TARGET)
    print(f"# MHD domain (UniProt FT): {dom}")
    assert dom is not None, "no MHD domain found in the O00189 feature table"
    for pos in SITES:
        assert dom[0] <= pos <= dom[1], f"position {pos} lies outside the MHD domain {dom}"
    print(f"#   both tested positions lie inside the MHD domain {dom[0]}-{dom[1]}")

    rows = []
    for group, members in (("ortholog", ORTHOLOGS), ("paralog", PARALOGS)):
        for acc, label in members.items():
            e = fetch(acc)
            mapping, pid = map_positions(target, e, sorted(SITES))
            rows.append(
                {
                    "group": group,
                    "accession": e.accession,
                    "uniprot_id": e.uniprot_id,
                    "label": label,
                    "length": e.length,
                    "sequence_version": e.sequence_version,
                    "percent_identity_to_O00189": round(pid, 1),
                    **{
                        f"aligned_to_{p}": (
                            f"{mapping[p][1]}{mapping[p][0]}"
                            if mapping[p][0]
                            else "gap"
                        )
                        for p in sorted(SITES)
                    },
                    **{
                        f"matches_{p}{SITES[p]}": mapping[p][1] == SITES[p]
                        for p in sorted(SITES)
                    },
                }
            )

    header = list(rows[0].keys())
    with open("mu_signal_site.tsv", "w") as fh:
        fh.write("\t".join(header) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[h]) for h in header) + "\n")

    print()
    print("\t".join(header))
    for r in rows:
        print("\t".join(str(r[h]) for h in header))

    orth = [r for r in rows if r["group"] == "ortholog"]
    para = [r for r in rows if r["group"] == "paralog"]
    print()
    print("# summary")
    for p, res in sorted(SITES.items()):
        n_o = sum(1 for r in orth if r[f"matches_{p}{res}"])
        n_p = sum(1 for r in para if r[f"matches_{p}{res}"])
        print(f"#   {res}{p}: retained in {n_o}/{len(orth)} mu4 orthologs, "
              f"{n_p}/{len(para)} clathrin-adaptor mu paralogs")
    pids_o = [r["percent_identity_to_O00189"] for r in orth]
    pids_p = [r["percent_identity_to_O00189"] for r in para]
    print(f"#   identity to human mu4: orthologs {min(pids_o)}-{max(pids_o)}%, "
          f"mu1/mu2/mu3 paralogs {min(pids_p)}-{max(pids_p)}%")

    with open("mu_signal_site.json", "w") as fh:
        json.dump(
            {
                "target": {
                    "accession": target.accession,
                    "length": target.length,
                    "sequence_version": target.sequence_version,
                    "mhd_domain": list(dom),
                    "tested_sites": SITES,
                },
                "rows": rows,
            },
            fh,
            indent=2,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
