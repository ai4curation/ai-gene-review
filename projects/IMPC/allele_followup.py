"""How much molecular and cellular knowledge comes from papers that use IMPC alleles?

Searches Europe PMC for papers whose text names an IMPC/KOMP/EUCOMM allele
designation (``tm1a(EUCOMM)Wtsi``, ``tm1b(KOMP)Wtsi``, ``tm1(KOMP)Vlcg``,
``em1(IMPC)J``, ...), drops the consortium's own resource papers, draws a
fixed-seed random sample, and classifies each sampled paper by the finest
readout it reports, using the readout catalogue of the ASSAY_TO_FUNCTION
project (``projects/ASSAY_TO_FUNCTION/readout_catalog.yaml``) and its own
loader (``mine_papers.load_catalog``):

- ``MOLECULAR``: a catalogue class with ``proximity: molecular`` matches
  (in vitro enzyme assay, direct binding, ChIP/EMSA, electrophysiology, ...).
- ``CELLULAR``: no molecular class, but a ``proximity: phenotypic`` class other
  than ``BEHAVIORAL_ASSAY`` matches (apoptosis, autophagy flux, proliferation,
  calcium imaging, reporter assays, ...). The catalogue defines phenotypic
  readouts as downstream *cellular* consequences.
- ``ORGANISM_ONLY``: neither of the above. This includes ``BEHAVIORAL_ASSAY``,
  the catalogue's one whole-animal class, and every paper in which no catalogue
  pattern matches. It is assigned by elimination, not by a positive match.

Each paper is classified twice: on its abstract (title + abstract, from Europe
PMC) and, when PubMed Central serves it (NCBI efetch, else Europe PMC), on its
full text with the reference list removed. The
catalogue's patterns are probe and instrument names written for methods text,
so the abstract classification under-counts molecular and cellular readouts.

Europe PMC's default field does not reach every section of the full text (a
phrase found in METHODS can be missing from a default query), so each
designation is searched in the default field and in the METHODS, RESULTS, FIG,
TABLE, SUPPL and BODY fields.

Raw downloads go to ``.cache/impc/europepmc/`` (git-ignored). Outputs:
``projects/IMPC/results/allele_followup.yaml``, ``allele_followup_sample.tsv``
and ``ALLELE_FOLLOWUP.md``.

    uv run python projects/IMPC/allele_followup.py
"""

from __future__ import annotations

import importlib.util
import json
import random
import re
import sys
import time
from collections import Counter
from pathlib import Path

import requests
import yaml

HERE = Path(__file__).parent
RESULTS = HERE / "results"
CACHE = Path(".cache/impc/europepmc")
CATALOG = Path("projects/ASSAY_TO_FUNCTION/readout_catalog.yaml")
MINER = Path("projects/ASSAY_TO_FUNCTION/mine_papers.py")
API = "https://www.ebi.ac.uk/europepmc/webservices/rest"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

SEED = 20261116
SAMPLE_SIZE = 200

# Europe PMC tokenises "tm1a(EUCOMM)Wtsi" into "tm1a EUCOMM Wtsi", so a phrase
# on the first two tokens catches every centre suffix.
DESIGNATIONS = [
    "tm1a EUCOMM", "tm1b EUCOMM", "tm1c EUCOMM", "tm1d EUCOMM", "tm1e EUCOMM",
    "tm1a KOMP", "tm1b KOMP", "tm1c KOMP", "tm1d KOMP", "tm1e KOMP",
    "tm1 KOMP", "tm1.1 KOMP",
    "em1 IMPC", "em2 IMPC",
]
FIELDS = ["", "METHODS:", "RESULTS:", "FIG:", "TABLE:", "SUPPL:", "BODY:"]

# The consortium's own resource and screen papers: the PMIDs given on the
# project page, papers with the consortium as a collective author, and papers
# whose title describes a resource or a high-throughput screen. Single-gene
# research papers from an IMPC centre (many list the "Sanger Mouse Genetics
# Project" as an author) are follow-up work and stay in the pool.
RESOURCE_PMIDS = {
    "27626380", "28650483", "36305825", "29626206",
    "28650954", "29348434", "29026089", "32005800", "23870131",
}
RESOURCE_AUTHOR = re.compile(r"International Mouse Phenotyping Consortium", re.I)
RESOURCE_TITLE = re.compile(
    r"Mouse Phenotyping Consortium|high-throughput (mouse )?phenotyp|mouse phenomics|"
    r"genome-wide (generation|lacZ)|systematic phenotyping|phenotyping screen|knockout mouse project",
    re.I,
)

