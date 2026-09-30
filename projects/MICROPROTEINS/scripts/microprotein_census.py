#!/usr/bin/env python3
"""Census of human microproteins in UniProt and their GO annotation coverage.

Fetches (and caches under ``projects/MICROPROTEINS/tmp/``, which is gitignored):

* every reviewed (Swiss-Prot) human UniProtKB entry of length <= MAX_LEN,
* the counts of unreviewed (TrEMBL) human reference-proteome entries by length,
* the current human GOA GAF from the GO Consortium release.

It then classifies each short Swiss-Prot entry into a coarse class (secreted peptide,
ribosomal, Ig/TCR gene segment, sORF-class "novel" microprotein, ...), joins the GAF,
and writes:

* ``data/human_microproteins.tsv``     one row per Swiss-Prot entry <= 100 aa
* ``data/go_coverage_by_class.tsv``    annotation coverage per class
* ``data/go_coverage_by_length.tsv``   coverage per length bin, whole proteome
* ``data/census_summary.md``           human-readable summary (pasted into the project page)

No numbers are hard-coded; re-running against a newer UniProt/GOA release will change them.

Usage:  python3 projects/MICROPROTEINS/scripts/microprotein_census.py [--refresh]
"""

from __future__ import annotations

import argparse
import collections
import csv
import gzip
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
CACHE = HERE / "tmp"
OUT = HERE / "data"

MICRO_LEN = 100  # conventional microprotein cutoff
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
GAF_URL = "https://current.geneontology.org/annotations/goa_human.gaf.gz"
FIELDS = (
    "accession,gene_primary,protein_name,length,annotation_score,protein_existence,"
    "keyword,ft_signal,ft_transmem,ft_propep,ft_peptide,cc_function,date_created,xref_hgnc"
)

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
PHYLO = {"IBA", "IBD", "IKR", "IRD"}
ELECTRONIC = {"IEA"}
# everything else (ISS, ISO, ISA, ISM, IGC, RCA, TAS, NAS, IC, ND) = "other"
PROTEIN_BINDING = "GO:0005515"
ROOTS = {"GO:0003674", "GO:0008150", "GO:0005575"}  # used with ND


def fetch_uniprot(query: str, fields: str, dest: Path, refresh: bool) -> Path:
    """Paginated UniProt TSV download (the /stream endpoint truncates on slow links)."""
    if dest.exists() and not refresh:
        return dest
    url = UNIPROT_SEARCH + "?" + urllib.parse.urlencode(
        {"query": query, "fields": fields, "format": "tsv", "size": 500}
    )
    header, rows, expected = None, [], None
    while url:
        with urllib.request.urlopen(url, timeout=300) as resp:
            expected = int(resp.headers.get("X-Total-Results", "0"))
            text = resp.read().decode()
            link = resp.headers.get("Link", "")
        lines = text.rstrip("\n").split("\n")
        header = header or lines[0]
        rows.extend(lines[1:])
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None
        print(f"  uniprot: {len(rows)}/{expected}", file=sys.stderr)
    if len(rows) != expected:
        raise RuntimeError(f"UniProt download incomplete: {len(rows)} of {expected}")
    dest.write_text(header + "\n" + "\n".join(rows) + "\n")
    return dest


def uniprot_count(query: str) -> int:
    url = UNIPROT_SEARCH + "?" + urllib.parse.urlencode({"query": query, "size": 1})
    with urllib.request.urlopen(url, timeout=120) as resp:
        return int(resp.headers["X-Total-Results"])


def fetch_gaf(refresh: bool) -> Path:
    dest = CACHE / "goa_human.gaf.gz"
    if not dest.exists() or refresh:
        print("  downloading GOA human GAF", file=sys.stderr)
        urllib.request.urlretrieve(GAF_URL, dest)
    return dest


