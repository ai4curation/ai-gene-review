"""Resolve every WITH/FROM identifier in the ARFGEF3 GOA file, and ask what
evidence each donor itself carries for the term it is donating.

Three outputs:

1. `withfrom_resolved.tsv` - one row per distinct WITH/FROM token, resolved to a
   UniProt accession, gene symbol, organism, Swiss-Prot/TrEMBL status, InterPro
   domain content and how the resolution was obtained.
2. `donor_evidence.tsv` - for every protein donor on every IBA row, the donor's
   own GO annotations to the donated term (or a descendant) with evidence codes.
   "This donor only carries the same family-level inference" is a testable
   claim; IBA WITH/FROM lists experimentally-annotated members by construction,
   so it is usually false.
3. `supporting_entities.json` - the `supporting_entities` list for every GOA row
   that has a WITH/FROM, built FROM the GOA field so the review YAML can be
   filled mechanically. Hand-maintained lists have drifted on every gene in this
   campaign that tried it.

Run: uv run python resolve_withfrom.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from uniprot import quickgo_annotations, resolve_mod_id, summarise, uniprot_entry

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ARFGEF3-goa.tsv"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}


def load_goa() -> list[dict[str, str]]:
    if not GOA.exists():
        raise FileNotFoundError(
            f"{GOA} is missing. Regenerate it with: just fetch-gene human ARFGEF3"
        )
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def _interpro_ids(entry: dict) -> list[str]:
    return [x["id"] for x in entry.get("uniProtKBCrossReferences", [])
            if x["database"] == "InterPro"]


def _panther_ids(entry: dict) -> list[str]:
    return [x["id"] for x in entry.get("uniProtKBCrossReferences", [])
            if x["database"] == "PANTHER"]


def _row(token: str, kind: str, **kw) -> dict[str, str]:
    base = {"token": token, "kind": kind, "accession": "", "entry_name": "",
            "gene": "", "protein": "", "organism": "", "reviewed": "",
            "length": "", "has_sec7_interpro": "", "panther": "",
            "n_hits": "", "resolved_by": ""}
    base.update({k: str(v) for k, v in kw.items()})
    return base


# IPR000904 is the Sec7 domain signature; its presence is what a
# "guanyl-nucleotide exchange factor activity" propagation is riding on.
SEC7_INTERPRO = "IPR000904"


def describe_entry(token: str, kind: str, entry: dict, n_hits: int,
                   resolved_by: str) -> dict[str, str]:
    s = summarise(entry)
    # An accession that returns no name is a DELETED entry, not a protein with
    # nothing to say. Fail loudly rather than emit a silent, vacuous zero.
    if not s["organism"]:
        raise RuntimeError(
            f"{token} -> {s['accession']} returned no organism: the accession is "
            "probably a deleted UniProt entry. Do not treat this as 'no data'."
        )
    return _row(
        token, kind,
        accession=s["accession"], entry_name=s["id"], gene=s["gene"],
        protein=s["protein"], organism=s["organism"],
        reviewed="Swiss-Prot" if s["reviewed"] else "TrEMBL",
        length=s["length"] or "",
        has_sec7_interpro="yes" if SEC7_INTERPRO in _interpro_ids(entry) else "no",
        panther=";".join(_panther_ids(entry)),
        n_hits=n_hits, resolved_by=resolved_by,
    )


def resolve_token(token: str) -> dict[str, str]:
    db, _, _local = token.partition(":")
    if db == "UniProtKB":
        acc = token.split(":", 1)[1]
        return describe_entry(token, "protein", uniprot_entry(acc), 1,
                              f"direct accession {acc}")
    if db == "PANTHER":
        # A PTN id is an internal ancestral tree node, not a protein.
        # "not a protein" and "unresolvable" are different facts.
        return _row(token, "panther-node", protein="PAINT ancestral node")
    if db in {"MGI", "RGD", "FB", "ZFIN", "AGI_LocusCode",
              "SGD", "PomBase", "dictyBase", "WB"}:
        hits, how = resolve_mod_id(token)
        if not hits:
            return _row(token, "mod-id", protein="UNRESOLVED", n_hits=0,
                        resolved_by=how)
        reviewed = [h for h in hits
                    if h.get("entryType", "").startswith("UniProtKB reviewed")]
        best = (reviewed or hits)[0]
        return describe_entry(token, "mod-id",
                              uniprot_entry(best["primaryAccession"]),
                              len(hits), how)
    if db in {"InterPro", "UniProtKB-SubCell", "GO", "ARBA"}:
        return _row(token, db.lower())
    raise ValueError(f"unhandled WITH/FROM database {db!r} in token {token!r}")


def main() -> None:
    rows = load_goa()
    resolved: dict[str, dict[str, str]] = {}
    per_row: list[dict] = []

    for i, row in enumerate(rows, start=1):
        wf = row["WITH/FROM"].strip()
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
        # Built FROM the GOA field, so the review YAML's supporting_entities
        # cannot drift from GOA. Assert the reconstruction round-trips.
        assert "|".join(tokens) == "|".join(
            dict.fromkeys(t.strip() for t in wf.split("|") if t.strip())
        ), f"token list does not reproduce GOA WITH/FROM on row {i}"
        per_row.append({
            "goa_row": i,
            "go_id": row["GO TERM"],
            "go_name": row["GO NAME"],
            "evidence": row["GO EVIDENCE CODE"],
            "reference": row["REFERENCE"],
            "supporting_entities": tokens,
        })

    fields = list(_row("", "").keys())
    with (HERE / "withfrom_resolved.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        w.writeheader()
        for tok in sorted(resolved):
            w.writerow(resolved[tok])

    # Donor-evidence query: what does each protein donor itself hold for the
    # term it is donating?
    donor_rows: list[dict[str, str]] = []
    for pr in per_row:
        if pr["evidence"] != "IBA":
            continue
        for tok in pr["supporting_entities"]:
            r = resolved[tok]
            if not r["accession"]:
                continue
            anns = quickgo_annotations(r["accession"], pr["go_id"])
            codes = sorted({a["goEvidence"] for a in anns})
            terms = sorted({a["goId"] for a in anns})
            donor_rows.append({
                "go_id": pr["go_id"],
                "token": tok,
                "accession": r["accession"],
                "gene": r["gene"],
                "organism": r["organism"],
                "reviewed": r["reviewed"],
                "n_annotations": str(len(anns)),
                "evidence_codes": ";".join(codes),
                "terms_held": ";".join(terms),
                "has_own_experimental": "yes" if set(codes) & EXPERIMENTAL else "no",
            })

    with (HERE / "donor_evidence.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(donor_rows[0].keys()))
        w.writeheader()
        w.writerows(donor_rows)

    (HERE / "supporting_entities.json").write_text(json.dumps(per_row, indent=2))

    print(f"GOA rows: {len(rows)}")
    print(f"GOA rows with a WITH/FROM: {len(per_row)}")
    print(f"distinct WITH/FROM tokens: {len(resolved)}")
    unresolved = [t for t, r in resolved.items() if r["protein"] == "UNRESOLVED"]
    print(f"unresolved tokens: {len(unresolved)} {unresolved}")
    multi = [(t, r["n_hits"]) for t, r in resolved.items()
             if r["n_hits"] not in {"", "0", "1"}]
    print(f"MOD ids with >1 UniProt hit: {len(multi)} {multi}")
    fallback = [t for t, r in resolved.items() if r["resolved_by"].startswith("FALLBACK")]
    print(f"tokens resolved only by free-text fallback: {len(fallback)} {fallback}")

    prot = [r for r in resolved.values() if r["accession"]]
    swiss = [r for r in prot if r["reviewed"] == "Swiss-Prot"]
    # "reviewed" is a substring of "unreviewed"; summarise() uses startswith,
    # and this assertion is what makes a 100%-reviewed count visible if it lies.
    assert len(swiss) <= len(prot)
    print(f"protein donors: {len(prot)} ({len(swiss)} Swiss-Prot, "
          f"{len(prot) - len(swiss)} TrEMBL)")
    sec7 = [r for r in prot if r["has_sec7_interpro"] == "yes"]
    print(f"protein donors carrying InterPro {SEC7_INTERPRO} (Sec7): {len(sec7)}/{len(prot)}")
    own = [d for d in donor_rows if d["has_own_experimental"] == "yes"]
    print(f"IBA donor rows whose donor holds its own experimental evidence: "
          f"{len(own)}/{len(donor_rows)}")


if __name__ == "__main__":
    main()
