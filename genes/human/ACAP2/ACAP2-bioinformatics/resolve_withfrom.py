#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Resolve every WITH/FROM identifier in ACAP2's GOA file, and check the domain
architecture of each protein-level source.

Motivation
----------
The ACAP2 review turns on two claims that cannot be read off the GOA file itself:

1. Which WITH/FROM entries are true orthologs of ACAP2 and which are paralogs or
   more distant family members.
2. Whether each source protein actually carries the ArfGAP catalytic domain, i.e.
   whether it could plausibly do what ACAP2 does.

This script answers both from primary APIs and writes RESULTS.md. It hardcodes no
findings: every value in the output comes from a live response, and any lookup that
fails is reported as UNRESOLVED rather than guessed.

Usage
-----
    uv run resolve_withfrom.py            # writes RESULTS.md next to this script
    uv run resolve_withfrom.py --stdout    # print instead of writing

Only the standard library is used, so it also runs under a bare `python3`.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ACAP2-goa.tsv"
PANTHER_CSV = HERE.parents[3] / "interpro" / "panther" / "PTHR23180" / "PTHR23180-entries.csv"

TARGET = "Q15057"  # human ACAP2
PANTHER_NODE = "PTN001142372"
UA = {"User-Agent": "ai-gene-review/ACAP2-withfrom-resolver"}


def get(url: str, accept: str = "application/json", tries: int = 3):
    """Fetch a URL, returning parsed JSON / raw text, or None on persistent failure."""
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={**UA, "Accept": accept})
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                raw = fh.read().decode("utf-8", "replace")
            return json.loads(raw) if accept == "application/json" else raw
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            if attempt == tries - 1:
                print(f"  ! failed {url}: {exc}", file=sys.stderr)
                return None
            time.sleep(2 * (attempt + 1))
    return None


# --------------------------------------------------------------------------- #
# UniProt
# --------------------------------------------------------------------------- #

FIELDS = "accession,id,gene_names,organism_name,protein_name,length,ft_domain,xref_panther,cc_function"


def uniprot_entry(acc: str) -> dict | None:
    d = get(f"https://rest.uniprot.org/uniprotkb/{acc}.json")
    return summarise_uniprot(d) if d else None


def uniprot_by_xref(db: str, value: str) -> list[dict]:
    """Search UniProt for entries cross-referenced to an external database id."""
    q = urllib.parse.quote(f"xref:{db}-{value}")
    d = get(f"https://rest.uniprot.org/uniprotkb/search?query={q}&fields={FIELDS}&size=5")
    if not d:
        return []
    return [summarise_uniprot(e) for e in d.get("results", [])]


def summarise_uniprot(e: dict) -> dict:
    domains = [
        (
            f["location"]["start"].get("value"),
            f["location"]["end"].get("value"),
            f.get("description"),
        )
        for f in e.get("features", [])
        if f["type"] == "Domain"
    ]
    panther = [
        (x["id"], next((p["value"] for p in x.get("properties", []) if p["key"] == "EntryName"), ""))
        for x in e.get("uniProtKBCrossReferences", [])
        if x["database"] == "PANTHER"
    ]
    function = ""
    for c in e.get("comments", []):
        if c["commentType"] == "FUNCTION" and c.get("texts"):
            function = c["texts"][0]["value"]
            break
    return {
        "accession": e.get("primaryAccession"),
        "entry_name": e.get("uniProtkbId"),
        "organism": e.get("organism", {}).get("scientificName"),
        "genes": [g.get("geneName", {}).get("value") for g in e.get("genes", [])],
        "protein_name": (
            e.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value")
            or (e.get("proteinDescription", {}).get("submissionNames") or [{}])[0]
            .get("fullName", {})
            .get("value")
        ),
        "length": e.get("sequence", {}).get("length"),
        "domains": domains,
        "panther": panther,
        "function": function[:160],
        "reviewed": e.get("entryType", "").startswith("UniProtKB reviewed"),
    }


# --------------------------------------------------------------------------- #
# Model-organism database resolvers
# --------------------------------------------------------------------------- #


def resolve_alliance(curie: str) -> dict | None:
    d = get(f"https://www.alliancegenome.org/api/gene/{curie}")
    if not d or not d.get("gene"):
        return None
    g = d["gene"]
    return {
        "symbol": (g.get("geneSymbol") or {}).get("displayText"),
        "full_name": (g.get("geneFullName") or {}).get("displayText"),
        "organism": (g.get("taxon") or {}).get("name"),
        "source": "AllianceGenome /api/gene",
    }


def resolve_wormbase(wbid: str) -> dict | None:
    d = get(f"https://rest.wormbase.org/rest/field/gene/{wbid}/name")
    if not d:
        return None
    lab = ((d.get("name") or {}).get("data") or {}).get("label")
    return {"symbol": lab, "organism": "Caenorhabditis elegans", "source": "WormBase REST"} if lab else None


