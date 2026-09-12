#!/usr/bin/env python3
"""Test whether human AP5B1 (beta-5 adaptin) carries the beta-adaptin clathrin-binding
apparatus that AP-1/AP-2/AP-3 beta subunits use, and whether it has a hinge to carry it in.

Background
----------
The beta subunits of AP-1, AP-2 and AP-3 are built as: N-terminal alpha-solenoid trunk ->
long unstructured hinge -> C-terminal appendage (ear). Clathrin is recruited by short
linear motifs that sit *in the hinge*:

  * the "clathrin box"      consensus L(phi)x(phi)[DE]   (phi = bulky hydrophobic)
    e.g. AP2B1 LLNLD, AP1B1 LLDLD
  * the type-II / "LLDLL" box
  * the W-box               PWxxW  (and the short WDW / YQW motifs named by Hirst et al.)

Hirst et al. 2011 (PMID:22022230) reported, for the then-unnamed beta-5 sequence
DKFZp761E198, that the classical clathrin box, LLDLL and YQW are all absent, that the one
WDW present lies inside the alpha-solenoid rather than in a linker, and that beta-5 "lacks
a long unstructured linker separating the solenoid and appendage domains". This script
re-tests all four statements against the *current* UniProt sequences and the *current*
InterPro domain assignments, for AP5B1 and for the four classical beta adaptins as
positive controls.

Everything is fetched live; nothing is hardcoded except the accession list, the motif
consensus definitions, and the expected sequence lengths, which are asserted (not assumed)
so that a silently changed record fails loudly.

Usage:  uv run python clathrin_box_scan.py [--json out.json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field

import requests

UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"
UNIPROT_JSON = "https://rest.uniprot.org/uniprotkb/{acc}.json?fields=ft_helix,ft_strand,ft_turn,ft_region"
INTERPRO_MATCHES = (
    "https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/?page_size=200"
)

# accession -> (gene symbol, expected length, role in this test)
TARGETS: dict[str, tuple[str, int, str]] = {
    "Q2VPB7": ("AP5B1", 878, "test subject: beta-5, AP-5"),
    "Q10567": ("AP1B1", 949, "positive control: beta-1, AP-1 (clathrin-dependent)"),
    "P63010": ("AP2B1", 937, "positive control: beta-2, AP-2 (clathrin-dependent)"),
    "O00203": ("AP3B1", 1094, "control: beta-3A, AP-3 (largely clathrin-independent)"),
    "Q9Y6B7": ("AP4B1", 739, "control: beta-4, AP-4 (clathrin-independent)"),
}

# Motif name -> regex. The clathrin box consensus is the standard L(phi)x(phi)[DE].
MOTIFS: dict[str, str] = {
    "clathrin_box_LPhixPhiDE": r"L[LIMFV].[LIMFV][DE]",
    "type_II_LLDLL": r"LLDLL",
    "YQW": r"YQW",
    "W_box_PWxxW": r"PW..W",
    "WDW": r"WDW",
}


@dataclass
class Protein:
    acc: str
    symbol: str
    seq: str
    domains: list[tuple[str, str, int, int]] = field(default_factory=list)  # db, id, start, end
    features: list[tuple[str, int, int, str]] = field(default_factory=list)  # type, start, end, note

    @property
    def length(self) -> int:
        return len(self.seq)


def fetch_sequence(acc: str) -> str:
    r = requests.get(UNIPROT_FASTA.format(acc=acc), timeout=60)
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    if not lines or not lines[0].startswith(">"):
        raise RuntimeError(f"{acc}: unexpected FASTA payload: {r.text[:200]!r}")
    return "".join(lines[1:])


def fetch_domains(acc: str) -> list[tuple[str, str, int, int]]:
    """Return (source_db, entry_accession, start, end) for every Pfam match."""
    r = requests.get(INTERPRO_MATCHES.format(acc=acc), timeout=120)
    r.raise_for_status()
    out: list[tuple[str, str, int, int]] = []
    for res in r.json().get("results", []):
        meta = res["metadata"]
        if meta.get("source_database") != "pfam":
            continue
        for prot in res.get("proteins", []):
            for loc in prot.get("entry_protein_locations", []):
                frags = loc.get("fragments", [])
                if not frags:
                    continue
                out.append(
                    (
                        meta["source_database"],
                        meta["accession"],
                        min(f["start"] for f in frags),
                        max(f["end"] for f in frags),
                    )
                )
    return sorted(out, key=lambda d: d[2])


def fetch_features(acc: str) -> list[tuple[str, int, int, str]]:
    """Secondary-structure (from PDB) and REGION features, as (type, start, end, note)."""
    r = requests.get(UNIPROT_JSON.format(acc=acc), timeout=60)
    r.raise_for_status()
    out: list[tuple[str, int, int, str]] = []
    for feat in r.json().get("features", []):
        loc = feat["location"]
        start, end = loc["start"].get("value"), loc["end"].get("value")
        if start is None or end is None:
            continue
        out.append((feat["type"], start, end, feat.get("description") or ""))
    return sorted(out, key=lambda f: f[1])


def features_at(pos: int, features: list[tuple[str, int, int, str]]) -> list[str]:
    return [
        f"{ftype}:{start}-{end}" + (f" ({note})" if note else "")
        for ftype, start, end, note in features
        if start <= pos <= end
    ]


def in_domain(pos: int, domains: list[tuple[str, str, int, int]]) -> str | None:
    """1-based residue position -> Pfam accession covering it, else None (= linker/loop)."""
    for _db, acc, start, end in domains:
        if start <= pos <= end:
            return acc
    return None


def scan(prot: Protein) -> dict[str, list[dict]]:
    hits: dict[str, list[dict]] = {}
    for name, pattern in MOTIFS.items():
        found = []
        for m in re.finditer(f"(?=({pattern}))", prot.seq):
            start = m.start() + 1  # 1-based
            text = m.group(1)
            found.append(
                {
                    "start": start,
                    "end": start + len(text) - 1,
                    "match": text,
                    "within_pfam_domain": in_domain(start, prot.domains),
                    "uniprot_features_at_start": features_at(start, prot.features),
                }
            )
        hits[name] = found
    return hits


def trunk_to_next_gap(prot: Protein) -> dict | None:
    """The linker between the alpha-solenoid trunk (taken as the longest Pfam domain)
    and the next domain C-terminal to it. In AP-1/AP-2 beta subunits this interval is
    the hinge that carries the clathrin box."""
    if len(prot.domains) < 2:
        return None
    trunk = max(prot.domains, key=lambda d: d[3] - d[2])
    after = [d for d in prot.domains if d[2] > trunk[3]]
    if not after:
        return None
    nxt = min(after, key=lambda d: d[2])
    return {
        "trunk": trunk[1],
        "trunk_span": [trunk[2], trunk[3]],
        "next_domain": nxt[1],
        "linker_start": trunk[3] + 1,
        "linker_end": nxt[2] - 1,
        "linker_length": nxt[2] - trunk[3] - 1,
    }


def inter_domain_gaps(prot: Protein) -> list[dict]:
    """Gaps between consecutive Pfam domains: the candidate hinge/linker regions."""
    gaps = []
    doms = prot.domains
    for a, b in zip(doms, doms[1:]):
        gap_start, gap_end = a[3] + 1, b[2] - 1
        if gap_end >= gap_start:
            gaps.append(
                {
                    "after": a[1],
                    "before": b[1],
                    "start": gap_start,
                    "end": gap_end,
                    "length": gap_end - gap_start + 1,
                }
            )
    return gaps


def c_terminal_tail(prot: Protein) -> dict:
    """Residues C-terminal to the last Pfam domain (contains the appendage in the
    beta adaptins whose ear is not Pfam-covered, and nothing much otherwise)."""
    if not prot.domains:
        return {"start": 1, "end": prot.length, "length": prot.length}
    last_end = max(d[3] for d in prot.domains)
    return {"start": last_end + 1, "end": prot.length, "length": prot.length - last_end}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", help="write the full result set to this path")
    args = ap.parse_args()

    report: dict[str, dict] = {}
    proteins: dict[str, Protein] = {}

    for acc, (symbol, expected_len, role) in TARGETS.items():
        seq = fetch_sequence(acc)
        # Assert, do not assume: a merged/updated accession must fail loudly.
        assert len(seq) == expected_len, (
            f"{symbol} ({acc}): UniProt now returns {len(seq)} aa, expected {expected_len}. "
            "Re-check the accession before trusting anything below."
        )
        prot = Protein(
            acc=acc, symbol=symbol, seq=seq,
            domains=fetch_domains(acc), features=fetch_features(acc),
        )
        proteins[symbol] = prot
        report[symbol] = {
            "accession": acc,
            "role": role,
            "length": prot.length,
            "pfam_domains": [
                {"accession": d[1], "start": d[2], "end": d[3]} for d in prot.domains
            ],
            "inter_domain_gaps": inter_domain_gaps(prot),
            "trunk_to_next_domain_linker": trunk_to_next_gap(prot),
            "c_terminal_tail_after_last_pfam_domain": c_terminal_tail(prot),
            "motif_hits": scan(prot),
        }

    # ---- human-readable summary -------------------------------------------------
    print("=" * 78)
    print("Clathrin-binding motifs in beta-adaptin family members (live UniProt/InterPro)")
    print("=" * 78)
    for symbol, data in report.items():
        print(f"\n### {symbol} ({data['accession']}), {data['length']} aa - {data['role']}")
        doms = data["pfam_domains"]
        print("  Pfam domains: " + (", ".join(f"{d['accession']}:{d['start']}-{d['end']}" for d in doms) or "none"))
        gaps = data["inter_domain_gaps"]
        print(
            "  Inter-domain gaps: "
            + ("; ".join(f"{g['after']}->{g['before']} {g['start']}-{g['end']} ({g['length']} aa)" for g in gaps) or "none")
        )
        tl = data["trunk_to_next_domain_linker"]
        if tl:
            print(
                f"  Trunk ({tl['trunk']} {tl['trunk_span'][0]}-{tl['trunk_span'][1]}) -> {tl['next_domain']} "
                f"linker: {tl['linker_length']} aa ({tl['linker_start']}-{tl['linker_end']})"
            )
        tail = data["c_terminal_tail_after_last_pfam_domain"]
        print(f"  Residues after last Pfam domain: {tail['length']} aa ({tail['start']}-{tail['end']})")
        for motif, hits in data["motif_hits"].items():
            if not hits:
                print(f"  {motif:24s}: ABSENT")
                continue
            rendered = "; ".join(
                f"{h['match']}@{h['start']}"
                + (f" [inside {h['within_pfam_domain']}]" if h["within_pfam_domain"] else " [outside Pfam domains]")
                for h in hits
            )
            print(f"  {motif:24s}: {len(hits)} hit(s): {rendered}")

    # ---- the three specific claims being tested ---------------------------------
    ap5 = report["AP5B1"]
    print("\n" + "=" * 78)
    print("Claims under test (Hirst et al. 2011, PMID:22022230), re-evaluated")
    print("=" * 78)

    cb = ap5["motif_hits"]["clathrin_box_LPhixPhiDE"]
    cb_outside = [h for h in cb if h["within_pfam_domain"] is None]
    print(
        f"1. classical clathrin box in AP5B1: {len(cb)} sequence match(es) to L(phi)x(phi)[DE], "
        f"of which {len(cb_outside)} outside any Pfam domain."
    )
    for sym in ("AP1B1", "AP2B1", "AP3B1", "AP4B1"):
        ctrl = report[sym]["motif_hits"]["clathrin_box_LPhixPhiDE"]
        ctrl_out = [h for h in ctrl if h["within_pfam_domain"] is None]
        print(
            f"   control {sym}: {len(ctrl)} match(es), {len(ctrl_out)} outside any Pfam domain"
            + (
                "  -> " + "; ".join(f"{h['match']}@{h['start']}" for h in ctrl_out)
                if ctrl_out
                else ""
            )
        )

    print(
        f"2. LLDLL in AP5B1: {'ABSENT' if not ap5['motif_hits']['type_II_LLDLL'] else ap5['motif_hits']['type_II_LLDLL']}"
        f"   |   YQW in AP5B1: {'ABSENT' if not ap5['motif_hits']['YQW'] else ap5['motif_hits']['YQW']}"
    )

    wdw = ap5["motif_hits"]["WDW"]
    print(f"3. WDW in AP5B1: {len(wdw)} hit(s); the validated W-box PW..W is "
          f"{'ABSENT' if not ap5['motif_hits']['W_box_PWxxW'] else 'PRESENT'}")
    for h in wdw:
        loc = h["within_pfam_domain"] or "outside any Pfam domain"
        feats = ", ".join(h["uniprot_features_at_start"]) or "no UniProt feature covers this residue"
        print(f"   WDW at {h['start']}-{h['end']}, {loc}; UniProt features here: {feats}")

    print("4. trunk -> next-domain linker (the hinge position in AP-1/AP-2 beta subunits):")
    for sym in ("AP5B1", "AP1B1", "AP2B1", "AP3B1", "AP4B1"):
        tl = report[sym]["trunk_to_next_domain_linker"]
        print(
            f"   {sym}: {tl['linker_length']} aa ({tl['trunk']} -> {tl['next_domain']})"
            if tl
            else f"   {sym}: n/a"
        )

    if args.json:
        with open(args.json, "w") as fh:
            json.dump(report, fh, indent=2)
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
