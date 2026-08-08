"""Resolve every WITH/FROM token in ACTA1's GOA TSV and query each source's own
evidence for the term it donated.

Outputs source_entities-ready JSON. Counts are derived FROM the GOA file, never
by hand; the script asserts the per-row token count matches the GOA field.
"""
import csv, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ACTA1-goa.tsv"
OUT = HERE / "withfrom_resolution.json"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# xref db name used by UniProt's `xref:` search for non-UniProt source databases
XREF_DB = {
    "MGI": "mgi", "RGD": "rgd", "SGD": "sgd", "WB": "wormbase", "FB": "flybase",
    "dictyBase": "dictybase", "PomBase": "pombase", "CGD": "cgd",
}

# Sources whose own-evidence query must be routed via UniProt because QuickGO
# rejects the native identifier; recorded here only for documentation - the code
# discovers the rejection at runtime rather than assuming this list is complete.
KNOWN_QUICKGO_GAPS = {"CGD"}


class Rejected(Exception):
    """The service understood the request and refused it (HTTP 400).

    Distinct from a transient failure: retrying cannot help, and the refusal is
    itself information (e.g. QuickGO does not index a given source database).
    """


def get(url: str) -> dict:
    for attempt in range(4):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code == 400:
                raise Rejected(url) from exc
            if attempt == 3:
                raise RuntimeError(f"failed after 4 attempts: {url}") from exc
            time.sleep(2 * (attempt + 1))
        except urllib.error.URLError as exc:
            if attempt == 3:
                raise RuntimeError(f"failed after 4 attempts: {url}") from exc
            time.sleep(2 * (attempt + 1))
    raise AssertionError("unreachable")


def _search(query: str) -> list[dict]:
    """size=5 so a multi-hit identifier is reported rather than silently collapsed."""
    q = urllib.parse.quote(query)
    d = get(
        "https://rest.uniprot.org/uniprotkb/search?query=" + q +
        "&fields=accession,id,protein_name,gene_names,organism_name,length&format=json&size=5"
    )
    return d.get("results", [])


def resolve_uniprot(acc: str) -> list[dict]:
    """Resolve a UniProtKB accession, refusing to return a dead entry quietly.

    Two independent guards, because each alone is insufficient:

    1. ``primaryAccession`` must equal the accession asked for. Catches a search
       that answered with a neighbour instead of the requested entry.
    2. ``entryType`` must not be ``Inactive``. This is the one that matters, and
       guard 1 does NOT imply it: a merged/deleted accession such as ``O15507``
       comes back **with its own accession** and an otherwise empty record - no
       protein name, no gene, no organism. Querying such an entry for annotations
       returns zero, which is indistinguishable from a live protein that genuinely
       carries none. That silent zero is the failure being prevented here, so the
       replacement accession is named in the error.
    """
    base = acc.split("-")[0]
    raw = _search(f"accession:{base}")
    for e in raw:
        if e.get("entryType") == "Inactive" and e["primaryAccession"] == base:
            reason = e.get("inactiveReason", {})
            raise RuntimeError(
                f"accession {acc} is an INACTIVE UniProt entry "
                f"({reason.get('inactiveReasonType')}"
                f"{' -> ' + ','.join(reason.get('mergeDemergeTo', [])) if reason.get('mergeDemergeTo') else ''}"
                "); querying it for annotations would return a vacuous zero"
            )
    hits = [summarise(e) for e in raw]
    if hits and not any(h["accession"] == base for h in hits):
        raise RuntimeError(
            f"accession {acc} resolved only to {[h['accession'] for h in hits]}; "
            "primaryAccession does not match the requested id"
        )
    return hits


def resolve_xref(db: str, token: str) -> tuple[list[dict], str]:
    """Resolve a model-organism WITH/FROM token to UniProt entries.

    Two lookup routes are needed because neither works for every source database:
    ``xref:<db>-<id>`` resolves MGI/RGD/SGD/dictyBase/PomBase/FlyBase/CGD, but
    UniProt does not cross-reference WormBase by ``WBGene`` id, so those need a
    plain identifier query. The route actually used is returned so that it shows
    up in the output instead of being invisible.

    MGI tokens arrive as ``MGI:MGI:nnn``; a query containing the inner colon
    returns HTTP 400, so the bare number is used.
    """
    bare = _bare(token)
    route = f"xref:{XREF_DB[db]}-{bare}"
    results = _search(route)
    if not results:
        route = f"identifier-query:{bare}"
        results = _search(bare)
    return [summarise(e) for e in results], route


def _bare(identifier: str) -> str:
    """Last colon-separated segment.

    Needed on both sides of the comparison: a GOA token is ``MGI:MGI:87906``
    while UniProt stores the cross-reference id as ``MGI:87906``, so comparing
    the raw strings would reject every correct MGI mapping.
    """
    return identifier.split(":")[-1]


