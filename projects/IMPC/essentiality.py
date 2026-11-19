"""IMPC lethality against human cell-line essentiality (DepMap common essentials).

An IMPC lethality call (preweaning, embryonic or prenatal lethality) says the
knockout animal does not survive. It has two readings: the gene product is
needed by every cell (a cell-autonomous essential function, which a CRISPR
screen in cultured human cells also detects), or it is needed only for
development or physiology of the whole organism. DepMap's CRISPR "common
essential" list separates the two: a lethal gene that is also common-essential
in human cell lines has a cell-level reading; one that is not is
developmental-only lethal as far as cultured cells can tell.

Inputs:

- ``.cache/impc/{genotype_phenotype,genes}.tsv`` from ``fetch_impc.py``.
- DepMap ``CRISPRInferredCommonEssentials.csv`` and
  ``AchillesCommonEssentialControls.csv``. The script asks the DepMap portal's
  download API (https://depmap.org/portal/api/download/files) first and records
  what it returned. If the portal does not return the file listing, it uses the
  same files from the DepMap team's own figshare deposit of a public release
  (``FIGSHARE_ARTICLE``), checking each file's MD5 against figshare's record.
  It does not substitute a different essential-gene list.

Mouse genes are mapped to human through IMPC's ``human_gene_symbol`` field; a
gene is common-essential if any mapped human symbol is.

Raw downloads go to ``.cache/impc/depmap/`` (git-ignored). Outputs:
``projects/IMPC/results/essentiality.yaml`` and ``ESSENTIALITY.md``.

    uv run python projects/IMPC/essentiality.py
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
import time
from pathlib import Path

import pandas as pd
import requests
import yaml

HERE = Path(__file__).parent
RESULTS = HERE / "results"
CACHE = Path(".cache/impc")
DEPMAP = CACHE / "depmap"
PORTAL = "https://depmap.org/portal/api/download/files"
FIGSHARE_ARTICLE = 27993248  # "DepMap 24Q4 Public", deposited by Broad DepMap
FILES = ["CRISPRInferredCommonEssentials.csv", "AchillesCommonEssentialControls.csv"]
LETHAL = re.compile(r"(?:preweaning|embryonic|prenatal|perinatal) lethality", re.I)


def try_portal() -> tuple[str, dict[str, str]]:
    """Return (status note, {filename: url}) from the DepMap portal download API."""
    try:
        r = requests.get(PORTAL, timeout=60)
    except requests.RequestException as e:
        return f"request failed: {type(e).__name__}", {}
    ctype = r.headers.get("content-type", "")
    if r.status_code != 200:
        return f"HTTP {r.status_code}", {}
    if "<html" in r.text[:2000].lower():
        title = re.search(r"<title>(.*?)</title>", r.text, re.S | re.I)
        return f"HTTP 200 but an HTML page ({title.group(1).strip() if title else ctype}), not the file listing", {}
    urls = {}
    for row in csv.DictReader(io.StringIO(r.text)):
        name = row.get("filename") or row.get("file_name") or ""
        if name in FILES and name not in urls:
            urls[name] = row.get("url") or ""
    return "file listing returned", urls


def figshare_files() -> tuple[str, dict[str, tuple[str, str]]]:
    a = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}", timeout=60).json()
    authors = ", ".join(x["full_name"] for x in a.get("authors", []))
    files = {
        f["name"]: (f["download_url"], f.get("supplied_md5") or f.get("computed_md5") or "")
        for f in a["files"]
        if f["name"] in FILES
    }
    return f"{a['title']} (figshare {FIGSHARE_ARTICLE}, doi:{a.get('doi')}, deposited by {authors})", files


def download(name: str, url: str, md5: str = "") -> Path:
    path = DEPMAP / name
    if not path.exists():
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        path.write_bytes(r.content)
    if md5:
        got = hashlib.md5(path.read_bytes()).hexdigest()
        if got != md5:
            raise RuntimeError(f"{name}: md5 {got} != {md5}")
    return path


def read_symbols(path: Path) -> set[str]:
    """DepMap gene columns are 'SYMBOL (EntrezID)'."""
    df = pd.read_csv(path)
    col = df.columns[0]
    return {str(v).split(" (")[0].strip() for v in df[col].dropna()}


def main() -> None:
    DEPMAP.mkdir(parents=True, exist_ok=True)
    portal_status, portal_urls = try_portal()
    source = ""
    paths = {}
    if all(portal_urls.get(f) for f in FILES):
        source = "DepMap portal download API"
        paths = {f: download(f, portal_urls[f]) for f in FILES}
    else:
        source, fs = figshare_files()
        paths = {f: download(f, *fs[f]) for f in FILES}
    common = read_symbols(paths["CRISPRInferredCommonEssentials.csv"])
    controls = read_symbols(paths["AchillesCommonEssentialControls.csv"])

    gp = pd.read_csv(CACHE / "genotype_phenotype.tsv", sep="\t")
    genes = pd.read_csv(CACHE / "genes.tsv", sep="\t")
    to_human = {
        acc: [x for x in str(sym).split("|") if x and x != "nan"]
        for acc, sym in zip(genes.mgi_accession_id, genes.human_gene_symbol)
    }
    phenotyped = set(genes.loc[genes.phenotyping_data_available == True, "mgi_accession_id"])  # noqa: E712
    with_call = set(gp.marker_accession_id)
    lethal_rows = gp[gp.mp_term_name.str.contains(LETHAL, na=False)]
    lethal = set(lethal_rows.marker_accession_id)
    lethal_terms = lethal_rows.mp_term_name.value_counts().to_dict()
    universe = phenotyped | with_call  # genes IMPC phenotyped
    nonlethal = universe - lethal

    def ess(acc: str, s: set[str]) -> bool:
        return any(h in s for h in to_human.get(acc, []))

    def split(group: set[str]) -> dict:
        mapped = {g for g in group if to_human.get(g)}
        e = {g for g in mapped if ess(g, common)}
        return {
            "genes": len(group),
            "with_human_symbol": len(mapped),
            "depmap_common_essential": len(e),
            "not_common_essential": len(mapped - e),
            "achilles_essential_control": sum(1 for g in mapped if ess(g, controls)),
        }

    # Penetrance / stage breakdown of the lethal genes.
    stage = {}
    for term, accs in lethal_rows.groupby("mp_term_name").marker_accession_id:
        stage[term] = split(set(accs))

    # Reverse: of phenotyped genes whose human ortholog is common-essential, how many are lethal?
    ce_universe = {g for g in universe if ess(g, common)}
    out = {
        "depmap_portal_status": portal_status,
        "depmap_source": source,
        "depmap_common_essentials": len(common),
        "achilles_common_essential_controls": len(controls),
        "impc_lethality_terms": {k: int(v) for k, v in lethal_terms.items()},
        "impc_genes_phenotyped": len(universe),
        "lethal": split(lethal),
        "not_lethal": split(nonlethal),
        "lethal_by_term": stage,
        "common_essential_phenotyped": len(ce_universe),
        "common_essential_phenotyped_lethal": len(ce_universe & lethal),
        "common_essential_phenotyped_not_lethal": len(ce_universe - lethal),
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "essentiality.yaml").write_text(yaml.safe_dump(out, sort_keys=False))

    def pct(a: int, b: int) -> str:
        return f"{a:,} ({100 * a / b:.0f}%)" if b else str(a)

    L, N = out["lethal"], out["not_lethal"]
    lines = [
        "# IMPC lethality against DepMap common essentials (generated)",
        "",
        "Generated by `essentiality.py`; do not edit by hand.",
        "",
        f"- DepMap portal download API ({time.strftime('%Y-%m-%d')}): {portal_status}.",
        f"- Essential-gene lists used: {source}. CRISPRInferredCommonEssentials: {len(common):,} genes;"
        f" AchillesCommonEssentialControls: {len(controls):,}.",
        f"- IMPC genes phenotyped: {len(universe):,}. Lethal = at least one significant call to an MP term matching"
        f" `{LETHAL.pattern}`. Mouse to human through IMPC's `human_gene_symbol`.",
        "",
        "| IMPC call | Genes | With human symbol | DepMap common essential | Not common essential |",
        "|---|---:|---:|---:|---:|",
        f"| Lethal | {L['genes']:,} | {L['with_human_symbol']:,} | {pct(L['depmap_common_essential'], L['with_human_symbol'])}"
        f" | {pct(L['not_common_essential'], L['with_human_symbol'])} |",
        f"| Not lethal | {N['genes']:,} | {N['with_human_symbol']:,} | {pct(N['depmap_common_essential'], N['with_human_symbol'])}"
        f" | {pct(N['not_common_essential'], N['with_human_symbol'])} |",
        "",
        f"- Of the {len(ce_universe):,} phenotyped genes whose human ortholog is common essential,"
        f" {pct(len(ce_universe & lethal), len(ce_universe))} have an IMPC lethality call.",
        "",
        "## By lethality term",
        "",
        "| MP term | Genes (with human symbol) | DepMap common essential |",
        "|---|---:|---:|",
    ]
    for term, s in sorted(stage.items(), key=lambda kv: -kv[1]["genes"]):
        lines.append(f"| {term} | {s['with_human_symbol']:,} | {pct(s['depmap_common_essential'], s['with_human_symbol'])} |")
    lines.append("")
    (RESULTS / "ESSENTIALITY.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
