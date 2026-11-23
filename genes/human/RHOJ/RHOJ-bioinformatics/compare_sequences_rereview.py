# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Independent re-review analysis of G3V4H1 versus canonical RHOJ (Q9H4E5).

Fetches both sequences from the UniProt REST API, the Ensembl transcript
record behind G3V4H1, and the canonical RHOJ cDNA, then reports:

* the shared N-terminal prefix and the divergence point;
* presence of the Rho-family G1-G5 motifs and the C-terminal CAAX box;
* whether the divergent G3V4H1 tail is encoded by canonical RHOJ exon
  sequence read in a different frame (frameshift) or by other sequence;
* the Ensembl biotype of the transcript that encodes G3V4H1.

Run: uv run --script compare_sequences_rereview.py > RESULTS-rereview.txt
"""

import json
import re
import urllib.request

UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.fasta"
ENSEMBL = "https://rest.ensembl.org"

CODON = {}
_bases = "TCAG"
_aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
_i = 0
for a in _bases:
    for b in _bases:
        for c in _bases:
            CODON[a + b + c] = _aa[_i]
            _i += 1


def get(url: str, accept: str = "text/plain") -> str:
    req = urllib.request.Request(url, headers={"Accept": accept})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def fasta_seq(acc: str) -> str:
    return "".join(get(UNIPROT.format(acc)).splitlines()[1:])


def translate(nt: str) -> str:
    return "".join(CODON.get(nt[i : i + 3], "X") for i in range(0, len(nt) - 2, 3))


def main() -> None:
    target = fasta_seq("G3V4H1")
    canon = fasta_seq("Q9H4E5")
    print(f"G3V4H1 length: {len(target)}")
    print(f"Q9H4E5 length: {len(canon)}")
    n = 0
    while n < min(len(target), len(canon)) and target[n] == canon[n]:
        n += 1
    print(f"Identical N-terminal prefix: residues 1-{n}")
    print(f"G3V4H1 divergent tail ({n + 1}-{len(target)}): {target[n:]}")
    print(f"Q9H4E5 region replaced ({n + 1}-{len(canon)}): {canon[n:]}")

    motifs = {
        "G1 P-loop GxxxxGK(S/T)": r"G....GK[ST]",
        "G2 switch I (T35-equivalent) PTVFD": r"PTVFD",
        "G3 DTAGQE": r"DTAGQ",
        "G4 (T/N)(K/Q)xD": r"[TN][KQ].D",
        "G5 (C/S)SA(L/K)": r"[CS]SA[LK]",
        "CAAX box (C-terminal)": r"C[A-Z]{3}$",
    }
    print("\nMotif presence (regex, first match position, 1-based):")
    for name, pat in motifs.items():
        for label, seq in (("Q9H4E5", canon), ("G3V4H1", target)):
            # restrict G4 search to after switch II to avoid spurious hits
            start = 100 if name.startswith("G4") else 0
            m = re.search(pat, seq[start:])
            pos = (m.start() + 1 + start) if m else None
            print(f"  {name:40s} {label}: {'absent' if pos is None else f'{pos} {m.group()}'}")

    # Ensembl transcript behind G3V4H1
    tx = json.loads(
        get(f"{ENSEMBL}/lookup/id/ENST00000557447?expand=1", "application/json")
    )
    print(
        f"\nENST00000557447 ({tx.get('display_name')}): biotype={tx.get('biotype')}, "
        f"canonical={tx.get('is_canonical')}, exons={len(tx.get('Exon', []))}"
    )
    ctx = json.loads(
        get(f"{ENSEMBL}/lookup/id/ENST00000316754?expand=1", "application/json")
    )
    print(
        f"ENST00000316754 ({ctx.get('display_name')}): biotype={ctx.get('biotype')}, "
        f"canonical={ctx.get('is_canonical')}, exons={len(ctx.get('Exon', []))}"
    )

    # Is the divergent tail a frameshifted read of canonical RHOJ coding sequence?
    cds = "".join(
        get(f"{ENSEMBL}/sequence/id/ENST00000316754?type=cds", "text/plain").split()
    )
    print(f"\nCanonical CDS length: {len(cds)} nt; translates to canonical: "
          f"{translate(cds).rstrip('*') == canon}")
    tail = target[n:]
    probe = tail[:8]
    found = False
    for frame in range(3):
        prot = translate(cds[frame:])
        idx = prot.find(probe)
        if idx >= 0:
            found = True
            print(f"Tail probe {probe} found in canonical CDS frame +{frame} at codon {idx + 1}")
    if not found:
        print(f"Tail probe {probe} not found in any frame of the canonical CDS")
    tcds = "".join(
        get(f"{ENSEMBL}/sequence/id/ENST00000557447?type=cds", "text/plain").split()
    )
    print(f"ENST00000557447 CDS translates to G3V4H1: {translate(tcds).rstrip('*') == target}")
    # where does the G3V4H1 CDS diverge from canonical CDS at nucleotide level?
    k = 0
    while k < min(len(tcds), len(cds)) and tcds[k] == cds[k]:
        k += 1
    print(f"Nucleotide identity of CDSs up to nt {k} (codon {k // 3 + 1})")
    rest = tcds[k:]
    for frame in range(3):
        hit = cds.find(rest[frame : frame + 30])
        if hit >= 0:
            print(
                f"Downstream G3V4H1 CDS (offset {frame}) resumes canonical CDS at nt {hit + 1}; "
                f"canonical frame there = {hit % 3} vs G3V4H1 frame {(k + frame) % 3}"
            )
            break
    else:
        print("Downstream G3V4H1 CDS does not resume canonical CDS within 30-nt probes")

    # Where is the divergent G3V4H1 coding sequence in the canonical transcript structure?
    def exons(t: dict) -> list[tuple[int, int]]:
        return sorted((e["start"], e["end"]) for e in t["Exon"])

    print("\nExon coordinates (GRCh38, gene on strand %s):" % tx.get("strand"))
    print("  RHOJ-201 canonical:", exons(ctx))
    print("  RHOJ-204 (G3V4H1):", exons(tx))
    print(
        f"  Translation bounds RHOJ-201: {ctx['Translation']['start']}-{ctx['Translation']['end']}; "
        f"RHOJ-204: {tx['Translation']['start']}-{tx['Translation']['end']}"
    )
    if tx["Translation"]["end"] > ctx["Translation"]["end"]:
        print("  RHOJ-204 stop codon lies 3' of the canonical stop codon (tail read from canonical 3' UTR)")
    shared = set(exons(ctx)) & set(exons(tx))
    print(f"  Exons shared exactly: {len(shared)}")
    only = sorted(set(exons(tx)) - set(exons(ctx)))
    for s_, e_ in only:
        overl = [c for c in exons(ctx) if c[0] <= e_ and s_ <= c[1]]
        print(f"  RHOJ-204-specific exon {s_}-{e_} ({e_ - s_ + 1} nt); overlaps canonical exons: {overl}")


if __name__ == "__main__":
    main()
