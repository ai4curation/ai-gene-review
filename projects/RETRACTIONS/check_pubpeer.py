#!/usr/bin/env python3
"""Check every PMID cited by the gene reviews for PubPeer discussion (prototype).

``check_retractions.py`` asks PubMed whether a cited paper has been formally
retracted or put under an expression of concern. Formal notices lag, often by
years, behind the post-publication discussion that eventually triggers them, and
most criticised papers never get one at all. PubPeer is where much of that
discussion happens. This script asks PubPeer, for the same set of cited PMIDs,
which ones have comments.

What it does
------------

1. Collects citations exactly as ``check_retractions.py`` does (same code), so each
   PMID carries its citation sites: ``reference``, ``annotation`` (an existing GO
   annotation's ``original_reference_id``) or ``supporting_text``.
2. Asks PubPeer in batches which of those PMIDs have a PubPeer page, and records
   the comment count, the date of the latest comment, and any publisher *updates*
   PubPeer has attached (``RETRACTED``, ``EXPRESSION OF CONCERN``, ``ERRATUM``).
3. Asks PubMed (with ``check_retractions.fetch_records``) about every PubPeer hit,
   so each row carries a *current* PubMed severity and the report can separate what
   PubPeer adds from what PubMed already says. Only the hits are re-fetched, which
   is a few requests, and avoids depending on a stale ``retraction-check.json``.
   PubPeer's relayed publisher updates are kept, but PubMed is authoritative: in
   testing PubPeer missed a retraction PubMed records, and showed only an erratum
   for a paper PubMed lists as retracted.
4. Writes ``pubpeer-check.tsv``, ``pubpeer-check.json`` and ``pubpeer-register.md``.

A comment count is not a verdict
--------------------------------

PubPeer comments range from image-duplication reports to a reader asking for a
reagent. A paper with comments has been *discussed*; nothing more is implied until
someone reads the thread. The register therefore ranks and lists, and never assigns
a severity of its own beyond the publisher updates PubPeer relays.

The endpoint
------------

This uses ``https://pubpeer.com/v3/publications``, the endpoint PubPeer's own
browser extensions call, with the extension's public ``devkey``. It needs no
account, but it is not a documented bulk API: for a production or scheduled run,
ask PubPeer for a key and set ``PUBPEER_DEVKEY``. Four behaviours matter:

* **At most 10 publications come back per request, however many PMIDs are sent.**
  Only publications that have a PubPeer page are returned, so a response with
  fewer than 10 entries is complete. A full response may have been truncated;
  that batch is split in half and re-asked until every answer is short of the
  cap or covers a single PMID.
* **Matching is not strictly by PMID.** Asked about PMID 13760, PubPeer
  returns PMID:27926515, an unrelated 2016 Oncotarget paper (apparently matching
  the number against another identifier). Entries whose PMID was not asked for
  are dropped. They still occupy response slots, which is why even a batch of
  10 or fewer PMIDs is split when its response is full.
* **Rate limit: 20 requests per minute** (``X-RateLimit-Limit: 20``). Requests
  are spaced ``--delay`` apart (default 3.1 s). On a 429 the client sleeps until
  ``X-RateLimit-Reset``; ``Retry-After`` alone is not enough, because PubPeer
  sometimes sends ``Retry-After: 0`` while still refusing requests.
* The default ``python-requests`` / ``urllib`` user agents are refused (403);
  a descriptive ``User-Agent`` is sent instead.

Usage::

    uv run --no-dev python projects/RETRACTIONS/check_pubpeer.py
    uv run --no-dev python projects/RETRACTIONS/check_pubpeer.py --limit 500 --out-dir /tmp/pp
    uv run --no-dev python projects/RETRACTIONS/check_pubpeer.py --from-json projects/RETRACTIONS/pubpeer-check.json
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_retractions import (  # noqa: E402
    GENES_DIR,
    OUT_DIR,
    Citation,
    _genes_cell,
    _norm_pmid,
    collect_citations,
    fetch_records,
)

PUBPEER_URL = "https://pubpeer.com/v3/publications"
# The public key of PubPeer's browser extension; override for a real API key.
DEFAULT_DEVKEY = "PubMedChrome"
USER_AGENT = (
    "ai-gene-review-pubpeer-check (+https://github.com/ai4curation/ai-gene-review)"
)
# PubPeer returns at most this many publications per request.
RESPONSE_CAP = 10

REGENERATE_CMD = "uv run --no-dev python projects/RETRACTIONS/check_pubpeer.py"

# PubPeer update types that correspond to PubMed's actionable severities.
FORMAL_UPDATES = {
    "RETRACTED": "RETRACTED",
    "EXPRESSION OF CONCERN": "EXPRESSION_OF_CONCERN",
}

ANNOTATION_TABLE_CAP = 60


# ---------------------------------------------------------------------------
# 1. Ask PubPeer
# ---------------------------------------------------------------------------


@dataclass
class PubPeerRecord:
    pmid: str
    title: str = ""
    journal: str = ""
    total_comments: int = 0
    last_commented_at: str = ""
    url: str = ""
    updates: List[str] = field(default_factory=list)  # e.g. RETRACTED, ERRATUM

    @property
    def formal_flags(self) -> List[str]:
        """PubMed-style severities implied by PubPeer's relayed publisher updates."""
        return sorted({FORMAL_UPDATES[u] for u in self.updates if u in FORMAL_UPDATES})


