"""Check whether the annotated PA4596 (Q9HVJ0) start codon truncates the TetR HTH.

Fetches the PAO1 genomic region upstream of PA4596 (NCBI E-utilities), translates
the annotated reading frame upstream of the annotated start, reports the first
upstream in-frame stop and candidate start codons, and summarises the length
distribution of UniRef50_Q9HVJ0 members (UniProt REST). Standard library only.
Usage: python3 start_site_check.py
"""
import collections
import itertools
import json
import urllib.request

CHROM = "NC_002516.2"
GENE_START, GENE_STOP = 5149064, 5149582  # NCBI Gene 881060 (0-based 5149063-5149581), plus strand, 1-based
UPSTREAM = 300

BASES = "TCAG"
AAS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODE = {"".join(c): AAS[i] for i, c in enumerate(itertools.product(BASES, repeat=3))}


def get(url):
    with urllib.request.urlopen(url, timeout=90) as r:
        return r.read().decode()


def translate(s):
    return "".join(CODE.get(s[i:i + 3], "X") for i in range(0, len(s) - 2, 3))


def main():
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore"
           f"&id={CHROM}&seq_start={GENE_START - UPSTREAM}&seq_stop={GENE_STOP}"
           "&rettype=fasta&strand=1")
    seq = "".join(l.strip() for l in get(url).splitlines() if not l.startswith(">"))
    up, gene = seq[:UPSTREAM], seq[UPSTREAM:]
    prot = translate(gene)
    print(f"Annotated ORF translation ({len(prot.rstrip('*'))} aa): {prot[:50]}...")
    codons = [up[i:i + 3] for i in range(0, UPSTREAM, 3)]
    stops = [i for i, c in enumerate(codons) if CODE.get(c) == "*"]
    last_stop = max(stops) if stops else -1
    print(f"Upstream in-frame codons: {len(codons)}; last in-frame stop at codon index "
          f"{last_stop} (i.e. {len(codons) - last_stop - 1} sense codons before the annotated start)")
    open_up = codons[last_stop + 1:]
    print("Open upstream extension translation:", translate("".join(open_up)))
    for i, c in enumerate(open_up):
        if c in ("ATG", "GTG", "TTG"):
            print(f"  candidate start {c} giving +{len(open_up) - i} aa N-terminal extension")
    try:
        tsv = get("https://rest.uniprot.org/uniprotkb/search?query=uniref_cluster_50:"
                  "UniRef50_Q9HVJ0&fields=accession,length&size=500&format=tsv")
        lens = [int(l.split("\t")[1]) for l in tsv.splitlines()[1:] if l.strip()]
        cnt = collections.Counter(lens)
        print(f"UniRef50_Q9HVJ0 members retrieved: {len(lens)}; median length "
              f"{sorted(lens)[len(lens) // 2]}; members >= 180 aa: "
              f"{sum(1 for x in lens if x >= 180)}; members <= 175 aa: "
              f"{sum(1 for x in lens if x <= 175)}")
        print("Most common lengths:", cnt.most_common(8))
    except Exception as e:  # network failure is reported, not hidden
        print("UniRef50 query failed:", e)


if __name__ == "__main__":
    main()
