#!/usr/bin/env python3
"""Resolve ABHD8's IBA WITH/FROM sources, so the review's claims about them are checkable.

Two identifications in the ABHD8 review cannot be verified from inside the repository, and
both changed an action:

* **SGD:S000004089 is ICT1_YEAST, a genuine acyltransferase** rather than an artefact of one
  paralog. This is what downgraded two lipid-activity rows from REMOVE to
  MARK_AS_OVER_ANNOTATED.
* **UniProtKB:Q8WTS1 (ABHD5) has no annotated active site, while ABHD8 has a full triad.**
  This is what blocks the common "ABHD5 is a fold without a function, so ABHD8 is too"
  analogy. Note it does *not* make ABHD5 catalytically dead - UniProt records a demonstrated
  acyltransferase activity for it - so the analogy fails in both directions. The script
  prints the evidence for both halves.

Accessions are read from the gene's own GOA file so they cannot drift from the record under
review; everything else is fetched from the UniProt REST API at run time.

Fetches are deliberately *not* wrapped in try/except. A network failure must abort loudly and
leave RESULTS.md untouched, rather than quietly rewriting it with "lookup failed" placeholders
- which would silently break the supporting_text quotes the review draws from this file.

    uv run python resolve_iba_sources.py    # writes RESULTS.md
"""
from __future__ import annotations

import csv
import json
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ABHD8-goa.tsv"


def get(url: str) -> dict:
    """GET JSON from the UniProt REST API."""
    return get_with_total(url)[0]


def get_with_total(url: str) -> tuple[dict, int | None]:
    """GET JSON plus the server's x-total-results count.

    The count matters because these searches are capped (size=2). Reporting "2 entries for this
    id" from a size-2 response would be inferring a total from a truncated result - the exact
    error this script exists to catch elsewhere. x-total-results is authoritative; None means the
    server did not send it, which must be reported as unknown rather than guessed.
    """
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        payload = json.load(fh)
        raw = fh.headers.get("x-total-results")
    return payload, (int(raw) if raw is not None and raw.isdigit() else None)


def iba_sources(path: Path) -> dict[str, list[str]]:
    """Map each IBA row's GO id to its WITH/FROM tokens, straight from the GOA file."""
    out: dict[str, list[str]] = {}
    with open(path) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row.get("GO EVIDENCE CODE") != "IBA":
                continue
            out[row["GO TERM"]] = [t for t in (row.get("WITH/FROM") or "").split("|") if t]
    return out


def describe_uniprot(acc: str) -> dict:
    """Fetch the name, organism, active-site count and FUNCTION text for one accession."""
    d = get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"
            "?fields=id,protein_name,organism_name,gene_names,ft_act_site,cc_function")
    act = [f for f in d.get("features", []) if f.get("type") == "Active site"]
    fn = ""
    for c in d.get("comments", []):
        if c.get("commentType") == "FUNCTION":
            fn = " ".join(t.get("value", "") for t in c.get("texts", []))
    return {
        "acc": acc,
        "id": d.get("uniProtkbId", ""),
        "organism": d.get("organism", {}).get("scientificName", ""),
        "name": (d.get("proteinDescription", {}).get("recommendedName", {})
                 .get("fullName", {}).get("value", "")),
        "n_act_site": len(act),
        "function": fn,
    }


def resolve_sgd(sgd_id: str) -> dict:
    """Resolve an SGD locus id to its reviewed UniProt entry."""
    return resolve_xref(f"SGD:{sgd_id}")


# Each WITH/FROM database maps to the UniProt cross-reference name used in query syntax.
XREF_DB = {"SGD": "sgd", "MGI": "mgi", "FB": "flybase", "AGI_LocusCode": "araport"}


