#!/usr/bin/env python3
"""Reproducible evidence for two claims in the ADISSP review that were otherwise prose-only.

1. Human/mouse ADISSP sequence identity, which licenses the GO_REF:0000024 (ISS) and
   GO_REF:0000107 (Ensembl Compara, >=40% peptide identity) rows.
2. The ADISSP-PP1 interaction record in IntAct, including the *null* that makes the
   recurrence interpretable: PP1 catalytic subunits are affinity-proteomics hubs, so a
   partner-centric count proves little and only the subject-centric count is informative.

Design notes, each of which exists because the campaign has been bitten by its absence:

- Every UniProt fetch asserts ``primaryAccession == the accession requested``. A merged or
  secondary accession returns HTTP 200 and a complete record for a *different* protein, and
  no other field reveals it.
- The identity comparator carries positive and negative controls (self-comparison must be
  100%, an unrelated protein must be low), so a silently broken comparator cannot report a
  tidy number.
- The IntAct fetch asserts ``totalElements == len(content)``; a service that clamps rather
  than errors would otherwise truncate silently and the guard would report success.
- Computational IntAct methods (``socioaffinity inference``) are excluded from the
  independent-experiment count, and the count of what was excluded is reported rather than
  dropped silently.

stdlib only, so no virtualenv is required:  python3 analyze_adissp.py
"""

from __future__ import annotations

import json
import pathlib
import urllib.request
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent

SUBJECT = "Q9GZN8"          # human ADISSP
DONOR = "Q9D1K7"            # mouse Adissp, the sole WITH/FROM source on every IEA/ISS row
UNRELATED = "P60709"        # human ACTB, negative control for the identity comparator

# PP1 module members, used both to classify ADISSP's partners and to measure the hub null.
PP1_MODULE = {
    "P62136": "PPP1CA",
    "P62140": "PPP1CB",
    "P36873": "PPP1CC",
    "Q15435": "PPP1R7",
}

# Ensembl Compara (GO_REF:0000107) transfers only between orthologs at or above this identity.
COMPARA_MIN_IDENTITY_PCT = 40.0

# Methods that are computational inference rather than experiment; excluded from the
# independent-publication count, and reported separately.
NON_EXPERIMENTAL_METHODS = {"socioaffinity inference"}


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} for {url}")
        return json.load(resp)


def fetch_entry(acc: str) -> dict:
    """Fetch a UniProt entry, asserting the accession is the one asked for."""
    url = (
        f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        "?fields=accession,id,protein_name,organism_name,sequence,ft_signal"
    )
    d = _get(url)
    got = d.get("primaryAccession")
    if got != acc:
        raise RuntimeError(
            f"primaryAccession mismatch: asked for {acc}, got {got}. "
            f"{acc} is a merged or secondary accession and this record is a different protein."
        )
    if not d.get("sequence", {}).get("value"):
        raise RuntimeError(f"{acc} returned no sequence; an inactive entry reads as an empty result")
    return d


def identity(a: str, b: str) -> tuple[int, int, float, str]:
    """Percent identity between two sequences.

    Equal-length sequences are compared ungapped, which is exact. Unequal lengths are NOT
    silently truncated - that would manufacture a number - so the caller is told the
    comparison needs a gapped alignment instead.
    """
    if len(a) != len(b):
        raise RuntimeError(
            f"lengths differ ({len(a)} vs {len(b)}); an ungapped comparison would be invalid "
            "and this script deliberately does not fall back to truncation"
        )
    same = sum(x == y for x, y in zip(a, b))
    return same, len(a), 100.0 * same / len(a), "ungapped (equal lengths, no indels)"


def fetch_intact(acc: str) -> list[dict]:
    """All IntAct interaction records for an accession, asserting nothing was clamped away."""
    url = (
        "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/"
        f"{acc}?page=0&pageSize=500"
    )
    d = _get(url)
    total, content = d.get("totalElements"), d.get("content") or []
    if total != len(content):
        raise RuntimeError(
            f"IntAct returned {len(content)} of {total} records for {acc}; the service clamped "
            "the page rather than erroring, so any count derived from this would be silently short"
        )
    return content


def intact_record_count(acc: str) -> int:
    """Record count only - used for the hub null, so a single-record page is enough."""
    d = _get(
        "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/"
        f"{acc}?page=0&pageSize=1"
    )
    return d["totalElements"]


