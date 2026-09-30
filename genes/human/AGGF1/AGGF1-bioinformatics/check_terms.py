"""Verify every GO term this review proposes, against QuickGO's complete record.

`just validate` passing is not proof a term is current, and OLS reports a MERGED
id and an ABSENT id identically. QuickGO's `/ontology/go/terms/<id>/complete`
returns `isObsolete` and `secondaryIds`, which distinguishes the two.

Run: uv run python check_terms.py
"""

from __future__ import annotations

from uniprot import quickgo_term

TERMS = {
    # already in GOA -- checked so the review does not restate a stale label
    "GO:0001525": "angiogenesis (IBA)",
    "GO:0001570": "vasculogenesis (TAS)",
    "GO:0001938": "positive regulation of endothelial cell proliferation (IDA)",
    "GO:0003676": "nucleic acid binding (IEA, InterPro2GO off IPR000467)",
    "GO:0005515": "protein binding (IPI x8)",
    "GO:0005576": "extracellular region (IBA/IEA/IDA)",
    "GO:0005737": "cytoplasm (IEA/IDA)",
    "GO:0007155": "cell adhesion (IDA)",
    "GO:0042802": "identical protein binding (IPI x3)",
    "GO:0045766": "positive regulation of angiogenesis (IDA)",
    "GO:0048471": "perinuclear region of cytoplasm (IDA)",
    # proposed by this review
    "GO:0003723": "RNA binding -- MODIFY target for the GO:0003676 IEA",
    "GO:0017151": "DEAD/H-box RNA helicase binding -- MODIFY target for the DHX15 IPI",
    "GO:0043120": "tumor necrosis factor binding -- MODIFY target for the TNFSF12 IPI",
    "GO:0005178": "integrin binding -- NEW (PMID:34551592)",
    "GO:0048018": "receptor ligand activity -- NEW (PMID:34551592)",
    "GO:0005634": "nucleus -- NEW",
    "GO:0042382": "paraspeckles -- NEW (PMID:35608889)",
    "GO:0000381": "regulation of alternative mRNA splicing, via spliceosome -- NEW",
    "GO:0043484": "regulation of RNA splicing -- parent, for reference",
    "GO:0035591": "signaling adaptor activity -- considered and NOT proposed",
    "GO:0050699": "WW domain binding -- control, expected absent",
}


def main() -> None:
    bad = []
    for go_id, why in TERMS.items():
        t = quickgo_term(go_id)
        obs = t.get("isObsolete", False)
        sec = t.get("secondaryIds") or []
        flag = "OBSOLETE" if obs else "ok"
        if obs:
            bad.append(go_id)
        print(f"{go_id}  {flag:9s} {t['name']}")
        print(f"      aspect={t.get('aspect')}  secondaryIds={sec or 'none'}")
        print(f"      use: {why}")
        if t.get("replacements"):
            print(f"      replacements: {t['replacements']}")
    print()
    print(f"{len(TERMS)} terms checked; obsolete: {bad or 'none'}")
    if bad:
        raise SystemExit(f"obsolete term(s) in the proposal set: {bad}")


if __name__ == "__main__":
    main()
