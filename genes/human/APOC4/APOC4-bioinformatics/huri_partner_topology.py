#!/usr/bin/env python3
"""Are APOC4's 23 HuRI two-hybrid partners in a compartment APOC4 can reach?

All 23 GO:0005515 rows on human APOC4 come from one reference, PMID:32296183
(HuRI), a systematic yeast two-hybrid screen. The review marks every one of them
MARK_AS_OVER_ANNOTATED, and the argument rests on where the partners live. This
script derives that topology table live from UniProt so the counts cited in the
review and in APOC4-notes.md are reproducible rather than asserted.

The relevant asymmetry is not simply "intracellular": APOC4's mature chain does
transit the ER and Golgi *lumen* on its way out of the cell. What it never does is
face the cytosol, the mitochondrial matrix, or the nucleus - and a Gal4 two-hybrid
tests exactly the last of those. So the script reports both the coarse count
(secreted / mitochondrial / transmembrane) and each partner's verbatim location
string, and leaves the per-partner argument to the review.

Run: uv run python huri_partner_topology.py
"""
import json
import re
import sys
import urllib.request

# The WITH/FROM entities of APOC4's 23 GO:0005515 rows, exactly as GOA records them.
PARTNER_IDS = [
    "UniProtKB:P07204", "UniProtKB:P40305-1", "UniProtKB:Q05329", "UniProtKB:Q17RD7",
    "UniProtKB:Q5SQN1", "UniProtKB:Q5TGZ0", "UniProtKB:Q5XKP0", "UniProtKB:Q6P1Q0",
    "UniProtKB:Q6ZUI0", "UniProtKB:Q8WWC4", "UniProtKB:Q8WXG1", "UniProtKB:Q92843",
    "UniProtKB:Q96BZ9", "UniProtKB:Q96QA5", "UniProtKB:Q9BQE5", "UniProtKB:Q9H237-2",
    "UniProtKB:Q9HC62", "UniProtKB:Q9NPL8", "UniProtKB:Q9NR28", "UniProtKB:Q9NUH8",
    "UniProtKB:Q9UHD9", "UniProtKB:Q9UMS0", "UniProtKB:Q9UMX0",
]
TARGET = "P55056"

SECRETED = re.compile(r"Secreted|Extracellular", re.I)
MITO = re.compile(r"Mitochondri", re.I)


def fetch(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    d = json.loads(urllib.request.urlopen(url, timeout=60).read())
    assert "sequence" in d, (
        f"{acc} is not an active UniProt entry ({d.get('entryType')}, "
        f"{d.get('inactiveReason')})"
    )
    locs: list[str] = []
    for c in d.get("comments", []):
        if c["commentType"] == "SUBCELLULAR LOCATION":
            for s in c.get("subcellularLocations", []):
                v = s.get("location", {}).get("value")
                if v and v not in locs:
                    locs.append(v)
    return {
        "accession": d["primaryAccession"],
        "id": d["uniProtkbId"],
        "symbol": d["genes"][0]["geneName"]["value"] if d.get("genes") else "",
        "name": d["proteinDescription"]["recommendedName"]["fullName"]["value"],
        "locations": locs,
        "transmembrane": any(f["type"] == "Transmembrane" for f in d.get("features", [])),
        "signal_peptide": any(f["type"] == "Signal" for f in d.get("features", [])),
    }


def main() -> int:
    target = fetch(TARGET)
    assert target["id"] == "APOC4_HUMAN", f"target resolved to {target['id']}"
    assert target["signal_peptide"], "APOC4 should carry a cleaved signal peptide"
    assert any(SECRETED.search(l) for l in target["locations"]), (
        "APOC4 should be curated Secreted"
    )
    print(f"target {target['id']} ({target['accession']}): "
          f"locations={target['locations']}, signal_peptide={target['signal_peptide']}")
    print(f"  -> the mature chain is lumenal/extracellular; it never faces the cytosol, "
          f"the mitochondrial matrix or the nucleus.\n")

    rows = []
    for pid in PARTNER_IDS:
        acc = pid.split(":", 1)[1].split("-")[0]
        r = fetch(acc)
        r["goa_id"] = pid
        r["secreted"] = any(SECRETED.search(l) for l in r["locations"])
        r["mitochondrial"] = any(MITO.search(l) for l in r["locations"])
        rows.append(r)

    assert len(rows) == 23, f"expected 23 partners, resolved {len(rows)}"

    hdr = f"{'GOA id':22} {'sym':9} {'sec':4} {'mito':5} {'TM':3} {'sig':4} locations"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['goa_id']:22} {r['symbol']:9} "
              f"{'YES' if r['secreted'] else '-':4} "
              f"{'YES' if r['mitochondrial'] else '-':5} "
              f"{'TM' if r['transmembrane'] else '-':3} "
              f"{'SIG' if r['signal_peptide'] else '-':4} "
              f"{'; '.join(r['locations']) or 'no curated subcellular location'}")

    n_sec = sum(1 for r in rows if r["secreted"])
    n_mito = sum(1 for r in rows if r["mitochondrial"])
    n_tm = sum(1 for r in rows if r["transmembrane"])
    sig = [r["symbol"] for r in rows if r["signal_peptide"]]
    noloc = [r["symbol"] for r in rows if not r["locations"]]
    print(f"\npartners resolved: {len(rows)}")
    print(f"  with a curated Secreted/Extracellular location: {n_sec}")
    print(f"  with a curated mitochondrial location:          {n_mito}")
    print(f"  with a transmembrane segment:                   {n_tm}")
    print(f"  with a cleaved signal peptide:                  {len(sig)} {sig}")
    print(f"  with no curated subcellular location:           {len(noloc)} {noloc}")

    with open("huri_partners.tsv", "w") as fh:
        fh.write("goa_id\taccession\tuniprot_id\tsymbol\tprotein_name\tsecreted\t"
                 "mitochondrial\ttransmembrane\tsignal_peptide\tlocations\n")
        for r in rows:
            fh.write(f"{r['goa_id']}\t{r['accession']}\t{r['id']}\t{r['symbol']}\t"
                     f"{r['name']}\t{r['secreted']}\t{r['mitochondrial']}\t"
                     f"{r['transmembrane']}\t{r['signal_peptide']}\t"
                     f"{'; '.join(r['locations'])}\n")
    with open("huri_partner_topology_result.json", "w") as fh:
        json.dump({"target": target, "n_partners": len(rows),
                   "n_secreted": n_sec, "n_mitochondrial": n_mito,
                   "n_transmembrane": n_tm, "with_signal_peptide": sig,
                   "no_curated_location": noloc, "partners": rows}, fh, indent=2)
    print("\nwrote huri_partners.tsv and huri_partner_topology_result.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