def parse_feedback(item: Dict[str, Any]) -> Optional[PubPeerRecord]:
    """Turn one PubPeer ``feedbacks`` entry into a record keyed by ``PMID:n``."""
    pmid = _norm_pmid(f"PMID:{item.get('id', '')}")
    if not pmid:
        return None
    journals = item.get("journals") or []
    journal = journals[0].get("title", "") if journals else ""
    updates = sorted(
        {str(u.get("type", "")).upper() for u in item.get("updates") or [] if u} - {""}
    )
    return PubPeerRecord(
        pmid=pmid,
        title=html.unescape(item.get("title") or ""),
        journal=html.unescape(journal),
        total_comments=int(item.get("total_comments") or 0),
        last_commented_at=item.get("last_commented_at") or "",
        url=item.get("url") or "",
        updates=updates,
    )


def _rate_limit_wait(headers: Any, attempt: int) -> float:
    """Seconds to sleep after a 429: until the window resets, never less than 5 s."""
    waits = [5.0 * attempt]
    reset = headers.get("X-RateLimit-Reset", "")
    if reset.isdigit():
        waits.append(int(reset) - time.time() + 1)
    retry_after = headers.get("Retry-After", "")
    if retry_after.isdigit():
        waits.append(int(retry_after) + 1)
    return min(max(waits), 120.0)


class PubPeerClient:
    def __init__(self, devkey: str, delay: float = 3.1, retries: int = 8):
        self.devkey = devkey
        self.delay = delay
        self.retries = retries
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        self.n_requests = 0

    def _post(self, pmids: List[str]) -> List[Dict[str, Any]]:
        payload = {"version": "1.6.2", "browser": "Chrome", "pmids": pmids}
        last_exc: Optional[Exception] = None
        for attempt in range(1, self.retries + 1):
            try:
                self.n_requests += 1
                resp = self.session.post(
                    PUBPEER_URL,
                    params={"devkey": self.devkey},
                    json=payload,
                    timeout=60,
                )
                if resp.status_code == 429:
                    wait = _rate_limit_wait(resp.headers, attempt)
                    print(f"  rate limited; waiting {wait:.0f}s", file=sys.stderr)
                    time.sleep(wait)
                    last_exc = RuntimeError("429 Too Many Requests")
                    continue
                resp.raise_for_status()
                body = resp.json()
                if body.get("status") != "good":
                    raise RuntimeError(f"PubPeer status {body.get('status')!r}")
                time.sleep(self.delay)
                return body.get("feedbacks") or []
            except Exception as exc:
                last_exc = exc
                time.sleep(self.delay * 4 * attempt)
        raise RuntimeError(
            f"PubPeer request failed after {self.retries} attempts: {last_exc}"
        )

    def query(self, pmids: List[str]) -> List[Dict[str, Any]]:
        """All feedback entries for ``pmids`` (bare digits), splitting on truncation."""
        feedbacks = self._post(pmids)
        if len(feedbacks) >= RESPONSE_CAP and len(pmids) > 1:
            mid = len(pmids) // 2
            return self.query(pmids[:mid]) + self.query(pmids[mid:])
        return feedbacks