def resolve_flybase(fbid: str) -> dict | None:
    d = get(f"https://api.flybase.org/api/v1.0/gene/summaries/auto/{fbid}")
    if not d:
        return None
    res = ((d.get("resultset") or {}).get("result") or [])
    if not res:
        return None
    return {"summary": res[0].get("summary", "")[:420], "source": "FlyBase API gene summary"}


def resolve_panther_gene(external_id: str, taxon: int) -> dict | None:
    d = get(
        "https://pantherdb.org/services/oai/pantherdb/geneinfo"
        f"?geneInputList={urllib.parse.quote(external_id)}&organism={taxon}"
    )
    if not d:
        return None
    g = ((d.get("search") or {}).get("mapped_genes") or {}).get("gene")
    if isinstance(g, list):
        g = g[0] if g else None
    if not g:
        return None
    return {"family_id": g.get("family_id"), "sf_id": g.get("sf_id"), "source": "PANTHER geneinfo"}


# --------------------------------------------------------------------------- #
# Node scope
# --------------------------------------------------------------------------- #


def source_own_evidence(acc: str, go_id: str) -> dict:
    """What evidence does the SOURCE protein itself hold for the term it donates?

    An IBA/ISS WITH/FROM list is supposed to name experimentally annotated family
    members, so this distinguishes a source with real wet-lab evidence from one that
    only carries the same family-level inference. Descendant terms count, since the
    source may be annotated more specifically than the propagated term.
    """
    d = get(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId={acc}&goId={go_id}&goUsage=descendants"
        "&goUsageRelationships=is_a,part_of&limit=50"
    )
    if not d:
        return {}
    codes: dict[str, int] = {}
    for r in d.get("results", []):
        codes[r.get("goEvidence", "?")] = codes.get(r.get("goEvidence", "?"), 0) + 1
    return {"n_hits": d.get("numberOfHits"), "codes": codes}


EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HDA", "HMP", "HGI", "HEP", "HTP"}


def node_scope(node: str) -> dict:
    """How widely is this PANTHER node's annotation set distributed?"""
    d = get(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?withFrom=PANTHER:{node}&limit=200"
    )
    if not d:
        return {}
    symbols, terms = set(), {}
    for r in d.get("results", []):
        if r.get("symbol"):
            symbols.add(r["symbol"])
        if r.get("goId"):
            terms[r["goId"]] = r.get("goName") or ""
    return {"n_hits": d.get("numberOfHits"), "symbols": sorted(symbols), "terms": terms}


# --------------------------------------------------------------------------- #
# GOA parsing
# --------------------------------------------------------------------------- #


def read_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def withfrom_ids(rows: list[dict]) -> dict[str, list[str]]:
    """Map each distinct WITH/FROM id to the GO terms it supports."""
    out: dict[str, list[str]] = {}
    for r in rows:
        for tok in (r.get("WITH/FROM") or "").split("|"):
            tok = tok.strip()
            if tok:
                out.setdefault(tok, []).append(f"{r['GO TERM']} ({r['GO EVIDENCE CODE']})")
    return out


