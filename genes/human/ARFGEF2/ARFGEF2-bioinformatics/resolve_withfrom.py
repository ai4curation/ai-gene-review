"""Resolve every WITH/FROM identifier in the ARFGEF2 GOA file.

Outputs:

1. `withfrom_resolved.tsv` - one row per distinct WITH/FROM token, resolved to a
   UniProt accession, gene symbol, organism and Swiss-Prot/TrEMBL status where
   such a resolution exists.
2. `supporting_entities.json` - the `supporting_entities` list for every GOA row
   that has a WITH/FROM, built **from the GOA file** so the review YAML can be
   filled mechanically. Hand-maintained source lists have drifted on every gene
   in this campaign that tried it.

Run: uv run python resolve_withfrom.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from uniprot import resolve_mod_id, summarise, uniprot_entry

HERE = Path(__file__).parent
GOA = HERE.parent / "ARFGEF2-goa.tsv"

MOD_DBS = {"MGI", "RGD", "FB", "ZFIN", "AGI_LocusCode", "SGD", "PomBase"}
# Tokens that are not entities at all: ontology/vocabulary/pipeline references.
NON_ENTITY_DBS = {"InterPro", "UniProtKB-SubCell", "ARBA", "GO", "ensembl", "Ensembl"}

UNRESOLVED = "UNRESOLVED"


def load_goa() -> list[dict[str, str]]:
    if not GOA.exists():
        raise FileNotFoundError(
            f"{GOA} is missing. Regenerate it with: just fetch-gene human ARFGEF2"
        )
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def _describe(acc: str, n_hits: int, kind: str, token: str) -> dict[str, str]:
    s = summarise(uniprot_entry(acc))
    if not s["id"]:
        raise RuntimeError(
            f"{acc} (from {token}) returned no entry name. A dead/deleted UniProt "
            "accession is indistinguishable from an entity with no annotations; "
            "resolve the live accession before using it."
        )
    return {
        "token": token,
        "kind": kind,
        "accession": s["accession"],
        "entry_name": s["id"],
        "gene": s["gene"],
        "protein": s["protein"],
        "organism": s["organism"],
        "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
        "length": str(s["length"]),
        "n_hits": str(n_hits),
    }


def resolve_token(token: str) -> dict[str, str]:
    db, _, _local = token.partition(":")
    if db == "UniProtKB":
        return _describe(token.split(":", 1)[1], 1, "protein", token)
    if db in MOD_DBS:
        hits = resolve_mod_id(token)
        if not hits:
            return {"token": token, "kind": "mod-id", "accession": "", "entry_name": "",
                    "gene": "", "protein": UNRESOLVED, "organism": "", "reviewed": "",
                    "length": "", "n_hits": "0"}
        reviewed = [h for h in hits
                    if h.get("entryType", "").startswith("UniProtKB reviewed")]
        best = (reviewed or hits)[0]
        return _describe(best["primaryAccession"], len(hits), "mod-id", token)
    if db == "PANTHER":
        # A PTN id is an internal ancestral tree node, not a protein.
        return {"token": token, "kind": "panther-node", "accession": "", "entry_name": "",
                "gene": "", "protein": "PAINT ancestral node", "organism": "",
                "reviewed": "", "length": "", "n_hits": ""}
    if db in NON_ENTITY_DBS:
        return {"token": token, "kind": db.lower(), "accession": "", "entry_name": "",
                "gene": "", "protein": "", "organism": "", "reviewed": "",
                "length": "", "n_hits": ""}
    raise ValueError(f"unhandled WITH/FROM database {db!r} in token {token!r}")


def main() -> None:
    rows = load_goa()
    resolved: dict[str, dict[str, str]] = {}
    per_row = []
    for i, row in enumerate(rows, start=1):
        wf = (row["WITH/FROM"] or "").strip()
        if not wf:
            continue
        tokens: list[str] = []
        for tok in wf.split("|"):
            tok = tok.strip()
            if tok and tok not in tokens:
                tokens.append(tok)
        for tok in tokens:
            if tok not in resolved:
                resolved[tok] = resolve_token(tok)
        per_row.append(
            {
                "goa_row": i,
                "go_id": row["GO TERM"],
                "go_name": row["GO NAME"],
                "evidence": row["GO EVIDENCE CODE"],
                "reference": row["REFERENCE"],
                "raw_withfrom": wf,
                "supporting_entities": tokens,
            }
        )
        # Counts must match GOA by construction.
        assert len(tokens) == len(set(wf.split("|"))), (
            f"row {i}: token de-duplication changed the count ({tokens} vs {wf})"
        )

    fields = ["token", "kind", "accession", "entry_name", "gene", "protein",
              "organism", "reviewed", "length", "n_hits"]
    with (HERE / "withfrom_resolved.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        w.writeheader()
        for tok in sorted(resolved):
            w.writerow(resolved[tok])

    (HERE / "supporting_entities.json").write_text(json.dumps(per_row, indent=2) + "\n")

    print(f"GOA rows: {len(rows)}")
    print(f"GOA rows with a WITH/FROM: {len(per_row)}")
    print(f"distinct WITH/FROM tokens: {len(resolved)}")
    unresolved = [t for t, r in resolved.items() if r["protein"] == UNRESOLVED]
    print(f"unresolved tokens: {len(unresolved)} {unresolved}")
    multi = [(t, r["n_hits"]) for t, r in resolved.items()
             if r["n_hits"] not in {"", "0", "1"}]
    print(f"MOD ids with >1 UniProt hit (ambiguous, reported not collapsed): "
          f"{len(multi)} {multi}")
    trembl = [t for t, r in resolved.items() if r["reviewed"] == "TrEMBL"]
    print(f"TrEMBL (unreviewed) sources: {len(trembl)} {trembl}")


if __name__ == "__main__":
    main()
