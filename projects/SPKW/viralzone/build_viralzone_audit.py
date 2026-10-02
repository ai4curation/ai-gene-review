#!/usr/bin/env python3
"""Audit ViralZone as an upstream source for GO term definitions and UniProt keywords.

ViralZone (https://viralzone.expasy.org) feeds the Gene Ontology twice over, by two
independent routes:

1. **Definition route.** GO cites ViralZone pages as definition dbxrefs, using the
   prefix ``VZ`` (e.g. ``GO:0039713`` carries ``VZ:1951``). The cited page is often
   the source the definition was written from.
2. **Annotation route.** A ViralZone page may declare one primary UniProt keyword in
   its header. That keyword maps to a GO term and generates SPKW (``GO_REF:0000043``)
   IEA annotations -- the propagation path the parent SPKW project reviews.

Nothing in this repository audited the shared upstream. This script measures both
routes and writes the tables the SPKW-VIRALZONE page reports:

* ``vz-go-xrefs.tsv``   -- every GO term carrying a ``VZ:`` dbxref, with a
  sentence-level similarity score between the GO definition and the cited page's
  prose, so heavily-copied definitions can be separated from ones that merely cite
  ViralZone as a reference.
* ``vz-dead-xrefs.tsv`` -- GO terms citing a ViralZone page that is absent from the
  live sitemap (link rot).
* ``vz-dual-path.tsv``  -- pages on both routes: they define a GO term *and* carry a
  primary UniProt keyword.

Caveats, deliberately not smoothed over:

* Similarity is ``difflib.SequenceMatcher`` on normalized text, best-matching window
  per definition sentence. ``autojunk`` MUST stay False: on strings over 200
  characters the default heuristic treats common characters as noise and collapses
  real matches to near-zero. A high score means textual reuse, not that the
  definition is wrong; a low score means GO wrote its own text, not that ViralZone
  was ignored.
* Page prose is cut at the first navigation/UniProt-table marker. ViralZone appends
  the full list of matching UniProt entries to keyword pages (thousands of
  accessions), which would otherwise swamp the prose.
* The primary keyword is read from the ``(kw:KW-####)`` string ViralZone renders in
  the page header. The SPKW-VIRUS audit read the same field from the header's
  ``data-about`` attribute and found 147 pages; this script reproducing that count
  is the cross-check that both readings agree.

Usage:
    uv run python projects/SPKW/viralzone/build_viralzone_audit.py
    uv run python projects/SPKW/viralzone/build_viralzone_audit.py --cache /tmp/vz.json
"""

from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SITEMAP = "https://viralzone.expasy.org/sitemap.xml"
PAGE = "https://viralzone.expasy.org/{pid}"
UA = "ai-gene-review/viralzone-audit (https://github.com/ai4curation/ai-gene-review)"
OUT_DIR = Path(__file__).resolve().parent

# ViralZone appends navigation and a full UniProt entry table below the prose.
NAV = re.compile(
    r"(Viral molecular biology Virion Virus entry|Links Uniprot Keyword"
    r"|DB LINKS|Matching UniProtKB)"
)
KW_IN_HEADER = re.compile(r"\(kw:(KW-\d+)\)")


def fetch(url: str, timeout: int = 45) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")


def sitemap_page_ids() -> list[str]:
    """Numeric page ids listed in the live ViralZone sitemap."""
    xml = fetch(SITEMAP)
    ids = re.findall(r"https://viralzone\.expasy\.org/(\d+)", xml)
    return sorted(set(ids), key=int)


def page_text(pid: str) -> tuple[str, str | None, str | None]:
    """Return ``(pid, title, visible_text)``; text is None when the fetch failed."""
    try:
        html = fetch(PAGE.format(pid=pid))
    except Exception as exc:  # noqa: BLE001 - network, reported not raised
        print(f"  ! VZ-{pid}: {type(exc).__name__}: {exc}", file=sys.stderr)
        return pid, None, None
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    title = re.sub(r"\s*~\s*ViralZone\s*$", "", m.group(1).strip()) if m else ""
    body = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", html)
    main = re.search(r"(?is)<main[^>]*>(.*?)</main>", body)
    if main:
        body = main.group(1)
    text = re.sub(r"(?s)<[^>]+>", " ", body)
    text = re.sub(r"&nbsp;?", " ", text).replace("&amp;", "&")
    return pid, title, re.sub(r"\s+", " ", text).strip()


def harvest(ids: list[str], workers: int = 6) -> dict[str, dict]:
    out: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for pid, title, text in pool.map(page_text, ids):
            out[pid] = {"title": title, "text": text}
    return out


def prose(text: str) -> str:
    m = NAV.search(text)
    return (text[: m.start()] if m else text).strip()


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def sentence_scores(definition: str, page_prose: str) -> list[float]:
    """Best-window similarity for each substantive sentence of the definition."""
    haystack = normalize(page_prose)
    scores: list[float] = []
    for sentence in re.split(r"(?<=[.;])\s+", definition):
        needle = normalize(sentence)
        if len(needle) < 25 or not haystack:
            continue
        best = 0.0
        for i in range(0, max(1, len(haystack) - len(needle) + 1), 8):
            window = haystack[i : i + len(needle) + 40]
            # autojunk=False is required; see the module docstring.
            r = difflib.SequenceMatcher(None, needle, window, autojunk=False).ratio()
            best = max(best, r)
        scores.append(best)
    return scores