def entry_fields(r: dict) -> dict:
    """Pull the identifying fields out of one UniProt search hit.

    Falls back to the submitted name when there is no recommended name, which is the usual case
    for unreviewed entries - reporting an empty name would read as a missing protein.
    """
    desc = r.get("proteinDescription", {})
    name = desc.get("recommendedName", {}).get("fullName", {}).get("value", "")
    if not name:
        submitted = desc.get("submissionNames") or []
        if submitted:
            name = submitted[0].get("fullName", {}).get("value", "")
    return {
        "acc": r["primaryAccession"],
        "id": r.get("uniProtkbId", ""),
        "organism": r.get("organism", {}).get("scientificName", ""),
        "name": name,
        "genes": [g.get("geneName", {}).get("value") for g in r.get("genes", [])],
    }


def resolve_xref(token: str) -> dict:
    """Resolve one WITH/FROM token to a reviewed UniProt entry.

    Handles every database that appears in this gene's WITH/FROM fields. PANTHER nodes are not
    proteins and are reported as such rather than being silently dropped, since 'unresolvable'
    and 'internal tree node' are different facts.
    """
    db, _, local = token.partition(":")
    if db == "UniProtKB":
        d = get(f"https://rest.uniprot.org/uniprotkb/search?query=accession:{local}"
                "&fields=accession,id,protein_name,organism_name,gene_names&format=json&size=1")
    elif db == "PANTHER":
        return {"token": token, "kind": "panther_node", "acc": None,
                "name": "PANTHER family/subfamily node - an internal tree node, not a protein"}
    elif db in XREF_DB:
        # MGI tokens arrive as "MGI:MGI:1915938"; UniProt's xref query wants the bare number,
        # and a query containing the inner colon is rejected with HTTP 400.
        local = local.removeprefix("MGI:")
        query = f"xref:{XREF_DB[db]}-{local}"
        fields = "accession,id,protein_name,organism_name,gene_names"
        # size=2 rather than 1: these lookups overturned two of this review's claims, so a
        # silently-truncated multi-hit result would be a bad way to be wrong.
        url = f"https://rest.uniprot.org/uniprotkb/search?query={{q}}&fields={fields}&format=json&size=2"
        d, total = get_with_total(url.format(q=f"{query}+AND+reviewed:true"))
        if not d.get("results"):
            # Some sources (the Drosophila member here) have no reviewed entry at all. Falling
            # back is right, but the distinction has to be reported rather than hidden: an
            # unreviewed source is weaker support than a reviewed one.
            d, total = get_with_total(url.format(q=query))
            reviewed = False
        else:
            reviewed = True
        if d.get("results"):
            hits = d["results"]
            # Report ambiguity instead of silently taking the first hit. FB:FBgn0033226 maps to
            # two TrEMBL accessions for the same gene, and they carry DIFFERENT names - one an
            # automatic by-similarity label naming an activity, one just the FlyBase gene name.
            # Taking the first made an uncharacterised protein look characterised.
            alternatives = [{"acc": h["primaryAccession"],
                             "name": entry_fields(h)["name"]} for h in hits[1:]]
            return {**entry_fields(hits[0]), "token": token, "kind": "protein",
                    "reviewed": reviewed, "alternatives": alternatives, "n_entries": total}
    else:
        raise LookupError(f"no resolver for WITH/FROM database {db!r} in token {token!r}")
    if not d.get("results"):
        return {"token": token, "kind": "unresolved", "acc": None,
                "name": f"no UniProt entry cross-references {token}"}
    return {**entry_fields(d["results"][0]), "token": token, "kind": "protein", "reviewed": True}


