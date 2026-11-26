# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Homology and family check for NCU04937 (Q7S3T0).

1. Report InterPro/PANTHER matches for Q7S3T0 (InterPro REST API).
2. BLASTP (EBI ncbiblast, UniProtKB, no low-complexity filter) of the
   sequence with the polyglutamine tract collapsed to 10 Q, so that hits
   reflect the non-repetitive flanks rather than the poly-Q run.
Writes results-rereview.json next to this script.
"""

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ACC = "Q7S3T0"
HERE = Path(__file__).parent
EBI = "https://www.ebi.ac.uk/Tools/services/rest/ncbiblast"


def get(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def main() -> None:
    seq = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{ACC}.json"))["sequence"]["value"]
    qrun = max(re.findall(r"Q+", seq), key=len)
    collapsed = seq.replace(qrun, "Q" * 10, 1)

    ipr = json.loads(get(f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{ACC}"))
    matches = []
    for res in ipr["results"]:
        for p in res["proteins"]:
            for loc in p["entry_protein_locations"]:
                matches.append({
                    "entry": res["metadata"]["accession"],
                    "name": res["metadata"]["name"],
                    "db": res["metadata"]["source_database"],
                    "model": loc.get("model"),
                    "score": loc.get("score"),
                    "subfamily": (loc.get("subfamily") or {}).get("accession"),
                    "subfamily_name": (loc.get("subfamily") or {}).get("name"),
                    "fragments": [(f["start"], f["end"]) for f in loc["fragments"]],
                })

    data = urllib.parse.urlencode({
        "email": "cmungall@gmail.com", "program": "blastp", "database": "uniprotkb",
        "stype": "protein", "filter": "F", "exp": "10", "alignments": "20", "scores": "20",
        "sequence": f">{ACC}_polyQcollapsed\n{collapsed}",
    }).encode()
    job = urllib.request.urlopen(urllib.request.Request(f"{EBI}/run", data=data)).read().decode()
    while get(f"{EBI}/status/{job}") not in ("FINISHED", "ERROR", "FAILURE"):
        time.sleep(10)
    out = get(f"{EBI}/result/{job}/out")
    hits = []
    block = out.split("Sequences producing significant alignments:")[1].split("\n>")[0]
    for line in block.strip().splitlines()[1:]:
        m = re.match(r"(\S+)\s+(\S+)\s+(.*?)\s+([\d.]+)\s+(\S+)$", line.strip())
        if m:
            hits.append({"id": m.group(1), "entry": m.group(2), "desc": m.group(3),
                         "bits": float(m.group(4)), "evalue": m.group(5)})

    result = {
        "accession": ACC, "length": len(seq), "polyQ_length": len(qrun),
        "polyQ_start": seq.index(qrun) + 1, "query_collapsed": collapsed,
        "interpro_matches": matches, "blast_job": job, "blast_hits": hits,
    }
    (HERE / "results-rereview.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
