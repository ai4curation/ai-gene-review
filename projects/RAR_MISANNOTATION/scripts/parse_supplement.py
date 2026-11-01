"""Parse the candidate-misannotation tables (S3-S6) of Wei et al. 2020 (PMID:32470107).

Downloads the authors' supplement (https://zhanggroup.org/RAR/SI.pdf) to the
git-ignored .cache/rar/ directory, extracts word positions with poppler's
``pdftotext -bbox``, and rebuilds each table row from layout:

- each row has exactly one GO id in the GO-term column (x < 140);
- the per-taxon count column holds a fixed number of integers per row
  (5 for the kingdom tables S3/S5, 2 for the phylum tables S4/S6), which
  gives each row's vertical span;
- example accessions form one consecutive run per row, cut by dynamic
  programming so that each run is centred on its row's GO id and every
  protein comes from a taxon that row could have flagged (annotation rate
  well below the row's top rate; UniProt lineage). Layout alone
  leaves off-by-one cuts between tall cells; the taxon check fixes them.

The supplement's footnote lists the five kingdom counts as Animals, Archaea,
Bacteria, Fungi, Plants, but the column header (and the data: nucleus is
0/28809/6/5925/7060) give Archaea, Animals, Bacteria, Fungi, Plants; the header
order is used. The "shaded" cell marking the flagged taxon is lost in text
extraction, so the flagged taxon is not inferred here; check_current_goa.py
takes it from the example proteins' UniProt lineage.

Usage:
    uv run python projects/RAR_MISANNOTATION/scripts/parse_supplement.py
"""

import re
import subprocess
import urllib.request
from pathlib import Path

import yaml

from check_current_goa import uniprot_info

ROOT = Path(__file__).resolve().parents[3]
CACHE = ROOT / ".cache" / "rar"
SI_URL = "https://zhanggroup.org/RAR/SI.pdf"
OUT = ROOT / "projects" / "RAR_MISANNOTATION" / "data" / "rar_supplement_cases.yaml"

# Supplement page ranges (1-based) per table, from its table of contents.
KINGDOM_ORDER = ["Archaea", "Animals", "Bacteria", "Fungi", "Plants"]
PHYLUM_ORDER = ["Vertebrates", "Invertebrates"]
HEADER_WORDS = {"GO", "term", "name", "Rate", "ratio"}
# Supplement Table S4 footnote: flagged in invertebrates and in Gallus gallus.
BOTH_PHYLUM_GROUPS = ("GO:0007565", "GO:0021987")

TABLES = {
    "S3": {"pages": [5, 6, 7], "release": "2019-06-03", "level": "kingdom", "ncounts": 5},
    "S4": {"pages": [8, 9], "release": "2019-06-03", "level": "phylum", "ncounts": 2},
    "S5": {"pages": [10, 11, 12, 13, 14], "release": "2018-11-06", "level": "kingdom", "ncounts": 5},
    "S6": {"pages": [15, 16], "release": "2018-11-06", "level": "phylum", "ncounts": 2},
}

WORD_RE = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>'
)
ACC_RE = re.compile(r"^(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})$")
EVIDENCE = {"IEA", "IBA", "ISS", "ISO", "ISM", "ISA", "IDA", "IMP", "IPI", "IGI", "IEP",
            "TAS", "NAS", "IC", "ND", "IKR", "IRD", "HDA", "HMP", "EXP", "RCA", "IGC", "HEP"}


def fetch_pdf() -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    pdf = CACHE / "SI.pdf"
    if not pdf.exists():
        urllib.request.urlretrieve(SI_URL, pdf)
    return pdf


def page_words(pdf: Path) -> list[list[tuple]]:
    html = CACHE / "SI.bbox.html"
    subprocess.run(["pdftotext", "-bbox", str(pdf), str(html)], check=True)
    pages = html.read_text().split("<page ")[1:]
    out = []
    for p in pages:
        words = []
        for x0, y0, x1, y1, text in WORD_RE.findall(p):
            words.append((float(x0), float(y0), float(x1), float(y1), text))
        out.append(words)
    return out


