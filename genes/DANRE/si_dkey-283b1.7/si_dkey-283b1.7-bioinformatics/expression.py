"""Compare public expression calls for a zebrafish paralog pair and the
spotted gar (unduplicated outgroup) ortholog.

Sources, queried live:
  * Bgee REST API (https://www.bgee.org/api/), anatomical-entity expression
    calls (call type EXPRESSED), once for all data types and once for RNA-Seq
    only. RNA-Seq calls come from the same libraries for both zebrafish genes,
    so they are the most comparable; in situ calls depend on which gene was
    studied. Bgee reports only present calls; a missing tissue is not evidence
    of absence.
  * ZFIN wild-type expression download (wildtype-expression_fish.txt): number
    of curated wild-type expression records and structures per gene.

Usage (from the repository root):
    uv run python <this script> --zf ENSDARG_A:ZDB-GENE-A:label_a \
        --zf ENSDARG_B:ZDB-GENE-B:label_b --gar ENSLOCG:label
"""

import argparse
import csv
import io
import json
import urllib.request

BGEE = ("https://www.bgee.org/api/?page=gene&action=expression&gene_id={g}&species_id={sp}"
        "&cond_param=anat_entity&display_type=json{extra}")
ZFIN = "https://zfin.org/downloads/wildtype-expression_fish.txt"
HEADERS = {"User-Agent": "ai-gene-review/expression.py (python urllib)"}


def fetch(url: str, timeout: int) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    return urllib.request.urlopen(req, timeout=timeout).read()


def bgee(gene: str, species: int, rnaseq_only: bool) -> dict[str, float]:
    extra = "&data_type=RNA_SEQ" if rnaseq_only else ""
    d = json.loads(fetch(BGEE.format(g=gene, sp=species, extra=extra), 120))
    out = {}
    for c in d["data"]["calls"]:
        out[c["condition"]["anatEntity"]["name"]] = float(c["expressionScore"]["expressionScore"])
    return out


def zfin_records(zdb_ids: set[str]) -> dict[str, list[list[str]]]:
    raw = fetch(ZFIN, 300).decode("utf-8", "replace")
    out: dict[str, list[list[str]]] = {z: [] for z in zdb_ids}
    for row in csv.reader(io.StringIO(raw), delimiter="\t"):
        if row and row[0] in zdb_ids:
            out[row[0]].append(row)
    return out


def fmt(calls: dict[str, float]) -> str:
    return ", ".join(f"{k} ({v:.1f})" for k, v in sorted(calls.items(), key=lambda x: -x[1])) or "none"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zf", action="append", required=True, help="ENSDARG:ZDB-GENE:label")
    ap.add_argument("--gar", required=True, help="ENSLOCG:label")
    args = ap.parse_args()
    zf = [tuple(x.split(":", 2)) for x in args.zf]
    gar_id, gar_label = args.gar.split(":", 1)

    print("## Bgee, all data types (expression score in brackets)\n")
    allcalls = {}
    for ens, zdb, label in zf:
        allcalls[label] = bgee(ens, 7955, False)
        print(f"- zebrafish {label} ({ens}): {fmt(allcalls[label])}")
    print(f"- gar {gar_label} ({gar_id}): {fmt(bgee(gar_id, 7918, False))}")

    print("\n## Bgee, RNA-Seq only\n")
    rs = {}
    for ens, zdb, label in zf:
        rs[label] = bgee(ens, 7955, True)
        print(f"- zebrafish {label}: {fmt(rs[label])}")
    gar_rs = bgee(gar_id, 7918, True)
    print(f"- gar {gar_label}: {fmt(gar_rs)}")

    (la, lb) = [z[2] for z in zf]
    a, b = set(rs[la]), set(rs[lb])
    print("\n### RNA-Seq overlap between the zebrafish copies\n")
    print(f"- both: {', '.join(sorted(a & b)) or 'none'}")
    print(f"- {la} only: {', '.join(sorted(a - b)) or 'none'}")
    print(f"- {lb} only: {', '.join(sorted(b - a)) or 'none'}")
    print(f"- gar tissues with a call in neither zebrafish copy: "
          f"{', '.join(sorted(set(gar_rs) - a - b)) or 'none'} "
          "(gar and zebrafish RNA-Seq sample different tissue sets)")

    print("\n## ZFIN curated wild-type expression\n")
    recs = zfin_records({z[1] for z in zf})
    for ens, zdb, label in zf:
        rows = recs[zdb]
        structures = sorted({r[4] for r in rows})
        assays = sorted({r[9] for r in rows})
        pubs = sorted({r[11] for r in rows})
        print(f"- {label} ({zdb}): {len(rows)} records; assays: {', '.join(assays) or 'none'}; "
              f"publications: {', '.join(pubs) or 'none'}")
        if structures:
            print(f"  - structures: {', '.join(structures)}")


if __name__ == "__main__":
    main()