ORDER = ["MOLECULAR", "CELLULAR", "ORGANISM_ONLY"]


def load_catalog() -> dict:
    spec = importlib.util.spec_from_file_location("a2f_mine_papers", MINER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load_catalog(CATALOG)


def get(
    url: str, params: dict | None = None, tries: int = 4, strict: bool = True, timeout: float = 60
) -> requests.Response | None:
    """GET with retries. Returns the last response; raises only when ``strict`` and nothing usable came back."""
    last = None
    for i in range(tries):
        try:
            last = requests.get(url, params=params, timeout=timeout)
            if last.status_code in (200, 404):
                return last
        except requests.RequestException:
            pass
        time.sleep(2 * (i + 1))
    if strict:
        raise RuntimeError(f"failed: {url} {params}")
    return last


def query() -> str:
    parts = [f'{f}"{d}"' for d in DESIGNATIONS for f in FIELDS]
    return "(" + " OR ".join(parts) + ") NOT SRC:PPR"


def fetch_hits() -> list[dict]:
    path = CACHE / "hits.json"
    if path.exists():
        return json.loads(path.read_text())
    CACHE.mkdir(parents=True, exist_ok=True)
    hits, cursor = [], "*"
    while True:
        r = get(f"{API}/search", {
            "query": query(), "format": "json", "resultType": "lite",
            "pageSize": 1000, "cursorMark": cursor,
        }).json()
        page = r["resultList"]["result"]
        hits += page
        nxt = r.get("nextCursorMark")
        if not page or nxt == cursor:
            break
        cursor = nxt
    path.write_text(json.dumps(hits))
    return hits


def is_resource(h: dict) -> bool:
    return (
        h.get("pmid") in RESOURCE_PMIDS
        or bool(RESOURCE_AUTHOR.search(h.get("authorString", "")))
        or bool(RESOURCE_TITLE.search(h.get("title", "")))
    )


def fetch_core(pmid: str) -> dict:
    path = CACHE / f"core_{pmid}.json"
    if path.exists():
        return json.loads(path.read_text())
    r = get(f"{API}/search", {
        "query": f"EXT_ID:{pmid} AND SRC:MED", "format": "json", "resultType": "core",
    }).json()
    res = r["resultList"]["result"]
    rec = res[0] if res else {}
    path.write_text(json.dumps(rec))
    return rec


def fetch_fulltext(pmcid: str) -> str | None:
    """Full-text JATS XML: NCBI PMC (E-utilities efetch) first, then Europe PMC.

    Only a document with a ``<body>`` counts as full text (an author manuscript
    or a restricted article can come back as front matter only).
    """
    path = CACHE / f"ft_{pmcid}.xml"
    miss = CACHE / f"ft_{pmcid}.missing"
    if path.exists():
        return path.read_text()
    if miss.exists():
        return None
    r = get(EFETCH, {"db": "pmc", "id": pmcid.removeprefix("PMC")}, tries=2, strict=False, timeout=60)
    time.sleep(0.4)  # stay under NCBI's 3 requests/s without an API key
    if r is not None and r.status_code == 200 and "<body" in r.text:
        path.write_text(r.text)
        return r.text
    r = get(f"{API}/{pmcid}/fullTextXML", tries=1, strict=False, timeout=45)
    if r is not None and r.status_code == 200 and "<body" in r.text:
        path.write_text(r.text)
        return r.text
    if r is None or r.status_code >= 500:
        print(f"full text unavailable (Europe PMC server error or timeout): {pmcid}", file=sys.stderr)
        return None  # not cached, so a re-run tries again
    miss.write_text("")
    return None


def xml_to_text(xml: str) -> str:
    """Article text without references, author/affiliation front matter, links and e-mail addresses."""
    for tag in ("ref-list", "contrib-group", "aff", "author-notes", "permissions", "ack"):
        xml = re.sub(rf"<{tag}[ >].*?</{tag}>", " ", xml, flags=re.S)
    xml = re.sub(r"<(email|ext-link|uri)[ >].*?</\1>", " ", xml, flags=re.S)
    xml = re.sub(r"<[^>]+>", " ", xml)
    xml = re.sub(r"https?://\S+|\S+@\S+", " ", xml)
    return re.sub(r"\s+", " ", xml)


# Catalogue matches that are a different word in these papers, found by reading
# the matched-string QC table (``allele_followup_matches.tsv``). In mouse
# knockout papers "reconstitution" is almost always haematopoietic or immune
# reconstitution, not reconstitution of a purified activity; the catalogue's
# case-insensitive ``\bEdU\b`` also matches ".edu" in addresses; and "flippase"
# is the FLP recombinase used to convert tm1a alleles, not a lipid flippase.
# These matches are dropped; the catalogue itself is unchanged.
QC_DROP = {
    "IN_VITRO_ENZYME": lambda m: m.lower().startswith("reconstitut"),
    "VIABILITY_PROLIFERATION": lambda m: m.lower() == "edu" and m != "EdU",
    "LIPID_TRANSFER_FLIPPASE": lambda m: m.lower() == "flippase",
}


def classify(text: str, catalog: dict, qc: Counter | None = None) -> tuple[str, list[str]]:
    low = text.lower()
    hit = []
    for name, spec in catalog.items():
        rx = spec["_compiled"]
        if rx is None or not any(lit in low for lit in spec["_screen"]):
            continue
        drop = QC_DROP.get(name, lambda m: False)
        kept = {mm.group(0) for mm in rx.finditer(text) if not drop(mm.group(0))}
        if kept:
            hit.append(name)
            if qc is not None:
                for k in {re.sub(r"\s+", " ", x).lower() for x in kept}:
                    qc[(name, k)] += 1
    prox = {catalog[n]["proximity"] for n in hit}
    if "molecular" in prox:
        level = "MOLECULAR"
    elif any(catalog[n]["proximity"] == "phenotypic" and n != "BEHAVIORAL_ASSAY" for n in hit):
        level = "CELLULAR"
    else:
        level = "ORGANISM_ONLY"
    return level, sorted(hit)


def main() -> None:
    catalog = load_catalog()
    hits = fetch_hits()
    with_pmid = [h for h in hits if h.get("pmid")]
    resource = [h for h in with_pmid if is_resource(h)]
    pool = sorted({h["pmid"]: h for h in with_pmid if not is_resource(h)}.values(), key=lambda h: int(h["pmid"]))
    sample = random.Random(SEED).sample(pool, min(SAMPLE_SIZE, len(pool)))

    rows = []
    qc_abs: Counter = Counter()
    qc_ft: Counter = Counter()
    for h in sorted(sample, key=lambda h: int(h["pmid"])):
        rec = fetch_core(h["pmid"])
        abstract = re.sub(r"<[^>]+>", " ", rec.get("abstractText", "") or "")
        title = rec.get("title", h.get("title", ""))
        a_level, a_hit = classify(f"{title} {abstract}", catalog, qc_abs) if abstract else ("NO_ABSTRACT", [])
        pmcid = rec.get("pmcid") or h.get("pmcid")
        ft = fetch_fulltext(pmcid) if pmcid else None
        f_level, f_hit = classify(xml_to_text(ft), catalog, qc_ft) if ft else ("NO_FULL_TEXT", [])
        rows.append({
            "pmid": h["pmid"], "pmcid": pmcid or "", "year": rec.get("pubYear", ""),
            "title": title, "abstract_level": a_level, "abstract_classes": ",".join(a_hit),
            "fulltext_level": f_level, "fulltext_classes": ",".join(f_hit),
        })

    with_abs = [r for r in rows if r["abstract_level"] != "NO_ABSTRACT"]
    with_ft = [r for r in rows if r["fulltext_level"] != "NO_FULL_TEXT"]
    a_counts = Counter(r["abstract_level"] for r in with_abs)
    f_counts = Counter(r["fulltext_level"] for r in with_ft)
    ab_classes = Counter(c for r in with_abs for c in r["abstract_classes"].split(",") if c)
    ft_classes = Counter(c for r in with_ft for c in r["fulltext_classes"].split(",") if c)
    behav_only_abs = sum(1 for r in with_abs if r["abstract_classes"] == "BEHAVIORAL_ASSAY")
    nomatch_abs = sum(1 for r in with_abs if not r["abstract_classes"])
    nomatch_ft = sum(1 for r in with_ft if not r["fulltext_classes"])
    # Abstract vs full text on the papers that have both.
    both = [r for r in with_abs if r["fulltext_level"] != "NO_FULL_TEXT"]
    pair = Counter((r["abstract_level"], r["fulltext_level"]) for r in both)

    out = {
        "europepmc_query_designations": DESIGNATIONS,
        "europepmc_fields": [f.rstrip(":") or "default" for f in FIELDS],
        "retrieved": time.strftime("%Y-%m-%d", time.gmtime((CACHE / "hits.json").stat().st_mtime)),
        "hits": len(hits),
        "hits_with_pmid": len(with_pmid),
        "excluded_as_consortium_resource": len(resource),
        "excluded_titles": sorted(h["title"] for h in resource),
        "sampling_pool": len(pool),
        "seed": SEED,
        "sample": len(rows),
        "sample_with_abstract": len(with_abs),
        "sample_with_full_text": len(with_ft),
        "abstract_level": {k: a_counts.get(k, 0) for k in ORDER},
        "abstract_no_catalogue_match": nomatch_abs,
        "abstract_behaviour_only": behav_only_abs,
        "fulltext_level": {k: f_counts.get(k, 0) for k in ORDER},
        "fulltext_no_catalogue_match": nomatch_ft,
        "abstract_vs_fulltext": {f"{a} -> {b}": n for (a, b), n in sorted(pair.items())},
        "abstract_class_papers": dict(ab_classes.most_common()),
        "fulltext_class_papers": dict(ft_classes.most_common()),
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "allele_followup.yaml").write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True))
    cols = list(rows[0].keys())
    with (RESULTS / "allele_followup_sample.tsv").open("w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]).replace("\t", " ") for c in cols) + "\n")

    with (RESULTS / "allele_followup_matches.tsv").open("w") as fh:
        fh.write("class\tproximity\tmatched\tabstracts\tfull_texts\n")
        for name, m in sorted(set(qc_abs) | set(qc_ft)):
            fh.write(f"{name}\t{catalog[name]['proximity']}\t{m}\t{qc_abs.get((name, m), 0)}\t{qc_ft.get((name, m), 0)}\n")

    def pct(a: int, b: int) -> str:
        return f"{a} ({100 * a / b:.0f}%)" if b else str(a)

    na, nf = len(with_abs), len(with_ft)
    lines = [
        "# Follow-up papers using IMPC alleles: finest readout (generated)",
        "",
        "Generated by `allele_followup.py`; do not edit by hand.",
        "",
        f"Europe PMC search ({out['retrieved']}) for {len(DESIGNATIONS)} IMPC/KOMP/EUCOMM allele designations"
        f" ({', '.join(DESIGNATIONS)}), preprints excluded: {len(hits):,} records, {len(with_pmid):,} with a PMID."
        f" {len(resource)} consortium resource papers removed (listed in `allele_followup.yaml`),"
        f" leaving {len(pool):,}. Random sample of {len(rows)} (seed {SEED});"
        f" {na} have an abstract and {nf} have full text in PubMed Central.",
        "",
        "Levels use the ASSAY_TO_FUNCTION readout catalogue: MOLECULAR = any `proximity: molecular` class;"
        " CELLULAR = otherwise any `proximity: phenotypic` class except BEHAVIORAL_ASSAY;"
        " ORGANISM_ONLY = everything else, assigned by elimination (it includes papers where no catalogue"
        " pattern matches). The catalogue patterns are written for methods text, so abstracts under-count."
        " Full-text matches anywhere in the article count, including introduction and discussion, so the"
        " full-text column over-counts what the paper itself measured. Matches dropped as a different word"
        f" here: {', '.join(QC_DROP)} (see the script); every kept match string is in `allele_followup_matches.tsv`.",
        "",
        "| Finest readout | Abstract | Full text (references removed) |",
        "|---|---:|---:|",
    ]
    for k in ORDER:
        lines.append(f"| {k} | {pct(a_counts.get(k, 0), na)} | {pct(f_counts.get(k, 0), nf)} |")
    lines += [
        "",
        f"- Abstracts with no catalogue match at all: {pct(nomatch_abs, na)}; full texts: {pct(nomatch_ft, nf)}.",
        "",
        "## Abstract level against full-text level (papers with both)",
        "",
        "| Abstract | Full text | Papers |",
        "|---|---|---:|",
    ]
    for (a, b), n in sorted(pair.items()):
        lines.append(f"| {a} | {b} | {n} |")
    lines += ["", "## Catalogue classes matched (papers)", "", "| Class | Proximity | Abstracts | Full texts |", "|---|---|---:|---:|"]
    for name in sorted(set(ab_classes) | set(ft_classes), key=lambda n: -ft_classes.get(n, 0)):
        lines.append(f"| {name} | {catalog[name]['proximity']} | {ab_classes.get(name, 0)} | {ft_classes.get(name, 0)} |")
    lines.append("")
    (RESULTS / "ALLELE_FOLLOWUP.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