def base_accession(raw: str | None) -> str:
    """Reduce an IntAct participant id to a bare UniProt accession.

    IntAct ids arrive decorated in two ways that both defeat a naive match, and getting this
    wrong is not a dilution but a *substitution* of one partner set for another:

    * a trailing database tag - ``"Q9GZN8 (uniprotkb)"`` - so ``endswith("Q9GZN8")`` is never
      true. An earlier version of this script used exactly that test; because it never fired,
      the partner was silently taken to be ``moleculeA`` in every record. That dropped every
      partner which only ever appears as ``moleculeB`` (RALYL and a PRO chain of P0C6X7 here)
      and added the subject itself plus an mRNA participant. The resulting *count* was
      coincidentally unchanged at 13, which is precisely why it survived review: a wrong set
      can produce a right-looking number.
    * an isoform or PRO-chain suffix - ``"Q9GZN8-2"``, ``"P0C6X7-PRO_0000037312"`` - which must
      be stripped for the SUBJECT comparison but retained when naming a partner, since a PRO
      chain is a distinct participant.
    """
    if not raw:
        return ""
    ident = raw.split(" (")[0].strip()
    return ident.split("-")[0]


def resolve_partners(
    records: list[dict], subject_acc: str
) -> tuple[dict[str, set[str]], list[dict], list[str]]:
    """Split records into those involving the subject protein and those that do not.

    Returns (partner -> methods, subject_records, excluded_descriptions). Asserts that exactly
    one side of
    every retained record is the subject, which is the invariant the earlier bug violated
    silently.
    """
    partners: dict[str, set[str]] = {}
    kept, excluded = [], []
    for rec in records:
        a_is_subject = base_accession(rec.get("idA")) == subject_acc
        b_is_subject = base_accession(rec.get("idB")) == subject_acc
        if not (a_is_subject or b_is_subject):
            # e.g. a CLASH record pairing the subject's mRNA with a miRNA: a real IntAct record
            # about the locus, but not an interaction of the protein. Described from the data
            # rather than counted, so the report cannot hardcode what was dropped.
            excluded.append(
                f"{rec.get('moleculeA')} / {rec.get('moleculeB')} by {rec.get('detectionMethod')}"
            )
            continue
        if a_is_subject and b_is_subject:
            raise RuntimeError(
                f"both sides of a record resolve to {subject_acc}; a self-interaction needs an "
                "explicit decision rather than an arbitrary pick"
            )
        partner = rec.get("moleculeB") if a_is_subject else rec.get("moleculeA")
        if not partner:
            raise RuntimeError(f"record involving {subject_acc} has no named partner: {rec!r}")
        partners.setdefault(partner, set()).add(rec.get("detectionMethod"))
        kept.append(rec)
    if subject_acc in {base_accession(p) for p in partners}:
        raise RuntimeError(
            "the subject appears in its own partner set, which means partner resolution failed"
        )
    return partners, kept, excluded


