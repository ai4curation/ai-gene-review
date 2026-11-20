import json, sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import rcpt, batcher
P = json.load(open(sys.argv[1]))
d = rcpt.load("papers"); items = []
for p in P:
    base = dict(title=p["title"], year=p["year"], journal=p["journal"], authors=p["authors"], doi=p["doi"],
                url=f"https://europepmc.org/article/MED/{p['id'][5:]}" if p["id"].startswith("PMID:") else (f"https://doi.org/{p['doi']}" if p["doi"] else None),
                found_by=p["queries"])
    if not p["abstract"] and not p["title"]:
        rcpt.put(d, p["id"], relevance=None, method="rule:no-metadata", rationale="No title or abstract returned.", **base); continue
    rcpt.put(d, p["id"], relevance=None, method="rule:pending", rationale="pending", **base)
    items.append((p["id"], f"# {p['title']}\n{p['authors']} ({p['year']}) {p['journal']} pubtype={p['pubtype']}\n\n"
                  + re.sub(r"<[^>]+>", "", p["abstract"] or "(no abstract)")))
rcpt.save(d, description="Receipts for candidate papers and book chapters on GO annotation practice, from Europe PMC "
          "queries (see found_by): GO/GO-annotation/GO-CAM in title; GO curation-guideline abstracts; ECO, PAINT and "
          "biocuration papers; the Gene Ontology Handbook (Methods Mol Biol 1446, 2017). Scored on title+abstract.")
print(batcher.write_batches(items, "papers/batches", "haiku", 100, 2500))
