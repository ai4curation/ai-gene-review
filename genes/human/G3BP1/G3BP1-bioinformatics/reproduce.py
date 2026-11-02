"""Test whether human G3BP1 carries the sequence features an ATP-dependent helicase needs.

Motivation: UniProt Q13283 carries EC 3.6.4.12/3.6.4.13 and the alternate name
"ATP-dependent DNA helicase VIII" on the strength of a single 1999 report
(PMID:9889278), and GOA carries GO:0003678, GO:0003724, GO:0033677 and GO:0016887
from it. All known ATP-dependent helicases are built on a RecA-like (SF1/SF2) or
RecA-fold (SF3-SF6) nucleotide-binding core whose Walker A (P-loop) and Walker B
motifs are required for ATP binding and hydrolysis. This script asks, from the
sequences and domain annotations themselves, whether G3BP1 has such a core.

Inputs are fetched live from the UniProt REST API (no API key needed) and cached.
Nothing here is hardcoded: the motif hits, the domain coverage and the verdict
counts are all computed from the downloaded records.

Usage: uv run reproduce.py   (or: python reproduce.py)
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

CACHE = Path(__file__).parent / "cache"
OUT = Path(__file__).parent / "results.json"

# Target plus positive and negative controls.
#   G3BP1    - the protein under test
#   DDX3X    - bona fide DEAD-box (SF2) RNA helicase
#   EIF4A3   - bona fide DEAD-box (SF2) RNA helicase
#   BLM      - bona fide RecQ (SF2) DNA helicase
#   UPF1     - bona fide SF1 RNA helicase
#   NUTF2    - NTF2 domain protein, no helicase activity (fold control for G3BP1's NTF2)
#   HNRNPA1  - RRM + RGG protein, no helicase activity (fold control for G3BP1's RRM/RGG)
ACCESSIONS = {
    "G3BP1": "Q13283",
    "DDX3X": "O00571",
    "EIF4A3": "P60842",
    "BLM": "P54132",
    "UPF1": "Q92900",
    "NUTF2": "P61970",
    "HNRNPA1": "P09651",
}
TARGET = "G3BP1"
POSITIVE_CONTROLS = ["DDX3X", "EIF4A3", "BLM", "UPF1"]
NEGATIVE_CONTROLS = ["NUTF2", "HNRNPA1"]

# Canonical nucleotide-binding / helicase motifs, as regular expressions.
# Walker A (P-loop) and Walker B are the two motifs that every ATP-dependent
# helicase superfamily shares; the DEAD/DEAH box is the SF2 Walker B variant.
MOTIFS = {
    # Walker A / P-loop: GxxxxGK[ST]
    "walker_a_ploop": r"G.{4}GK[ST]",
    # DEAD-box / DExD/H box: the SF2 Walker B motif
    "dexdh_box": r"D E [AI] [DH]".replace(" ", ""),
    # Walker B, general form: 4 hydrophobic residues followed by DE
    "walker_b": r"[ILVFMAC]{4}DE",
    # Helicase motif VI (SF2 QxxGRxGR arginine finger)
    "motif_vi_qxxgrxgr": r"Q.{2}GR.GR",
    # SF2 motif III (SAT)
    "motif_iii_sat": r"SAT",
    # SF1/SF2 motif Q (adenine recognition)
    "q_motif": r"[FILV].{2}Q[AP].{2}[ILV]",
}

# InterPro / Pfam / CDD signature prefixes that indicate a helicase ATPase core.
HELICASE_SIGNATURE_PATTERNS = [
    r"helicase",
    r"P-loop",
    r"DEAD",
    r"DEAH",
    r"RecA",
    r"AAA",
    r"UvrD",
    r"RecQ",
    r"ATPase",
]


def fetch(accession: str) -> dict:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{accession}.json"
    if not path.is_file():
        url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
        with urllib.request.urlopen(url, timeout=60) as fh:
            path.write_bytes(fh.read())
    return json.loads(path.read_text())


def domains(record: dict) -> list[dict]:
    kept = []
    for feature in record.get("features", []):
        if feature["type"] not in {"Domain", "Region", "Nucleotide binding", "Binding site"}:
            continue
        loc = feature["location"]
        start, end = loc["start"].get("value"), loc["end"].get("value")
        if start is None or end is None:
            continue
        kept.append(
            {
                "type": feature["type"],
                "note": feature.get("description", ""),
                "start": start,
                "end": end,
            }
        )
    return kept


def signatures(record: dict) -> list[str]:
    names = []
    for xref in record.get("uniProtKBCrossReferences", []):
        if xref["database"] not in {"InterPro", "Pfam", "PROSITE", "CDD", "SMART", "SUPFAM", "Gene3D"}:
            continue
        for prop in xref.get("properties", []):
            if prop["key"] in {"EntryName", "Description"}:
                names.append(f"{xref['database']}:{xref['id']}:{prop['value']}")
    return names


def helicase_signature_hits(sig_names: list[str]) -> list[str]:
    hits = []
    for name in sig_names:
        for pattern in HELICASE_SIGNATURE_PATTERNS:
            if re.search(pattern, name, flags=re.IGNORECASE):
                hits.append(name)
                break
    return hits


def motif_hits(sequence: str) -> dict:
    found = {}
    for name, pattern in MOTIFS.items():
        found[name] = [
            {"start": m.start() + 1, "match": m.group(0)}
            for m in re.finditer(pattern, sequence)
        ]
    return found


def analyse(symbol: str, accession: str) -> dict:
    record = fetch(accession)
    sequence = record["sequence"]["value"]
    sig_names = signatures(record)
    hel_sigs = helicase_signature_hits(sig_names)
    motifs = motif_hits(sequence)
    core_motifs = ["walker_a_ploop", "walker_b", "dexdh_box"]
    n_core = sum(1 for m in core_motifs if motifs[m])
    return {
        "symbol": symbol,
        "accession": accession,
        "length": len(sequence),
        "sequence_version": record["entryAudit"]["sequenceVersion"],
        "domains": domains(record),
        "n_signatures": len(sig_names),
        "helicase_signatures": hel_sigs,
        "motifs": motifs,
        "n_core_nucleotide_motifs_present": n_core,
        "has_helicase_atpase_signature": bool(hel_sigs),
    }


# --------------------------------------------------------------------------- #
# Part 2: where in the PANTHER family do the helicase annotations actually sit? #
# --------------------------------------------------------------------------- #
# The three helicase IBA rows on Q13283 descend from PANTHER node PTN002581351.
# An IBA asserts that the function was present at that node and inherited; the
# question that bears on it is what descendant evidence the node rests on. This
# census asks, for every reviewed member of PTHR10693, which helicase terms it
# carries and under which evidence codes.
PANTHER_FAMILY = "PTHR10693"
MEMBER_CSV = "interpro/panther/PTHR10693/PTHR10693-entries.csv"
HELICASE_TERMS = {
    "GO:0003678": "DNA helicase activity",
    "GO:0003724": "RNA helicase activity",
    "GO:0033677": "DNA/RNA helicase activity",
    "GO:0004386": "helicase activity",
    "GO:0016887": "ATP hydrolysis activity",
}
# Evidence codes that represent an experiment on the gene product itself.
EXPERIMENTAL_ECO = {
    "ECO:0000314",  # IDA
    "ECO:0000315",  # IMP
    "ECO:0000316",  # IGI
    "ECO:0000353",  # IPI
    "ECO:0000269",  # EXP
    "ECO:0006056",  # HDA
}


def repo_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "genes").is_dir() and (parent / "justfile").is_file():
            return parent
    raise RuntimeError("cannot locate repository root")


def family_members() -> list[dict]:
    path = repo_root() / MEMBER_CSV
    if not path.is_file():
        return []
    import csv

    with path.open() as fh:
        return list(csv.DictReader(fh))


def quickgo(accession: str) -> list[dict]:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"quickgo-{accession}.json"
    if not path.is_file():
        url = (
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
            f"?geneProductId=UniProtKB:{accession}&limit=200"
        )
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as fh:
            path.write_bytes(fh.read())
    return json.loads(path.read_text()).get("results", [])


def family_census() -> dict:
    members = family_members()
    if not members:
        return {"available": False, "reason": f"{MEMBER_CSV} not found; run `just fetch-gene human G3BP1`"}
    per_member = []
    for m in members:
        anns = quickgo(m["id"])
        hel = sorted(
            {f"{a['goId']}/{a['evidenceCode']}" for a in anns if a["goId"] in HELICASE_TERMS}
        )
        experimental = sorted(
            {
                a["goId"]
                for a in anns
                if a["goId"] in HELICASE_TERMS and a["evidenceCode"] in EXPERIMENTAL_ECO
            }
        )
        per_member.append(
            {
                "accession": m["id"],
                "gene": m["gene"],
                "organism": m["source_tax_name"],
                "subfamily": m["subfamily"],
                "n_annotations": len(anns),
                "helicase_rows": hel,
                "helicase_terms_with_experimental_evidence": experimental,
            }
        )
    with_hel = [x for x in per_member if x["helicase_rows"]]
    with_exp = [x for x in per_member if x["helicase_terms_with_experimental_evidence"]]
    return {
        "available": True,
        "family": PANTHER_FAMILY,
        "n_reviewed_members": len(per_member),
        "members_with_any_helicase_row": [x["accession"] for x in with_hel],
        "subfamilies_with_any_helicase_row": sorted({x["subfamily"] for x in with_hel}),
        "members_with_experimental_helicase_evidence": [x["accession"] for x in with_exp],
        "per_member": per_member,
    }


def main() -> int:
    results = {sym: analyse(sym, acc) for sym, acc in ACCESSIONS.items()}

    target = results[TARGET]
    summary = {
        "target": TARGET,
        "target_has_helicase_atpase_signature": target["has_helicase_atpase_signature"],
        "target_core_nucleotide_motifs": target["n_core_nucleotide_motifs_present"],
        "positive_controls_with_helicase_signature": [
            s for s in POSITIVE_CONTROLS if results[s]["has_helicase_atpase_signature"]
        ],
        "positive_controls_without_helicase_signature": [
            s for s in POSITIVE_CONTROLS if not results[s]["has_helicase_atpase_signature"]
        ],
        "negative_controls_with_helicase_signature": [
            s for s in NEGATIVE_CONTROLS if results[s]["has_helicase_atpase_signature"]
        ],
        "target_domain_notes": sorted(
            {d["note"] for d in target["domains"] if d["type"] == "Domain"}
        ),
        "target_nucleotide_binding_features": [
            d for d in target["domains"] if d["type"] in {"Nucleotide binding", "Binding site"}
        ],
    }
    # The discriminating test: does the assay separate known helicases from the target?
    summary["controls_behave_as_expected"] = (
        not summary["positive_controls_without_helicase_signature"]
        and not summary["negative_controls_with_helicase_signature"]
    )

    census = family_census()

    OUT.write_text(
        json.dumps(
            {"summary": summary, "per_protein": results, "panther_family_census": census},
            indent=2,
        )
        + "\n"
    )

    print(f"{'protein':10s} {'len':>5s}  helicase/ATPase signature  core nt motifs  domains")
    for sym in ACCESSIONS:
        r = results[sym]
        notes = ", ".join(sorted({d["note"] for d in r["domains"] if d["type"] == "Domain"})) or "-"
        print(
            f"{sym:10s} {r['length']:5d}  {str(r['has_helicase_atpase_signature']):>25s}"
            f"  {r['n_core_nucleotide_motifs_present']:>14d}  {notes[:70]}"
        )
    print()
    print("controls behave as expected:", summary["controls_behave_as_expected"])
    print()
    if not census["available"]:
        print("PANTHER family census skipped:", census["reason"])
    else:
        print(f"{PANTHER_FAMILY} census over {census['n_reviewed_members']} reviewed members:")
        for m in census["per_member"]:
            exp = ",".join(m["helicase_terms_with_experimental_evidence"]) or "-"
            print(
                f"  {m['accession']:8s} {m['gene']:10s} {m['subfamily']:16s}"
                f" {m['organism'][:30]:32s} helicase rows={len(m['helicase_rows']):2d}  experimental={exp}"
            )
        print("  subfamilies with any helicase row:", census["subfamilies_with_any_helicase_row"])
        print(
            "  members with experimental helicase evidence:",
            census["members_with_experimental_helicase_evidence"],
        )
    print()
    print("wrote", OUT.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
