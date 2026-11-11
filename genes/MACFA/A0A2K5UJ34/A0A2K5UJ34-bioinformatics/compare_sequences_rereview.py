"""Compare macaque A0A2K5UJ34 with human TTC39C (Q8N584) and zebrafish ttc39c (Q1LXE6).

Fetches FASTA from the UniProt REST API, locates the macaque sequence as a
contiguous segment of the human canonical sequence, and lists substitutions.
Run: python3 compare_sequences_rereview.py
"""
import urllib.request


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    return "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))


def main() -> None:
    mac = fetch("A0A2K5UJ34")
    hum = fetch("Q8N584")
    zf = fetch("Q1LXE6")
    print(f"A0A2K5UJ34 (macaque) length: {len(mac)}")
    print(f"Q8N584 (human TTC39C) length: {len(hum)}")
    print(f"Q1LXE6 (zebrafish ttc39c) length: {len(zf)}")
    start = hum.find(mac[:30])
    if start < 0:
        print("Macaque N-terminal 30 aa not found in human sequence")
        return
    print(f"Macaque residue 1 aligns to human residue {start + 1} ({hum[start]})")
    print(f"Human residues absent from macaque model: 1-{start} = {hum[:start]}")
    seg = hum[start:start + len(mac)]
    subs = [(i + 1, start + i + 1, seg[i], mac[i]) for i in range(min(len(seg), len(mac))) if seg[i] != mac[i]]
    ident = 1 - len(subs) / len(mac)
    print(f"Ungapped identity over aligned segment: {ident:.4f} ({len(subs)} substitutions)")
    for mpos, hpos, h, m in subs:
        print(f"  macaque {mpos} / human {hpos}: {h} -> {m}")
    print(f"Aligned segment reaches human C-terminus: {start + len(mac) == len(hum)}")


if __name__ == "__main__":
    main()
