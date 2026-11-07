import concurrent.futures
import json
from urllib.parse import urlencode
from acquire import get, P

queries = {
    "bacsu": "organism_id:224308 AND (gene:yrvO OR gene:mnmA)",
    "ecoli": "organism_id:83333 AND (gene:iscS OR gene:tusA OR gene:tusB OR gene:tusC OR gene:tusD OR gene:tusE OR gene:mnmA)",
    "thermus": "organism_id:274 AND (gene:mnmA OR gene:TTC1727 OR gene:iscS OR gene:sufS)",
}
jobs = [
    (
        "identity-" + k + ".json",
        "https://rest.uniprot.org/uniprotkb/search?"
        + urlencode({"query": v, "format": "json", "size": 100}),
    )
    for k, v in queries.items()
]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    out = list(pool.map(get, jobs))
(P / "identity-acquisition.json").write_text(json.dumps(out, indent=2) + "\n")
for k in queries:
    d = json.loads((P / ("identity-" + k + ".json")).read_text())
    for x in d.get("results", []):
        print(
            k,
            x["primaryAccession"],
            x["organism"],
            x.get("genes"),
            len(x["sequence"]["value"]),
            [
                (y["id"], y.get("properties"))
                for y in x["uniProtKBCrossReferences"]
                if y["database"] == "PANTHER"
            ],
        )
