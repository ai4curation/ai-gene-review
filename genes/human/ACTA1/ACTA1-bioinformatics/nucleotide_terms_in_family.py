"""Which PTHR11937 members carry ATP binding, ADP binding, or both?

Written to check a claim this review had inherited from the merged ACTR10 review and
restated as its own: that ACTA1 was one of a pair of family members carrying both terms.
The measurement refuted it - but read the SCOPE of what is measured, because it is
narrower than "the family".

SCOPE. The member list comes from interpro/panther/PTHR11937/PTHR11937-entries.csv,
which this repo builds from InterPro's **reviewed-only** protein endpoint
(fetch_interpro_family_simple.py: /protein/reviewed/entry/...). That is 533 Swiss-Prot
entries, against the ~88,887 proteins PTHR11937's own metadata reports (parsed from
PTHR11937-metadata.yaml, not transcribed) - about 0.6%. So
every count here is over the REVIEWED subset, and the script says so in its output and
in its JSON keys. A claim about the whole family is not something this measurement makes.

RESULT (reviewed subset): 31 members carry GO:0005524 ATP binding and exactly one -
ACTA1 - carries GO:0043531 ADP binding, so ACTA1 is the sole holder of both. The
sibling's list had been about ATP binding alone. Relay a sibling review's claim as a
claim, not as a fact.

Whether it extends family-wide is an ARGUMENT, not this measurement, and is labelled as
one wherever it is used: ACTA1's GO:0043531 is a manual TAS annotation, unreviewed
TrEMBL entries receive only IEA, and no IEA pipeline maps the actin fold to ADP binding -
so an unreviewed member acquiring the term is unlikely. Unlikely is not measured.

Two traps this script exists to avoid, both of which produced a wrong answer first:

1. **Querying by GO term alone paginates into a false negative.** GO:0043531 has
   ~205,000 annotations across all of GO and GO:0005524 has ~9.6 million; a single
   unpaged request returns page one and intersecting that with the family yields an
   empty set that looks like "no member carries this term". The query is therefore
   keyed on the family's own accessions.
2. **Per-accession queries are too slow to finish** (533 members x 2 terms). QuickGO
   accepts a comma-separated geneProductId list, so requests are batched, and each
   batch asserts its result was not itself truncated - by comparing the reported hit
   count against the number of rows ACTUALLY RETURNED, never against the requested page
   size, since a service that clamps the limit would satisfy a constant-based check while
   handing back fewer rows.

goUsage=descendants over is_a,part_of is set, matching the sibling resolve_withfrom.py, so
a member annotated only to a child term is counted rather than missed.
"""
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
FAMILY_DIR = HERE.parents[3] / "interpro" / "panther" / "PTHR11937"
ENTRIES = FAMILY_DIR / "PTHR11937-entries.csv"
METADATA = FAMILY_DIR / "PTHR11937-metadata.yaml"
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


def family_protein_total() -> int:
    """Total proteins in PTHR11937, PARSED from the family metadata.

    The numerator (533 reviewed members) is read from a file, so the denominator must be
    too. Transcribing it would leave the only hand-typed number in this script free to go
    stale: a refreshed member list would move the numerator and fire the audit, while the
    denominator and the derived percentage silently would not.
    """
    if not METADATA.exists():
        raise SystemExit(f"missing {METADATA}; the PANTHER family cache is required")
    # Require EXACTLY ONE match, as mature_chain_start() does. Taking the first `proteins:`
    # line at any nesting would silently pick the wrong one if the metadata ever grew a
    # second counter block - the reviewer's point, and the same "first match wins" laxity
    # that makes a parser quietly authoritative about the wrong number.
    hits = re.findall(r"^\s*proteins:\s*(\d+)\s*$", METADATA.read_text(), flags=re.M)
    if len(hits) != 1:
        raise RuntimeError(
            f"expected exactly one `proteins:` count in {METADATA.name}, found "
            f"{len(hits)}: {hits}; refusing to guess which is the family total"
        )
    return int(hits[0])


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
               + urllib.parse.quote(ids, safe=",:") + f"&goId={go_id}&limit={PAGE}"
               + "&goUsage=descendants&goUsageRelationships=is_a,part_of")
        d = get(url)
        total = d["numberOfHits"]
        returned = len(d["results"])
        # Refuse a silently truncated batch. Compare the hit count against what was
        # ACTUALLY RETURNED, never against the requested page size: a service that clamps
        # the limit rather than rejecting it would satisfy a constant-based check while
        # handing back fewer rows, which is exactly the silent truncation this guard
        # exists to prevent. (Measured: QuickGO does honour limit=200 here - but the
        # check must not depend on that remaining true.)
        if total > returned:
            raise RuntimeError(
                f"{go_id} batch at offset {i} reports {total} hits but returned only "
                f"{returned} rows; the response is truncated. Reduce BATCH or add paging "
                "rather than trusting the first page."
            )
        for r in d["results"]:
            acc = r["geneProductId"].split(":")[-1].split("-")[0]
            rec = found.setdefault(acc, {"symbol": r["symbol"], "evidence": set()})
            rec["evidence"].add(r["goEvidence"])
    return found


def main() -> None:
    accs = members()
    total = family_protein_total()
    print(f"{len(accs)} REVIEWED (Swiss-Prot) PTHR11937 members, batched {BATCH} at a time")
    print(f"  scope: {len(accs)} of the {total:,} proteins PTHR11937 metadata reports "
          f"({len(accs) / total:.1%}); InterPro's /protein/reviewed/ endpoint is "
          "reviewed-only, so nothing here is a claim about the whole family")
    per_term = {go: holders(accs, go) for go in TERMS}

    for go, label in TERMS.items():
        h = per_term[go]
        print(f"\n{go} {label}: {len(h)} reviewed member(s)")
        for acc, rec in sorted(h.items(), key=lambda kv: kv[1]["symbol"]):
            print(f"  {acc:8} {rec['symbol']:12} {','.join(sorted(rec['evidence']))}")

    both = sorted(set(per_term["GO:0005524"]) & set(per_term["GO:0043531"]))
    print(f"\ncarrying BOTH: {len(both)} -> "
          f"{[(a, per_term['GO:0043531'][a]['symbol']) for a in both]}")
    if SUBJECT not in both:
        raise RuntimeError(
            f"{SUBJECT} (ACTA1) does not carry both terms; the review says it does"
        )
    print("\nNOTE: counts are over REVIEWED entries only. goUsage=descendants is set (as in "
          "the sibling resolve_withfrom.py), so a member annotated to a child term counts.")

    result = {
        "family": "PTHR11937",
        "member_scope": "reviewed (Swiss-Prot) members only, from InterPro's "
                        "/protein/reviewed/ endpoint",
        "n_reviewed_members_queried": len(accs),
        "n_proteins_in_family_per_panther_metadata": total,
        "fraction_of_family_measured": round(len(accs) / total, 4),
        "terms": TERMS,
        "holders": {
            go: {a: {"symbol": r["symbol"], "evidence": sorted(r["evidence"])}
                 for a, r in sorted(h.items())}
            for go, h in per_term.items()
        },
        "n_reviewed_with_atp_binding": len(per_term["GO:0005524"]),
        "n_reviewed_with_adp_binding": len(per_term["GO:0043531"]),
        "accessions_with_both": both,
        "n_reviewed_with_both": len(both),
        "subject_is_sole_adp_holder_among_reviewed": list(per_term["GO:0043531"]) == [SUBJECT],
        "go_usage": "descendants over is_a,part_of - a member annotated only to a child "
                    "term is counted, matching the sibling resolve_withfrom.py",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    sys.exit(main())