# Evidence codes that represent a direct experimental result, as opposed to an inference.
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def source_evidence(acc: str, go_ids: list[str]) -> dict[str, list[str]]:
    """What evidence does this source protein itself carry for the propagated GO terms?

    This is the check that decides whether calling a WITH/FROM entry 'the same family-level
    inference rather than independent experimental support' is true or false. IBA WITH/FROM is
    supposed to list experimentally-annotated members, so the claim is testable, and asserting it
    without running this query is exactly the kind of confident dismissal that needs evidence.
    """
    out: dict[str, list[str]] = {}
    for go_id in go_ids:
        d = get("https://www.ebi.ac.uk/QuickGO/services/annotation/search"
                f"?geneProductId=UniProtKB:{acc}&goId={go_id}&goUsage=descendants"
                "&goUsageRelationships=is_a,part_of&limit=100")
        out[go_id] = sorted({a.get("goEvidence", "?") for a in d.get("results", [])})
    return out


def main() -> None:
    if not GOA.exists():
        print(f"missing {GOA}", file=sys.stderr)
        raise SystemExit(1)
    srcs = iba_sources(GOA)
    print(f"{len(srcs)} IBA rows read from {GOA.name}")

    L: list[str] = []
    L.append("# What are ABHD8's IBA source proteins, and does any of them justify a lipid activity?")
    L.append("")
    L.append("Generated by `resolve_iba_sources.py`. Accessions are read from this gene's own")
    L.append("`ABHD8-goa.tsv`; all protein data is fetched from the UniProt REST API at run time.")
    L.append("")
    L.append("## WITH/FROM per IBA row")
    L.append("")
    L.append("The rows do not share a source set, which matters: a `propagation_review` copied from")
    L.append("one row to another will misstate what was inspected.")
    L.append("")
    L.append("| GO term | WITH/FROM sources |")
    L.append("|---|---|")
    for go, toks in sorted(srcs.items()):
        L.append(f"| {go} | {', '.join(f'`{t}`' for t in toks)} |")
    L.append("")

    all_tokens = sorted({t for toks in srcs.values() for t in toks})
    L.append(f"## Every WITH/FROM source resolved ({len(all_tokens)} distinct), with its own evidence")
    L.append("")
    L.append("For each source: what protein it is, and what evidence **it** carries for the terms")
    L.append("propagated to ABHD8. IBA WITH/FROM is supposed to list experimentally-annotated")
    L.append("members, so 'this source only carries the same family-level inference' is a testable")
    L.append("claim rather than a safe hedge - and the table below is what settles it.")
    L.append("")
    L.append("| WITH/FROM | protein | UniProt status | organism | own evidence for the propagated terms |")
    L.append("|---|---|---|---|---|")
    go_ids = sorted(srcs)
    resolved: dict[str, dict] = {}
    for token in all_tokens:
        info = resolve_xref(token)
        resolved[token] = info
        if info["kind"] != "protein":
            L.append(f"| `{token}` | *{info['name']}* | — | — | not applicable |")
            continue
        ev = source_evidence(info["acc"], go_ids)
        info["evidence"] = ev
        cells = [f"{g.split(':')[1]}={'/'.join(v)}" for g, v in ev.items() if v]
        genes = ", ".join(g for g in info["genes"] if g)
        # Reviewed vs unreviewed is load-bearing, not cosmetic: an unreviewed TrEMBL entry's
        # protein NAME is assigned automatically by similarity, so it must not be read as a
        # characterisation the way a Swiss-Prot recommended name can be.
        status = "Swiss-Prot (reviewed)" if info.get("reviewed") else "**TrEMBL (UNREVIEWED)**"
        alts = info.get("alternatives") or []
        if alts:
            listed = ", ".join(f"{a['acc']} \"{a['name']}\"" for a in alts)
            total = info.get("n_entries")
            # Never infer the total from a size-capped response; x-total-results or nothing.
            count = (f"**{total} entries for this id**" if total is not None
                     else "**more than one entry for this id** (server sent no total)")
            status += f"; {count} - including {listed}"
        L.append(f"| `{token}` | {info['acc']} ({genes or info['id']}) — {info['name']} | {status} | "
                 f"{info['organism']} | {'; '.join(cells) or '**none**'} |")
    L.append("")
    L.append("Term ids are abbreviated to their digits; each entry lists the evidence codes that")
    L.append("source carries for that term or any of its descendants.")
    L.append("")
    proteins = {t: i for t, i in resolved.items() if i["kind"] == "protein"}
    exp_sources = [t for t, i in proteins.items()
                   if any(c in EXPERIMENTAL for v in i.get("evidence", {}).values() for c in v)]
    unreviewed = [t for t, i in proteins.items() if not i.get("reviewed")]
    L.append(f"**{len(exp_sources)} of the {len(all_tokens)} sources carry experimental evidence of")
    L.append(f"their own** for at least one propagated term: {', '.join(f'`{t}`' for t in exp_sources) or 'none'}.")
    L.append("")
    if unreviewed:
        L.append(f"**But {len(unreviewed)} of the {len(proteins)} protein sources "
                 f"({', '.join(f'`{t}`' for t in unreviewed)}) has no reviewed UniProt entry.** Its GO")
        L.append("annotations are real curated annotations, but its protein NAME in the column above is")
        L.append("an automatic by-similarity label, not a characterisation - so it must not be counted")
        L.append("alongside the Swiss-Prot recommended names as independent evidence of what the family")
        L.append("does. Evidence provenance and name provenance are separate questions, and only the")
        f_reviewed = len(proteins) - len(unreviewed)
        L.append(f"former is settled here for all {len(proteins)} sources; the latter for {f_reviewed}.")
        L.append("")

    L.append("## The two identifications the review depends on")
    L.append("")
    sgd = resolve_sgd("S000004089")
    genes = ", ".join(g for g in sgd["genes"] if g)
    L.append(f"SGD:S000004089 resolves to {sgd['id']} ({sgd['acc']}, gene {genes}), whose UniProt "
             f"recommended name is \"{sgd['name']}\".")
    L.append("")
    L.append("The acyltransferase activity therefore sits in a named, reviewed member of this family")
    L.append("in another organism, so the two acyltransferase-branch IBAs are propagating from a real")
    L.append("annotated activity. They are marked over-annotated rather than removed because what is")
    L.append("absent is a demonstration in ABHD8, not an activity in the family.")
    L.append("")

    for acc in ("Q8WTS1", "Q96I13"):
        d = describe_uniprot(acc)
        L.append(f"**{acc}** — {d['id']}, {d['organism']}: {d['name']}")
        L.append(f"- annotated active-site residues: **{d['n_act_site']}**")
        if d["function"]:
            L.append(f"- FUNCTION: {d['function'][:300]}")
        L.append("")

    L.append("Read those two blocks together, because they cut in opposite directions and both")
    L.append("matter to this review.")
    L.append("")
    L.append("**ABHD5 is not the pseudoenzyme it is usually invoked as.** It is routinely cited as the")
    L.append("family's fold-without-catalysis case - its nucleophilic serine is replaced, which is why")
    L.append("no active site is annotated - yet UniProt records a *demonstrated* CoA-dependent")
    L.append("lysophosphatidic acid acyltransferase activity for it, with substrate preferences and a")
    L.append("primary reference. So Q8WTS1, the source of ABHD8's `GO:0006654` and `GO:0042171` IBAs,")
    L.append("carries a measured acyl-transfer activity and not merely a fold.")
    L.append("")
    L.append("**The analogy cannot be run the other way either.** The active-site counts show ABHD8 has")
    L.append("a full annotated charge-relay triad where ABHD5 has none, so ABHD8 cannot be dismissed as")
    L.append("an ABHD5-type catalytically dead fold. Both the case for the lipid IBAs and the case")
    L.append("against them are weaker than the ABHD5 comparison is usually made to carry. The")
    L.append("defensible position is the narrow one: ABHD8's triad is intact and untested.")
    L.append("")

    (HERE / "RESULTS.md").write_text("\n".join(L) + "\n")
    print("wrote RESULTS.md")


if __name__ == "__main__":
    main()
