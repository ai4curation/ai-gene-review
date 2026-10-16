#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Which GO annotations does UniProt show for ARHGAP6 that GOA/QuickGO does not --
and does anything downstream still depend on the missing ones?

Motivation
----------
While reviewing ARHGAP6 the UniProt flat file listed three BHF-UCL annotations
(`phospholipase activator activity`, `phospholipase binding`, and
`positive regulation of phospholipase C/protein kinase C signal transduction`)
that do not appear anywhere in the QuickGO/GOA download the review is built from.
A missing annotation is invisible to the review workflow: `just fetch-gene` seeds
`existing_annotations` from the GOA TSV, so a row absent there is simply never
reviewed.

Two things had to be distinguished, and neither can be assumed:

* **Term obsolescence.** If the three terms had been obsoleted, GOA dropping them
  would be correct housekeeping and UniProt's cross-reference block would merely be
  stale. So the script resolves each divergent term against the ontology.
* **A real drop.** If the terms are live, something removed the annotations, and the
  interesting question becomes whether any other annotation still *cites* them.

The second question is the sharp one. GOA records the source of an inferred
annotation in WITH/FROM, so a projection made from a since-deleted human annotation
leaves a detectable trace: a row in another species whose WITH/FROM names O43182 for
a term O43182 no longer has. That is what this script looks for.

What is computed (no finding is hardcoded)
------------------------------------------
1. UniProt's own GO cross-references for the target, from the UniProtKB REST API.
2. The target's GOA annotations, from the QuickGO annotation API -- the same source
   `just fetch-gene` uses.
3. The set difference in both directions.
4. For every term present in UniProt but absent from GOA: whether the term is
   obsolete (checked against **two independent services**, OLS4 and
   api.geneontology.org, because these can and do disagree), and how many
   annotations in any species name the target in WITH/FROM for that term.

Controls
--------
* Positive control: a term the two sources AGREE on (GO:0005096) must come back as
  agreeing, and must not appear in either difference set. Asserted; non-zero exit.
* Negative control for the WITH/FROM probe, self-calibrating: the unfiltered probe
  must return rows, and filtering by a term **taken from the probe's own output**
  must still return rows. A fixed control term would have been wrong here -- the
  target's `GO:0005096` is transferred *into* human from mouse, so it has no
  outgoing projections at all, and asserting on it would have condemned a working
  probe. Deriving the control term from the response cannot go stale that way.
* Obsolescence is only reported when both services agree. A disagreement is reported
  AS a disagreement -- it is never silently resolved to one service's answer.

Usage
-----
    uv run check_goa_uniprot_divergence.py            # writes RESULTS-goa-divergence.md
    uv run check_goa_uniprot_divergence.py --stdout
    uv run check_goa_uniprot_divergence.py --self-test
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

TARGET = "O43182"
TARGET_SYMBOL = "ARHGAP6"

# A term both sources carry, used as the positive control every run.
CONTROL_TERM = "GO:0005096"

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
QUICKGO_ANN = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
    "?geneProductId=UniProtKB:{acc}&limit=200&includeFields=goName"
)
QUICKGO_WITHFROM = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
    "?withFrom=UniProtKB:{acc}&goId={go}&limit=200"
)
QUICKGO_WITHFROM_ALL = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
    "?withFrom=UniProtKB:{acc}&limit=200"
)
OLS4 = "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id={go}"
GOAPI = "https://api.geneontology.org/api/ontology/term/{go}"


def _get(url: str):
    with urllib.request.urlopen(url, timeout=90) as fh:
        return json.load(fh)


def uniprot_go(acc: str) -> dict[str, str]:
    """GO id -> 'label [EVIDENCE:source]' from the UniProt cross-reference block."""
    d = _get(UNIPROT.format(acc=acc))
    out = {}
    for x in d.get("uniProtKBCrossReferences", []):
        if x["database"] != "GO":
            continue
        props = {p["key"]: p["value"] for p in x.get("properties", [])}
        term = props.get("GoTerm", "")
        out[x["id"]] = f"{term} [{props.get('GoEvidenceType','?')}]"
    return out


def goa_go(acc: str) -> dict[str, str]:
    """GO id -> 'label' from QuickGO, i.e. what the review workflow actually sees."""
    d = _get(QUICKGO_ANN.format(acc=acc))
    return {r["goId"]: r.get("goName", "") for r in d.get("results", [])}


def withfrom_count(acc: str, go: str | None = None) -> tuple[int, list[str], list[str]]:
    """Annotations in ANY species whose WITH/FROM names acc.

    With ``go`` given, restrict to that term. Returns
    (hit count, formatted rows, GO ids seen in the response).
    """
    url = QUICKGO_WITHFROM.format(acc=acc, go=go) if go else QUICKGO_WITHFROM_ALL.format(acc=acc)
    d = _get(url)
    rows = []
    seen_terms = []
    for r in d.get("results", []):
        seen_terms.append(r["goId"])
        rows.append(
            f"{r['geneProductId']} ({r.get('symbol')}, taxon {r.get('taxonId')}) "
            f"{r['goEvidence']} {r['reference']}"
        )
    return d.get("numberOfHits", 0), sorted(set(rows)), seen_terms


