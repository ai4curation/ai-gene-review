from pathlib import Path
import urllib.request
import json
import hashlib
import datetime
import concurrent.futures
from bs4 import BeautifulSoup

w = Path("/private/tmp/aigr-nitrogen-pts-taxon-audit")
c = (
    w
    / "analysis/module_audits/bacterial_nitrogen_regulatory_pts/literature-acquisition-20261107"
)
items = [
    ("18296519", "PMC2347394"),
    ("17416664", "PMC1913348"),
    ("24633875", "PMC4011000"),
]


def get(x):
    pmid, pmc = x
    u = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/"
    try:
        with urllib.request.urlopen(u, timeout=25) as f:
            b = f.read()
        soup = BeautifulSoup(b, "html.parser")
        article = soup.find("main", id="main-content")
        assert article is not None, "No main-content element; not accepted as full text"
        for n in article.select("script,style"):
            n.decompose()
        t = article.get_text("\n", strip=True)
        assert "METHODS" in t.upper() and len(t) > 10000, "Missing substantive body"
        return (
            pmid,
            {
                "url": u,
                "status": 200,
                "fulltext": True,
                "observed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "raw_sha256": hashlib.sha256(b).hexdigest(),
            },
            b,
            t,
        )
    except Exception as e:
        return pmid, {"url": u, "error": str(e), "fulltext": False}, None, None


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    r = list(pool.map(get, items))
for pmid, d, b, t in r:
    if b:
        (c / f"PMID_{pmid}-pmc-body.html").write_bytes(b)
        (c / f"PMID_{pmid}-pmc-body.txt").write_text(t + "\n")
        d["text_sha256"] = hashlib.sha256((t + "\n").encode()).hexdigest()
        d["extraction"] = (
            "BeautifulSoup main#main-content element get_text newline strip; script/style removed; raw retained"
        )
    (c / f"PMID_{pmid}-pmc-body-retrieval.json").write_text(
        json.dumps(d, indent=2) + "\n"
    )
    print(pmid, json.dumps(d), flush=True)
