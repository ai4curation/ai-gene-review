"""Which PTHR11937 members carry ATP binding, ADP binding, or both?

Written to check a claim this review had inherited from the merged ACTR10 review and
restated as its own: that "ACTA1 is one of only two gene products in this family that
carry both". The measurement refuted it. ACTA1 is the **only** member of PTHR11937
carrying GO:0043531 ADP binding at all, and 31 members carry GO:0005524 ATP binding -
so the sibling's list, which was about ATP binding alone, had been converted into a
count about two terms. Relay a sibling review's claim as a claim, not as a fact.

Two traps this script exists to avoid, both of which produced a wrong answer first:

1. **Querying by GO term alone paginates into a false negative.** GO:0043531 has
   ~205,000 annotations across all of GO and GO:0005524 has ~9.6 million; a single
   unpaged request returns page one and intersecting that with the family yields an
   empty set that looks like "no member carries this term". The query is therefore
   keyed on the family's own accessions.
2. **Per-accession queries are too slow to finish** (533 members x 2 terms). QuickGO
   accepts a comma-separated geneProductId list, so requests are batched, and each
   batch asserts its result was not itself truncated.
"""
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRIES = HERE.parents[3] / "interpro" / "panther" / "PTHR11937" / "PTHR11937-entries.csv"
OUT = HERE / "nucleotide_terms_in_family.json"

TERMS = {
    "GO:0005524": "ATP binding",
    "GO:0043531": "ADP binding",
}
BATCH = 100
PAGE = 200
SUBJECT = "P68133"


def get(url: str) -> dict:
    last: Exception | None = None
    for _ in range(4):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            time.sleep(3)
    raise RuntimeError(f"failed after 4 attempts: {url}") from last


def members() -> list[str]:
    if not ENTRIES.exists():
        raise SystemExit(
            f"missing input {ENTRIES}; the PANTHER family cache is required "
            "(interpro/panther/PTHR11937/PTHR11937-entries.csv)"
        )
    with ENTRIES.open() as fh:
        rows = list(csv.DictReader(fh))
    accs = [r["id"] for r in rows if r.get("entry_type") == "protein"]
    if not accs:
        raise RuntimeError(f"{ENTRIES} yielded no protein entries")
    return accs


def holders(accs: list[str], go_id: str) -> dict[str, dict]:
    """Family members annotated to go_id, keyed on accession."""
    found: dict[str, dict] = {}
    for i in range(0, len(accs), BATCH):
        chunk = accs[i:i + BATCH]
        ids = ",".join(f"UniProtKB:{a}" for a in chunk)
        url = ("https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId="
               + urllib.parse.quote(ids, safe=",:") + f"&goId={go_id}&limit={PAGE}")
        d = get(url)
        total = d["numberOfHits"]
        # Refuse a silently truncated batch. Without this the script would report a
        # subset as if it were the whole answer - the same failure the term-keyed query
        # produces, just harder to notice.
        if total > PAGE:
            raise RuntimeError(
                f"{go_id} batch at offset {i} returned {total} hits, above the page size "
                f"{PAGE}; reduce BATCH or add paging rather than trusting page one"
            )
        for r in d["results"]:
            acc = r["geneProductId"].split(":")[-1].split("-")[0]
            rec = found.setdefault(acc, {"symbol": r["symbol"], "evidence": set()})
            rec["evidence"].add(r["goEvidence"])
    return found


def main() -> None:
    accs = members()
    print(f"{len(accs)} PTHR11937 protein members, batched {BATCH} at a time")
    per_term = {go: holders(accs, go) for go in TERMS}

    for go, label in TERMS.items():
        h = per_term[go]
        print(f"\n{go} {label}: {len(h)} family member(s)")
        for acc, rec in sorted(h.items(), key=lambda kv: kv[1]["symbol"]):
            print(f"  {acc:8} {rec['symbol']:12} {','.join(sorted(rec['evidence']))}")

    both = sorted(set(per_term["GO:0005524"]) & set(per_term["GO:0043531"]))
    print(f"\ncarrying BOTH: {len(both)} -> "
          f"{[(a, per_term['GO:0043531'][a]['symbol']) for a in both]}")
    if SUBJECT not in both:
        raise RuntimeError(
            f"{SUBJECT} (ACTA1) does not carry both terms; the review says it does"
        )

    result = {
        "family": "PTHR11937",
        "n_members_queried": len(accs),
        "terms": TERMS,
        "holders": {
            go: {a: {"symbol": r["symbol"], "evidence": sorted(r["evidence"])}
                 for a, r in sorted(h.items())}
            for go, h in per_term.items()
        },
        "n_with_atp_binding": len(per_term["GO:0005524"]),
        "n_with_adp_binding": len(per_term["GO:0043531"]),
        "accessions_with_both": both,
        "n_with_both": len(both),
        "subject_is_sole_adp_holder": list(per_term["GO:0043531"]) == [SUBJECT],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    sys.exit(main())
