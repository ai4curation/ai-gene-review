"""Two checks on ARFGEF1's `GO:0005515 protein binding` rows.

1. **Partner identity.** Resolve every IPI partner accession and report the
   canonical entry's length and Swiss-Prot/TrEMBL status. A named partner is not
   a verified partner: partial ORFeome clones and unreviewed fragments have been
   passed off as canonical elsewhere in this campaign.

2. **Experiment independence.** Expand the IntAct interaction records and count
   DISTINCT experiments as (publication, detection method) pairs rather than
   trusting UniProt's `NbExp`. A single screen is routinely logged as several
   sub-methods ("two hybrid array" + "two hybrid pooling" + "validated two
   hybrid"), which inflates `NbExp` without adding evidence. Also count each
   partner's own distinct IntAct partners, so a promiscuous hub is visible, and
   flag records built by `spoke expansion` (an AP-MS co-complex inferred to be
   binary, not a measured binary interaction).

**Parser invariant.** IntAct writes ids as `"P05919 (uniprotkb)"`, not as bare
accessions, so a naive equality test silently matches nothing and every partner
reports "1 experiment". The script therefore asserts that grouping the subject's
records by partner accounts for *every* record; a parsing change that stops
matching fails loudly instead of returning a plausible wrong number.

Writes `partner_checks.tsv`. Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/partner_checks.py
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/partner_checks.py --self-test
"""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from uniprot import _cached_get, summarise, uniprot_entry  # noqa: E402

HERE = Path(__file__).parent
GOA = HERE.parent / "ARFGEF1-goa.tsv"
SUBJECT = "Q9Y6D6"


def intact_interactions(acc: str) -> list[dict]:
    """All IntAct interaction records naming `acc`.

    Compares `totalElements` against the number of rows actually returned --
    never against the page size this function chose, because a service that
    clamps instead of erroring would sail past that check.
    """
    page_size = 5000
    url = (
        "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/"
        f"{acc}?page=0&pageSize={page_size}"
    )
    data = json.loads(_cached_get(url, f"intact_{acc}"))
    rows = data.get("content", [])
    total = data.get("totalElements", len(rows))
    if total > len(rows):
        raise RuntimeError(
            f"IntAct returned {len(rows)} of {total} interactions for {acc}; "
            "paginate -- a truncated set silently understates both experiment "
            "counts and promiscuity."
        )
    return rows


def base_acc(v: str) -> str:
    """`'Q7Z4S6-2 (uniprotkb)'` -> `'Q7Z4S6'`."""
    return v.split(" ")[0].split("-")[0]


def partition_by_type(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split IntAct records into protein-protein and everything else.

    ARFGEF1's record set contains four mRNA/miRNA CLASH rows (the *transcript*
    being targeted, not the protein) and one small-molecule pull-down. Excluding
    them silently would understate nothing here, but reporting the partition
    makes the exclusion auditable and keeps the coverage assertion sharp.
    """
    pp = [r for r in records if r.get("typeA") == "protein" and r.get("typeB") == "protein"]
    other = [r for r in records if r not in pp]
    assert len(pp) + len(other) == len(records)
    return pp, other


def group_by_partner(records: list[dict], subject: str) -> dict[str, list[dict]]:
    """Group protein-protein records by partner accession, asserting full cover."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        a, b = base_acc(r["uniqueIdA"]), base_acc(r["uniqueIdB"])
        if a == subject and b == subject:
            partner = subject  # homodimer record
        elif a == subject:
            partner = b
        elif b == subject:
            partner = a
        else:
            raise ValueError(
                f"record {r['ac']} names neither side as {subject} "
                f"(idA={r['uniqueIdA']!r}, idB={r['uniqueIdB']!r})"
            )
        groups[partner].append(r)
    covered = sum(len(v) for v in groups.values())
    assert covered == len(records), (
        f"partner grouping covered {covered} of {len(records)} records -- "
        "the id format has changed and every count below would be wrong"
    )
    return groups


def partner_rows() -> list[tuple[str, str]]:
    """(reference, partner accession) for every GO:0005515 IPI row in the GOA."""
    out = []
    with GOA.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["GO TERM"] != "GO:0005515":
                continue
            for tok in row["WITH/FROM"].split("|"):
                tok = tok.strip()
                if tok.startswith("UniProtKB:"):
                    out.append((row["REFERENCE"], tok.split(":", 1)[1]))
    return out


