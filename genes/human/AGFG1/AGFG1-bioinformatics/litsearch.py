"""Europe PMC searches, recorded verbatim so that a negative result is reportable
as what it is: "this query returned no hits", never "no such study exists".

Usage: uv run python litsearch.py
"""

from __future__ import annotations

import json
import pathlib
import sys
import urllib.parse
import urllib.request

OUT = pathlib.Path(__file__).parent / "litsearch.json"

QUERIES = {
    # Has ArfGAP catalytic activity ever been measured on AGFG1/HRB/RIP?
    "agfg1_gap_activity": '(AGFG1 OR HRB OR "Rev-interacting protein" OR "Rev binding protein") AND ("GAP activity" OR "GTPase-activating" OR "GTPase activating" OR "ArfGAP activity")',
    "agfg1_arf": '(AGFG1 OR "HIV-1 Rev-binding protein") AND (ARF1 OR ARF6 OR "ADP-ribosylation factor")',
    "drongo_arf": 'drongo AND (Arf OR ArfGAP OR "GTPase activating")',
    # The arginine-finger question for the ArfGAP domain generally.
    "arfgap_arginine_finger": '"arginine finger" AND (ArfGAP OR "Arf GAP" OR ASAP1 OR ARFGAP1)',
    # AGFG2-specific function, for the paralogue comparison.
    "agfg2_function": 'AGFG2 AND (function OR acrosome OR spermatid OR endocytosis OR ArfGAP)',
    # Human AGFG1 acrosome / spermatogenesis evidence.
    "agfg1_human_sperm": '(AGFG1 OR HRB) AND (globozoospermia OR acrosome) AND human',
    # Is there any direct evidence that AGFG1 itself binds RNA? The GO:0003723
    # TAS row cites PMID:7634337, whose abstract describes a protein-protein
    # interaction with the Rev activation domain.
    "agfg1_rna_binding": '(AGFG1 OR hRIP OR HRB) AND ("RNA binding protein" OR "RNA-binding protein" OR "RNA interactome" OR CLIP OR "crosslinking immunoprecipitation" OR "interactome capture")',
    # Does AGFG1 bind the NXF/TAP export factors via its FG repeats?
    "agfg1_nxf": '(AGFG1 OR hRIP OR HRB OR "Rev-interacting protein") AND (NXF1 OR NXF3 OR TAP OR "FG repeat" OR nucleoporin)',
    # A control: a query that must return many hits, so a zero above is interpretable.
    "control_agfg1_any": 'AGFG1 OR "HIV-1 Rev-binding protein"',
}


def search(q: str) -> dict:
    params = urllib.parse.urlencode(
        {
            "query": q,
            "format": "json",
            "pageSize": "25",
            "resultType": "lite",
        }
    )
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{params}"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        return json.load(fh)


def main() -> None:
    out = {}
    for name, q in QUERIES.items():
        d = search(q)
        hits = d["hitCount"]
        recs = [
            {
                "id": r.get("pmid") or r.get("id"),
                "year": r.get("pubYear"),
                "journal": r.get("journalTitle"),
                "title": r.get("title"),
            }
            for r in d["resultList"]["result"]
        ]
        out[name] = {"query": q, "hitCount": hits, "top": recs}
        print(f"\n### {name}: {hits} hits")
        print(f"    query: {q}")
        for r in recs[:15]:
            print(f"    {r['id']} ({r['year']}) {r['journal']}: {r['title']}")
    ctrl = out["control_agfg1_any"]["hitCount"]
    assert ctrl > 10, (
        f"control query returned {ctrl}; a zero elsewhere would be uninterpretable"
    )
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwrote {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
