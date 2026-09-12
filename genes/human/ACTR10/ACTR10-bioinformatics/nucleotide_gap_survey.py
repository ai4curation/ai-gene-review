"""Is ACTR10's missing nucleotide-binding annotation an isolated gap or a family-wide one?

Section A-C establish that ACTR10 has an intact, occupied actin-fold nucleotide site while
GOA records no nucleotide-binding term for it. Two questions follow, and both are answered
by asking QuickGO what the rest of the family carries:

1. **Is the gap peculiar to ACTR10?** If most actins and Arps also lack a
   nucleotide-binding term, the omission is a family-wide curation gap rather than a
   judgement that ACTR10 in particular does not bind nucleotide.
2. **Which term should be used?** Deposited dynactin models place ADP in the Arp11 chain
   more often than ATP, so `GO:0005524 ATP binding` needs justifying against
   `GO:0043531 ADP binding` and against their common parent
   `GO:0032559 adenyl ribonucleotide binding`. GO's own precedent on characterised
   actins settles which of these curators actually use, and how many at once.

Every annotation is counted with `goUsage=descendants` under `GO:0000166 nucleotide
binding`, so a term more specific than the three named ones would still be caught, and
each hit is reported with the term it was found under and its evidence code.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request

# The actin-fold panel, with the role each protein plays. Nothing is asserted from
# memory: each accession's UniProt entry name is fetched and printed alongside.
PANEL = [
    ("ACTA1", "P68133", "conventional actin (skeletal muscle alpha)"),
    ("ACTB", "P60709", "conventional actin (cytoplasmic beta)"),
    ("ACTG1", "P63261", "conventional actin (cytoplasmic gamma)"),
    ("ACT1", "P60010", "conventional actin (S. cerevisiae)"),
    ("ACTR1A", "P61163", "dynactin filament (Arp1)"),
    ("ACTR1B", "P42025", "dynactin filament (Arp1 paralog)"),
    ("ACTR2", "P61160", "Arp2/3 complex (Arp2)"),
    ("ACTR3", "P61158", "Arp2/3 complex (Arp3)"),
    ("ACTR10", "Q9NZ32", "dynactin pointed end (Arp11) - the gene under review"),
    ("ARP10", "Q04549", "yeast dynactin pointed end (Arp11 ortholog)"),
    ("ACTL6A", "O96019", "nuclear ARP (BAF/PBAF)"),
    ("ACTR8", "Q9H981", "nuclear ARP (INO80)"),
]

ROOT = "GO:0000166"  # nucleotide binding
NAMED = {
    "GO:0005524": "ATP binding",
    "GO:0043531": "ADP binding",
    "GO:0032559": "adenyl ribonucleotide binding",
}


def http_json(url: str, tries: int = 4) -> dict:
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries} tries: {url}") from last


def assert_not_truncated(payload: dict, url: str) -> None:
    """Fail if QuickGO reported more hits than one page returned.

    A `limit=100` query that silently drops page 2 is the same class of defect as a
    denominator that silently shrinks: the result still looks complete.
    """
    hits = payload.get("numberOfHits")
    got = len(payload.get("results", []))
    if hits is not None and hits > got:
        raise SystemExit(
            f"truncated result: QuickGO reports {hits} hits but only {got} were returned "
            f"for {url} - raise the limit or paginate before trusting the counts."
        )


def entry_name(acc: str) -> str:
    """Entry name for `acc`, rejecting a dead or merged accession."""
    d = http_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=id")
    returned = d.get("primaryAccession")
    entry_type = d.get("entryType", "")
    if returned != acc or "Inactive" in entry_type:
        # A merged accession makes UniProt return the merge target's record, so the reply
        # looks healthy while describing a different protein. See the long note in
        # subunit_granule_survey.entry_name: primaryAccession is the only reliable check.
        raise SystemExit(
            f"bad input: UniProt accession {acc} is not a live entry - returned "
            f"primaryAccession={returned!r}, entryType={entry_type!r}. Replace it in this "
            "module's panel with the current accession."
        )
    return d["uniProtkbId"]


def nucleotide_annotations(acc: str) -> list[tuple[str, str]]:
    """(GO id, evidence code) pairs under GO:0000166 for this accession."""
    url = "https://www.ebi.ac.uk/QuickGO/services/annotation/search?" + urllib.parse.urlencode(
        {
            "geneProductId": f"UniProtKB:{acc}",
            "goId": ROOT,
            "goUsage": "descendants",
            "goUsageRelationships": "is_a,part_of",
            "limit": 100,
        }
    )
    payload = http_json(url)
    assert_not_truncated(payload, url)
    return sorted({(r["goId"], r["goEvidence"]) for r in payload.get("results", [])})


def main() -> str:
    lines: list[str] = []
    out = lines.append
    out("## E. Nucleotide-binding annotation across the actin-fold family")
    out("")
    out(
        "QuickGO annotations under `GO:0000166 nucleotide binding` (descendants included) "
        "for a panel of actins and actin-related proteins. This asks whether ACTR10's "
        "missing nucleotide term is peculiar to ACTR10, and which term GO curators "
        "actually use for the actin-fold nucleotide site."
    )
    out("")
    out("| gene | UniProt | entry name | role | nucleotide-binding annotations |")
    out("|---|---|---|---|---|")
    have: list[str] = []
    lack: list[str] = []
    term_use: dict[str, list[str]] = {}
    for symbol, acc, role in PANEL:
        name = entry_name(acc)
        anns = nucleotide_annotations(acc)
        if anns:
            have.append(symbol)
            cell = "; ".join(
                f"{gid} {NAMED.get(gid, '')} ({ev})".replace("  ", " ").strip() for gid, ev in anns
            )
            for gid, _ in anns:
                term_use.setdefault(gid, []).append(symbol)
        else:
            lack.append(symbol)
            cell = "**none**"
        out(f"| {symbol} | {acc} | {name} | {role} | {cell} |")
    out("")
    out(
        f"- {len(have)}/{len(PANEL)} panel members carry any nucleotide-binding annotation "
        f"({', '.join(have) if have else 'none'})"
    )
    out(
        f"- {len(lack)}/{len(PANEL)} carry none ({', '.join(lack) if lack else 'none'})"
    )
    for gid in sorted(term_use):
        label = NAMED.get(gid, "")
        out(f"- `{gid}` {label}: {', '.join(term_use[gid])}")
    out("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.stdout.write(main())
