import concurrent.futures
import json
import subprocess
from urllib.parse import urlencode
from acquire import get, P

jobs = [
    (
        "identity-thermus-donors.json",
        "https://rest.uniprot.org/uniprotkb/search?"
        + urlencode(
            {
                "query": 'organism_id:262724 AND (gene:TT_C0087 OR gene:TT_C1373 OR protein_name:"cysteine desulfurase")',
                "format": "json",
                "size": 100,
            }
        ),
    ),
    ("16547008-publisher.pdf", "https://www.jbc.org/article/S0021925820780750/pdf"),
    ("2024-counterclaim.html.gz", "https://www.mdpi.com/2304-6740/12/3/67"),
    (
        "33885822-metadata.json",
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
        + urlencode(
            {
                "query": "EXT_ID:33885822 AND SRC:MED",
                "format": "json",
                "resultType": "core",
            }
        ),
    ),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(get, jobs))
(P / "followup-acquisition.json").write_text(json.dumps(results, indent=2) + "\n")
for pr in json.loads((P / "expanded-overlap.json").read_text())["hits"]:
    n = pr["number"]
    meta = subprocess.check_output(
        ["gh", "api", f"repos/ai4curation/ai-gene-review/pulls/{n}"]
    )
    (P / f"PR{n}-metadata.json").write_bytes(meta)
    for path in pr["overlap"]:
        d = subprocess.check_output(
            [
                "gh",
                "api",
                f"repos/ai4curation/ai-gene-review/contents/{path}?ref={pr['headRefOid']}",
                "-H",
                "Accept: application/vnd.github.raw+json",
            ]
        )
        (P / f"PR{n}-{path.split('/')[-1]}").write_bytes(d)
print(results)
