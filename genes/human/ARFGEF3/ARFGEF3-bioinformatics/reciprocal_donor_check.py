"""For every WITH/FROM donor that looks architecturally wrong for the term it
donates, ask what that donor has itself RECEIVED, and on what evidence.

Why this exists
---------------
A mis-clustered family member is both a donor and a victim, and the victim side
is usually the easier half to demonstrate. ARFGEF3's `GO:0005085` row is donated
to by a set of Sec7 exchange factors, but `resolve_withfrom.py` shows one donor
carries **no annotated SEC7 domain and no IPR000904 at all**. If that donor also
*receives* the term by IBA from the same node, then the node is donating exchange
activity to at least two members that may not perform it, and the observation is
about the node rather than about ARFGEF3.

The review states three facts about that donor. Each is derived here rather than
asserted, because an uncommitted check is not a check:

1. which node the donor's own IBA comes from;
2. whether the donor's IBA WITH/FROM set is identical to the subject's;
3. what non-IBA evidence it has, and from how many distinct references.

Suspect donors are **selected by measurement, not named by hand**: any protein
donor of the term that lacks the term's own InterPro signature.

Run: uv run python reciprocal_donor_check.py
     uv run python reciprocal_donor_check.py --self-test
"""

from __future__ import annotations

import csv
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from uniprot import UA

HERE = Path(__file__).resolve().parent

GEF_TERM = "GO:0005085"
SEC7_INTERPRO = "IPR000904"
SUBJECT = "Q5TH69"
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}


def quickgo_annotations_full(acc: str, go_id: str) -> list[dict]:
    """Annotations of `acc` to `go_id`, keeping reference and WITH/FROM.

    `uniprot.quickgo_annotations` discards those fields; this needs them, so it
    queries directly rather than widening the shared helper for one caller.

    Raises on truncation, comparing numberOfHits against len(results) rather than
    against a page-size constant -- a service that clamps an over-large limit
    would sail past a constant while returning a partial page.
    """
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId=UniProtKB:{acc}&goId={go_id}"
        "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100"
    )
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as resp:
        d = json.load(resp)
    n, res = d.get("numberOfHits", 0), d.get("results", [])
    if n > len(res):
        raise RuntimeError(
            f"QuickGO truncated {acc}/{go_id}: numberOfHits={n} but {len(res)} "
            "returned; paginate before trusting this."
        )
    return res


def withfrom_ids(ann: dict) -> list[str]:
    out = []
    for conn in (ann.get("withFrom") or []):
        for x in conn.get("connectedXrefs", []):
            out.append(f"{x.get('db')}:{x.get('id')}" if x.get("db") else x.get("id"))
    return out


def _bare(token: str) -> str:
    """Last colon-separated component, so GOA's `SGD:S000005241` and QuickGO's
    `SGD:S000005241` compare equal to each other and to bare `S000005241`.

    Necessary because the two services disagree on prefixing: GOA writes
    `MGI:MGI:1334257` while QuickGO returns `MGI:1334257` for the same entity.
    Comparing raw strings would report the two sets as different when they are
    the same set, which is the failure this normalisation exists to prevent.
    """
    return token.rsplit(":", 1)[-1]


def subject_iba_withfrom() -> list[str]:
    ents = json.loads((HERE / "supporting_entities.json").read_text())
    rows = [r for r in ents if r["go_id"] == GEF_TERM and r["evidence"] == "IBA"]
    if len(rows) != 1:
        raise RuntimeError(f"expected 1 {GEF_TERM} IBA row, got {len(rows)}")
    return rows[0]["supporting_entities"]


def suspect_donors() -> list[dict[str, str]]:
    """Protein donors of the term that lack the term's InterPro signature.

    Selected by measurement. Returns [] when there are none -- which is a finding,
    not a failure, and is what the self-test's negative control checks.
    """
    tsv = HERE / "withfrom_resolved.tsv"
    if not tsv.exists():
        raise FileNotFoundError(
            f"{tsv} is missing. Run `uv run python resolve_withfrom.py` first.")
    subject_tokens = {_bare(t) for t in subject_iba_withfrom()}
    rows = [r for r in csv.DictReader(tsv.open(), delimiter="\t")
            if r["accession"] and _bare(r["token"]) in subject_tokens]

    # "Exactly one qualifies" must be a claim over ALL protein donors, not over
    # the ones that happened to resolve. resolve_withfrom.py leaves
    # has_sec7_interpro empty for a token it could not resolve, and a bare
    # `== "no"` test would skip those silently -- undercounting suspects while
    # still reporting a confident number. Assert presence rather than validating
    # on match, so a future GOA change that breaks a lookup fails loudly here
    # instead of quietly shrinking the result.
    undetermined = [r["token"] for r in rows if r["has_sec7_interpro"] not in {"yes", "no"}]
    if undetermined:
        raise RuntimeError(
            f"{len(undetermined)} protein donor(s) have no InterPro determination "
            f"({undetermined}); the suspect count would be a floor, not a total. "
            "Re-run `uv run python resolve_withfrom.py` and check those tokens."
        )
    return [r for r in rows if r["has_sec7_interpro"] == "no"]


