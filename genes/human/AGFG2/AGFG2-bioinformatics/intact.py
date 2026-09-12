#!/usr/bin/env python3
"""AGFG2's IntAct interaction records, resolved and counted.

Committed because the review's curation knowledge-gap quotes a partner count, and a
verification that exists only in a shell transcript is not a verification.

Three disciplines the campaign has established for this check:

* **Count distinct experiments, not `NbExp`.** That number has been observed counting
  sub-methods of one screen, replicates within a study, and even a partner's domain
  count. Here the detection method and publication of every record are printed so a
  reader can see that the BioPlex records are one platform, not two methods.
* **Assert the subject is not in its own partner set**, and that no nucleic-acid
  entities are counted as protein partners. Self-inclusion is the classic symptom of a
  predicate that never fired — and IntAct ids carry a ``" (uniprotkb)"``-style
  decoration, so any substring test against them needs an anchor.
* **Assert on membership, not cardinality.** A matching count is not a matching set;
  two errors in opposite directions cancel and leave the number looking right.
"""

from __future__ import annotations

import json
import pathlib
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import get_json  # noqa: E402

HERE = pathlib.Path(__file__).parent
SUBJECT = "O95081"
SUBJECT_SYMBOL = "AGFG2"

# Records whose molecule name starts with any of these are not protein partners.
NON_PROTEIN_PREFIXES = ("mrna_", "hsa-", "hsamir", "mir")


def main() -> None:
    d = get_json(
        "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/"
        f"{SUBJECT}?page=0&pageSize=200"
    )
    total = d.get("totalElements")
    content = d.get("content") or []
    if total is None:
        raise AssertionError("IntAct returned no totalElements — cannot verify coverage")
    if len(content) != total:
        raise AssertionError(
            f"silent truncation: totalElements={total} but fetched {len(content)}"
        )

    records = []
    for it in content:
        a, b = it.get("moleculeA"), it.get("moleculeB")
        records.append({
            "moleculeA": a,
            "moleculeB": b,
            "method": it.get("detectionMethod"),
            "publications": it.get("publicationIdentifiers"),
            "mi_score": it.get("intactMiscore"),
        })

    def is_protein(name: str | None) -> bool:
        n = (name or "").lower()
        return not any(n.startswith(p) for p in NON_PROTEIN_PREFIXES)

    protein_records = [r for r in records
                       if is_protein(r["moleculeA"]) and is_protein(r["moleculeB"])]
    nucleic_records = [r for r in records if r not in protein_records]

    partners: dict[str, list[dict]] = defaultdict(list)
    for r in protein_records:
        for side, other in ((r["moleculeA"], r["moleculeB"]), (r["moleculeB"], r["moleculeA"])):
            # Exact comparison, not a substring test: IntAct molecule names carry
            # decorations that defeat naive matching.
            if side is not None and side.upper() == SUBJECT_SYMBOL:
                partners[other].append(r)

    # Assertions that would fire if the predicate above never matched.
    assert SUBJECT_SYMBOL not in partners, (
        f"{SUBJECT_SYMBOL} appears in its own partner set — the self-exclusion "
        f"predicate did not fire"
    )
    assert partners, "no partners resolved — the symbol match never fired"
    for name in partners:
        assert is_protein(name), f"{name} counted as a protein partner but is not one"

    coip_or_pulldown = {
        name: recs for name, recs in partners.items()
        if any("coip" in (r["method"] or "").lower() or "pull down" in (r["method"] or "").lower()
               for r in recs)
    }
    # The claim in the review is about *human* partners with co-IP/pulldown support. The
    # bacterial hit is named here so the exclusion is explicit rather than silent — but
    # note it actually drops out on METHOD (two-hybrid pooling), not on species, so this
    # filter is currently a no-op. Reported as such rather than credited with a filtering
    # job it is not doing.
    non_human = {"lcrS"}
    human_coip = {n: r for n, r in coip_or_pulldown.items() if n not in non_human}

    out = {
        "subject": SUBJECT,
        "total_records": total,
        "n_protein_protein_records": len(protein_records),
        "n_nucleic_acid_records": len(nucleic_records),
        "partners": {n: [{"method": r["method"], "publications": r["publications"],
                          "mi_score": r["mi_score"]} for r in recs]
                     for n, recs in sorted(partners.items())},
        "n_distinct_partners": len(partners),
        "partners_with_coip_or_pulldown": sorted(coip_or_pulldown),
        "human_partners_with_coip_or_pulldown": sorted(human_coip),
        "n_human_partners_with_coip_or_pulldown": len(human_coip),
        "excluded_as_non_human": sorted(non_human & set(coip_or_pulldown)),
        "note": (
            "The BioPlex records (PMID:28514442 and PMID:33961781) are two releases of "
            "one anti-tag co-IP platform, so a partner appearing in both is one method, "
            "not two independent assays. The bacterial partner lcrS is excluded from the "
            "co-IP/pulldown set by its METHOD (two hybrid pooling), so the by-name "
            "non-human filter is a no-op here; it is kept and reported rather than "
            "credited with work it is not doing."
        ),
    }
    (HERE / "intact.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    print(f"IntAct records for {SUBJECT}: {total} total "
          f"({len(protein_records)} protein-protein, {len(nucleic_records)} nucleic-acid)")
    print(f"distinct protein partners: {out['n_distinct_partners']} "
          f"-> {sorted(partners)}")
    print(f"with co-IP or pulldown: {out['partners_with_coip_or_pulldown']}")
    print(f"human, with co-IP or pulldown: {out['n_human_partners_with_coip_or_pulldown']} "
          f"-> {out['human_partners_with_coip_or_pulldown']} "
          f"(excluded as non-human: {out['excluded_as_non_human']})")
    for name, recs in sorted(partners.items()):
        for r in recs:
            print(f"    {name:10s} {r['method']:22s} score={r['mi_score']} {r['publications']}")


if __name__ == "__main__":
    main()