def reuse_band(best: float) -> str:
    if best >= 0.85:
        return "VERBATIM_ISH"
    if best >= 0.70:
        return "CLOSE_PARAPHRASE"
    if best >= 0.55:
        return "REWORDED"
    return "INDEPENDENT"


def go_vz_xrefs() -> list[tuple[str, str, str, str, str]]:
    """``(go_id, label, aspect, definition, vz_curie)`` for GO terms citing ViralZone.

    The candidate set comes straight from the semsql ``has_dbxref_statement``
    table rather than from walking every GO term: ``entity_metadata_map`` is a
    per-term round trip and GO has ~50k terms, which makes the full walk
    impractical. Only the matching terms are then resolved through the adapter, so
    labels, definitions and aspects still come from OAK.
    """
    from oaklib import get_adapter
    from sqlalchemy import text

    adapter = get_adapter("sqlite:obo:go")
    with adapter.engine.connect() as conn:
        pairs = list(
            conn.execute(
                text(
                    "select subject, value from has_dbxref_statement "
                    "where value like 'VZ:%' and subject like 'GO:%'"
                )
            )
        )
    rows = []
    for go_id, curie in pairs:
        meta = adapter.entity_metadata_map(go_id) or {}
        definition = (meta.get("IAO:0000115") or [""])[0] or ""
        aspect = (meta.get("oio:hasOBONamespace") or [""])[0] or ""
        rows.append((go_id, adapter.label(go_id) or "", aspect, definition, str(curie)))
    return sorted(rows)


def write_tsv(path: Path, header: list[str], rows: list[list]) -> None:
    with path.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)
    print(f"wrote {path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path} ({len(rows)} rows)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cache", type=Path, help="JSON cache of fetched pages (read if present, else written)")
    args = ap.parse_args()

    if args.cache and args.cache.exists():
        pages = json.loads(args.cache.read_text())
        print(f"loaded {len(pages)} cached ViralZone pages from {args.cache}")
    else:
        ids = sitemap_page_ids()
        print(f"sitemap lists {len(ids)} numeric ViralZone pages; fetching...")
        pages = harvest(ids)
        if args.cache:
            args.cache.write_text(json.dumps(pages))
    live = {pid: v for pid, v in pages.items() if v["text"]}
    print(f"fetched prose for {len(live)}/{len(pages)} pages")

    keywords = {}
    for pid, v in live.items():
        m = KW_IN_HEADER.search(v["text"][:400])
        if m:
            keywords[pid] = m.group(1)
    print(f"pages declaring a primary UniProt keyword: {len(keywords)}")

    xrefs = go_vz_xrefs()
    print(f"GO terms citing ViralZone: {len({r[0] for r in xrefs})} ({len(xrefs)} xrefs)")

    scored, dead = [], []
    for go_id, label, aspect, definition, curie in xrefs:
        pid = curie.split(":", 1)[1]
        if pid not in live:
            dead.append([go_id, label, aspect, curie, PAGE.format(pid=pid)])
            continue
        scores = sentence_scores(definition, prose(live[pid]["text"]))
        best = max(scores) if scores else ""
        mean = round(sum(scores) / len(scores), 3) if scores else ""
        scored.append([
            go_id, label, aspect, curie, live[pid]["title"],
            round(best, 3) if scores else "", mean, len(scores),
            reuse_band(best) if scores else "UNSCORED",
            keywords.get(pid, ""),
            len(prose(live[pid]["text"])),
        ])

    scored.sort(key=lambda r: (-(r[5] or 0), r[0]))
    write_tsv(OUT_DIR / "vz-go-xrefs.tsv",
              ["go_id", "go_label", "go_aspect", "vz_curie", "vz_title",
               "best_sentence_similarity", "mean_sentence_similarity",
               "sentences_scored", "reuse_band", "vz_primary_keyword", "vz_prose_chars"],
              scored)
    write_tsv(OUT_DIR / "vz-dead-xrefs.tsv",
              ["go_id", "go_label", "go_aspect", "vz_curie", "url"], dead)

    xref_pages = {r[4].split(":", 1)[1] for r in xrefs}
    dual = sorted(set(keywords) & xref_pages, key=int)
    by_page: dict[str, list[str]] = {}
    for go_id, _l, _a, _d, curie in xrefs:
        by_page.setdefault(curie.split(":", 1)[1], []).append(go_id)
    write_tsv(OUT_DIR / "vz-dual-path.tsv",
              ["vz_page", "vz_title", "vz_primary_keyword", "go_terms_citing_page"],
              [[f"VZ:{p}", live[p]["title"], keywords[p], ";".join(sorted(by_page[p]))] for p in dual])

    bands = {}
    for row in scored:
        bands[row[8]] = bands.get(row[8], 0) + 1
    print("\nreuse bands:", bands)
    print(f"dead xrefs: {len(dead)}")
    print(f"dual-path pages: {len(dual)}  "
          f"(keyword-only {len(set(keywords) - xref_pages)}, xref-only {len(xref_pages - set(keywords))})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
