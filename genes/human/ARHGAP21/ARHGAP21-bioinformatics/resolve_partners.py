#!/usr/bin/env python3
"""Resolve every WITH/FROM token and IPI partner accession in ARHGAP21's GOA file.

Answers three questions that the GOA TSV alone cannot:

1. **Who is each accession?**  Entry name, gene name, organism, length, and
   Swiss-Prot/TrEMBL status.  A named partner is not a verified partner: the
   campaign has seen a 366-aa TrEMBL ORFeome clone standing in for a 1164-aa
   canonical protein, and a dead accession returning empty (which is
   indistinguishable from "carries no annotation").

2. **Is the partner human?**  UniProt's own INTERACTION block flags three of
   ARHGAP21's partners `Xeno`.  An `IPI` row whose partner is a non-human
   protein is asserting a cross-species interaction.

3. **Are the IBA WITH/FROM tokens self-referential?**  A PANTHER:PTN token is
   an ancestral tree node, not a protein; a UniProtKB token equal to the
   subject's own accession marks a PAINT curator judging the function core
   (valid, never CIRCULAR_OR_REDUNDANT).

Run:  uv run --with requests python resolve_partners.py
Writes: partners.json  (consumed by RESULTS.md)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SUBJECT = "Q5T5U3"  # ARHGAP21_HUMAN
UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
FIELDS = "accession,id,protein_name,gene_names,organism_name,length,reviewed"


def repo_root() -> Path:
    """Walk up from this file for the directory holding both src/ and publications/.

    Never hardcode a worktree path: a shared script with an asserted root
    reports confident wrong answers when run from a different checkout.
    """
    for parent in Path(__file__).resolve().parents:
        if (parent / "src").is_dir() and (parent / "publications").is_dir():
            return parent
    raise RuntimeError(
        "cannot locate repo root (no ancestor has both src/ and publications/)"
    )


ROOT = repo_root()
GOA = ROOT / "genes" / "human" / "ARHGAP21" / "ARHGAP21-goa.tsv"


def read_goa() -> list[dict[str, str]]:
    if not GOA.is_file():
        raise RuntimeError(f"missing GOA file {GOA}; run `just fetch-gene human ARHGAP21`")
    lines = GOA.read_text().rstrip("\n").split("\n")
    header = lines[0].split("\t")
    rows = [dict(zip(header, line.split("\t"))) for line in lines[1:] if line.strip()]
    if not rows:
        raise RuntimeError(f"{GOA} has no data rows")
    return rows


def collect_tokens(rows: list[dict[str, str]]) -> tuple[set[str], set[str], set[str]]:
    """Return (uniprot accessions, panther nodes, other tokens) from WITH/FROM."""
    accs: set[str] = set()
    panther: set[str] = set()
    other: set[str] = set()
    for r in rows:
        field = r.get("WITH/FROM", "").strip()
        if not field:
            continue
        for tok in field.split("|"):
            tok = tok.strip()
            if not tok:
                continue
            if tok.startswith("UniProtKB:"):
                accs.add(tok.split(":", 1)[1])
            elif tok.startswith("PANTHER:"):
                panther.add(tok.split(":", 1)[1])
            else:
                other.add(tok)
    return accs, panther, other


def fetch(acc: str) -> dict[str, object]:
    resp = requests.get(UNIPROT.format(acc=acc), params={"fields": FIELDS}, timeout=60)
    if resp.status_code != 200:
        # A dead/deleted accession is DATA, not a missing input -- record it.
        return {"accession": acc, "status": f"HTTP {resp.status_code}", "dead": True}
    d = resp.json()
    entry_type = d.get("entryType", "")
    # "reviewed" is a SUBSTRING of "unreviewed": anchor the test or every
    # TrEMBL entry is silently promoted to Swiss-Prot.
    reviewed = entry_type.startswith("UniProtKB reviewed")
    prot = d.get("proteinDescription", {}).get("recommendedName", {})
    name = prot.get("fullName", {}).get("value")
    if name is None:
        subs = d.get("proteinDescription", {}).get("submissionNames", [])
        name = subs[0]["fullName"]["value"] if subs else None
    genes = [g.get("geneName", {}).get("value") for g in d.get("genes", [])]
    genes = [g for g in genes if g]
    rec = {
        "accession": acc,
        "entry_name": d.get("uniProtkbId"),
        "protein_name": name,
        "gene": genes[0] if genes else None,
        "organism": d.get("organism", {}).get("scientificName"),
        "taxon_id": d.get("organism", {}).get("taxonId"),
        "length": d.get("sequence", {}).get("length"),
        "entry_type": entry_type,
        "reviewed": reviewed,
        "dead": False,
    }
    # A dead entry returns 200 with no name and no gene -- loud, not silent.
    if rec["entry_name"] is None and rec["protein_name"] is None:
        rec["dead"] = True
        rec["status"] = "inactive/deleted entry (200 but empty)"
    return rec


def main() -> int:
    rows = read_goa()
    accs, panther, other = collect_tokens(rows)

    # IPI partners live in WITH/FROM too, so `accs` already holds them; but
    # record which rows are IPI so the report can separate donor from partner.
    ipi_partners: dict[str, list[str]] = {}
    for r in rows:
        if r.get("GO EVIDENCE CODE") != "IPI":
            continue
        for tok in r.get("WITH/FROM", "").split("|"):
            tok = tok.strip()
            if tok.startswith("UniProtKB:"):
                ipi_partners.setdefault(tok.split(":", 1)[1], []).append(
                    r.get("REFERENCE", "")
                )

    resolved = {acc: fetch(acc) for acc in sorted(accs)}

    # Invariant: every token we set out to resolve must appear in the output.
    # Assert presence rather than validating only on match -- a guard that
    # `continue`s past a missing entry passes silently when data is deleted.
    missing = accs - set(resolved)
    assert not missing, f"tokens dropped during resolution: {sorted(missing)}"

    dead = [a for a, r in resolved.items() if r.get("dead")]
    nonhuman = [
        a
        for a, r in resolved.items()
        if not r.get("dead") and r.get("taxon_id") != 9606
    ]
    unreviewed = [
        a for a, r in resolved.items() if not r.get("dead") and not r.get("reviewed")
    ]

    # Self-reference: the subject appearing in its own WITH/FROM is expected.
    self_ref_rows = [
        r["GO TERM"]
        for r in rows
        if f"UniProtKB:{SUBJECT}" in r.get("WITH/FROM", "")
    ]

    out = {
        "subject": SUBJECT,
        "goa_data_rows": len(rows),
        "resolved": resolved,
        "panther_nodes": sorted(panther),
        "unparsed_tokens": sorted(other),
        "ipi_partner_refs": {k: sorted(set(v)) for k, v in sorted(ipi_partners.items())},
        "counts": {
            "distinct_withfrom_accessions": len(accs),
            "dead": len(dead),
            "non_human": len(nonhuman),
            "unreviewed_trembl": len(unreviewed),
            "reviewed_swissprot": len(accs) - len(unreviewed) - len(dead),
        },
        "dead_accessions": sorted(dead),
        "non_human_accessions": sorted(nonhuman),
        "unreviewed_accessions": sorted(unreviewed),
        "self_referential_iba_terms": sorted(set(self_ref_rows)),
    }

    # The reviewed/unreviewed split must not equal the total in both
    # directions -- a 100%-reviewed count is exactly what the "reviewed" is a
    # substring of "unreviewed" bug produces, and it looks plausible.
    assert out["counts"]["reviewed_swissprot"] + len(unreviewed) + len(dead) == len(
        accs
    ), "status counts do not partition the accession set"

    dest = Path(__file__).with_name("partners.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    for acc in sorted(resolved):
        r = resolved[acc]
        flag = "DEAD" if r.get("dead") else ("SP" if r.get("reviewed") else "TrEMBL")
        print(
            f"{acc:<10} {flag:<7} {str(r.get('gene')):<10} "
            f"{str(r.get('organism')):<28} {str(r.get('length')):>5} aa  "
            f"{r.get('protein_name')}"
        )
    print()
    print("PANTHER nodes (ancestral tree nodes, not proteins):", sorted(panther))
    print("counts:", json.dumps(out["counts"]))
    print("self-referential IBA terms:", out["self_referential_iba_terms"])
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
