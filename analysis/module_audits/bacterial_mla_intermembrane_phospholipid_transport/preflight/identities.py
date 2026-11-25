from pathlib import Path
import requests
import json
import hashlib
import concurrent.futures

P = Path(".cache/module-audit-logs/mla-preflight-20261107")
out = {}
queries = {str(n): f"(gene:BP{n}) AND (organism_id:257313)" for n in range(3757, 3762)}
queries["B213"] = '(organism_name:"Bordetella pertussis") AND (strain:B213)'
queries["PA4453"] = "accession:Q9HVW4"
queries["N_mlaA"] = "(gene:mlaA) AND (organism_id:242231)"


def fetch(item):
    key, q = item
    u = "https://rest.uniprot.org/uniprotkb/search"
    r = requests.get(u, params={"query": q, "format": "json", "size": 100}, timeout=45)
    f = P / ("uniprot-" + key + ".json")
    f.write_bytes(r.content)
    return key, {
        "url": r.url,
        "status": r.status_code,
        "path": str(f),
        "sha256": hashlib.sha256(r.content).hexdigest(),
        "entries": [
            {
                k: x.get(k)
                for k in [
                    "primaryAccession",
                    "uniProtkbId",
                    "organism",
                    "genes",
                    "sequence",
                ]
            }
            for x in r.json().get("results", [])
        ],
    }


for k, v in concurrent.futures.ThreadPoolExecutor(max_workers=3).map(
    fetch, queries.items()
):
    out[k] = v
u = "https://data.rcsb.org/rest/v1/core/polymer_entity/6HSY/1"
r = requests.get(u, timeout=45)
f = P / "6HSY-entity1.json"
f.write_bytes(r.content)
out["6HSY"] = {
    "url": u,
    "status": r.status_code,
    "path": str(f),
    "sha256": hashlib.sha256(r.content).hexdigest(),
}
(P / "identity-source-access.json").write_text(json.dumps(out, indent=2) + "\n")
print(
    json.dumps(
        {
            k: [
                (x.get("primaryAccession"), x.get("uniProtkbId"), x.get("genes"))
                for x in v.get("entries", [])
            ]
            for k, v in out.items()
        },
        indent=2,
    )
)