def parse_page(words, ncounts, groups, order, both_groups=()):
    gos = sorted((w for w in words if re.fullmatch(r"GO:\d{7}", w[4]) and w[0] < 140),
                 key=lambda w: w[1])
    if not gos:
        return []
    top = gos[0][1] - 60
    counts = sorted((w for w in words if 150 < w[0] < 200 and w[4].isdigit() and w[1] > top),
                    key=lambda w: w[1])
    if len(counts) != ncounts * len(gos):
        raise ValueError(f"{len(counts)} counts for {len(gos)} rows")
    rows = []
    for i, go in enumerate(gos):
        grp = counts[i * ncounts:(i + 1) * ncounts]
        rows.append({
            "go": go,
            "counts": [int(w[4]) for w in grp],
            "span": (grp[0][1], grp[-1][3]),
            "centre": (go[1] + go[3]) / 2,
        })

    def row_for(w):
        c = (w[1] + w[3]) / 2
        for r in rows:
            if r["span"][0] - 1 <= c <= r["span"][1] + 1:
                return r
        return min(rows, key=lambda r: abs(r["centre"] - c))

    for r in rows:
        r.update(accs=[], name=[], evidence=None, freq=None, pvals=[], ratio=None, aspect=None)
    for w in words:
        x, text = w[0], w[4]
        if w[1] < top:
            continue
        if 115 <= x < 140 and re.fullmatch(r"\((BP|MF|CC)\)", text):
            row_for(w)["aspect"] = text.strip("()")
        elif 200 <= x < 260 and text in EVIDENCE:
            row_for(w)["evidence"] = text
        elif 200 <= x < 260 and re.fullmatch(r"\([\d.]+\)", text):
            row_for(w)["freq"] = float(text.strip("()"))
        elif 260 <= x < 325 and re.fullmatch(r"\(?[\d.]+E-\d+\)?|\(?1\.00\)?", text):
            row_for(w)["pvals"].append(text.strip("()"))
        elif 325 <= x < 365 and re.fullmatch(r"[\d.]+E-\d+", text):
            row_for(w)["ratio"] = float(text)
        elif 365 <= x < 440:
            row_for(w)["name"].append((w[1], w[0], text))
    assign_accessions(rows, words, groups, order, both_groups)
    return rows


MISMATCH_PENALTY = 1000.0


# Annotated-protein totals N_t per taxon are not tabulated in the paper. They
# are back-calculated from its printed rate ratios, RAR = (n_min/N_min) /
# (n_max/N_max): N_Bacteria = 19922 is stated in the text; nucleus (fungal rate
# 0.347) gives Fungi; peptidoglycan biosynthesis (1 plant vs 182 bacterial,
# RAR 2.04E-3) gives Plants; sporulation (1 animal, RAR 4.61E-4) gives Animals;
# histone acetylation (1 archaeal vs 117 fungal, RAR 3.77E-2) gives Archaea.
# Female pregnancy and compound eye development both give N_vert/N_invert = 3.07.
TAXON_SIZE = {
    "Archaea": 3873, "Animals": 156600, "Bacteria": 19922, "Fungi": 17075, "Plants": 53660,
    "Vertebrates": 3.07, "Invertebrates": 1.0,
}
# The paper screened RAR < 0.1 but lists phylum rows up to 0.164; 0.2 admits them.
FLAG_RATIO = 0.2


def flaggable(counts, order):
    """Taxa a row could have flagged: annotation rate at most FLAG_RATIO of the top rate."""
    rates = {t: c / TAXON_SIZE[t] for t, c in zip(order, counts)}
    top = max(rates.values())
    return {t for t, r in rates.items() if 0 < r <= FLAG_RATIO * top}