def read_gaf(path: Path) -> dict[str, list[tuple[str, str, str, str]]]:
    """accession -> list of (go_id, aspect, evidence, qualifier)."""
    ann: dict[str, list] = collections.defaultdict(list)
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            c = line.rstrip("\n").split("\t")
            if c[0] != "UniProtKB":
                continue
            acc = c[1].split("-")[0]  # fold isoform-level annotations onto the entry
            ann[acc].append((c[4], c[8], c[6], c[3]))
    return ann


# --- classification ---------------------------------------------------------------

NOVEL_NAME = re.compile(
    r"uncharacterized|small integral membrane|micropeptide|microprotein|upstream open reading"
    r"|alternative protein|small open reading|long intergenic|lncRNA|putative",
    re.I,
)
NOVEL_SYMBOL = re.compile(r"^(C\d+orf\d+|CXorf\d+|SMIM\d+|LINC\d+|.*-AS\d*|.*URF|.*OS\d*)$")
HUMANIN = re.compile(r"^(MT-RNR|MTRNR2L|MT-?ULYSSES|MOTS)", re.I)


def classify(row: dict) -> str:
    sym = row["Gene Names (primary)"] or ""
    name = row["Protein names"] or ""
    kw = row["Keywords"] or ""
    if re.match(r"^(IG[HKL][VDJC]|TR[ABDG][VDJC])", sym):
        return "Ig/TCR gene segment"
    if HUMANIN.match(sym) or "Humanin" in name:
        return "mtDNA-rRNA-encoded peptide (humanin-like)"
    if re.match(r"^(KRTAP|LCE\d|SPRR|FLG|LOR)", sym) or "Keratinization" in kw:
        return "keratin-associated / cornified envelope"
    if "Ribosomal protein" in kw or re.search(r"ribosomal protein", name, re.I):
        return "ribosomal protein"
    if re.search(r"^MT-", sym) or re.search(
        r"NADH dehydrogenase|cytochrome c oxidase|ATP synthase|cytochrome b-c1|ubiquinol-cytochrome",
        name, re.I,
    ):
        return "OXPHOS subunit"
    if "Metal-thiolate cluster" in kw or re.match(r"^MT\d", sym):
        return "metallothionein"
    if row["Signal peptide"] or any(k in kw for k in ("Secreted", "Hormone", "Antimicrobial", "Cytokine")):
        return "secreted peptide / hormone / defensin"
    if NOVEL_NAME.search(name) or NOVEL_SYMBOL.match(sym) or (row["Date of creation"] or "") >= "2013":
        # PE1 (protein level) / PE2 (transcript level) vs PE3-5 (homology/predicted/uncertain)
        pe = row["Protein existence"] or ""
        if pe.startswith("Evidence at protein") and not name.lower().startswith("putative"):
            return "sORF-class microprotein, protein-level evidence"
        return "sORF-class microprotein, putative (no protein-level evidence)"
    return "other characterized small protein"


def go_labels(ids: set[str], refresh: bool) -> dict[str, str]:
    """Look up GO term names from QuickGO (cached)."""
    cache = CACHE / "go_labels.tsv"
    labels = {}
    if cache.exists() and not refresh:
        labels = dict(line.rstrip("\n").split("\t", 1) for line in cache.open() if "\t" in line)
    todo = sorted(i for i in ids if i not in labels)
    for k in range(0, len(todo), 100):
        chunk = ",".join(todo[k:k + 100])
        url = f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{chunk}"
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            for t in json.load(resp)["results"]:
                labels[t["id"]] = t["name"]
    cache.write_text("".join(f"{k}\t{v}\n" for k, v in sorted(labels.items())))
    return labels