def cross_references(acc: str) -> set[str]:
    """The resolved entry's own cross-reference ids, for verifying a mapping."""
    d = get(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=xref_wormbase,"
        "xref_mgi,xref_rgd,xref_sgd,xref_flybase,xref_dictybase,xref_pombase,xref_cgd"
    )
    ids: set[str] = set()
    for x in d.get("uniProtKBCrossReferences", []):
        if x.get("id"):
            ids.add(_bare(x["id"]))
        for prop in x.get("properties", []):
            if prop.get("value") and prop["value"] != "-":
                ids.add(_bare(prop["value"]))
    return ids


def verify_mapping(token: str, candidates: list[dict]) -> dict:
    """Check the source id really appears in the resolved entry's own xrefs.

    Load-bearing for the plain-identifier route, which can match on free text.
    A resolution that cannot be confirmed this way is reported as unverified
    rather than silently trusted.
    """
    bare = _bare(token)
    verified: list[str] = []
    unverified: list[str] = []
    for c in candidates:
        target = verified if bare in cross_references(c["accession"]) else unverified
        target.append(c["accession"])
    return {
        "verified": verified,
        "unverified": unverified,
        "all_verified": bool(verified) and not unverified,
    }


def summarise(e: dict) -> dict:
    pd = e.get("proteinDescription", {})
    name = (pd.get("recommendedName", {}).get("fullName", {}) or {}).get("value")
    if not name:
        sub = pd.get("submissionNames") or []
        if sub:
            name = sub[0].get("fullName", {}).get("value")
    return {
        "accession": e["primaryAccession"],
        "entry_name": e.get("uniProtkbId"),
        "reviewed": e.get("entryType", "").startswith("UniProtKB reviewed"),
        "protein_name": name,
        "genes": [g.get("geneName", {}).get("value") for g in e.get("genes", [])],
        "organism": e.get("organism", {}).get("scientificName"),
        "length": e.get("sequence", {}).get("length"),
    }


def _quickgo(gp_id: str, go_id: str) -> dict:
    return get(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId={gp_id}&goId={go_id}&goUsage=descendants"
        "&goUsageRelationships=is_a,part_of&limit=100"
    )


def own_evidence(gp_id: str, go_id: str, fallback_accessions: list[str]) -> dict:
    """What evidence does this source itself carry for the term it donated?

    QuickGO does not index every source database that appears in a GOA WITH/FROM
    field (CGD, for one), and answers such a query with HTTP 400. That refusal is
    recorded in ``route`` and the query is retried against the source's resolved
    UniProt accession, so the fallback is visible in the output rather than silent.
    """
    route = gp_id
    try:
        d = _quickgo(gp_id, go_id)
    except Rejected:
        if not fallback_accessions:
            return {"n": 0, "rows": [], "has_own_experimental": False,
                    "exact_term": False, "route": None,
                    "route_note": f"QuickGO rejected {gp_id} and no UniProt accession resolved"}
        route = f"UniProtKB:{fallback_accessions[0]}"
        print(f"    QuickGO rejected {gp_id}; querying {route} instead", flush=True)
        d = _quickgo(route, go_id)
    rows = [
        {"goId": r["goId"], "evidence": r["goEvidence"], "reference": r["reference"],
         "assignedBy": r["assignedBy"]}
        for r in d.get("results", [])
    ]
    return {
        "n": d.get("numberOfHits", 0),
        "rows": rows,
        "has_own_experimental": any(r["evidence"] in EXPERIMENTAL for r in rows),
        "exact_term": any(r["goId"] == go_id for r in rows),
        "route": route,
        "route_note": None if route == gp_id else f"fell back from {gp_id}",
    }


