"""Resolve every WITH/FROM identifier in the ARFGEF1 GOA file.

Three outputs:

1. `withfrom_resolved.tsv` - one row per distinct WITH/FROM token, resolved to a
   UniProt accession, gene symbol, organism and Swiss-Prot/TrEMBL status where
   such a resolution exists, plus the strategy used to resolve it.
2. `supporting_entities.json` - the token list for every GOA row that has a
   WITH/FROM, keyed by GOA row number, so `supporting_entities` in the review
   YAML is built FROM the GOA field rather than by hand.
3. `donor_evidence.tsv` - for every (IBA/ISS/IEA-from-ortholog row, protein
   donor) pair, the evidence codes that donor itself carries for the propagated
   GO term (descendants included). "This donor only carries the same
   family-level inference" is a testable claim, not a safe hedge.

Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/resolve_withfrom.py
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from uniprot import (  # noqa: E402
    quickgo_annotations,
    resolve_mod_id,
    summarise,
    uniprot_entry,
)

HERE = Path(__file__).parent
GOA = HERE.parent / "ARFGEF1-goa.tsv"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
# Evidence codes whose WITH/FROM names a donor entity rather than a signature.
DONOR_CODES = {"IBA", "ISS", "ISO", "IEA"}


def load_goa() -> list[dict[str, str]]:
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def resolve_token(token: str) -> dict[str, str]:
    """Resolve one WITH/FROM token to a described entity."""
    db, _, _local = token.partition(":")
    if db == "UniProtKB":
        acc = token.split(":", 1)[1]
        s = summarise(uniprot_entry(acc))
        if not s["gene"] and not s["protein"]:
            raise ValueError(
                f"{token} resolved to an entry with no gene and no protein name "
                "- a deleted/inactive accession reads as 'carries no annotation'. "
                "Check the accession is live."
            )
        return {
            "token": token,
            "kind": "protein",
            "accession": s["accession"],
            "entry_name": s["id"],
            "gene": s["gene"],
            "protein": s["protein"],
            "organism": s["organism"],
            "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "length": str(s["length"]),
            "n_hits": "1",
            "resolved_by": "direct accession",
        }
    if db in {"MGI", "RGD", "FB", "ZFIN", "AGI_LocusCode", "SGD", "PomBase", "dictyBase", "WB"}:
        hits, how = resolve_mod_id(token)
        if not hits:
            return {"token": token, "kind": "mod-id", "accession": "", "entry_name": "",
                    "gene": "", "protein": "UNRESOLVED", "organism": "", "reviewed": "",
                    "length": "", "n_hits": "0", "resolved_by": how}
        # Prefer a reviewed (Swiss-Prot) hit when the MOD id maps to several, but
        # report the hit count so the ambiguity stays visible.
        reviewed = [h for h in hits if h.get("entryType", "").startswith("UniProtKB reviewed")]
        best = (reviewed or hits)[0]
        s = summarise(uniprot_entry(best["primaryAccession"]))
        return {
            "token": token,
            "kind": "mod-id",
            "accession": s["accession"],
            "entry_name": s["id"],
            "gene": s["gene"],
            "protein": s["protein"],
            "organism": s["organism"],
            "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "length": str(s["length"]),
            "n_hits": str(len(hits)),
            "resolved_by": how,
        }
    if db == "PANTHER":
        return {"token": token, "kind": "panther-node", "accession": "", "entry_name": "",
                "gene": "", "protein": "PAINT ancestral node (not a protein)", "organism": "",
                "reviewed": "", "length": "", "n_hits": "", "resolved_by": "n/a"}
    if db in {"InterPro", "UniProtKB-SubCell", "GO", "ARBA", "ensembl"}:
        return {"token": token, "kind": db.lower(), "accession": "", "entry_name": "",
                "gene": "", "protein": "", "organism": "", "reviewed": "",
                "length": "", "n_hits": "", "resolved_by": "n/a"}
    raise ValueError(f"unhandled WITH/FROM database {db!r} in token {token!r}")


def donor_evidence(accession: str, go_id: str) -> dict[str, object]:
    """Evidence codes the donor itself carries for `go_id` (descendants included)."""
    data = quickgo_annotations(
        geneProductId=f"UniProtKB:{accession}",
        goId=go_id,
        goUsage="descendants",
        goUsageRelationships="is_a,part_of",
        limit="100",
    )
    codes: dict[str, int] = {}
    terms: set[str] = set()
    for r in data.get("results", []):
        codes[r["goEvidence"]] = codes.get(r["goEvidence"], 0) + 1
        terms.add(r["goId"])
    return {
        "codes": codes,
        "terms": sorted(terms),
        "has_experimental": bool(EXPERIMENTAL & set(codes)),
        "truncated": data["_truncated"],
        "n_hits": data.get("numberOfHits", 0),
    }


def main() -> None:
    rows = load_goa()
    resolved: dict[str, dict[str, str]] = {}
    per_row = []
    for i, row in enumerate(rows, start=1):
        wf = row["WITH/FROM"].strip()
        if not wf:
            continue
        tokens: list[str] = []
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

    fields = ["token", "kind", "accession", "entry_name", "gene", "protein", "organism",
              "reviewed", "length", "n_hits", "resolved_by"]
    with (HERE / "withfrom_resolved.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        w.writeheader()
        for tok in sorted(resolved):
            w.writerow(resolved[tok])

    (HERE / "supporting_entities.json").write_text(json.dumps(per_row, indent=2) + "\n")

    # --- donor evidence, for propagated rows only -------------------------
    donor_rows = []
    for entry in per_row:
        if entry["evidence"] not in DONOR_CODES:
            continue
        for tok in entry["supporting_entities"]:
            r = resolved[tok]
            if r["kind"] not in {"protein", "mod-id"} or not r["accession"]:
                continue
            ev = donor_evidence(r["accession"], entry["go_id"])
            donor_rows.append({
                "goa_row": entry["goa_row"],
                "go_id": entry["go_id"],
                "evidence": entry["evidence"],
                "token": tok,
                "accession": r["accession"],
                "gene": r["gene"],
                "organism": r["organism"],
                "reviewed": r["reviewed"],
                "donor_codes": ";".join(f"{k}x{v}" for k, v in sorted(ev["codes"].items())) or "NONE",
                "donor_terms": ";".join(ev["terms"]),
                "donor_has_experimental": str(ev["has_experimental"]),
                "quickgo_truncated": str(ev["truncated"]),
            })
    dfields = ["goa_row", "go_id", "evidence", "token", "accession", "gene", "organism",
               "reviewed", "donor_codes", "donor_terms", "donor_has_experimental",
               "quickgo_truncated"]
    with (HERE / "donor_evidence.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=dfields)
        w.writeheader()
        w.writerows(donor_rows)

    print(f"GOA rows total: {len(rows)}")
    print(f"GOA rows with a WITH/FROM: {len(per_row)}")
    print(f"distinct WITH/FROM tokens: {len(resolved)}")
    unresolved = [t for t, r in resolved.items() if r["protein"] == "UNRESOLVED"]
    print(f"unresolved tokens: {len(unresolved)} {unresolved}")
    multi = [(t, r["n_hits"]) for t, r in resolved.items() if r["n_hits"] not in {"", "0", "1"}]
    print(f"MOD ids with >1 UniProt hit: {len(multi)} {multi}")
    prot = [r for r in resolved.values() if r["kind"] in {"protein", "mod-id"} and r["accession"]]
    n_rev = sum(1 for r in prot if r["reviewed"] == "Swiss-Prot")
    print(f"protein donors: {len(prot)} ({n_rev} Swiss-Prot, {len(prot) - n_rev} TrEMBL)")
    assert n_rev <= len(prot)
    n_exp = sum(1 for r in donor_rows if r["donor_has_experimental"] == "True")
    print(f"donor-term pairs: {len(donor_rows)}; with own experimental evidence: {n_exp}")
    trunc = [r for r in donor_rows if r["quickgo_truncated"] == "True"]
    if trunc:
        print(f"WARNING: {len(trunc)} QuickGO donor queries were truncated")


if __name__ == "__main__":
    main()
