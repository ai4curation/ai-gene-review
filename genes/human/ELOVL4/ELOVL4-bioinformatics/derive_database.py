"""Saved-only ELOVL4 provenance projections; no network or source writes."""

from pathlib import Path
import json, re, hashlib, csv, collections

O = Path(__file__).resolve().parent
E = O / "owner-evidence-v1"
J = lambda p: json.loads(p.read_text())


def paragraphs(p):
    s = p.read_text()
    return [
        {"index": i, "start_line": s[: m.start()].count("\n") + 1, "text": m.group()}
        for i, m in enumerate(re.finditer(r"[^\n].*?(?=\n\n|\Z)", s, flags=re.S))
    ]


def derive():
    joins = J(O / "bootstrap-v1/source-joins.json")
    raw = E / "raw"
    target = J(O / "intake-v1/raw/UniProt-Q9GZR5.json")
    all_mitab = []
    for line, s in enumerate((raw / "IntAct-Q9GZR5.tsv").read_text().splitlines(), 1):
        if s.startswith("#") or not s.strip():
            continue
        f = s.split("\t")
        if len(f) != 42:
            raise ValueError("Unexpected MITAB width")
        all_mitab.append({"line": line, "fields": f})
    huri = [x for x in all_mitab if "pubmed:32296183" in x["fields"][8]]
    expected = sorted({x for xs in joins[18]["current_support_lists"] for x in xs})
    partner_rows = []
    for partner in expected:
        acc = partner.split(":", 1)[-1]
        hits = [
            x
            for x in huri
            if set(x["fields"][:2]) == {"uniprotkb:Q9GZR5", "uniprotkb:" + acc}
        ]
        if not hits:
            raise ValueError("Unverified imported partner " + partner)
        if any(x["fields"][35].lower() != "false" for x in hits):
            raise ValueError("Negative interaction")
        partner_rows.append({"partner": partner, "records": hits})
    all_pairs = sorted({tuple(sorted(x["fields"][:2])) for x in huri})
    huri_projection = {
        "source_index": 18,
        "all_query_records": len(all_mitab),
        "publication_records": len(huri),
        "publication_pairs": all_pairs,
        "method_counts": dict(collections.Counter(x["fields"][6] for x in huri)),
        "imported_partner_count": len(expected),
        "imported_pairs": partner_rows,
        "unimported_pairs": [
            list(p)
            for p in all_pairs
            if not any("uniprotkb:" + x.split(":", 1)[-1] in p for x in expected)
        ],
        "other_publications": dict(
            collections.Counter(x["fields"][8] for x in all_mitab if x not in huri)
        ),
        "scope": "The three curated method records per pair are not three independent biological validations. No per-pair MAPPIT/GPCA confirmation or present-day insert equivalence is inferred.",
    }
    donor_projection = []
    terms = {x["source"]["term"]["id"] for x in joins}
    for acc in ["Q9EQC4", "Q9BW60", "D4ACH5"]:
        j = J(raw / f"QuickGO-{acc}-page1.json")
        rows = j["results"]
        if len(rows) != j["numberOfHits"]:
            raise ValueError("Incomplete donor page")
        for n, r in enumerate(rows):
            if r["goId"] in terms and r["goEvidence"] in [
                "EXP",
                "IDA",
                "IPI",
                "IMP",
                "IGI",
                "IEP",
            ]:
                donor_projection.append({"accession": acc, "raw_index": n, "record": r})
    memberships = {}
    for x in target["uniProtKBCrossReferences"]:
        memberships.setdefault(x["database"], []).append(x["id"])
        if x["database"] == "PANTHER":
            memberships["PANTHER"] += [
                p["value"]
                for p in x.get("properties", [])
                if p["value"].startswith("PTHR")
            ]
    lineage = set(target["organism"]["lineage"]) | {
        target["organism"]["scientificName"]
    }
    rules = []
    for ident in ["ARBA00028259", "ARBA00028685", "UR000254926"]:
        obj = J(raw / (ident + ".json"))
        sets = []
        for si, cs in enumerate(obj["mainRule"]["conditionSets"]):
            cond = []
            for c in cs["conditions"]:
                typ = c["type"]
                vs = [v["value"] for v in c.get("conditionValues", [])]
                db = {
                    "InterPro id": "InterPro",
                    "PANTHER id": "PANTHER",
                    "HAMAP id": "HAMAP",
                }.get(typ)
                if typ == "taxon":
                    status = any(v in lineage for v in vs)
                elif db:
                    status = any(v in memberships.get(db, []) for v in vs)
                elif typ == "fragment":
                    status = bool(
                        target["proteinDescription"].get("flag") == "Fragment"
                    )
                else:
                    status = None
                if c.get("isNegative") and status is not None:
                    status = not status
                cond.append({"condition": c, "matches_saved_target": status})
            statuses = [c["matches_saved_target"] for c in cond]
            matched = False if False in statuses else None if None in statuses else True
            sets.append({"index": si, "conditions": cond, "satisfied": matched})
        rules.append(
            {
                "id": ident,
                "modifiedDate": obj.get("modifiedDate"),
                "condition_sets": sets,
                "matching_set_indices": [
                    x["index"] for x in sets if x["satisfied"] is True
                ],
                "unknown_set_indices": [
                    x["index"] for x in sets if x["satisfied"] is None
                ],
                "GO_outputs": [
                    a["dbReference"]["id"]
                    for a in obj["mainRule"]["annotations"]
                    if a.get("dbReference", {}).get("database") == "GO"
                ],
            }
        )
    term_projection = {}
    for name in [
        "GO35338-ancestors.json",
        "GO34626-ancestors.json",
        "GO42761-ancestors.json",
        "GO19367-ancestors.json",
        "GO0005789-ancestors.json",
    ]:
        r = J(raw / name)["results"][0]
        term_projection[r["id"]] = {
            "name": r["name"],
            "definition": r["definition"]["text"],
            "ancestors": r["ancestors"],
            "raw": name,
        }
    return {
        "huri": huri_projection,
        "donor_records": donor_projection,
        "target_memberships": memberships,
        "target_lineage": sorted(lineage),
        "rules": rules,
        "term_relations": term_projection,
    }