def summarise(anns: list[tuple[str, str, str, str]]) -> dict:
    pos = [a for a in anns if not a[3].startswith("NOT")]
    informative = [a for a in pos if a[0] != PROTEIN_BINDING and a[0] not in ROOTS]
    ev = collections.Counter()
    for go, aspect, code, _ in informative:
        if code in EXPERIMENTAL:
            ev["exp"] += 1
        elif code in PHYLO:
            ev["iba"] += 1
        elif code in ELECTRONIC:
            ev["iea"] += 1
        else:
            ev["other"] += 1
    exp_aspects = sorted({a for _, a, c, _ in informative if c in EXPERIMENTAL})
    return {
        "n_annotations": len(pos),
        "n_informative": len(informative),
        "n_exp": ev["exp"],
        "n_iba": ev["iba"],
        "n_iea": ev["iea"],
        "n_other": ev["other"],
        "only_protein_binding_or_root": int(bool(pos) and not informative),
        "exp_aspects": "".join(exp_aspects),
        "has_MF": int(any(a == "F" for _, a, _, _ in informative)),
        "has_BP": int(any(a == "P" for _, a, _, _ in informative)),
        "has_CC": int(any(a == "C" for _, a, _, _ in informative)),
        "go_terms": ";".join(sorted({g for g, *_ in informative})),
        "exp_go_terms": ";".join(sorted({f"{g}|{a}|{c}" for g, a, c, _ in informative if c in EXPERIMENTAL})),
    }