def resolve(token: str) -> dict:
    """Dispatch a WITH/FROM token to the right resolver. Never guesses."""
    rec: dict = {"id": token}
    if token.startswith("UniProtKB:"):
        rec["uniprot"] = uniprot_entry(token.split(":", 1)[1])
    elif token.startswith("MGI:MGI:") or token.startswith("RGD:") or token.startswith("SGD:"):
        curie = token[4:] if token.startswith("MGI:MGI:") else token
        rec["mod"] = resolve_alliance(curie)
        db = {"M": "mgi", "R": "rgd", "S": "sgd"}[token[0]]
        # UniProt's xref:mgi- index wants the bare numeric id; the inner colon 400s.
        key = curie.split(":", 1)[1]
        hits = uniprot_by_xref(db, key)
        rec["uniprot"] = next((h for h in hits if h["reviewed"]), hits[0] if hits else None)
    elif token.startswith("WB:"):
        wb = token.split(":", 1)[1]
        rec["mod"] = resolve_wormbase(wb)
        rec["panther"] = resolve_panther_gene(wb, 6239)
        # UniProt has no xref:wormbase- index for WBGene ids, so go via the symbol
        # WormBase just gave us. Only accept a reviewed C. elegans entry.
        sym = (rec["mod"] or {}).get("symbol")
        if sym:
            d = get(
                "https://rest.uniprot.org/uniprotkb/search?query="
                + urllib.parse.quote(f"gene_exact:{sym} AND organism_id:6239 AND reviewed:true")
                + f"&fields={FIELDS}&size=3"
            )
            hits = [summarise_uniprot(e) for e in (d or {}).get("results", [])]
            rec["uniprot"] = hits[0] if hits else None
    elif token.startswith("FB:"):
        fb = token.split(":", 1)[1]
        rec["mod"] = resolve_flybase(fb)
        rec["panther"] = resolve_panther_gene(fb, 7227)
        rec["isoforms"] = uniprot_by_xref("flybase", fb)
    elif token.startswith("dictyBase:"):
        hits = uniprot_by_xref("dictybase", token.split(":", 1)[1])
        rec["uniprot"] = hits[0] if hits else None
    elif token.startswith("PomBase:") or token.startswith("AGI_LocusCode:"):
        gene = token.split(":", 1)[1]
        d = get(
            "https://rest.uniprot.org/uniprotkb/search?query="
            f"{urllib.parse.quote('gene_exact:' + gene)}&fields={FIELDS}&size=3"
        )
        results = [summarise_uniprot(e) for e in (d or {}).get("results", [])]
        rec["uniprot"] = next((r for r in results if r["reviewed"]), results[0] if results else None)
    elif token.startswith("ensembl:"):
        hits = uniprot_by_xref("ensembl", token.split(":", 1)[1])
        rec["uniprot"] = hits[0] if hits else None
    elif token.startswith("UniProtKB-SubCell:"):
        d = get(f"https://rest.uniprot.org/locations/{token.split(':', 1)[1]}")
        rec["note"] = (
            f"UniProt subcellular-location vocabulary term: {d.get('name')} ({d.get('category')})"
            if d
            else "UNRESOLVED"
        )
    elif token.startswith(("PANTHER:", "InterPro:")):
        rec["note"] = "node/signature, not a gene product"
    else:
        rec["note"] = "UNRESOLVED - no resolver for this prefix"
    return rec


def has_arfgap(rec: dict) -> str:
    up = rec.get("uniprot")
    if not up:
        return "n/a"
    names = " ".join(str(d[2]) for d in up["domains"])
    return "yes" if "Arf-GAP" in names or "ArfGAP" in names else "NO"


