"""Compare SKIP (FBgn0051163) UniProt products against A0A0B4K6C1.

Fetches all UniProtKB entries cross-referenced to FlyBase FBgn0051163 and, for
each, reports the length of the shared N-terminal prefix with A0A0B4K6C1, the
C-terminal residues of each product, and whether each product's last 8 residues
occur anywhere in A0A0B4K6C1. Diao et al. 2009 (PMID:19463952) mapped Shal binding
to the 8 C-terminal residues unique to the short isoform SKIP3.
Usage: python compare_isoforms.py
"""
import urllib.request

URL = ("https://rest.uniprot.org/uniprotkb/search?query=xref:flybase-FBgn0051163"
       "&fields=accession,length,sequence,xref_refseq&format=tsv")
REF = "A0A0B4K6C1"


def main():
    rows = urllib.request.urlopen(URL, timeout=60).read().decode().strip().split("\n")[1:]
    seqs = {}
    refseq = {}
    for r in rows:
        acc, length, seq, rs = (r.split("\t") + [""] * 4)[:4]
        seqs[acc] = seq
        refseq[acc] = rs
    ref = seqs[REF]
    print(f"{REF}\tlength={len(ref)}")
    print("accession\tlength\trefseq\tshared_Nterm_prefix_with_ref\tlast8\tlast8_in_ref")
    for acc, s in sorted(seqs.items(), key=lambda kv: len(kv[1])):
        n = 0
        while n < min(len(s), len(ref)) and s[n] == ref[n]:
            n += 1
        last8 = s[-8:]
        print(f"{acc}\t{len(s)}\t{refseq[acc]}\t{n}\t{last8}\t{last8 in ref}")
    if "A0A0B4KH49" in seqs:
        print("A0A0B4KH49 full sequence:", seqs["A0A0B4KH49"])
        print("A0A0B4K6C1 residues 1-140:", ref[:140])


if __name__ == "__main__":
    main()
