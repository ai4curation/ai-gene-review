"""Trace the bacterial GO:0004321 rows that QuickGO serves to their EC source.

1. Download every GO:0004321 annotation on Bacteria from QuickGO and count rows
   by reference (GO_REF:0000003 is EC2GO, GO_REF:0000117 is ARBA).
2. For each EC2GO row, look the entry up in the current UniProtKB release and
   record whether it still carries EC 2.3.1.86, and on what evidence.
3. For an evenly spaced sample (first to last accession) of the entries that
   no longer carry it, read every UniSave version current at or after the
   first of TALLY_RELEASES and report which carried EC 2.3.1.86, whether the
   evidence was ARBA00048237, and how many entries carried it in each of
   TALLY_RELEASES.

Writes RESULTS-bacterial-rows.md next to this script.

Usage: python check_bacterial_go_rows.py [--quickgo-tsv FILE]

With --quickgo-tsv, step 1 reads a saved QuickGO download of the same query
instead of fetching it (QuickGO's download endpoint can be unavailable); the
receipt then records the file's modification date as the QuickGO date.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?" + urllib.parse.urlencode(
    {
        "goId": "GO:0004321",
        "goUsage": "exact",
        "taxonId": "2",
        "taxonUsage": "descendants",
        "selectedFields": "geneProductId,goEvidence,reference,assignedBy,withFrom",
        "downloadLimit": "50000",
    }
)
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
#: Network attempts per request (UniProt batch lookups can be slow).
ATTEMPTS = 6
#: Accessions per UniProtKB batch lookup.
BATCH = 50
#: The releases whose EC 2.3.1.86 the review describes (June and September 2026).
TALLY_RELEASES = ("2026_02", "2026_03")
#: Entries whose UniSave history is read, spread evenly over the sorted accession list.
SAMPLE = 20


def fetch(url: str, accept: str = "application/json") -> tuple[bytes, dict]:
    """GET with retries; return body and headers."""
    req = urllib.request.Request(url, headers={"Accept": accept})
    for attempt in range(ATTEMPTS):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read(), dict(r.headers)
        except Exception:  # network: retry with backoff
            if attempt == ATTEMPTS - 1:
                raise
            time.sleep(5 * 2**attempt)
    raise RuntimeError("unreachable")


def release_span(version: dict) -> tuple[str, str] | None:
    """First and last UniProt release (YYYY_NN) a UniSave version was current in.

    >>> release_span({"firstRelease": "2026_02/2026_02", "lastRelease": "2026_03/2026_03"})
    ('2026_02', '2026_03')
    >>> release_span({"firstRelease": "2026_03/2026_03"}) is None
    True
    """
    first = (version.get("firstRelease") or "").split("/")[0]
    last = (version.get("lastRelease") or "").split("/")[0]
    return (first, last) if first and last else None


def in_span(release: str, span: tuple[str, str]) -> bool:
    """Whether ``release`` falls within ``span``; YYYY_NN labels sort as text.

    No release cadence is assumed: a version current from 2025_03 to 2025_06
    contains 2025_05 whatever the number of releases per year.

    >>> in_span("2026_02", ("2026_02", "2026_03"))
    True
    >>> in_span("2025_05", ("2025_03", "2025_06"))
    True
    >>> in_span("2026_04", ("2026_02", "2026_03"))
    False
    """
    return span[0] <= release <= span[1]


def ec_evidence(entry: dict) -> list[str]:
    """Evidence codes on EC 2.3.1.86 in the entry's names and catalytic activities."""
    found: list[str] = []
    for c in entry.get("comments", []):
        r = c.get("reaction", {})
        if r.get("ecNumber") == "2.3.1.86":
            found += [f"CA {e.get('evidenceCode')} {e.get('source', '')}:{e.get('id', '')}" for e in r.get("evidences", [])] or ["CA curated"]
    desc = entry.get("proteinDescription", {})
    names = list(desc.get("submissionNames") or []) + ([desc["recommendedName"]] if desc.get("recommendedName") else [])
    for n in names:
        for x in n.get("ecNumbers", []):
            if x["value"] == "2.3.1.86":
                found += [f"DE {e.get('evidenceCode')} {e.get('source', '')}" for e in x.get("evidences", [])] or ["DE curated"]
    return found


