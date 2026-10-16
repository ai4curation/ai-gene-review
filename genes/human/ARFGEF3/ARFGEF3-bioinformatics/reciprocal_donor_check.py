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


# Token kinds that are SUPPOSED to resolve to a protein. A PANTHER node or an
# InterPro signature legitimately has no accession; a `mod-id` or `protein` that
# has none failed to resolve, and dropping it silently would make the suspect
# count a floor while it reads as a total.
PROTEIN_KINDS = {"protein", "mod-id"}


def suspect_donors(tsv_path: Path | None = None) -> list[dict[str, str]]:
    """Protein donors of the term that lack the term's InterPro signature.

    Selected by measurement. Returns [] when there are none -- which is a finding,
    not a failure, and is what the self-test's negative control checks.

    `tsv_path` exists so the self-test can point at a COPY. A test that mutates
    the committed file and restores it is one failed restore away from dirtying
    the working tree; parameterising the input removes that failure class instead
    of hardening the recovery from it.
    """
    tsv = tsv_path or (HERE / "withfrom_resolved.tsv")
    if not tsv.exists():
        raise FileNotFoundError(
            f"{tsv} is missing. Run `uv run python resolve_withfrom.py` first.")
    subject_tokens = {_bare(t) for t in subject_iba_withfrom()}
    in_scope = [r for r in csv.DictReader(tsv.open(), delimiter="\t")
                if _bare(r["token"]) in subject_tokens]

    # THE REACHABLE HOLE. resolve_withfrom.py emits an unresolvable MOD id with an
    # EMPTY accession (kind `mod-id`, protein `UNRESOLVED`), so filtering on
    # accession first would drop it before any InterPro test could see it --
    # undercounting suspects while still printing a confident "exactly one".
    # Checked on `kind` precisely because `kind` is what distinguishes a token
    # that failed to resolve from a PANTHER node that legitimately has no
    # accession.
    unresolved = sorted(r["token"] for r in in_scope
                        if r["kind"] in PROTEIN_KINDS and not r["accession"])
    if unresolved:
        raise RuntimeError(
            f"{len(unresolved)} donor token(s) did not resolve to a protein "
            f"({unresolved}); the suspect count would be a floor, not a total. "
            "Re-run `uv run python resolve_withfrom.py` and check those tokens."
        )

    rows = [r for r in in_scope if r["accession"]]

    # Defence in depth ONLY, and unreachable against the current producer:
    # describe_entry() sets has_sec7_interpro unconditionally whenever an
    # accession exists. Kept as a tripwire against a future producer change, and
    # labelled as such so it is not mistaken for the guard above -- an
    # unreachable check that reads as coverage is worse than no check.
    undetermined = sorted(r["token"] for r in rows
                          if r["has_sec7_interpro"] not in {"yes", "no"})
    if undetermined:
        raise RuntimeError(
            f"{len(undetermined)} resolved donor(s) carry no InterPro "
            f"determination ({undetermined}); the producer's contract changed."
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
    committed_tsv = HERE / "withfrom_resolved.tsv"
    committed_bytes = committed_tsv.read_bytes()

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

    # 1b. The REACHABLE guard must fire. Build a copy of the TSV in which one
    #     in-scope protein-kind row has its accession cleared -- exactly what an
    #     unresolvable MOD id looks like -- and require a raise. Operates on a
    #     COPY in a TemporaryDirectory, so the committed file is never touched
    #     and a failed restore cannot dirty the working tree. Asserts the victim
    #     is in the guard's scope before mutating, since a row the selector never
    #     reads would make this a silent no-op that "passes".
    import tempfile

    tsv_path = HERE / "withfrom_resolved.tsv"
    lines = tsv_path.read_text().splitlines()
    hdr = lines[0].split("\t")
    acc_col = hdr.index("accession")
    kind_col = hdr.index("kind")
    tok_col = hdr.index("token")
    det_col = hdr.index("has_sec7_interpro")
    subject_toks = {_bare(t) for t in subject_iba_withfrom()}

    def _copy_with(td: str, col: int, value: str, row_i: int) -> Path:
        copy = Path(td) / "withfrom_resolved.tsv"
        parts = lines[row_i].split("\t")
        parts[col] = value
        copy.write_text("\n".join(
            [lines[0]] + lines[1:row_i] + ["\t".join(parts)] + lines[row_i + 1:]
        ) + "\n")
        return copy

    victim = next((i for i, ln in enumerate(lines[1:], start=1)
                   if ln.split("\t")[acc_col]
                   and ln.split("\t")[kind_col] in PROTEIN_KINDS
                   and _bare(ln.split("\t")[tok_col]) in subject_toks), None)
    if victim is None:
        problems.append("no in-scope protein-kind row to clear; guard test is a no-op")
    else:
        with tempfile.TemporaryDirectory() as td:
            try:
                suspect_donors(_copy_with(td, acc_col, "", victim))
                problems.append("unresolved-donor guard did NOT fire on a cleared "
                                "accession")
            except RuntimeError:
                pass  # expected

        # 1c. The tripwire must also fire when a RESOLVED row loses its
        #     determination, even though the current producer cannot emit that.
        if lines[victim].split("\t")[det_col] not in {"yes", "no"}:
            problems.append("victim row has no determination to blank")
        else:
            with tempfile.TemporaryDirectory() as td:
                try:
                    suspect_donors(_copy_with(td, det_col, "", victim))
                    problems.append("determination tripwire did NOT fire")
                except RuntimeError:
                    pass  # expected

        # 1e. A PANTHER node legitimately has no accession and must NOT trip the
        #     unresolved guard -- otherwise the guard would fire on every run.
        node_i = next((i for i, ln in enumerate(lines[1:], start=1)
                       if ln.split("\t")[kind_col] == "panther-node"), None)
        if node_i is not None:
            try:
                suspect_donors()
            except RuntimeError as exc:
                problems.append(f"guard fires on unmodified input: {exc}")

    # 2. Prefix normalisation must make GOA and QuickGO spellings compare equal,
    #    and must NOT collapse genuinely different ids.
    if _bare("MGI:MGI:1334257") != _bare("MGI:1334257"):
        problems.append("_bare fails to reconcile GOA/QuickGO MGI spellings")
    if _bare("SGD:S000005241") == _bare("SGD:S000000748"):
        problems.append("_bare collapses two distinct SGD ids")

    # The committed TSV must be byte-identical after every test above. Compared
    # in BYTES because read_text() normalises newlines while csv.DictWriter emits
    # CRLF, so a text comparison cannot see a line-ending rewrite.
    if committed_tsv.read_bytes() != committed_bytes:
        problems.append("a test mutated the committed withfrom_resolved.tsv")

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