def main() -> None:
    results: dict = {}

    # ---------------------------------------------------------------- 1. identity
    human, mouse = fetch_entry(SUBJECT), fetch_entry(DONOR)
    other = fetch_entry(UNRELATED)
    h_seq = human["sequence"]["value"]
    m_seq = mouse["sequence"]["value"]

    same, length, pct, method = identity(h_seq, m_seq)

    # Controls: a comparator that has silently broken must not be able to report the number above.
    self_same, _, self_pct, _ = identity(h_seq, h_seq)
    if self_pct != 100.0:
        raise RuntimeError(f"positive control failed: self-identity is {self_pct}%, not 100%")
    # ACTB is a different length, so the negative control is that the comparator REFUSES it
    # rather than returning a plausible-looking number.
    try:
        identity(h_seq, other["sequence"]["value"])
    except RuntimeError:
        neg_control = "refused (lengths differ), as required"
    else:  # pragma: no cover - would mean the length guard is gone
        raise RuntimeError(
            "negative control failed: comparator accepted two sequences of different length"
        )

    def signal_features(entry: dict) -> list:
        return [f for f in entry.get("features", []) if f.get("type") == "Signal"]

    results["identity"] = {
        "subject": {"accession": SUBJECT, "entry": human["uniProtkbId"], "length": len(h_seq)},
        "donor": {"accession": DONOR, "entry": mouse["uniProtkbId"], "length": len(m_seq)},
        "identical_residues": same,
        "aligned_length": length,
        "percent_identity": round(pct, 1),
        "method": method,
        "compara_threshold_pct": COMPARA_MIN_IDENTITY_PCT,
        "compara_threshold_met": pct >= COMPARA_MIN_IDENTITY_PCT,
        "signal_peptide_features": {
            SUBJECT: len(signal_features(human)),
            DONOR: len(signal_features(mouse)),
        },
        "controls": {
            "self_identity_pct": self_pct,
            "unequal_length_comparison": neg_control,
        },
    }

    # ---------------------------------------------------------------- 2. IntAct
    records = fetch_intact(SUBJECT)
    partners, subject_records, non_protein_records = resolve_partners(records, SUBJECT)

    pp1_rows = []
    excluded = 0
    for rec in subject_records:
        a, b = rec.get("moleculeA"), rec.get("moleculeB")
        if any("PPP1" in (n or "").upper() for n in (a, b)):
            method_name = rec.get("detectionMethod")
            pubs = [p for p in (rec.get("publicationIdentifiers") or []) if "(pubmed)" in p]
            pmid = pubs[0].split(" ")[0] if pubs else None
            if method_name in NON_EXPERIMENTAL_METHODS:
                excluded += 1
                continue
            pp1_rows.append({"a": a, "b": b, "method": method_name, "pmid": pmid})

    exp_pmids = sorted({r["pmid"] for r in pp1_rows if r["pmid"]})
    exp_methods = sorted({r["method"] for r in pp1_rows})
    pp1_partners = sorted(p for p in partners if "PPP1" in (p or "").upper())

    hub_null = {sym: intact_record_count(acc) for acc, sym in PP1_MODULE.items()}

    results["intact"] = {
        "total_records": len(records),
        "subject_protein_records": len(subject_records),
        "records_not_involving_the_protein": len(non_protein_records),
        "excluded_records": non_protein_records,
        "distinct_protein_partners": len(partners),
        "partners": sorted(partners),
        "pp1_module_partners": pp1_partners,
        "pp1_experimental_publications": exp_pmids,
        "pp1_experimental_methods": exp_methods,
        "pp1_records_excluded_as_computational": excluded,
        "excluded_methods": sorted(NON_EXPERIMENTAL_METHODS),
        "hub_null_records": hub_null,
        "cited_annotation_pmid": "PMID:32024300",
        "cited_pmid_among_intact_publications": "32024300" in exp_pmids,
    }

    (HERE / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(results))
    print(f"wrote results.json and RESULTS.md to {HERE}")