def assign_accessions(rows, words, groups, order, both_groups=()):
    """Split the example-protein column into consecutive per-row groups.

    Each row's cell is vertically centred on its GO id, and a cell can be far
    taller than the row's other cells (up to ~40 accessions), so neither the
    count span nor the nearest centre bounds it. The column is cut into one
    non-empty run per row, choosing the cuts (by dynamic programming) that
    best centre every run on its row's GO id.
    """
    accs = sorted(((w[1] + w[3]) / 2, w[4].rstrip(","))
                  for w in words if w[0] >= 440 and ACC_RE.match(w[4].rstrip(",")))
    n, m = len(accs), len(rows)
    if n < m:
        raise ValueError(f"{n} accessions for {m} rows")
    inf = float("inf")
    # best[k][j]: cost of placing the first j accessions into the first k rows
    best = [[inf] * (n + 1) for _ in range(m + 1)]
    cut = [[0] * (n + 1) for _ in range(m + 1)]
    best[0][0] = 0.0
    for k in range(1, m + 1):
        row = rows[k - 1]
        centre = row["centre"]
        allowed = set(order) if row["go"][4] in both_groups else flaggable(row["counts"], order)
        bad = [0] * (n + 1)  # prefix count of proteins whose group is not allowed
        for x, (_, acc) in enumerate(accs):
            g = groups.get(acc)
            bad[x + 1] = bad[x] + (g is not None and g not in allowed)
        for j in range(k, n + 1):
            for i in range(k - 1, j):
                if best[k - 1][i] == inf:
                    continue
                c = (best[k - 1][i] + abs((accs[i][0] + accs[j - 1][0]) / 2 - centre)
                     + MISMATCH_PENALTY * (bad[j] - bad[i]))
                if c < best[k][j]:
                    best[k][j], cut[k][j] = c, i
    j = n
    for k in range(m, 0, -1):
        i = cut[k][j]
        rows[k - 1]["accs"] = accs[i:j]
        j = i


def main():
    pages = page_words(fetch_pdf())
    all_accs = {w[4].rstrip(",") for p in pages for w in p
                if w[0] >= 440 and ACC_RE.match(w[4].rstrip(","))}
    groups = {}
    for acc, i in uniprot_info(all_accs).items():
        g = i.get("group")
        if g in ("Vertebrates", "Invertebrates"):
            groups[acc] = g
            groups[acc + "#kingdom"] = "Animals"
        elif g:
            groups[acc] = groups[acc + "#kingdom"] = g
    cases = []
    for table, spec in TABLES.items():
        order = KINGDOM_ORDER if spec["level"] == "kingdom" else PHYLUM_ORDER
        level_groups = ({a: groups[a + "#kingdom"] for a in all_accs if a + "#kingdom" in groups}
                        if spec["level"] == "kingdom" else
                        {a: groups[a] for a in all_accs if groups.get(a) in PHYLUM_ORDER})
        for pno in spec["pages"]:
            for r in parse_page(pages[pno - 1], spec["ncounts"], level_groups, order,
                                BOTH_PHYLUM_GROUPS):
                tokens = [t for _, _, t in sorted(r["name"])]
                while tokens and tokens[0] in HEADER_WORDS:
                    tokens.pop(0)
                name = " ".join(tokens).replace("- ", "-")
                cases.append({
                    "table": table,
                    "release": spec["release"],
                    "analysis": spec["level"],
                    "go_id": r["go"][4],
                    "go_label_in_paper": name,
                    "aspect": r["aspect"],
                    "annotated_protein_counts": dict(zip(order, r["counts"])),
                    "most_frequent_evidence": r["evidence"],
                    "evidence_frequency": r["freq"],
                    "p_value": r["pvals"][0] if r["pvals"] else None,
                    "q_value": r["pvals"][1] if len(r["pvals"]) > 1 else None,
                    "rate_ratio": r["ratio"],
                    "example_proteins": [a for _, a in sorted(r["accs"])],
                })
    per_table = {t: sum(c["table"] == t for c in cases) for t in TABLES}
    OUT.write_text(yaml.safe_dump({
        "source": {
            "reference": "PMID:32470107",
            "supplement_url": SI_URL,
            "generated_by": "projects/RAR_MISANNOTATION/scripts/parse_supplement.py",
            "rows_per_table": per_table,
        },
        "cases": cases,
    }, sort_keys=False, width=100))
    print(per_table, "->", OUT)


if __name__ == "__main__":
    main()
