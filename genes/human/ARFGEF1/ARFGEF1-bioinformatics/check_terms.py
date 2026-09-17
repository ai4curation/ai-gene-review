"""Check the status and shape of every GO term this review argues about.

For each term of interest print QuickGO's `complete` record: name, aspect,
`isObsolete`, `replacements`/`secondaryIds` (which distinguish a MERGED id from
an absent one -- OLS reports both identically), definition, and the direct
`is_a` children. A failed keyword search is NOT evidence a term is absent, so
term-availability claims are made by walking parents/children here rather than
by searching text.

Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/check_terms.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from uniprot import _cached_get, quickgo_term  # noqa: E402

HERE = Path(__file__).parent

# Terms the ARFGEF1 review reasons about, plus the candidate replacements.
TERMS = [
    "GO:0005085",  # guanyl-nucleotide exchange factor activity (IBA + IDA + IEA on ARFGEF1)
    "GO:0005086",  # ARF guanyl-nucleotide exchange factor activity -- candidate MODIFY target
    "GO:0005096",  # GTPase activator activity (carries a NOT on ARFGEF1)
    "GO:0034260",  # negative regulation of GTPase activity (IDA on ARFGEF1)
    "GO:0043547",  # positive regulation of GTPase activity
    "GO:0030532",  # small nuclear ribonucleoprotein complex (IDA on ARFGEF1)
    "GO:0005732",  # sno(s)RNA-containing ribonucleoprotein complex -- candidate MODIFY target
    "GO:0031428",  # box C/D methylation guide snoRNP complex
    "GO:0032012",  # regulation of ARF protein signal transduction
    "GO:0016192",  # vesicle-mediated transport
    "GO:0042147",  # retrograde transport, endosome to Golgi
    "GO:0034237",  # protein kinase A regulatory subunit binding
    "GO:0017022",  # myosin binding
    "GO:0090303",  # positive regulation of wound healing
    "GO:0030837",  # negative regulation of actin filament polymerization
    "GO:0009101",  # glycoprotein biosynthetic process
    "GO:0007030",  # Golgi organization
    "GO:0010256",  # endomembrane system organization
    "GO:0006887",  # exocytosis
    "GO:2000114",  # regulation of establishment of cell polarity
    "GO:0031175",  # neuron projection development
    "GO:0051897",  # positive regulation of PI3K/AKT signal transduction
    "GO:0043001",  # Golgi to plasma membrane protein transport
    "GO:0032483",  # regulation of Rab protein signal transduction
    "GO:1902017",  # regulation of cilium assembly (control: unrelated, exercises the absent path)
    # --- candidate NEW / MODIFY targets ---------------------------------
    "GO:0042802",  # identical protein binding (BIG1 homodimer)
    "GO:0019894",  # kinesin binding (KIF21A)
    "GO:0031267",  # small GTPase binding (ARL1)
    "GO:0032014",  # positive regulation of ARF protein signal transduction
    "GO:0032588",  # trans-Golgi network membrane
    "GO:0030674",  # protein-macromolecule adaptor activity
    "GO:0006893",  # Golgi to plasma membrane transport
    "GO:0032266",  # phosphatidylinositol-3-phosphate binding (screen hit, NOT imported)
    "GO:0051018",  # protein kinase A binding
    "GO:0034260",  # (repeat; harmless)
]

CHILD_PARENTS = [
    "GO:0005085",  # what children does the generic GEF term actually have?
    "GO:0030529",  # ribonucleoprotein complex
    "GO:0005096",
]


def children_of(go_id: str) -> list[dict[str, str]]:
    """Direct is_a/part_of children, read from QuickGO's children endpoint."""
    body = _cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/children",
        f"gochild_{go_id.replace(':', '_')}",
    )
    res = json.loads(body)["results"][0]
    return res.get("children", []) or []


def main() -> None:
    out = {}
    for t in TERMS:
        rec = quickgo_term(t)
        out[t] = {
            "name": rec.get("name"),
            "aspect": rec.get("aspect"),
            "isObsolete": rec.get("isObsolete"),
            "replacements": rec.get("replacements"),
            "secondaryIds": rec.get("secondaryIds"),
            "definition": (rec.get("definition") or {}).get("text"),
            "comment": rec.get("comment"),
        }
        print(f"{t}\t{rec.get('name')}\taspect={rec.get('aspect')}\t"
              f"obsolete={rec.get('isObsolete')}\treplacements={rec.get('replacements')}\t"
              f"secondaryIds={rec.get('secondaryIds')}")
    print()
    kids = {}
    for p in CHILD_PARENTS:
        cs = children_of(p)
        kids[p] = [{"id": c["id"], "relation": c.get("relation")} for c in cs]
        print(f"children of {p} ({quickgo_term(p).get('name')}): {len(cs)}")
        for c in cs:
            print(f"    {c['id']}\t{c.get('relation')}\t{quickgo_term(c['id']).get('name')}")
    (HERE / "term_status.json").write_text(
        json.dumps({"terms": out, "children": kids}, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