def fetch_pubpeer(
    pmids: List[str], client: PubPeerClient, batch_size: int = 60
) -> Tuple[Dict[str, PubPeerRecord], List[str]]:
    """Ask PubPeer about ``pmids`` (``PMID:n``); return hits and never-asked PMIDs.

    As in ``check_retractions.fetch_records``, "no PubPeer page" and "request
    failed" must stay distinguishable, so failed batches are returned separately.
    """
    out: Dict[str, PubPeerRecord] = {}
    failed: List[str] = []
    batches = [pmids[i : i + batch_size] for i in range(0, len(pmids), batch_size)]
    for index, batch in enumerate(batches, start=1):
        asked = {p.split(":", 1)[1] for p in batch}
        try:
            feedbacks = client.query(sorted(asked))
        except Exception as exc:
            print(f"  ! batch {index}/{len(batches)}: {exc}", file=sys.stderr)
            failed.extend(batch)
            continue
        for item in feedbacks:
            rec = parse_feedback(item)
            if rec is None or rec.pmid.split(":", 1)[1] not in asked:
                print(
                    f"  ! unexpected PubPeer entry {item.get('id')!r}", file=sys.stderr
                )
                continue
            out[rec.pmid] = rec
        if index % 25 == 0 or index == len(batches):
            print(
                f"  batch {index}/{len(batches)} done ({len(out)} with comments, "
                f"{client.n_requests} requests)",
                file=sys.stderr,
            )
    return out, failed


# ---------------------------------------------------------------------------
# 2. Report
# ---------------------------------------------------------------------------


def _action_of(cite: Citation) -> str:
    return cite.detail.rsplit("action=", 1)[1] if "action=" in cite.detail else ""


def build_rows(
    records: Dict[str, PubPeerRecord],
    citations: Dict[str, List[Citation]],
    pubmed_severity: Dict[str, str],
) -> List[Dict[str, Any]]:
    rows = []
    for pmid, rec in records.items():
        cites = citations.get(pmid, [])
        ann = [c for c in cites if c.site == "annotation"]
        actions = Counter(_action_of(c) for c in ann)
        pubmed = pubmed_severity.get(pmid, "")
        rows.append(
            {
                "pmid": pmid,
                "total_comments": rec.total_comments,
                "last_commented_at": rec.last_commented_at,
                "pubpeer_updates": ";".join(rec.updates),
                "pubmed_severity": pubmed,
                # PubPeer relays a retraction / EoC that the PubMed scan did not see
                "pubpeer_only_formal_flag": ";".join(
                    f for f in rec.formal_flags if pubmed != f and pubmed != "RETRACTED"
                ),
                "title": rec.title,
                "journal": rec.journal,
                "url": rec.url,
                "n_citing_genes": len({(c.organism, c.gene) for c in cites}),
                "citing_genes": ";".join(
                    sorted({f"{c.organism}/{c.gene}" for c in cites})
                ),
                "citation_sites": ";".join(sorted({c.site for c in cites})),
                "used_as_annotation_evidence": bool(ann),
                "n_annotations": len(ann),
                "n_annotations_accept_or_keep": actions["ACCEPT"]
                + actions["KEEP_AS_NON_CORE"],
                "annotation_actions": ";".join(
                    f"{a or 'NONE'}:{n}" for a, n in sorted(actions.items())
                ),
                "already_flagged_is_invalid": any(c.already_invalid for c in cites),
                "annotation_details": ";".join(
                    sorted({f"{c.organism}/{c.gene} {c.detail}".strip() for c in ann})
                ),
            }
        )
    rows.sort(
        key=lambda r: (
            -int(r["used_as_annotation_evidence"]),
            -r["n_annotations_accept_or_keep"],
            -r["total_comments"],
            r["pmid"],
        )
    )
    return rows


def write_reports(
    records: Dict[str, PubPeerRecord],
    citations: Dict[str, List[Citation]],
    pmids_checked: List[str],
    pubmed_severity: Dict[str, str],
    out_dir: Path,
) -> Dict[str, Any]:
    rows = build_rows(records, citations, pubmed_severity)
    out_dir.mkdir(parents=True, exist_ok=True)
    tsv_path = out_dir / "pubpeer-check.tsv"
    fieldnames = list(rows[0].keys()) if rows else ["pmid"]
    with tsv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "generated_by": "projects/RETRACTIONS/check_pubpeer.py",
        "generated_on": date.today().isoformat(),
        "endpoint": PUBPEER_URL,
        "n_review_files": len(
            {(c.organism, c.gene) for cl in citations.values() for c in cl}
        ),
        "n_distinct_pmids_cited": len(citations),
        "n_pmids_checked": len(pmids_checked),
        "n_with_pubpeer_comments": len(rows),
        "flagged": rows,
    }
    json_path = out_dir / "pubpeer-check.json"
    json_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"wrote {tsv_path}")
    print(f"wrote {json_path}")
    return summary


