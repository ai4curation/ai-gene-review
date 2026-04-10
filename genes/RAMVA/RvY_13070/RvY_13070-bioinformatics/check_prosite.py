"""Check PROSITE signature matches for SOD paralogs via InterPro REST API.

PROSITE patterns for Cu/Zn SOD:
- PS00087 (SOD_CU_ZN_1): C-terminal signature near H120 Cu ligand
  G-[GNHD]-[SGA]-[GR]-x-R-x(7,9)-[LIVAT]-x-G
- PS00332 (SOD_CU_ZN_2): N-terminal signature with H-x-H motif (H46-H48)
  [GA]-[IMFAT]-H-[LIVF]-H-x(2)-[GP]-[SDG]-x-[STAGDE]

Both are part of InterPro IPR018152 (Cu/Zn SOD binding site).

A protein that matches IPR001424 (SOD Cu/Zn domain by Pfam/CDD) but FAILS
PS00332 specifically is a strong pseudoenzyme candidate because PS00332
requires the catalytic H-x-H motif.
"""
import json
import urllib.request
import time

# Map ORF -> UniProt accession
PARALOGS = {
    "RvY_13070": "A0A1D1VU85",  # RvSOD15 - confirmed pseudoenzyme
    "RvY_00650": "A0A1D1UDY8",
    "RvY_00651": "A0A1D1UKR0",
    "RvY_01767": "A0A1D1USM4",
    "RvY_03754": "A0A1D1UP68",
    "RvY_03757": "A0A1D1UP59",
    "RvY_09480": "A0A1D1VEY6",
    "RvY_10893": "A0A1D1VE88",
    "RvY_17310": "A0A1D1W3Y1",
    "RvY_15948": "A0A1D1VWP9",  # copper chaperone
}


def fetch_interpro(accession: str) -> dict:
    """Fetch InterPro entries for a UniProt accession."""
    url = f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/UniProt/{accession}/?format=json&page_size=100"
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode())


def fetch_prosite_details(accession: str) -> list[dict]:
    """Fetch PROSITE matches specifically (member database)."""
    url = f"https://www.ebi.ac.uk/interpro/api/entry/prosite/protein/UniProt/{accession}/?format=json&page_size=100"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode())
    return data.get("results", [])


def main():
    print(f"{'Gene':<12} {'Pfam SODC':<12} {'PS00087':<25} {'PS00332':<25} {'Verdict'}")
    print("=" * 110)

    for gene, acc in PARALOGS.items():
        pfam_match = False
        ps00087 = "MISSING"
        ps00332 = "MISSING"

        # Check PROSITE specifically
        try:
            prosite_results = fetch_prosite_details(acc)
            for entry in prosite_results:
                meta = entry.get("metadata", {})
                accession_db = meta.get("accession", "")
                if accession_db == "PS00087":
                    locs = entry.get("proteins", [{}])[0].get("entry_protein_locations", [])
                    if locs:
                        frag = locs[0]["fragments"][0]
                        ps00087 = f"MATCH {frag['start']}-{frag['end']}"
                elif accession_db == "PS00332":
                    locs = entry.get("proteins", [{}])[0].get("entry_protein_locations", [])
                    if locs:
                        frag = locs[0]["fragments"][0]
                        ps00332 = f"MATCH {frag['start']}-{frag['end']}"
        except Exception as e:
            print(f"  ERROR fetching PROSITE for {gene} ({acc}): {e}")
            continue

        # Check Pfam SODC family - use all entries query
        try:
            url = f"https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/UniProt/{acc}/?format=json&page_size=100"
            with urllib.request.urlopen(url) as resp:
                data = json.loads(resp.read().decode())
                for r in data.get("results", []):
                    if r.get("metadata", {}).get("accession") == "PF00080":
                        pfam_match = True
                        break
        except Exception as e:
            pfam_match = False

        # Verdict: matches Pfam but NOT PS00332 -> pseudoenzyme candidate
        if pfam_match and ps00332 == "MISSING":
            verdict = "*** PSEUDOENZYME (no PS00332) ***"
        elif pfam_match and ps00087 == "MISSING":
            verdict = "PARTIAL (no PS00087)"
        elif pfam_match and ps00087 != "MISSING" and ps00332 != "MISSING":
            verdict = "Both PROSITE patterns OK"
        elif not pfam_match:
            verdict = "Not in Pfam SODC"
        else:
            verdict = "Unknown"

        pfam_str = "YES" if pfam_match else "NO"
        print(f"{gene:<12} {pfam_str:<12} {ps00087:<25} {ps00332:<25} {verdict}")
        time.sleep(0.5)  # be polite


if __name__ == "__main__":
    main()
