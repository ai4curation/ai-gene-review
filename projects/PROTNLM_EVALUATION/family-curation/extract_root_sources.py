import json
import pathlib
import gzip
import yaml
import html
import re

R = pathlib.Path.cwd()
B = R / "projects/PROTNLM_EVALUATION/family-curation"
G = json.loads((B / "family-groups.json").read_text())
A = json.loads((B / "assignments.json").read_text())["root"]
U = {}
for f in ("uniprot-records.jsonl.gz", "uniprot-retries.jsonl.gz"):
    for line in gzip.open(B / f, "rt"):
        x = json.loads(line)
        if x["status"] == 200:
            U[x["accession"]] = x["record"]
for fam in A:
    src = json.loads((B / "family-sources" / f"{fam}.json").read_text())
    m = src.get("interpro", {}).get("metadata", {})
    lines = [
        f"# {fam}: source excerpts",
        "",
        f"Raw provenance: [family snapshot](family-sources/{fam}.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).",
        "",
        f"## Integrated InterPro {m.get('accession', 'unavailable')}",
        "",
        f"Generated description flag: {m.get('is_llm')}; reviewed generated text flag: {m.get('is_reviewed_llm')}. Generated prose is a source lead, not independent biological validation.",
        "",
    ]
    for d in m.get("description", []):
        if isinstance(d, dict):
            lines.append(html.unescape(re.sub("<[^>]+>", "", d["text"])))
    lines += ["", "## Exact benchmark records", ""]
    print("\n" + fam)
    for row in G[fam]:
        u = U[row["accession"]]
        a = u["primaryAccession"]
        p = R / row["gene_review"]
        print(
            row["gene_symbol"],
            a,
            u["sequence"]["length"],
            [
                x["id"]
                for x in u.get("uniProtKBCrossReferences", [])
                if x["database"] == "PANTHER"
            ],
        )
        lines += [
            f"### {row['species']}/{row['gene_symbol']} — {a}",
            f"UniProt record: https://www.uniprot.org/uniprotkb/{a}/entry",
            f"Status: {u['entryType']}; length: {u['sequence']['length']} aa; sequence version: {u['entryAudit']['sequenceVersion']}.",
            "",
        ]
        for c in u.get("comments", []):
            if c["commentType"] not in [
                "FUNCTION",
                "CATALYTIC ACTIVITY",
                "CAUTION",
                "SIMILARITY",
                "SUBCELLULAR LOCATION",
            ]:
                continue
            lines.append(f"**{c['commentType']}**")
            for t in c.get("texts", []):
                lines.append(t["value"])
                lines.append(
                    "Evidence: "
                    + json.dumps(t.get("evidences", []), ensure_ascii=False)
                )
            if "reaction" in c:
                lines.append(json.dumps(c["reaction"], ensure_ascii=False))
            for t in c.get("subcellularLocations", []):
                lines.append(json.dumps(t, ensure_ascii=False))
        for x in u.get("uniProtKBCrossReferences", []):
            if x["database"] in ["InterPro", "Pfam", "PANTHER"]:
                lines.append(
                    x["database"]
                    + ": "
                    + x["id"]
                    + " "
                    + json.dumps(x.get("properties", []))
                )
        if p.is_file():
            for pf in p.parent.glob("*protnlm-predictions-review.yaml"):
                d = yaml.safe_load(pf.read_text())
                print(
                    "GO",
                    [
                        (x.get("predicted_term"), x.get("review", {}).get("assessment"))
                        for x in d.get("predictions", [])
                        if x.get("predicted_term", {}).get("id", "").startswith("GO:")
                    ],
                )
            d = yaml.safe_load(p.read_text())
            print(
                "CORE",
                [x.get("molecular_function") for x in d.get("core_functions", [])],
            )
        lines += [""]
    (B / f"{fam}-evidence.md").write_text("\n".join(lines) + "\n")