def main() -> None:
    if not GOA.exists():
        raise SystemExit(f"missing input {GOA}; run: just fetch-gene human ACTA1")
    out: dict = {"rows": []}
    with GOA.open() as fh:
        for i, row in enumerate(csv.DictReader(fh, delimiter="\t"), start=1):
            raw = (row["WITH/FROM"] or "").strip()
            if not raw:
                continue
            tokens = raw.split("|")
            go_id = row["GO TERM"]
            entry = {
                "goa_row": i, "go_id": go_id, "go_name": row["GO NAME"],
                "evidence": row["GO EVIDENCE CODE"], "reference": row["REFERENCE"],
                "assigned_by": row["ASSIGNED BY"],
                "n_tokens_in_goa": len(tokens), "tokens": tokens, "sources": [],
            }
            for tok in tokens:
                db, _, ident = tok.partition(":")
                rec: dict = {"token": tok, "db": db}
                if db == "PANTHER":
                    rec["kind"] = "panther_tree_node"
                    rec["note"] = "internal PANTHER tree node, not a protein"
                elif db == "UniProtKB":
                    rec["kind"] = "protein"
                    rec["candidates"] = resolve_uniprot(ident)
                    rec["own_evidence"] = own_evidence(
                        f"UniProtKB:{ident}", go_id,
                        [c["accession"] for c in rec["candidates"]],
                    )
                elif db.startswith("UniProtKB-"):
                    rec["kind"] = "uniprot_controlled_vocabulary"
                    rec["note"] = f"{db} term {ident}, not a gene product"
                elif db in XREF_DB:
                    rec["kind"] = "protein"
                    rec["candidates"], rec["resolution_route"] = resolve_xref(db, tok)
                    rec["mapping_check"] = verify_mapping(tok, rec["candidates"])
                    rec["own_evidence"] = own_evidence(
                        tok, go_id, [c["accession"] for c in rec["candidates"]]
                    )
                elif db == "ensembl":
                    rec["kind"] = "ensembl_protein"
                    rec["note"] = f"Ensembl protein {ident}"
                else:
                    raise RuntimeError(f"unhandled WITH/FROM db {db!r} in token {tok!r}")
                entry["sources"].append(rec)
            assert len(entry["sources"]) == entry["n_tokens_in_goa"], (
                f"row {i}: resolved {len(entry['sources'])} sources for "
                f"{entry['n_tokens_in_goa']} GOA tokens"
            )
            unresolved = [
                s["token"] for s in entry["sources"]
                if s["kind"] == "protein" and not s.get("candidates")
            ]
            entry["unresolved_protein_tokens"] = unresolved
            multi = [
                s["token"] for s in entry["sources"]
                if s["kind"] == "protein" and len(s.get("candidates", [])) > 1
            ]
            entry["ambiguous_protein_tokens"] = multi
            prot = [s for s in entry["sources"] if s["kind"] == "protein"]
            entry["n_protein_sources"] = len(prot)
            entry["n_with_own_experimental"] = sum(
                1 for s in prot if s["own_evidence"]["has_own_experimental"]
            )
            entry["n_with_exact_term"] = sum(
                1 for s in prot if s["own_evidence"]["exact_term"]
            )
            entry["n_reviewed_sources"] = sum(
                1 for s in prot if any(c["reviewed"] for c in s.get("candidates", []))
            )
            out["rows"].append(entry)
            print(
                f"row {i:2} {go_id} {row['GO EVIDENCE CODE']:4} "
                f"tokens={len(tokens):2} proteins={entry['n_protein_sources']:2} "
                f"own_exp={entry['n_with_own_experimental']:2} "
                f"exact_term={entry['n_with_exact_term']:2} "
                f"unresolved={len(unresolved)} ambiguous={len(multi)}",
                flush=True,
            )
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwrote {OUT}")


def self_test() -> None:
    """Exercise the guards, including on a deliberately WRONG mapping.

    A self-test can only prove the guards you thought of fire; it cannot tell you
    which guard you failed to write. Each case below therefore states the failure
    it is protecting against.
    """
    # 1. A correct mapping must verify.
    cands, route = resolve_xref("MGI", "MGI:MGI:87906")
    assert cands, "MGI:MGI:87906 must resolve"
    assert any(c["accession"] == "P63260" for c in cands), cands
    assert verify_mapping("MGI:MGI:87906", cands)["all_verified"]
    print(f"self-test 1 OK: correct mapping verifies (route={route})")

    # 2. A deliberately WRONG mapping must FAIL verification, or the check is
    #    decorative. Real token paired with a real but unrelated accession.
    wrong = [{"accession": "P68133"}]  # human ACTA1, which is not MGI:87906
    assert not verify_mapping("MGI:MGI:87906", wrong)["all_verified"], (
        "verify_mapping accepted a wrong mapping - the guard is broken"
    )
    print("self-test 2 OK: wrong mapping rejected")

    # 3. QuickGO rejects every non-UniProtKB gene product id used in this file's
    #    WITH/FROM fields. own_evidence must record the fallback route rather than
    #    report a vacuous zero, which would read as "this source has no evidence".
    ev = own_evidence("WB:WBGene00000064", "GO:0015629", ["P10984"])
    assert ev["route"] == "UniProtKB:P10984", ev
    assert ev["route_note"], "the fallback must be recorded, not silent"
    assert ev["n"] > 0, "C. elegans act-2 must carry actin-cytoskeleton annotations"
    print(f"self-test 3 OK: fallback recorded (route={ev['route']}, n={ev['n']})")

    # 4. The liveness guard must distinguish a DEAD accession from a live one that
    #    genuinely carries no annotations. O15507 is inactive, and note that it
    #    comes back WITH its own accession, so an accession-match check alone
    #    passes it - this case is what proved the accession check insufficient.
    try:
        resolve_uniprot("O15507")
    except RuntimeError as exc:
        assert "INACTIVE" in str(exc), exc
        print(f"self-test 4 OK: liveness guard fired -- {exc}")
    else:
        raise AssertionError(
            "resolve_uniprot accepted inactive accession O15507; the liveness "
            "guard is broken and a vacuous zero could be read as a finding"
        )

    # 5. A live accession must still pass guard 4, or the guard is a blanket
    #    refusal rather than a discriminator.
    live = resolve_uniprot("P68133")
    assert live and live[0]["genes"] == ["ACTA1"], live
    print("self-test 5 OK: live accession P68133 passes the liveness guard")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        main()
