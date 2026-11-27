# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Map the 74-aa A0A061AL94 (Y39G10AR.14b) product onto canonical MCM-4 (Q95XQ8, Y39G10AR.14a).

Fetches both sequences and the canonical feature table from UniProt REST, and the
mcm-4 gene models from Ensembl REST, then reports where the fragment lies in the
canonical protein and which canonical features it retains or lacks.

Run: uv run compare_to_canonical.py
"""
import json
import urllib.request

FRAG = "A0A061AL94"
CANON = "Q95XQ8"
GENE = "WBGene00003156"


def get(url: str, accept: str = "application/json") -> str:
    req = urllib.request.Request(url, headers={"Accept": accept, "Content-Type": accept})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def fasta_seq(acc: str) -> str:
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", "text/plain")
    return "".join(line.strip() for line in txt.splitlines() if not line.startswith(">"))


def main() -> None:
    frag = fasta_seq(FRAG)
    canon = fasta_seq(CANON)
    print(f"{FRAG} length: {len(frag)}")
    print(f"{CANON} length: {len(canon)}")
    pos = canon.find(frag)
    if pos < 0:
        print("Fragment is NOT an exact substring of the canonical sequence")
        return
    start, end = pos + 1, pos + len(frag)
    print(f"Fragment = canonical residues {start}-{end} (exact identity, 100%)")
    print(f"Fragment covers {len(frag) / len(canon):.1%} of canonical length")

    entry = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{CANON}.json"))
    print("\nCanonical features vs fragment span:")
    for f in entry.get("features", []):
        loc = f["location"]
        s, e = loc["start"]["value"], loc["end"]["value"]
        desc = f.get("description") or f.get("ligand", {}).get("name", "")
        inside = s >= start and e <= end
        overlap = not (e < start or s > end)
        status = "RETAINED" if inside else ("PARTIAL" if overlap else "ABSENT")
        print(f"  {f['type']:<20} {s}-{e:<5} {desc:<40} {status}")

    gene = json.loads(get(f"https://rest.ensembl.org/lookup/id/{GENE}?expand=1;species=caenorhabditis_elegans"))
    print(f"\nEnsembl gene models for {gene.get('display_name')} ({gene['start']}-{gene['end']}, strand {gene['strand']}):")
    for t in gene.get("Transcript", []):
        tr = t.get("Translation") or {}
        print(f"  {t['id']}: {t['start']}-{t['end']}, {len(t.get('Exon', []))} exon(s), protein {tr.get('length')} aa")


if __name__ == "__main__":
    main()
