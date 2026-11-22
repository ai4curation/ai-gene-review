"""Check the G6PD catalytic-site motif in PTHR23429 members cited by node assessments.

Run from this directory:  python3 motif_check.py
Writes PTHR23429-motif-check.txt. For each accession it fetches the current UniProt
entry and reports (a) whether the sequence matches the PROSITE PS00069 G6PD
active-site pattern D-H-Y-L-G-K-[EQ], (b) whether it contains the shorter
catalytic-histidine core IDHY, and (c) whether UniProt lists the InterPro
active-site signature IPR019796 (G6P_DH_AS). Human G6PD (P11413) is the positive
control. Nothing about the result is hard-coded.
"""
import json
import re
import urllib.request

ACCESSIONS = {
    "P11413": "human G6PD (positive control)",
    "Q9VNW4": "Drosophila CG7140 (PTN000604499)",
    "Q93ZW0": "Arabidopsis G6PD4 (PTN001159959)",
    "O59812": "S. pombe gcd1 (PTN008599524)",
    "O14137": "S. pombe SPAC3C7.13c (PTN008599526)",
}
PS00069 = re.compile(r"DHYLGK[EQ]")
CORE = "IDHY"


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def main():
    lines = ["accession\tdescription\tsequence_version\tPS00069_match\tIDHY_core\tIPR019796_listed"]
    for acc, desc in ACCESSIONS.items():
        entry = fetch(acc)
        seq = entry["sequence"]["value"]
        version = entry.get("entryAudit", {}).get("sequenceVersion")
        m = PS00069.search(seq)
        ps = f"{m.group(0)}@{m.start() + 1}" if m else "none"
        core = seq.find(CORE)
        core_txt = f"{CORE}@{core + 1}" if core >= 0 else "none"
        ipr = any(
            x.get("database") == "InterPro" and x.get("id") == "IPR019796"
            for x in entry.get("uniProtKBCrossReferences", [])
        )
        lines.append(f"{acc}\t{desc}\t{version}\t{ps}\t{core_txt}\t{'yes' if ipr else 'no'}")
    with open("PTHR23429-motif-check.txt", "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
