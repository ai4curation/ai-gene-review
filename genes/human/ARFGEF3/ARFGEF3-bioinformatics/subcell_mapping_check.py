"""Are ARFGEF3's UniProt-SubCell-derived CC annotations in the right GO branch?

Three of ARFGEF3's GOA rows come from `GO_REF:0000044`, the UniProtKB-SubCell
keyword mapping. Each row's WITH/FROM names the SubCell id it came from. This
script asks, for each one:

1. what does UniProt's own SubCell vocabulary call it, and how does UniProt
   define it?
2. which GO term does UniProt's mapping send it to, and how does GO define that?
3. is the GO term the literature supports an ancestor, a descendant, or a
   **disjoint sibling** of the mapped term?

(3) is the question that matters. A mapped term that is a coarse ancestor of the
truth is imprecise but not wrong. A mapped term in a *disjoint* branch is wrong,
and no amount of propagation fixes it.

Ancestry is queried from QuickGO's closure over `is_a`/`part_of` rather than read
off the labels, because "secretory vesicle" and "transport vesicle" sound like
they ought to be related and are not.

The affected-entry count is read from the `x-total-results` HEADER, never from
the length of a page that this script chose the size of.

Run: uv run python subcell_mapping_check.py
"""

from __future__ import annotations

import csv
import json
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ARFGEF3-goa.tsv"

UA = {"User-Agent": "ai-gene-review-ARFGEF3/1.0 (https://github.com/ai4curation/ai-gene-review)",
      "Accept": "application/json"}

# The GO terms the primary literature supports for this protein's vesicular pool.
# Insulin/glucagon granules are REGULATED secretory granules (PMID:24711543,
# PMID:25737957), not vesicles of the constitutive secretory pathway.
LITERATURE_SUPPORTED = {
    "GO:0030133": "GO:0030141",  # transport vesicle      -> secretory granule
    "GO:0030658": "GO:0030667",  # transport vesicle mem.  -> secretory granule membrane
}


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.load(resp)


def subcell(sl: str) -> dict:
    return _get(f"https://rest.uniprot.org/locations/{sl}")


def go_term(gid: str) -> dict:
    u = ("https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
         f"{urllib.parse.quote(gid)}/complete")
    return _get(u)["results"][0]


def go_ancestors(gid: str) -> list[str]:
    u = ("https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
         f"{urllib.parse.quote(gid)}/ancestors?relations=is_a,part_of")
    return _get(u)["results"][0].get("ancestors", [])


def entries_with_subcell(sl: str) -> int:
    """How many UniProtKB entries carry this SubCell term.

    Read from the `x-total-results` response header. Deriving it from a page
    length would be inferring a total from a number we chose.
    """
    q = urllib.parse.quote(f"cc_scl_term:{sl}")
    url = f"https://rest.uniprot.org/uniprotkb/search?query={q}&size=1&fields=accession"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as resp:
        total = resp.headers.get("x-total-results")
    if total is None:
        raise RuntimeError(f"UniProt returned no x-total-results header for {sl}; "
                           "refusing to substitute a page length")
    return int(total)


def subcell_tokens() -> dict[str, list[str]]:
    """{SubCell id: [GO ids it was mapped to in this gene's GOA]} from the TSV."""
    if not GOA.exists():
        raise FileNotFoundError(
            f"{GOA} is missing. Regenerate it with: just fetch-gene human ARFGEF3")
    out: dict[str, list[str]] = {}
    with GOA.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            for tok in row["WITH/FROM"].split("|"):
                tok = tok.strip()
                if tok.startswith("UniProtKB-SubCell:"):
                    sl = tok.split(":", 1)[1]
                    out.setdefault(sl, []).append(row["GO TERM"])
    if not out:
        raise RuntimeError("no UniProtKB-SubCell tokens found in the GOA file")
    return out


def classify(mapped: str, supported: str) -> str:
    if mapped == supported:
        return "EXACT"
    if mapped in go_ancestors(supported):
        return "ANCESTOR (imprecise but not wrong)"
    if supported in go_ancestors(mapped):
        return "DESCENDANT (over-specific)"
    return "DISJOINT (wrong branch)"


def main() -> None:
    rows = []
    for sl, go_ids in sorted(subcell_tokens().items()):
        sc = subcell(sl)
        mappings = [g["goId"] for g in (sc.get("geneOntologies") or [])]
        for gid in sorted(set(go_ids)):
            t = go_term(gid)
            supported = LITERATURE_SUPPORTED.get(gid)
            rel = classify(gid, supported) if supported else "n/a (not contested)"
            rows.append({
                "subcell_id": sl,
                "subcell_name": sc.get("name", ""),
                "subcell_definition": " ".join((sc.get("definition") or "").split())[:300],
                "uniprot_maps_to": ";".join(mappings),
                "goa_term": gid,
                "goa_term_name": t["name"],
                "goa_term_definition": " ".join(
                    (t.get("definition", {}).get("text") or "").split())[:300],
                "literature_supported_term": supported or "",
                "literature_supported_name": go_term(supported)["name"] if supported else "",
                "relation_of_mapped_to_supported": rel,
                "uniprotkb_entries_with_this_subcell_term": entries_with_subcell(sl),
            })

    with (HERE / "subcell_mapping.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    (HERE / "subcell_mapping.json").write_text(json.dumps(rows, indent=2))

    for r in rows:
        print(f"{r['subcell_id']} {r['subcell_name']!r}")
        print(f"   UniProt maps to : {r['uniprot_maps_to']}")
        print(f"   GOA row term    : {r['goa_term']} {r['goa_term_name']}")
        if r["literature_supported_term"]:
            print(f"   literature says : {r['literature_supported_term']} "
                  f"{r['literature_supported_name']}")
            print(f"   RELATION        : {r['relation_of_mapped_to_supported']}")
        print(f"   UniProtKB entries carrying {r['subcell_id']}: "
              f"{r['uniprotkb_entries_with_this_subcell_term']}")
        print()

    wrong = [r for r in rows if r["relation_of_mapped_to_supported"].startswith("DISJOINT")]
    print(f"rows whose SubCell-derived GO term is in a DISJOINT branch: "
          f"{len(wrong)}/{len(rows)}")


if __name__ == "__main__":
    main()
