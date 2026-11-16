"""Bucket every file in the GO shared drive manifest. Text comes from drive_txt/<path-as-downloaded>.txt."""
import json, sys, re, os, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent)); import rcpt, batcher
S = pathlib.Path(__file__).parent.parent
M = json.load(open(S / "drive_all.json"))
TXT = S / "drive_txt"
# map manifest path -> downloaded text (google-native files get a new extension on export)
txtfiles = {str(p.relative_to(TXT))[:-4]: p for p in TXT.rglob("*.txt")}
by_stem = collections.defaultdict(list)
for k, p in txtfiles.items(): by_stem[os.path.splitext(k)[0]].append(p)
def text_for(path):
    p = txtfiles.get(path) or (by_stem.get(os.path.splitext(path)[0]) or [None])[0]
    return p.read_text(errors="replace") if p else None
MEDIA = ("image/", "video/", "audio/")
DATA_EXT = (".gz", ".tgz", ".tar", ".zip", ".gaf", ".gpad", ".gpi", ".obo", ".owl", ".jar", ".tz", ".json", ".xml", ".tsv", ".bam", ".ttl", ".ofn", ".jnl")
GUIDE_DIRS = ("Annotation/Annotation guidelines", "ZZZ-archived/Archived annotation guidelines", "GO-CAM and Noctua/GO-CAM specifications",
              "Annotation/Curator training", "Annotation/Annotation Transfer", "Annotation/Annotation QC", "Annotation/Protein Complexes",
              "Ontology/Design patterns", "Ontology/Taxon constraints", "Annotation/Curation Workflows", "Annotation/Annotation support",
              "Annotation/Annotation workshops", "Outreach/Presentations - introduction to GO", "Documentation", "Working Groups/IEA WG",
              "GO-CAM and Noctua/Evidence Unwinding Project", "Annotation/Signaling Project", "Annotation/Response_to_Project",
              "ZZZ-archived/Annotation Conference Calls", "Ontology/Ontology relations", "Ontology/regulates o part_of", "Subsets")
d = rcpt.load("go-drive"); items = {"haiku": [], "careful": []}; B = collections.Counter()
for x in M:
    p, mt = x["Path"], x["MimeType"]; low = p.lower(); top = p.split("/")[0]
    base = dict(title=p.rsplit("/", 1)[-1], path=p, mime=mt, drive_id=x.get("ID"),
                url=f"https://drive.google.com/open?id={x['ID']}" if x.get("ID") else None, modified=(x.get("ModTime") or "")[:10])
    id = "drive:" + p
    def rule(r, name, why): rcpt.put(d, id, relevance=r, method="rule:" + name, rationale=why, **base); B[name] += 1
    if mt.startswith(MEDIA) or low.endswith((".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".cr2", ".heic", ".svg", ".mp4", ".mov")):
        rule(None, "media-not-assessed", f"Media file ({mt}); not assessed per instructions."); continue
    if low.endswith(DATA_EXT) or "x-gzip" in mt or mt in ("application/gzip", "application/x-tar"):
        rule(None, "data-file-not-assessed", f"Data/archive file ({mt}); raw annotation/ontology data, not a guidance document."); continue
    if p.startswith("PAINT/PAINT Release stats"):
        rule(1, "release-stats", "PAINT release statistics spreadsheet (per-release counts); no guidance."); continue
    if p.startswith(("Release checks/gorules-validation", "Release checks/Monthly releases stats", "Release checks/GOEx data_exchange",
                     "Release checks/SynGO", "Release checks/GO-CAM stats", "PAINT/PAINT Validator")):
        rule(1, "release-qc-output", "Per-release QC/validation output or statistics (generated report); no curation guidance."); continue
    if p.startswith("Annotation/Annotation Reviews") and ("sheet" in mt or low.endswith((".csv", ".xlsx"))):
        m = re.search(r"#\s?(\d{3,5})", p)
        rule(2, "annotation-review-sheet", "Spreadsheet of annotations under review for an obsoletion/refactoring ticket"
             + (f" (go-annotation #{m.group(1)})" if m else "") + "; row-level case decisions, the guidance is in the linked ticket."); continue
    if p.startswith(("GO-CAM and Noctua/Reactome_and_Pathway_Mapping", "Working Groups/MOD Imports", "GO-CAM and Noctua/Model & Validations",
                     "Ontology/Enzymes", "GO-CAM and Noctua/Testing", "GO-CAM and Noctua/Quality_Control", "Ontology/Rhea-Reactome")) \
            and ("sheet" in mt or low.endswith((".csv", ".xlsx", ".xls"))):
        rule(2, "data-worksheet", "Working spreadsheet (pathway/reaction mapping table, import or validation report, term list) supporting a "
             "GO-CAM/ontology project; tabular data, any conventions live in the project's documents."); continue
    if p.startswith("Call Recordings") or low.endswith(".vtt"):
        pass  # transcripts -> haiku below
    txt = text_for(p)
    if txt is None:
        rule(None, "no-text-extracted", "Could not download or extract text (over-long/odd filename, unsupported format such as .ppt, or >60 MB); "
             "not assessed. Title suggests: " + base["title"][:120]); continue
    if len(txt.strip()) < 200:
        rule(1, "near-empty", f"Extracted text is only {len(txt.strip())} characters (empty or image-only document)."); continue
    tier = "careful" if p.startswith(GUIDE_DIRS) or re.search(r"guideline|best practice|SOP|curation manual|how to annotate", low) else "haiku"
    lim = 8000 if tier == "careful" else (1500 if ("sheet" in mt or low.endswith(".csv")) else 3000)
    items[tier].append((id, f"# {p}\nmime: {mt} | modified {base['modified']}\n\n{txt[:lim]}"))
    rcpt.put(d, id, relevance=None, method="rule:pending", rationale="pending " + tier, **base); B[tier] += 1
rcpt.save(d, description="Receipts for every file in the GO shared Google Drive (rclone remote gdrive-go, listed 2026-11-14). "
          "Google-native files were exported to text/csv; office/PDF files were converted with markitdown; first 20k characters kept.")
print(B)
for t, size, lim in (("haiku", 60, 3000), ("careful", 30, 8000)):
    print(t, batcher.write_batches(items[t], S / "drive/batches", t, size, lim + 200)[-1:] if items[t] else None)
