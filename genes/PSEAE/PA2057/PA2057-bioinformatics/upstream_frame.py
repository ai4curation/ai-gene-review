"""Check whether the PAO1 genome upstream of the annotated PA2057 start
(NC_002516.2:2251275..2253815, + strand) continues the PA2057 reading frame,
and compare the in-frame translation with the 985-aa P. aeruginosa UniParc
variant UPI000EB53B2E from the same UniRef90 cluster.

Usage: python upstream_frame.py
Network access to NCBI E-utilities and UniProt REST is required.
"""
import urllib.request

START = 2251275  # annotated PA2057 start (1-based, + strand)
UP = 600

CODON = {}
bases = "TCAG"
aas = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
i = 0
for a in bases:
    for b in bases:
        for c in bases:
            CODON[a + b + c] = aas[i]
            i += 1


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def main():
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_002516.2"
           f"&seq_start={START - UP}&seq_stop={START + 59}&rettype=fasta&retmode=text")
    nt = "".join(fetch(url).split("\n")[1:]).upper()
    prot = "".join(CODON.get(nt[j:j + 3], "X") for j in range(0, len(nt) - 2, 3))
    print("in-frame translation of", UP, "nt upstream + first 20 codons:")
    print(prot)
    annotated = prot[UP // 3:]
    print("annotated start region:", annotated)
    upstream = prot[:UP // 3]
    last_stop = upstream.rfind("*")
    open_up = upstream[last_stop + 1:]
    print(f"open upstream extension (no stop) length: {len(open_up)} codons")
    print("open upstream extension:", open_up)
    up = "".join(fetch("https://rest.uniprot.org/uniparc/UPI000EB53B2E.fasta").split("\n")[1:])
    k = up.find(annotated[:12])
    print("UPI000EB53B2E offset of annotated start motif:", k)
    if k > 0:
        long_n = up[:k]
        print("UPI000EB53B2E N-terminal extension:", long_n)
        tail = open_up[-len(long_n):] if len(open_up) >= len(long_n) else open_up
        same = sum(1 for x, y in zip(reversed(tail), reversed(long_n)) if x == y)
        print(f"identity of genomic extension to variant over last {len(tail)} residues: {same}/{len(tail)}")


if __name__ == "__main__":
    main()
