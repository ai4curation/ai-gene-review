import json, re, collections, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import rcpt
G = pathlib.Path(sys.argv[1])
I = {i["number"]: i for i in map(json.loads, open(G / "issues.jsonl"))}
C = collections.defaultdict(list)
for c in map(json.loads, open(G / "comments.jsonl")):
    C[int(c["issue_url"].rsplit("/", 1)[1])].append(c)
T = G / "issue_text"; T.mkdir(exist_ok=True)
for n, i in I.items():
    txt = f"# #{n} {i['title']}\nstate: {i['state']} labels: {', '.join(i['labels'])} created: {i['created_at'][:10]}\n\n{i['body'] or ''}\n"
    for c in C[n]: txt += f"\n--- comment by {c['user']}\n{c['body'] or ''}\n"
    (T / f"{n}.md").write_text(txt)
GUIDE = re.compile(r"guideline|best practice|policy|convention|documentation|should (always|never|not) be annotated|"
                   r"rule of thumb|curator guidance|annotation (practice|policy|rule)|we (should|agreed|decided)|consensus|"
                   r"recommend|do not annotate|don't annotate|not appropriate to annotate", re.I)
DOC_LABELS = {"documentation", "request for guidelines", "annotation relations", "annotation extensions", "evidence codes",
              "HTP guidelines", "QC", "GAF", "GPAD/GPI", "request for proposal", "protein complex", "annotation request",
              "GO workshop signalling 2017", "action Item from NYC-05-2018", "transcription", "mitochondrion",
              "vesicle-mediated-transport", "GO-CAM", "function_pred_eval", "no clear request", "wish list", "Matrix"}
CASE_LABELS = {"PAINT annotation", "InterPro mapping", "UniProt KW2GO mapping", "ARBA", "ARBA - checked", "TreeGrafter",
               "UniRule", "HAMAP2GO mapping", "EC2GO mapping", "Rfam2GO", "PAINT - waiting for primary annotation",
               "ARBA - waiting for update", "suggestion for new PAINT annotations", "UniPathway", "RHEA"}
d = rcpt.load("go-annotation-issues")
buckets = collections.Counter(); triage = []
for n, i in sorted(I.items()):
    labs = set(i["labels"]); text = (T / f"{n}.md").read_text()
    hits = len(GUIDE.findall(text)); L = len(text)
    base = dict(title=i["title"], url=i["url"], state=i["state"], labels=sorted(labs), n_comments=len(C[n]))
    t = i["title"]
    if i["pull"] and re.match(r"(Update|Create|Add) .*(gpad|gpi|gaf)", t, re.I):
        rcpt.put(d, f"issue:{n}", relevance=2, method="rule:format-spec-pr", rationale=
          "Pull request editing GAF/GPAD/GPI format spec text; file-format specification, not annotation best practice "
          "(the spec itself is tracked on geneontology.org).", **base); buckets["format-pr"] += 1; continue
    if i["pull"] and re.search(r"issue template|workflow|report", t, re.I):
        rcpt.put(d, f"issue:{n}", relevance=1, method="rule:repo-maintenance-pr", rationale=
          "Repository maintenance PR (issue templates / GitHub Actions / report generation); no curation guidance.", **base)
        buckets["maint-pr"] += 1; continue
    if labs & CASE_LABELS and not labs & DOC_LABELS and hits == 0:
        rcpt.put(d, f"issue:{n}", relevance=2, method="rule:case-level-mapping-fix", rationale=
          f"Case-level report against one {'/'.join(sorted(labs & CASE_LABELS))} rule/node; corrects a specific inference "
          "with no general guidance language in body or comments. Useful only as an example of an error pattern.", **base)
        buckets["case"] += 1; continue
    if re.match(r"Review annotations to", t) and hits == 0 and not labs & DOC_LABELS:
        rcpt.put(d, f"issue:{n}", relevance=2, method="rule:term-obsoletion-review", rationale=
          "Term-refactoring/obsoletion annotation review for specific GO term(s); case-level curation task with no "
          "general guidance language.", **base); buckets["review"] += 1; continue
    if L < 400 and not labs & DOC_LABELS:
        rcpt.put(d, f"issue:{n}", relevance=1, method="rule:near-empty", rationale=
          f"Issue text is only {L} characters with no guidance labels; too little content to inform best practice.", **base)
        buckets["tiny"] += 1; continue
    tier = "careful" if (labs & {"documentation", "request for guidelines", "annotation relations", "annotation extensions",
                                 "evidence codes", "HTP guidelines", "request for proposal"} or hits >= 4) else "haiku"
    triage.append({"n": n, "tier": tier, "hits": hits, "len": L, **base}); buckets[tier] += 1
rcpt.save(d, description="Receipts for every issue and PR in github.com/geneontology/go-annotation (fetched 2026-11-14).")
json.dump(triage, open(G / "triage.json", "w"), indent=0)
print(buckets)
