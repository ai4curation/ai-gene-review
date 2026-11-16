"""Write full text of every receipt with relevance>=3 into corpus/<source>/<slug>.md, plus corpus/index.tsv."""
import json, re, pathlib, yaml, os, collections
S = pathlib.Path(__file__).parent.parent
R = pathlib.Path("projects/GO_GUIDELINES/sources")
C = S / "corpus"; C.mkdir(exist_ok=True)
wiki = json.load(open(S / "wiki/go-wiki-dump.json"))
papers = {p["id"]: p for p in json.load(open(S / "papers/candidates.json"))}
TXT = S / "drive_txt"
txtfiles = {str(p.relative_to(TXT))[:-4]: p for p in TXT.rglob("*.txt")}
by_stem = collections.defaultdict(list)
for k, p in txtfiles.items(): by_stem[os.path.splitext(k)[0]].append(p)
def drive_text(path):
    p = txtfiles.get(path) or (by_stem.get(os.path.splitext(path)[0]) or [None])[0]
    return p.read_text(errors="replace") if p else None
def slug(s): return re.sub(r"[^A-Za-z0-9._-]+", "_", s)[:150]
rows = []
for f, src in [("go-wiki-receipts.yaml", "wiki"), ("go-drive-receipts.yaml", "drive"), ("go-annotation-issues-receipts.yaml", "issues"),
               ("papers-receipts.yaml", "papers"), ("go-annotation-repo-files-receipts.yaml", "repo")]:
    d = yaml.load(open(R / f), Loader=yaml.CSafeLoader)
    (C / src).mkdir(exist_ok=True)
    for e in d["entries"]:
        if (e.get("relevance") or 0) < 3 or e["id"].startswith("drive:") and "#" in e["id"]: continue
        i = e["id"]
        if src == "wiki": t = wiki.get(e["title"], {}).get("text")
        elif src == "drive": t = drive_text(i[6:])
        elif src == "issues": p = S / "gh/issue_text" / (i.split(":")[1] + ".md"); t = p.read_text() if p.exists() else None
        elif src == "papers": p = papers.get(i, {}); t = f"{p.get('title')}\n{p.get('journal')} {p.get('year')}\n\n{p.get('abstract')}"
        else: p = S / "gh/repo" / i[5:]; t = p.read_text(errors="replace") if p.exists() else None
        if not t: continue
        out = C / src / (slug(i.split(":", 1)[1]) + ".md")
        out.write_text(f"<!-- id: {i}\nurl: {e.get('url')}\nrelevance: {e['relevance']}\nrationale: {e['rationale']} -->\n\n{t}")
        rows.append((src, e["relevance"], i, e.get("url") or "", str(out.relative_to(C)), e["rationale"].replace("\t", " ").replace("\n", " ")))
with open(C / "index.tsv", "w") as fh:
    fh.write("source\trelevance\tid\turl\tpath\trationale\n")
    for r in sorted(rows, key=lambda r: (-r[1], r[0])): fh.write("\t".join(map(str, r)) + "\n")
print(collections.Counter((r[0], r[1]) for r in rows))