def main() -> None:
    """Run the three steps and write RESULTS-bacterial-rows.md."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--quickgo-tsv", type=Path, help="saved QuickGO download of the same query")
    args = parser.parse_args()
    if args.quickgo_tsv:
        body = args.quickgo_tsv.read_bytes()
        quickgo_date = time.strftime("%Y-%m-%d", time.localtime(args.quickgo_tsv.stat().st_mtime))
        quickgo_note = f"QuickGO download of {quickgo_date} (saved file, same query)"
    else:
        body, _ = fetch(QUICKGO, "text/tsv")
        quickgo_note = f"QuickGO retrieved {time.strftime('%Y-%m-%d')}"
    rows = list(csv.DictReader(io.StringIO(body.decode()), delimiter="\t"))
    by_ref = Counter(f"{r['REFERENCE']} / {r['ASSIGNED BY']}" for r in rows)
    accs = sorted({r["GENE PRODUCT ID"] for r in rows if r["REFERENCE"] == "GO_REF:0000003"})

    status: Counter[str] = Counter()
    release = None
    without: list[str] = []
    for i in range(0, len(accs), BATCH):
        chunk = accs[i : i + BATCH]
        q = " OR ".join(f"accession:{a}" for a in chunk)
        url = UNIPROT + "?" + urllib.parse.urlencode(
            {"query": q, "format": "json", "size": str(BATCH), "fields": "accession,protein_name,ec,cc_catalytic_activity"}
        )
        data, headers = fetch(url)
        release = headers.get("X-UniProt-Release") or headers.get("x-uniprot-release") or release
        got = json.loads(data)["results"]
        status["not in current release"] += len(chunk) - len(got)
        for e in got:
            ev = ec_evidence(e)
            key = "; ".join(sorted(set(ev))) if ev else "no EC 2.3.1.86 in current entry"
            status[key] += 1
            if not ev:
                without.append(e["primaryAccession"])

    history: list[str] = []
    without.sort()
    n = len(without)
    k = min(SAMPLE, n)
    # Evenly spaced indices from the first to the last entry, so the newest
    # accessions are sampled too.
    sample = [without[round(i * (n - 1) / (k - 1))] for i in range(k)] if k > 1 else without[:k]
    attributed = 0
    by_release: Counter[str] = Counter()
    missing_span = 0
    spanned = 0
    release_dates: dict[str, str] = {}
    for acc in sample:
        versions = json.loads(fetch(f"https://rest.uniprot.org/unisave/{acc}?format=json")[0])["results"]
        sources: list[str] = []
        covered: set[str] = set()
        for v in versions:
            span = release_span(v)
            if span is None:
                missing_span += 1
                continue
            spanned += 1
            for key in ("first", "last"):
                label = (v.get(f"{key}Release") or "").split("/")[0]
                if label and v.get(f"{key}ReleaseDate"):
                    release_dates[label] = v[f"{key}ReleaseDate"]
            # Every version current in any tallied release, however many there are.
            if span[1] < TALLY_RELEASES[0]:
                continue
            txt = fetch(
                f"https://rest.uniprot.org/unisave/{acc}?format=txt&versions={v['entryVersion']}", "text/plain"
            )[0].decode()
            if "EC=2.3.1.86" not in txt:
                continue
            ev = "ARBA00048237" if "ARBA:ARBA00048237" in txt else "other"
            if ev == "ARBA00048237":
                covered.update(r for r in TALLY_RELEASES if in_span(r, span))
            label = span[0] if span[0] == span[1] else f"{span[0]} to {span[1]}"
            sources.append(f"v{v['entryVersion']} ({label}): {ev}")
        if any(x.endswith("ARBA00048237") for x in sources):
            attributed += 1
        by_release.update(covered)
        history.append(
            f"- {acc}: "
            + ("; ".join(sources) if sources else f"EC 2.3.1.86 in no version current since {TALLY_RELEASES[0]}")
        )
    if not spanned:
        raise RuntimeError("No UniSave version had firstRelease/lastRelease; check the field names")
    head = [
        f"{attributed} of {len(sample)} sampled entries carried EC 2.3.1.86 from ARBA00048237 in an earlier version.",
        "",
        "Sampled entries carrying it from ARBA00048237 in each release (every UniSave version current at or "
        f"after {TALLY_RELEASES[0]} is read; a version counts for each release it spans):",
        "",
        *[
            f"- release {r} ({release_dates.get(r, 'date not reported')}): {by_release[r]} of {len(sample)}"
            for r in TALLY_RELEASES
        ],
        "",
        f"UniSave versions without release fields (skipped; when non-zero the per-release counts above are "
        f"lower bounds): {missing_span}",
        "",
    ]
    history = head + history

    lines = [
        "# Bacterial GO:0004321 rows and their EC source",
        "",
        f"{quickgo_note}; UniProtKB release {release}, UniSave read {time.strftime('%Y-%m-%d')}. "
        "Produced by `check_bacterial_go_rows.py`.",
        "",
        f"QuickGO serves {len(rows)} GO:0004321 annotations on Bacteria:",
        "",
        *[f"- {k}: {v}" for k, v in by_ref.most_common()],
        "",
        f"The {len(accs)} entries with an EC2GO (GO_REF:0000003) row, in the current UniProtKB release:",
        "",
        *[f"- {k}: {v}" for k, v in status.most_common()],
        "",
        f"UniSave history of {len(sample)} of the {len(without)} entries that no longer carry EC 2.3.1.86:",
        "",
        *history,
    ]
    Path(__file__).with_name("RESULTS-bacterial-rows.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
