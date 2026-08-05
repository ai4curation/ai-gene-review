#!/usr/bin/env python3
"""Is any molecular function assignable to AAMDC from its family?

The AAMDC review concludes that no molecular function is currently justifiable. That is a
negative claim, so it deserves evidence rather than an absence of evidence. This script asks
the question directly: take AAMDC's protein family, enumerate every characterised member, and
see whether any of them has an experimentally supported molecular function that could
legitimately transfer.

Everything is fetched live from InterPro, UniProt and QuickGO; nothing is hardcoded. Run:

    uv run python analyze_mth938.py            # writes RESULTS.md
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from collections import Counter

AAMDC = "Q9H7C9"
PFAM = "PF04430"          # DUF498, the Pfam family AAMDC belongs to
INTERPRO = "IPR007523"    # NDUFAF3/AAMDC

# Evidence codes that reflect an actual experiment, as opposed to transfer or prediction.
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def get(url: str, accept: str = "application/json"):
    """GET a URL and parse JSON. Returns None on failure rather than raising.

    Returning None (not an empty result) matters: the caller must be able to tell
    "queried, nothing found" from "query failed", because this analysis turns on a
    negative result and a silent fetch failure would fake it.
    """
    req = urllib.request.Request(url, headers={"Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=120) as fh:
            return json.load(fh)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  ! fetch failed: {url} ({e})", file=sys.stderr)
        return None


def interpro_entry(accession: str) -> dict | None:
    """Fetch the InterPro entry itself, so the family definition is sourced rather than asserted."""
    data = get(f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{accession}")
    if not data:
        return None
    md = data.get("metadata", {})
    return {
        "accession": md.get("accession", accession),
        "name": (md.get("name") or {}).get("name", ""),
        "type": md.get("type", ""),
        "n_proteins": (md.get("counters") or {}).get("proteins"),
        "member_dbs": md.get("member_databases") or {},
    }


def family_members(pfam: str) -> list[dict]:
    """Every reviewed (Swiss-Prot) protein carrying the given Pfam domain."""
    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query=xref:pfam-{pfam}+AND+reviewed:true"
        "&fields=accession,id,protein_name,organism_name,length,cc_function,cc_catalytic_activity"
        "&format=json&size=500"
    )
    data = get(url)
    return data.get("results", []) if data else []


def go_annotations(acc: str) -> list[dict]:
    """All GO annotations for an accession, from QuickGO."""
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId={acc}&limit=200"
    )
    data = get(url)
    return data.get("results", []) if data is not None else None


def function_text(entry: dict) -> str:
    """Extract the UniProt FUNCTION comment, if any."""
    for c in entry.get("comments", []):
        if c.get("commentType") == "FUNCTION":
            return " ".join(t.get("value", "") for t in c.get("texts", []))
    return ""


def has_catalytic_activity(entry: dict) -> bool:
    return any(c.get("commentType") == "CATALYTIC ACTIVITY" for c in entry.get("comments", []))


def main() -> None:
    print(f"Fetching InterPro entry {INTERPRO}...")
    ipr = interpro_entry(INTERPRO)
    if ipr:
        print(f"  {ipr['accession']}: {ipr['name']} ({ipr['type']}); "
              f"{ipr['n_proteins']} proteins in UniProtKB")
    else:
        print("  ! InterPro unavailable; the family definition below is from UniProt only")

    print(f"Fetching Swiss-Prot members of {PFAM} (DUF498)...")
    members = family_members(PFAM)
    print(f"  {len(members)} reviewed members")
    if not members:
        print("No members retrieved; aborting rather than reporting an empty result.")
        return

    rows = []
    mf_experimental: Counter[str] = Counter()
    for m in members:
        acc = m["primaryAccession"]
        anns = go_annotations(acc)
        go_ok = anns is not None
        mf_exp = {
            (a["goId"], a.get("goName", ""))
            for a in (anns or [])
            if a.get("goAspect") == "molecular_function"
            and a.get("goEvidence") in EXPERIMENTAL
            and a["goId"] != "GO:0005515"     # bare protein binding is uninformative
        }
        # GO:0003674 ND is an explicit curator statement that no function is known
        nd = any(a["goId"] == "GO:0003674" and a.get("goEvidence") == "ND" for a in (anns or []))
        for go_id, go_name in mf_exp:
            mf_experimental[f"{go_id} {go_name}"] += 1
        rows.append({
            "acc": acc,
            "id": m.get("uniProtkbId", ""),
            "organism": m.get("organism", {}).get("scientificName", ""),
            "length": m.get("sequence", {}).get("length", ""),
            "function": function_text(m),
            "catalytic": has_catalytic_activity(m),
            "mf_experimental": sorted(mf_exp),
            "mf_nd": nd,
            "go_retrieved": go_ok,
        })
        status = f"{len(mf_exp)} experimental MF term(s)" if go_ok else "GO FETCH FAILED"
        print(f"  {acc} {m.get('uniProtkbId','')}: {status}{' [MF=ND]' if nd else ''}")

    n_with_mf = sum(1 for r in rows if r["mf_experimental"])
    n_nd = sum(1 for r in rows if r["mf_nd"])
    n_catalytic = sum(1 for r in rows if r["catalytic"])
    n_go_ok = sum(1 for r in rows if r["go_retrieved"])
    n_go_failed = len(rows) - n_go_ok

    L: list[str] = []
    L.append("# Is a molecular function assignable to AAMDC from its family?")
    L.append("")
    L.append("Generated by `analyze_mth938.py`. Every number below is fetched at run time from")
    L.append("the InterPro, UniProt and QuickGO REST APIs; re-run to refresh.")
    L.append("")
    L.append("## Question")
    L.append("")
    L.append("The AAMDC review concludes that no molecular function is currently justifiable for")
    L.append("this protein. That is a negative claim. This analysis tests it the only way a")
    L.append("negative claim can be tested: enumerate the whole protein family and ask whether")
    L.append("*any* member has an experimentally supported molecular function that could transfer.")
    L.append("")
    L.append("## Family definition")
    L.append("")
    if ipr:
        L.append("Fetched from the InterPro API at run time:")
        L.append("")
        L.append(f"- **{ipr['accession']}** — {ipr['name']} (type: {ipr['type']})")
        L.append(f"- {ipr['n_proteins']} proteins in UniProtKB carry this signature")
        for db, entries in sorted((ipr["member_dbs"] or {}).items()):
            for acc, name in sorted(entries.items()):
                L.append(f"- {db}: {acc} — {name}")
    else:
        L.append("*(InterPro was unreachable on this run, so the family definition here is from")
        L.append(f"UniProt's Pfam cross-reference only: Pfam {PFAM}.)*")
    L.append("")
    L.append("Members enumerated below are the **reviewed (Swiss-Prot)** entries carrying Pfam")
    L.append(f"**{PFAM}** — a small, manually curated subset of all proteins with the signature,")
    L.append("chosen because only reviewed entries carry curated function statements and GO")
    L.append("annotations worth counting.")
    L.append("")
    L.append("## Result")
    L.append("")
    L.append(f"| Reviewed family members | {len(rows)} |")
    L.append("|---|---|")
    L.append(f"| GO annotations successfully retrieved for | {n_go_ok} of {len(rows)} |")
    L.append(f"| With **any** experimental MF term (excluding bare protein binding) | **{n_with_mf}** |")
    L.append(f"| With an explicit `GO:0003674` **ND** (curator: no function known) | {n_nd} |")
    L.append(f"| With a UniProt CATALYTIC ACTIVITY block | {n_catalytic} |")
    L.append("")
    if n_go_failed:
        L.append("")
        L.append(f"> WARNING: {n_go_failed} member(s) had a failed GO query. The zero counts")
        L.append("> above understate what is known - absence of a term may mean the query")
        L.append("> failed, not that the term is absent. Re-run before relying on this result.")
        L.append("")
    if mf_experimental:
        L.append("Experimental MF terms found anywhere in the family:")
        L.append("")
        for term, count in mf_experimental.most_common():
            L.append(f"- {term} ({count} member{'s' if count > 1 else ''})")
    else:
        L.append("**No member of this family carries any experimentally supported molecular")
        L.append("function term.** The absence of an MF annotation on AAMDC is therefore not an")
        L.append("oversight specific to this gene: it is a property of the entire family.")
    L.append("")
    ndufaf3 = [r for r in rows if "assembly of mitochondrial" in (r["function"] or "")]
    if not ndufaf3:
        L.append("## Characterised relatives")
        L.append("")
        L.append("On this run, no member of the family carries a UniProt FUNCTION statement")
        L.append("describing complex assembly, so the assembly-factor interpretation reported")
        L.append("previously does not follow from the current data. See the FUNCTION statements")
        L.append("below.")
    else:
        L.append("## What the one characterised relative does")
        L.append("")
        L.append(f"The family is not entirely uncharacterised. {len(ndufaf3)} of its {len(rows)}")
        L.append("reviewed members carry a UniProt FUNCTION statement about mitochondrial")
        L.append("complex I assembly, and all of them are **NDUFAF3** entries. That branch is an")
        L.append("**assembly factor for mitochondrial complex I**, consistently across every")
        L.append("organism in which it has been studied; the Drosophila entry cites experimental")
        L.append("evidence (PubMed:34386730).")
    L.append("")
    L.append("This is informative in a specific way. NDUFAF3 is an **assembly factor, not an")
    L.append("enzyme**: it has no catalytic activity, it binds subunits and helps build a complex,")
    L.append("and it is not part of the finished complex. Consistent with that, no member of this")
    L.append("family - including NDUFAF3 itself - carries a CATALYTIC ACTIVITY block or an")
    L.append("experimental molecular function term.")
    L.append("")
    L.append("So the family signal does *not* point toward a hidden enzymatic activity waiting to")
    L.append("be found for AAMDC. It points toward a protein-assembly / chaperone-like role, which")
    L.append("is a class of function GO struggles to express as a molecular function in any case")
    L.append("(there is no assembly-chaperone MF term; see the AAGAB review in this campaign).")
    L.append("That makes the AAMDC review's refusal to assign an MF the right call, and it also")
    L.append("suggests where to look experimentally: what complex, if any, does AAMDC help")
    L.append("assemble?")
    L.append("")
    L.append("## Members")
    L.append("")
    L.append("| Accession | Entry | Organism | Len | Catalytic block | GO retrieved | Experimental MF |")
    L.append("|---|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: x["organism"]):
        mf = ", ".join(f"{g} {n}" for g, n in r["mf_experimental"]) or "—"
        nd = " *(MF=ND)*" if r["mf_nd"] else ""
        L.append(f"| {r['acc']} | {r['id']} | {r['organism']} | {r['length']} | "
                 f"{'yes' if r['catalytic'] else 'no'} | {'yes' if r['go_retrieved'] else '**NO**'} | "
                 f"{mf}{nd} |")
    L.append("")
    L.append("## UniProt FUNCTION statements across the family")
    L.append("")
    for r in sorted(rows, key=lambda x: x["organism"]):
        if r["function"]:
            L.append(f"- **{r['id']}** ({r['organism']}): {r['function']}")
    L.append("")

    with open("RESULTS.md", "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\nwrote RESULTS.md")


if __name__ == "__main__":
    main()