def analyse_donor(r: dict[str, str], subject_tokens: set[str]) -> dict:
    anns = quickgo_annotations_full(r["accession"], GEF_TERM)
    iba = [a for a in anns if a["goEvidence"] == "IBA"]
    non_iba = [a for a in anns if a["goEvidence"] != "IBA"]

    iba_nodes, iba_sets = [], []
    for a in iba:
        ids = withfrom_ids(a)
        iba_nodes += [i for i in ids if "PTN" in i]
        iba_sets.append({_bare(i) for i in ids})

    same_as_subject = [s == subject_tokens for s in iba_sets]
    refs = sorted({a.get("reference", "") for a in non_iba if a.get("reference")})
    codes = sorted({a["goEvidence"] for a in non_iba})
    return {
        "token": r["token"],
        "accession": r["accession"],
        "gene": r["gene"],
        "organism": r["organism"],
        "reviewed": r["reviewed"],
        "has_sec7_interpro": r["has_sec7_interpro"],
        "n_annotations_to_term": len(anns),
        "receives_term_by_iba": bool(iba),
        "iba_source_nodes": sorted(set(iba_nodes)),
        "iba_withfrom_identical_to_subject_row": all(same_as_subject) and bool(same_as_subject),
        "iba_withfrom_size": [len(s) for s in iba_sets],
        "non_iba_evidence_codes": codes,
        "non_iba_references": refs,
        "n_distinct_non_iba_references": len(refs),
        "has_own_experimental_non_iba": bool(set(codes) & EXPERIMENTAL),
        "has_own_ida": "IDA" in codes,
    }