def coverage(rows: list[dict]) -> dict:
    n = len(rows)
    pct = lambda k: round(100 * sum(1 for r in rows if r[k]) / n, 1) if n else 0.0  # noqa: E731
    return {
        "n": n,
        "pct_any_go": round(100 * sum(1 for r in rows if r["n_annotations"]) / n, 1) if n else 0,
        "pct_informative_go": pct("n_informative"),
        "pct_experimental": pct("n_exp"),
        "pct_MF": pct("has_MF"),
        "pct_BP": pct("has_BP"),
        "pct_CC": pct("has_CC"),
        "pct_only_protein_binding": pct("only_protein_binding_or_root"),
        "median_informative": sorted(r["n_informative"] for r in rows)[n // 2] if n else 0,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--refresh", action="store_true", help="re-download UniProt and GAF")
    args = ap.parse_args()
    CACHE.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)

    # Whole reviewed human proteome (lightweight fields) for the length-bin baseline.
    all_tsv = fetch_uniprot(
        "reviewed:true AND organism_id:9606", "accession,length", CACHE / "sp_human_lengths.tsv", args.refresh
    )
    short_tsv = fetch_uniprot(
        f"reviewed:true AND organism_id:9606 AND length:[1 TO {MICRO_LEN}]",
        FIELDS,
        CACHE / "sp_human_micro.tsv",
        args.refresh,
    )
    ann = read_gaf(fetch_gaf(args.refresh))

    # -- baseline by length bin
    bins = [(1, 50), (51, 100), (101, 150), (151, 300), (301, 600), (601, 10**6)]
    by_bin: dict[str, list] = collections.defaultdict(list)
    with open(all_tsv) as fh:
        for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            ln = int(r["Length"])
            label = next(f"{a}-{b}" if b < 10**6 else f">{a - 1}" for a, b in bins if a <= ln <= b)
            by_bin[label].append(summarise(ann.get(r["Entry"], [])))
    with open(OUT / "go_coverage_by_length.tsv", "w") as fh:
        w = None
        for a, b in bins:
            label = f"{a}-{b}" if b < 10**6 else f">{a - 1}"
            row = {"length_bin": label, **coverage(by_bin[label])}
            w = w or csv.DictWriter(fh, fieldnames=list(row), delimiter="\t")
            if fh.tell() == 0:
                w.writeheader()
            w.writerow(row)

    # -- short Swiss-Prot entries, classified
    micro = []
    with open(short_tsv) as fh:
        for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            s = summarise(ann.get(r["Entry"], []))
            micro.append({
                "accession": r["Entry"],
                "symbol": r["Gene Names (primary)"],
                "length": int(r["Length"]),
                "class": classify(r),
                "protein_existence": r["Protein existence"],
                "annotation_score": r["Annotation"],
                "created": r["Date of creation"],
                "signal_peptide": int(bool(r["Signal peptide"])),
                "transmembrane": int(bool(r["Transmembrane"])),
                "protein_name": r["Protein names"],
                **s,
                "function_cc": (r["Function [CC]"] or "").replace("FUNCTION: ", "")[:300],
            })
    labels = go_labels({t.split("|")[0] for r in micro for t in r["exp_go_terms"].split(";") if t}, args.refresh)
    for r in micro:
        r["exp_go_terms"] = "; ".join(
            f"{labels.get(t.split('|')[0], t.split('|')[0])} [{t.split('|')[0]}, {t.split('|')[2]}]"
            for t in r["exp_go_terms"].split(";") if t
        )
    micro.sort(key=lambda r: (r["class"], r["symbol"] or r["accession"]))
    with open(OUT / "human_microproteins.tsv", "w") as fh:
        w = csv.DictWriter(fh, fieldnames=list(micro[0]), delimiter="\t")
        w.writeheader()
        w.writerows(micro)

    by_class: dict[str, list] = collections.defaultdict(list)
    for r in micro:
        by_class[r["class"]].append(r)
    with open(OUT / "go_coverage_by_class.tsv", "w") as fh:
        w = None
        for cls in sorted(by_class, key=lambda c: -len(by_class[c])):
            row = {"class": cls, **coverage(by_class[cls])}
            w = w or csv.DictWriter(fh, fieldnames=list(row), delimiter="\t")
            if fh.tell() == 0:
                w.writeheader()
            w.writerow(row)

    # -- unreviewed (TrEMBL) scale
    trembl = {
        "trembl_ref_proteome_le100_nonfragment": uniprot_count(
            f"reviewed:false AND proteome:UP000005640 AND length:[1 TO {MICRO_LEN}] AND fragment:false"
        ),
    }

    # -- markdown summary
    L = ["# Human microprotein census (auto-generated)", ""]
    L.append(f"Swiss-Prot human entries <= {MICRO_LEN} aa: **{len(micro)}**; "
             f"unreviewed reference-proteome entries <= {MICRO_LEN} aa (non-fragment): "
             f"**{trembl['trembl_ref_proteome_le100_nonfragment']}**.")
    L += ["", "## GO coverage by class (Swiss-Prot <= 100 aa)", "",
          "| class | n | any GO | informative GO | experimental | MF | BP | only protein binding |",
          "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for cls in sorted(by_class, key=lambda c: -len(by_class[c])):
        c = coverage(by_class[cls])
        L.append(f"| {cls} | {c['n']} | {c['pct_any_go']}% | {c['pct_informative_go']}% | "
                 f"{c['pct_experimental']}% | {c['pct_MF']}% | {c['pct_BP']}% | {c['pct_only_protein_binding']}% |")
    L += ["", "## GO coverage by length (all Swiss-Prot human)", "",
          "| length | n | any GO | informative GO | experimental | MF | BP |", "|---|---:|---:|---:|---:|---:|---:|"]
    for a, b in bins:
        label = f"{a}-{b}" if b < 10**6 else f">{a - 1}"
        c = coverage(by_bin[label])
        L.append(f"| {label} | {c['n']} | {c['pct_any_go']}% | {c['pct_informative_go']}% | "
                 f"{c['pct_experimental']}% | {c['pct_MF']}% | {c['pct_BP']}% |")
    L += ["", "## sORF-class microproteins with protein-level evidence", "",
          "| symbol (UniProt gene) | acc | aa | informative GO | exp | IBA | IEA | experimental GO terms | name |",
          "|---|---|---:|---:|---:|---:|---:|---|---|"]
    for r in by_class.get("sORF-class microprotein, protein-level evidence", []):
        L.append(f"| {r['symbol']} | {r['accession']} | {r['length']} | {r['n_informative']} | {r['n_exp']} | "
                 f"{r['n_iba']} | {r['n_iea']} | {r['exp_go_terms'] or '-'} | {r['protein_name'].split(' (')[0][:60]} |")
    (OUT / "census_summary.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:30]))


if __name__ == "__main__":
    main()
