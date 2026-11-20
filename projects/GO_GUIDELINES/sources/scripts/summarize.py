"""Write projects/GO_GUIDELINES/sources/top-sources.md: per-source tallies and every item with final score 5."""
import sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent)); import rcpt
SRC = [("go-drive", "GO shared Google Drive"), ("go-wiki", "GO wiki"), ("papers", "Papers and books"),
       ("go-annotation-issues", "go-annotation issues and PRs"), ("go-annotation-repo-files", "go-annotation repository files")]
out = ["# GO best-practice sources: tallies and top tier", "",
       "Generated from the receipt YAMLs in this folder. `None` = not assessed (media, raw data, or no extractable text).", "",
       "| Source | Items | 5 | 4 | 3 | 2 | 1 | not assessed | by rule | haiku | opus |", "|---|---|---|---|---|---|---|---|---|---|---|"]
tops = {}
for s, label in SRC:
    d = rcpt.load(s); E = list(d["entries"].values())
    r = collections.Counter(e.get("relevance") for e in E); m = collections.Counter(e["method"].split(":")[0] for e in E)
    out.append(f"| {label} | {len(E)} | {r[5]} | {r[4]} | {r[3]} | {r[2]} | {r[1]} | {r[None]} | {m['rule']} | {m['haiku']} | {m['opus']} |")
    tops[label] = sorted((e for e in E if e.get("relevance") == 5), key=lambda e: str(e.get("title") or e["id"]))
for label, T in tops.items():
    out += ["", f"## {label}: score 5 ({len(T)})", ""]
    for e in T:
        t = (e.get("title") or e["id"]).replace("|", "/")
        link = f"[{t}]({e['url']})" if e.get("url") else t
        out.append(f"- {link} ({e['method']}): {e['rationale']}")
(rcpt.OUT / "top-sources.md").write_text("\n".join(out) + "\n")
print("\n".join(out[:12]))
