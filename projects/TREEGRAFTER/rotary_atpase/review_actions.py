"""Tabulate reviewer actions on rotary-ATP-synthase-family GO rows across the FliI/SctN reviews.

Reads the committed gene reviews (no hard-coded results) and writes review_actions.tsv.
Run: uv run --with pyyaml projects/TREEGRAFTER/rotary_atpase/review_actions.py
"""
import collections, csv, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).parent
REVIEWS = ["CAUVC/fliI", "HELPJ/fliI", "PSEPK/fliI", "ECOLI/fliI", "SALTY/fliI",
           "SALTY/sctN1", "SALTY/sctN2", "YEREN/sctN", "SHIFL/sctN"]
LEAK_TERMS = {"GO:0046933", "GO:0045259", "GO:0015986", "GO:0046961",
              "GO:1902600", "GO:0006754", "GO:0046034"}
PIPELINE = {"GO_REF:0000118": "TreeGrafter", "GO_REF:0000033": "PAINT IBA",
            "GO_REF:0000002": "InterPro2GO", "GO_REF:0000108": "GO logical inference"}


def goa_with(org_gene):
    """Map (term, reference) -> WITH/FROM from the gene's GOA file."""
    org, gene = org_gene.split("/")
    out = {}
    for r in csv.DictReader(open(ROOT / "genes" / org / gene / f"{gene}-goa.tsv"), delimiter="\t"):
        out[(r["GO TERM"], r["REFERENCE"])] = r["WITH/FROM"]
    return out


def main():
    rows = [("gene", "uniprot", "term_id", "term_label", "evidence", "reference", "pipeline", "with_from", "action")]
    for rg in REVIEWS:
        org, gene = rg.split("/")
        doc = yaml.safe_load(open(ROOT / "genes" / org / gene / f"{gene}-ai-review.yaml"))
        withs = goa_with(rg)
        for a in doc.get("existing_annotations", []):
            tid = a["term"]["id"]
            if tid not in LEAK_TERMS:
                continue
            ref = a.get("original_reference_id", "")
            rows.append((rg, doc["id"], tid, a["term"]["label"], a.get("evidence_type", ""), ref,
                         PIPELINE.get(ref, ref), withs.get((tid, ref), ""), a["review"]["action"]))
    with open(OUT / "review_actions.tsv", "w", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
    body = rows[1:]
    print(len(body), "rows;", dict(collections.Counter(r[8] for r in body)))
    for pipe, n in collections.Counter((r[6], r[8]) for r in body).most_common():
        print(" ", pipe, n)


if __name__ == "__main__":
    main()