def _table(rows: List[Dict[str, Any]], with_actions: bool) -> List[str]:
    header = "| PMID | Comments | Last comment | Title | Cited by | PubMed notice |"
    if with_actions:
        header += " Annotation actions |"
    lines = [header, "|" + "---|" * (header.count("|") - 1)]
    for row in rows:
        title = row["title"].replace("|", "\\|")
        if len(title) > 90:
            title = title[:87] + "..."
        cells = [
            f"[{row['pmid']}]({row['url']})" if row["url"] else row["pmid"],
            str(row["total_comments"]),
            (row["last_commented_at"] or "-")[:10],
            title,
            _genes_cell(row, 4),
            row["pubmed_severity"] or "-",
        ]
        if with_actions:
            cells.append(row["annotation_actions"].replace(";", ", ") or "-")
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def write_register(summary: Dict[str, Any], out_dir: Path) -> Path:
    rows = summary["flagged"]
    discrepant = [r for r in rows if r.get("pubpeer_only_formal_flag")]
    ann_no_notice = [
        r for r in rows if r["used_as_annotation_evidence"] and not r["pubmed_severity"]
    ]
    with_notice = [
        r
        for r in rows
        if r["pubmed_severity"] in ("RETRACTED", "EXPRESSION_OF_CONCERN")
    ]
    other = [r for r in rows if not r["used_as_annotation_evidence"]]

    lines: List[str] = [
        "---",
        'title: "PubPeer Register"',
        "---",
        "",
        "# PubPeer Register",
        "",
        f"<!-- GENERATED FILE. Do not edit by hand. Regenerate with `{REGENERATE_CMD}`. -->",
        "",
        f"Every `PMID:` cited in the gene reviews, checked for PubPeer discussion. "
        f"Generated {summary.get('generated_on', date.today().isoformat())} from "
        f"**{summary['n_review_files']}** review files; "
        f"**{summary['n_pmids_checked']}** of {summary['n_distinct_pmids_cited']} "
        f"distinct cited PMIDs checked, **{summary['n_with_pubpeer_comments']}** have "
        f"PubPeer comments. See the [project page](../RETRACTIONS.md) for method.",
        "",
        "**A comment count is not a verdict.** PubPeer threads range from image-"
        "duplication reports to routine questions; a listed paper has been discussed, "
        "and nothing more is implied until someone reads the thread.",
        "",
    ]

    lines += ["## PubPeer reports a formal notice that PubMed does not", ""]
    if not discrepant:
        lines.append("None.")
    else:
        lines.append(
            "PubPeer relays publisher retractions and expressions of concern. These are "
            "papers where it shows one that the last PubMed scan did not. Check the "
            "notice before acting: the two sources can disagree for indexing reasons."
        )
        lines.append("")
        lines += _table(discrepant, with_actions=True)
    lines.append("")

    lines += [
        "## Discussed papers behind GO annotations, no PubMed notice",
        "",
        f"{len(ann_no_notice)} papers with PubPeer comments are the "
        "`original_reference_id` of at least one reviewed GO annotation and carry no "
        "retraction, expression of concern or erratum in PubMed. This is what PubPeer "
        "adds to the retraction scan. Ordered by the number of `ACCEPT` / "
        "`KEEP_AS_NON_CORE` annotations resting on the paper, then by comment count.",
        "",
    ]
    shown = ann_no_notice[:ANNOTATION_TABLE_CAP]
    if shown:
        lines += _table(shown, with_actions=True)
        if len(ann_no_notice) > len(shown):
            lines += [
                "",
                f"({len(shown)} of {len(ann_no_notice)} shown; the full list is in "
                "`pubpeer-check.tsv`.)",
            ]
    lines.append("")

    lines += ["## Already flagged by PubMed", ""]
    if not with_notice:
        lines.append("None.")
    else:
        lines.append(
            f"{len(with_notice)} papers in the [retraction register]"
            "(retraction-register.md) also have PubPeer threads, which are often the "
            "fastest way to see what the problem was."
        )
        lines.append("")
        lines += _table(with_notice, with_actions=True)
    lines.append("")

    lines += [
        "## Other discussed papers",
        "",
        f"{len(other)} further papers with PubPeer comments are cited only in reference "
        "lists or supporting text, not as annotation evidence. They are in "
        "`pubpeer-check.tsv`.",
        "",
    ]

    path = out_dir / "pubpeer-register.md"
    path.write_text("\n".join(lines))
    print(f"wrote {path}")
    return path