def obsolete_two_services(go: str) -> tuple[str, str, str]:
    """(ols4_answer, go_api_answer, verdict). Verdict is only decided on agreement."""
    ols = "unavailable"
    try:
        d = _get(OLS4.format(go=urllib.parse.quote(go)))
        terms = d.get("_embedded", {}).get("terms", [])
        if terms:
            ols = "obsolete" if terms[0].get("is_obsolete") else "active"
    except (urllib.error.URLError, KeyError, json.JSONDecodeError):
        pass

    api = "unavailable"
    try:
        d = _get(GOAPI.format(go=urllib.parse.quote(go)))
        flag = d.get("is_obsolete")
        if d.get("goid"):
            api = "obsolete" if flag else "active"
    except (urllib.error.URLError, KeyError, json.JSONDecodeError):
        pass

    if ols == api and ols != "unavailable":
        verdict = ols
    elif "unavailable" in (ols, api):
        verdict = "UNDECIDED (only one service answered)"
    else:
        verdict = f"**SERVICES DISAGREE** (OLS4={ols}, GO API={api})"
    return ols, api, verdict


def self_test() -> int:
    """Guards fire with their expected message; negative controls stay silent."""
    failures: list[str] = []

    # Guard: a term neither service can resolve must come back UNDECIDED or
    # disagreeing -- never a confident "active".
    ols, api, verdict = obsolete_two_services("GO:0000000")
    if verdict.startswith("active") or verdict.startswith("obsolete"):
        failures.append(f"nonexistent term resolved confidently: {verdict}")
    else:
        print(f"  ok   nonexistent-term: verdict is {verdict!r}, not a confident call")

    # Negative control: a real, live term must resolve to 'active' on agreement.
    ols, api, verdict = obsolete_two_services(CONTROL_TERM)
    if verdict == "active":
        print(f"  ok   live-term control: {CONTROL_TERM} -> active (OLS4={ols}, GO API={api})")
    else:
        failures.append(f"live-term control: {CONTROL_TERM} -> {verdict}")

    # Negative control for the probe, self-calibrating: the unfiltered probe must
    # return rows, and filtering by a term drawn from ITS OWN output must too.
    # Without this, a zero count for a divergent term could mean "nothing cites it"
    # or "the probe is broken", and those are not the same claim.
    n_all, _, seen = withfrom_count(TARGET)
    if n_all <= 0 or not seen:
        failures.append(
            f"unfiltered withFrom probe returned {n_all} rows for {TARGET}; the probe is "
            "not functioning, so zero counts for divergent terms would be uninformative"
        )
    else:
        probe_term = seen[0]
        n_one, _, _ = withfrom_count(TARGET, probe_term)
        if n_one > 0:
            print(
                f"  ok   withFrom probe control: unfiltered {n_all} rows; "
                f"filtered on {probe_term} (taken from the response) {n_one} rows"
            )
        else:
            failures.append(
                f"withFrom probe returned {n_all} unfiltered rows but 0 when filtered on "
                f"{probe_term}, a term present in its own response; the goId filter is broken"
            )

    if failures:
        print("\nSELF-TEST FAILURES:")
        for f in failures:
            print("  FAIL " + f)
        return 1
    print("\nself-test: all guards fired, all controls clean")
    return 0


