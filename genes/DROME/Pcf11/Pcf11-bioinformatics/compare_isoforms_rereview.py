"""Compare the 86-aa Pcf11 product C0P8M6 with other D. melanogaster Pcf11 UniProt entries.

Fetches sequences live from UniProt REST and reports the shared N-terminal prefix
and the CID domain boundaries reported by UniProt (PROSITE PS51391).
Run: python3 compare_isoforms_rereview.py
"""
import json
import urllib.request

ACCS = ["C0P8M6", "E1JH69", "Q8IGR2", "A1Z9W4"]


def fetch(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    with urllib.request.urlopen(url) as fh:
        return json.load(fh)


def shared_prefix(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def main() -> None:
    recs = {a: fetch(a) for a in ACCS}
    query = recs["C0P8M6"]["sequence"]["value"]
    for acc, rec in recs.items():
        seq = rec["sequence"]["value"]
        cid = [
            (f["location"]["start"]["value"], f["location"]["end"]["value"])
            for f in rec.get("features", [])
            if f["type"] == "Domain" and f.get("description") == "CID"
        ]
        print(
            f"{acc}\tlength={len(seq)}\tshared_prefix_with_C0P8M6={shared_prefix(query, seq)}"
            f"\tidentical_to_C0P8M6={seq == query}\tCID={cid}"
        )


if __name__ == "__main__":
    main()