# ---------------------------------------------------------------------------
# 3. Main
# ---------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--genes-dir", type=Path, default=GENES_DIR)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    parser.add_argument(
        "--batch-size", type=int, default=60, help="PMIDs per PubPeer request"
    )
    parser.add_argument(
        "--delay", type=float, default=3.1, help="seconds to pause between requests"
    )
    parser.add_argument("--limit", type=int, default=0, help="only the first N PMIDs")
    parser.add_argument("--pmids", nargs="*", default=None, help="only these PMIDs")
    parser.add_argument(
        "--from-json",
        type=Path,
        default=None,
        help="rebuild the register from an existing pubpeer-check.json (no network)",
    )
    args = parser.parse_args(argv)

    if args.from_json:
        write_register(json.loads(args.from_json.read_text()), args.out_dir)
        return 0

    review_files = sorted(args.genes_dir.glob("*/*/*-ai-review.yaml"))
    print(f"scanning {len(review_files)} review files ...")
    citations: Dict[str, List[Citation]] = defaultdict(list)
    for path in review_files:
        for cite in collect_citations(path):
            citations[cite.pmid].append(cite)
    print(f"found {len(citations)} distinct PMIDs cited")

    pmids = sorted(citations, key=lambda p: int(p.split(":")[1]))
    if args.pmids:
        raw = [tok for arg in args.pmids for tok in str(arg).split(",") if tok.strip()]
        wanted = [_norm_pmid(t) or _norm_pmid(f"PMID:{t.strip()}") for t in raw]
        if not all(wanted):
            parser.error(
                "not valid PMIDs: " + ", ".join(t for t, w in zip(raw, wanted) if not w)
            )
        pmids = sorted(set(wanted), key=lambda p: int(p.split(":")[1]))  # type: ignore[arg-type]
    if args.limit:
        pmids = pmids[: args.limit]
    if not pmids:
        parser.error(
            "no PMIDs selected to check - refusing to overwrite existing reports"
        )
    if (args.pmids or args.limit) and args.out_dir == OUT_DIR:
        parser.error(
            "--pmids/--limit is a partial scan and would overwrite the full-scan "
            f"reports in {OUT_DIR}; pass --out-dir to write somewhere else"
        )

    client = PubPeerClient(
        devkey=os.environ.get("PUBPEER_DEVKEY", DEFAULT_DEVKEY), delay=args.delay
    )
    print(f"querying PubPeer for {len(pmids)} PMIDs ...")
    records, failed = fetch_pubpeer(pmids, client, batch_size=args.batch_size)
    if failed:
        print(
            f"ERROR: {len(failed)} of {len(pmids)} PMIDs were never checked (PubPeer "
            "requests failed). Refusing to write reports from a partial scan.",
            file=sys.stderr,
        )
        return 1

    print(f"asking PubMed about the {len(records)} PubPeer hits ...")
    pubmed, pm_failed = fetch_records(sorted(records), delay=0.5)
    if pm_failed:
        print(
            f"ERROR: PubMed did not answer for {len(pm_failed)} PubPeer hits; "
            "refusing to write reports without their PubMed status.",
            file=sys.stderr,
        )
        return 1
    pubmed_severity = {
        pmid: rec.severity
        for pmid, rec in pubmed.items()
        if rec.severity and not rec.is_notice
    }
    summary = write_reports(records, citations, pmids, pubmed_severity, args.out_dir)
    write_register(summary, args.out_dir)
    print(
        f"{len(records)} of {len(pmids)} PMIDs have PubPeer comments "
        f"({client.n_requests} requests)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
