"""Resolve every WITH/FROM identifier in the AGT GOA file.

Two outputs:

1. `withfrom_resolved.tsv` - one row per (GOA row, WITH/FROM token), with the
   token resolved to a UniProt accession, gene symbol, organism and MEROPS id
   where such a resolution exists.
2. `supporting_entities.yaml` - the `supporting_entities` list for every GOA row
   that has a WITH/FROM, keyed by (GO id, evidence, reference, raw with/from) so
   the review YAML can be filled mechanically rather than by hand.

Run: uv run python resolve_withfrom.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from uniprot import resolve_mod_id, summarise, uniprot_entry

GOA = Path(__file__).parent.parent / "AGT-goa.tsv"
OUT = Path(__file__).parent


def load_goa() -> list[dict[str, str]]:
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def resolve_token(token: str) -> dict[str, str]:
    """Resolve one WITH/FROM token to a described entity."""
    db, _, _local = token.partition(":")
    if db == "UniProtKB":
        acc = token.split(":", 1)[1]
        s = summarise(uniprot_entry(acc))
        return {
            "token": token,
            "kind": "protein",
            "accession": s["accession"],
            "gene": s["gene"],
            "protein": s["protein"],
            "organism": s["organism"],
            "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "merops": ";".join(s["merops"]),
            "n_hits": "1",
        }
    if db in {"MGI", "RGD", "FB", "ZFIN", "AGI_LocusCode"}:
        hits = resolve_mod_id(token)
        if not hits:
            return {"token": token, "kind": "mod-id", "accession": "", "gene": "",
                    "protein": "UNRESOLVED", "organism": "", "reviewed": "",
                    "merops": "", "n_hits": "0"}
        # Prefer a reviewed (Swiss-Prot) hit when the MOD id maps to several.
        reviewed = [h for h in hits if h.get("entryType", "").startswith("UniProtKB reviewed")]
        best = (reviewed or hits)[0]
        s = summarise(uniprot_entry(best["primaryAccession"]))
        return {
            "token": token,
            "kind": "mod-id",
            "accession": s["accession"],
            "gene": s["gene"],
            "protein": s["protein"],
            "organism": s["organism"],
            "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "merops": ";".join(s["merops"]),
            "n_hits": str(len(hits)),
        }
    if db == "PANTHER":
        return {"token": token, "kind": "panther-node", "accession": "", "gene": "",
                "protein": "PAINT ancestral node", "organism": "", "reviewed": "",
                "merops": "", "n_hits": ""}
    if db in {"InterPro", "UniProtKB-SubCell", "GO", "ARBA"}:
        return {"token": token, "kind": db.lower(), "accession": "", "gene": "",
                "protein": "", "organism": "", "reviewed": "", "merops": "", "n_hits": ""}
    raise ValueError(f"unhandled WITH/FROM database {db!r} in token {token!r}")


def main() -> None:
    rows = load_goa()
    resolved: dict[str, dict[str, str]] = {}
    per_row = []
    for i, row in enumerate(rows, start=1):
        wf = row["WITH/FROM"].strip()
        if not wf:
            continue
        tokens = []
        for tok in wf.split("|"):
            tok = tok.strip()
            if not tok or tok in tokens:
                continue
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
                "qualifier": row["QUALIFIER"],
                "supporting_entities": tokens,
            }
        )

    with (OUT / "withfrom_resolved.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            delimiter="\t",
            fieldnames=["token", "kind", "accession", "gene", "protein", "organism",
                        "reviewed", "merops", "n_hits"],
        )
        w.writeheader()
        for tok in sorted(resolved):
            w.writerow(resolved[tok])

    (OUT / "supporting_entities.json").write_text(json.dumps(per_row, indent=2))

    print(f"GOA rows with a WITH/FROM: {len(per_row)}")
    print(f"distinct WITH/FROM tokens: {len(resolved)}")
    unresolved = [t for t, r in resolved.items() if r["protein"] == "UNRESOLVED"]
    print(f"unresolved tokens: {len(unresolved)} {unresolved}")
    multi = [(t, r['n_hits']) for t, r in resolved.items() if r["n_hits"] not in {"", "0", "1"}]
    print(f"MOD ids with >1 UniProt hit: {len(multi)} {multi}")


if __name__ == "__main__":
    main()