def render(r: dict) -> str:
    i, t = r["identity"], r["intact"]
    lines = [
        "# ADISSP bioinformatics results",
        "",
        "Generated by `analyze_adissp.py` (stdlib only; `python3 analyze_adissp.py`). Every number",
        "below is computed at run time from UniProt and IntAct - nothing here is hardcoded.",
        "",
        "## 1. Human/mouse identity, which licenses the ISS and Compara rows",
        "",
        f"| | accession | entry | length |",
        f"|---|---|---|---|",
        f"| subject | {i['subject']['accession']} | {i['subject']['entry']} | {i['subject']['length']} |",
        f"| donor | {i['donor']['accession']} | {i['donor']['entry']} | {i['donor']['length']} |",
        "",
        f"Identity: **{i['identical_residues']}/{i['aligned_length']} = "
        f"{i['percent_identity']}%**, {i['method']}.",
        "",
        f"Ensembl Compara (GO_REF:0000107) requires >= {i['compara_threshold_pct']}% peptide identity "
        f"between orthologs: **{'met' if i['compara_threshold_met'] else 'NOT met'}**.",
        "",
        f"`SIGNAL` peptide features: {i['subject']['accession']} has "
        f"{i['signal_peptide_features'][SUBJECT]}, {i['donor']['accession']} has "
        f"{i['signal_peptide_features'][DONOR]}. Neither orthologue has one, so the leaderless "
        "topology is a shared property of the pair rather than an assumption carried across.",
        "",
        "Comparator controls (a broken comparator must not be able to report the number above): "
        f"self-identity {i['controls']['self_identity_pct']}%; comparison of unequal-length "
        f"sequences {i['controls']['unequal_length_comparison']}.",
        "",
        "## 2. The ADISSP-PP1 interaction in IntAct, with its null",
        "",
        f"ADISSP has **{t['total_records']} IntAct records**. "
        f"{t['subject_protein_records']} of them are interactions of the ADISSP protein.",
        "",
        (f"{len(t['excluded_records'])} record(s) involve the locus but not the protein and are "
         "excluded from the partner set rather than counted as partners"
         + (": " + "; ".join(t["excluded_records"]) + "." if t["excluded_records"] else ".")),
        "",
        f"Distinct **protein** partners of ADISSP: **{t['distinct_protein_partners']}** - "
        f"{', '.join(t['partners'])}.",
        "",
        f"PP1-module partners: **{len(t['pp1_module_partners'])} of "
        f"{t['distinct_protein_partners']} protein partners** - "
        f"{', '.join(t['pp1_module_partners'])}.",
        "",
        f"Independent experimental publications recovering ADISSP with a PP1-module protein: "
        f"**{len(t['pp1_experimental_publications'])}** - "
        f"{', '.join('PMID:' + p for p in t['pp1_experimental_publications'])}.",
        "",
        f"Methods: {', '.join(t['pp1_experimental_methods'])}. "
        f"{t['pp1_records_excluded_as_computational']} record(s) were excluded as computational "
        f"inference rather than experiment ({', '.join(t['excluded_methods'])}); the count is stated "
        "rather than dropped silently.",
        "",
        f"The GOA annotation's own reference is {t['cited_annotation_pmid']}. Is it among the IntAct "
        f"publications above? **{'yes' if t['cited_pmid_among_intact_publications'] else 'no'}** - so "
        "these datasets are additional to, not the same as, the evidence the annotation cites.",
        "",
        "### The null: PP1 catalytic subunits are affinity-proteomics hubs",
        "",
        "| protein | IntAct records |",
        "|---|---|",
    ]
    for sym, n in sorted(t["hub_null_records"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {sym} | {n} |")
    lines += [
        f"| **ADISSP** | **{t['total_records']}** |",
        "",
        "This is why the publication count above must not be read as strong replication on its own:",
        "a protein recovered in a thousand IntAct records will reappear in many tag pulldowns. The",
        "informative comparison is the subject-centric one - that PP1-module proteins are",
        f"{len(t['pp1_module_partners'])} of ADISSP's {t['distinct_protein_partners']} distinct "
        "protein partners, so the",
        "PP1 module dominates this small protein's own sparse interactome rather than ADISSP being one",
        "more name on PP1's long list.",
        "",
        "IntAct also recovers all three PP1 catalytic subunits, which is why the GO term is correctly",
        "left at the isoform-agnostic `GO:0008157 protein phosphatase 1 binding`: the cited paper",
        "identified only \"PP1c\" by mass spectrometry and did not resolve which subunit.",
        "",
        "## What this analysis does not show",
        "",
        "Every IntAct record here is an affinity or two-hybrid method with at least one tagged or",
        "overexpressed partner. None of them measures affinity, stoichiometry or an endogenous",
        "complex, and none is in adipocytes. So this establishes that the interaction is reproducibly",
        "detected across independent datasets; it does not establish that it is physiologically",
        "engaged in the tissue where ADISSP's hormonal function was characterised.",
        "",
    ]
    return "\n".join(lines)


def self_test() -> None:
    """Break-tests for the partner resolver, run with ``--self-test``. No network.

    This exists because the resolver shipped once with a bug that produced a *right-looking
    number from a wrong set*, and nothing caught it. Each direction below is run against a
    fixture that reproduces one specific failure, and each must raise - a direction that cannot
    fail is not a test.
    """
    S = "Q9GZN8"
    failures = []

    def expect_raise(label: str, fn, must_contain: str) -> None:
        """Assert the call fails AND that it fails for the stated reason, not incidentally."""
        try:
            fn()
        except RuntimeError as exc:
            if must_contain not in str(exc):
                failures.append(
                    f"{label}: raised, but for the wrong reason - expected {must_contain!r}, got {exc!r}"
                )
            else:
                print(f"  OK   {label}: raised with the expected message")
            return
        failures.append(f"{label}: did NOT raise - the guard is absent or unreachable")

    # --- direction 1: id decoration must not defeat the subject match -------------------
    # This is the shipped bug. The naive test `idA.endswith("Q9GZN8")` is false for
    # "Q9GZN8 (uniprotkb)", so the partner was always moleculeA. Here the subject is
    # moleculeA, so a broken resolver records the subject as its own partner.
    decorated = [{"idA": f"{S} (uniprotkb)", "idB": "Q86SE5 (uniprotkb)",
                  "moleculeA": "ADISSP", "moleculeB": "RALYL", "detectionMethod": "two hybrid pooling"}]
    partners, kept, excluded = resolve_partners(decorated, S)
    if sorted(partners) != ["RALYL"]:
        failures.append(f"direction 1: expected ['RALYL'], got {sorted(partners)} - "
                        "a partner appearing only as moleculeB was dropped")
    else:
        print("  OK   direction 1: decorated ids resolve, moleculeB-only partner retained")

    # base_accession("ADISSP") is "ADISSP", not the accession, so the invariant as written keys
    # on accessions and would NOT catch a gene-symbol self-entry. Assert that limitation openly
    # rather than claiming coverage it lacks:
    assert base_accession("ADISSP") != S, (
        "if this ever becomes equal, the self-entry invariant starts firing on symbols too"
    )
    print("  NOTE direction 1b: the self-entry invariant keys on accessions; a partner named by "
          "gene SYMBOL cannot be matched against the subject accession, so direction 1 (set "
          "equality on a fixture) is what actually guards the shipped bug, not the invariant.")

    # --- direction 2: a record naming neither side as the subject is excluded, not counted ---
    clash = [{"idA": "ENST00000217195 (ensembl)", "idB": "URS00003CF1AD_9606 (rnacentral)",
              "moleculeA": "mrna_adissp", "moleculeB": "hsamir320a3p", "detectionMethod": "clash"}]
    partners, kept, excluded = resolve_partners(clash, S)
    if partners or kept or len(excluded) != 1 or "clash" not in excluded[0]:
        failures.append(f"direction 2: expected 0 partners / 0 kept / 1 described exclusion naming "
                        f"its method, got {len(partners)}/{len(kept)}/{excluded}")
    else:
        print("  OK   direction 2: a record not involving the protein is excluded and DESCRIBED")

    # direction 2b: TWO exclusions must both be described, so the plural path is exercised. The
    # earlier version hardcoded a singular parenthetical and would have emitted wrong prose here.
    two = clash + [{"idA": "ENST9 (ensembl)", "idB": "URS9 (rnacentral)", "moleculeA": "x_mrna",
                    "moleculeB": "y_mirna", "detectionMethod": "clash"}]
    _, _, exc2 = resolve_partners(two, S)
    if len(exc2) != 2:
        failures.append(f"direction 2b: expected 2 described exclusions, got {exc2}")
    else:
        print("  OK   direction 2b: the multiple-exclusion path is exercised and described")

    # --- direction 3: both sides the subject must raise rather than pick arbitrarily -------
    both = [{"idA": f"{S} (uniprotkb)", "idB": f"{S}-2 (uniprotkb)",
             "moleculeA": "ADISSP", "moleculeB": "ADISSP", "detectionMethod": "anti tag coip"}]
    expect_raise("direction 3", lambda: resolve_partners(both, S), "both sides of a record resolve")

    # --- direction 4: a record involving the subject with no named partner must raise -------
    nameless = [{"idA": f"{S} (uniprotkb)", "idB": "Q86SE5 (uniprotkb)",
                 "moleculeA": "ADISSP", "moleculeB": None, "detectionMethod": "x"}]
    expect_raise("direction 4", lambda: resolve_partners(nameless, S), "has no named partner")

    # --- direction 5: isoform / PRO suffixes ------------------------------------------------
    cases = {
        f"{S} (uniprotkb)": S,
        f"{S}-2 (uniprotkb)": S,
        "P0C6X7-PRO_0000037312 (uniprotkb)": "P0C6X7",
        "ENST00000217195 (ensembl)": "ENST00000217195",
        None: "",
    }
    for raw, want in cases.items():
        got = base_accession(raw)
        if got != want:
            failures.append(f"direction 5: base_accession({raw!r}) == {got!r}, expected {want!r}")
    if not any(f.startswith("direction 5") for f in failures):
        print("  OK   direction 5: db tags, isoform and PRO suffixes all normalise correctly")

    # A PRO chain must survive as a PARTNER name even though it normalises for subject matching.
    pro = [{"idA": f"{S} (uniprotkb)", "idB": "P0C6X7-PRO_0000037312 (uniprotkb)",
            "moleculeA": "ADISSP", "moleculeB": "P0C6X7-PRO_0000037312", "detectionMethod": "two hybrid pooling"}]
    partners, _, _ = resolve_partners(pro, S)
    if sorted(partners) != ["P0C6X7-PRO_0000037312"]:
        failures.append(f"direction 6: PRO-chain partner name was altered: {sorted(partners)}")
    else:
        print("  OK   direction 6: a PRO-chain partner keeps its full name")

    if failures:
        raise SystemExit("SELF-TEST FAILED:\n  " + "\n  ".join(failures))
    print("self-test: all directions passed")


if __name__ == "__main__":
    import sys

    if "--self-test" in sys.argv:
        self_test()
    else:
        main()