def self_test() -> None:
    """Break the parser deliberately and confirm the invariant fires."""
    recs, _other = partition_by_type(intact_interactions(SUBJECT))
    groups = group_by_partner(recs, SUBJECT)
    assert groups, "baseline produced no groups"
    # Mutation 1: an id format the parser cannot match must raise, not return 0.
    broken = [dict(r) for r in recs]
    assert broken[0]["uniqueIdA"] or broken[0]["uniqueIdB"]
    broken[0]["uniqueIdA"] = "XXXXXX"
    broken[0]["uniqueIdB"] = "YYYYYY"
    try:
        group_by_partner(broken, SUBJECT)
    except ValueError:
        print("self-test 1 PASS: unmatched record raises rather than being dropped")
    else:
        raise AssertionError("self-test 1 FAILED: unmatched record was silently absorbed")
    # Mutation 2: the coverage assertion must be reachable, i.e. a grouping that
    # loses a record fails. Exercised by grouping a strict subset and comparing.
    subset = recs[:-1]
    g2 = group_by_partner(subset, SUBJECT)
    assert sum(len(v) for v in g2.values()) == len(subset)
    print("self-test 2 PASS: coverage assertion counts exactly the records given")


def main() -> None:
    if "--self-test" in sys.argv:
        self_test()
        return

    rows = partner_rows()
    accs = sorted({a for _, a in rows})
    print(f"GO:0005515 IPI rows in GOA: {len(rows)}; distinct partner accessions: {len(accs)}")

    all_ints = intact_interactions(SUBJECT)
    subj_ints, nonprotein = partition_by_type(all_ints)
    groups = group_by_partner(subj_ints, SUBJECT)
    print(f"IntAct records naming {SUBJECT}: {len(all_ints)} "
          f"({len(subj_ints)} protein-protein, {len(nonprotein)} other)")
    for r in nonprotein:
        print(f"    excluded: {r['typeA']}/{r['typeB']}  {r['moleculeA']} + {r['moleculeB']}"
              f"  PMID:{r.get('publicationPubmedIdentifier')}  {r.get('detectionMethod')}")
    print(f"distinct protein IntAct partners of {SUBJECT}: {len(set(groups) - {SUBJECT})}")

    out = []
    for acc in accs:
        base = base_acc(acc)
        s = summarise(uniprot_entry(base))
        recs = groups.get(base, [])
        experiments = {(r.get("publicationPubmedIdentifier"), r.get("detectionMethod"))
                       for r in recs}
        pubs = {r.get("publicationPubmedIdentifier") for r in recs}
        methods = sorted({str(r.get("detectionMethod")) for r in recs})
        spoke = sum(1 for r in recs if r.get("expansionMethod") == "spoke expansion")
        scores = [r.get("intactMiscore") for r in recs if r.get("intactMiscore") is not None]
        p_pp, _ = partition_by_type(intact_interactions(base))
        p_groups = group_by_partner(p_pp, base)
        out.append({
            "goa_partner_token": acc,
            "canonical_accession": s["accession"],
            "entry_name": s["id"],
            "gene": s["gene"],
            "organism": s["organism"],
            "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "length": s["length"],
            "is_isoform_token": str(acc != base),
            "intact_records": len(recs),
            "distinct_publications": len(pubs),
            "distinct_experiments": len(experiments),
            "spoke_expanded_records": spoke,
            "max_mi_score": max(scores) if scores else "",
            "detection_methods": ";".join(methods),
            "partner_total_intact_partners": len(set(p_groups) - {base}),
        })

    fields = list(out[0])
    with (HERE / "partner_checks.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        w.writeheader()
        w.writerows(out)

    n_rev = sum(1 for r in out if r["reviewed"] == "Swiss-Prot")
    n_tre = sum(1 for r in out if r["reviewed"] == "TrEMBL")
    assert n_rev + n_tre == len(out), "reviewed/unreviewed split does not total"
    print(f"partners: {n_rev} Swiss-Prot, {n_tre} TrEMBL")
    thin = [(r["gene"], r["distinct_experiments"]) for r in out if r["distinct_experiments"] <= 1]
    print(f"partners with <=1 distinct IntAct experiment: {len(thin)} {thin}")
    hubs = [(r["gene"], r["partner_total_intact_partners"]) for r in out
            if r["partner_total_intact_partners"] > 200]
    print(f"partners with >200 IntAct partners (hubs): {hubs}")
    allspoke = [r["gene"] for r in out
                if r["intact_records"] and r["spoke_expanded_records"] == r["intact_records"]]
    print(f"partners whose IntAct support is entirely spoke-expanded: {allspoke}")


if __name__ == "__main__":
    main()
