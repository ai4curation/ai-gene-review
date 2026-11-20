"""Query the OLS4 GO API for the is_a/part_of ancestry of the Cbc transport terms.

Checks whether the carnitine / quaternary-ammonium transport terms used in the
Cbc and CaiX reviews sit under GO:0005275 (amine transmembrane transporter
activity) or GO:0015837 (amine transport), and prints both definitions.
Writes nothing but stdout; RESULTS.md is produced by redirecting it.

Usage: python go_placement.py > RESULTS.md
"""

import json
import urllib.parse
import urllib.request
from datetime import date

OLS = "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/"
QUERY_TERMS = ["GO:0015226", "GO:0015879", "GO:1902603", "GO:0015418",
               "GO:0015651", "GO:0015697", "GO:0015220", "GO:0015871",
               "GO:0031460", "GO:0015199"]
AMINE_TERMS = ["GO:0005275", "GO:0015837"]


def _iri(curie: str) -> str:
    """Return the double-encoded OBO IRI OLS expects for a GO CURIE."""
    iri = "http://purl.obolibrary.org/obo/" + curie.replace(":", "_")
    return urllib.parse.quote(urllib.parse.quote(iri, safe=""), safe="")


def _get(url: str) -> dict:
    """GET a JSON document from OLS."""
    with urllib.request.urlopen(url, timeout=60) as fh:
        return json.load(fh)


def term(curie: str) -> dict:
    """Return the OLS term record (label, definition, obsolete flag)."""
    return _get(OLS + _iri(curie))


def ancestors(curie: str) -> list[tuple[str, str]]:
    """Return (id, label) of every hierarchical ancestor (is_a and part_of)."""
    data = _get(OLS + _iri(curie) + "/hierarchicalAncestors?size=500")
    return sorted((t["obo_id"], t["label"])
                  for t in data.get("_embedded", {}).get("terms", [])
                  if (t.get("obo_id") or "").startswith("GO:"))


def main() -> None:
    """Print the placement report as Markdown."""
    print("# GO placement of Cbc transport terms (OLS4 query)\n")
    print(f"Generated {date.today().isoformat()} by `go_placement.py` against {OLS}"
          " (hierarchicalAncestors = is_a + part_of closure).\n")
    print("## Amine terms\n")
    for c in AMINE_TERMS:
        t = term(c)
        print(f"- {c} {t['label']}: definition: \"{(t.get('description') or [''])[0]}\"")
    print("\n## Ancestry check\n")
    print("| term | label | under GO:0005275? | under GO:0015837? | under GO:0015697 or GO:0015651? |")
    print("|---|---|---|---|---|")
    for c in QUERY_TERMS:
        anc = {i for i, _ in ancestors(c)}
        lab = term(c)["label"]
        qac = "yes" if anc & {"GO:0015697", "GO:0015651"} else "no"
        print(f"| {c} | {lab} | {'yes' if 'GO:0005275' in anc else 'no'} "
              f"| {'yes' if 'GO:0015837' in anc else 'no'} | {qac} |")
    print("\n## Full ancestor lists\n")
    for c in QUERY_TERMS:
        print(f"- {c}: " + "; ".join(f"{i} {lab}" for i, lab in ancestors(c)))


if __name__ == "__main__":
    main()
