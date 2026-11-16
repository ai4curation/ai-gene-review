import json, re, sys, pathlib, collections, urllib.parse
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import rcpt, batcher
P = json.load(open(sys.argv[1]))
GUIDE = re.compile(r"guideline|best practice|policy|convention|should (always|never|not) be annotated|curator|"
                   r"annotation (practice|policy|rule)|we (agreed|decided)|consensus|do not annotate|evidence code|"
                   r"annotation extension|qualifier|NOT annotation|IBA|PAINT|ISS|IEA", re.I)
GENE_CATS = {"Immune genes", "Muscle Genes", "Cardiovascular Genes", "Lung Development Genes"}
SOFT_CATS = {"Software", "OBO-Edit", "OBO-Edit working group", "AmiGO", "AmiGO Hub", "AmiGO_Manual", "AmiGO_2", "AmiGO_2_Manual",
             "AmiGO working group", "SWUG Projects", "SWUG_Meetings", "SWUG Meetings", "Web Presence Working Group", "SourceForge",
             "Release Pipeline"}
CAREFUL_CATS = {"Annotation Guidelines", "Evidence Codes", "annotation extension", "Gene Product to Term Relations", "Quality Control",
                "GO-CAM", "GO-CAM Relations", "Annotation", "Function-Process", "Taxon", "Relations", "relations", "Annotation Working Group",
                "Editor_Guide_2018", "Transcription", "Signaling", "Viruses"}
MEETING = re.compile(r"(conf(erence)?\.? call|phone conference|meeting|minutes|stand up|update meeting|webex|call \d|agenda|"
                     r"^AHWG|^WPWG|^OEWG|^AWG|^SWUG|\d{4}-\d\d-\d\d|\d{1,2} \w+ \d{4})", re.I)
d = rcpt.load("go-wiki"); items = {"haiku": [], "careful": []}; B = collections.Counter()
for t, p in P.items():
    txt = p["text"] or ""; cats = {c.strip().strip("‏‎") for c in re.findall(r"\[\[Category:([^\]|]+)", txt)}
    hits = len(GUIDE.findall(txt)); L = len(txt)
    base = dict(title=t, url="https://wiki.geneontology.org/index.php/" + urllib.parse.quote(t.replace(" ", "_")),
                last_edit=(p.get("last_edit") or "")[:10], length=L, categories=sorted(cats))
    id = "wiki:" + t
    def rule(r, name, why): rcpt.put(d, id, relevance=r, method="rule:" + name, rationale=why, **base); B[name] += 1
    if re.search(r"logistics", t, re.I):
        rule(1, "meeting-logistics", "Meeting logistics page (venue, travel, hotel); no curation guidance."); continue
    if cats & SOFT_CATS and not cats & CAREFUL_CATS:
        rule(1, "software-docs", f"Software/tooling page ({', '.join(sorted(cats & SOFT_CATS))}): user manual or developer notes for "
             "OBO-Edit/AmiGO/web/release infrastructure, not annotation practice."); continue
    if cats & GENE_CATS and hits < 2:
        rule(2, "gene-worksheet", f"Per-gene annotation worksheet from a targeted curation project ({', '.join(sorted(cats & GENE_CATS))}); "
             "lists the gene's terms/status, no general guidance text."); continue
    if re.match(r"PTHR\d+|Panther ID", t) and hits < 3:
        rule(2, "paint-family-page", "PAINT family curation notes for one PANTHER family; case-level, no general guidance."); continue
    if L < 300:
        rule(1, "near-empty", f"Page has only {L} characters of wikitext (stub, redirect-like or placeholder)."); continue
    if MEETING.search(t) and hits == 0:
        rule(1 if re.search(r"ontology meeting|manager|projects|software|developer|SWUG|sourceforge|WPWG|OBO-Edit|stand up", t, re.I) else 2,
             "minutes-no-guidance", "Meeting minutes/agenda with no annotation-guidance language (no mention of guidelines, "
             "evidence codes, qualifiers, extensions, PAINT/IBA, conventions or decisions)."); continue
    tier = "careful" if (cats & CAREFUL_CATS and not MEETING.search(t)) or (hits >= 8 and not MEETING.search(t)) else "haiku"
    items[tier].append((id, f"# {t}\ncategories: {', '.join(sorted(cats))} | last edit {base['last_edit']} | {L} chars\n\n{txt}"))
    rcpt.put(d, id, relevance=None, method="rule:pending", rationale="pending " + tier, **base); B[tier] += 1
rcpt.save(d, description="Receipts for every non-redirect page (main, GO Wiki, Help, Category namespaces) of wiki.geneontology.org, fetched 2026-11-14.")
print(B)
print(batcher.write_batches(items["haiku"], "wiki/batches", "haiku", 60, 3000)[-1],
      batcher.write_batches(items["careful"], "wiki/batches", "careful", 30, 10000)[-1])
