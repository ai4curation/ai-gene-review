"""Extract text (first 20k chars) from every file under SRC into DST/<rel>.txt. Records failures in DST/_errors.json."""
import sys, pathlib, json, subprocess
from concurrent.futures import ProcessPoolExecutor
SRC, DST = map(pathlib.Path, sys.argv[1:3])
TEXT = {".txt", ".md", ".csv", ".tsv", ".vtt", ".html", ".htm", ".yaml", ".yml", ".json", ".tex", ".py", ".sh", ".xml", ".rtf"}
MD = {".docx", ".pptx", ".xlsx", ".xls", ".pdf"}
LIMIT = 20000
def one(p):
    rel = p.relative_to(SRC); out = DST / (str(rel) + ".txt")
    if out.exists(): return None
    ext = p.suffix.lower()
    if ext in TEXT: txt = p.read_text(errors="replace")[:LIMIT]
    elif ext == ".doc":
        r = subprocess.run(["textutil", "-convert", "txt", "-stdout", str(p)], capture_output=True, text=True, timeout=120)
        if r.returncode: return (str(rel), r.stderr[:200])
        txt = r.stdout[:LIMIT]
    elif ext in MD:
        from markitdown import MarkItDown
        cmd = [sys.executable, "-c", "import sys;from markitdown import MarkItDown;print(MarkItDown().convert(sys.argv[1]).text_content[:%d])" % LIMIT, str(p)]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:  # very large spreadsheets/decks: record as not extractable
            return (str(rel), "conversion timed out after 120 s")
        if r.returncode: return (str(rel), r.stderr[-300:])
        txt = r.stdout
    else: return (str(rel), "unsupported extension " + ext)
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(txt); return None
if __name__ == "__main__":
    files = [p for p in SRC.rglob("*") if p.is_file() and not p.name.endswith(".partial")]
    with ProcessPoolExecutor(8) as ex: errs = [e for e in ex.map(one, files, chunksize=4) if e]
    json.dump(dict(errs), open(DST / "_errors.json", "w"), indent=1); print(len(files), "files,", len(errs), "errors")