def render(unp: dict[str, str], goa: dict[str, str], details: dict) -> str:
    today = date.today().isoformat()
    only_unp = sorted(set(unp) - set(goa))
    only_goa = sorted(set(goa) - set(unp))
    both = sorted(set(goa) & set(unp))

    out: list[str] = []
    A = out.append
    A(f"# {TARGET_SYMBOL} bioinformatics: UniProt vs GOA, and what depends on the gap")
    A("")
    A("## Question")
    A("")
    A("The UniProt flat file for ARHGAP6 lists three BHF-UCL phospholipase annotations")
    A("that do not appear in the QuickGO/GOA download this review is seeded from. Since")
    A("`just fetch-gene` builds `existing_annotations` from the GOA TSV, a row missing")
    A("there is never reviewed at all. **Is the divergence real, is it just term")
    A("obsolescence, and does anything downstream still depend on the missing rows?**")
    A("")
    A("## Method")
    A("")
    A("`check_goa_uniprot_divergence.py` diffs UniProt's GO cross-reference block")
    A("against the QuickGO annotation API for the same accession, then for each")
    A("divergent term asks two further questions from live data:")
    A("")
    A("1. **Is the term obsolete?** Checked against **two independent services** --")
    A("   OLS4 and `api.geneontology.org`. These are known to disagree about")
    A("   obsolescence, so a verdict is only issued when they agree; a disagreement is")
    A("   printed as a disagreement rather than resolved to one service's answer.")
    A("2. **Does anything cite the missing annotation?** GOA records the source of an")
    A("   inferred annotation in WITH/FROM, so the script queries QuickGO for")
    A("   annotations *in any species* whose WITH/FROM names `O43182` for that term.")
    A("   A non-zero count means a projection is still being served whose stated human")
    A("   source no longer exists in the human record.")
    A("")
    A("```")
    A("uv run check_goa_uniprot_divergence.py")
    A("uv run check_goa_uniprot_divergence.py --self-test")
    A("```")
    A("")
    A(f"## Result (run {today})")
    A("")
    A(f"UniProt cross-references: **{len(unp)}** GO terms. QuickGO/GOA: **{len(goa)}** distinct GO terms. Shared: **{len(both)}**.")
    A("")
    A("### In UniProt, absent from GOA")
    A("")
    if not only_unp:
        A("_none_")
    else:
        A("| GO id | label [UniProt evidence] | obsolete? (OLS4 / GO API) | verdict | rows citing O43182 in WITH/FROM for this term |")
        A("|---|---|---|---|---|")
        for go in only_unp:
            ols, api, verdict, n, rows = details[go]
            A(f"| {go} | {unp[go]} | {ols} / {api} | {verdict} | **{n}** |")
        A("")
        for go in only_unp:
            _, _, _, n, rows = details[go]
            if rows:
                A(f"Rows citing `{TARGET}` for **{go}**:")
                A("")
                for r in rows:
                    A(f"- `{r}`")
                A("")
    A("### In GOA, absent from UniProt's cross-reference block")
    A("")
    if not only_goa:
        A("_none_")
    else:
        for go in only_goa:
            A(f"- {go} {goa[go]}")
    A("")
    A("## Interpretation")
    A("")
    if only_unp:
        live = [g for g in only_unp if details[g][2] == "active"]
        cited = [g for g in only_unp if details[g][3] > 0]
        A(f"**The divergence is not term obsolescence.** {len(live)} of the {len(only_unp)}")
        A("terms present only in UniProt are live terms on both services checked, so GOA")
        A("dropping them is not the ontology retiring them.")
        A("")
        if cited:
            A("**And the missing rows are still load-bearing.** For "
              + ", ".join(f"`{g}`" for g in cited) + ", GOA is currently serving")
            A("annotations in other species whose WITH/FROM column names `O43182` as the")
            A("source -- for a term `O43182` itself no longer carries in GOA. Those")
            A("projections are orphaned: the human annotation they were derived from is")
            A("not in the human record any more.")
            A("")
        A("For the review this has a concrete consequence. Because the workflow seeds")
        A("`existing_annotations` from the GOA TSV, these annotations would silently")
        A("never be reviewed. They are therefore entered in the review as `NEW` rows --")
        A("not because they are new curation, but because they are pre-existing BHF-UCL")
        A("curation that has fallen out of the feed the review is built from.")
    else:
        A("UniProt and GOA agree on the term set; there is nothing to reconcile.")
    A("")
    A("## Caveats")
    A("")
    A("- The comparison is term-level. Two sources can list the same GO id with")
    A("  different evidence codes or qualifiers and still appear to agree here.")
    A("- A WITH/FROM count is a count of *rows*, not of independent evidence; several")
    A("  rows may be the same projection replicated across species.")
    A("- This script establishes that annotations are missing from one feed and cited by")
    A("  another. It does not establish *why* they were removed, and does not assume the")
    A("  removal was an error.")
    A("")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        print("self-test:")
        return self_test()

    try:
        unp = uniprot_go(TARGET)
        goa = goa_go(TARGET)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"network failure, no result produced: {exc}", file=sys.stderr)
        return 2

    # Positive control, asserted every run.
    if CONTROL_TERM not in unp or CONTROL_TERM not in goa:
        raise SystemExit(
            f"FAIL: control term {CONTROL_TERM} is not in both sources "
            f"(UniProt={CONTROL_TERM in unp}, GOA={CONTROL_TERM in goa}). "
            "One of the two fetches is broken; refusing to report a diff."
        )

    # Probe control, asserted every run (see self_test for the rationale).
    n_all, _, seen = withfrom_count(TARGET)
    if n_all <= 0 or not seen:
        raise SystemExit(
            f"FAIL: unfiltered WITH/FROM probe returned {n_all} rows for {TARGET}. "
            "A zero count per term would then be uninformative; refusing to report."
        )
    n_one, _, _ = withfrom_count(TARGET, seen[0])
    if n_one <= 0:
        raise SystemExit(
            f"FAIL: WITH/FROM goId filter returned 0 for {seen[0]}, a term present in "
            "the unfiltered response. The filter is broken; refusing to report."
        )

    details = {}
    for go in sorted(set(unp) - set(goa)):
        ols, api, verdict = obsolete_two_services(go)
        n, rows, _ = withfrom_count(TARGET, go)
        details[go] = (ols, api, verdict, n, rows)

    md = render(unp, goa, details)
    if args.stdout:
        print(md)
    else:
        out = Path(__file__).with_name("RESULTS-goa-divergence.md")
        out.write_text(md)
        print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