def self_test() -> list[str]:
    """Break the selection and the comparison on purpose."""
    problems: list[str] = []

    # 1. The suspect selector must be driven by the data, not by a hardcoded id.
    tsv = HERE / "withfrom_resolved.tsv"
    rows = list(csv.DictReader(tsv.open(), delimiter="\t"))
    with_sig = [r for r in rows if r["has_sec7_interpro"] == "yes"]
    if not with_sig:
        problems.append("no donor carries the signature; selector is untestable here")
    else:
        # A donor that HAS the signature must never be selected as suspect.
        chosen = {d["accession"] for d in suspect_donors()}
        if any(r["accession"] in chosen for r in with_sig):
            problems.append("a donor carrying IPR000904 was selected as suspect")

    # 1b. The undetermined-donor guard must FIRE, not be skipped. Blank one
    #     determination in a copy of the TSV and require a raise. Asserts the
    #     target row exists before blanking it, so a drifted column name cannot
    #     turn this into a silent no-op that "passes".
    import shutil
    import tempfile
    tsv_path = HERE / "withfrom_resolved.tsv"
    lines = tsv_path.read_text().splitlines()
    hdr = lines[0].split("\t")
    col = hdr.index("has_sec7_interpro")
    # The victim must be IN the guard's scope: a protein donor of THIS term's
    # row. The TSV also holds the GO:0016192 row's donors, and blanking one of
    # those leaves the guard correctly silent -- which is how the first version
    # of this test "failed" against a guard that was working. Asserting the row
    # exists is not enough; it has to be a row the guard would look at.
    subject_toks = {_bare(t) for t in subject_iba_withfrom()}
    victim = next((i for i, ln in enumerate(lines[1:], start=1)
                   if ln.split("\t")[col] in {"yes", "no"}
                   and ln.split("\t")[hdr.index("accession")]
                   and _bare(ln.split("\t")[hdr.index("token")]) in subject_toks), None)
    if victim is None:
        problems.append("no resolved donor row to blank; guard test is a no-op")
    else:
        # BINARY backup/restore, and a BINARY comparison. resolve_withfrom.py
        # writes through csv.DictWriter, whose default lineterminator is CRLF,
        # while read_text()/write_text() silently translate to LF -- so a
        # text-mode round trip rewrites every line ending in a committed file.
        # The first version of this test did exactly that AND checked its own
        # restore with read_text(), which normalises newlines on read and so
        # could not see the damage it had just done. Verify in the same
        # representation you mutate, or the check is blind by construction.
        original_bytes = tsv_path.read_bytes()
        with tempfile.TemporaryDirectory() as td:
            backup = Path(td) / "orig.tsv"
            backup.write_bytes(original_bytes)
            try:
                parts = lines[victim].split("\t")
                parts[col] = ""
                mutated = [lines[0]] + lines[1:victim] + ["\t".join(parts)] + lines[victim + 1:]
                tsv_path.write_text("\n".join(mutated) + "\n")
                try:
                    suspect_donors()
                    problems.append("undetermined-donor guard did NOT fire on a "
                                    "blanked determination")
                except RuntimeError:
                    pass  # expected
            finally:
                tsv_path.write_bytes(backup.read_bytes())
        if tsv_path.read_bytes() != original_bytes:
            problems.append("self-test failed to restore withfrom_resolved.tsv byte-for-byte")

    # 2. Prefix normalisation must make GOA and QuickGO spellings compare equal,
    #    and must NOT collapse genuinely different ids.
    if _bare("MGI:MGI:1334257") != _bare("MGI:1334257"):
        problems.append("_bare fails to reconcile GOA/QuickGO MGI spellings")
    if _bare("SGD:S000005241") == _bare("SGD:S000000748"):
        problems.append("_bare collapses two distinct SGD ids")

    # 3. The set-identity claim must be falsifiable: perturbing the subject set
    #    by one member must flip it. Asserts the set is non-empty first, so a
    #    dropped input cannot make this a vacuous pass.
    subject = {_bare(t) for t in subject_iba_withfrom()}
    if not subject:
        problems.append("subject WITH/FROM set is empty; identity test would be vacuous")
    else:
        donors = suspect_donors()
        if not donors:
            problems.append("no suspect donor to exercise the identity test")
        else:
            d = analyse_donor(donors[0], subject)
            if not d["iba_withfrom_identical_to_subject_row"]:
                problems.append("baseline identity is False; cannot test the flip")
            else:
                perturbed = set(subject)
                perturbed.pop()
                d2 = analyse_donor(donors[0], perturbed)
                if d2["iba_withfrom_identical_to_subject_row"]:
                    problems.append(
                        "identity still True after removing a member from the "
                        "subject set -- the comparison cannot report a difference")
    return problems


def main() -> None:
    if "--self-test" in sys.argv:
        problems = self_test()
        for p in problems:
            print("SELF-TEST FAIL:", p)
        print(f"self-test: {len(problems)} problem(s)")
        sys.exit(1 if problems else 0)

    subject_tokens = {_bare(t) for t in subject_iba_withfrom()}
    donors = suspect_donors()
    print(f"protein donors of {GEF_TERM} lacking {SEC7_INTERPRO}: {len(donors)}")

    results = [analyse_donor(r, subject_tokens) for r in donors]
    (HERE / "reciprocal_donors.json").write_text(json.dumps(
        {"subject": SUBJECT, "term": GEF_TERM,
         "subject_iba_withfrom_size": len(subject_tokens),
         "donors": results}, indent=2))

    if results:
        with (HERE / "reciprocal_donors.tsv").open("w", newline="") as fh:
            fields = ["token", "accession", "gene", "organism", "reviewed",
                      "has_sec7_interpro", "receives_term_by_iba",
                      "iba_withfrom_identical_to_subject_row",
                      "n_distinct_non_iba_references", "has_own_ida"]
            w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields,
                               extrasaction="ignore")
            w.writeheader()
            w.writerows(results)

    for d in results:
        print(f"\n{d['token']} -> {d['accession']} {d['gene']} ({d['organism']})")
        print(f"   receives {GEF_TERM} by IBA      : {d['receives_term_by_iba']}")
        print(f"   IBA source node(s)             : {d['iba_source_nodes']}")
        print(f"   IBA WITH/FROM == subject's     : "
              f"{d['iba_withfrom_identical_to_subject_row']} "
              f"(sizes {d['iba_withfrom_size']} vs {len(subject_tokens)})")
        print(f"   non-IBA evidence               : {d['non_iba_evidence_codes']}")
        print(f"   non-IBA reference(s)           : {d['non_iba_references']} "
              f"({d['n_distinct_non_iba_references']} distinct)")
        print(f"   holds its own IDA              : {d['has_own_ida']}")


if __name__ == "__main__":
    main()