def fmt_domains(up: dict | None) -> str:
    if not up or not up["domains"]:
        return "(none annotated)"
    return "; ".join(f"{d[2]} {d[0]}-{d[1]}" for d in up["domains"])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    if not GOA.exists():
        print(f"missing {GOA}", file=sys.stderr)
        return 1

    rows = read_goa(GOA)
    ids = withfrom_ids(rows)
    print(f"resolving {len(ids)} WITH/FROM ids from {len(rows)} GOA rows", file=sys.stderr)

    target = uniprot_entry(TARGET)
    resolved = {tok: resolve(tok) for tok in sorted(ids)}
    scope = node_scope(PANTHER_NODE)

    sf399 = []
    if PANTHER_CSV.exists():
        with PANTHER_CSV.open() as fh:
            sf399 = [r for r in csv.DictReader(fh) if r.get("subfamily") == "PTHR23180:SF399"]

    out: list[str] = []
    w = out.append
    w("# ACAP2 WITH/FROM resolution and domain-architecture check\n")
    w(
        "Generated by `resolve_withfrom.py` from live API responses. Re-run with "
        "`uv run resolve_withfrom.py` to regenerate; values may change as the "
        "underlying databases are updated.\n"
    )
    w("## Reference: human ACAP2\n")
    if target:
        w(f"- `{target['accession']}` {target['entry_name']} ({target['organism']}), {target['length']} aa")
        w(f"- domains: {fmt_domains(target)}")
        w(f"- PANTHER: {', '.join(f'{p[0]} {p[1]}' for p in target['panther'])}\n")
    else:
        w("- UNRESOLVED (lookup failed)\n")

    w("## Every WITH/FROM identifier in ACAP2-goa.tsv\n")
    w("| WITH/FROM | resolves to | organism | length | ArfGAP domain? | supports |")
    w("|---|---|---|---|---|---|")
    for tok, rec in resolved.items():
        up = rec.get("uniprot")
        mod = rec.get("mod")
        if up:
            who = f"{up['accession']} {up['entry_name']} ({'/'.join(x for x in up['genes'] if x) or '-'})"
            org, ln = up["organism"] or "?", up["length"] or "?"
        elif mod and mod.get("symbol"):
            who = f"{mod['symbol']} - {mod.get('full_name') or ''}".strip(" -")
            org, ln = mod.get("organism", "?"), "?"
        elif mod:
            who = "see notes below"
            org, ln = "Drosophila melanogaster", "?"
        else:
            who = rec.get("note", "UNRESOLVED")
            org, ln = "-", "-"
        terms = ", ".join(sorted(set(ids[tok])))
        w(f"| `{tok}` | {who} | {org} | {ln} | {has_arfgap(rec)} | {terms} |")
    w("")

    w("## Ortholog vs paralog\n")
    w(
        "Classification is by gene symbol and by whether the source carries an ArfGAP "
        "domain. Sources cited by IPI rows are interaction partners rather than "
        "phylogenetic sources, and are labelled as such.\n"
    )
    ipi_only = {
        tok
        for tok, terms in ids.items()
        if all("(IPI)" in t or "(IEA)" in t for t in terms) and tok.startswith("UniProtKB:")
    }
    for tok, rec in resolved.items():
        up = rec.get("uniprot")
        mod = rec.get("mod")
        name = None
        if up:
            name = "/".join(x for x in up["genes"] if x)
        elif mod:
            name = mod.get("symbol")
        if not name:
            continue
        low = name.lower()
        if low == "acap2":
            verdict = "ORTHOLOG of human ACAP2" if tok != f"UniProtKB:{TARGET}" else "the target itself (self-referential)"
        elif low in {"acap1", "acap3"}:
            verdict = "PARALOG (not the ACAP2 ortholog)"
        elif low == "cnt-1":
            verdict = "invertebrate ACAP family member"
        elif has_arfgap(rec) == "NO" and tok in ipi_only:
            verdict = "INTERACTION PARTNER, not a family member"
        else:
            verdict = "more distant family member (ArfGAP domain present)"
        w(f"- `{tok}` -> **{name}** - {verdict}")
    w("")

    w("## Does each source hold its own evidence for the term it donates?\n")
    w(
        "An IBA/ISS WITH/FROM list is meant to name experimentally annotated family members. "
        "For every source with a resolvable UniProt accession, this queries QuickGO for that "
        "protein's own annotations to the donated term (descendants included) and reports the "
        "evidence codes found. `EXPERIMENTAL` means at least one of "
        + ", ".join(sorted(EXPERIMENTAL))
        + ".\n"
    )
    w("| source | UniProt | donated term | source's own evidence | experimental? |")
    w("|---|---|---|---|---|")
    for tok, rec in resolved.items():
        up = rec.get("uniprot")
        accs = [up["accession"]] if up else []
        for iso in rec.get("isoforms") or []:
            if iso["accession"] not in accs:
                accs.append(iso["accession"])
        if not accs:
            continue
        for entry in sorted({t.split(" ")[0] for t in ids[tok]}):
            for acc in accs:
                ev = source_own_evidence(acc, entry)
                if not ev:
                    w(f"| `{tok}` | {acc} | {entry} | LOOKUP FAILED | ? |")
                    continue
                codes = ev["codes"]
                shown = ", ".join(f"{k}x{v}" for k, v in sorted(codes.items())) or "(none)"
                exp = "**yes**" if set(codes) & EXPERIMENTAL else "no"
                w(f"| `{tok}` | {acc} | {entry} | {shown} (n={ev['n_hits']}) | {exp} |")
    w("")

    w("## Drosophila blow (FB:FBgn0004133) in detail\n")
    blow = resolved.get("FB:FBgn0004133", {})
    if blow.get("panther"):
        w(f"- PANTHER assignment: {blow['panther']['family_id']} / {blow['panther']['sf_id']}")
    for iso in blow.get("isoforms") or []:
        w(
            f"- `{iso['accession']}` {iso['entry_name']}, {iso['length']} aa, "
            f"domains: {fmt_domains(iso)}, PANTHER xrefs in UniProt: "
            f"{', '.join(p[0] for p in iso['panther']) or 'NONE'}"
        )
    if blow.get("mod", {}).get("summary"):
        w(f"\nFlyBase summary: {blow['mod']['summary']}\n")

    if sf399:
        w("\nOther members of the same PANTHER subfamily, from the cached "
          "`interpro/panther/PTHR23180/PTHR23180-entries.csv`:\n")
        for r in sf399:
            w(f"- `{r['id']}` {r['gene']} ({r['source_tax_name']}), {r['length']} aa - {r['name']}")
        w("")

    w(f"\n## Scope of PANTHER node {PANTHER_NODE}\n")
    if scope:
        w(f"- QuickGO reports {scope['n_hits']} annotations citing this node.")
        w("- terms propagated from it: " + ", ".join(f"{k} {v}" for k, v in sorted(scope["terms"].items())))
        w(f"- gene symbols in the first page of results ({len(scope['symbols'])} distinct): "
          + ", ".join(scope["symbols"]))
    else:
        w("- UNRESOLVED (QuickGO lookup failed)")
    w("")

    text = "\n".join(out) + "\n"
    if args.stdout:
        sys.stdout.write(text)
    else:
        (HERE / "RESULTS.md").write_text(text)
        print(f"wrote {HERE / 'RESULTS.md'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
